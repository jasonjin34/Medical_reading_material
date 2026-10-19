#!/usr/bin/env python3
"""Build the paper-relationship graph (deliverable #5).

Edges:
  * cites        — paper A's reference list (Semantic Scholar) contains paper B
  * same-topic   — A and B share a category
  * anchors      — every paper links to its category; categories link to the
                   central research-direction node.

Reads cached papers/<slug>/s2.json (written at ingest) for reference lists;
falls back to a live Semantic Scholar call if absent.

Outputs:
  relationships/graph.json   nodes + edges
  relationships/graph.mmd    Mermaid source
  relationships/relationships.md   narrative (from _narrative.md) + graph + edge tables
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _meta  # noqa: E402
import fetch_metadata as fm  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
REL = ROOT / "relationships"
DIRECTION = "Anomaly-detection-based virtual tissue modelling"

# Curated conceptual edges (shared method / dataset / backbone). These papers are
# mostly 2025–2026 siblings that do not cite each other, so the meaningful links
# are semantic, not bibliographic. Maintain by hand as the library grows.
# (source_slug, target_slug, label)
CONCEPT_EDGES = [
    ("virtual-tissue-2501", "spatial-biorxiv-2025", "in-silico perturbation"),
    ("spatial-biorxiv-2025", "scrna-natmachintell-2026", "perturbation/revert"),
    ("scrna-natmachintell-2026", "virtual-cell-challenge", "perturbation benchmark"),
    ("hest1k-2024", "spatial-natcommun-2024", "spatial-omics data"),
    ("hest1k-2024", "virtual-tissue-2501", "histology↔expression data"),
    ("virchow-2024", "uni2-h-model", "pathology FM"),
    ("uni2-h-model", "fm-arxiv-2604", "pathology FM"),
    ("virchow-2024", "histo-nejmai-2024", "FM backbone → anomaly det."),
    ("uni2-h-model", "spatial-natcommun-2024", "FM backbone → anomaly det."),
    ("histo-miccai-2025", "histo-sciencedirect-2026", "reconstruct-to-normal"),
    ("histo-miccai-2025", "histo-nejmai-2024", "histopath anomaly det."),
    ("histo-anomaly-bi-repo", "histo-nejmai-2024", "histopath anomaly det."),
    ("pathbench-natcommun-2026", "uni2-h-model", "pathology FM benchmark"),
    ("pathbench-natcommun-2026", "virchow-2024", "pathology FM benchmark"),
    ("pathbench-natcommun-2026", "fm-arxiv-2604", "pathology FM benchmark"),
    ("pathbench-natcommun-2026", "hest1k-2024", "linear-probe eval protocol"),
    ("deepevidence-natmachintell-2026", "semnovel-jbi-2025", "literature/evidence agents"),
    ("deepevidence-natmachintell-2026", "investorbench-arxiv-2024", "LLM agent benchmark"),
    ("deepevidence-natmachintell-2026", "biomednlp-natcommun-2025", "biomedical LLM benchmark"),
    ("biomednlp-natcommun-2025", "pathbench-natcommun-2026", "scale ≠ performance"),
    ("ehr-pancreatic-trajectory-natmed-2023", "ehr-pancreatic-llm-npjdigitmed-2025", "pancreatic-cancer EHR risk"),
    ("ehr-pancreatic-trajectory-natmed-2023", "ehr-delphi2m-nature-2025", "disease-trajectory transformer"),
    ("ehr-delphi2m-nature-2025", "ehr-apollo-arxiv-2026", "patient-trajectory foundation model"),
    ("ehr-apollo-arxiv-2026", "ehr-comet-natmachintell-2025", "EHR pretraining → transfer"),
    ("ehr-comet-natmachintell-2025", "ehr-delphi2m-nature-2025", "UK Biobank EHR modelling"),
    ("ehr-apollo-arxiv-2026", "medagentbench-nejmai-2025", "EHR environment"),
    ("resolvi-natmethods-2026", "xenium-split-natmethods-2026", "transcript-misassignment correction"),
    ("resolvi-natmethods-2026", "ovrlpy-natbiotech-2026", "segmentation-artifact correction"),
    ("xenium-split-natmethods-2026", "ovrlpy-natbiotech-2026", "Xenium contamination"),
    ("ambient-rna-bench-biorxiv-2026", "xenium-split-natmethods-2026", "wrong-cell signal contamination"),
    ("resolvi-natmethods-2026", "mrvi-natmethods-2025", "scvi-tools generative models"),
    ("ovrlpy-natbiotech-2026", "spatial-natcommun-2024", "technical vs anatomic anomaly map"),
    ("inflammatory-pt-natcommun-2025", "lake-kidney-atlas-nature-2023", "failed-repair PT state"),
    ("inflammatory-pt-natcommun-2025", "kidney-epigenome-nataging-2026", "altered PT state"),
    ("kidney-epigenome-nataging-2026", "lake-kidney-atlas-nature-2023", "kidney atlas PT states"),
    ("inflammatory-pt-natcommun-2025", "damage-scores-cellgenomics-2026", "injured kidney cell states"),
    ("abc-agentic-benchmarks-neurips-2025", "holistic-agent-leaderboard-iclr-2026", "benchmark rigor → harness"),
    ("abc-agentic-benchmarks-neurips-2025", "ailuminate-arxiv-2025", "MLCommons benchmark rigor"),
    ("mast-neurips-2025", "trail-arxiv-2025", "agent failure taxonomy"),
    ("scitrace-arxiv-2026", "trail-arxiv-2025", "trajectory-level verification"),
    ("scitrace-arxiv-2026", "ailuminate-arxiv-2025", "hazard taxonomy"),
    ("abc-agentic-benchmarks-neurips-2025", "bixbench-arxiv-2025", "benchmark-validity audit"),
    ("holistic-agent-leaderboard-iclr-2026", "clinical-agent-reruns-arxiv-2026", "rerun stability"),
    ("mast-neurips-2025", "autoresearch-failures-arxiv-2026", "agent failure taxonomy"),
    ("trail-arxiv-2025", "llm-judge-healthcare-arxiv-2026", "LLM-as-judge reliability"),
    ("healthy-ref-natgenet-2023", "refmap-eval-biorxiv-2025", "healthy reference → mapping QC"),
    ("healthy-ref-natgenet-2023", "mrvi-natmethods-2025", "cluster-free differential abundance"),
    ("healthy-ref-natgenet-2023", "lake-kidney-atlas-nature-2023", "healthy atlas reference"),
    ("refmap-eval-biorxiv-2025", "conformal-scrna-bioinformatics-2025", "reference–query shift"),
    ("conformal-scrna-bioinformatics-2025", "scatac-novel-genomeres-2026", "out-of-reference cell types"),
    ("sardine-bioinformatics-2025", "spatial-natcommun-2024", "spatial anomaly detection"),
    ("sardine-bioinformatics-2025", "meatrd-aaai-2025", "anomalous region detection"),
    ("meatrd-aaai-2025", "spatial-natcommun-2024", "H&E + ST anomalous regions"),
    ("meatrd-aaai-2025", "hest1k-2024", "paired H&E + ST"),
    ("mrvi-natmethods-2025", "scrna-natmachintell-2026", "counterfactual effect modelling"),
    ("sourcecheckup-natcommun-2025", "reference-hallucination-arxiv-2026", "citation support vs existence"),
    ("sourcecheckup-natcommun-2025", "medragchecker-arxiv-2026", "claim-level verification"),
    ("sourcecheckup-natcommun-2025", "deeptrace-arxiv-2025", "statement × source support"),
    ("deeptrace-arxiv-2025", "deep-research-hallucination-arxiv-2026", "deep-research audit"),
    ("deep-research-hallucination-arxiv-2026", "mast-neurips-2025", "agent failure taxonomy"),
    ("medragchecker-arxiv-2026", "deepevidence-natmachintell-2026", "KG evidence grounding"),
    ("medragchecker-arxiv-2026", "medical-hallucination-arxiv-2025", "medical hallucination detection"),
    ("llm-judge-healthcare-arxiv-2026", "sourcecheckup-natcommun-2025", "judge vs physician panel"),
    ("generalization-bias-rsos-2025", "medical-hallucination-arxiv-2025", "unfaithful medical text"),
    ("reference-hallucination-arxiv-2026", "citation-faithfulness-arxiv-2026", "citation reliability"),
    ("medical-hallucination-arxiv-2025", "biomednlp-natcommun-2025", "biomedical LLM benchmarking"),
    ("kidney-multimodal-genomebiol-2026", "multimodal-integration-bench-natmethods-2025", "multimodal integration benchmark"),
    ("kidney-multimodal-genomebiol-2026", "lake-kidney-atlas-nature-2023", "kidney reference atlas"),
    ("kidney-multimodal-genomebiol-2026", "nephrobase-biorxiv-2025", "kidney snRNA/snATAC"),
    ("nephrobase-biorxiv-2025", "scfm-zeroshot-genomebiol-2025", "single-cell FM evaluation"),
    ("scfm-zeroshot-genomebiol-2025", "linear-baselines-natmethods-2025", "FMs vs simple baselines"),
    ("linear-baselines-natmethods-2025", "virtual-cell-challenge", "perturbation benchmark"),
    ("nicheformer-natmethods-2025", "scfm-zeroshot-genomebiol-2025", "single-cell FM"),
    ("loki-omiclip-natmethods-2025", "hest1k-2024", "histology↔ST pairs"),
    ("loki-omiclip-natmethods-2025", "he2expr-bench-natcommun-2025", "H&E→expression"),
    ("he2expr-bench-natcommun-2025", "hest1k-2024", "H&E→expression benchmark"),
    ("multimodal-integration-bench-natmethods-2025", "scatac-novel-genomeres-2026", "RNA–ATAC cross-modal"),
    ("rq-bench-arxiv-2026", "ideation-execution-gap-arxiv-2025", "novelty judging unreliable"),
    ("rq-bench-arxiv-2026", "llm-judge-healthcare-arxiv-2026", "LLM-as-judge alignment"),
    ("rq-bench-arxiv-2026", "semnovel-jbi-2025", "novelty assessment"),
    ("falsifiable-ideation-arxiv-2026", "ideation-execution-gap-arxiv-2025", "testable ≠ successful"),
    ("truthhypo-ijcai-2025", "hypogen-llm-colm-2024", "biomedical hypothesis generation"),
    ("truthhypo-ijcai-2025", "deepevidence-natmachintell-2026", "KG + literature grounding"),
    ("scirigor-arxiv-2026", "autoresearch-failures-arxiv-2026", "unsupported claims"),
    ("scirigor-arxiv-2026", "fev-bioinformatics-agents-arxiv-2026", "workflow correctness"),
    ("scirigor-arxiv-2026", "medragchecker-arxiv-2026", "claim-to-evidence verification"),
    ("clinical-agent-reruns-arxiv-2026", "medagentbench-nejmai-2025", "reruns on MedAgentBench"),
    ("autoresearch-failures-arxiv-2026", "kosmos-arxiv-2025", "AI-scientist research"),
    ("fev-bioinformatics-agents-arxiv-2026", "biomni-biorxiv-2025", "bio agent review"),
    ("fev-bioinformatics-agents-arxiv-2026", "cellvoyager-natmethods-2026", "bio agent review"),
    ("fev-bioinformatics-agents-arxiv-2026", "spatialagent-biorxiv-2025", "bio agent review"),
    ("lab-bench-arxiv-2024", "bixbench-arxiv-2025", "FutureHouse agent benchmarks"),
    ("bixbench-arxiv-2025", "biomnibench-biorxiv-2026", "outcome vs process scoring"),
    ("bioml-bench-biorxiv-2025", "bixbench-arxiv-2025", "executable bio agent benchmarks"),
    ("biomnibench-biorxiv-2026", "biomni-biorxiv-2025", "built from Biomni traces"),
    ("lab-bench-arxiv-2024", "paperqa2-arxiv-2024", "LitQA2"),
    ("lab-bench-arxiv-2024", "deepevidence-natmachintell-2026", "LitQA2 evaluation set"),
    ("biomnibench-biorxiv-2026", "scbench-arxiv-2026", "omics-analysis agent benchmarks"),
    ("medagentbench-nejmai-2025", "llm-judge-healthcare-arxiv-2026", "healthcare LLM evaluation"),
    ("citation-blame-emnlp-2026", "citation-faithfulness-arxiv-2026", "citation faithfulness"),
    ("citation-blame-emnlp-2026", "trail-arxiv-2025", "trace-level error localization"),
    ("citation-faithfulness-arxiv-2026", "paperqa2-arxiv-2024", "audits PaperQA2 citations"),
    ("citation-faithfulness-arxiv-2026", "sourcecheckup-natcommun-2025", "citation-support auditing"),
    ("citation-faithfulness-arxiv-2026", "conformal-scrna-bioinformatics-2025", "conformal guarantees"),
    ("biomni-biorxiv-2025", "spatialagent-biorxiv-2025", "same lab lineage"),
    ("biomni-biorxiv-2025", "deepevidence-natmachintell-2026", "baseline agent"),
    ("cellvoyager-natmethods-2026", "heurekabench-arxiv-2026", "single-cell agent evaluation"),
    ("scbench-arxiv-2026", "scbench-long-arxiv-2026", "single-step → long-horizon"),
    ("scbench-long-arxiv-2026", "heurekabench-arxiv-2026", "claims reproduced before grading"),
    ("cellvoyager-natmethods-2026", "scbench-arxiv-2026", "scRNA-seq agent analysis"),
    ("spatialagent-biorxiv-2025", "xenium-split-natmethods-2026", "Xenium data"),
    ("spatialagent-biorxiv-2025", "dkd-spatial-atlas-nature-2026", "spatial niches"),
    ("paperqa2-arxiv-2024", "robin-nature-2026", "FutureHouse literature agent"),
    ("lake-kidney-atlas-nature-2023", "dkd-spatial-atlas-nature-2026", "kidney injury states → spatial niches"),
    ("lake-kidney-atlas-nature-2023", "damage-scores-cellgenomics-2026", "discrete states vs damage score"),
    ("lake-kidney-atlas-nature-2023", "cellspectra-natgenet-2025", "KPMP snRNA reference"),
    ("lake-kidney-atlas-nature-2023", "nih-kidney-ai-challenge-2026", "KPMP open data"),
    ("damage-scores-cellgenomics-2026", "cellspectra-natgenet-2025", "per-sample injury scoring"),
    ("nih-kidney-ai-challenge-2026", "histo-nejmai-2024", "WSI anomaly detection"),
    ("nih-kidney-ai-challenge-2026", "virtual-cell-challenge", "community challenge"),
    ("nih-kidney-ai-challenge-2026", "pathology-ad-bench-mlhealth-2025", "pathology AD benchmark"),
    ("counterfactual-diffusion-cancerres-2026", "histo-miccai-2025", "diffusion on histopathology"),
    ("counterfactual-diffusion-cancerres-2026", "virtual-tissue-2501", "virtual perturbation / revert"),
    ("hypogen-llm-colm-2024", "co-scientist-nature-2026", "hypothesis generation"),
    ("hypogen-llm-colm-2024", "semnovel-jbi-2025", "novelty of biomedical ideas"),
    ("dkd-spatial-atlas-nature-2026", "xenium-split-natmethods-2026", "Xenium artifacts"),
    ("pathology-ad-bench-mlhealth-2025", "medianomaly-media-2025", "anomaly-detection benchmarks"),
    ("pathology-ad-bench-mlhealth-2025", "histo-anomaly-bi-repo", "histology AD methods"),
    ("pathology-ad-bench-mlhealth-2025", "histo-nejmai-2024", "histopathology AD"),
    ("medianomaly-media-2025", "histo-miccai-2025", "diffusion-based AD"),
    ("kidney-ssl-histology-scirep-2025", "uni2-h-model", "UNI embeddings comparison"),
    ("kidney-ssl-histology-scirep-2025", "lake-kidney-atlas-nature-2023", "histology vs molecular atlas"),
    ("co-scientist-nature-2026", "robin-nature-2026", "AI scientists"),
    ("co-scientist-nature-2026", "virtual-lab-nature-2025", "multi-agent research"),
    ("robin-nature-2026", "kosmos-arxiv-2025", "FutureHouse lineage"),
    ("robin-nature-2026", "bixbench-arxiv-2025", "Finch on BixBench"),
    ("kosmos-arxiv-2025", "cellvoyager-natmethods-2026", "autonomous omics analysis"),
    ("virtual-lab-nature-2025", "biomni-biorxiv-2025", "multi-agent biomedical systems"),
    # general anomaly detection ↔ biomedical AD: shared idea, no citation (citations go to maps/matrix.yaml transfers)
    ("anogan-ipmi-2017", "spatial-natcommun-2024", "GAN on normal data; reconstruction-residual score"),
    ("diffusion-medical-ad-miccai-2022", "histo-miccai-2025", "diffusion reconstruct-to-normal AD"),
    ("diffusion-medical-ad-miccai-2022", "counterfactual-diffusion-cancerres-2026", "diffusion counterfactuals"),
    ("patchcore-cvpr-2022", "histo-nejmai-2024", "pretrained features + kNN distance"),
    ("patchcore-cvpr-2022", "spatial-natcommun-2024", "memory bank of normal features"),
    ("deep-svdd-icml-2018", "histo-anomaly-bi-repo", "one-class boundary on learned features"),
    ("cflow-ad-wacv-2022", "sardine-bioinformatics-2025", "density-based anomaly scoring"),
    ("mahalanobis-ood-neurips-2018", "refmap-eval-biorxiv-2025", "distance to a reference distribution"),
    ("conformal-outliers-annstat-2023", "refmap-eval-biorxiv-2025", "healthy reference as the null"),
    ("energy-ood-neurips-2020", "histo-nejmai-2024", "outlier-exposure training"),
    ("draem-iccv-2021", "medianomaly-media-2025", "synthetic-anomaly family"),
    ("ad-unifying-review-procieee-2021", "medianomaly-media-2025", "multi-paradigm AD taxonomy"),
    ("imaging-nature-2026", "imaging-ehjdh-2026", "medical-imaging biomarker"),
    ("pathomics-repo", "pathomics-npjpo-2026", "pathomics survival"),
    ("pathomics-npjpo-2026", "pathomics-blood-2023", "pathomics"),
]


def _norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (t or "").lower())


def load_refs(m: dict) -> list[dict]:
    cache = _meta.PAPERS / m["_dir"] / "s2.json"
    if cache.exists():
        try:
            return json.loads(cache.read_text()).get("references") or []
        except Exception:
            pass
    if m.get("doi") or m.get("arxiv"):
        s2 = fm.fetch_s2(m.get("doi", ""), m.get("arxiv", ""))
        refs = s2.get("references") or []
        if refs:  # cache for reproducibility / offline rebuilds
            try:
                cache.write_text(json.dumps({"references": refs}), encoding="utf-8")
            except Exception:
                pass
        return refs or []
    return []


def main() -> None:
    metas = _meta.all_meta()
    REL.mkdir(exist_ok=True)

    by_doi, by_arxiv, by_title = {}, {}, {}
    for m in metas:
        if m.get("doi"):
            by_doi[str(m["doi"]).lower()] = m["id"]
        if m.get("arxiv"):
            by_arxiv[str(m["arxiv"])] = m["id"]
        if m.get("title"):
            by_title[_norm_title(m["title"])] = m["id"]

    cite_edges = []
    for m in metas:
        for ref in load_refs(m):
            ext = ref.get("externalIds") or {}
            tgt = (
                by_doi.get(str(ext.get("DOI", "")).lower())
                or by_arxiv.get(str(ext.get("ArXiv", "")))
                or by_title.get(_norm_title(ref.get("title", "")))
            )
            if tgt and tgt != m["id"]:
                cite_edges.append({"source": m["id"], "target": tgt, "type": "cites"})

    # nodes
    nodes = [{"id": "DIRECTION", "label": DIRECTION, "kind": "direction"}]
    cats = sorted({m.get("category", "other") for m in metas})
    nodes += [{"id": f"cat:{c}", "label": c, "kind": "category"} for c in cats]
    nodes += [
        {
            "id": m["id"],
            "label": (m.get("title") or m["id"])[:60],
            "kind": "paper",
            "category": m.get("category", "other"),
            "relevance": m.get("relevance", "medium"),
            "year": m.get("year"),
        }
        for m in metas
    ]

    ids = {m["id"] for m in metas}
    concept_edges = [
        {"source": s, "target": t, "type": "concept", "label": lbl}
        for (s, t, lbl) in CONCEPT_EDGES if s in ids and t in ids
    ]

    anchor_edges = [{"source": f"cat:{c}", "target": "DIRECTION", "type": "anchor"} for c in cats]
    anchor_edges += [
        {"source": m["id"], "target": f'cat:{m.get("category","other")}', "type": "in-category"}
        for m in metas
    ]

    graph = {"nodes": nodes, "edges": cite_edges + concept_edges + anchor_edges, "direction": DIRECTION}
    (REL / "graph.json").write_text(json.dumps(graph, indent=2, ensure_ascii=False), encoding="utf-8")

    mmd = _mermaid(metas, cats, cite_edges, concept_edges)
    (REL / "graph.mmd").write_text(mmd, encoding="utf-8")

    _write_md(metas, cite_edges, concept_edges, mmd)
    print(f"✓ relationships: {len(nodes)} nodes, {len(cite_edges)} citation edges, "
          f"{len(concept_edges)} concept edges + {len(anchor_edges)} anchors")


def _safe(nid: str) -> str:
    return re.sub(r"[^A-Za-z0-9_]", "_", nid)


def _mermaid(metas, cats, cite_edges, concept_edges) -> str:
    lines = ["flowchart LR", f'  DIRECTION(["{DIRECTION}"])']
    for c in cats:
        lines.append(f'  cat_{_safe(c)}["{c}"] --> DIRECTION')
    for m in metas:
        star = "★" if m.get("relevance") == "high" else ""
        label = (m.get("title") or m["id"])[:40].replace('"', "'")
        lines.append(f'  {_safe(m["id"])}["{star}{label}"] --> cat_{_safe(m.get("category","other"))}')
    for e in cite_edges:
        lines.append(f'  {_safe(e["source"])} -.->|cites| {_safe(e["target"])}')
    for e in concept_edges:
        lines.append(f'  {_safe(e["source"])} ==>|{e["label"]}| {_safe(e["target"])}')
    return "\n".join(lines) + "\n"


def _write_md(metas, cite_edges, concept_edges, mmd) -> None:
    narrative = ""
    nfile = REL / "_narrative.md"
    if nfile.exists():
        narrative = nfile.read_text(encoding="utf-8").strip() + "\n\n"
    id2title = {m["id"]: (m.get("title") or m["id"]) for m in metas}

    crows = "\n".join(
        f"| `{e['source']}` | cites | `{e['target']}` |" for e in cite_edges
    ) or "| _(none detected — this set is parallel 2025–26 work, no intra-set citations)_ | | |"
    krows = "\n".join(
        f"| `{e['source']}` | {e['label']} | `{e['target']}` |" for e in concept_edges
    ) or "| _(none)_ | | |"

    md = (
        "# 论文关系 / Paper relationships\n\n"
        f"> Auto-generated by `scripts/build_relationships.py`. Central node: **{DIRECTION}**.\n"
        "> Solid `==>` edges are curated conceptual links (shared method/data/backbone); "
        "dotted `-.->` edges are bibliographic citations within the set.\n\n"
        + narrative
        + "## 关系图 / Graph\n\n```mermaid\n" + mmd + "```\n\n"
        + "## 概念边 / Concept edges (shared method · dataset · backbone)\n\n"
        + "| From | link | To |\n|---|---|---|\n" + krows + "\n\n"
        + "## 引用边 / Citation edges (within this set)\n\n"
        + "| From | | To |\n|---|---|---|\n" + crows + "\n\n"
        + "## 按类别 / By category\n\n"
    )
    from collections import defaultdict
    bycat = defaultdict(list)
    for m in metas:
        bycat[m.get("category", "other")].append(m)
    for c in sorted(bycat):
        md += f"### {c}\n"
        for m in sorted(bycat[c], key=lambda x: -(x.get("relevance") == "high")):
            star = " ★" if m.get("relevance") == "high" else ""
            md += f"- [`{m['id']}`](../papers/{m['_dir']}/deep-read.md) — {id2title[m['id']]}{star}\n"
        md += "\n"
    (REL / "relationships.md").write_text(md, encoding="utf-8")


if __name__ == "__main__":
    main()

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

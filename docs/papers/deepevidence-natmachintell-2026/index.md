# Empowering biomedical evidence exploration and synthesis with deep knowledge graph research

> **Bibkey** `Wang_2026b` · **Venue** Nature Machine Intelligence (2026) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1038/s42256-026-01266-0> · `status: complete`

---

## One-liner
DeepEvidence is a biomedical deep-research agent: an orchestrator plus specialized subagents coordinate breadth-first (BFRS) and depth-first (DFRS) research strategies to explore heterogeneous knowledge bases and literature over long horizons, while **incrementally constructing an evidence graph** of entities, relations and provenance that makes the research process trackable, attributable and verifiable. It outperforms generic agents across four public benchmarks and seven newly built tasks.

## Problem
Biomedical evidence is scattered across structurally divergent, continuously evolving resources — PubTator/PKG (literature-derived knowledge), KEGG/Gene Ontology (pathways and function), OpenTargets (gene–disease), BioThings, ChEMBL, OpenFDA, ClinicalTrials.gov — with poor interoperability, making cross-resource reasoning hard in practice. Generic deep-research systems (OpenAI DeepResearch, Gemini, Perplexity) operate mainly over unstructured web text and fit poorly; existing biomedical agents (Biomni, ToolUniverse) wire in many knowledge-base APIs but **explore shallowly** — a few searches before answering — while their large tool suites induce tool confusion, wrong tool picks and wrong reasoning paths.

## Method
**Architecture**: an orchestrator agent maintains the research plan and an internal evidence graph, dispatching to two kinds of research subagent — **BFRS** issues multigraph queries to sweep first-hop neighbourhoods fast (e.g. drugs linked to a disease across disease–drug and gene–disease graphs); **DFRS** takes the key entities BFRS surfaces and goes multihop deep (e.g. recursively tracing references to build the evidence graph for a systematic review). The authors deliberately avoid the names BFS/DFS: agents choose traversal steps autonomously rather than following fixed graph-theoretic rules, and can bridge heterogeneous graphs by recognizing shared entities or inferring cross-graph relations (**bridge entities**). **Environment**: unified entity-search and data-fetch interfaces over heterogeneous web APIs — one drug query fans out to KEGG, ChEMBL, OpenFDA, OpenTargets in parallel — plus an **execution sandbox** where agents write code to query APIs at scale, persist structured files and run downstream extraction. **Key design**: the continually updated evidence graph preserves provenance, enabling transparent reasoning and human validation. The authors stress this is **not GraphRAG**, and not traversal over a pre-unified knowledge graph — because the underlying sources are fragmented, heterogeneous and constantly evolving.

## Data
Two evaluation layers. **Four public benchmarks**: HLE-Medicine (the medical slice of Humanity's Last Exam), LabBench-LitQA2 (retrieval and synthesis of publication evidence), SuperGPQA-Medicine-Hard (hard mechanistic reasoning) and TrialPanorama-EvidenceQA (evidence reasoning grounded in real clinical trials). **Seven purpose-built tasks** spanning four stages of the discovery lifecycle — drug discovery, preclinical in vivo experimentation, clinical trial development and evidence-based medicine (EBM). Knowledge sources include PubMed, ClinicalTrials.gov, KEGG, Gene Ontology, OpenTargets, ChEMBL, OpenFDA, BioThings and PubTator. Test sets are public on HuggingFace.

## Key results
The fairness setup matters: **all agent systems including DeepEvidence run on the same underlying LLM (GPT-5)**, with baselines being GPT-5 and Sonnet-4.5 equipped with literature search, plus the biomedical agents Biomni and ToolUniverse. It leads on all four public benchmarks: **HLE-Medicine 40.0%** (Biomni 20.0%, ToolUniverse 10.0%, Sonnet-4.5 3.3%, GPT-5 3.3%); **LabBench-LitQA2 64.7%** (Biomni 48.9%, ToolUniverse 25.0%); **SuperGPQA-Medicine-Hard 47.1%** (Biomni 40.7%, Sonnet-4.5 43.6%); **TrialPanorama-EvidenceQA 96.0%** (Biomni 84.0%, Sonnet-4.5 88.0%). The built tasks show the same pattern — e.g. 68% (Biomni 56%, ToolUniverse 40%), 72% (both 44%), 80% (Biomni 68%), 52% (Biomni 36%) — winning five to six of eight evaluation dimensions against Biomni. The authors attribute this not to tool availability but to baselines' **shallow exploration plus tool confusion**, whereas evidence-graph-guided BFRS–DFRS performs structured, targeted deep investigation — exactly what multihop reasoning and evidence synthesis demand.

## Contributions
- Brings the deep-research paradigm to heterogeneous biomedical knowledge sources rather than generic web text.
- Dual BFRS/DFRS orchestration: sweep first-hop neighbourhoods, then go multihop deep on key entities, with traversal chosen autonomously.
- **An explicit evidence graph as agent memory**: entities, relations and provenance preserved so the process is trackable, attributable and expert-verifiable — the most transferable idea here.
- An execution sandbox lets agents query APIs at scale programmatically and persist structured results for analysis.
- Seven new benchmark tasks covering the full discovery lifecycle (drug discovery → preclinical → trial design → EBM).

## Limitations
- Knowledge-source coverage remains incomplete; current benchmarks reflect only a subset of biomedical research tasks.
- Currently relies on **well-curated** bases like KEGG and Gene Ontology with stable schemas and good APIs; proprietary or in-house sources (missing values, inconsistent structure, incomplete interfaces) would require the agent to build new tools.
- **No explicit probabilistic modelling or uncertainty-aware mechanism to reconcile conflicting evidence** — it leans on the base LLM's parametric reasoning to weigh sources; the authors flag calibrated confidence and probabilistic frameworks as future work.
- Only two strategies (BFRS/DFRS), which the authors concede are unlikely optimal; ideally agents would discover better strategies through self-directed adaptation.
- Not yet expert-level; and **text-only** — imaging, structural biology and proteomic modalities are out of scope.

## Relation to our direction
This sits on the **evidence layer above** the detect → model → revert chain: when the pipeline nominates "which genes/perturbations would revert the anomaly," that nomination must carry a checkable evidence chain or it cannot enter wet-lab prioritization. DeepEvidence is the engineering form of that chain — an evidence graph holding entities, relations and provenance so every step is attributable and expert-verifiable. Three reusable pieces: **(1) the evidence graph as a concrete auditable-memory implementation**, directly borrowable for provenance tracking behind target nomination; **(2) the BFRS/DFRS division of labour**, matching the real workflow of "sweep first-hop associations for candidate genes, then dig deep into literature and trial evidence for the shortlist"; **(3) the same-base-LLM controlled comparison** (every system on GPT-5), the experimental discipline to copy when evaluating agents — otherwise one cannot tell agent design from base-model strength. **Most valuable is the gap it names itself**: no uncertainty modelling to reconcile conflicting evidence, and text-only. This direction happens to hold both missing pieces — a notion of data-level reliability (how trustworthy is the data an item of evidence rests on) and the imaging / spatial-omics modalities. Closing the chain "data confidence → evidence confidence → conclusion confidence" is precisely the interface it leaves open.

## Reusable assets
- **Code:** the DeepEvidence implementation (inside the BioDSA repo).
<https://github.com/RyanWangZf/BioDSA/tree/main/biodsa/agents/deepevidence>
- **Data:** the test datasets used in the experiments are public.
<https://huggingface.co/datasets/zifeng-ai/DeepEvidence>
- **Eval protocol:** four public benchmarks (HLE-Medicine, LabBench-LitQA2, SuperGPQA-Medicine-Hard, TrialPanorama-EvidenceQA) plus seven built tasks; crucially, **all compared systems share one base LLM**.
- **Baseline systems:** Biomni and ToolUniverse — the standard comparators for biomedical agents.

## Follow-ups
- The Biomni and ToolUniverse papers (no entries in this repo yet) — the default baselines on this line.
- How TrialPanorama and LabBench construct their tasks — how evidence-style benchmarks are authored and grounded.
- Track the "calibrated confidence / probabilistic reasoning" future work it flags, and whether follow-ups already exist.

## Cite
```bibtex
@article{Wang_2026b, title={Empowering biomedical evidence exploration and synthesis with deep knowledge graph research}, volume={8}, ISSN={2522-5839}, url={http://dx.doi.org/10.1038/s42256-026-01266-0}, DOI={10.1038/s42256-026-01266-0}, number={7}, journal={Nature Machine Intelligence}, publisher={Springer Science and Business Media LLC}, author={Wang, Zifeng and Chen, Zheng and Yang, Ziwei and Wang, Xuan and Jin, Qiao and Peng, Yifan and Lu, Zhiyong and Sun, Jimeng}, year={2026}, month=July, pages={1142–1156} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

# SpatialAgent: An autonomous AI agent for spatial biology

> **Bibkey** `Wang2025_SpatialAgent` · **Venue** bioRxiv (2025) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1101/2025.04.03.646459> · `status: complete`

---

## One-liner
SpatialAgent is the Genentech/Regev-lab agent specialised for spatial omics: a Plan-Act-Conclude architecture with dynamic retrieval over 72 tools / 17 reusable skills, image interpretation, and **reporting and verification subagents that audit numerical and visual claims**, covering gene-panel design, cell/niche annotation, trajectories, cell–cell communication, imputation and hypothesis generation. It beats established methods and matches or exceeds experts on DLPFC panel design and fetal-heart MERFISH annotation, and designed a 100-gene add-on panel used in a prospective mouse prostate-cancer Xenium study (4.2M cells, 21 samples).

## Problem
Spatial-omics analysis is fragmented and expert-bound: reasoning spans molecules, cells and multicellular interactions and must integrate histology/anatomical images, so fixed pipelines generalise poorly to new tissues, platforms and questions. The authors want an agent that goes from experimental design (panel selection) through annotation to hypothesis generation, autonomously or as a co-pilot, and they explicitly aim to separate "successful execution" from "reliable scientific reasoning."

## Method
**Architecture**: a LangGraph state machine for Plan (retrieve skills/tools, decompose, update plan on observations) → Act (run code, database/literature search, specialised tools in a persistent Python environment) → Conclude (synthesise an answer/report, optionally calling reporting and verification subagents). Sessions are capped at 50 steps; execution errors return as observations. **Tools and skills**: 72 registered tools with typed signatures and failure-mode metadata across 13 categories (data access, spatial statistics, mapping, domain detection, deconvolution, trajectories, multimodal integration, CCC, …), with 5–20 retrieved per query; 17 skills encode common multi-step procedures (panel design, spatial domains, condition-aware CCC, trajectories) as structured guidance rather than fixed scripts. **Auditability**: every action is logged as JSONL (code, tool calls, outputs, errors, artifact pointers); new figures are auto-interpreted by a vision model and fed back as observations. **Verification subagent**: checks numerical claims against saved outputs and re-inspects figures for visual claims, returning claim-level assessments and fixes. **Backends**: pluggable (Claude/GPT/Gemini and local Qwen, Ministral); after backend/temperature/skill ablations the default is Claude Sonnet 4.5 at T=0.5.

## Data
Benchmarks: human DLPFC Visium (12 sections from 3 donors) for panel design; developing human heart scRNA-seq + MERFISH (6 samples, 9–16 PCW; 142,946 scRNA profiles and >1.5M MERFISH cells) for cell and niche annotation. Open cases: in-house healthy human tonsil CosMx (neighbourhoods, B-cell differentiation trajectories, Tangram imputation); DSS mouse colitis MERFISH (healthy / DSS3 / DSS9 / DSS21, multi-turn co-pilot). Wet lab: mouse prostate-cancer Xenium 5k Pan-Tissue + a 100-gene add-on panel, 4.2M cells across 21 samples (wild type, adenocarcinoma, metastasis), plus a post-treatment cohort (anti-gp120, JAK inhibitor, anti-PD1, combination). Human comparators: 10 scientists for panels (50/100/150 genes), 8 for annotation, all barred from using LLMs.

## Key results
**Panel design (DLPFC)**: vs. HVG/GeneBasis/PERSIST/Spapros, cell-type prediction accuracy improves **15.9–45.2%** and spatial-coordinate R² by up to **178.1%**; across 30 matched human comparisons it wins 26/30 (accuracy) and 29/30 (y-coordinate R²); agent refinement of human panels improves 27/30 and 29/30; agent-refined human panels beat the agent's own from-scratch design in 10/30 and 16/30 — complementary strengths. Runtime ~**12.2 min at ~$1.8 per run** vs. Spapros 3.8 h/$123.2 and a median human 4.0 h/$212.8. **Cell annotation (heart MERFISH)**: overall accuracy **0.853** vs. PopV 0.262, scTab 0.157, **Biomni 0.394**, GPTCellType 0.811; GPTCellType calls 98.1% of epicardial, 85.5% of immune and 96.9% of neuronal cells fibroblasts; SpatialAgent still labels epicardial cells mostly as fibroblasts (82.2%, only 14.5% correct); 8 human experts span 0.459–0.834. **Niche annotation**: accuracy **0.661** vs. humans 0.108–0.873; errors concentrate in thin structures (conduction system, outflow tracts, valves — the best expert gets conduction system right only 37.8%). **Tonsil**: the verification subagent caught the main agent misreading the "LQ" (low-quality) label as a follicular subzone, a correlation analysis run on only a subset of fields of view, and only weak-to-moderate correlations; Tangram imputation held-out reconstruction cosine ≈0.5 per cell and ≈0.3 per gene. **Colitis**: recovers the original study's main findings and proposes seven neighbourhood trajectories (incl. FOL2→FOL1→FOL3 follicle maturation) and stage-specific therapeutic hypotheses (unvalidated). **Prospective Xenium**: the 100-gene add-on reaches **0.896** cell-type/malignant-state accuracy (random 100 genes 0.516, 5k panel 0.929, all 5.1k genes 0.950); add-on genes have higher Moran's I; treatment-condition prediction 0.459 (random 0.371, 5k 0.581, all 0.592).

## Contributions
- The first spatial-omics-specialised agent spanning design → annotation → hypothesis, with a **prospective wet-lab** test (the agent-designed panel was actually run).
- **Reporting and verification subagents** that check each main-agent claim against saved outputs/figures — one of the closest engineering realisations of claim-to-evidence checking in this repo, and it caught real errors in the tonsil case.
- A skill library as a "reliability layer": ablations show the largest gains in annotation, reducing label collapse, incomplete workflows and rare-class loss.
- Systematic backend/temperature/skill ablations with cost-latency tracking; per-gene rationales with provenance.

## Limitations
- Self-reported: performance depends on curated skills/tools; ad hoc LLM planning and code generation are brittle for specialised analyses; agents can produce plausible outputs that hide methodological failures (benchmark choice, leakage, metric misuse, post-hoc selection).
- The verification subagent is qualitative — **no calibrated confidence or measured verifier accuracy**; it was not invoked in the multi-turn colitis case.
- Benchmarks treat author labels as ground truth and are mostly single-dataset/single-tissue; new hypotheses in open cases (TLS maturation, targets) are unvalidated; most authors are Genentech employees and the prostate data are in-house.
- Tissue-specific states such as epicardial cells remain hard — LLM components default to common labels rather than dataset-specific context.

## Relation to our direction
This is the paper in this batch **closest to both thesis plans**. **Topic 1 (kidney omics anomaly detection)**: its data shape (MERFISH/CosMx/Xenium + scRNA reference + anatomical images) is isomorphic to a multi-modal design of this kind (snRNA + snATAC + Xenium + H&E), and its reported failures are exactly what anomaly detection must face: **rare/tissue-specific states absorbed into common classes** (82.2% of epicardial cells called fibroblasts) and thin anatomical structures (conduction system) being hardest — in kidney, rare injury states (failed-repair PT, inflammatory PT) and small structures (glomeruli, JGA). Anomaly scores built on agent or reference-mapping labels would systematically under-detect true lesions; and "a low-quality-cell label misread as a biological subzone" is precisely the counter-example Topic 1 addresses by using cross-modal agreement (snRNA vs. Xenium vs. H&E) to separate **artifact from disease**. Its Xenium add-on panel design is directly reusable: a custom add-on for kidney injury/repair states, i.e. "designing the measurement to validate the anomaly" within detect → revert. **Topic 2 (trustworthy agents)**: the verification subagent is a direct precursor of our calibrated verifier — it shows that re-reading outputs and figures to audit claims one by one is feasible and useful, but stays qualitative; Topic 2's increment is to quantify it (claim-level precision/recall, calibration, rerun stability) and to file the failures seen in the tonsil case (misreading a QC label, reporting on a subset as if global, overstating correlation strength, treating imputation as quantitative) into the omics-specific failure taxonomy. Its JSONL execution logs are a template for the trace format our auditing needs.

## Reusable assets
- **Code:** SpatialAgent implementation, tutorial notebooks and hypothesis-generation agent traces.
<https://github.com/Genentech/SpatialAgent>
- **Data:** human-scientist and baseline outputs for panel design and annotation.
<https://huggingface.co/datasets/hansen7/spatialagent_human>
- **Eval protocol:** panel evaluation (logistic-regression cell type + Lasso coordinate regression, 80/20 × 10), annotation metrics (accuracy/precision/F1/ARI), and the three-axis add-on panel evaluation (discriminative power, Moran's I spatial structure, treatment prediction).

## Follow-ups
- Supplementary 1.5 (reporting/verification subagent prompts and output format) — to compare against the Topic 2 verifier design.
- v1 vs. v2 differences (GPT-4o → Sonnet 4.5) as a case of whether conclusions survive a backbone swap.
- Ref. 39 (agents hiding methodological failures) and the AI-scientist evaluation work the authors cite.

## Cite
```bibtex
@article{Wang2025_SpatialAgent, title={SpatialAgent: An autonomous AI agent for spatial biology}, url={http://dx.doi.org/10.1101/2025.04.03.646459}, DOI={10.1101/2025.04.03.646459}, journal={bioRxiv}, publisher={openRxiv}, note={Version 2 posted 2026-08-12}, author={Wang, Hanchen and He, Yichun and Coelho, Paula P. and Bucci, Matthew and Nazir, Abbas and Chen, Bob and Trinh, Linh T. and Zhang, Serena and Lu, Ziyu and Huang, Kexin and Chandrasekar, Vineethkrishna and Chung, Douglas C. and Hao, Minsheng and Leote, Ana Carolina and Lee, Yongju and Li, Bo and Liu, Tianyu and Liu, Jin and Lopez, Romain and Tawaun, Lucas and Ma, Mingyu and Makarov, Nikita and McGinnis, Lisa and Peng, Linna and Ra, Stephen and Scalia, Gabriele and Singh, Avtar and Tao, Liming and Uehara, Masatoshi and Wang, Chenyu and Wei, Runmin and Copping, Ryan and Rozenblatt-Rosen, Orit and Leskovec, Jure and Regev, Aviv}, year={2025}, month=Apr }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

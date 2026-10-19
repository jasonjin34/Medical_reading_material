<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# BioML-bench: Evaluation of AI Agents for End-to-End Biomedical ML

- **Authors:** Miller, Henry E.; Greenig, Matthew; Tenmann, Benjamin; Wang, Bo
- **Affiliations:** Shift Bioscience; University of Cambridge / ScienceMachine; ScienceMachine; University of Toronto / Vector Institute
- **Venue / Year:** bioRxiv (preprint, CC-BY 4.0) · 2025 (v3 posted 2025-09-28)
- **DOI:** 10.1101/2025.09.01.673319
- **URL:** https://doi.org/10.1101/2025.09.01.673319
- **Bibkey:** Miller_2025
- **Status:** complete (extract from bioRxiv v3 full text)

## Abstract
Large language model (LLM) agents hold promise for accelerating biomedical research and development (R&D). Several biomedical agents have recently been proposed, but their evaluation has largely been restricted to question answering (e.g., LAB-Bench) or narrow bioinformatics tasks. Presently, there remains a lack of benchmarks evaluating agent capability in multi-step data analysis workflows or in solving the machine learning (ML) challenges central to AI-driven therapeutics development, such as perturbation response modeling or drug toxicity prediction. We introduce BioML-bench, the first benchmarking suite for evaluating AI agents on end-to-end biomedical ML tasks. BioML-bench spans four domains (protein engineering, single-cell omics, biomedical imaging, and drug discovery) with tasks that require agents to parse a task description, build a pipeline, implement models, and submit predictions graded by established metrics (e.g., AUROC, Spearman). We evaluate four open-source agents: two biomedical specialists (STELLA, Biomni) and two generalists (AIDE, MLAgentBench). On average, agents underperform relative to human baselines, and biomedical specialization does not confer a consistent advantage. We also found that agents which employed more diverse ML strategies more often tended to score highest, suggesting that architecture and scaffolding may be stronger determinants of performance. These findings underscore both the potential and current limits of agentic systems for biomedical ML, and highlight the need for systematic, reproducible evaluations. BioML-bench is provided open-source at github.com/science-machine/biomlbench.

## Full text / Extract

### Setup
Adapted from MLE-bench, with support for multiple biomedical domains, new agents, tasks and metrics, bioinformatics file formats (e.g. h5ad), cloud deployment and mkdocs documentation. Task capsules provide a structured task description, training data, test features and a sample submission. Agents run in Docker with a pre-built conda environment; submissions are automatically validated and scored against held-out ground truth.

### Task suite (24 tasks)
- **Drug discovery (PolarisHub / TDC):** EGFR WT kinase inhibitor classification; human liver microsomal intrinsic clearance; plasma protein binding (fraction unbound); solubility; CYP2D6 substrate; lipophilicity; hERG blockers; BBB penetration (Martins); Caco-2 permeability (Wang).
- **Biomedical imaging (Kaggle):** OSIC pulmonary fibrosis (FVC decline from CT + clinical); histopathologic cancer detection (PatchCamelyon 32×32 patches); RSNA brain tumour MGMT promoter methylation from mpMRI; UW GI-tract segmentation.
- **Protein engineering (ProteinGym):** SPIKE_SARS2_Starr_2020; SPA_STAAU_Tsuboyama_2023; PSAE_PICP2 indels; CBX4_HUMAN multi-substitution; Q8EG35_SHEON indels; CSN4_MOUSE indels.
- **Single-cell omics (OpenProblems):** modality prediction (protein from RNA, CITE-seq); perturbation response (PBMC small molecules); label projection across diabetic kidney disease datasets; spatially variable genes (mouse cortex Slide-seqV2); cell–cell communication (breast cancer scRNA-seq).

### Agents
Biomni v0.0.5 (Claude Sonnet 4), STELLA (OpenRouter default), AIDE v6.3.3 (GPT-4.1), MLAgentBench (GPT-4.1), and a Dummy agent (random or zero predictions).

### Protocol
Four independent replicates per agent–task. Metrics: leaderboard percentile (failed runs = 0 when penalized, omitted when non-penalized); mean rank across agents; above-median (%); any-medal (%) (MLE-bench definition); completion rate (%). Imaging: one NVIDIA L4 GPU, 16 vCPUs, 64 GB RAM, 16 h limit; other tasks CPU-only, 8 h limit.

### Overall results (Table 2)
| Setting | Agent | Leaderboard pct. | Mean rank | Above median % | Any medal % | Completion % |
|---|---|---|---|---|---|---|
| Penalized | Dummy | 2.50 ± 1.16 | 4.33 ± 0.21 | 0.0 | 0.0 | 100.0 |
| Penalized | MLAgentBench | 21.43 ± 4.40 | 3.06 ± 0.24 | 16.7 ± 5.6 | 6.2 ± 3.4 | 97.9 |
| Penalized | AIDE | 28.50 ± 5.22 | 2.56 ± 0.23 | 28.1 ± 6.4 | 12.5 ± 5.2 | 80.2 |
| Penalized | STELLA | 31.84 ± 5.82 | 2.62 ± 0.24 | 34.4 ± 7.6 | 17.7 ± 6.1 | 91.7 |
| Penalized | Biomni | 34.45 ± 5.36 | 1.88 ± 0.18 | 32.3 ± 8.0 | 19.8 ± 6.7 | 100.0 |
| Non-penalized | Dummy | 2.50 ± 1.16 | 4.38 ± 0.20 | 0.0 | 0.0 | – |
| Non-penalized | MLAgentBench | 23.44 ± 4.65 | 3.07 ± 0.19 | 18.5 ± 5.9 | 7.6 ± 4.0 | – |
| Non-penalized | AIDE | 37.41 ± 5.85 | 2.20 ± 0.21 | 36.2 ± 7.9 | 14.5 ± 6.0 | – |
| Non-penalized | STELLA | 39.45 ± 6.52 | 2.45 ± 0.21 | 42.8 ± 8.7 | 20.8 ± 7.1 | – |
| Non-penalized | Biomni | 34.45 ± 5.36 | 2.08 ± 0.22 | 32.3 ± 8.0 | 19.8 ± 6.7 | – |

Differences between AIDE, STELLA and Biomni are generally within SEM.

### Domain results (penalized leaderboard percentile, Table 4)
- Biomedical imaging: MLAgentBench 21.73, Biomni 19.04, AIDE 12.11, STELLA 5.91.
- Drug discovery: Biomni 32.55, STELLA 28.84, AIDE 24.75, MLAgentBench 22.45.
- Protein engineering: STELLA 34.98, Biomni 29.93, AIDE 24.50, MLAgentBench 13.52 (Biomni best mean rank 2.00).
- Single-cell omics: Biomni 55.62, STELLA 54.23, AIDE 53.17, MLAgentBench 28.83.
- Non-penalized: STELLA leads imaging (44.32), AIDE leads protein engineering (35.99), Biomni leads drug discovery (32.55); single-cell STELLA 61.97, AIDE 60.67.

### Strategies and failures
- 94 above-median runs: strongest agents (AIDE, STELLA, Biomni) used a wider variety of strategies (feature engineering, model types) more often. AIDE reached the 100th percentile on Tsuboyama 2023 (BLOSUM scores, conservation indices, amino-acid charge, volume, H-bond propensity), but another replicate on the same task reached only the 54th percentile with less extensive feature engineering.
- Architectures: Biomni and MLAgentBench used random forests in ~50% of cases; STELLA alternated random forests, ridge, XGBoost; AIDE often stacked or gradient-boosting models (e.g. LightGBM). Deep learning was rarely attempted and almost never the final model, even on image tasks, unlike DL-dominated human leaderboards.
- 41 failed runs: AIDE resource exhaustion (copying large image files); MLAgentBench and STELLA early exits without outputs (silent errors from try–except fallbacks; stalls on unnecessary environment creation); uncaught framework exceptions (AIDE, STELLA); time-limit overruns. Authors consider these addressable scaffolding issues.

### Limitations (authors)
LLM choice confounds agent comparisons (each agent paired with its default/recommended LLM); public leaderboards are an imperfect human reference; future comparators include H2O AutoML and Lazy Predict; better DL support, tool use, memory/self-evolving and multi-agent designs to be explored.

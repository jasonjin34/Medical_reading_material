# BioML-bench: Evaluation of AI Agents for End-to-End Biomedical ML

> **Bibkey** `Miller_2025` · **Venue** bioRxiv (2025) · **Category** agents · **Relevance** medium · **Access** open
> **Link** <https://doi.org/10.1101/2025.09.01.673319> · `status: complete`

---

## One-liner
BioML-bench ports MLE-bench's "task capsule + automatic grading" paradigm to biomedicine: 24 end-to-end ML tasks (drug discovery, biomedical imaging, protein engineering, single-cell) where the agent builds the pipeline, trains models and submits predictions, scored as percentiles on **largely expert-populated public leaderboards**. Four agents (Biomni, STELLA, AIDE, MLAgentBench) average only the **34th–39th percentile**, and **biomedical specialization confers no consistent advantage**.

## Problem
Biomedical agents have mostly been evaluated on QA (e.g. LAB-Bench) or narrow bioinformatics; no benchmark tests whether agents can complete the **supervised ML challenges** central to therapeutics (perturbation response, toxicity prediction) end to end. MLE-bench showed executable end-to-end evaluation is feasible, but its Kaggle leaderboards are crowd-sourced rather than expert-populated; BixBench is mainly text answers without supervised learning.

## Method
Adapted from MLE-bench, adding biomedical domains, new agents and metrics, bioinformatics formats such as h5ad, cloud deployment configs and mkdocs documentation. Each task capsule gives a structured description, training data, test features and a sample submission; agents run in Docker with a pre-built conda environment, and submissions are auto-validated and scored with the task's original metric (AUROC, Spearman, …). **Agents**: Biomni v0.0.5 (Claude Sonnet 4), STELLA (OpenRouter default), AIDE v6.3.3 and MLAgentBench (both GPT-4.1), plus a Dummy agent with uninformative predictions. **Four independent replicates** per agent–task. **Metrics**: leaderboard percentile, mean rank across agents, % above human median, % any medal (MLE-bench definition), completion rate; reported **penalized** (failed run = 0th percentile) and **non-penalized** (failed runs dropped). **Compute**: imaging tasks on one NVIDIA L4 (16 vCPU, 64 GB) with 16 h limit; other tasks CPU-only with 8 h limit.

## Data
24 tasks: **drug discovery 9** (PolarisHub / TDC: EGFR inhibitor classification, liver microsomal clearance, plasma protein binding, solubility, CYP2D6, logP, hERG, BBB, Caco-2); **biomedical imaging 4** (Kaggle: OSIC pulmonary fibrosis FVC, PatchCamelyon histopathology metastasis, RSNA brain-tumour MGMT methylation, UW GI-tract segmentation); **protein engineering 6** (ProteinGym: SARS-CoV-2 spike RBD, Tsuboyama 2023 stability, indels, …); **single-cell 5** (OpenProblems: CITE-seq modality prediction, PBMC small-molecule perturbation response, **cell-type label projection across diabetic kidney disease (DKD) datasets**, Slide-seqV2 spatially variable genes, breast-cancer cell–cell communication).

## Key results
**Penalized overall**: Biomni leaderboard percentile **34.45 ± 5.36** (best; mean rank 1.88; 100% completion), STELLA 31.84 ± 5.82 (91.7% completion), AIDE 28.50 ± 5.22 (80.2%), MLAgentBench 21.43 ± 4.40, Dummy 2.50. **Non-penalized**: STELLA overtakes at 39.45 ± 6.52, AIDE 37.41 ± 5.85, Biomni 34.45 — differences mostly within SEM. Best above-median rates ~34–43%; any-medal ≤ 21%. **By domain (penalized)**: single-cell — Biomni 55.62 (STELLA 54.23, AIDE 53.17 close); imaging — MLAgentBench best at 21.73; protein and drug — Biomni leads; without penalties STELLA leads imaging by a wide margin, AIDE leads protein, Biomni leads drug discovery. **Strategies**: across 94 above-median runs, strong agents more often tried diverse feature engineering and model types; AIDE hit the **100th percentile** on Tsuboyama 2023 with BLOSUM, conservation and physicochemical features, yet another replicate of the same agent on the same task reached only the **54th** — strategies are not stable across reruns. **Architectures**: Biomni and MLAgentBench used random forests ~50% of the time, AIDE stacked/gradient-boosting models; **deep learning was rarely tried and almost never the final model, even on imaging**, unlike DL-dominated human leaderboards. **Failures**: 41 failed runs were mostly scaffolding issues — resource exhaustion (copying large images), silent errors (try–except fallbacks: scripts ran but saved no predictions), stalls on unnecessary environment creation, uncaught framework exceptions, timeouts.

## Contributions
- The first **end-to-end executable ML** agent benchmark across four biomedical domains, with expert-dominated leaderboards as the human baseline.
- Reports both penalized and non-penalized views, separating capability from scaffolding reliability.
- Manual log analysis of strategies in successful runs, chosen architectures and causes of failed runs.
- A pip-installable, documented open-source package lowering the reproduction barrier.

## Limitations
- Each agent uses its own default LLM (GPT-4.1 / Claude Sonnet 4 / OpenRouter default), **confounding agent design with base model**; the authors concede LLMs should be varied systematically.
- Public leaderboards mix expertise, effort and compute, so they are an imperfect human baseline; only 24 tasks (4–9 per domain), so error bars are wide.
- Scores predictions only; does not check for leakage, proper validation use, or whether the agent's account of its method is truthful.
- No AutoML (H2O, Lazy Predict) comparison, so the gain of LLM agents over automated pipelines is unknown.

## Relation to our direction
For **Topic 2**, three concrete pieces of evidence: (1) AIDE's 100th vs 54th percentile on two reruns of the same task is a direct case for the rerun-stability axis — performance/conclusions can swing wildly across reruns; (2) the **silent-error** failure mode (try–except fallbacks make a script look successful while producing nothing) is exactly what claim-to-evidence verification must catch — the agent reports "done" but the evidence (prediction file) does not exist — and belongs in our omics failure taxonomy; (3) the agent/LLM confound tells us to fix the base model in our evaluations, as DeepEvidence does. For **Topic 1**, its single-cell suite contains **label projection across DKD datasets** (from OpenProblems), a ready-made kidney-omics task usable as a comparator for the reference-mapping / label-transfer baseline in KidneyAnomalyBench; but BioML-bench scores prediction metrics only, not anomaly or artifact detection. For the detect → model → revert line, agents' preference for classical ML (random forests, gradient boosting) over deep learning means having agents autonomously build virtual-tissue models (inherently DL) is not yet realistic.

## Reusable assets
- **Code / package:** BioML-bench (pip-installable, with docs and tutorials).
<https://github.com/science-machine/biomlbench>
- **Task sources:** PolarisHub, TDC, Kaggle, ProteinGym, OpenProblems (including the DKD label-projection task).
- **Reporting convention:** penalized / non-penalized plus completion rate, to separate capability from reliability.

## Follow-ups
- MLE-bench (arXiv 2410.07095), STELLA (arXiv 2507.02004), AIDE (arXiv 2502.13138).
- Details of OpenProblems' DKD label-projection task (data source, metric) as a possible Topic 1 baseline.
- Whether later versions fix the base LLM or add AutoML comparators.

## Cite
```bibtex
@article{Miller_2025, title={BioML-bench: Evaluation of AI Agents for End-to-End Biomedical ML}, url={http://dx.doi.org/10.1101/2025.09.01.673319}, DOI={10.1101/2025.09.01.673319}, publisher={openRxiv}, author={Miller, Henry E. and Greenig, Matthew and Tenmann, Benjamin and Wang, Bo}, year={2025}, month=Sept }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

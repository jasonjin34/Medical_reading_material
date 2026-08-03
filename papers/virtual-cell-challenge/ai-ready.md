<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# Virtual Cell Challenge

- **Authors:** Arc Institute (organizer); companion paper by Arc Institute researchers
- **Venue / Year:** Arc Institute public competition; companion paper in *Cell* · 2025
- **DOI:** 10.1016/j.cell.2025.06.008 (companion paper)
- **URL:** https://virtualcellchallenge.org/
- **Bibkey:** virtual-cell-challenge
- **Status:** complete

## Abstract
The Virtual Cell Challenge is an annual public competition, launched in 2025 by the Arc Institute, in which machine-learning models compete to predict how single cells respond to genetic (CRISPR) perturbations. The inaugural edition frames the problem as "a Turing test for the virtual cell" and focuses on the hardest realistic setting — context generalization: predicting the transcriptomic effects of single-gene perturbations in a held-out cell type, the H1 human embryonic stem cell (H1 hESC). The goal is to establish rigorous, public, comparable standards for AI "virtual cell" models and to accelerate creation of high-quality perturbation datasets.

## Full text / Extract

### What the challenge is
- Organized by the Arc Institute as an annual, public, prize-based competition on cellular-response prediction.
- Companion paper: "Virtual Cell Challenge: Toward a Turing test for the virtual cell," *Cell*, 2025.
- Purpose: incentivize progress in AI + biology, produce high-quality datasets, and set rigorous standards for evaluating how well AI models simulate cellular behavior. Arc plans to repeat it each year with new single-cell datasets, different cell types, and progressively harder biological tasks (e.g., more complex perturbations).

### Task / objective
- Core task: **context generalization** — predict the effects of single-gene perturbations in a held-out cell context (H1 hESC).
- Given an unperturbed H1 hESC transcriptomic reference plus training profiles, participants build a model that predicts the post-perturbation single-cell gene-expression profile for held-out (unseen) perturbation genes.
- Scientific motivation: an accurate perturbation→expression map enables in-silico screening for interventions that shift cell state.

### Dataset
- A purpose-built single-cell transcriptomics (Perturb-seq) dataset: ~300,000 H1 human embryonic stem cells (H1 hESCs) with 300 genetic perturbations chosen to span a broad range of phenotypic responses.
- Splits:
  - Unperturbed transcriptomic reference of H1 hESCs.
  - Training set: single-cell profiles for 150 gene perturbations (~150,000 cells).
  - Validation set: 50 gene perturbations, used to drive a live leaderboard during the competition.
  - Final test set: 100 held-out perturbations.
- Additional data allowed: Arc Virtual Cell Atlas (>500 million cells), scBaseCount, Tahoe-100M, and X-Atlas/Orion (the largest publicly available Perturb-seq dataset).

### Evaluation metrics (composite score of three)
1. **Differential Expression Score (DES)** — how accurately the model predicts differentially expressed genes in response to a perturbation.
2. **Perturbation Discrimination Score (PDS)** — how well predicted expression changes distinguish the effects of different perturbations relative to ground truth.
3. **Mean Absolute Error (MAE)** — global absolute error between predicted and true post-perturbation expression across all genes.

### Baseline model (STATE)
- Arc released STATE, a transformer-based virtual cell model with two modules:
  - **State Transition (ST):** bidirectional transformer trained on 100M+ perturbed cells across ~70 contexts, predicting perturbation effects across cell collections.
  - **State Embedding (SE):** trained on ~167M human cells to learn expression variation and detect biological perturbation signal while resisting technical noise.
- On unseen single-gene perturbations, STATE improved over a cell-mean baseline by 26%, vs 19% for a linear baseline and 22% for GEARS. STATE reportedly improved perturbation-effect discrimination by >50% and identified differentially expressed genes with >2-fold accuracy vs prior models.
- Overall finding: perturbation-prediction models do not yet consistently outperform naive baselines across all metrics.

### Timeline (2025 edition)
- Validation submissions due October 27, 2025.
- Final submissions due November 3, 2025.
- Winners announced December 2025.

### Prizes and sponsors
- Top three teams: prizes valued at $100,000, $50,000, and $25,000 (combining cash and NVIDIA DGX Cloud credits) — $175,000 total.
- Additional Generalist Prize ($100,000) for the highest average ranking across seven metrics.
- Sponsored by NVIDIA, 10x Genomics, and Ultima Genomics.

### Participation and results
- Over 5,000 people registered across 114 countries; over 1,200 teams submitted results; over 300 teams made final submissions.
- Winners:
  - 1st ($100,000) — Team BM_xTVC (Yucheng Guo, Qirong Yang, BioMap Research), model xTrimoSCPerturb: hybrid deep learning + classical statistics using an improved scFoundation architecture with protein embeddings and public perturbation datasets.
  - 2nd ($50,000) — Team XLearning Lab (Xi Peng, Sichuan University), model "X": metric-driven conditional generation with fully connected networks, ESM-2 protein embeddings, and pseudo-bulk representation.
  - 3rd ($25,000) — Team Outlier (Qiyuan Liu, Qirui Zhang, Jin-Hong Du, Siming Zhao, Jingshu Wang), model TransPert: statistical framework using summary-level data and similarity-aware aggregation across reference cell lines.
  - Generalist Prize ($100,000) — Team Altos Labs, model "go-with-the-flow": flow-matching generative model capturing heterogeneous cellular responses.
- Technical insights: purely AI-based approaches did not consistently outperform statistical baselines; hybrid models (deep learning + statistical features) outperformed pure neural networks; multi-modal features, especially protein embeddings, added value; almost all models performed worse than the baseline on MAE.

### How to participate
- Register and submit via https://virtualcellchallenge.org/ (evaluation details at /evaluation). Participants download the provided reference/training data, optionally leverage external corpora, and submit predictions scored on the live leaderboard (validation) and final held-out test set.

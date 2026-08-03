<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# Conditional Monge Gap enables generalizable single-cell perturbation modelling

- **Authors:** Driessen, Alice; Rajwade, Dhruva Abhijit; Harsanyi, Benedek; Rapsomaniki, Marianna; Born, Jannis
- **Venue / Year:** Nature Machine Intelligence · 2026
- **DOI:** 10.1038/s42256-026-01242-8
- **URL:** https://doi.org/10.1038/s42256-026-01242-8
- **Bibkey:** Driessen_2026
- **Status:** complete

## Abstract
Learning the response of single cells to various treatments offers great potential to enable targeted therapies. In this context, neural optimal transport has emerged as a principled methodological framework because it inherently accommodates the challenges of unpaired data induced by cell destruction during data acquisition. However, most existing optimal transport approaches are incapable of conditioning on different treatment contexts (for example, time, drug treatment, drug dose or cell type), and we still lack methods that unanimously show promising generalizability to unseen treatments. Here we propose the Conditional Monge Gap (CMonge), which learns optimal transport maps conditionally on arbitrary covariates. We demonstrate its value in predicting single-cell perturbation responses conditional to one or more drugs, drug dose or combinations thereof. We found that our conditional models achieve results comparable with and sometimes even superior to the condition-specific state-of-the-art single-cell RNA sequencing as well as multiplexed protein imaging data. Notably, by scaling to hundreds of conditions and training on hundreds of millions of drugs, we enable cross-task learning and unlock generalizability to unseen drugs. Our method widely outperforms other conditional models in capturing heterogeneity in cell populations. In short, CMonge is mathematically grounded, highly parameter-efficient relative to single-cell foundation models and yields accurate predictions for unseen drugs using only the compound structure. Thus, it opens a practical route for accelerating drug discovery and repurposing. Driessen et al. present a conditional optimal transport method that can model the distribution shift between perturbed and unperturbed cell transcriptomes and that can generalize to unseen contexts.

## Full text / Extract
<!-- Full cleaned text for open-access; for paywalled leave the note below. -->
> status: abstract-only — Nature Machine Intelligence full text is behind a paywall. The content below is drawn from the public preprint (arXiv:2504.08328, "Towards generalizable single-cell perturbation modeling via the Conditional Monge Gap") and the open-source code/data (MIT-licensed `AI4SCR/conditional-monge-gap`). Numbers may differ slightly from the final journal version. Drop `source.pdf` into this folder and re-run extraction to add the exact journal text.

### Preprint / repository summary (public sources)

**Problem.** Single-cell perturbation data are unpaired because cells are destroyed during sequencing/imaging, so responses must be modelled at the distribution level. Existing neural optimal transport (OT) methods (e.g. CellOT) train one model per condition, cannot condition on treatment context (drug, dose, cell type, time), and do not generalize to unseen treatments.

**Method — Conditional Monge Gap (CMonge).** Extends the Monge Gap (an ICNN-free regularizer that pushes a learned map toward the optimal-transport / minimal-displacement solution) to be conditioned on arbitrary covariates. An encoder–decoder maps control-cell representations to perturbed ones while a condition vector (a drug/dose/combination embedding) is injected into the map. Training objective = Sinkhorn-divergence fitting term + Monge-gap regularizer. An autoencoder is trained first for dimensionality reduction; the conditional Monge model is then trained in the latent space. Aggregating data across hundreds of conditions enables cross-task learning and out-of-distribution (OOD) prediction for unseen drugs/doses.

**Drug embeddings compared.**
- RDKit fingerprints — 194-dimensional, structure-based, computed from SMILES.
- Mode-of-Action (MoA) embeddings — 10-dimensional, effect-based, from multidimensional scaling over pairwise Wasserstein distances between treated cell populations.

**Datasets.**
- SciPlex3 (scRNA-seq): 762,039 cells; three cancer lines (A549, K562, MCF7); 187–188 compounds at four doses (10/100/1000/10000 nM) plus control; 748 drug–dose conditions. Experiments run on a 9-drug subset and on the full set of hundreds of conditions.
- 4i (multiplexed protein imaging / iterative indirect immunofluorescence): 97,748 cells (10,995 controls); melanoma tumor lines; 35 therapies (~2,500 cells each); 48 marker and morphology features; includes combination therapies.

**Evaluation metrics.** R² between predicted and target feature means; Maximum Mean Discrepancy (MMD); (entropic-regularized) Wasserstein distance; Sinkhorn divergence (also in the training objective).

**Baselines.** Identity mapping (lower bound); unconditional Monge Gap models (one per condition); autoencoder/VAE variant; ICNN via CellOT; chemCPA (state-of-the-art conditional method for unseen-drug prediction).

**Key results.**
- In-distribution (SciPlex, 9 drugs): unconditional Monge upper bound R² ≈ 0.950–0.978; CMonge-Dose-ID R² = 0.882–0.974 while using 4× fewer models; CMonge-DrugDose-MoA-ID on par with 36 condition-specific models.
- OOD (unseen drugs, SciPlex): CMonge-MoA-OOD R² ≈ 0.90 vs chemCPA ≈ 0.76 at the highest dose; scaling to 712 training conditions gives CMonge-MoA-OOD R² = 0.900 ± 0.059 vs chemCPA 0.760 ± 0.211; RDKit embeddings improve markedly once scaled to 187 drugs.
- 4i: CMonge-MoA beats the identity baseline on MMD for combination therapies; gains for single drugs limited by small effect sizes.
- CMonge is parameter-efficient relative to single-cell foundation models and predicts unseen drugs from compound structure alone.

**Limitations.** RDKit fingerprints need substantially more training conditions to match MoA (structure representations add noise at low condition counts); highest-dose conditions are hardest to learn; MoA embeddings require measured single-drug populations, so combinations lacking single-drug measurements cannot be evaluated; a mechanistically distinct drug (trametinib) predicted notably worse; on 4i the identity baseline already reaches R² > 0.6 (small effect sizes limit the benefit of conditioning); DrugDose-MoA-ID captures feature-mean R² worse than 36 individual models despite better Wasserstein performance.

**Reusable assets.** Code: `AI4SCR/conditional-monge-gap` (MIT, `pip install cmonge`, Python 3.10/3.11, JAX/OTT backend). CAR-T extension: `AI4SCR/car-conditional-monge`. Upstream integration: OTT (`ott-jax`) PR #605. Preprocessed SciPlex3 and 4i data: ETH research collection (handle 20.500.11850/609681). Pre-trained checkpoints in the repo `models/` directory (legacy checkpoints via the `cmonge_checkpoint_loading` git tag). Preprint: arXiv:2504.08328.

# PaDiM: A Patch Distribution Modeling Framework for Anomaly Detection and Localization

> **Bibkey** `Defard2020_201108785` · **Venue** Pattern Recognition. ICPR International Workshops and Challenges (ICPR 2020 Workshops), LNCS 12664 (2021) · **Category** anomaly · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2011.08785> · `status: complete`

---

## One-liner
PaDiM trains no network at all: it embeds every patch position with multi-layer features from an ImageNet-pretrained CNN, fits one multivariate Gaussian N(μ_ij, Σ_ij) per position over the normal training images, and at test time scores each patch by its **Mahalanobis distance** to produce an anomaly map — reaching 97.5% pixel AUROC / 92.1% PRO on MVTec AD with inference cost independent of training-set size.

## Problem
Joint **anomaly detection (image level) and localization (pixel/patch level)** in the one-class setting (normal-only training data). Both existing routes had drawbacks: reconstruction methods (AE/VAE/GAN) are intuitive but AEs often reconstruct anomalies well too; embedding-similarity methods (SPADE, Patch SVDD) were best, but SPADE runs K-NN over the whole training embedding set at test time, so time and memory grow linearly with training size — a deployment problem. PaDiM targets "SPADE-level accuracy with inference complexity independent of training-set size."

## Method
**(1) Patch embedding**: as in SPADE, activation maps from the first three layers of a pretrained CNN (ResNet18, Wide-ResNet-50-2 or EfficientNet-B5, all ImageNet-pretrained) are spatially aligned and **concatenated**, so the vector at each position (i,j) carries both fine-grained and semantic information; the grid equals the resolution of the largest activation map used. **Random dimensionality reduction**: randomly keep 100 or 550 of the concatenated dimensions (448 for R18) — which the authors find beats PCA. **(2) Learning normality**: for the N normal training images' embeddings X_ij at position (i,j), assume a multivariate Gaussian and estimate the sample mean μ_ij and covariance Σ_ij = 1/(N−1) Σ(x−μ)(x−μ)ᵀ + εI (ε = 0.01 to keep it invertible); since embeddings span several layers, Σ_ij naturally encodes **inter-layer correlations**. **(3) Inference**: inspired by Rippel et al. (MahalanobisAD) and Lee et al. (Mahalanobis confidence scores for OOD detection), each test patch is scored by M(x_ij) = sqrt((x−μ_ij)ᵀ Σ_ij⁻¹ (x−μ_ij)), forming the anomaly map; image score = map maximum. Preprocessing follows SPADE (resize 256×256, centre-crop 224×224; σ = 4 Gaussian smoothing of the map). "Training" is a single forward pass plus covariance estimation — no gradient optimization.

## Method lineage
**Paradigm: feature-embedding & memory bank** (specifically its parametric-density branch — one Gaussian per position, so also density / one-class in spirit). **Builds on**: Lee et al. 2018 (class-conditional Gaussians + Mahalanobis on classifier features for OOD detection); Rippel et al. 2020 (MahalanobisAD) moving that to image-level AD; SPADE's pretrained multi-layer features with patch-level K-NN localization. PaDiM's step is from one global Gaussian to **one Gaussian per patch position**, keeping inter-layer covariance. **Led to**: PatchCore names PaDiM as its closest predecessor and targets its limits (alignment dependence; each patch compared only to same-position statistics); CFLOW-AD shows that under an MVG prior the normalizing-flow objective reduces to the Mahalanobis distance and reuses PaDiM's pyramid-pooling setup verbatim. PaDiM is now a standard baseline in libraries such as anomalib.

## Data
**MVTec AD**: 15 classes (10 objects + 5 textures), ~240 images each, native 700²–1024², objects centred and aligned. **Rd-MVTec AD** (new): random rotation (−10°, +10°) and random crop (256→224) applied to both train and test sets to simulate misalignment, averaged over 5 random versions. **ShanghaiTech Campus (STC)**: static-camera surveillance video, 274,515 train / 42,883 test frames across 13 scenes at 856×480.

## Key results
- **Localization (MVTec AD)**: PaDiM-WR50-Rd550 averages (AUROC 97.5%, PRO 92.1%) over all classes, above SPADE (96.5, 91.7) and Patch SVDD (95.7, –); the gap is largest on textures — +4.0 pp AUROC and +4.8 pp PRO over SPADE. The light PaDiM-R18-Rd100 reaches (96.7, 90.1).
- **Detection (image AUROC)**: PaDiM-WR50-Rd550 95.3%, slightly below MahalanobisAD (EfficientNet-B4) at 95.8%; PaDiM-EfficientNet-B5 reaches **97.9%**, at least 2.6 pp above every method.
- **Inter-layer ablation (R18)**: summing three per-layer models gives 96.0/89.0 vs 97.1/90.8 for PaDiM-R18 with cross-layer covariance (+1.1 AUROC, +1.8 PRO). **Dim. reduction**: random 100-d (96.7, 90.5) clearly beats PCA 100-d (93.5, 85.7) and nearly matches full 448-d (97.1, 90.8).
- **Misalignment robustness (Rd-MVTec AD)**: PaDiM-WR50-Rd550 (92.2, 73.1) vs SPADE (87.2, 69.0) vs VAE (62.1, 27.8); relative to standard MVTec, PaDiM's AUROC drops 5.3 pp vs 12.2 (VAE) and 8.8 (SPADE).
- **STC localization**: PaDiM-R18-Rd100 91.2% AUROC vs SPADE 89.9% and CAVGA-RU 85%.
- **Cost**: CPU inference 7.10 s/image for SPADE vs 0.95 s (PaDiM-WR50-Rd550) and 0.23 s (PaDiM-R18-Rd100); memory on STC 37 GB for SPADE vs 5.2 GB for PaDiM-WR50-Rd550. Training (serial CPU) takes ~150 s per MVTec class.

## Contributions
- Pushes "Gaussian + Mahalanobis" from image level to **per patch position**, making a parametric density model state-of-the-art for localization for the first time.
- Models **inter-semantic-level correlations** via full covariance over concatenated multi-layer embeddings, with ablations showing the gain.
- Finds random dimensionality reduction beats PCA (high-variance directions are not necessarily the discriminative ones).
- Introduces a misaligned evaluation (Rd-MVTec AD); inference time and memory independent of training-set size.

## Limitations
- **Position-bound**: one Gaussian per (i,j) assumes the same position means the same thing across images — it needs alignment, and train/test images must share a shape (exactly what PatchCore targets).
- **Unimodal Gaussian**: one Gaussian per position cannot represent multimodal normality.
- Memory grows with image resolution (H×W inverse D×D covariances stored); fully reliant on ImageNet feature transferability with no domain adaptation.
- Validated only on industrial and surveillance data; no discussion of how to set an operating threshold.

## Relation to our direction
PaDiM is the **simplest, interpretable "healthy reference → distance" baseline** for the detect stage and a natural floor for the artifact-injection topic. **Mapping to kidney omics**: samples = cells or Xenium/Visium spots; "normal training set" = a healthy kidney reference (Lake atlas, KPMP/HuBMAP healthy donors, normal controls within the cohort under test); feature space = scVI / scArches latent space or single-cell foundation-model embeddings, and UNI2-h / Virchow patch embeddings on the H&E side. PaDiM's "one Gaussian per position" maps most naturally to **"one Gaussian per cell type (or per anatomical unit: glomerulus / proximal tubule / interstitium)"** — the Mahalanobis distance of a cell from its own type's healthy distribution is the conditional version of PaDiM. **What breaks**: (1) PaDiM relies on positional alignment; the omics analogue is correct cell-type annotation — mis-annotated cells get compared with the wrong Gaussian and false positives explode; (2) a unimodal Gaussian fails on continuous states (the proximal-tubule healthy → injured → failed-repair axis); (3) batch effects, ambient RNA and doublets all push cells away from the mean, and Mahalanobis cannot tell technical artifacts from disease — exactly what the artifact-injection topic resolves with **cross-modal agreement** (snRNA ↔ snATAC ↔ Xenium ↔ H&E); (4) omics has no pixel masks, so PRO / pixel AUROC cannot be computed and KidneyAnomalyBench must substitute expert labels or synthetic perturbations. **Existing repo papers with the same idea**: healthy-ref-natgenet-2023 finds disease states in an scVI healthy-atlas latent space (via Milo differential abundance rather than a distance score); pathology-ad-bench-mlhealth-2025 benchmarks PaDiM within its "feature distribution" family on Camelyon16, Crohn's colon and mouse glomeruli, finding that family best overall but real pathology far harder than industrial data; histo-nejmai-2024 scores pathology-foundation-model features with kNN distance — the same "pretrained features + distance" paradigm. PaDiM's "random beats PCA" finding is also a warning for us: in scVI/PCA latent spaces the high-variance components are often batch or cell type, not the lesion direction.

## Reusable assets
- **Code:** no official code release in the paper; the commonly used implementation is in anomalib (used by pathology-ad-bench-mlhealth-2025).
<https://github.com/open-edge-platform/anomalib>
- **Eval protocol:** the Rd-MVTec AD misalignment test (random rotation + crop, averaged over 5) — analogous to robustness tests that perturb cell-type annotation or spatial registration in omics.
- **Recipe:** multi-layer concatenation + random dim. reduction + one Gaussian per group + ε = 0.01 regularization, directly applicable to scVI / foundation-model embeddings as a per-cell-type baseline.

## Follow-ups
- Rippel et al. 2020 (MahalanobisAD) and SPADE (Cohen & Hoshen 2020), the two direct predecessors — not yet in the repo.
- Compare with mahalanobis-ood-neurips-2018 — how class-conditional Gaussians on classifier features map to "per-cell-type Gaussians".
- Run a per-cell-type PaDiM-style baseline on the Lake-atlas scVI latent space as a floor for KidneyAnomalyBench.

## Cite
```bibtex
@inproceedings{Defard2020_201108785,
  title = {{PaDiM}: A Patch Distribution Modeling Framework for Anomaly Detection and Localization},
  author = {Defard, Thomas and Setkov, Aleksandr and Loesch, Angelique and Audigier, Romaric},
  booktitle = {Pattern Recognition. ICPR International Workshops and Challenges},
  series = {Lecture Notes in Computer Science},
  volume = {12664},
  pages = {475--489},
  publisher = {Springer},
  year = {2021},
  doi = {10.1007/978-3-030-68799-1_35},
  eprint = {2011.08785},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2011.08785}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

# CFLOW-AD: Real-Time Unsupervised Anomaly Detection with Localization via Conditional Normalizing Flows

> **Bibkey** `Gudovskiy2021_210712571` · **Venue** 2022 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV) (2022) · **Category** anomaly · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2107.12571> · `status: complete`

---

## One-liner
CFLOW-AD trains, for each scale of an ImageNet-pretrained CNN encoder, a **normalizing-flow decoder conditioned on positional encoding** that estimates the exact log-likelihood of each patch feature as the anomaly score. The authors show that under a multivariate-Gaussian prior the flow objective reduces to the Mahalanobis distance (so PaDiM is a special case), and CFLOW-AD reaches 98.26% detection AUROC, 98.62% localization AUROC and 94.60% AUPRO on MVTec while being ~10× faster and smaller than PaDiM/SPADE in the same setting.

## Problem
State-of-the-art unsupervised AD + localization (SPADE, PaDiM) was accurate but costly in post-processing: SPADE runs kNN over a training feature gallery with prohibitive memory and speed; PaDiM stores a D×D inverse covariance per spatial position, so memory grows with resolution (the authors infer this is why it was only timed on CPU). Meanwhile fully generative models (GANs, VAEs) cannot give exact likelihoods and do not beat traditional methods on MVTec. The question: can one have **exact density estimation** with a **fully convolutional, low-memory, real-time** architecture?

## Method
**Theory**: CNNs trained with L2 weight decay impose an implicit multivariate-Gaussian (MVG) prior on intermediate features — justifying the Mahalanobis scoring of Lee et al. / Rippel et al. / PaDiM; the authors further show that under MVG the normalizing flow's reverse-KL loss can be written as a Mahalanobis-minus-Euclidean distance term plus a log-Jacobian term, so the flow framework converges to Mahalanobis-like solutions while fitting **arbitrary** distributions, not just MVG. **Encoder**: ImageNet-pretrained CNN (ResNet-18, WideResNet-50 or MobileNetV3L) with the same multi-scale pyramid pooling as PaDiM (K scales, default 3, layers 1–3). **Decoders**: an independent conditional normalizing flow g_k per scale; the condition c_i is a 2D sinusoidal **positional encoding** (C_k = 128), concatenated with intermediate vectors in every coupling layer; a coupling layer = fully connected + softplus + permutation; because decoders act on single feature vectors with parameters shared across positions, the whole model is translation-equivariant and fully convolutional, independent of feature-map size. **Training**: maximum likelihood, i.e. minimizing ‖u‖²/2 − log|det J|, sampling 8,192 feature vectors from 32 feature maps per mini-batch; Adam lr 2e-4, 100 epochs, cosine annealing. **Inference**: per-scale log-likelihoods → probabilities normalized to [0,1] → bilinear upsampling to input size → aggregated across scales into the anomaly map S. One model per MVTec class and per STC scene.

## Method lineage
**Paradigm: density / one-class** (exact density estimation in a pretrained feature space; shares the encoder with the feature-embedding family). **Builds on**: RealNVP (Dinh et al.) and conditional INNs (Ardizzone et al.) for the flow architecture; DifferNet (Rudolph et al., WACV 2021) as the first flow for image-level AD; the "MVG + Mahalanobis" line Lee et al. 2018 → Rippel et al. 2020 → PaDiM, which the authors theoretically unify as a special case of the flow; PaDiM's pyramid-pooling setup is adopted verbatim. **Led to**: together with FastFlow and CS-Flow it forms the normalizing-flow family in AD and is a standard anomalib baseline; pathology-ad-bench-mlhealth-2025 benchmarks CFLOW-AD within that family on pathology and notes the family's "high computational cost and sensitivity to architectural choices".

## Data
**MVTec AD**: 15 classes, 3,629 training (all defect-free) / 1,725 test images; resized without cropping to the chosen resolution (128/256/512), ±5° rotation augmentation in training. **STC**: 274,515 training / 42,883 test frames over 13 campus scenes, fixed 256×256.

## Key results
- **MVTec average (WRN-50)**: detection AUROC **98.26%** (PaDiM 97.9, CutPaste 97.1, DifferNet 94.9, Patch SVDD 92.1, SPADE 85.5); localization AUROC **98.62%** (PaDiM 97.5, SPADE/CutPaste 96.0, Patch SVDD 95.7, DFR 95.0); AUPRO **94.60%** (PaDiM 92.1, SPADE 91.7, DFR 91.0) — i.e. +0.36 detection, +1.12 localization AUROC / +2.5 AUPRO; each run repeated 4× and averaged.
- **STC**: detection AUROC 72.63% (CAVGA 71.9); localization 94.48% (PaDiM 91.2, SPADE 89.9, CAVGA 85.0).
- **Ablations (localization AUROC)**: 4→8 coupling layers +0.15% on average; 3 scales vs 2 +1.4% (adding the 32×32 layer 1); conditional vs unconditional flow +0.5% (the positional prior helps); WRN-50 vs R18 +0.81%; **optimal input resolution varies by class** (512 for most, 256 for cable/pill, 128 for transistor).
- **Speed**: on a GPU (1080 8GB) CFLOW-AD-WRN50 runs at 27 / 9 fps (256 / 512 input) vs PaDiM-WRN50 1.1 fps and SPADE-WRN50 0.1 fps (the latter two from the PaDiM paper's CPU measurements); R18 version 34 / 12 fps vs PaDiM-R18 4.4 fps — summarized as 8–25× faster. Excluding the encoder, the model is 1.7–50× smaller than SPADE and 2–7× smaller than PaDiM.

## Contributions
- **Theoretical unification**: explains why MVG/Mahalanobis is a justified prior and shows the flow objective converges to similar solutions under it — placing Lee et al., Rippel et al. and PaDiM in one likelihood framework.
- **Position-conditioned flow**: puts a spatial prior into the density model via positional-encoding conditioning while sharing parameters across positions (unlike PaDiM's per-position parameters).
- Fully convolutional, feature-map-size agnostic, small and real-time on GPU; open code with reproducible experiments.

## Limitations
- **Per-class input resolution**: headline results use the best resolution per class (128/256/512), and the paper does not explain how it was chosen without seeing test anomalies — a risk of test-set tuning that makes comparison with uniformly configured PaDiM/PatchCore imperfect.
- Unequal speed comparison: CFLOW-AD timed on GPU, PaDiM/SPADE numbers taken from CPU measurements.
- The authors cite "why normalizing flows fail to detect OOD data" (Kirichenko et al.) and "do deep generative models know what they don't know?" (Nalisnick et al.) but do not systematically test that risk in the AD setting; likelihoods still depend on ImageNet features.
- Requires training (100 epochs per class), still one model per class.

## Relation to our direction
CFLOW-AD gives the artifact-injection topic the **"conditional density" modelling angle**: anomaly score = negative log-likelihood given context. **Mapping to kidney omics**: samples = cells/spots; normal training set = healthy reference; features = scVI latents or foundation-model embeddings; and crucially the **condition c** — positional encoding of pixels in the paper, which in omics becomes **cell type, anatomical region (cortex/medulla, glomerulus/tubule/interstitium), spatial niche composition, donor covariates (age, sex)**. The model then learns p(cell state | cell type, niche, donor), so a cell that looks normal in the medulla but is out of place next to a cortical glomerulus can be flagged. This is more flexible than PaDiM's one Gaussian per group (it can be multimodal) and more probabilistic than PatchCore's kNN distance, and it can in principle feed conformal calibration (as conformal-scrna-bioinformatics-2025 does with reconstruction error as non-conformity score — swap in the negative log-likelihood). **What breaks**: (1) **likelihood ≠ anomaly** — flows are known to assign high likelihood to simple/low-complexity samples; in snRNA, low-UMI, high-ambient "empty-droplet-like" cells carry little information and may get high likelihood and pass as normal, while rich, high-quality healthy cells may score low; (2) batch effects shift the density directly, so batch must be in the condition or integrated out first; (3) under continuous disease states the likelihood says "how rare", not in which direction; (4) the paper's per-class resolution picking is, in omics terms, "tuning hyperparameters per sample while looking at results" — it must be disallowed in KidneyAnomalyBench, with parameters chosen on anomaly-free validation data only (cf. pathology-ad-bench-mlhealth-2025's unbiased epoch-selection protocol). **Existing repo papers with the same idea**: pathology-ad-bench-mlhealth-2025 benchmarks CFLOW-AD on Camelyon16, Crohn's colon and mouse glomeruli; sardine-bioinformatics-2025 compares local **densities** on an expression-manifold kNN graph across conditions — a spatial-transcriptomics relative of the density view, though non-parametric and cross-condition rather than a conditional likelihood learned on a healthy reference.

## Reusable assets
- **Code:** official PyTorch implementation (built on the FrEIA flow library) with reproducible experiments.
<https://github.com/gudovskiy/cflow-ad>
- **Library:** the CFLOW implementation in anomalib.
<https://github.com/open-edge-platform/anomalib>
- **Modelling piece:** the conditional coupling layer (condition concatenated into every layer) — cell type / niche / donor one-hots or embeddings can serve as the condition for conditional density on scVI latents.

## Follow-ups
- DifferNet (Rudolph et al., WACV 2021), FastFlow and CS-Flow — the rest of the flow family in AD.
- Kirichenko et al. 2020, "Why normalizing flows fail to detect out-of-distribution data" — to assess the "likelihood ≠ anomaly" risk for low-quality single cells.
- Contrast with mahalanobis-ood-neurips-2018 and energy-ood-neurips-2020: likelihood vs Mahalanobis vs energy scores on the same embedding.

## Cite
```bibtex
@inproceedings{Gudovskiy2021_210712571,
  title = {{CFLOW-AD}: Real-Time Unsupervised Anomaly Detection with Localization via Conditional Normalizing Flows},
  author = {Gudovskiy, Denis and Ishizaka, Shun and Kozuka, Kazuki},
  booktitle = {2022 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)},
  pages = {1819--1828},
  publisher = {IEEE},
  year = {2022},
  doi = {10.1109/WACV51458.2022.00188},
  eprint = {2107.12571},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2107.12571}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

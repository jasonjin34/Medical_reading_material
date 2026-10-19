# A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks

> **Bibkey** `Lee2018_180703888` · **Venue** Advances in Neural Information Processing Systems 31 (NeurIPS 2018) (2018) · **Category** anomaly · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/1807.03888> · `status: complete`

---

## One-liner
Without retraining a pre-trained softmax classifier, fit **class-conditional Gaussians with a tied covariance** (GDA/LDA) in its feature space and use the **Mahalanobis distance** of a test sample to the closest class mean as the confidence score; with input pre-processing and a multi-layer feature ensemble, the same score reached state of the art on both OOD and adversarial-sample detection, was more robust to noisy labels and small training sets, and enabled training-free class-incremental learning.

## Problem
Softmax classifiers produce overconfident posteriors even for abnormal samples — statistically far OOD inputs or adversarial ones. Prior detectors targeted only OOD (the MSP baseline and ODIN, both using output-layer confidence) or only adversarial samples (kernel density KD+PU, LID); no **universal detector** worked well on both. ODIN also tunes its hyperparameters on OOD validation data, which is usually unavailable in advance.

## Method
**From softmax to a generative classifier**: under GDA, the posterior induced by class-conditional Gaussians with a tied covariance is equivalent to a softmax classifier, so pre-trained features f(x) may approximately follow class-conditional Gaussians. Empirical class means μ̂_c and the tied covariance Σ̂ are estimated from training data (the MLE fit). **Score**: M(x) = max_c −(f(x)−μ̂_c)ᵀ Σ̂⁻¹ (f(x)−μ̂_c), i.e. the log-density of the test sample. The authors first check that a Mahalanobis-distance classifier matches softmax accuracy (contrary to the belief that generative classifiers must be worse) and that the Mahalanobis score beats Euclidean distance and MSP on ResNet/CIFAR-10 vs TinyImageNet. **Calibration techniques**: (1) **input pre-processing** — perturb the input in the direction that increases M(x), x̂ = x − ε·sign(∇ₓ distance), like ODIN but on the Mahalanobis score; (2) **feature ensemble** — extract features at the end of every dense/residual block (average-pooled F×H×W → F×1), compute M_ℓ per layer and combine with weights α_ℓ learned by **logistic regression**; low-level features are often better for LSUN, TinyImageNet and DeepFool. Hyperparameters (ε, α_ℓ) are tuned on a validation set of 1,000 images per ID/OOD pair, or **using only ID samples plus FGSM adversarial samples** (no OOD data at all). **Class-incremental learning**: a new class just adds its mean and updates the tied covariance Σ̂ ← C/(C+1)·Σ̂ + 1/(C+1)·Σ̂_{C+1}, with no retraining.

## Method lineage
**Paradigm: feature-embedding density (a parametric one-class model)**, used as post-hoc OOD detection. It builds on the MSP baseline (`msp-ood-iclr-2017`, ref [13]) and ODIN (input pre-processing), and upgrades the feature-density adversarial detectors KD+PU and LID (Euclidean only) to Mahalanobis. **What it led to**: PaDiM (`padim-icpr-2020`) states "Inspired by [23], [26], we use the Mahalanobis distance" to score each patch position, with [26] being this paper — moving the idea from image-level OOD to **pixel-level industrial anomaly localization** and additionally modelling cross-layer correlations; the energy score (`energy-ood-neurips-2020`) uses it as a baseline; OpenOOD / the survey (`generalized-ood-survey-ijcv-2024`) list it as the distance-based representative (MDS), noting it does well on MNIST but poorly on CIFAR, while non-parametric KNN generalizes better.

## Data
Classifiers: DenseNet-100 and ResNet-34 trained on CIFAR-10, CIFAR-100 and SVHN. OOD tests: the other datasets, plus TinyImageNet (ImageNet subset, 10,000 test images, 200 classes) and LSUN (10,000 test images, 10 scenes), downsampled to 32×32. Adversarial attacks: FGSM, BIM, DeepFool, CW. Class-incremental learning: ResNet-34 with CIFAR-100 → downsampled ImageNet (and CIFAR-100 → CIFAR-10 in the appendix).

## Key results
- **Ablation** (ResNet / CIFAR-10 vs SVHN, TNR@TPR95): MSP baseline 32.47, ODIN 86.55; plain Mahalanobis 54.51 (AUROC 93.92); with input pre-processing + feature ensemble 96.42 (AUROC 99.14, AUPR-out 99.60).
- **Full OOD table** (tuned on OOD validation): beats MSP and ODIN in every ID/OOD pair. E.g. DenseNet / CIFAR-100 vs LSUN TNR@TPR95: MSP 16.7 / ODIN 41.2 / Mahalanobis 91.4; ResNet / CIFAR-100 vs LSUN: 18.8 / 45.6 / 90.9 (the abstract's "45.6% → 90.9%"); DenseNet / CIFAR-10 vs SVHN AUROC 89.9 / 95.5 / 98.1.
- **Tuning without OOD data** (ID + FGSM only): Mahalanobis still beats both consistently, even beating OOD-tuned ODIN, while ODIN sometimes falls below the baseline (e.g. DenseNet on SVHN). It degrades noticeably on ResNet / CIFAR-100 (e.g. TNR 41.9 vs SVHN).
- **Adversarial detection**: vs LID, CW TNR rises from 82.9% to 95.8% on ResNet / CIFAR-10; tuning only on FGSM still detects unseen BIM, DeepFool and CW.
- **Robustness**: with few training samples or up to 40% random labels, Mahalanobis AUROC stays high while MSP and ODIN drop.
- **Class-incremental**: after all new classes, AUC 40.0% (22.1% in the second scenario) vs 32.7% (15.6%) for a fine-tuned softmax and 32.9% (17.1%) for a Euclidean classifier.

## Contributions
(1) Motivates class-conditional Gaussian density in feature space via the GDA–softmax equivalence and shows the generative classifier loses no accuracy; (2) one score for both OOD and adversarial samples; (3) a multi-layer feature ensemble (low-level features are often more sensitive); (4) shows hyperparameters can be tuned without OOD data, using synthetic perturbations; (5) training-free class-incremental learning by updating means and the tied covariance.

## Limitations
The tied-covariance Gaussian is a strong assumption that fails for multi-modal classes or very different per-class variances; the best numbers rely on logistic-regression weights fit with OOD validation samples, and the FGSM substitute degrades on CIFAR-100/ResNet; input pre-processing needs an input gradient (an extra forward/backward at test time); all experiments use 32×32 images; OpenOOD later found it weaker than newer methods on CIFAR near-OOD (see the survey). It needs a labelled classifier (class means).

## Relation to our direction
**One of the most natural Plan-A detect baselines.** Mapping: samples = cells (or spots, H&E patches); feature space = the scVI/scANVI latent, a single-cell foundation-model embedding, or a pathology foundation model's patch embedding (UNI, Virchow); "classes" = cell types in a healthy reference (KPMP, the Lake atlas, HuBMAP normal kidney). Fit a mean and (tied) covariance per cell type and use the Mahalanobis distance to the nearest type as the anomaly score — **once on the snRNA latent and once on the snATAC latent**: both high → more likely disease, only one high → more likely artifact, which is exactly how Plan A's cross-modal agreement can be scored. The class-incremental update is also useful: once experts confirm a new injury state (e.g. aPT), add it to the reference as a new "normal" class by computing its mean and updating the covariance — a fit for iteratively building KidneyAnomalyBench. **Which assumptions break**: (1) **batch effects** — a global shift for a new donor or platform raises every cell's distance, so the score becomes batch-dominated; it must run on an integrated latent, and `refmap-eval-biorxiv-2025` (mapQC) handles exactly this by using the reference's own inter-sample variation as a null; (2) a **tied covariance** fits the kidney poorly — PT and immune cells have very different variance structure, calling for per-type covariances (QDA) or shrinkage, while rare types (e.g. MD, podocytes) have few cells and ill-conditioned covariances; (3) **doublets** fall between two class means at moderate distance and can be missed or mis-flagged; **ambient RNA** pushes all cells toward the soup profile, a systematic shift; **segmentation errors** (Xenium) blend neighbours' transcripts into "mixed" embeddings too; (4) **continuous disease states** blur "nearest class"; (5) input pre-processing needs an input gradient, which suits count data or frozen foundation-model embeddings poorly; (6) the ensemble weights are learned on an OOD validation set that the kidney setting does not have; substituting synthetic perturbations (the authors use FGSM) needs care — tuning on simulated doublets or injected ambient RNA would **teach the detector to find artifacts**. **Repo papers already in this family**: `padim-icpr-2020` is explicitly inspired by this paper and uses Mahalanobis distance per patch position for pixel-level localization (a direct template for H&E patches); `kidney-multimodal-genomebiol-2026` uses Mahalanobis distance to measure separation between integrated cell populations (as an integration metric, not anomaly detection); `histo-anomaly-bi-repo` fits a one-class SVM on healthy-tissue deep features and `histo-nejmai-2024` scores CTransPath features with a modified kNN — the same "distance/density in a healthy feature space" family; `healthy-ref-natgenet-2023` and `refmap-eval-biorxiv-2025` do neighbourhood-level comparisons against a healthy reference in the scVI latent. **For Plan B**: a callable, deterministic Mahalanobis scorer is a good tool for testing agent rerun stability and checking whether an agent states the Gaussian / tied-covariance assumption it relies on.

## Reusable assets
- **Code:** official PyTorch implementation (feature ensemble and input pre-processing included).
<https://github.com/pokaxpoka/deep_Mahalanobis_detector>
- **Algorithms:** Algorithm 1 (multi-layer Mahalanobis score) and Algorithm 2 (class-incremental mean / tied-covariance update) — a few lines of numpy on an scVI latent.
- **Metrics:** TNR@TPR95, AUROC, detection accuracy, AUPR-in/out.

## Follow-ups
- "A simple fix to Mahalanobis distance for improving near-OOD detection" (Ren et al., 2021, relative Mahalanobis) — targets near-OOD, closer to kidney "mild injury vs normal".
- Non-parametric KNN OOD (Sun et al., 2022; more robust per the survey) as the comparator to Mahalanobis on the scVI latent.
- On the KPMP reference, compare tied vs per-type vs shrinkage covariances and report AUROC separately on batch, doublet and true-injury "anomalies".

## Cite
```bibtex
@inproceedings{Lee2018_180703888,
  title = {A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks},
  author = {Lee, Kimin and Lee, Kibok and Lee, Honglak and Shin, Jinwoo},
  booktitle = {Advances in Neural Information Processing Systems 31 (NeurIPS 2018)},
  year = {2018},
  eprint = {1807.03888},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/1807.03888}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

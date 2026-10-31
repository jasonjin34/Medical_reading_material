# MedIAnomaly: A comparative study of anomaly detection in medical images

> **Bibkey** `Cai_2025` · **Venue** Medical Image Analysis (2025) · **Category** imaging · **Relevance** medium · **Access** paywall
> **Link** <https://doi.org/10.1016/j.media.2025.103500> · `status: complete`

---

## One-liner
Cai, Chen, Cheng et al. (HKUST) build MedIAnomaly, a unified medical-image AD benchmark — 7 datasets, 5 modalities (chest X-ray, brain MRI, fundus, dermoscopy, histopathology), 30 methods — comparing image-level classification and pixel-level segmentation under **unified architectures**, and dissecting key components one by one (latent size, reconstruction distance, gradient scores, DDPM noise type, ImageNet weights). Headline findings: a plain AE is a strong baseline, ImageNet features are surprisingly strong, and reconstruction quality correlates only weakly with detection performance.

## Problem
Medical AD has many methods but no fair, comprehensive comparison: (1) datasets and splits differ, and some datasets are too easy — the authors' plain AE is near-perfect on Hyper-Kvasir and OCT2017, so "beating SOTA" there means little; (2) methods of the same paradigm use different architectures and tricks (f-AnoGAN residual blocks, AE-Flow Wide ResNet-50-2, AE-U plain convs), so comparisons measure engineering rather than method. Prior surveys either run no experiments, cover one modality or one paradigm, or do not dissect components.

## Method
**Taxonomy**: reconstruction (image reconstruction: AE, VAE, MemAE, Constrained AE, AE-U, DAE, f-AnoGAN, GANomaly, AnoDDPM, AutoDDPM…; feature reconstruction: FAE…), self-supervised (one-stage: synthetic-anomaly classification/segmentation such as CutPaste, FPI, NSA, PII, AnatPaste; two-stage: train on synthetic anomalies, drop the head, fit a Gaussian density estimator on the representation) and feature-reference methods (knowledge distillation, feature modelling — ReContrast, PANDA, MSC). **Unified implementation**: all reconstruction methods share one AE where possible (64×64 input, four encoder blocks, latent 16); all SSL methods share a ResNet18 extractor (224×224). A frozen ImageNet ResNet18/ResNet152 + one-class classifier serves as a no-frills control. **Metrics**: image-level AUC and AP; pixel-level AP and dataset-wise best Dice (at the optimal test operating point, avoiding threshold selection); pixel AUC is deliberately excluded (insensitive to false positives). Three random seeds per experiment.

## Data
**Image-level classification (6)**: RSNA pneumonia CXR (train 3851 normal; test 1000+1000), VinDr-CXR (14 anomaly classes; train 4000; test 1000+1000), Brain Tumor MRI (train 1000; test 600 normal + 300 glioma + 300 meningioma), LAG glaucoma fundus (train 1500; test 811+811), ISIC2018 (nevus normal vs six other classes; train 6705; test 909+603), Camelyon16 (Bao et al.'s processed version, 40× patches; train 5088; test 1120 normal + 1113 abnormal). **Pixel-level segmentation (1)**: BraTS2021 FLAIR — 4211 normal axial slices from 1051 scans for training, 828 normal + 1948 tumour slices from 200 scans for testing. Two anomaly types are distinguished: CXR/MRI/fundus have **local anomalies** (a healthy image plus a lesion), whereas Camelyon16 and ISIC2018 have **global semantic anomalies** (a different category altogether). No validation set, since anomalies are unavailable at training.

## Key results
- **Baseline**: a plain AE is near-perfect on Hyper-Kvasir and OCT2017 — these datasets are unsuitable AD benchmarks; AE is also a stable baseline across the seven datasets, and the authors urge every paper to report it.
- **ImageNet weights**: a frozen ImageNet ResNet18 with a two-stage one-class classifier lands top-3 on nearly all datasets, beating most SSL methods with more complex training; adaptation methods like PANDA and MSC give no significant gain. Without ImageNet weights, reconstruction methods are more robust than SSL.
- **Pathology (Camelyon16)**: without ImageNet weights most AE/GAN methods fail outright, with only AE-U and DAE above 51% AUC; DDPM methods stand out — AutoDDPM **80.7%** and AnoDDPM-Simplex **70.6%** AUC. The authors argue pathology anomalies are tied to cellular morphology, so high-fidelity reconstruction helps here.
- **Latent size**: for local anomalies a tiny latent helps a lot — 128 → 4 gives RSNA +12.4% AUC / +10.0% AP, VinDr-CXR +12.7% AUC, LAG +7.3% AUC; brain MRI prefers larger latents (≈32/16); ISIC2018 (global anomalies) improves with larger latents. MemAE fails on medical images, and OC-SVM on AE latents is near chance (e.g. Camelyon16 AUC 0.49), showing normal/abnormal latents are inseparable.
- **Distance function**: perceptual loss (AE-PL) is SOTA or close on six datasets and >20% AUC above L2 on some, yet 6.1% worse on ISIC2018; SSIM gains >10% on RSNA but loses >10% on LAG. No distance beats L2 on all seven datasets.
- **Segmentation**: reconstruction beats SSL clearly; a plain AE beats every one-stage SSL segmenter on BraTS2021; DAE is best, >10% Dice above second place; **simple intensity thresholding ranks second**, ahead of DDPM methods. Simplex noise beats Gaussian noise in AnoDDPM by >30% Dice on BraTS.
- **Within SSL**: more realistic synthetic anomalies help (two-stage AnatPaste over CutPaste: +20.2% AUC on RSNA, +14.0% on VinDr-CXR); with the same synthesis, two-stage usually beats one-stage (AnatPaste: +11.5% AUC on RSNA, +16.0% on Brain Tumor).
- **Reconstruction quality ≠ detection**: AnoDDPM-Gaussian reconstructs best yet performs worst overall; AE-PL reconstructs with visible distortion yet is highly competitive — what matters is separable normal vs anomalous residual distributions, not overall fidelity.

## Contributions
- A unified medical-AD benchmark of 30 methods across three paradigms and five modalities, evaluating both classification and segmentation.
- **Unified architectures within each paradigm**, so comparisons isolate the method rather than engineering; and naive controls (frozen ImageNet features, intensity thresholding) are included in the benchmark.
- First systematic dissection of key components (latent restriction, distance function, gradient scores, noise type, SSL stages, synthesis realism), distilled into a "local vs global anomaly" explanatory frame.
- Dataset re-partitions and code are fully released.

## Limitations
- 2D only (MRI is sliced); 3D/volumetric AD is not covered; pixel-level evaluation has only BraTS2021, dominated by conspicuous tumours.
- The unified small AE (64×64 input) and ResNet18 sacrifice each method's original best configuration; pathology is represented only by one processed Camelyon16 version, and no pathology/medical foundation models are included.
- Best Dice picks the threshold on the test set — an optimistic upper bound; the authors also note Dice favours over-segmenting methods, current metrics may not reflect clinical utility, and feature-space scores lack calibration.
- Key configurations such as optimal latent size are still found by looking at test results; no unsupervised selection criterion is given.

## Relation to our direction
This is the detect-stage methods benchmark for **cross-modality medical images**, complementing the pathology-specific `pathology-ad-bench-mlhealth-2025` (which cites this paper as the most recent medical-AD benchmark). For **the artifact-injection topic / KidneyAnomalyBench** its biggest value is **benchmark hygiene**: (1) **prove the dataset is non-trivial first** — a plain AE acing Hyper-Kvasir means our benchmark must report naive baselines (AE, frozen features + one-class classifier, even non-learned "intensity/cell-count thresholding"), or it cannot show the task is hard; for kidney omics the naive controls might be single-gene expression thresholds or cell-type-proportion shifts; (2) **local vs global anomalies** — kidney lesions are mostly local (one sclerotic glomerulus, a patch of tubular injury), and the paper shows local anomalies need tightly constrained representations while global ones do the opposite, so KidneyAnomalyBench should stratify by these two types; (3) **frozen pretrained features are strong** — suggesting frozen foundation-model embeddings (UNI2-h, Nicheformer) + a one-class classifier as the default strong baseline; (4) **thresholds and calibration** — the "best Dice on the test set" and "uncalibrated feature-space scores" the authors criticize are exactly what the benchmark must avoid; we should fix thresholds on the expert-validated split and report calibration. For **the agent-trustworthiness topic**: when an agent claims "method X detects anomalies better than baseline," the verifier should check that it was compared against naive baselines like AE or thresholding — a concrete entry for the omics/imaging-specific failure taxonomy ("missing naive baseline").

## Reusable assets
- **Code and dataset re-partitions:** the MedIAnomaly repo (unified implementations of 30 methods + splits for seven datasets).
<https://github.com/caiyu6666/MedIAnomaly>
- **Preprint full text:** arXiv 2404.04518 (v4 is the journal version).
<https://arxiv.org/abs/2404.04518>
- **Evaluation conventions:** image AUC + AP, pixel AP + best Dice, three seeds, no pixel AUC; plus the "plain AE + frozen ImageNet features + intensity threshold" control trio.

## Follow-ups
- Lagogiannis et al. and Bao et al. (BMAD) medical-AD benchmarks, to compare conclusions.
- Cai et al.'s information-theoretic analysis that optimal latent entropy should match normal-data entropy — a possible unsupervised latent-size criterion.
- The one-class semi-supervised and few/zero-shot (VLM) settings in Section 5.5, and whether they transfer to kidney data with only a few expert-confirmed anomalies.

## Cite
```bibtex
@article{Cai_2025, title={MedIAnomaly: A comparative study of anomaly detection in medical images}, volume={102}, ISSN={1361-8415}, url={http://dx.doi.org/10.1016/j.media.2025.103500}, DOI={10.1016/j.media.2025.103500}, journal={Medical Image Analysis}, publisher={Elsevier BV}, author={Cai, Yu and Zhang, Weiwen and Chen, Hao and Cheng, Kwang-Ting}, year={2025}, month=May, pages={103500} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

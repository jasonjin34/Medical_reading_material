# Quantitative benchmarking of anomaly detection methods in digital pathology images

> **Bibkey** `Cui_2025` · **Venue** Machine Learning: Health (2025) · **Category** histopath · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1088/3049-477x/ae0f9f> · `status: complete`

---

## One-liner
Yuankai Huo's group (HRLB, Vanderbilt) benchmarks 23 generic anomaly-detection methods (reconstruction, feature-distribution, distillation, normalizing-flow and synthetic-anomaly families) under one protocol on real pathology (Camelyon16, Crohn's colon, mouse glomeruli), controlled synthetic pathology and MVTec industrial data, and systematically studies three under-examined factors — **image scale, "reversed" anomaly patterns, and how to pick a training epoch when no anomalies are available**. No method wins everywhere; feature-distribution methods are best overall; and real pathology is far harder than industrial data (mean ROC-AUC ≈ 0.645 vs 0.888).

## Problem
Pathology is a natural fit for normal-only anomaly detection: normal tissue is abundant, lesions are small, variable, ill-bounded and rarely annotated, and may be rare or entirely novel; AD is also used in preclinical toxicology to flag drug-induced tissue change. Yet most AD algorithms were built for industrial defect inspection, and pathology has three peculiarities — **multi-scale** structure (cell and tissue), **stain variability**, and **repetitive patterns with blurry normal/abnormal boundaries** — so how generic methods fare is unclear. Moreover, prior pathology-AD work trains for a fixed number of epochs and never discusses model selection when the validation set itself has no anomalies.

## Method
**Method pool**: 23 methods in five families — reconstruction (GANomaly, SkipGanomaly, DAE, FAE, DFR, HTAES, IGD, UniAD, DRAEM…), feature distribution (PatchCore, PaDiM, PANDA, CFA, DFKDE, DFM), distillation (STFPM, Reverse Distillation, Revisit Distillation, ReContrast, EfficientAD), normalizing flow (FastFlow, CFLOW-AD, CS-Flow) and synthetic anomaly (CutPaste, DRAEM), sourced from anomalib, UPD_study and official repos (note: the main results table lists 22 method rows). **Unified setup**: 256×256 inputs, 200 epochs, batch 16, pretrained weights when available, ImageNet normalization, horizontal-flip augmentation only, no per-dataset tuning. Object/patient-level scores aggregate the **mean of the top 20% patch scores**; metric is ROC-AUC (PR-AUC also reported). **Three experiments**: (1) **scale** — predict a region either from one downsampled large patch or from tiled small patches aggregated; (2) **unbiased epoch selection** — four strategies: ① sample-wise maximal ratio (Reiss et al.: each checkpoint's score normalized by the mean normal-validation score, take the max), ② best AUC on a complete validation set with anomalies (an upper bound), ③ minimum normal-validation loss, ④ last epoch; (3) **normal/abnormal reversal** — swap the definitions on the synthetic density data and rerun.

## Data
**Real pathology (3)**: Camelyon16 breast lymph-node metastasis (768×768 patches at 40×; train 5462 normal; val 2150 normal + 2169 tumour; test 4000 normal + 817 tumour); an in-house Crohn's disease colon biopsy set (16 CD patients + 53 healthy controls, 20×, 1812×1812 patches labelled normal/abnormal by pathologists, re-tiled to 512×512); a mouse glomerulus set (40× H&E, centre crops at 3072×3072 and 512×512; a patch is normal only if every glomerulus in it is normal; the paper describes it as "benign and malignant glomeruli of mice"). **Synthetic pathology (2)**: patterns overlaid on 56 normal 2048×2048 Unitopatho patches — circles vs crosses (morphology) and 75% vs 25% circle density (density), each at two scales. **Industrial (2)**: MVTec Hazelnut (object) and Tile (texture) as reference. Training sets contain only normal data.

## Key results
- **No universal winner**: Reverse Distillation, SkipGanomaly, UniAD and others are well above average on some datasets and nearly fail on others.
- **By family** (complete-validation epoch selection, object-level mean ROC-AUC): feature distribution **0.692** > distillation **0.600** > reconstruction **0.564**; reconstruction methods often reconstruct anomalies well while blurring normal images.
- **Difficulty gap**: dataset-averaged ROC-AUC is 0.888 on industrial, 0.636 on synthetic pathology and 0.645 on real pathology — methods that work on industrial data do not suffice for pathology. PANDA is the most robust on real pathology (0.882 mean under complete-validation selection; 0.943 on Camelyon16, 0.990 on colon at 2048).
- **Epoch selection**: overall ranking complete-val > sample-wise > min-loss > last; "last epoch" is worst in 19 of 20 dataset settings. Both unbiased strategies (sample-wise, min-loss) need no anomalies; sample-wise is slightly better but stores N checkpoints and costs N× inference.
- **Scale**: glomeruli favour the small scale (0.650 vs 0.611; small patches resolve intraglomerular detail); colon favours the large scale (0.767 vs 0.640; crypt architecture and inflammation need context); the synthetic data agree — morphology anomalies prefer small scale, density anomalies large scale. Internal multi-scale features do not replace choosing the input scale.
- **Reversal**: on the same test images, "high density = normal" averages 0.792 while "low density = normal" reaches only 0.551 — **how learnable the normal pattern is** governs AD difficulty.

## Contributions
- The first unified AD benchmark dedicated to pathology covering 23 methods across five families, plus a review of pathology-AD literature.
- Makes "how to choose an epoch without anomalies" an explicit experimental variable — a practical problem almost nobody had examined systematically.
- Controlled synthetic pathology (morphology vs density, two scales, reversible definitions) that disentangles scale, anomaly type and normal-pattern difficulty.
- Clinically oriented advice: ensemble several detectors and flag consistently high-scoring regions, show heatmaps, and migrate toward supervised models as anomalies accumulate.

## Limitations
- All methods use default hyperparameters with no per-dataset tuning; the authors concede this leaves the causes of between-method differences unexplained.
- Inputs are uniformly resized to 256×256, limiting large-scale training patches; and no pathology foundation-model features (UNI, Virchow, …) are tested as backbones, so the conclusions mainly concern ImageNet-era methods.
- Only three real datasets, two in-house (Vanderbilt DUA required), and the glomerulus set is murine; only patch/object-level classification, no pixel-level localization evaluation.
- The "complete validation" strategy needs anomalies distributed like the test set — unavailable in practice — so it is only an upper bound.

## Relation to our direction
This is the **methodological benchmark textbook** for the detect stage on pathology images, and it comes straight from a kidney-pathology group (funding includes a KPMP Glue Grant; data include glomeruli). Four pieces transfer directly to **Plan A (kidney-omics AD + KidneyAnomalyBench)**: **(1) unbiased epoch selection** — our 95-biopsy models train only on normal/reference tissue and the validation set has no expert-confirmed anomalies either, so "sample-wise maximal ratio" and "minimum normal loss" are protocol-ready choices and "last epoch" should be explicitly disallowed; **(2) scale is a first-class variable** — glomerular lesions need small scale, interstitial fibrosis/inflammation large scale, so KidneyAnomalyBench should report per anatomical unit (glomerulus, tubule, interstitium) rather than one global AUC; **(3) the reversal experiment exposes "learnability of normal"** — normal kidney is itself heterogeneous (cortex/medulla, tubular segments), so how the reference set is built directly drives detection rates and must be controlled when designing healthy references; **(4) controlled synthetic anomalies** — porting "known-ground-truth synthetic perturbations" to Xenium/snRNA (e.g. injected expression shifts or cell-density changes) gives the benchmark a layer with ground truth. Most important is what it **does not answer**: it is H&E-only and cannot separate stain/sectioning artifacts from true lesions, which is exactly Plan A's core hypothesis — use **cross-modal agreement** between H&E and spatial omics to make that call — so these single-modality results serve as the baseline a cross-modal method must beat. For Plan B the lesson is indirect: "no universal method + default hyperparameters" means an agent that runs one AD method at one scale with the last epoch should have its conclusions flagged low-confidence by a verifier.

## Reusable assets
- **Code and synthetic data:** HRLB's PathAnomalyDetect repo (the paper states code and simulation data will be released).
<https://github.com/hrlblab/PathAnomalyDetect>
- **Method implementations:** the anomalib and UPD_study unified libraries.
<https://github.com/openvinotoolkit/anomalib> · <https://github.com/iolag/UPD_study>
- **Eval protocol:** four epoch-selection strategies + top-20% mean aggregation + multi-scale comparison + normal/abnormal reversal — portable wholesale into KidneyAnomalyBench.
- **Data:** Camelyon16 is public; the colon and glomerulus sets require a Vanderbilt DUA.

## Follow-ups
- MedIAnomaly (`medianomaly-media-2025` in this repo) — the sister benchmark across five modalities, complementary to this one.
- Reiss et al.'s PANDA and Cui et al.'s earlier epoch-selection work, for the rationale of the sample-wise maximal-ratio strategy.
- Rerun this benchmark with pathology foundation models (UNI2-h, Virchow) as feature-distribution backbones — the gap here most relevant to us.

## Cite
```bibtex
@article{Cui_2025, title={Quantitative benchmarking of anomaly detection methods in digital pathology images}, volume={1}, ISSN={3049-477X}, url={http://dx.doi.org/10.1088/3049-477x/ae0f9f}, DOI={10.1088/3049-477x/ae0f9f}, number={1}, journal={Machine Learning: Health}, publisher={IOP Publishing}, author={Cui, Can and Zheng, Xindong and Deng, Ruining and Liu, Quan and Yao, Tianyuan and Wilson, Keith T and Coburn, Lori A and Landman, Bennett A and Yang, Haichun and Wang, Yaohong and Huo, Yuankai}, year={2025}, month=Oct, pages={010502} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

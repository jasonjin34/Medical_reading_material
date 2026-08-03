# Boehringer-Ingelheim/anomaly-detection-in-histology

> **Bibkey** `histo-anomaly-bi-repo` · **Venue** GitHub (2022) · **Category** histopath · **Relevance** medium · **Access** open
> **Link** <https://github.com/Boehringer-Ingelheim/anomaly-detection-in-histology> · `status: complete`

---

## One-liner
An open-source PyTorch repo from Boehringer Ingelheim that learns representations from healthy tissue only, then applies one-class classifiers to flag drug-induced histological anomalies in whole-slide images. Companion code to Zingman et al., *Medical Image Analysis* 2024.

## Problem
In drug-development toxicity assessment, abnormal/lesion samples are scarce and cannot be exhaustively labeled, so supervised classification fails. The goal is to learn a discriminative representation from abundant healthy tissue alone so that any deviation from "normal" is detectable, enabling early-stage compound toxicity screening.

## Method
Two stages. (1) Representation learning: a CNN (EfficientNet-B0, 320px input) is trained on healthy tissue with an auxiliary task of discriminating species/organ/staining — labels obtained automatically from metadata, no extra annotation — plus a center-loss term to make same-class features compact and anomaly-friendly. (2) Detection: a one-class SVM is fit on deep features to score new slides. Supports H&E and Masson's Trichrome. Entry points: `train_cnn.py`, `anomaly_detector.py`, `model_use_example.py`; configs under `configs/`.

## Data
Training on healthy tissue spanning multiple species, organs, and stains. Evaluation on normal mouse liver vs. NAFLD pathology (a published liver-anomaly dataset). Data hosted on OSF: <https://osf.io/gqutd/>.

## Key results
Liver anomaly detection: H&E — balanced accuracy 94.20%, AU-ROC 97.33%, F1 94.09%; Masson's Trichrome — 97.51% / 99.03% / 97.51%. The paper reports it beats established anomaly-detection baselines and matches methods purpose-built for liver-lesion quantification.

## Contributions
- Auxiliary task built from free healthy-sample metadata (species/organ/stain) — representation learning with zero extra labels.
- Center-loss regularization + one-class SVM combination markedly improves lesion detection.
- Fully reproducible package: code + OSF data + checkpoints + eval scripts, MIT-licensed.

## Limitations
- Validation centers on liver (mouse liver / NAFLD); transfer to other organs/lesion types not demonstrated here.
- Outputs an anomaly score only — no localization of driving genes/pathways; not generative and not invertible.
- Relies on patch-level CNN features at fixed 320px and two stains; new stains/scanners likely need retraining.

## Relation to our direction
Maps squarely onto **stage 1: anomaly detection**. It is a clean, industrially validated instance of the "learn-normal, flag-deviation" paradigm on histopathology — exactly our approach for detecting disease/drug-perturbed regions. Reusable: (a) the metadata-driven auxiliary-task representation trick, portable to our own histopath/spatial-omics normal atlases; (b) the center-loss + one-class scoring protocol as a baseline. It stops at scoring — no virtual-tissue modeling, no gene-revert prediction — so stages 2–3 must be layered on top of its detected regions. Best used as a histopath-modality baseline and engineering template.

## Reusable assets
- MIT-licensed repo with training, detection, and feature-extraction scripts + configs.
- Pretrained CNN weights (`.pt`) and one-class SVM classifiers (`.pkl`).
- OSF dataset <https://osf.io/gqutd/> (normal mouse liver + NAFLD eval set).
- Eval protocol (balanced accuracy / AU-ROC / F1) reusable as an anomaly-detection benchmark.

## Follow-ups
- Read the companion paper (DOI 10.1016/j.media.2023.103067; arXiv:2210.07675) for center-loss ablations and baseline comparisons.
- Test swapping the CNN for a pathology foundation model (UNI/CONCH/Virchow) as the feature extractor.
- Explore coupling detected anomaly patches with spatial transcriptomics toward the virtual-tissue / gene-revert stages.

## Cite
```bibtex
% no BibTeX fetched
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

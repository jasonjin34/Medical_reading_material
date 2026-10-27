<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# AI-Based Anomaly Detection for Clinical-Grade Histopathological Diagnostics

- **Authors:** Dippel, Jonas; Prenißl, Niklas; Hense, Julius; Liznerski, Philipp; Winterhoff, Tobias; Schallenberg, Simon; Kloft, Marius; Buchstab, Oliver; Horst, David; Alber, Maximilian; Ruff, Lukas; Müller, Klaus-Robert; Klauschen, Frederick
- **Venue / Year:** NEJM AI · 2024 (Vol. 1, No. 11)
- **DOI:** 10.1056/AIoa2400468
- **URL:** https://doi.org/10.1056/aioa2400468
- **Bibkey:** Dippel_2024
- **Status:** complete — read from the authors' open arXiv preprint (arXiv:2406.14866v1, 21 Jun 2024). The NEJM AI version of record is paywalled; its wording and numbers may differ slightly.

## Abstract (arXiv preprint, verbatim)
While previous studies have demonstrated the potential of AI to diagnose diseases in imaging data, clinical implementation is still lagging behind. This is partly because AI models require training with large numbers of examples only available for common diseases. In clinical reality, however, only few diseases are common, whereas the majority of diseases are less frequent (long-tail distribution). Current AI models overlook or misclassify these diseases. We propose a deep anomaly detection approach that only requires training data from common diseases to detect also all less frequent diseases. We collected two large real-world datasets of gastrointestinal biopsies, which are prototypical of the problem. Herein, the ten most common findings account for approximately 90% of cases, whereas the remaining 10% contained 56 disease entities, including many cancers. 17 million histological images from 5,423 cases were used for training and evaluation. Without any specific training for the diseases, our best-performing model reliably detected a broad spectrum of infrequent ("anomalous") pathologies with 95.0% (stomach) and 91.0% (colon) AUROC and generalized across scanners and hospitals. By design, the proposed anomaly detection can be expected to detect any pathological alteration in the diagnostic tail of gastrointestinal biopsies, including rare primary or metastatic cancers. This study establishes the first effective clinical application of AI-based anomaly detection in histopathology that can flag anomalous cases, facilitate case prioritization, reduce missed diagnoses and enhance the general safety of AI models, thereby driving AI adoption and automation in routine diagnostics and beyond.

## Digest of the preprint (all facts from arXiv:2406.14866v1)

**Method.** H&E WSIs → 340×340-px patches at 20× (~0.5 µm/px), >80%-background patches dropped, Reinhard stain normalisation (App. B.4). Separate models for stomach and colon; "normal" = frequent-finding patches; low-grade adenomas excluded from training (§2.2). Paradigms: (a) CTransPath features (Swin Transformer pretrained on 32,220 TCGA + PAIP slides) + modified kNN; (b) CTransPath fine-tuned with a one-class (PANDA-style) loss + kNN; (c) **Outlier Exposure** — binary cross-entropy classifier, normal patches vs auxiliary anomalies (2,901 other-organ Charité slides plus normal patches of the other GI organ), class-balanced batches, OE sampled 50% near / 50% far tissue, OE patches with cosine similarity >0.9 to normal removed (§2.3, App. B.2). Main OE results use CTransPath fine-tuned on the OE task; a ResNet-18 from scratch is comparable (App. D.4, Table 15). Patch score = anomaly-class probability averaged over 10 test-time augmentations; slide score = mean of top-10% patch scores; heatmaps from 75-px-overlap patches with averaged scores (§2.2, App. B.3).

**Data.** 5,423 slides, ~17M patches. Charité: 1,973 frequent-finding slides (stomach 961, colon 1,012) + 200 anomalous slides, 65 diagnoses, 3DHistech P1000 scanner; 2,901 auxiliary OE slides. LMU Munich external cohort: 192 gastric + 157 colon slides, Leica Aperio GT 450 scanner (§2.1, §3.3, App. B).

**Results.** Charité OE: slide-AUROC 95.04% (stomach) / 91.01% (colon); patch-AUROC 91.37% / 90.47% (Table 1). Malignant group slide-AUROC 97.72% / 96.97%. At 100% sensitivity, 36.2% of stomach and 4.21% of colon cases are called not abnormal (22.29% for colon excluding pseudomelanosis coli and spirochaetosis) (§3.1). LMU, no retraining: 94.5% / 85.88% slide-AUROC (App. Table 4). Autoencoder baseline 63.73% / 65.58% slide-AUROC (App. Table 10). OE with ImageNet fails (colon slide-AUROC 52.17%) (App. Table 11). Performance saturates around 100 training slides (App. D.1).

**Code / data.** The preprint gives no code or data link.

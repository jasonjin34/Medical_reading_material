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
- **Status:** abstract-only (NEJM AI paywalled; abstract + details below sourced from the public arXiv preprint arXiv:2406.14866 and the authors' institutional press release)

## Abstract
While previous studies have demonstrated the potential of AI to diagnose diseases in imaging data, clinical implementation is still lagging behind. This is partly because AI models require training with large numbers of examples only available for common diseases. In clinical reality, however, only few diseases are common, whereas the majority of diseases are less frequent (long-tail distribution). Current AI models overlook or misclassify these diseases. We propose a deep anomaly detection approach that only requires training data from common diseases to detect also all less frequent diseases. We collected two large real-world datasets of gastrointestinal biopsies, which are prototypical of the problem: the ten most common findings account for roughly 90% of cases, while the remaining 10% contain 56 disease entities, including rare cancers. Our best anomaly detection model reliably detected a broad spectrum of rare pathologies — including primary and metastasizing cancers — that it had never seen during training. The approach generalized across scanners and hospitals, and points to a workflow in which normal/common cases can be automatically cleared or prioritized, reducing missed diagnoses.

_(Wording of the NEJM AI version of record may differ slightly; the above is the preprint abstract with detail added from public sources.)_

## Full text / Extract
<!-- Full cleaned text for open-access; for paywalled leave the note below. -->
> status: abstract-only — NEJM AI version of record is behind a paywall. The publicly available preprint (arXiv:2406.14866) and press release supply the method/data/results digest below. Drop `source.pdf` into this folder and re-run extraction to enrich with the full version of record.

### Public method / results digest (from preprint + press release)

**Problem framing.** Supervised pathology classifiers need many labeled examples per disease class, but clinical disease is long-tailed. The paper reframes diagnosis as anomaly detection: learn only "normal / common", flag any deviation for human review — no rare-disease training data required.

**Method.** Compared paradigms:
- Self-supervised features + distance scoring: patch embeddings from the pathology foundation model **CTransPath** (SwinTransformer pretrained on 32,220 TCGA/PAIP H&E slides), scored with a modified k-nearest-neighbors (kNN) algorithm; alternatively fine-tuned with a one-class classification loss.
- **Outlier Exposure (OE)** — best method: a binary classifier trained with cross-entropy to separate normal gastrointestinal patches from auxiliary out-of-domain tissue patches; anomaly score = predicted probability of the anomaly class. Backbone **ResNet-18** (random initialization performs on par with fine-tuned CTransPath).
- Slide-level score = mean of the top-10% highest-scoring patches. Anomaly **heatmaps** produced by spatially averaging scores of overlapping patches, giving a smooth localization map for pathologist confirmation.

**Data.** Two real-world gastrointestinal biopsy datasets: ~17 million H&E histological images across 5,423 cases. Top-10 common diagnoses ≈ 90% of cases; remaining 10% span 56 disease entities including rare primary and metastatic cancers. Primary cohort: Charité. External validation: LMU Munich (different scanner, no retraining). Multi-scanner, multi-hospital.

**Results.**
- Charité — Stomach: slide-AUROC 95.04%, patch-AUROC 91.37%. Colon: slide-AUROC 91.01%, patch-AUROC 90.47%.
- Automation at 100% sensitivity (no missed anomaly): 36.2% of normal stomach cases and 4.21% of normal colon cases can bypass review.
- External validation (LMU, new scanner, no retraining): stomach slide-AUROC 94.5%, colon slide-AUROC 85.88%.
- Press-release framing: AI can automatically handle roughly 25–33% of cases (normal/common) and prioritize the remainder to reduce missed diagnoses; colored heatmaps mark anomaly locations for pathologist review.

**Code / data.** No official code or dataset release link identified; Charité/LMU clinical data are access-restricted. Authors affiliated with TU Berlin / Aignostics (Ruff, Müller, Alber, Klauschen).

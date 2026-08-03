<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# Deep learning-based pathomics signature predicts prognosis and treatment response in gastric cancer: a multicenter retrospective study

- **Authors:** Wang, Hao; Li, Hao; Ma, Keru; Mo, Genshen; Yan, Meihong; Zhang, Xinyue; Xie, Haonan; Huang, Yuze; Li, Huiying; Xue, Yingwei; Han, Peng; Lou, Shenghan
- **Venue / Year:** npj Precision Oncology · 2026
- **DOI:** 10.1038/s41698-026-01381-6
- **URL:** https://doi.org/10.1038/s41698-026-01381-6
- **Bibkey:** Wang_2026
- **Status:** complete

## Abstract
The existing TNM staging system provides insufficient prognostic information in gastric cancer (GC) patients. This study aims to establish a pathomics signature of GC (PSGC) that uses deep learning (DL) to directly analyze H&E slides for predicting GC outcomes. We propose a multi-scale graph neural network with gated attention mechanism for multi-instance learning (MS-GMIL) for the construction of PSGC. Moreover, transcriptomic data investigated the possible pathophysiological mechanisms of the PSGC. The PSGC was identified as an independent prognostic factor in all cohorts. Patients with stage II and III GC, along with a high PSGC, showed considerable benefits from chemotherapy and an effective response to immunotherapy. The primary histological features underlying the PSGC were tumor cell anaplasia, intraepithelial neoplasia, tumor-stroma fibrosis, and intestinal epithelial metaplasia. Moreover, the PSGC was associated with cell cycle regulation, drug resistance pathways, and mechanisms of cancer progression. The PSGC functions as a valuable tool in clinical decision-making for the management of GC, providing insights into the underlying pathogenic mechanisms.

## Full text / Extract
<!-- Full cleaned text for open-access; for paywalled leave the note below. -->
> status: abstract-only — full text behind paywall (npj Precision Oncology). Body not fetched; below are additional publicly visible details from the Nature landing page and indexed metadata. Drop `source.pdf` into this folder and re-run extraction to enrich.

### Publicly visible details (landing page / indexed metadata)
- **Cohort scale:** 3,138 patients across a multicenter retrospective design; median age 60 years; 71.64% (2,248/3,138) male. Multiple cohorts (training + validation) — the PSGC was an independent prognostic factor in *all* cohorts.
- **Model:** MS-GMIL = multi-scale graph neural network with a gated attention mechanism for multiple-instance learning (MIL). It operates directly on whole-slide H&E images (weakly supervised, slide-level labels) to predict overall survival (OS).
- **Signature:** an interpretable pathomics signature (PSGC) built from **11 features** derived from the digital H&E slides. Traditional machine learning is combined with the MS-GMIL deep features to construct the final signature.
- **Interpretation:** Shapley Additive exPlanations (SHAP) and pathogenomics analyses were used to interpret the PSGC. The primary histological features underlying the PSGC were tumor cell anaplasia, intraepithelial neoplasia, tumor-stroma fibrosis, and intestinal epithelial metaplasia.
- **Mechanism (transcriptomics):** PSGC was associated with cell cycle regulation, drug resistance pathways, and mechanisms of cancer progression.
- **Treatment response:** Stage II and III GC patients with high PSGC showed considerable benefit from chemotherapy and effective response to immunotherapy.
- **Availability:** Data/code availability statements not visible without full-text access.

> Note: specific discrimination metrics (C-index, HR, AUC, p-values) for individual cohorts are not visible on the public landing page and are not reproduced here.

<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# An artificial intelligence model to detect abnormal ejection fraction from non-contrast chest computed tomography: the CT–LVEF study

- **Authors:** Raikhelkar, Jayant; Bai, Zilong; Beecy, Ashley N; Richter, Ilan; Liu, Fengbei; Nizam, Nusrat Binta; Kishore, Varsha; Kelsey, Chris; vanMaanen, David; Ruhl, Jeffrey; Tesfuzigta, Naomi; Lancet, Erica; Leb, Jay; Legasto, Alan; Elias, Pierre; Poterucha, Timothy; Kumaraiah, Deepa; Prince, Martin; Wang, Fei; Sayer, Gabriel; Estrin, Deborah; Sabuncu, Mert; Uriel, Nir
- **Venue / Year:** European Heart Journal - Digital Health · 2026
- **DOI:** 10.1093/ehjdh/ztag088
- **URL:** https://doi.org/10.1093/ehjdh/ztag088
- **Bibkey:** Raikhelkar_2026
- **Status:** complete

## Abstract
Abstract
                  
                    Aims
                    Heart failure (HF), a major global health challenge, affects millions worldwide and poses substantial healthcare and economic burdens. It is estimated that a large proportion of those with early systolic dysfunction remain asymptomatic at a stage when guideline-directed medical therapies have been shown to prevent disease progression. To develop an artificial intelligence (AI) model capable of predicting abnormal left ventricular ejection fraction (EF) directly from static, non-gated, non-contrast chest computed tomography (CT) scans as a form of opportunistic screening,
                  
                  
                    Methods and results
                    Using a multi-institutional dataset of 34 058 paired non- contrast CT images and echocardiogram reports from two academic centres, we trained our model of classification for predicting left-ventricle ejection fraction (LVEF) categories: abnormal EF (EF &amp;lt; 50%) vs. normal on 25 948 studies. We validated the model on 8110 paired chest CT and echocardiogram results from a separate institution. The model achieved an area under the receiver operating characteristic (AUROC) curve of 0.786 on the hold-out test set and 0.762 on external validation to detect an abnormal EF (&amp;lt;50%). Beyond strong predictive performance, the AI model surpassed expert radiologists in both accuracy and efficiency and provided interpretable visualizations highlighting imaging features linked to reduced LVEF.
                  
                  
                    Conclusion
                    In this study, we developed and validated an AI model capable of predicting abnormal LVEF directly from static, non-gated, non-contrast chest CT scans, a novel application for an imaging modality typically used for unrelated indications as a form of opportunistic screening. This technology holds significant promise for early detection of systolic HF, reducing the diagnostic gap, and improving outcomes in asymptomatic HF patients.

## Full text / Extract
<!-- Full cleaned text for open-access; for paywalled leave the note below. -->
> status: abstract-only — full text behind the OUP paywall. Drop `source.pdf` into this folder and re-run extraction to enrich. Below is public content gathered from the article landing page (abstract, publicly visible results, and technical details); the full Methods/Results body is not reproduced.

### Publicly visible details (from landing page, not the full paywalled text)

**Task.** Binary classification: abnormal LVEF (EF < 50%) vs. normal, predicted directly from static, non-gated, non-contrast chest CT as opportunistic heart-failure screening.

**Model / architecture.** Adapts a pretrained vision transformer using the CT-ViT encoder. Inputs are 3D CT volumes resampled to 164 × 164 × 164 voxels, normalized to 2 × 2 × 2 mm resolution.

**Data.** Multi-institutional dataset of 34,058 paired non-contrast CT + echocardiogram-report studies from two academic centers. Trained on 25,948 studies (with a hold-out internal test set); externally validated on 8,110 paired CT + echo results from a separate institution. Internal validation = Columbia University; external validation = Weill Cornell.

**Key results.**
- Internal (Columbia) hold-out: AUROC 0.786, F1 0.822.
- External (Weill Cornell) validation: AUROC 0.762, F1 0.812.
- Reader study on 90 Columbia scans: model F1 0.808 vs. thoracic-radiologist F1 0.646–0.802; model ~1 min/scan vs. 2+ min per scan for radiologists.

**Interpretability.** Grad-CAM visualizations localized clinically recognizable features associated with reduced LVEF: enlarged heart, ascending aorta (especially when calcified), dilated superior vena cava, presence of a pacemaker, and pulmonary-edema infiltrates.

**Clinical framing.** A substantial number of patients with early systolic dysfunction remain undiagnosed despite evidence that early guideline-directed medical therapy prevents disease progression; the model aims to close this diagnostic gap using scans already acquired for unrelated indications.

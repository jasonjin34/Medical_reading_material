# A multimodal and temporal foundation model for virtual patient representations at healthcare system scale

> **Bibkey** `Zhang2026_260418570` · **Venue** arXiv preprint (2026) · **Category** ehr · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2604.18570> · `status: complete`

---

## One-liner
APOLLO (Mahmood lab): a multimodal temporal Transformer pretrained with masked modelling on 33 years of records from 17 Mass General Brigham hospitals — **7.2M patients, 25.3B medical events, 28 modalities** (structured codes, labs, vitals, medications, note and report text, pathology/blood-smear images) — compressing a whole care journey into a "virtual patient" embedding. Frozen embeddings with a linear Cox head substantially beat an age–sex baseline across 261 prognostic and 61 retrieval tasks on a 1.4M-patient test set.

## Problem
The EHR is medicine's system of record, but its data are fragmented across modality silos and are high-dimensional, sparse and irregularly sampled. Existing longitudinal EHR foundation models mostly use **structured data only** (codes, labs), thanks to ontologies and discrete-token modelling, whereas progression detail, clinical reasoning and novel biomarkers often live only in free text and images. Prior work also leans on heavily curated public datasets (e.g. MIMIC-IV, ICU only). The question: on **real, uncurated, all-department** health-system data, can the full longitudinal record — structured + text + images — be unified into one time-aware patient representation that generalizes across onset, progression, treatment response, adverse events and hospital operations? The authors explicitly draw the analogy to the "virtual cell": unified multimodal representations capturing system dynamics.

## Method
**Tokenization**: structured data → discrete tokens (each ICD diagnosis and RxNorm ingredient is a token; numeric measurements become (code, quantile-bin) tokens; categorical ones (code, canonical-category) tokens), **235,768** learnable structured tokens in total; vitals/flowsheet names are harmonized to LOINC classes with Qwen-32B. **Unstructured** data use frozen off-the-shelf encoders: all clinical text with **GatorTron-base** (long notes chunked and averaged); whole-slide images with **TITAN**; blood smears with **DinoBloom**; electron-microscopy and gross images with **CONCHv1.5**; non-pathology imaging via its report text only. **Architecture**: modality-specific projections into a shared space; prepended demographic tokens (age at last event, sex, ethnicity) and a CLS token; per-event patient age as the time encoding; encoder–decoder. **Pretraining**: **masked token modelling with modality-specific masks** (the mask token tells the head which modality to reconstruct); contiguous 1,536-event windows per step; AdamW, 30,000 iterations, 8×A100. **Inference**: append the last time step plus a modality mask token; its hidden state is the patient embedding — the diagnosis mask for most tasks, text or image masks for retrieval. **Downstream**: frozen embeddings → PCA → Cox proportional hazards (time-to-event with right-censoring), time-dependent AUROC at a fixed threshold duration; comparator is an **age+sex Cox model**. **Interpretability**: patient-level leave-one-token-out (LOTO) sensitivity; population-level Integrated Gradients on pre-Transformer inputs.

## Data
**MGB-7M**: Mass General Brigham, 1992–2025; 7,155,044 patients, 25,296,943,893 events, 28 modalities, 12 major specialties — 22.9B flowsheet entries, 1.44B labs, 505M vitals, 159M progress notes, 78M diagnostic reports, 1.16M images (incl. haematology and histopathology). All 14 ATC chapters and all ICD chapters covered. 75:5:20 train/val/test split; **all downstream tasks drawn from the 1.43M-patient test set**. Downstream: 95 new-onset tasks (≥60k patients each, 157–27,503 events), 78 progression, 59 treatment-response, 17 adverse-event, 12 hospital-operations tasks, and 61 retrieval cohorts. Data shared case-by-case only, under institutional review and an MTA.

## Key results
- **New onset (95 tasks)**: significantly better than age–sex on 74/95 (p<0.05); 1-year all-cause mortality AUROC **0.92**; 3-year heart failure 0.77→**0.88**; 1-year acute MI 0.68→0.82; 3-year **type 2 diabetes 0.61→0.85**; 1-year gout 0.74→0.83; 1-year schizophrenia 0.65→0.92.
- **Progression (78 tasks)**: 53/78 significant; cardiovascular average 0.65→0.75; **hypertension→heart failure at 5 years 0.75→0.86**; 3-year survival after stroke 0.72→0.84; after aortic stenosis 0.72→0.83; asthma exacerbation 0.57→0.83; melanoma 3-year survival 0.71→0.87.
- **Treatment response (59 tasks)**: 30/59 significant; endocrine drugs average 0.57→0.80; stroke-free survival on apixaban for AF 0.69→0.81; MACE-free survival on losartan/amlodipine for hypertension 0.80/0.79; trastuzumab 0.66→0.93.
- **Adverse events (17 tasks)**: 12/17 significant; **AKI after NSAIDs 0.80→0.91**; GI bleeding after NSAIDs 0.80→0.91; treatment-emergent T2D after corticosteroids 0.70→0.87.
- **Hospital operations (12 tasks, balanced accuracy)**: 9/12 significant; **in-hospital dialysis dependence 0.65→0.97**; **acute kidney failure 0.64→0.80**; sepsis 0.66→0.79; 30-day readmission 0.54→0.62.
- **Ablation (neoplasm progression set, 28 tasks in the Results text)**: APOLLO mean AUROC **0.735**; structured-only 0.71 (multimodal +0.025); same architecture supervised per task 0.626; latest progress-note embedding 0.615; age–sex 0.619 — pretraining, multimodality and temporal context each matter.
- **Retrieval**: Acc@5 above the latest-progress-note baseline on all 61 cohorts; retrieves a kidney-transplant patient lacking the Z94.0 code; supports natural-language inclusion criteria and an external TCGA slide as queries.
- **Interpretability**: one patient's 3-year CKD risk rises after hypertension, dyslipidaemia and T2D are documented and jumps again when eGFR falls to the low 50s; IG for heart failure→acute kidney failure highlights obesity, post-procedural states and ageing proxies; the authors treat attributions as associative, not causal.

## Contributions
- The first health-system-scale foundation model unifying the **full longitudinal record (structured + text + images, 28 modalities)** into a time-aware patient representation.
- Frozen off-the-shelf unimodal encoders + a trained temporal Transformer: raw data never enter the final model (lower PHI-leakage risk) and compute stays feasible.
- **Modality-specific masks as prompts**: one model yields diagnosis-, text- or image-tuned patient embeddings, enabling cross-modal retrieval.
- A 322-task evaluation framework (all time-to-event, with calibration).

## Limitations
- **Single health system** (MGB, shared Epic instance, US northeast): within-system generalization only, no external validation — given CancerRiskNet's cross-system drop, this is the biggest unknown.
- **Only an age–sex comparator**: no head-to-head against ASCVD, CHA₂DS₂-VASc, Framingham or other EHR foundation models.
- Observational, associational predictions; "treatment response" is prognostic stratification within a treated cohort and **cannot say which drug is best for a patient** (the authors flag the counterfactual task as open).
- Frozen encoders and naive averaging of long notes; no wearables/lifestyle.
- Preprint; code only "upon publication", data not public.

## Relation to our direction
**For the Sinai EHR project APOLLO is the upper-bound reference for "what if we used every Sinai modality"**: its scale (7.2M patients) matches Sinai's millions, on equally real, uncurated US academic health-system data, so its engineering choices map almost one-to-one — quantile-bin tokens for lab values, LLM harmonization of local flowsheet names to LOINC, frozen text/pathology encoders, modality masks as prompts, Cox time-to-event evaluation throughout. Delphi and CancerRiskNet use diagnosis codes only; together the three form a "codes-only → multimodal" gradient that the Sinai project can climb step by step, quantifying each step's gain (APOLLO's ablation shows multimodality adds only +0.025 AUROC over structured-only, while pretraining vs supervised differs by 0.109 — **pretraining scale matters more than modality count**, a direct input to early Sinai priorities). **Highly relevant to cardiometabolic-kidney disease**: many of its strongest results are kidney or cardiometabolic endpoints — dialysis dependence (0.97 balanced accuracy), acute kidney failure, AKI after NSAIDs, hypertension→heart failure, new-onset T2D, heart failure→acute kidney failure, and a CKD risk-trajectory example — precisely the endpoint set the lab's Novo-funded cardiometabolic-kidney foundation models/agents should cover, usable as a Sinai task list with target numbers. **On detect → model → revert**: the authors themselves invoke the virtual cell and call this a "virtual patient" — patient-scale "model"; it also embeds slides with TITAN/CONCH, the same encoder family (Mahmood lab) as Plan A's H&E side. **What it does not do is revert**: the authors state treatment-response prediction is not counterfactual and cannot say which drug to switch to — the missing causal interface between tissue-scale perturbation/reversion modelling and the EHR-scale virtual patient. For Plan B: the auditable LOTO + IG explanations, and the authors' sorting of attributions into "association / care-process proxy / hypothesis-generating", translate directly into an evidence-grading scheme for agents drawing conclusions from EHR.

## Reusable assets
- **Code:** pretraining and evaluation pipeline (risk prediction, retrieval) to be released for academic use "upon publication"; not yet public.
- **Data:** MGB-7M not public; case-by-case with an MTA.
- **Directly usable encoders:** GatorTron-base (clinical text), TITAN (WSI), CONCHv1.5, DinoBloom (blood smears).
- **Task definitions:** Extended Data Tables 6–17 list endpoints, threshold durations and sample sizes for all 322 tasks — a template task list for Sinai.
<https://arxiv.org/abs/2604.18570>

## Follow-ups
- The full kidney/cardiometabolic rows of Extended Data Tables 7–15 (CKD, dialysis, AKI, heart failure).
- The other longitudinal EHR foundation models cited (refs 25–35) — look for ones with external validation or head-to-head clinical-score comparisons.
- The TITAN paper (multimodal whole-slide foundation model), to compare against this repo's pathology foundation-model entries.
- Track whether the published version adds external validation and code.

## Cite
```bibtex
@misc{Zhang2026_260418570,
  title = {A multimodal and temporal foundation model for virtual patient representations at healthcare system scale},
  author = {Andrew Zhang and Tong Ding and Sophia J. Wagner and Caiwei Tian and Ming Y. Lu and Rowland Pettit and Joshua E. Lewis and Alexandre Misrahi and Dandan Mo and Long Phi Le and Faisal Mahmood},
  year = {2026},
  eprint = {2604.18570},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2604.18570}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

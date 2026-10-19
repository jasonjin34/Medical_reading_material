# Learning the natural history of human disease with generative transformers

> **Bibkey** `Shmatko_2025` · **Venue** Nature (2025) · **Category** ehr · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1038/s41586-025-09529-3> · `status: complete`

---

## One-liner
Delphi-2M turns GPT-2 into a **continuous-time, competing-risk generative model of multi-morbidity**: given a person's sequence of first ICD-10 diagnoses (1,256 diseases + death) plus sex/BMI/smoking/alcohol, it predicts both what the next event is and when it happens. Trained on 0.4M UK Biobank participants with only 2.2M parameters, it reaches an average age-stratified AUC of ~0.76 across >1,000 diseases, 0.67 on 1.93M Danish individuals with no parameter changes, and can sample synthetic health trajectories up to 20 years ahead.

## Problem
Disease progression is multimorbid and time-evolving, yet most risk models are single-disease (cardiovascular, one cancer); few algorithms predict the full spectrum of >1,000 top-level ICD-10 diagnoses. Hard parts of multimorbidity modelling: many diagnoses, temporal dependencies between events, heterogeneous data integration, and calibration. LLMs model language as token sequences generated one by one — disease histories are likewise "past events → future sequence". Can a GPT-style model learn the natural history of human disease while being calibrated, generative and externally valid?

## Method
GPT-2 via nanoGPT with three key changes: **(1) continuous age encoding** replacing discrete positional encoding (sin/cos bases, lowest frequency 1/365, followed by a trainable linear combination) — allowing arbitrary-length input; **(2) a second output head for time-to-next-event** under a **competing-exponential waiting-time model**: each token has rate λᵢ = exp(logitᵢ); P(next = j) = λⱼ/Σλᵢ (exactly softmax cross-entropy), and time to next event is exponential with rate Σλᵢ, so logits are interpretable as **daily incidence rates**; **(3) causal attention additionally masks tokens recorded at the same time**. Also: **"no event" padding tokens** inserted at ~1 per 5 years remove long empty gaps (and allow querying risk at any time at inference); sex, BMI (<22/22–28/>28), smoking and alcohol are input tokens excluded from the loss; lifestyle token times are randomized −20 to +40 years around enrolment to break spurious associations from immortal-time bias. A hyperparameter sweep reproduces scaling laws, with ~2M parameters optimal at UK Biobank scale; the chosen model has 120-d embeddings, 12 layers, 12 heads, **2.2M parameters**. Weight tying (input embedding = output projection) aids interpretation. Training: Adam, 200k iterations, batch 128, cosine LR 6e-4→6e-5. **Sampling**: draw the next disease from the softmax and the time as the minimum over exponentials, iterating to full trajectories. **Interpretability**: embedding UMAP, SHAP, attention maps.

## Data
**UK Biobank**: ~500k participants (recruited 2006–2010, aged 37–73); diseases from "first occurrence" data (category 1712, integrating primary care, hospital admissions, death registry, self-report) plus cancer registry (added by the authors), ICD-10 level 3, 1,256 diagnoses in total. Training 402,799 (80%), validation 100,639 (20%), longitudinal test on 471,057 alive on 1 July 2020 (incidence July 2021–July 2022, with a 1-year gap). **Danish external validation**: National Patient Registry (LPR) + cause-of-death registry; **1.93M** people aged 50–80 on 1 January 2016, 11.51M disease tokens from 1978–2016, evaluated on 2017 incidence (796 ICD-10 codes with ≥25 cases); ICD-8 mapped to ICD-10; no lifestyle data (treated as absent).

## Key results
- **Full-spectrum prediction**: average age-stratified next-event AUC **≈0.76** on internal validation; AUC > 0.5 for 97% of diagnoses; death AUC **0.97**; well calibrated in 5-year age bins.
- **Long horizon**: average AUC declines from 0.76 to **0.70** at 10 years, retaining long-term prognostic value.
- **Versus dedicated scores**: comparable to clinical scores for CVD and dementia (QRisk3, SCORE2, PREVENT, Framingham, UKBDRS), better than Charlson/Elixhauser for death; **worse than HbA1c alone for diabetes**; generally higher AUC than MILTON (67 blood biomarkers; 410 diseases comparable).
- **Generated trajectories**: conditioning on history up to age 60, 63,662 sampled trajectories recapitulate population incidence at ages 70–75; ~17% of disease tokens correct in year 1, <14% after 20 years (vs 12–13% from age and sex alone).
- **Training on synthetic data only**: a model trained exclusively on synthetic trajectories reaches AUC **0.74** on real validation data, only 3 points below the original — a less privacy-sensitive alternative.
- **External validation**: applied to Denmark with no changes, average AUC **0.67** (s.d. 0.09) vs 0.69 for UKB longitudinal testing; per-disease performance correlates at r = 0.76 (95% CI 0.72–0.80).
- **Interpretability**: embeddings cluster by ICD chapter without being told; both diabetes types cluster with retinal disorders and neuropathies; MI and septicaemia cluster with death. SHAP example: a run of digestive diagnoses raised one person's pancreatic cancer risk 19-fold. Cancer's effect on mortality decays with a multi-year half-life, septicaemia's much faster.
- **Biases**: the model learns the data-collection process — hospital-only diseases are predicted at ~10× higher rates in people with any other hospital record (septicaemia, 93% hospital-diagnosed, at 8×); UKB's healthy-volunteer bias, absence of pre-recruitment deaths (immortality bias) and sparse data beyond age 80 are all inherited.

## Contributions
- **Competing-exponential waiting-time head**: makes GPT's softmax double as an incidence model, yielding interpretable absolute rates rather than relative probabilities only.
- Continuous age encoding + same-time masking + no-event padding: a small, ablated set of changes turning a text GPT into a continuous-time event GPT.
- One model covering >1,000 diseases, **externally validated with zero tuning** in another country.
- **Generative**: sampling 20-year futures for population disease-burden projection; training downstream models on synthetic data.
- A candid bias analysis showing how the model "learns" data-source missingness patterns.

## Limitations
- First diagnoses plus a few lifestyle factors only; no labs, medications, imaging or text (listed as extensions; clearly inferior to HbA1c for diabetes).
- UKB biases: healthy volunteers, over-representation of white and affluent participants; no pre-recruitment deaths; sparse data beyond age 80.
- The model exploits data-source missingness (presence of hospital records); some associations are collection artefacts.
- The authors explicitly caution that temporally directed dependencies **must not be read as causal** levers for changing future health.
- Individual predictions are dominated by chance and compatible with many outcomes; clinical decision support still needs a regulatory framework.

## Relation to our direction
**For the Sinai EHR project this is the clearest paradigm of a patient-trajectory foundation model**: a small model (2.2M parameters) learns competing risks for >1,000 diseases from 0.4M people, while Sinai has millions of patients — by the scaling law reproduced here the optimal model at Sinai scale should be noticeably larger, itself a testable question. Directly borrowable design: (1) the **competing-exponential head** yields calibrated absolute incidences, ideal for modelling CKD stage progression, dialysis, heart failure, MI and death as **competing** endpoints simultaneously — the essence of cardiometabolic-kidney multimorbidity; (2) no-event padding enables risk queries at any time, i.e. risk trajectories; (3) its external-validation discipline (zero-tuning transfer plus per-disease performance correlation). **The explicit gap is Sinai's opportunity**: Delphi loses to HbA1c for diabetes, so for metabolic-kidney endpoints **lab values (HbA1c, eGFR, UACR) and medications (SGLT2i, GLP-1RA, RAS inhibitors) must become tokens** — Sinai's EHR has them, UKB first-occurrence data does not. For the lab's Novo-funded cardiometabolic-kidney agents, a Delphi-style model can be a **numerical prediction tool the agent calls** (the authors themselves propose LLMs invoking Delphi for numerical accuracy), consistent with Plan B's requirement that agent conclusions rest on verifiable computational evidence. **The bias analysis is isomorphic to Plan A's concern**: the model learns data-source missingness rather than disease — the same failure as treating batch/artefact as disease signal in omics; Plan A separates artefacts from disease via cross-modal agreement, and the EHR analogue is explicitly modelling or stratifying by data source / care intensity. On detect → model → revert: Delphi is patient-scale "model" (a generative, sampleable virtual patient), but the authors explicitly rule out causal intervention — reaching "revert" needs a causal/counterfactual layer or a link to tissue-scale virtual tissue.

## Reusable assets
- **Code:** Delphi code, scripts and Jupyter notebooks (built on nanoGPT).
<https://github.com/gerstung-lab/delphi>
- **Checkpoints:** via UK Biobank controlled access (upload ID 7318).
- **Data:** UK Biobank (application); Danish registries via the Danish Health Data Authority in secure environments.
- **Baseline suite:** QRisk3, SCORE2, PREVENT, Framingham, UKBDRS, Charlson, Elixhauser, AutoPrognosis v2, a Llama3.1-8B prompting baseline, MILTON — a ready comparator set for Sinai.

## Follow-ups
- Extended Data Fig. 5: Delphi variants using data beyond health records (biomarkers etc.).
- The MILTON paper (67-biomarker full-spectrum model) as the lab-driven comparator.
- Subgroup fairness analyses in the Supplementary Discussion (Supplementary Figs. 10–11).
- Compare with `ehr-apollo-arxiv-2026`: discrete-code GPT vs multimodal temporal Transformer.

## Cite
```bibtex
@article{Shmatko_2025, title={Learning the natural history of human disease with generative transformers}, volume={647}, ISSN={1476-4687}, url={http://dx.doi.org/10.1038/s41586-025-09529-3}, DOI={10.1038/s41586-025-09529-3}, number={8088}, journal={Nature}, publisher={Springer Science and Business Media LLC}, author={Shmatko, Artem and Jung, Alexander Wolfgang and Gaurav, Kumar and Brunak, Søren and Mortensen, Laust Hvas and Birney, Ewan and Fitzgerald, Tom and Gerstung, Moritz}, year={2025}, month=Sept, pages={248–256} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

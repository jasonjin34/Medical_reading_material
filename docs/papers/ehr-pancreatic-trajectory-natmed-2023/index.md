# A deep learning algorithm to predict risk of pancreatic cancer from disease trajectories

> **Bibkey** `Placido_2023` · **Venue** Nature Medicine (2023) · **Category** ehr · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1038/s41591-023-02332-5> · `status: complete`

---

## One-liner
CancerRiskNet: using **only timestamped ICD diagnosis-code sequences** (disease trajectories), a Transformer trained on the Danish National Patient Registry (6.2M patients, 23,985 pancreatic cancer cases) predicts pancreatic cancer risk within 3/6/12/36/60 months. 36-month AUROC is 0.879, and still 0.83 when the last 3 months before diagnosis are excluded; transferred as-is to the US Veterans Affairs system it falls to 0.71, recovering to 0.78 after local retraining — showing both that temporal order carries signal and that models do not transfer across health systems for free.

## Problem
Pancreatic cancer is rare but lethal: ~80% of patients present with locally advanced or metastatic disease (2–9% five-year survival), whereas early-stage disease can be cured by surgery plus chemotherapy. Population screening is impractical (low incidence, costly tests, false positives), and existing surveillance covers only the small minority with family history, germline variants or cystic lesions. The question: can **disease trajectories in routine clinical records** pick out a small high-risk group (e.g. the top 1,000 of 1 million) to make costly imaging surveillance affordable? Previous EHR-based pancreatic cancer models used only code occurrence, not **time order**; Danish registry trajectory work had been descriptive.

## Method
**Input**: per-patient sequences of three-character ICD codes (ICD-8 and ICD-10 in DNPR used side by side without semantic mapping; ~2,000 level-3 codes), each with a timestamp, plus age. **Augmentation**: for each patient, all continuous partial trajectories starting at the first record with ≥5 diagnoses and different endpoints (the "time of assessment"); for cases only trajectories ending before diagnosis; for non-cases only trajectories ending ≥2 years before the end of their record (to avoid undiagnosed cancer among controls). Batches are **balance-sampled** between positives and negatives. **Model**: three stages — embedding (codes → low-dimensional vectors, trained jointly) → encoding (GRU or Transformer compresses the trajectory into a "fingerprint"; the Transformer uses cosine positional embeddings at 128 frequencies computed from **age at diagnosis and inter-diagnosis intervals**) → prediction (feed-forward head outputting risk for five windows: 3/6/12/36/60 months). **Loss**: summed cross-entropy against step-function labels at the five time points, plus L2. Comparators: bag-of-words (order-agnostic), MLP, GRU. **Data-exclusion experiments**: remove diagnoses from the last 3/6/12 months before cancer in training, to test whether the model only reads late symptoms. **Interpretability**: Integrated Gradients (Captum), aggregated by time-to-cancer strata 0–6/6–12/12–24/24–36 months. **Evaluation**: AUROC plus relative risk (RR) at an operating point of the top-n highest-risk patients per 1 million (N1000 = top 0.1%). 80/10/10 patient-level split; model selection by AUPRC; 95% CIs from 200 bootstrap resamples.

## Data
**Danish DNPR**: 8.6M patients and 229M hospital diagnoses, 1977–2018 (inpatient since 1977, outpatient/ED since 1995; no GP records). After demographic-continuity filtering (excluding Greenland residents, no stable residence, etc.), removing temporary/referral codes (8.3%) and patients with <5 diagnoses: **6.2M patients, 23,985 pancreatic cancer cases** (ICD-10 C25 / ICD-8 157). Cross-checked against the Danish Cancer Registry: 88% case overlap (a lower bound on label accuracy). **US-VA CDW**: 1999–2020; ~3M randomly sampled from 15.9M; cases defined as present in *both* the VA cancer registry and EHR ICD codes (only 32.4% of patients with a pancreatic cancer code in the EHR appear in the registry — EHR codes are noisy); final **1,948,209 patients, 3,418 cases** (the abstract's ~3M / 3,900 refer to pre-filtering counts). The systems differ sharply: VA trajectories are shorter (median 12 vs 23 years) but denser (median 188 vs 22 records per patient).

## Key results
- **Time order matters**: 36-month window, Transformer AUROC **0.879** (0.877–0.880), GRU 0.852, MLP 0.845, bag-of-words 0.807; RR at N1000: Transformer **104.7**, MLP 26.6, bag-of-words 2.1.
- **Excluding near-diagnosis data**: excluding the last 3/6/12 months lowers AUROC to 0.843/0.829/0.827 — a drop, not a collapse, so the model is not just reading late symptoms like jaundice and abdominal pain.
- **All codes beat known risk factors**: restricting to codes for 23 known risk factors gives AUROC 0.838 vs 0.879 with all ~2,000 codes.
- **Longer horizons are harder**: AUROC 0.908 for 12 months vs 0.879 for 36 months; recall at the F1 point falls from 8% at ~1 year before diagnosis to 4% at ~3 years.
- **Cross-system transfer**: the Danish model applied to US-VA with only ICD mapping gives AUROC 0.710 (RR 57.4); retrained from scratch on VA, AUROC **0.775** (RR 80.4). Conclusion: independent local training is needed when health systems differ substantially.
- **Realistic surveillance scenario**: age >50, 3-month exclusion, 12-month window, top 0.1%: RR = 58.7 (DNPR, GRU) / 33.1 (US-VA, Transformer). Taking the top 1,000 of 1M (no exclusion) gives PPV 0.32, i.e. ~320 eventual cases; a conservative estimate (3-month exclusion, PPV 0.07) gives ~70 newly identified high-risk patients.
- **Features**: 0–6 months before diagnosis are dominated by jaundice, biliary disease, abdominal pain, weight loss and digestive neoplasms; in earlier trajectories type 2 diabetes, cholelithiasis and reflux disease gain weight. Features partly overlap between systems; excluding chronic pancreatitis patients leaves RR nearly unchanged.

## Contributions
- Uses the **time sequence of disease trajectories** (not just code occurrence) as Transformer input, with continuous-time positional embeddings from age and intervals.
- **Multi-horizon risk outputs** (3–60 months), directly addressing "how early can we detect".
- **Data-exclusion protocol**: systematically dropping the last 3/6/12 months to separate early signal from symptom leakage — an evaluation norm later adopted by follow-ups (including the npj 2025 LLM-embedding paper).
- **RR at the top-0.1% operating point** as the clinical metric, translating model performance into an affordable surveillance-programme size.
- A direct **cross-system transfer vs local retraining** comparison across two very different national systems.

## Limitations
- Diagnosis codes only: no medications, labs, notes or imaging (the authors list these as future gains).
- Poor cross-system generalization (0.879 → 0.710) requiring local retraining; federated learning is proposed but not done.
- Danish data lack GP records; VA is a veteran (predominantly male) population with limited representativeness.
- Labels depend on registry/coding quality (88% DNPR–DCR overlap; low PPV of VA EHR codes).
- Retrospective; cost–benefit only estimated in the supplement, no prospective validation; IG features are correlational, not causal.
- Shared multi-horizon heads may let strong proximal features leak into distal windows (the npj 2025 paper notes over half of this paper's top-10 features overlap between 0–6 and 24–36 months).

## Relation to our direction
**For the Mount Sinai EHR (millions of patients) project this is the PI's designated starting template**, for a simple reason: it defines a complete, reproducible minimal recipe for early risk prediction from disease trajectories that needs only ICD codes plus timestamps — the cleanest and earliest-available slice of the Sinai data. What should be copied is the **evaluation protocol**, not just the model: (1) multiple assessment-time sub-trajectories per patient; (2) controls truncated 2 years before record end; (3) **excluding the last 3/6/12 months** to test symptom leakage; (4) reporting RR at the top-0.1% operating point, which maps onto clinical capacity; (5) cross-system transfer vs local retraining. Sinai is a US urban academic centre whose coding density and visit patterns resemble US-VA more than the Danish registry, so the finding that transfer drops AUROC to 0.71 while local retraining recovers 0.78 says directly: **train locally on Sinai and treat direct transfer of public models as a baseline**. **Link to cardiometabolic-kidney disease**: the paper identifies type 2 diabetes as a distal pancreatic-cancer risk factor, and the whole trajectory recipe (multi-horizon heads, data exclusion, stratified IG attribution) transfers unchanged to endpoints such as CKD progression, DKD, heart failure or dialysis — the most natural EHR-side task for the lab's Novo-funded cardiometabolic-kidney agents and foundation models. Relative to detect → model → revert: a trajectory model is **patient-scale "detect"** (flagging people who deviate from normal trajectories before clinical presentation); it answers "who and when", whereas tissue-scale virtual tissue and revert must answer "why and what to change". The authors stress that IG features are not causal — exactly where an interface is needed (e.g. selecting EHR-flagged high-risk patients who have biopsies/omics for Plan-A-style tissue anomaly detection). For Plan B (trustworthy agents): the data-exclusion and cross-system checks are the anti-leakage verifications an agent should be forced to run before asserting any EHR risk claim.

## Reusable assets
- **Code:** CancerRiskNet (PyTorch 1.9; Integrated Gradients via Captum 0.3.1).
<https://github.com/BrunakSanderLabs/CancerRiskNet>
- **Data:** DNPR via the Danish Health Data Authority (3–6 months); US-VA via VINCI approval (≥6 months). Not public.
- **Eval protocol:** multi-assessment-time trajectory augmentation, 2-year control truncation, 3/6/12-month exclusion, RR@N1000, MI-CLAIM reporting checklist (Supplementary Table 6).

## Follow-ups
- The cost estimate (Supplementary Notes) and full model-comparison tables (Supplementary Table 3).
- Delphi-2M (Nature 2025, Brunak co-author) generalizes from one cancer to a generative model of >1,000 diseases — see `ehr-delphi2m-nature-2025` in this repo.
- Ref. 23 (prediction of acute kidney injury progression) — directly relevant to kidney endpoints, worth reading.
- Existing work applying this protocol to CKD/DKD endpoints (to search).

## Cite
```bibtex
@article{Placido_2023, title={A deep learning algorithm to predict risk of pancreatic cancer from disease trajectories}, volume={29}, ISSN={1546-170X}, url={http://dx.doi.org/10.1038/s41591-023-02332-5}, DOI={10.1038/s41591-023-02332-5}, number={5}, journal={Nature Medicine}, publisher={Springer Science and Business Media LLC}, author={Placido, Davide and Yuan, Bo and Hjaltelin, Jessica X. and Zheng, Chunlei and Haue, Amalie D. and Chmura, Piotr J. and Yuan, Chen and Kim, Jihye and Umeton, Renato and Antell, Gregory and Chowdhury, Alexander and Franz, Alexandra and Brais, Lauren and Andrews, Elizabeth and Marks, Debora S. and Regev, Aviv and Ayandeh, Siamack and Brophy, Mary T. and Do, Nhan V. and Kraft, Peter and Wolpin, Brian M. and Rosenthal, Michael H. and Fillmore, Nathanael R. and Brunak, Søren and Sander, Chris}, year={2023}, month=May, pages={1113–1122} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

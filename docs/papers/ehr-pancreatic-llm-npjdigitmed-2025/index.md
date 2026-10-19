# Enhancing EHR-based pancreatic cancer prediction with LLM-derived embeddings

> **Bibkey** `Park_2025` · **Venue** npj Digital Medicine (2025) · **Category** ehr · **Relevance** medium · **Access** open
> **Link** <https://doi.org/10.1038/s41746-025-01869-8> · `status: complete`

---

## One-liner
In a CancerRiskNet-style pancreatic cancer trajectory Transformer, replace randomly initialized code embeddings with **LLM text embeddings of OMOP concept names** (OpenAI text-embedding-3-small): on two US institutional EHRs — Columbia (CUMC) and Cedars-Sinai (CSMC) — 6–12-month AUROC rises from 0.59/0.82 to 0.67/0.86, and to 0.82/0.89 once data from the 0–3 months before diagnosis are excluded.

## Problem
Pancreatic cancer five-year survival is 13%, rising to 44% if caught early; but screening covers only those with family history or germline variants (5–10% of cases), and MRI/CT cannot be applied population-wide. Longitudinal EHR histories may hold early signals. Inspired by GenePT (GPT embeddings of NCBI gene descriptions), the authors hypothesize that **LLM semantic embeddings of medical concept names** represent diagnosis codes better than embeddings learned from scratch, improving early prediction — especially on single-institution data far smaller and more heterogeneous than a national registry. A second issue is **leakage from near-diagnosis data**: in shared multi-horizon models, strong proximal signal "bleeds" into distal windows.

## Method
**Data format**: OMOP CDM condition sequences with age at recording as positional encoding. **Embedding sources** (initializing code embeddings): (a) baseline: randomly initialized PyTorch nn.Embedding; (b) RGCN: a relational graph convolutional network trained on the knowledge graph of OMOP ancestor–descendant relations; (c) **GPT**: OpenAI text-embedding-3-small on OMOP concept names, at 32 and 1536 dimensions; (d) Mistral: SFR-Embedding-Mistral (4096-d). Each frozen vs fine-tuned — 12 models. **Two task framings**: (1) a **multi-label model** (CancerRiskNet-style) predicting five windows (0–3, 3–6, 6–12, 12–36, 36–60 months), evaluated per window only on cases whose diagnosis falls in that window so proximal cases do not inflate distal scores, plus a version **excluding 0–3-month data** (moved to augment the 3–6-month window); (2) **binary models** (one each for 3–6, 6–12, 12–36 months) with **data augmentation**: proximal cases' most recent records are removed until the last remaining record falls in the target window, enlarging distal case counts. 60/20/20 split; bootstrap 95% CIs; LIME explanations; PPV compared against traditional risk factors (CA19-9, type 2 diabetes, pancreatitis) and known germline variants.

## Data
**CUMC** (Columbia University Medical Center) 3,300 cases / 785,335 controls; **CSMC** (Cedars-Sinai Medical Center, Los Angeles — note: **not** Mount Sinai) 1,781 cases / 484,515 controls. Cases have a pancreatic malignancy code and no other cancer history; controls exclude any cancer-related terms, diagnoses within the last 2 years, <5 condition records, and age <18 or >100. CSMC has genetic data: 1,500 carriers of pancreatic-cancer-associated variants, 130 of whom have pancreatic cancer (50 retained in the dataset). **Held-out distal windows have very few cases**: CUMC 23 cases at 6–12 months and 14 at 36–60; CSMC 18 and 7. HIPAA prohibits EHR sharing; the two sites ran shared code independently.

## Key results
- **6–12 months (multi-label, including 0–3-month data)**: CUMC baseline 0.592 → GPT-1536 **0.673**; CSMC 0.819 → **0.858**. On CUMC, RGCN 0.647, Mistral 0.598 (though Mistral has the best max-F1, p = 0.035).
- **After excluding 0–3 months (GPT-1536)**: 6–12 months CUMC **0.819**, CSMC **0.893**; but 3–6 months drops (CUMC 0.856→0.763, CSMC 0.884→0.870) — late symptoms extend back about 6 months, not further.
- **Embedding size**: 32-d GPT often matches or beats 1536-d; 4096-d Mistral is not consistently better; fine-tuning helps 32-d much more than 1536-d.
- **Versus CancerRiskNet (within 36 months)**: baseline AUROC 0.694 (CUMC) / 0.744 (CSMC) vs CancerRiskNet's 0.88; with 0–3-month exclusion 0.737/0.771 vs 0.83; with LLM embeddings **0.761/0.811** — institutional data still trail the Danish national registry.
- **Clinical utility (CUMC, 6–12-month binary, 338 cases / 157,067 controls)**: GPT model PPV **0.141** at max-F1 (22 TP / 134 FP) vs **0.004** for "any traditional risk factor" (96 TP / 24,950 FP); detecting 50% of cases requires screening 17% of the population. **But on CSMC the GPT model's max-F1 PPV is only 0.012** (baseline 0.084) — the abstract's 0.141 is CUMC only.
- **Complementing risk factors**: among model-detected cases, over 50% (CUMC) and over 85% (CSMC) had neither traditional risk factors nor known germline variants.
- **Features**: LIME shows the GPT-embedding model favours clinically interpretable features (baseline surfaces unrelated ones such as fractures); the binary models rank **kidney/ureter disorders** and liver disease among top features in both 6–12- and 12–36-month windows.

## Contributions
- Initializes EHR code embeddings with **LLM text embeddings of concept names** — no extra training cost, pluggable into any EHR sequence model.
- A systematic comparison of embedding source (random / KG-RGCN / GPT / Mistral), dimension and frozen vs fine-tuned.
- Explicitly identifies and handles **leakage in multi-label multi-horizon models**: per-window case restriction, 0–3-month exclusion, binary models with truncation-based augmentation.
- Two-site, code-sharing-not-data-sharing validation; reports PPV and "how many must be screened".

## Limitations
- **Very few distal-window cases** (18–23 held-out cases at 6–12 months), wide CIs (e.g. CUMC 0.673 [0.559, 0.776]); some gains are not significant.
- **Inconsistent across sites**: GPT embeddings help consistently at CSMC but not at CUMC; CSMC PPV is actually lower than baseline.
- Condition sequences only — no labs, medications or text; key risk factors like family history live in unstructured notes and are unused.
- Evaluation-cohort prevalence (215 per 100k) far exceeds the real population (~32 per 100k), so real-world PPV would be lower.
- Relies on a closed OpenAI embedding API (concept names contain no PHI, but reproducibility and version stability are limited).

## Relation to our direction
**For the Sinai EHR project this is the closest to the situation we will actually face**: a single US academic centre, OMOP format, hundreds of thousands to a million patients — not a complete national registry like Denmark's. It shows the same task scores clearly lower on institutional data than CancerRiskNet, and the two hospitals disagree. Three directly borrowable pieces: (1) **LLM concept-name embeddings as initialization** — near-zero cost, generable straight from Sinai's OMOP concept table; open embedding models should be tested too to avoid a closed dependency; (2) **anti-leakage evaluation**: per-window case restriction + 0–3-month exclusion + truncation-based augmentation — far stricter than reporting one AUROC; (3) **reporting**: PPV and "how many must be screened to catch 50%". A caution: the abstract reports only CUMC's PPV of 0.141, while CSMC's is 0.012 — exactly the selective-reporting pattern Plan B's claim-to-evidence verification should catch, and a concrete example for an omics/EHR agent failure taxonomy. **For cardiometabolic-kidney disease**: the binary models rank **kidney disorders** among early features 6–36 months before pancreatic cancer, which the authors read as a multi-organ systemic signal — suggesting kidney codes are strong cross-disease signals in Sinai trajectory models; conversely, the "LLM embeddings + multi-horizon + anti-leakage" pipeline applies unchanged to CKD/DKD progression. On detect → model → revert: this is EHR-level detect, improving representation (injecting medical knowledge into embeddings) rather than causality.

## Reusable assets
- **Code:** the pancreatic cancer Transformer (shared across both sites).
<https://github.com/jp4147/pdac_tf>
- **Data:** not shared (HIPAA).
- **Embedding models:** OpenAI text-embedding-3-small (32/1536-d), Salesforce/SFR-Embedding-Mistral; OMOP-hierarchy RGCN (Supplementary Note 2).

## Follow-ups
- GenePT (the gene text-embedding work that inspired this paper).
- Ref. 13: kidney abnormalities as early systemic manifestations of pancreatic cancer.
- Supplementary Notes 4–5: consistently high-risk individuals across models (multi-model consensus as a screening definition).
- Read side by side with `ehr-pancreatic-trajectory-natmed-2023` (CancerRiskNet).

## Cite
```bibtex
@article{Park_2025, title={Enhancing EHR-based pancreatic cancer prediction with LLM-derived embeddings}, volume={8}, ISSN={2398-6352}, url={http://dx.doi.org/10.1038/s41746-025-01869-8}, DOI={10.1038/s41746-025-01869-8}, number={1}, journal={npj Digital Medicine}, publisher={Springer Science and Business Media LLC}, author={Park, Jiheum and Patterson, Jason and Acitores Cortina, Jose M. and Gu, Tian and Hur, Chin and Tatonetti, Nicholas}, year={2025}, month=July }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

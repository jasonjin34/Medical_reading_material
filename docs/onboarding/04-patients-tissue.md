# 4 · Patients and tissue

> ⏱ About 30 min · Day 1 · Understand

!!! abstract "After this module you can answer"
    - How do AKI and CKD differ?
    - What is wrong with each of biopsy, nephrectomy and deceased-donor tissue?
    - Why do healthy donors also have altered cells?

Module 1's obs has three columns that describe where a cell came from: `condition` (what disease the person has), `tissue_type` (how the tissue was obtained) and `region` (which layer of the kidney was sampled). This module explains what lies behind them, and why they can **mislead** a model.

Numbers on this page come from two places: the literature (marked [n]) or our own counts from the Lake 2023 single-nucleus label table downloaded from GEO (marked "our count").

## Step 1 · Two kidney diseases: AKI and CKD

Kidney disease is split by **time** into two groups. KDIGO, the international kidney guideline body, gives operational definitions:

- **AKI (acute kidney injury)**: kidney function drops markedly **within days**. Any one of the following is enough [1]:
    - serum creatinine rises by ≥ 0.3 mg/dl (26.5 µmol/l) within 48 hours;
    - serum creatinine rises to ≥ 1.5 times baseline within 7 days;
    - urine output is below 0.5 ml/kg/h for 6 hours.
- **CKD (chronic kidney disease)**: abnormalities of kidney structure or function **present for at least 3 months**, with implications for health [2].

**Serum creatinine** is a metabolite in the blood that the kidneys filter out; when filtration slows, it builds up. KDIGO advises using serum creatinine with an estimating equation (the eGFR of step 2) for the initial assessment of kidney function. How much creatinine is made depends on muscle mass, so the estimate is biased in people with unusually high or low muscle mass [2].

The two are not exclusive: a person who already has CKD can also have an episode of AKI [1].

!!! tip "Computer analogy"
    AKI is an **incident**: things get worse within hours to days, and you detect it from a jump in a short time window. CKD is **long-term degradation**: the problem persists for months, and you judge it from the long-run state. A degraded system can still have an incident on top.

### In the data

KPMP, the source of Lake 2023's patient samples, focuses on the most common kinds: **CKD attributed to diabetes or hypertension**, and **AKI attributed to ischaemic or toxic injury** [3]. That is exactly what `condition.l2` holds in Lake's single-nucleus label table (our count, in people):

| `condition.l1` | `condition.l2` | Meaning | People |
|---|---|---|---|
| AKI | AKI | acute kidney injury | 6 |
| AKI | COV-AKI | AKI with COVID-19 | 4 |
| CKD | DKD | diabetic kidney disease | 7 |
| CKD | H-CKD | hypertensive CKD | 6 |
| Ref | Ref | healthy reference | 13 |

## Step 2 · How severe: eGFR

**GFR** (glomerular filtration rate) is how much plasma the kidneys filter per minute, the core measure of kidney function. Measuring it directly is laborious, so in practice it is **estimated** from serum creatinine and/or cystatin C together with age and sex, giving **eGFR** (estimated GFR) [4]. KDIGO groups CKD into six GFR categories [2]:

| Category | GFR (ml/min/1.73 m²) | Term |
|---|---|---|
| G1 | ≥ 90 | normal or high |
| G2 | 60–89 | mildly decreased |
| G3a | 45–59 | mildly to moderately decreased |
| G3b | 30–44 | moderately to severely decreased |
| G4 | 15–29 | severely decreased |
| G5 | < 15 | kidney failure |

G1 and G2 alone do not count as CKD; there must also be evidence of kidney damage [2].

**In the data: Lake 2023's public single-nucleus label table has no eGFR column and no age column** (we checked). We know whether and which disease a person has, but not how severe it is.

## Step 3 · Where the tissue comes from

<div class="grid" markdown>

![Lake 2023 Fig. 1a: kidney tissue from biopsy, nephrectomy (Nx) or deceased donor (DD), processed into cells, nuclei or sections / 肾组织来自活检、肾切除（Nx）或死亡供体（DD），处理成细胞、细胞核或切片](img/lake2023_fig1a_crop.jpg)

<div markdown>

Lake 2023's tissue has three sources [5]:

- **Needle biopsy**: a thin core of tissue taken with a needle. Patient biopsies come from KPMP and are taken for research [3]; some healthy reference tissue is also **living-donor** biopsies [5].
- **Nephrectomy** (Nx in the figure): tissue from people who had part or all of a kidney removed [5].
- **Deceased donor** (DD in the figure): kidneys from deceased donors that were not used for transplant [5].

</div>

</div>

Figure: Lake et al. 2023, Fig. 1a (cropped), Nature, CC BY 4.0.

**How the tissue was taken decides which part of the kidney you see.** Here is where the nuclei of each tissue type sit in Lake's single-nucleus data (our count):

| `tissue_type` | Cortex | Medulla | Papilla |
|---|---|---|---|
| Biopsy | 81,716 | 42,832 | 8,064 |
| Nephrectomy | 43,805 | 7,945 | 0 |
| Deceased donor | 0 | 7,013 | 12,327 |

In this dataset the deceased-donor samples come **entirely** from medulla and papilla, with no cortex at all, while nephrectomies are mostly cortex. Recall module 3: cortex and medulla hold different cell types, so samples from different sources start out with different cell-type mixes.

## Step 4 · Why healthy donors have altered cells too

You would expect every cell of a healthy reference (`condition.l1 = Ref`) to be in the reference state. In fact (our count):

- **25.7%** of healthy reference nuclei are labelled altered (43.2% in AKI, 42.5% in CKD);
- per person, the altered share among the 13 healthy donors ranges from **12% to 50%**.

Lake 2023's authors suggest that altered states in reference tissue **might arise from ischaemic stress during sample acquisition or from normal ageing** [5]. Ischaemia here means the time tissue spends cut off from blood supply, without oxygen.

!!! warning "What this means for our work"
    `Ref` is a label **per person**, not per cell. If you train an anomaly detector on "all cells from healthy people", about a quarter of the training cells are ones the authors labelled altered. Decide first whether "normal" means "cells from healthy people" or "cells with `state.l1 = reference`": the two answer different questions (module 8).

## Step 5 · The biggest trap: confounding

Cross-tabulate `condition` against `tissue_type` (our count, people / nuclei):

| `condition.l1` | Biopsy | Nephrectomy | Deceased donor |
|---|---|---|---|
| AKI | 10 / 51,868 | — | — |
| CKD | 10 / 55,274 | 3 / 8,100 | — |
| Ref | 5 / 25,470 | 5 / 43,650 | 3 / 19,340 |

Three things to notice:

1. **All AKI tissue is biopsy**, while more than half of the healthy reference is nephrectomy or deceased donor. Any "AKI vs healthy" difference is mixed with a "biopsy vs other sources" difference.
2. Within healthy reference, the altered share by tissue type is 26.5% for biopsy, 29.8% for nephrectomy and 15.6% for deceased donor (our count). Deceased donors are lowest, but they were sampled only from medulla and papilla (step 3) and are only 3 people. **From this data alone you cannot tell whether the difference comes from the tissue source, the region, or those particular people.**
3. Each combination has only 3 to 10 people. Each person contributes thousands of cells, so cell counts look large, but the number of independent units you can compare is just these few people (module 7, question 2).

These are our own inferences from the counts, not findings from the literature.

!!! tip "Computer analogy"
    It is like an A/B test where the treatment group all ran in a new data centre and the control group mostly in the old one. When the metrics differ, you cannot tell whether the feature or the data centre caused it. Before training a classifier, print the `condition` × `tissue_type` × `region` cross-table and look at it.

## Self-check

??? question "1. What is the basic difference between AKI and CKD?"
    Time. AKI is an acute drop within days (for example serum creatinine rising ≥ 0.3 mg/dl within 48 hours); CKD is an abnormality lasting at least 3 months. A person can have both.

??? question "2. Why do healthy donors have altered cells?"
    The authors suggest ischaemic stress during sample acquisition, or normal ageing. In Lake's single-nucleus data 25.7% of healthy reference nuclei are altered, ranging from 12% to 50% per person.

??? question "3. A classifier separates AKI from healthy with high accuracy. Why not trust it straight away?"
    All AKI samples are biopsies, while healthy samples are mostly nephrectomies and deceased donors, sampled from different regions. The model may have learned the tissue source or region rather than the disease. Look at the cross-table first, and split by person (module 1).

## References

1. Kidney Disease: Improving Global Outcomes (KDIGO) Acute Kidney Injury Work Group. Section 2: AKI definition. *Kidney Int Suppl* 2012;2(1):19–36. [doi:10.1038/kisup.2011.32](https://doi.org/10.1038/kisup.2011.32) — Recommendation 2.1.1; Figure 2.
2. KDIGO CKD Work Group (Stevens PE, Ahmed SB, et al.). KDIGO 2024 clinical practice guideline for the evaluation and management of chronic kidney disease. *Kidney Int* 2024;105(4S):S117–S314. [doi:10.1016/j.kint.2023.10.018](https://doi.org/10.1016/j.kint.2023.10.018) — CKD definition; Table 2; Practice Point 1.2.2.1.
3. de Boer IH, Alpers CE, Azeloglu EU, et al. Rationale and design of the Kidney Precision Medicine Project. *Kidney Int* 2021;99(3):498–510. [doi:10.1016/j.kint.2020.08.039](https://doi.org/10.1016/j.kint.2020.08.039) — abstract.
4. Inker LA, Eneanya ND, Coresh J, et al. New creatinine- and cystatin C–based equations to estimate GFR without race. *N Engl J Med* 2021;385:1737–1749. [doi:10.1056/NEJMoa2102953](https://doi.org/10.1056/NEJMoa2102953)
5. Lake BB, Menon R, Winfree S, et al. An atlas of healthy and injured cell states and niches in the human kidney. *Nature* 2023;619:585–594. [doi:10.1038/s41586-023-05769-3](https://doi.org/10.1038/s41586-023-05769-3) — Fig. 1a; Methods (ethical compliance); Results on altered states. Deep-read: [Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md).

"Our count" numbers: GEO GSE183277, `GSE183277_Kidney_Healthy-Injury_Cell_Atlas_snCv3_Metadata_03282022.txt.gz`, counted by `condition.l1`, `condition.l2`, `tissue_type`, `region.l1`, `state.l1` and `patient`.

## Terms in this module

| English | 中文 | In one sentence |
|---|---|---|
| [Acute kidney injury (AKI)](glossary.md#acute-kidney-injury) | 急性肾损伤 | A sudden loss of kidney function over hours to days (e.g. after surgery, sepsis or drugs); it can recover, or progress to chronic kidney disease. |
| [Chronic kidney disease (CKD)](glossary.md#chronic-kidney-disease) | 慢性肾脏病(CKD) | Progressive, largely irreversible loss of kidney function over months to years; the non-tumor disease setting where computational pathology benchmarks are conspicuously absent. |
| [Diabetic / hypertensive kidney disease (DKD / H-CKD)](glossary.md#diabetic-kidney-disease) | 糖尿病肾病 / 高血压肾病 | The two most common causes of chronic kidney disease, labelled DKD and H-CKD (or HKD) in kidney atlases. |
| [Estimated glomerular filtration rate (eGFR)](glossary.md#egfr-kidney-function) | 估算肾小球滤过率(eGFR) | The standard blood-derived estimate of how much the kidneys filter per minute; its trajectory over years is the clinical outcome any prognostic kidney model is ultimately judged against. |
| [Kidney biopsy](glossary.md#kidney-biopsy) | 肾活检 | A needle-extracted core of renal tissue a few millimetres long, the shared raw material every kidney modality reads in its own way — stained, dissociated or profiled in situ. |
| [Nephrectomy (tumour nephrectomy)](glossary.md#nephrectomy) | 肾切除 | Surgical removal of a kidney, usually for a tumour; tissue far from the tumour is used as 'healthy' reference, but it has gone without blood flow for a while. |
| [Deceased donor](glossary.md#deceased-donor) | 死亡供体 | An organ donor whose kidney was not transplanted and was used for research; ischaemia time is usually longer than for biopsies or nephrectomies. |
| [Ischaemia (procurement ischaemia)](glossary.md#ischaemia) | 缺血（取样缺血） | Lack of blood flow; tissue left without blood during surgery or after death switches on stress genes, which can make healthy cells look injured. |

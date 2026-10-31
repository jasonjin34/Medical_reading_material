# Datasets

The public kidney datasets we use, one page each: what was measured, on how many people, which labels, where to download, format and licence, known issues, and which research topic uses it. New to the assays or terms? Read **[Onboarding](../onboarding/index.md)** first; for how to judge whether a dataset is usable, see [Onboarding · How to read a dataset](../onboarding/07-datasets.md).

Numbers were checked on 2026-10-26 against GEO, Zenodo, cellxgene, SRA and the papers; "counted by us" means computed from the downloaded label tables.

**Availability:** on 2026-10-26 all 33 files of the 8 datasets were checked without downloading (one 16-byte request per file): every file is downloadable and has the expected format. Each dataset page has a tested "How to prepare" section with loading steps and code. The perturbation group was added on 2026-10-31 and checked against the GEO records and papers only; downloads are not yet tested.

## Disease cohorts (human): healthy reference and disease labels

| Dataset | Species | Assays | Scale | People / samples | Access | Topics |
|---|---|---|---|---|---|---|
| [Lake 2023 · Kidney atlas (KPMP / HuBMAP)](lake-2023.md) | human | scRNA, snRNA, multiome, spatial | 203,702 nuclei (sn) + 109,741 cells (sc) + 104,809 nuclei (SNARE2) | 71 people in the three single-cell parts (35 healthy, 19 CKD, 17 AKI) | open | 2, 3 |
| [Abedini 2024 · Second cohort](abedini-2024.md) | human | scRNA, snRNA, ATAC, spatial | 338,565 cells / nuclei | 58 people in the paper (81 samples: 36 control, 45 CKD of which 20 DKD, 25 HKD); the GEO single-cell data hold 44 of them (21 controls) | open | 2 |

## Measurement controls (human): known answers for measurement-caused anomalies

| Dataset | Species | Assays | Scale | People / samples | Access | Topics |
|---|---|---|---|---|---|---|
| [mBDRC 2026 · One donor, three assays](mbdrc-2026.md) | human | scRNA, multiome | 119,744 cells / nuclei | 19 healthy donors, 33 samples of normal cortex | open | 2 |
| [Hoeft 2024 · Four patients in one channel](hoeft-2024.md) | human | snRNA, genotype | 11,490 nuclei | 4 patients (frozen kidney biopsies) | open | 2 |
| [Lake 2019 · Same patients, different storage and processing](lake-2019.md) | human | snRNA | 17,659 nuclei (after QC) | 15 people (nephrectomies and deceased donors) | open | 2 |
| [Malone 2020 · Transplant donor and recipient](malone-2020.md) | human | scRNA, genotype | 81,139 cells | 5 transplant biopsies | open | 2 |

## Calibration (mouse): experiments human kidney data does not have

| Dataset | Species | Assays | Scale | People / samples | Access | Topics |
|---|---|---|---|---|---|---|
| [Janssen 2023 · Real ambient RNA in mouse kidney](janssen-2023.md) | mouse | scRNA, snRNA, genotype | 3 single-cell + 2 single-nucleus runs | mice of 3 strains (CAST, BL6, SvImJ) pooled per run | open | 2 |
| [Denisenko 2020 · Dissociation and storage in mouse kidney](denisenko-2020.md) | mouse | scRNA, snRNA | 77,656 cells + 98,303 nuclei | 3 mice per arm | open | 2 |

## Perturbation experiments (mouse): outcomes measured after a drug or an injury

| Dataset | Species | Assays | Scale | People / samples | Access | Topics |
|---|---|---|---|---|---|---|
| [Wu 2022 · Diabetic kidney disease under five treatments](wu-dkd-2022.md) | mouse | snRNA | nearly 1 million nuclei (GEO summary) | 70 GEO samples | open | 1, 3 |
| [Wu 2022 · SGLT2 inhibitor and ARB in db/db mice](wu-sglt2-arb-2022.md) | mouse | scRNA | 30 GEO samples (sequencing lanes) | about 2–4 mice per group (our count from the sample names) | open | 1 |
| [Kirita 2020 · Mouse kidney injury and repair time course](kirita-iri-2020.md) | mouse | snRNA | 24 GEO samples | sham, 4 h, 12 h, 2 d, 14 d, 6 weeks; 3 mice per time point, some with two libraries (GEO sample names) | open | 1 |
| [Dixon 2022 · Spatial time course of mouse kidney injury](dixon-iri-visium-2022.md) | mouse | spatial | 5 Visium sections | one female mouse per time point: sham, 4 h, 12 h, 2 d, 6 weeks (GEO sample names) | open | 1 |
| [Gaedcke 2022 · Single cell vs single nucleus after injury](gaedcke-sc-sn-2022.md) | mouse | scRNA, snRNA | 6 GEO samples | control, mild (17 min) and severe (27 min) IRI, each measured by single cell and single nucleus (GEO sample names) | open | 1, 2 |

## Data sources and portals

| Dataset | Species | Assays | Scale | People / samples | Access | Topics |
|---|---|---|---|---|---|---|
| [KPMP · Kidney Precision Medicine Project](kpmp.md) | human | scRNA, snRNA, multiome, spatial | consortium; growing | AKI and CKD patients with research biopsies, plus reference tissue | processed open, raw controlled | 2 |
| [CZ CELLxGENE · single-cell portal](cellxgene.md) | human | scRNA, snRNA, multiome | portal | — | open | 2 |

**Topic numbers:** 1 = [An Honest Benchmark for Perturbation Prediction in Kidney](../research/perturbation-benchmark.md) · 2 = [Artifact Injection to Boost Anomaly Detection in Kidney Single-Cell Omics](../research/anomaly-benchmark.md) · 3 = [Trustworthiness of Agent Analyses on Kidney Perturbation Data](../research/agent-claims.md)

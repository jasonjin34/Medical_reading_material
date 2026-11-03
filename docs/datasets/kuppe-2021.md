# Kuppe 2021 · Human kidney fibrosis (hypertensive CKD)

> Human CKD tissue from a third centre (Aachen), sorted into fractions: an independent cohort for checking whether a CKD hypothesis formed elsewhere holds, especially on fibrosis.

**Species** human · **Assays** scRNA · **Access** open

## At a glance

| | |
|---|---|
| Scale | CD10− 53,672 cells, CD10+ 33,690, PDGFRβ+ 37,380 (paper text; the figure legends give 51,849 and 31,875) |
| People / samples | 13 patients with hypertensive nephrosclerosis (7 eGFR > 60, 6 < 60); CD10− 11 (7 / 4), CD10+ 8 (5 / 3), PDGFRβ+ 8 (4 / 4); no healthy controls |
| Labels | cluster labels per cell (eGFR group per person in the files not yet checked) |
| Licence | CC BY 4.0 (Zenodo) |
| Paper | Kuppe C et al. Nature 2021;589:281–286. doi:10.1038/s41586-020-2941-1 |

## What was measured

Single-cell RNA of FACS-sorted CD10+, CD10− and PDGFRβ+ cells from human kidneys; spatial checks by RNA in-situ hybridisation (RNAscope), no spatial dataset released. The paper traces myofibroblasts mainly to pericytes and fibroblasts and supports it with fate tracing in mice.

## Known issues

- Sorted fractions, so cell-type proportions are not those of the tissue; no healthy controls, only higher vs lower eGFR.
- The paper's own counts disagree: 13 patients with both fractions in the text, but 11 (CD10−) and 8 (CD10+) per fraction, and 15 kidneys in the Fig. 1b legend; Zenodo files not yet counted.

## Download

| Format | File | Size | Link |
|---|---|---|---|
| `Zenodo` | record 4059315: processed matrices and labels (human tarballs 109 / 257 / 243 MB) | 2.06 GB | [↗](https://zenodo.org/records/4059315) |

Download not yet tested.

## Used in our research topics

- **[Verifiable Research Agents for Chronic Kidney Disease: A Rule-Engine Harness with Experts in the Loop](../research/hypothesis-agents.md)**: Held-out replication cohort for hypertensive CKD and fibrosis hypotheses; independent of the KPMP donors.

# Wu 2022 · Diabetic kidney disease under five treatments

> Mouse DKD kidneys after vehicle, ACE inhibitor, rosiglitazone, SGLT2 inhibitor and two combinations, at two time points. Our reading: the cleanest public kidney data for predicting a combination from its single drugs.

**Species** mouse · **Assays** snRNA · **Access** open

## At a glance

| | |
|---|---|
| Scale | nearly 1 million nuclei (GEO summary) |
| People / samples | 70 female mice in 14 groups, 4–6 per group (one sample per mouse) |
| Labels | treatment arm × time point (2 days, 2 weeks) |
| Licence | GEO: not stated |
| Paper | Wu H et al. Cell Metab 2022;34:1064–1078.e6. doi:10.1016/j.cmet.2022.05.010 |

## What was measured

Single-nucleus RNA of whole kidneys. Arms: vehicle, ACEi, rosiglitazone, SGLT2i, ACEi + rosiglitazone, ACEi + SGLT2i, each at 2 days and 2 weeks, plus db/m and db/db controls without the renin AAV (2 days only). The authors report that different drugs affected strikingly different cell types and that the combinations had the largest, largely non-overlapping effects (GEO summary).

## Known issues

- Mouse model, not patients; five treatments only, so it cannot test prediction for arbitrary unseen perturbations.

## Download

| Format | File | Size | Link |
|---|---|---|---|
| `GEO` | GSE184652 (CSV, H5) |  | [↗](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE184652) |

Download not yet tested.

## Used in our research topics

- **[Verifiable Research Agents for Chronic Kidney Disease: A Rule-Engine Harness with Experts in the Loop](../research/hypothesis-agents.md)**: Main source of questions: the held-out treated groups (a drug combination, the 2-week arm) are the measured answers the agents' hypotheses are scored against.
- **[Verifiable Virtual Cells: When Can In-Vitro Drug Predictions Be Trusted in Kidney Tissue?](../research/perturbation-benchmark.md)**: In-vivo test: SGLT2i and ACEi arms (mechanism missing in vitro) and the rosiglitazone arm (partial transfer) in one kidney dataset.

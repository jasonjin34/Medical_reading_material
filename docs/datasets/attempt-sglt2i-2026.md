# ATTEMPT 2026 · SGLT2 inhibitor vs placebo, baseline and 16-week biopsies

> The only public randomised human trial we found with single-cell data on kidney tissue before and after a drug: the human answer for treatment hypotheses.

**Species** human · **Assays** scRNA · **Access** open

## At a glance

| | |
|---|---|
| Scale | 27 biopsies, 214,415 cells |
| People / samples | dapagliflozin 9 before / 7 after, placebo 7 before / 4 after (counted from the GEO sample records) |
| Labels | arm and time point per sample; no per-cell labels |
| Licence | GEO: not stated |
| Paper | Bjornstad P et al. Sci Transl Med 2026;18:eaee1005. doi:10.1126/scitranslmed.aee1005 |

## What was measured

Single-cell RNA of kidney biopsies taken before and after 16 weeks of dapagliflozin or placebo (trial NCT04333823).

## Known issues

- Small: only 11 follow-up biopsies; early disease in young people, so effects may differ from established CKD.
- No cell-type labels in the public files; cells must be annotated first, which is itself a step an agent can get wrong.
- GEO has no participant ID, so baseline and follow-up biopsies of the same person cannot be paired from the public data; only group comparisons are possible.

## Download

| Format | File | Size | Link |
|---|---|---|---|
| `GEO` | GSE316742 (per-sample count matrices) |  | [↗](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE316742) |

Download not yet tested.

## Used in our research topics

- **[Verifiable Research Agents for Chronic Kidney Disease: A Rule-Engine Harness with Experts in the Loop](../research/hypothesis-agents.md)**: Human treatment answers: the post-treatment biopsies are held out, and hypotheses about what an SGLT2 inhibitor does to each cell type are scored against them by group comparison.
- **[Verifiable Virtual Cells: When Can In-Vitro Drug Predictions Be Trusted in Kidney Tissue?](../research/perturbation-benchmark.md)**: In-vivo test against patients: dapagliflozin, the same drug as in Tahoe-100M; scored by group comparison.

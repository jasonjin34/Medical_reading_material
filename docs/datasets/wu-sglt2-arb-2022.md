# Wu 2022 · SGLT2 inhibitor and ARB in db/db mice

> An independent lab's single-cell data on the same two drug classes (ARB, SGLT2 inhibitor) and their combination: the second dataset for testing whether a model trained on one lab transfers to another.

**Species** mouse · **Assays** scRNA · **Access** open

## At a glance

| | |
|---|---|
| Scale | 30 GEO samples (sequencing lanes) |
| People / samples | about 2–4 mice per group (our count from the sample names) |
| Labels | treatment arm |
| Licence | GEO: not stated |
| Paper | Wu J et al. Mol Ther 2022;30:1741–1753. doi:10.1016/j.ymthe.2021.10.013 |

## What was measured

Single-cell RNA of kidneys from db/db mice treated with vehicle, ARB, SGLT2i or both, plus db/m mice. The authors report 10 clusters dominated by proximal tubule cells and a PT subcluster increased in DKD and reversed by treatment (GEO summary).

## Known issues

- Few mice per group; single-cell (not single-nucleus), so it differs from Wu H 2022 in assay as well as lab.

## Download

| Format | File | Size | Link |
|---|---|---|---|
| `GEO` | GSE181382 (RDS, TXT) |  | [↗](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE181382) |

Download not yet tested.

## Used in our research topics

- **[An Honest Benchmark for Perturbation Prediction in Kidney](../research/perturbation-benchmark.md)**: Task A′: train on Wu H 2022, test on this lab.

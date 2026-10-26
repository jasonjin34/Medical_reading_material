# Janssen 2023 · Real ambient RNA in mouse kidney

> Kidneys of three mouse strains pooled in one channel; strain SNPs show how much foreign RNA each cell carries.

**Species** mouse · **Assays** scRNA · snRNA · genotype · **Access** open

## At a glance

| | |
|---|---|
| Scale | 3 single-cell + 2 single-nucleus runs |
| People / samples | mice of 3 strains (CAST, BL6, SvImJ) pooled per run |
| Labels | contamination fraction per cell (with 95% CI) |
| Licence | CC BY 4.0 |
| Paper | Janssen P et al. Genome Biol 2023;24:140. doi:10.1186/s13059-023-02978-x · [deep-read](../papers/janssen-ambient-noise-genomebiol-2023/index.md) |

![Janssen 2023 · Real ambient RNA in mouse kidney](img/janssen2023_fig1.jpg)

*Original figure: Janssen 2023 Fig. 1 A–D (cropped). A: kidneys of three strains pooled → single-cell / single-nucleus sequencing → strain SNPs assign each RNA → foreign RNA per CAST cell (red bar = background noise); B: cells per strain per run; C: strain-specific SNPs; D: informative sites per cell. Genome Biol 2023, CC BY 4.0.*

## What was measured

Single-cell RNA ×3 (fresh) and single-nucleus RNA ×2 (RNAlater, frozen), 10x.

## People and samples

Healthy mice only.

## Labels

Median contamination: 35% and 17% in single-nucleus vs 11% and 3% in single-cell runs. The absolute number of contaminating UMIs per cell is roughly constant, so injection should add a fixed amount, not a fixed fraction.

## Known issues

- Mouse, healthy only; all tools performed worst on nuc3, which the authors set aside.

## Download

| Format | File | Size | Link |
|---|---|---|---|
| `zip` | Zenodo 7328632: rep1 / rep2 / rep3 / nuc2 / nuc3 | 3.4 GB total | [↗](https://doi.org/10.5281/zenodo.7328632) |
| `H5` | in each zip: raw (with empty droplets) + filtered 10x matrices | 163–226 MB | — |
| `RDS` | in each zip: per-cell contamination fraction | 70–310 KB | — |
| `H5` | GEO GSE218853: the same raw / filtered h5 files | 1.1 GB | [↗](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE218853) |

The smallest file, rep3.zip (0.31 GB), is a good first look at the format.

## How to prepare

*Tested on 2026-10-26 in plain Python (anndata, scanpy, h5py, scipy, pandas, rdata); no R needed. Keep the data outside this repository.*

1. Each Zenodo zip (rep3.zip is the smallest, 0.31 GB) holds `raw_feature_bc_matrix.h5`, `filtered_feature_bc_matrix.h5`, `perCell_noMito_CAST_binom.RDS` and two Seurat objects.
2. rep3: filtered 28,692 genes × 6,546 cells (mm10); raw 6,794,880 barcodes, empty droplets included (use these for the ambient profile).
3. The contamination table covers **CAST cells only** (2,096 in rep3): `contPerCell_binom` with `CI_low` / `CI_high` and the number of informative SNPs.

```python
import scanpy as sc, rdata
filt = sc.read_10x_h5("rep3/filtered_feature_bc_matrix.h5")
raw  = sc.read_10x_h5("rep3/raw_feature_bc_matrix.h5")
cont = rdata.read_rds("rep3/perCell_noMito_CAST_binom.RDS")      # pandas DataFrame
```

## Used in our research topics

- **[A Benchmark for Anomaly Detection in Kidney Single-Cell Omics](../research/anomaly-benchmark.md)**: Calibrates how strong and what shape injected ambient RNA should have. Not a test set.

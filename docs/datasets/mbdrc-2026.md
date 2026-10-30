# mBDRC 2026 · One donor, three assays

> Healthy kidney cortex from 19 donors, measured with up to three assays (in the cellxgene file 3 of 18 donors have all three, 8 have two): differences caused by the assay are a design-given answer, no injection needed.

**Species** human · **Assays** scRNA · multiome · **Access** open

## At a glance

| | |
|---|---|
| Scale | 119,744 cells / nuclei |
| People / samples | 19 healthy donors, 33 samples of normal cortex |
| Labels | cell types; assay and donor per cell |
| Licence | CC BY 4.0 (data); paper CC BY-NC-ND 4.0 |
| Paper | Acera-Mateos M et al. Genome Biol 2026;27:64. doi:10.1186/s13059-026-04002-4 · [deep-read](../papers/kidney-multimodal-genomebiol-2026/index.md) |

![mBDRC 2026 · One donor, three assays](img/mbdrc_fig1.jpg)

*Original figure: Acera-Mateos 2026 Fig. 1, unmodified. Bottom left, "DATA SCHEME": 10x Multiome (11 samples, RNA + ATAC), 10x 3′ v3 (18), 10x 5′ v1 (4), all healthy cortex; the rest is the paper's integration framework, which we do not use. Genome Biol 2026, CC BY-NC-ND 4.0.*

## What was measured

3′ single-cell RNA, 5′ single-cell RNA, and 10x multiome (snRNA + snATAC in the same nucleus).

## People and samples

19 healthy donors (the paper's term); normal tissue from the unaffected part of total nephrectomies, cut into about 25 biopsy-sized cores and kept in different media (CryoStor, RNAlater, OCT, liquid nitrogen). Cortex only, no medulla. Paper: 33 samples, 25 from donors with several samples and 8 from donors with one.

## Labels

Cell types, plus the assay and donor of every cell. Key number from the paper (3′ scRNA vs snRNA, 5 donors, 14 cell types): the assay explains a median 24% of expression variance, the donor about 3%.

## Known issues

- Healthy donors only, and cortex only.
- Only 3 donors have all three assays; assay is also confounded with the tissue core and its preservation medium.

## Download

| Format | File | Size | Link |
|---|---|---|---|
| `H5AD` | cellxgene: integrated RNA, 97,125 cells (3′ / 5′ / multiome) | 1.41 GB | — |
| `H5AD` | cellxgene: multiome, 37,717 nuclei | 0.3 GB | — |
| `TSV` | cellxgene: ATAC fragments + index | 4.1 GB | — |
| `tar.gz` | Zenodo: all processed data + README | 35.2 GB | [↗](https://doi.org/10.5281/zenodo.18157241) |

The three cellxgene files (about 6 GB) are enough to start. Raw sequencing is at dbGaP phs004459 and needs an application.

## How to prepare

*Tested on 2026-10-26 in plain Python (anndata, scanpy, h5py, scipy, pandas, rdata); no R needed. Keep the data outside this repository.*

1. Download the cellxgene all-assay h5ad (1.41 GB): 97,125 cells × 36,030 genes; integer counts in `raw.X`.
2. `obs` already holds what the benchmark needs: `assay` (10x 3′ v3 / 5′ v1 / multiome), `donor_id` (18 donors), `sample_id` (28), `author_cell_type` (36 types), `pct_counts_mt`, preservation method.
3. For the assay-change task, group cells by `donor_id` × `assay`. The multiome-only h5ad (0.3 GB) and its ATAC fragments (4.1 GB) are only needed for ATAC.

```python
import scanpy as sc
adata = sc.read_h5ad("mbdrc_all.h5ad")
adata.X = adata.raw.X
adata.obs.groupby(["donor_id", "assay"], observed=True).size()
```

## Used in our research topics

- **[Artifact Injection to Boost Anomaly Detection in Kidney Single-Cell Omics](../research/anomaly-benchmark.md)**: Task T2b: anything flagged as anomalous only because the same donor was measured with another assay is treated as a false alarm (tier 2; our design choice). Also extends the healthy reference.

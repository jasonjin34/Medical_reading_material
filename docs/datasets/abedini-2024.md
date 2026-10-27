# Abedini 2024 · Second cohort

> A second lab and a second set of people: used to test whether false alarms on healthy donors stay under control.

**Species** human · **Assays** scRNA · snRNA · ATAC · spatial · **Access** open

## At a glance

| | |
|---|---|
| Scale | 338,565 cells / nuclei |
| People / samples | 58 people in the paper (81 samples: 36 control, 45 CKD of which 20 DKD, 25 HKD); the GEO single-cell data hold 44 of them (21 controls) |
| Labels | cell types; disease group per sample |
| Licence | not stated |
| Paper | Abedini A et al. Nat Genet 2024;56:1712–1724. doi:10.1038/s41588-024-01802-x · [deep-read](../papers/abedini-kidney-atlas-natgenet-2024/index.md) |

## What was measured

Single-cell RNA, single-nucleus RNA, snATAC (measured separately, not multiome), Visium and CosMx.

## People and samples

Left-over kidney tissue (the paper says only "Left-over kidney samples"); cortex and outer medulla. Controls: eGFR > 60 and fibrosis < 10%. By person (counted by us from the GEO metadata): 14 single-cell and 7 single-nucleus controls; 8 people (5 of them controls) have both single-cell and single-nucleus data.

## Labels

Cell types and the disease group of each sample; no per-cell altered state.

## Known issues

- Counts are not integers (282,610 of 338,565 `nCount_RNA` values, counted by us), so they were corrected before release: the Supplementary Information says "Ambient RNA was corrected using SoupX (v1.5.0) and doublets were removed by DoubletFinder (v2.0) with default parameters". Part of the artifacts is therefore already gone.
- Single-cell data used 37 °C enzymatic digestion, so it carries dissociation stress. No raw data ("due to privacy concerns").

## Download

| Format | File | Size | Link |
|---|---|---|---|
| `H5AD` | GEO GSE211785: sc + sn + ATAC, before / after scVI | 4.7 / 5.5 GB | [↗](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE211785) |
| `H5AD` | same, merged with KPMP data | 9.0 GB | [↗](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE211785) |
| `RDS` | count matrix (sc + sn + ATAC) | 1.7 GB | [↗](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE211785) |
| `TXT` | per-cell metadata + UMAP | 15 MB | [↗](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE211785) |

The paper is not open access and not CC-licensed, so no original figure is shown here. The licence of the data must be confirmed before releasing derived labels.

## How to prepare

*Tested on 2026-10-26 in plain Python (anndata, scanpy, h5py, scipy, pandas, rdata); no R needed. Keep the data outside this repository.*

1. Per-cell labels (`Cluster_Idents` cell type, `tech`, `group`, sex, age, QC) are in `GSE211785_scRNA-seq_snRNA-seq_snATAC-seq_metadata.txt.gz` (9 MB, 338,565 rows); the `EXPORT_..._umap.txt.gz` has only cell ID and UMAP. Counts are in the h5ad (5.0 GB gzipped, **18 GB** unzipped); open it in backed mode.
2. 338,565 cells × 34,733 genes. `X` is normalised; integer counts are in `layers["counts"]`. `tech` = SC_RNA / SN_RNA / SN_ATAC; `group` = Control / DKD / HKD; `sample` = 44 people.
3. Numeric obs columns are stored as text; convert them before use. `nCount_RNA` is not an integer, most likely because ambient RNA was corrected with SoupX before release (Supplementary Information; our inference); whether `layers["counts"]` is before or after that correction is not confirmed.
4. Controls by person: 14 single-cell, 7 single-nucleus, 7 ATAC.

```python
import anndata as ad
a = ad.read_h5ad("GSE211785_Susztak_SC_SN_ATAC_merged_PreSCVI_final.h5ad", backed="r")
rna = a[a.obs["tech"].astype(str) != "SN_ATAC"].to_memory()
rna.X = rna.layers["counts"]
```

## Used in our research topics

- **[A Benchmark for Anomaly Detection in Kidney Single-Cell Omics](../research/anomaly-benchmark.md)**: Task T4: every anomaly called on a healthy donor is counted as a false alarm (our design choice; healthy tissue also carries altered cells, 26% of healthy-donor nuclei in Lake 2023); does the observed rate stay below the target?

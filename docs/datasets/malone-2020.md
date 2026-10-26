# Malone 2020 · Transplant donor and recipient

> Kidney transplant biopsies where each cell is assigned to donor or recipient by genotype.

**Species** human · **Assays** scRNA · genotype · **Access** open

## At a glance

| | |
|---|---|
| Scale | 81,139 cells |
| People / samples | 5 transplant biopsies |
| Labels | donor / recipient per cell (public file disagrees with the paper) |
| Licence | not CC |
| Paper | Malone AF et al. JASN 2020;31(9):1977–1986. doi:10.1681/ASN.2020030326 · [deep-read](../papers/malone-transplant-chimerism-jasn-2020/index.md) |

## What was measured

Single-cell RNA (10x 5′); whole-exome sequencing of donors and recipients.

## People and samples

5 kidney transplant biopsies; the disease is transplant rejection, not AKI / CKD.

## Labels

Donor / recipient labels per cell. The public labels contradict the paper (macrophages: 4,715 / 312 in the file vs 1,229 / 3,798 in the paper), reason unknown.

## Known issues

- Doublets were removed by hand; no doublet labels, no empty droplets; ambient RNA is not discussed.

## Download

| Format | File | Size | Link |
|---|---|---|---|
| `CSV` | GEO GSE145927: count tables of 7 biopsies (after QC) | 247 MB | [↗](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE145927) |
| `CSV` | per-cell metadata (donor / recipient, cell type, rejection) | 2.1 MB | [↗](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE145927) |
| `FASTQ` | SRA SRP250734 (36 runs, incl. exomes) | ≈ 861 GB | — |

JASN is not CC-licensed, so no original figure is shown. Using it would mean re-running from about 30–65 GB of raw data per sample.

## How to prepare

*Tested on 2026-10-26 in plain Python (anndata, scanpy, h5py, scipy, pandas, rdata); no R needed. Keep the data outside this repository.*

1. Metadata: 81,139 cells from 5 biopsies (`orig.ident` biopsy62/64/65/67/68), `SNV_GT` donor 75,741 / recipient 5,398.
2. Count files are genes × cells, one per sample, with a different barcode format: `AAACCTGAGAGCTTCT.1` → `AAACCTGAGAGCTTCT-1_3` for biopsy65 (`day11rawcounts`); all 5,395 then match. There are 7 count files but only 5 biopsies in the metadata.
3. Not used for now: the public donor / recipient labels disagree with the paper.

```python
import pandas as pd
md = pd.read_csv("GSE145927_MGI.metadata.csv.gz", index_col=0)
c = pd.read_csv("GSM4339777_day11rawcounts.csv.gz", index_col=0)  # biopsy65, genes x cells
c.columns = c.columns.str.replace(r"\.(\d+)$", r"-\1", regex=True) + "_3"
```

## Used in our research topics

- **[A Benchmark for Anomaly Detection in Kidney Single-Cell Omics](../research/anomaly-benchmark.md)**: Not used for now; human-kidney ground truth for artifacts relies on Hoeft 2024.

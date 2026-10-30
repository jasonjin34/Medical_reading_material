# Hoeft 2024 · Four patients in one channel

> Four patients' kidney biopsies pooled in one 10x single-nucleus channel and separated by SNPs, so real ambient RNA and doublets can be computed. Our reading: the smallest and most direct such human kidney dataset we know of (Malone 2020 also has genotypes, but its raw data, including exomes, are about 700 GB in SRA).

**Species** human · **Assays** snRNA · genotype · **Access** open

## At a glance

| | |
|---|---|
| Scale | 11,490 nuclei |
| People / samples | 4 patients (frozen kidney biopsies) |
| Labels | donor by SNP; 250 genotype doublets (2.2%) |
| Licence | CC BY 4.0 (paper) |
| Paper | Hoeft K et al. Nat Commun 2024;15:10612. doi:10.1038/s41467-024-54270-6 · [deep-read](../papers/hoeft-genotype-multiplexing-natcommun-2024/index.md) |

![Hoeft 2024 · Four patients in one channel](img/hoeft2024_fig2ij.jpg)

*Original figure: Hoeft 2024 Fig. 2 i–j (kidney part, cropped). i: conceptual cartoon (the paper's term) of UMAPs of the pooled kidney nuclei (4 donors), coloured by cluster or by each method's donor assignment; j: share of each donor, doublets and unassigned nuclei per cluster. Most nuclei in the "Low Quality" and "Mixed/Doublets" clusters belong to a single donor. Nat Commun 2024, CC BY 4.0.*

## What was measured

Single-nucleus RNA (10x 3′ v3.1); bulk RNA-seq per patient, turned into genotype files (VCF).

## People and samples

4 patients; the diagnoses are not reported.

## Labels

A nucleus carrying another donor's alleles is contaminated (ambient); a droplet with two genotypes is a doublet. Per-nucleus donor assignments are not public and must be recomputed from the raw data.

## Known issues

- The GEO matrix labelled "raw" is already filtered (no empty droplets); ambient RNA is not quantified in the paper.
- Only 4 people: enough for validation, not for main results.
- Useful finding: the expression cluster "Mixed/Doublets" holds 4,488 nuclei (39%), but only 123 of them are genotype doublets (counted by us from the Source Data). Judging the cause of an anomaly from expression alone is unreliable.

## Download

| Format | File | Size | Link |
|---|---|---|---|
| `MTX` | GEO GSE247708: kidney 10x matrix (filtered, 11,490 nuclei) | 65 MB | [↗](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE247708) |
| `VCF` | genotypes of the 4 kidney patients (from bulk RNA-seq) | 0.1–0.4 MB each | [↗](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE247708) |
| `FASTQ` | SRA PRJNA1040187, kidney run SRR29832267 | ≈ 29 GB (SRA) | [↗](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA1040187) |

To get ambient and doublet ground truth, rerun CellRanger and souporcell on the FASTQ with the VCFs.

## How to prepare

*Tested on 2026-10-26 in plain Python (anndata, scanpy, h5py, scipy, pandas, rdata); no R needed. Keep the data outside this repository.*

1. Download only the kidney sample GSM8397034 (matrix + barcodes + features, 68 MB) instead of the 611 MB RAW.tar: 36,601 genes × 11,490 nuclei, median 1,055 UMIs per nucleus.
2. The kidney genotypes are the four small VCFs (TS116, TS120, TS121, TS126; from bulk RNA-seq, so only about a thousand sites each, e.g. 1,260 in TS116). Confirm on the GEO sample pages that these are the kidney donors.
3. The matrix is filtered and the donor of each nucleus is not public, so the doublet and ambient ground truth needs a rerun from FASTQ (SRR29832267, about 29 GB in SRA, 95 Gb of bases): CellRanger, then souporcell or vireo with the VCFs.

```python
import scanpy as sc, pandas as pd
k = sc.read_mtx("GSM8397034_Kidney_Pooled_matrix.mtx.gz").T      # -> nuclei x genes
k.obs_names = pd.read_csv("GSM8397034_Kidney_Pooled_barcodes.tsv.gz", header=None)[0].values
k.var_names = pd.read_csv("GSM8397034_Kidney_Pooled_features.tsv.gz", header=None, sep="\t")[1].values
k.var_names_make_unique()
```

## Used in our research topics

- **[Artifact Injection to Boost Anomaly Detection in Kidney Single-Cell Omics](../research/anomaly-benchmark.md)**: Main line: real human-kidney doublet and ambient answers; the examiner for task T2 and a check that our injected artifacts look real.

# 7 · How to read a dataset

> ⏱ About 40 min · Day 1 · Understand

!!! abstract "After this module you can answer"
    - Which questions do you ask first about a single-cell dataset?
    - Why does the number of people matter more than the number of cells?
    - How do raw vs filtered and open vs controlled limit what you can do?

The facts about each dataset are under the **[Datasets](../datasets/index.md)** tab. This module does not go through them one by one; it gives **six questions to ask of any dataset**, with those datasets as examples. Afterwards you will know which lines of a dataset page to look at.

## The big picture: five datasets side by side

One dataset on its own hardly shows what is special about it. Below, five representative datasets sit side by side, one row per question that follows. Skim it first and notice **which rows differ most**; each question below comes back to this table.

| | [Lake 2023](../datasets/lake-2023.md) | [Abedini 2024](../datasets/abedini-2024.md) | [mBDRC 2026](../datasets/mbdrc-2026.md) | [Hoeft 2024](../datasets/hoeft-2024.md) | [Janssen 2023 (mouse)](../datasets/janssen-2023.md) |
|---|---|---|---|---|---|
| **1 · Measured** | scRNA, snRNA, multiome, spatial | scRNA, snRNA, ATAC, spatial | scRNA, multiome | snRNA, genotype | scRNA, snRNA, genotype |
| **2 · People** | 71 people in the three single-cell parts (35 healthy, 19 CKD, 17 AKI) | 58 people in the paper (81 samples: 36 control, 45 CKD of which 20 DKD, 25 HKD); the GEO single-cell data hold 44 of them (21 controls) | 19 healthy donors, 33 samples of normal cortex | 4 patients (frozen kidney biopsies) | mice of 3 strains (CAST, BL6, SvImJ) pooled per run |
| **3 · Tissue** | patients: mostly KPMP biopsies (3 CKD nephrectomies in snCv3); healthy: nephrectomy, deceased donor, living-donor biopsy; cortex, medulla, papilla | left-over (de-identified) kidney tissue; cortex and outer medulla | normal cortex at nephrectomy; cortex only | frozen kidney biopsies; diagnoses not reported | healthy mouse kidney, 3 strains pooled per run |
| **4 · Labels** | cell type + reference / altered state for every cell except 3,364 single-nucleus nuclei | cell types; disease group per sample | cell types; assay and donor per cell | donor by SNP; 250 genotype doublets (2.2%) | contamination fraction per cell (with 95% CI) |
| **5 · Processing** | filtered counts; raw FASTQ controlled, so no empty droplets | low-quality cells removed; ambient RNA corrected with SoupX and doublets removed with DoubletFinder (Supplementary Information); no raw data | processed matrices (cellxgene, Zenodo); raw at dbGaP, on application | GEO "raw" matrix is in fact filtered; FASTQ open, donor labels must be recomputed | raw (with empty droplets) + filtered matrices |
| **6 · Licence** | CC BY 4.0 (cellxgene); GEO: not stated | not stated | CC BY 4.0 (data); paper CC BY-NC-ND 4.0 | CC BY 4.0 (paper) | CC BY 4.0 |

A few contrasts worth noticing:

- **Lake 2023 and Abedini 2024** are both large patient cohorts. Lake gives almost every cell a reference / altered label (a small number of nuclei are unlabelled); Abedini has per-sample disease groups plus a few per-cell injury clusters (such as `iPT`), but no systematic altered-state label. Both were partly cleaned before release: Lake removed doublets in every assay and subtracted ambient RNA with SoupX in its single-cell data [1]; Abedini also corrected ambient RNA and removed doublets [2].
- **mBDRC 2026, Hoeft 2024 and Janssen 2023** have few people but carry answers fixed by the design: the assay, donors assigned by SNPs, per-cell contamination. Our reading: for finding artifacts they are more useful than a big atlas.
- Only **Janssen 2023** provides ready-made raw matrices with empty droplets, and it is mouse. The raw sequencing (FASTQ) of Hoeft 2024 and Lake 2019 is open on SRA, so re-running the alignment pipeline can recover the empty droplets (see their dataset pages).

## Question 1 · What was measured?

Single-cell or single-nucleus? Is there ATAC? Were two things measured in the same nucleus (multiome)? The assay sets the biases (modules 5 and 6). Example: [Lake 2023](../datasets/lake-2023.md) has all three, but RNA + ATAC only for 7 healthy donors; [Abedini 2024](../datasets/abedini-2024.md) measured RNA and ATAC separately, so the two tables do not describe the same cells.

## Question 2 · How many people, not how many cells

200,000 cells sounds like a lot, but they come from a few dozen people. As module 1 explained, cells from one person are strongly correlated and splits go by person, so **the real sample size is the number of people**, especially how many are healthy and how many are patients. Example: [Hoeft 2024](../datasets/hoeft-2024.md) has over ten thousand nuclei but only 4 people; our reading: enough for validation only.

## Question 3 · Where did the tissue come from?

Biopsy, nephrectomy or deceased donor? Cortex or medulla? Procurement brings ischaemic stress, and region sets the cell mix (modules 3 and 4). Example: [mBDRC](../datasets/mbdrc-2026.md) is cortex only; [Lake 2019](../datasets/lake-2019.md) has no biopsies.

## Question 4 · What are the labels, and how far can you trust them?

Are there cell-type, cell-state, donor or assay labels? Are they **fixed by the experimental design** (one donor measured by several assays, donors assigned by SNPs) or **read off clusters by experts**? The first kind can serve as ground truth; the second needs care (module 2). Example: [Lake 2023](../datasets/lake-2023.md)'s altered states are expert calls; [Janssen 2023](../datasets/janssen-2023.md)'s per-cell contamination is computed from genotypes.

## Question 5 · How far has the data been processed?

- **Raw or filtered:** a raw matrix contains empty droplets, which you need to estimate ambient RNA; a filtered one has cells only. Example: [Janssen 2023](../datasets/janssen-2023.md) has raw; the "raw" file of [Hoeft 2024](../datasets/hoeft-2024.md) on GEO is in fact filtered.
- **Have artifacts already been removed:** example: [Abedini 2024](../datasets/abedini-2024.md) already ran SoupX and DoubletFinder [2], so counts are no longer integers; [Lake 2023](../datasets/lake-2023.md)'s single-cell data was corrected with SoupX too [1].
- **Was anything dropped:** example: [Lake 2019](../datasets/lake-2019.md) removed mitochondrial genes from the public matrix, so mitochondrial fractions cannot be computed directly.

## Question 6 · Can you get it, and can you publish from it?

- **Open or controlled:** processed data usually sit on GEO / cellxgene / Zenodo and download directly; human raw sequencing usually sits in dbGaP / EGA and needs an application (exceptions on this site: the FASTQ of Hoeft 2024 and Lake 2019 are open on SRA; see the dataset pages).
- **Licence:** CC BY allows free use and publishing derived results; where no licence is stated (for example [Abedini 2024](../datasets/abedini-2024.md)), confirm before releasing derived labels.
- **Size and format:** h5ad reads directly in Python (module 1); RDS / h5Seurat are R formats and need converting.

!!! tip "Computer analogy"
    These six questions are a code review for someone else's dataset: provenance (who collected it and how), sample size (how many independent samples), label quality (ground truth or weak labels), preprocessing history (what cleaning was done), and access and licence.

## Self-check

??? question "1. One dataset has 500,000 cells from 6 people, another 100,000 cells from 40 people. Which is better for testing whether a method generalises to new patients?"
    The one with 40 people. Splitting by person, 6 people cannot give a reliable training and test set.

??? question "2. To estimate real ambient contamination, what do you most need in the data?"
    A raw matrix with empty droplets, ideally plus genotypes: for the RNA molecules that cover a SNP, they show which individual the molecule came from, which gives each cell's contamination fraction (as in Janssen 2023 [3]).

??? question "3. Why is Abedini 2024 a poor choice for testing artifact-detection methods directly?"
    Ambient RNA was already removed with SoupX and doublets with DoubletFinder [2], so part of the artifacts is gone. The same partly applies to Lake 2023: it also removed doublets and ran SoupX on its single-cell data [1]; only Lake's single-nucleus counts are still raw integers.

## References

1. Lake BB, Menon R, Winfree S, et al. An atlas of healthy and injured cell states and niches in the human kidney. *Nature* 2023;619:585–594. [doi:10.1038/s41586-023-05769-3](https://doi.org/10.1038/s41586-023-05769-3) — Methods "Quality control of sequencing data" (snCv3: "doublets were identified using the DoubletDetection software… and removed"; scCv3: "The ambient mRNA contamination was corrected using SoupX"; SNARE2: doublets removed). Deep-read: [Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md).
2. Abedini A, Levinsohn J, Klötzer KA, et al. Single-cell multi-omic and spatial profiling of human kidneys implicates the fibrotic microenvironment in kidney disease progression. *Nat Genet* 2024;56:1712–1724. [doi:10.1038/s41588-024-01802-x](https://doi.org/10.1038/s41588-024-01802-x) — Supplementary Information, "Data Processing and Computational Analyses" ("Ambient RNA was corrected using SoupX (v1.5.0) and doublets were removed by DoubletFinder (v2.0)"). Deep-read: [Abedini 2024](../papers/abedini-kidney-atlas-natgenet-2024/index.md).
3. Janssen P, Kliesmete Z, Vieth B, et al. The effect of background noise and its removal on the analysis of single-cell expression data. *Genome Biol* 2023;24:140. [doi:10.1186/s13059-023-02978-x](https://doi.org/10.1186/s13059-023-02978-x) — Results (contamination estimated from strain-specific SNPs, per cell). Deep-read: [Janssen 2023](../papers/janssen-ambient-noise-genomebiol-2023/index.md).

## Terms in this module

| Term | In one sentence |
|---|---|
| [KPMP (Kidney Precision Medicine Project)](glossary.md#kpmp) | An NIH consortium that collects kidney biopsies from AKI and CKD patients and profiles them with single-cell, spatial and imaging assays; the main source of Lake 2023. |
| [CZ CELLxGENE](glossary.md#cellxgene) | The Chan Zuckerberg single-cell portal that serves curated datasets as standard h5ad files with harmonised metadata; a convenient way to download Lake 2023 and mBDRC. Column names differ from the authors' GEO tables (e.g. donor_id), X is normalised with raw counts in raw.X, and the Lake single-nucleus and single-cell files do not include the author state labels. |
| [GEO / SRA](glossary.md#geo-sra) | NCBI's public repositories: GEO holds processed data (count matrices, metadata tables), SRA holds raw sequencing reads (FASTQ); free to download. |
| [dbGaP / EGA (controlled access)](glossary.md#dbgap) | Controlled-access archives for human raw sequencing data that could identify a person; access requires an application and a data-use agreement. |

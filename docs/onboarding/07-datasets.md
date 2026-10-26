# 7 · How to read a dataset

> ⏱ About 40 min · Day 1 · Understand

!!! abstract "After this module you can answer"
    - Which questions do you ask first about a single-cell dataset?
    - Why does the number of people matter more than the number of cells?
    - How do raw vs filtered and open vs controlled limit what you can do?

The facts about each dataset are under the **[Datasets](../datasets/index.md)** tab. This module does not go through them one by one; it gives **six questions to ask of any dataset**, with those datasets as examples. Afterwards you will know which lines of a dataset page to look at.

## Question 1 · What was measured?

Single-cell or single-nucleus? Is there ATAC? Were two things measured in the same nucleus (multiome)? The assay sets the biases (modules 5 and 6). Example: [Lake 2023](../datasets/lake-2023.md) has all three, but RNA + ATAC only for 7 healthy donors; [Abedini 2024](../datasets/abedini-2024.md) measured RNA and ATAC separately, so the two tables do not describe the same cells.

## Question 2 · How many people, not how many cells

200,000 cells sounds like a lot, but they come from a few dozen people. As module 1 explained, cells from one person are strongly correlated and splits go by person, so **the real sample size is the number of people**, especially how many are healthy and how many are patients. Example: [Hoeft 2024](../datasets/hoeft-2024.md) has 11,490 nuclei but only 4 people, enough for validation only.

## Question 3 · Where did the tissue come from?

Biopsy, nephrectomy or deceased donor? Cortex or medulla? Procurement brings ischaemic stress, and region sets the cell mix (modules 3 and 4). Example: [mBDRC](../datasets/mbdrc-2026.md) is cortex only; [Lake 2019](../datasets/lake-2019.md) has no biopsies.

## Question 4 · What are the labels, and how far can you trust them?

Are there cell-type, cell-state, donor or assay labels? Are they **fixed by the experimental design** (one donor measured by several assays, donors assigned by SNPs) or **read off clusters by experts**? The first kind can serve as ground truth; the second needs care (module 2). Example: [Lake 2023](../datasets/lake-2023.md)'s altered states are expert calls; [Janssen 2023](../datasets/janssen-2023.md)'s per-cell contamination is computed from genotypes.

## Question 5 · How far has the data been processed?

- **Raw or filtered:** a raw matrix contains empty droplets, which you need to estimate ambient RNA; a filtered one has cells only. Example: [Janssen 2023](../datasets/janssen-2023.md) has raw; the "raw" file of [Hoeft 2024](../datasets/hoeft-2024.md) on GEO is in fact filtered.
- **Have artifacts already been removed:** example: [Abedini 2024](../datasets/abedini-2024.md) already ran SoupX and DoubletFinder, so counts are no longer integers.
- **Was anything dropped:** example: [Lake 2019](../datasets/lake-2019.md) removed mitochondrial genes from the public matrix, so mitochondrial fractions cannot be computed directly.

## Question 6 · Can you get it, and can you publish from it?

- **Open or controlled:** processed data usually sit on GEO / cellxgene / Zenodo and download directly; human raw sequencing sits in dbGaP / EGA and needs an application.
- **Licence:** CC BY allows free use and publishing derived results; where no licence is stated (for example [Abedini 2024](../datasets/abedini-2024.md)), confirm before releasing derived labels.
- **Size and format:** h5ad reads directly in Python; RDS / h5Seurat are R formats and need converting (module 1).

!!! tip "Computer analogy"
    These six questions are a code review for someone else's dataset: provenance (who collected it and how), sample size (how many independent samples), label quality (ground truth or weak labels), preprocessing history (what cleaning was done), and access and licence.

## Self-check

??? question "1. One dataset has 500,000 cells from 6 people, another 100,000 cells from 40 people. Which is better for testing whether a method generalises to new patients?"
    The one with 40 people. Splitting by person, 6 people cannot give a reliable training and test set.

??? question "2. To estimate real ambient contamination, what do you most need in the data?"
    A raw matrix with empty droplets, ideally plus genotypes that show where each RNA came from (as in Janssen 2023).

??? question "3. Why is Abedini 2024 a poor choice for testing artifact-detection methods directly?"
    Ambient RNA was already removed with SoupX and doublets with DoubletFinder, so part of the artifacts is gone.

## Terms in this module

| English | 中文 | In one sentence |
|---|---|---|
| [KPMP (Kidney Precision Medicine Project)](glossary.md#kpmp) | KPMP（肾脏精准医学项目） | An NIH consortium that collects kidney biopsies from AKI and CKD patients and profiles them with single-cell, spatial and imaging assays; the main source of Lake 2023. |
| [CZ CELLxGENE](glossary.md#cellxgene) | CELLxGENE 数据平台 | The Chan Zuckerberg single-cell portal that serves curated datasets as standard h5ad files with harmonised metadata; the easiest way to download Lake 2023 and mBDRC. |
| [GEO / SRA](glossary.md#geo-sra) | GEO / SRA 公共数据库 | NCBI's public repositories: GEO holds processed data (count matrices, metadata tables), SRA holds raw sequencing reads (FASTQ); free to download. |
| [dbGaP / EGA (controlled access)](glossary.md#dbgap) | dbGaP / EGA（受控访问） | Controlled-access archives for human raw sequencing data that could identify a person; access requires an application and a data-use agreement. |

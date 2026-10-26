# Start here

> ⏱ About 5 min

This is the group's onboarding material, shared by all of the group's [research topics](../research/index.md), written for new students and colleagues, especially those with a **computer-science background and no biology**. After reading it you should understand how kidney single-cell data is made, what it looks like, where its traps are, and what problem we are working on. The deep-reads in the paper library will then be readable without getting stuck on background.

## Roadmap

Day 1 takes about 6 hours and gets you to the point of understanding the data. Day 2 is optional: run code and start on the papers. Each module stands on its own, but reading in order is easiest.

| Module | Time | You will be able to answer |
|---|---|---|
| [1 · Two tables: X and obs](01-two-tables.md) | 30 min | What is a row, a column, a label? |
| [2 · Cells and RNA](02-cells-rna.md) | 30 min | Where is RNA in a cell; cell type vs cell state? |
| [3 · The kidney](03-kidney.md) | 45 min | What are PT and TAL, and why do they get injured first? |
| [4 · Patients and tissue](04-patients-tissue.md) | 30 min | Why do healthy donors also have "abnormal" cells? |
| [5.1 · Assays: tissue to matrix](05-1-assays-rna.md) | 45 min | How do barcodes and UMIs turn tissue into X, and what does single-cell vs single-nucleus cost? |
| [5.2 · Assays: ATAC, multiome, spatial](05-2-assays-more.md) | 45 min | What other matrices exist besides RNA, and how are pooled people told apart? |
| [6 · Artifacts](06-artifacts.md) | 60 min | Is an abnormal row disease, a measurement artifact, handling or batch? |
| [7 · How to read a dataset](07-datasets.md) | 40 min | Which questions decide whether a dataset is usable? |
| [8 · What we are working on](08-our-problem.md) | 20 min | What do our research topics ask? |
| [9 · Hands-on](09-hands-on.md) | Day 2, 3 h | Load the data and reproduce a first result |
| [10 · What to read next](10-next-reading.md) | Day 2, 3 h | Which papers to read, in which order |

## How each module is laid out

- Each module opens with the questions you will **be able to answer**. Skim them first and read with them in mind.
- The text goes **step by step**, and every concept says where it ends up in the data: which rows or columns of the matrix, or which field of the label table.
- **Computer analogy** boxes translate biology into things you already know (source code, processes, batches, ID collisions…).
- **Biology note** boxes explain biology terms that come up in passing (such as gene names), with links for reading further.
- Each module ends with 2–3 **self-check questions** (answers hidden until you open them) and a **terms in this module** table, linked to the [glossary](glossary.md).
- Numbers come from data we checked ourselves (for example the label tables downloaded from GEO), not from memory. Figures are CC-licensed originals with their authors named.

## What is not here

Onboarding covers **background** only. Facts about each dataset are under **[Datasets](../datasets/index.md)**, what each topic is doing is under **[Research topics](../research/index.md)**, and deep-reads, the literature review and the knowledge map are under **Papers**; module 10 tells you what to read and in which order.

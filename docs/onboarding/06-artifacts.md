# 6 · Artifacts, and biology that looks like one

> ⏱ About 1 h · Day 1 · Understand

!!! abstract "After this module you can answer"
    - How do doublets, ambient RNA, low-quality cells and dissociation stress arise?
    - What do they look like in the data, and why can they pass for disease?
    - Which real biological states can pass for artifacts?

This module answers one question: **when a row of X looks abnormal, is it disease, or something else?**

"Something else" comes in three kinds, covered one by one below:

- **Measurement artifacts**: the cell was fine, but the measurement left a row that does not represent it.
- **Handling-induced changes**: the cell really changed, but lab handling caused it, not disease.
- **Batch effects**: not a problem of one row, but a whole batch of data shifted together.

The difficulty is that they often look just like real disease in the data. So we go in three steps:

1. **Where non-disease changes come from**: what the data-making process assumes, and which assumption each change breaks;
2. **Check by what you see**: for each pattern, the non-disease reading and the biology reading side by side, and what tells them apart;
3. **What this means for QC**: what the usual filtering steps remove.

## Step 1 · Where non-disease changes come from

The data is made like this (module 5 has the details): tissue is digested into single cells (or nuclei are extracted), an instrument wraps them one by one into tiny oil droplets, each droplet gets a **barcode**, and in the end **one barcode = one row of X**.

This assumes several things: **each droplet holds exactly one cell, the cell is intact, the RNA read comes only from that cell, handling does not change the cell, and every batch is measured the same way**. The table lists, by kind, which assumption each change breaks:

| Kind | Change | Assumption broken | What happened |
|---|---|---|---|
| measurement artifact | empty droplet | exactly one cell | no cell, only RNA floating in the liquid |
| measurement artifact | doublet | exactly one cell | two cells in one droplet, sharing a barcode |
| measurement artifact | low-quality cell | the cell is intact | the cell broke and lost part of its RNA |
| measurement artifact | ambient RNA | RNA only from this cell | RNA released by broken cells, the "soup", gets into every droplet |
| handling-induced | dissociation stress | handling does not change the cell | digestion at 37 °C makes the cell switch on stress genes |
| batch | batch effect | every batch measured the same way | a different date, reagent lot or assay shifts a whole batch |

How the three kinds differ:

- **Measurement artifacts** affect individual rows; the row does not represent the cell's real state. This is what "artifact" means in the strict sense.
- In **dissociation stress**, the RNA change really happened, only after the tissue left the body. The literature often calls it a "dissociation artifact" too, because it is not the state we want to measure.
- A **batch effect** affects every row of a batch. It contains purely technical shifts and possibly real differences (single-nucleus and single-cell assays capture different parts of the RNA, module 5). It acts more like a **confounder**: the danger is when it lines up with disease.

One more kind of noise fits none of the three but is everywhere: **technical dropout**. As module 1 said, most of X is 0, and many of those zeros mean "not caught", not "not expressed". A single gene at 0 is not evidence.

!!! tip "Computer analogy"
    Think of each droplet as a log file meant for one server.

    - **Measurement artifacts**: an **empty droplet** is an empty file; a **doublet** is two servers writing to the same file; a **low-quality cell** is a server that crashed halfway; **ambient RNA** is leftover logs on a shared disk leaking into every file.
    - **Handling-induced**: **dissociation stress** is the monitoring probe itself driving the server's CPU up. The CPU really is high, but the probe caused it, not the workload.
    - **Batch effect**: a new log format or collection script changes a whole batch of files.

## Step 2 · Check by what you see

In practice you first see a **pattern** in a row, not its cause. Below, the patterns are listed one by one, each with two readings: non-disease and biological (disease).

### Pattern A · Few genes, high mitochondrial fraction

- **Non-disease reading**: a low-quality cell or an empty droplet. The cell broke and lost cytoplasmic RNA, so `nCount_RNA` and `nFeature_RNA` are low; what stays is mostly mitochondrial RNA, so `percent.mt` is high.
- **Biology reading**: injured, degenerating cells look the same. In Lake 2023's single-nucleus data, degenerative nuclei have exactly fewer genes and more mitochondrial RNA (see the known issues on the [Lake 2023 dataset page](../datasets/lake-2023.md)).
- **What tells them apart**: totals alone cannot. Check whether injury-related genes go up, rather than everything going down.

### Pattern B · Markers of two cell types in one row

For example, one nucleus with both PT's `LRP2` and TAL's `UMOD`.

- **Non-disease reading**: a doublet (a PT and a TAL nucleus in one droplet), or ambient RNA (a TAL nucleus picked up PT RNA from the soup, which is dominated by the most common cell type). Single-nucleus data is usually more contaminated than single-cell data; see [Janssen 2023](../datasets/janssen-2023.md).
- **Biology reading**: real transitioning or repairing cells express genes of both states.
- **What tells them apart**: expression alone hardly can. The most reliable signal is **genotype**: when several people's samples are pooled, only a droplet carrying two people's DNA differences (SNPs) is a true doublet.

Hoeft 2024 did exactly this: nuclei from 4 patients were pooled, then assigned to people by SNPs. The right half of the figure shows the result: in the cluster that expression called "Mixed/Doublets", most nuclei come from a single person, and true doublets (dark grey) are few. **Judging artifacts from expression alone is easy to get wrong.** The numbers are on the [Hoeft 2024 dataset page](../datasets/hoeft-2024.md).

![Hoeft 2024 Fig. 2 i–j: expression clusters vs genotype-based donor assignment / 表达聚类和按基因型分人的对照](img/hoeft2024_fig2ij.jpg)

Figure: Hoeft 2024 Fig. 2 i–j (kidney part, cropped). Left: expression clusters of the pooled kidney sample; right: share of each patient, doublets (dark grey) and unassigned nuclei (light grey) per cluster; the left-hand SoupLadle group is enough. Hoeft K et al., Nat Commun 2024, CC BY 4.0.

### Pattern C · Very many RNA molecules

- **Non-disease reading**: a doublet, two cells' RNA added together.
- **Biology reading**: polyploid or multinucleated cells. After injury, some tubular cells carry extra DNA copies and some podocytes become binucleated, so they have more RNA.
- **What tells them apart**: genotype again; also the cell type, since such cells occur mainly in tubules and podocytes after injury.

### Pattern D · Stress genes up

- **Non-disease reading**: dissociation stress. Digestion at 37 °C switches on `FOS`, `JUN` and heat-shock genes; fragile cells (podocytes, for example) are also largely lost during digestion.
- **Biology reading**: tissue injury, or ischaemia during collection (module 4), switches on the same family of genes. Lake 2023's degenerative state includes `FOS` / `JUN`; healthy donors carry many altered cells too, which the authors suggest may partly come from procurement ischaemia or normal ageing.
- **What tells them apart**: a control experiment that changes only the handling. The same mouse kidney digested cold on ice has far lower stress genes; see [Denisenko 2020](../datasets/denisenko-2020.md). Similar stress clusters have been seen in human kidney; see [Lake 2019](../datasets/lake-2019.md).

### Pattern E · One cell type splits by batch

- **Non-disease reading**: a batch effect; each `library` or assay is shifted on its own.
- **Biology reading**: if patients and healthy donors happened to be run in separate batches, "batch" and "disease" are mixed up and cannot be told apart.
- **What tells them apart**: the experimental design, measuring the same tissue with several assays or in several batches. [mBDRC 2026](../datasets/mbdrc-2026.md) did this with healthy tissue and three assays: the assay made a bigger difference than the person did.

## Step 3 · Summary

| Pattern | Non-disease reading | Biology reading | What tells them apart |
|---|---|---|---|
| A · few genes, high `percent.mt` | low-quality cell, empty droplet | injured, degenerating cell | injury genes up, not just counts down |
| B · markers of two cell types | doublet, ambient RNA / doublet、ambient | transitioning, repairing cell | genotype when donors are pooled |
| C · very many RNA molecules | doublet | polyploid, binucleated cell | genotype; cell type |
| D · stress genes up | dissociation stress | injury, ischaemia | same tissue, cold vs warm digestion |
| E · one cell type splits by batch | batch effect | disease, if confounded with batch | same tissue, several assays or batches |

Look at the last column: **what really tells them apart is almost always information from the experimental design** (genotypes, several assays, cold vs warm digestion), not the expression profile itself. That is why the [Datasets](../datasets/index.md) tab has a group of "measurement control" datasets.

## Step 4 · What this means for QC

Most analysis pipelines start with **quality control** (QC), using the three columns from module 1 to remove suspicious rows. Matched to the patterns above:

- `nFeature_RNA` too low or `percent.mt` too high → removed (pattern A), **and injured cells go with them**;
- `nCount_RNA` too high, or a high doublet-tool score → removed (patterns B and C), **and polyploid or transitioning cells may go too**;
- a tool estimates and subtracts the ambient counts (pattern B).

There are no universal thresholds; they differ by dataset and assay.

!!! warning "For our problem, QC is part of the question"
    Standard pipelines treat QC as cleaning: remove and move on. But every filtering rule above may also remove the diseased cells we most want to find. So we cannot assume that data after QC is clean: telling non-disease changes from real disease is exactly the problem we work on (module 8).

## Self-check

??? question "1. A nucleus has both PT's `LRP2` and TAL's `UMOD`. What could it be, and how would you tell?"
    Artifacts: a doublet or ambient RNA. Biology: a real transitioning cell. Expression alone can hardly tell; if donors were pooled, genotypes show whether it is a doublet.

??? question "2. Why can't we simply apply standard QC thresholds and then run anomaly detection?"
    Injured, degenerating cells look like low-quality cells (fewer genes, more mitochondrial RNA), and polyploid cells after injury look like doublets. A hard threshold removes the diseased cells we want to find.

??? question "3. Both dissociation stress and tissue injury raise `FOS`. What data helps you tell them apart?"
    A controlled experiment that changes only the handling, for example the same kidney digested at 37 °C and on ice (Denisenko 2020).

## Terms in this module

| English | 中文 | In one sentence |
|---|---|---|
| [Artifact (technical artifact)](glossary.md#technical-artifact) | 伪影（技术伪影） | A change in the data that does not come from the cell's real state in the body, such as empty droplets, doublets, low-quality cells or ambient RNA; in a broader sense also handling-induced changes such as dissociation stress. |
| [Empty droplet](glossary.md#empty-droplet) | 空液滴 | A droplet without a cell; it captures only free-floating RNA, so it samples the ambient profile. Present in the raw matrix, removed from the filtered one. |
| [Doublet](glossary.md#doublet) | 双细胞假象(doublet) | A technical artifact where two cells or nuclei are captured under one barcode and analysed as a single cell, producing a chimeric expression profile that can masquerade as a novel cell state. |
| [Low-quality cell](glossary.md#low-quality-cell) | 低质量细胞 | A dying or broken cell with few RNA molecules and genes and a high mitochondrial fraction; usually filtered by QC thresholds, but injured cells can look similar. |
| [Ambient RNA](glossary.md#ambient-rna) | 游离 RNA 污染(ambient RNA) | Free-floating transcripts released by lysed cells that get counted into other droplets, adding a background signal that makes unrelated cells look alike. |
| [Dissociation stress](glossary.md#dissociation-stress) | 解离应激 | Stress genes (FOS, JUN, heat-shock genes) switched on while tissue is digested at 37 °C; makes cells look injured although the injury happened in the lab. |
| [Batch effect](glossary.md#batch-effect) | 批次效应 | Systematic non-biological variation between datasets acquired at different sites, times, or platforms that can confound analysis if not corrected. |
| [Confounder (confounding)](glossary.md#confounder) | 混杂因素 | A factor that varies together with the label, so a model cannot tell which one it learned; for example, patients and healthy donors measured in separate batches confound batch with disease. |
| [Technical dropout (false zero)](glossary.md#technical-dropout) | 技术性丢失(假零) | A zero in a count matrix caused by failed capture rather than absent expression; because true and false zeros are indistinguishable, sparsity is both biology and noise at once. |
| [Mitochondrial fraction (percent.mt)](glossary.md#mitochondrial-fraction) | 线粒体比例 | The share of a cell's RNA from mitochondrial genes; a standard QC metric (high = stressed or dying cell). Naturally higher in whole cells than in nuclei. |
| [Quality control (QC)](glossary.md#quality-control) | 质控（QC） | The first step of most single-cell analyses: rows with too few genes, too high a mitochondrial fraction or too many RNA molecules are removed and ambient counts subtracted; thresholds differ by dataset and can also remove injured cells. |
| [Polyploidy / multinucleation](glossary.md#polyploidy) | 多倍体 / 多核 | Cells with extra DNA copies or more than one nucleus; after injury some tubular cells become polyploid and some podocytes binucleated. In single-cell data such cells can look like doublets. |

# 6 · Artifacts, and biology that looks like one

> ⏱ About 45 min · Day 1 · Understand

!!! abstract "After this module you can answer"
    - How do doublets, ambient RNA, low-quality cells and dissociation stress arise?
    - What do they look like in the data, and why can they pass for disease?
    - Which real biological states can pass for artifacts?

## Content

!!! note "In progress"
    The text of this module is being written.

## Terms in this module

| English | 中文 | In one sentence |
|---|---|---|
| [Doublet](glossary.md#doublet) | 双细胞假象(doublet) | A technical artifact where two cells or nuclei are captured under one barcode and analysed as a single cell, producing a chimeric expression profile that can masquerade as a novel cell state. |
| [Ambient RNA](glossary.md#ambient-rna) | 游离 RNA 污染(ambient RNA) | Free-floating transcripts released by lysed cells that get counted into other droplets, adding a background signal that makes unrelated cells look alike. |
| [Empty droplet](glossary.md#empty-droplet) | 空液滴 | A droplet without a cell; it captures only free-floating RNA, so it samples the ambient profile. Present in the raw matrix, removed from the filtered one. |
| [Low-quality cell](glossary.md#low-quality-cell) | 低质量细胞 | A dying or broken cell with few RNA molecules and genes and a high mitochondrial fraction; usually filtered by QC thresholds, but injured cells can look similar. |
| [Mitochondrial fraction (percent.mt)](glossary.md#mitochondrial-fraction) | 线粒体比例 | The share of a cell's RNA from mitochondrial genes; a standard QC metric (high = stressed or dying cell). Naturally higher in whole cells than in nuclei. |
| [Dissociation stress](glossary.md#dissociation-stress) | 解离应激 | Stress genes (FOS, JUN, heat-shock genes) switched on while tissue is digested at 37 °C; makes cells look injured although the injury happened in the lab. |
| [Technical dropout (false zero)](glossary.md#technical-dropout) | 技术性丢失(假零) | A zero in a count matrix caused by failed capture rather than absent expression; because true and false zeros are indistinguishable, sparsity is both biology and noise at once. |
| [Batch effect](glossary.md#batch-effect) | 批次效应 | Systematic non-biological variation between datasets acquired at different sites, times, or platforms that can confound analysis if not corrected. |
| [Polyploidy / multinucleation](glossary.md#polyploidy) | 多倍体 / 多核 | Cells with extra DNA copies or more than one nucleus; after injury some tubular cells become polyploid and some podocytes binucleated. In single-cell data such cells can look like doublets. |

# 5 · Assays: how the data is made

> ⏱ About 90 min · Day 1 · Understand

!!! abstract "After this module you can answer"
    - What do single-cell and single-nucleus sequencing capture, and at what cost?
    - How do barcodes and UMIs turn reads into a count matrix?
    - What does ATAC measure, and what matrix does it give?
    - Why does measuring two things in the same nucleus (multiome / SNARE2) matter?

## Content

!!! note "In progress"
    The text of this module is being written.

## Terms in this module

| English | 中文 | In one sentence |
|---|---|---|
| [Single-cell RNA sequencing (scRNA-seq)](glossary.md#single-cell-rna-seq) | 单细胞 RNA 测序(scRNA-seq) | A technique that profiles the transcriptome of individual cells, revealing cell-type heterogeneity that bulk sequencing averages away. |
| [Single-nucleus RNA-seq (snRNA-seq)](glossary.md#snrna-seq) | 单核 RNA 测序(snRNA-seq) | Dissociates tissue down to individual nuclei and sequences the RNA in each, giving genome-wide expression per nucleus at the cost of losing every cell's position in the tissue. |
| [Tissue dissociation](glossary.md#tissue-dissociation) | 组织解离 | Breaking tissue into single cells, usually with enzymes at 37 °C, before single-cell RNA-seq; needed for whole cells but stresses them. |
| [10x Chromium (Cv3)](glossary.md#chromium-10x) | 10x Chromium（Cv3 = 第 3 版试剂） | The most common commercial single-cell platform: it packs each cell or nucleus into an oil droplet with a barcoded bead. Cv3 = Chromium v3 chemistry (snCv3 / scCv3 in Lake 2023). |
| [Cell barcode](glossary.md#cell-barcode) | 细胞条形码 | A short DNA tag attached to every RNA from the same droplet (or the same split-pool path), so reads can be sorted back to their cell; becomes the row ID of the count matrix. |
| [UMI (unique molecular identifier)](glossary.md#umi) | UMI（分子唯一标识） | A random tag on each RNA molecule before amplification, so copies made by PCR can be collapsed; the numbers in the count matrix are UMI counts (nCount_RNA = total UMIs per cell). |
| [Single-nucleus ATAC-seq (snATAC-seq)](glossary.md#snatac-seq) | 单核 ATAC 测序(snATAC-seq) | Uses a transposase that cuts only unpacked DNA to map which genomic regions are open per nucleus, revealing which genes are permitted to be expressed rather than which currently are. |
| [Chromatin accessibility](glossary.md#chromatin-accessibility) | 染色质开放性 | How physically reachable a stretch of DNA is for transcription machinery; tightly packed regions are effectively switched off, loosened ones are available for expression. |
| [Tn5 transposase](glossary.md#tn5-transposase) | Tn5 转座酶 | The enzyme used in ATAC-seq: it can only cut into open (unwound) DNA and inserts sequencing adapters as it cuts, so where it cuts marks accessible chromatin. |
| [ATAC peak](glossary.md#atac-peak) | ATAC 峰 | A genomic interval where transposase cut sites pile up across many nuclei, defining a region of open chromatin and forming the row dimension of the peak-by-cell matrix. |
| [Multiome (joint RNA + ATAC)](glossary.md#multiome) | Multiome(RNA 与 ATAC 同核联测) | An assay that measures transcription and chromatin accessibility in the very same nucleus, pairing 'what is expressed' with 'what is permitted' without having to match cells across separate runs. |
| [SNARE-seq2](glossary.md#snare-seq2) | SNARE-seq2（SNARE2） | Single-Nucleus chromatin Accessibility and mRNA Expression sequencing, version 2: measures RNA and ATAC in the same nucleus using split-pool (combinatorial) barcoding instead of droplets; used for 7 healthy donors in Lake 2023. |
| [Spatial transcriptomics](glossary.md#spatial-transcriptomics) | 空间转录组学 | A family of technologies that measure gene expression while preserving each cell's or spot's position within an intact tissue section. |
| [Visium](glossary.md#visium) | Visium | A widely used 10x Genomics spatial-transcriptomics platform that captures gene expression on a grid of barcoded spots overlaid on a tissue slide. |
| [Xenium](glossary.md#xenium) | Xenium | A 10x Genomics imaging-based platform that measures a targeted panel of transcripts in situ at subcellular resolution with single-cell segmentation. |
| [SNP / genotype](glossary.md#snp-genotype) | SNP / 基因型 | Single-base differences between people (or mouse strains); the set a person carries is their genotype, a DNA fingerprint stored in VCF files and measured by WES or arrays. |
| [Genotype multiplexing / demultiplexing](glossary.md#genotype-demultiplexing) | 基因型混样 / 分人 | Pooling cells from several people in one run and sorting them back by SNPs (demuxlet, souporcell, vireo); it also reveals droplets with two people's SNPs (doublets) and foreign RNA (ambient contamination). |

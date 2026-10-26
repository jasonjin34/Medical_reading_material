# 5 · 测法：数据是怎么产生的

> ⏱ 约 90 分钟 · 第 1 天 · 读懂

!!! abstract "读完能回答"
    - 单细胞和单个细胞核测序各测到什么、各有什么代价？
    - 条形码和 UMI 怎么把测序读段变成计数矩阵？
    - ATAC 测的是什么，得到什么矩阵？
    - 为什么“同一个核测两样”（multiome / SNARE2）重要？

## 正文

!!! note "正在编写"
    这一模块的正文还在写。

## 本模块名词

| 中文 | English | 一句话 |
|---|---|---|
| [单细胞 RNA 测序(scRNA-seq)](glossary.md#single-cell-rna-seq) | Single-cell RNA sequencing (scRNA-seq) | 一种对单个细胞转录组进行测序的技术,可揭示被批量测序平均掉的细胞类型异质性。 |
| [单核 RNA 测序(snRNA-seq)](glossary.md#snrna-seq) | Single-nucleus RNA-seq (snRNA-seq) | 把组织解离成单个细胞核并分别测其 RNA,得到每个核的全基因组表达,代价是彻底丢失细胞原本在组织中的位置。 |
| [组织解离](glossary.md#tissue-dissociation) | Tissue dissociation | 做单细胞 RNA 测序前把组织拆成单个细胞，通常用酶在 37 °C 消化；能得到完整细胞，但会让细胞应激。 |
| [10x Chromium（Cv3 = 第 3 版试剂）](glossary.md#chromium-10x) | 10x Chromium (Cv3) | 最常用的商业单细胞平台：把每个细胞或核和一颗带条形码的珠子一起包进油滴。Cv3 = Chromium 第 3 版试剂（Lake 2023 里的 snCv3 / scCv3）。 |
| [细胞条形码](glossary.md#cell-barcode) | Cell barcode | 贴在同一个油滴（或同一条分池路径）里所有 RNA 上的短 DNA 标签，用来把读段分回各个细胞；它就是计数矩阵的行 ID。 |
| [UMI（分子唯一标识）](glossary.md#umi) | UMI (unique molecular identifier) | 扩增前贴在每条 RNA 分子上的随机标签，用来去掉 PCR 复制出的重复；计数矩阵里的数字就是 UMI 数（nCount_RNA = 一个细胞的 UMI 总数）。 |
| [单核 ATAC 测序(snATAC-seq)](glossary.md#snatac-seq) | Single-nucleus ATAC-seq (snATAC-seq) | 用只能切开松散 DNA 的转座酶,逐核绘制哪些基因组区域处于开放状态,揭示哪些基因「有资格」表达,而非当前正在表达什么。 |
| [染色质开放性](glossary.md#chromatin-accessibility) | Chromatin accessibility | 一段 DNA 对转录机器的物理可及程度;缠绕紧密的区域等同于被关闭,松开的区域才可能被表达。 |
| [Tn5 转座酶](glossary.md#tn5-transposase) | Tn5 transposase | ATAC-seq 用的酶：只能剪进打开（没缠紧）的 DNA，剪的同时插入测序接头，所以它剪过的位置标出了开放染色质。 |
| [ATAC 峰](glossary.md#atac-peak) | ATAC peak | 转座酶切点在众多细胞核中反复堆积的基因组区间,标定一段开放染色质,并构成「峰 × 细胞」矩阵的行维度。 |
| [Multiome(RNA 与 ATAC 同核联测)](glossary.md#multiome) | Multiome (joint RNA + ATAC) | 在同一个细胞核里同时测转录与染色质开放性的实验,把「表达了什么」与「允许表达什么」直接配对,无需在两批细胞之间猜对应关系。 |
| [SNARE-seq2（SNARE2）](glossary.md#snare-seq2) | SNARE-seq2 | 单核染色质可及性与 mRNA 表达测序第 2 版：在同一个核里同时测 RNA 和 ATAC，用分池混合编码代替油滴；Lake 2023 用它测了 7 个健康人。 |
| [空间转录组学](glossary.md#spatial-transcriptomics) | Spatial transcriptomics | 一类在保留细胞或位点在完整组织切片中位置的同时测量基因表达的技术。 |
| [Visium](glossary.md#visium) | Visium | 一种广泛使用的 10x Genomics 空间转录组平台,在覆盖组织切片的条形码位点阵列上捕获基因表达。 |
| [Xenium](glossary.md#xenium) | Xenium | 一种基于成像的 10x Genomics 平台,在亚细胞分辨率下原位测量目标转录本组合,并进行单细胞分割。 |
| [SNP / 基因型](glossary.md#snp-genotype) | SNP / genotype | 人与人（或小鼠品系之间）单个碱基的差异；一个人带的这一整套就是他的基因型，相当于 DNA 指纹，存成 VCF 文件，用 WES 或芯片测得。 |
| [基因型混样 / 分人](glossary.md#genotype-demultiplexing) | Genotype multiplexing / demultiplexing | 把几个人的细胞混在一次实验里测，事后按 SNP 分回各人（demuxlet、souporcell、vireo）；同时能发现带两个人 SNP 的液滴（doublet）和外来 RNA（ambient 污染）。 |

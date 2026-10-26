# 5.2 · 测法：ATAC、多模态、空间、混样

> ⏱ 约 45 分钟 · 第 1 天 · 读懂

!!! abstract "读完能回答"
    - ATAC 测的是什么，得到什么矩阵？
    - 为什么“同一个核测两样”（multiome / SNARE2）重要？
    - 空间测序多给了什么信息？
    - 几个人的样本混在一次上机里，怎么把细胞分回各自的人？

5.1 讲的 RNA 测法回答"细胞**此刻**在用哪些基因"。这一页讲另外几种测法：它们测的不是 RNA，或者在 RNA 之外多记了一样东西。每一种最后也都是一张矩阵。本页标 [n] 的来自文献。

## 第 1 步 · DNA 有"开"和"关"

模块 2 说过，细胞核里存着 DNA，也就是全部源代码。但 DNA 不是一根光秃秃的线：它一段一段地缠在一种蛋白质小球上，这个小球加上缠在上面的 DNA 叫**核小体**（nucleosome）。

- 有的区域核小体挤得很紧，DNA 被包住，别的分子够不着，叫**关闭**的染色质；
- 有的区域核小体稀疏，DNA 露在外面，叫**开放**的染色质。正在使用的基因，它开头那一段（启动子）通常就是开放的，那里没有核小体 [1]。

下图最上面一行画的就是这两种状态：左边挤在一起的蓝色小球是关闭区，右边稀疏的、旁边有一个 Gene 的是开放区。

![ATAC-seq: Tn5 cuts and tags open chromatin; sequenced fragments pile up into peaks over open regions / ATAC-seq：Tn5 在开放区剪开并贴上接头，测序片段在开放区堆成 peak](img/atac_seq.png)

图：Wikimedia「Figure.1 ATAC-Seq illustration」，Deema108，CC BY-SA 4.0。

!!! tip "计算机类比"
    把 DNA 想成一个很大的代码仓库。大部分文件被压缩归档了（关闭），程序想用也读不到；少数文件已经解压、放在工作目录里（开放），随时可以运行。RNA 测的是"**哪些程序正在运行**"，ATAC 测的是"**哪些文件已经解压、可以运行**"。这是一个帮助理解的类比，两者的真实关系比这复杂。

## 第 2 步 · Tn5：只在开放的地方下刀

ATAC 的全称是 Assay for Transposase-Accessible Chromatin，意思是"用转座酶测哪些染色质够得着"。核心工具是一种改造过的酶 **Tn5**，对应上图第二行的绿色小块：

1. Tn5 事先装好两段测序**接头**（图中红色和蓝色的小尾巴）；
2. 它在 DNA 上**一边剪断、一边把接头插进去**，这一步叫 tagmentation [1]；
3. 关闭区的 DNA 被核小体挡着，Tn5 很难插进去；开放区就容易得多 [1]。

所以最后能测到的 DNA 片段，几乎都来自开放区。**测到片段的位置，就是开放区的位置。**

## 第 3 步 · 从片段到 peak，再到矩阵

把很多片段比对回基因组，开放区那里的片段会**堆起来**，形成一个个小山峰，叫 **peak**（上图最下面一行）。

单个细胞核的情况特殊：一段调控区域在二倍体基因组里只有**两份拷贝**，所以一个核在一个位置上最多只能测到很少几个片段，结果几乎是**0 或 1** [2]。这让单细胞 ATAC 数据**极其稀疏**，看单个位置、单个核基本没有意义；但把几百个核加在一起，就和用几千万个细胞做出来的结果很像 [2]。

最后得到一张矩阵：**一行 = 一个细胞核，一列 = 一个 peak（基因组上的一段区间）**，数字是落在这段区间里的片段数。它和 RNA 矩阵最大的不同是：**列不是基因**，而是一段坐标，比如 `chr2:169,200,000-169,200,500`。

!!! warning "初学者最容易误会的一点"
    在单个核里，某个 peak 是 0，**不等于**那里是关闭的，很可能只是没测到。判断"开不开"要看一群同类的核加起来的结果。

## 第 4 步 · 同一个核测两样：SNARE2

假如 RNA 和 ATAC 分别来自**两批不同的核**：你手里有两张表，行是两套不同的 barcode，没法直接对上。只能靠算法猜"这个 RNA 核和那个 ATAC 核大概是同一类细胞"。

**SNARE-seq2**（Lake 2023 里简称 SNARE2）在**同一个核**里先做 ATAC 的 tagmentation，再抓 RNA；然后通过几轮"分开—加一段 barcode—合并"（split-pool），让同一个核的 RNA 和 ATAC 片段带上**同一个 barcode 组合** [3]。这样两张表的行就是同一套核，可以直接一行对一行。模块 4 那张 Lake Fig. 1a 截图里，SNARE2 下面的 BC1、BC2、BC3 就是这三轮加上去的 barcode。

下图把两张表画在一起，和模块 1 的 X / obs 图是同一种画法：

<figure class="xobs" markdown="0"><div class="xo-scroll"><table aria-label="同一个核的 RNA 和 ATAC 两个矩阵按行对齐">
<thead><tr class="xo-cap"><th></th><th colspan="3"><span class="xo-tag">RNA</span>RNA 计数 <span class="xo-sub">· 核 × 基因</span></th><th></th><th colspan="3"><span class="xo-tag">ATAC</span>ATAC 计数 <span class="xo-sub">· 核 × peak</span></th><th></th><th></th></tr>
<tr class="xo-genes"><th></th><th>LRP2<i style="background:var(--xo-pt)"></i></th><th>UMOD<i style="background:var(--xo-tal)"></i></th><th>NPHS2<i style="background:var(--xo-pod)"></i></th><th></th><th>chr2:169.2M<i style="background:var(--xo-pt)"></i></th><th>chr16:20.3M<i style="background:var(--xo-tal)"></i></th><th>chr1:179.6M<i style="background:var(--xo-pod)"></i></th><th></th><th class="xo-o">细胞类型</th></tr></thead><tbody>
<tr tabindex="0"><td class="xo-bc">AAACAGCC…</td><td class="xo-x"><b style="--c:var(--xo-pt);--a:65%">11</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-seam"><div></div></td><td class="xo-x"><b style="--c:var(--xo-pt);--a:65%">1</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-seam"><div></div></td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-pt)">PT</span></td></tr>
<tr tabindex="0"><td class="xo-bc">AAACATGC…</td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-tal);--a:80%">19</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-seam"><div></div></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-tal);--a:85%">2</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-seam"><div></div></td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-tal)">TAL</span></td></tr>
<tr tabindex="0"><td class="xo-bc">AAACCAAC…</td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-pod);--a:50%">5</b></td><td class="xo-seam"><div></div></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-pod);--a:65%">1</b></td><td class="xo-seam"><div></div></td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-pod)">POD</span></td></tr>
<tr tabindex="0"><td class="xo-bc">AAACCGAA…</td><td class="xo-x"><b style="--c:var(--xo-pt);--a:56%">7</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-seam"><div></div></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-seam"><div></div></td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-pt)">PT</span></td></tr>
</tbody></table></div>
<p class="xo-hint">点击图片放大，再点一次或按 Esc 关闭</p>
<figcaption>示意数据。左右两张表来自同一批细胞核，所以行是同一套 barcode。ATAC 的列不是基因，而是基因组上的一段区间（这里用染色体和大致位置表示，例如 chr2:169.2M 指 2 号染色体约 1.692 亿碱基处；这三段分别落在 LRP2、UMOD、NPHS2 基因上，位置取自 Ensembl 的 GRCh38），数字大多是 0、1、2。第 4 行的 PT 核有 LRP2 的 RNA，但这一段区间上没测到 ATAC 片段：ATAC 数据非常稀疏，单个核里没测到不代表那里是关着的。</figcaption></figure>

**在数据里**：Lake 2023 的 SNARE2 有 104,809 个核，但只来自 7 名健康人（见 [Lake 2023 数据集页](../datasets/lake-2023.md)）。所以如果想同时看 RNA 和 ATAC，就只有健康人的数据。Lake 2023 用 SNARE2 的 ATAC 部分找调控区域，并推断了 TAL 的基因调控网络 [4]；单细胞和 SNARE2 的细胞类型标签，是把它们对齐到单核数据上得到的 [4]。

## 第 5 步 · 空间：保留位置

前面所有方法都要先把组织拆散，**细胞原来在哪里**就丢了。空间转录组的思路是：把一张组织切片直接铺在一块芯片上，芯片上排满了带**位置 barcode** 的引物，切片里的 RNA 被抓住时就记下了自己在哪个位置 [5]。

- **Visium**：芯片上是一个个圆点，Lake 2023 写的点（原文叫 bead）直径是 55 µm [4]。一个点通常盖住好几个细胞，所以一个点的表达是几个细胞的混合，需要用单细胞数据去"拆"出点里有哪些细胞类型 [6]。
- **Xenium**：直接在切片上成像，分辨率可以到细胞内部，但只测**事先选好的一组基因**，比如 Janesick 2023 用的是 313 个基因 [6]。

空间数据多了一张**坐标表**：每个点（或细胞）一行，记录它在切片上的 x、y。Lake 2023 有 Visium 数据，我们目前的工作不用。

## 第 6 步 · 多人混样：用 SNP 把细胞分回每个人

有时为了省钱、减少批次差异，会把**几个人的细胞混在一起**上一次机 [8]。测完以后怎么知道每个细胞是谁的？

靠每个人 DNA 上天然的小差别，叫 **SNP**（单核苷酸多态性）：同一个位置，有的人是 A，有的人是 G。测序读段里带着这些位置，就能像比对指纹一样，判断一个油滴里的细胞来自哪个人 [7, 8]：

- **demuxlet** 需要事先知道每个人的基因型。模拟实验里，每个细胞有 50 个 SNP 就能把 97% 的单个细胞分对，在多达 64 人的混样里也是如此 [7]。
- **souporcell** 不需要事先的基因型，直接按读段里的变异把细胞聚成几群 [8]。

顺带的好处：如果一个油滴里同时出现**两个人**的 SNP，那它一定是 doublet [7, 8]，而这种 doublet 光看表达谱可能发现不了 [8]。

**在数据里**：混样上机的数据，obs 里的 `patient` 这一列就是这样算出来的，而不是实验时直接记下的。一份数据是不是混样，要看它的方法部分。

## 总表：5.1 和 5.2 的所有测法

| 测法 | 一行 | 一列 | 主要偏差 | In Lake 2023 |
|---|---|---|---|---|
| scRNA-seq (scCv3) | 细胞 | 基因 | 消化应激、线粒体比例高、丢细胞类型 | 109,741 cells |
| snRNA-seq (snCv3) | 细胞核 | 基因 | 没有胞质 RNA、淋巴细胞偏少 | 203,702 nuclei |
| snATAC-seq | 细胞核 | peak（基因组区间） | 极其稀疏、近乎 0/1 | in SNARE2 |
| SNARE2 (RNA + ATAC) | 细胞核 | 基因 + peak | Lake 里只有健康人 | 104,809 nuclei |
| Visium | 点 | 基因 | 一个点混了几个细胞 | yes, not used by us |
| Xenium | 细胞 | 预选基因 | 只测选定的基因 | — |
| SNP demultiplexing | — | — | 给出 `patient`，找跨人 doublet | — |

表中数字见 5.1 和 [Lake 2023 数据集页](../datasets/lake-2023.md)；偏差的出处见 5.1 和本页各步。

## 自测

??? question "1. ATAC 矩阵的一列是什么？和 RNA 矩阵有什么不同？"
    一列是一个 peak，也就是基因组上的一段区间（坐标），不是基因。数字是落在这段区间里的片段数，单个核里几乎只有 0 或 1。

??? question "2. 一个核在某个 peak 上是 0，能说明那里是关闭的吗？"
    不能。单细胞 ATAC 极其稀疏，0 很可能只是没测到。要把一群同类的核加起来看。

??? question "3. SNARE2 比\"RNA 和 ATAC 分开测\"好在哪里？"
    两者来自同一个核、带同一个 barcode，所以两张表的行可以直接一一对应；分开测时只能靠算法猜哪些核对得上。

??? question "4. 混样上机时，怎么知道一个细胞属于谁？顺便还能发现什么？"
    用读段里的 SNP 像指纹一样比对（demuxlet、souporcell）。同一个油滴里出现两个人的 SNP，就说明它是 doublet。

## 参考文献

1. Buenrostro JD, Giresi PG, Zaba LC, et al. Transposition of native chromatin for fast and sensitive epigenomic profiling of open chromatin, DNA-binding proteins and nucleosome position. *Nat Methods* 2013;10:1213–1218. [doi:10.1038/nmeth.2688](https://doi.org/10.1038/nmeth.2688) — Results (Tn5 tagmentation; steric hindrance in less accessible chromatin; nucleosome-free promoter at active TSSs).
2. Buenrostro JD, Wu B, Litzenburger UM, et al. Single-cell chromatin accessibility reveals principles of regulatory variation. *Nature* 2015;523:486–490. [doi:10.1038/nature14590](https://doi.org/10.1038/nature14590) — abstract; Results (two copies in a diploid genome, near-digital 0/1; sparse data).
3. Plongthongkum N, Diep D, Chen S, et al. Scalable dual-omics profiling with single-nucleus chromatin accessibility and mRNA expression sequencing 2 (SNARE-seq2). *Nat Protoc* 2021;16:4992–5029. [doi:10.1038/s41596-021-00507-3](https://doi.org/10.1038/s41596-021-00507-3) — abstract.
4. Lake BB, Menon R, Winfree S, et al. An atlas of healthy and injured cell states and niches in the human kidney. *Nature* 2023;619:585–594. [doi:10.1038/s41586-023-05769-3](https://doi.org/10.1038/s41586-023-05769-3) — Results (SNARE2 regulatory elements and TAL GRNs; anchoring scCv3 and SNARE2 to snCv3; 55 µm Visium beads). Deep-read: [Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md).
5. Ståhl PL, Salmén F, Vickovic S, et al. Visualization and analysis of gene expression in tissue sections by spatial transcriptomics. *Science* 2016;353:78–82. [doi:10.1126/science.aaf2403](https://doi.org/10.1126/science.aaf2403) — abstract.
6. Janesick A, Shelansky R, Gottscho AD, et al. High resolution mapping of the tumor microenvironment using integrated single-cell, spatial and in situ analysis. *Nat Commun* 2023;14:8353. [doi:10.1038/s41467-023-43458-x](https://doi.org/10.1038/s41467-023-43458-x) — Results (313-gene Xenium panel; subcellular resolution; deconvolving cell types in Visium spots).
7. Kang HM, Subramaniam M, Targ S, et al. Multiplexed droplet single-cell RNA-sequencing using natural genetic variation. *Nat Biotechnol* 2018;36:89–94. [doi:10.1038/nbt.4042](https://doi.org/10.1038/nbt.4042) — abstract.
8. Heaton H, Talman AM, Knights A, et al. Souporcell: robust clustering of single-cell RNA-seq data by genotype without reference genotypes. *Nat Methods* 2020;17:615–620. [doi:10.1038/s41592-020-0820-1](https://doi.org/10.1038/s41592-020-0820-1) — abstract (why donors are pooled; cross-genotype doublets).

## 本模块名词

| 中文 | English | 一句话 |
|---|---|---|
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

# 5.2 · 测法：ATAC、多模态、空间、混样

> ⏱ 约 45 分钟 · 第 1 天 · 读懂

!!! abstract "读完能回答"
    - ATAC 测的是什么，得到什么矩阵？
    - 为什么“同一个核测两样”（multiome / SNARE2）重要？
    - 空间测序（spatial sequencing）多给了什么信息？
    - 几个人的样本混在一次上机里，怎么把细胞分回各自的人？

5.1 讲的 RNA 测法回答"细胞**此刻**在用哪些基因"。这一页讲另外几种测法（assay）：它们测的不是 RNA，或者在 RNA 之外多记了一样东西。每一种最后也都是一张矩阵。本页标 [n] 的来自文献。

## 第 1 步 · DNA 有开和关

模块 2 说过，细胞核里存着 DNA。把 DNA 想成一根很长的线，上面写满"说明书"，也就是基因。细胞把这根线一段一段缠在小线轴上；一个线轴加上缠在它上面的 DNA，叫**核小体**（nucleosome）。DNA 连同这些线轴，合称染色质（chromatin）。

- 缠得紧的地方，线被裹住，谁也碰不到。这部分暂时不用，叫**关闭**（closed）。
- 缠得松、线露在外面的地方，细胞随时可以读，叫**开放**（open）。正在用的基因，开头那一小段（启动子，promoter）通常就露在外面，上面没有线轴 [1]。

**哪里开着，说明细胞在用、或者准备用那部分说明书。**开着的地方不只是基因的开头，还有基因附近那些控制它的调控区域（regulatory region）。一段 DNA 开不开，叫染色质开放性（chromatin accessibility），ATAC 测的就是它。

下图最上面一行就是这两种状态：左边挤在一起的蓝色小球是关闭区，右边稀疏、旁边标着 Gene 的是开放区。

![ATAC-seq: Tn5 cuts and tags open chromatin; sequenced fragments pile up into peaks over open regions / ATAC-seq：Tn5 在开放区剪开并贴上接头，测序片段在开放区堆成 peak](img/atac_seq.png)

图：Wikimedia「Figure.1 ATAC-Seq illustration」，Deema108，CC BY-SA 4.0。

!!! tip "计算机类比"
    把 DNA 想成一个很大的代码仓库。大部分文件被压缩归档了（关闭），程序想用也读不到；少数文件已经解压在工作目录里（开放），随时可以运行。这只是帮助理解的类比，真实情况比这复杂。

## 第 2 步 · Tn5：只剪露在外面的线

ATAC 的全称是 Assay for Transposase-Accessible Chromatin，意思是"用转座酶（transposase）看哪些染色质够得着"。它的工具是一种改造过的酶，叫 **Tn5**，就是上图第二行的绿色小块。

把 Tn5 想成一把**只能剪露在外面的线**的剪刀：

- 它剪断 DNA 的同时，在断口贴上一个标签：测序用的**接头**（adapter），图中红色和蓝色的小尾巴。边剪边贴这一步叫 tagmentation [1]。
- 缠在线轴里的线被核小体挡着，它够不着；露在外面的线才剪得到 [1]。

所以剪下来的碎片（fragment）几乎都来自开放区。**哪里碎片多，哪里就开着。**

单细胞 ATAC 还要知道每个碎片来自哪个核：和 5.1 一样，每个核的碎片都带上这个核自己的 barcode，测完再按 barcode 分回各个核。

## 第 3 步 · 从碎片到 peak，再到矩阵

**碎片从哪来：比对回基因组。**测序后，每个碎片就是一小串字母（A、C、G、T）。人类的参考基因组（reference genome）像一本约 30 亿个字母的书。比对（align）就是拿这串字母去书里搜索它是从哪一页、哪一行抄来的，像全文搜索一样。搜到了，就知道这个碎片在基因组上的位置。

**位置怎么写：一个地址。**例如 `chr2:169,200,000-169,200,500` 的意思是：2 号染色体（chromosome，可以想成"第 2 册"），从第 169,200,000 个字母到第 169,200,500 个字母这一段。

**从碎片到矩阵，用 3 个核举例：**

1. 先把 3 个核的碎片全部放在一起，比对回基因组。碎片不是均匀撒开的，而是挤在几段地方（开放区），堆成小山，叫 **peak**（峰；上图最下面一行）。假设它们挤在 A、B、C 三段。
2. 这三段就是矩阵的 3 列。每列的名字就是上面那种地址。
3. 再给每个核分别数：它有几个碎片落在 A、B、C 里。每个核是一行。

| 核 | A 段 | B 段 | C 段 |
|---|---|---|---|
| 核 1 | 1 | 0 | 1 |
| 核 2 | 0 | 1 | 0 |
| 核 3 | 1 | 0 | 0 |

（示意数据。）所以 ATAC 矩阵的**列不是基因，而是基因组上的一段地址**。

**为什么几乎只有 0 和 1？**RNA 是"复印件"：一个基因在一个细胞里可以有几十份。DNA 是"原件"：每一段在一个细胞里只有**两份**，父母各一份（二倍体，diploid）。两份都可能没被剪到，所以一个核在一个位置上最多也只有很少几个碎片 [2]。

后果是：单个核里的 0，分不清是"关着"还是"开着但没剪到"。单细胞 ATAC 因此**极其稀疏**；但把几百个同类的核加在一起，结果就和用几千万个细胞做出来的很像 [2]。

!!! warning "初学者最容易误会的一点"
    单个核里某个 peak 是 0，**不等于**那里关着，很可能只是没剪到。判断开不开，要看一群同类的核加起来的结果。

**一句话：**RNA 看"细胞正在读哪几页说明书"，ATAC 看"哪几页是摊开的、随时能读"。两个一起看，才能推断谁在控制谁；第 4 步会看到 Lake 2023 就是这样用的。

## 第 4 步 · 同一个核测两样：SNARE2

如果 RNA 和 ATAC 来自**两批不同的核**，就像两场不同派对的两份宾客名单：名单上根本不是同一批人，没法一行对一行，只能按"长得像"去猜谁和谁是同一类。

**SNARE-seq2**（single-nucleus chromatin accessibility and mRNA expression sequencing 2；Lake 2023 里简称 SNARE2）在**同一个核**里两样都测：先用 Tn5 剪出 ATAC 碎片，再抓 RNA [3]。难点是怎么让这两种分子都记住"我来自哪个核"。办法是几轮"分组—加一段标签—再合并"（split-pool）：

1. 把核分成很多组，每组加上不同的一段 barcode；
2. 把所有核倒回一起混匀，再重新分组，加第二段；
3. 再来一轮，加第三段。

三轮下来，同一个核里的 RNA 和 ATAC 碎片带的是**同一个 barcode 组合** [3]，而不同的核几乎不会拿到同样的组合。所以两张表的行是同一批核，可以直接一行对一行。模块 4 那张 Lake Fig. 1a 截图里，SNARE2 下面的 BC1、BC2、BC3 就是这三轮加上去的三段标签。

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
<figcaption>示意数据。左右两张表来自同一批细胞核，所以行是同一套 barcode。ATAC 的列不是基因，而是基因组上的一段区间（这里用染色体（chromosome）和大致位置表示，例如 chr2:169.2M 指 2 号染色体约 1.692 亿碱基（base）处；这三段分别落在 LRP2、UMOD、NPHS2 基因上，位置取自 Ensembl 的 GRCh38，即人类参考基因组（reference genome）第 38 版），数字大多是 0、1、2。第 4 行的 PT 核有 LRP2 的 RNA，但这一段区间上没测到 ATAC 片段：ATAC 数据非常稀疏，单个核里没测到不代表那里是关着的。</figcaption></figure>

**在数据里**：Lake 2023 的 SNARE2 有 104,809 个核，但只来自 7 名健康人（见 [Lake 2023 数据集页](../datasets/lake-2023.md)）。也就是说，想同时看 RNA 和 ATAC，手里只有健康人的数据。Lake 2023 用 SNARE2 的 ATAC 部分找调控区域，并推断了 TAL 的基因调控网络（gene regulatory network, GRN）[4]。单细胞和 SNARE2 的细胞类型标签，是把它们对齐（anchoring）到单核数据上得到的 [4]。

## 第 5 步 · 空间：保留位置

前面所有方法都要先把组织拆散，**细胞原来在哪里**就丢了。空间转录组学（spatial transcriptomics）的思路是：把一张组织切片（tissue section）直接铺在一块芯片（slide）上，芯片上排满了带**位置 barcode**（positional barcode）的引物（primer），切片里的 RNA 被抓住时就记下了自己在哪个位置 [5]。

- **Visium**：芯片上是一个个圆点（spot），Lake 2023 写的点（原文叫 bead）直径是 55 µm [4]。一个点通常盖住好几个细胞，所以一个点的表达是几个细胞的混合，需要用单细胞数据去"拆"（deconvolution）出点里有哪些细胞类型 [6]。
- **Xenium**：直接在切片上成像（imaging），分辨率可以到细胞内部（subcellular resolution），但只测**事先选好的一组基因**（gene panel），比如 Janesick 2023 用的是 313 个基因 [6]。

空间数据多了一张**坐标表**（coordinate table）：每个点（或细胞）一行，记录它在切片上的 x、y。Lake 2023 有 Visium 数据，我们目前的工作不用。

## 第 6 步 · 多人混样：用 SNP 把细胞分回每个人

有时为了省钱、减少批次差异（batch effect），会把**几个人的细胞混在一起**（pooling）上一次机 [8]。测完以后怎么知道每个细胞是谁的？

靠每个人 DNA 上天然的小差别，叫 **SNP**（single-nucleotide polymorphism，单核苷酸多态性）：同一个位置，有的人是 A，有的人是 G。测序读段（reads）里带着这些位置，就能像比对指纹一样，判断一个油滴（droplet）里的细胞来自哪个人 [7, 8]：

- **demuxlet** 需要事先知道每个人的基因型（genotype）。模拟实验（simulation）里，每个细胞有 50 个 SNP 就能把 97% 的单个细胞分对，在多达 64 人的混样里也是如此 [7]。
- **souporcell** 不需要事先的基因型，直接按读段里的变异（variant）把细胞聚成几群（clustering） [8]。

顺带的好处：如果一个油滴里同时出现**两个人**的 SNP，那它一定是 doublet（双细胞假象）[7, 8]，而这种 doublet 光看表达谱（expression profile）可能发现不了 [8]。

**在数据里**：混样上机的数据，obs 里的 `patient` 这一列就是这样算出来的，而不是实验时直接记下的。一份数据是不是混样，要看它的方法部分（Methods）。

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

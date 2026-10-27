# 7 · 怎么读懂一份数据集

> ⏱ 约 40 分钟 · 第 1 天 · 读懂

!!! abstract "读完能回答"
    - 拿到一份单细胞数据，要先问哪几个问题？
    - 为什么"人数"比"细胞数"更重要？
    - raw 和 filtered、公开和受控，分别影响你能做什么？

每份数据的具体信息在 **[数据集](../datasets/index.md)** 标签页。这一模块不逐个介绍，只讲**看任何一份数据时都要问的六个问题**，并用那些数据集当例子。读完以后，去数据集页面时你就知道该看哪几行。

## 先看全貌：五份数据放在一起

单看一份数据，很难知道它哪里特别。下面把五份有代表性的数据放在一起，每一行是后面的一个问题。先扫一眼，注意它们**在哪些行上差别最大**；后面每个问题都会回到这张表。

| | [Lake 2023](../datasets/lake-2023.md) | [Abedini 2024](../datasets/abedini-2024.md) | [mBDRC 2026](../datasets/mbdrc-2026.md) | [Hoeft 2024](../datasets/hoeft-2024.md) | [Janssen 2023 (小鼠)](../datasets/janssen-2023.md) |
|---|---|---|---|---|---|
| **1 · 测了什么** | 单细胞 RNA、单核 RNA、同核 RNA+ATAC、空间 | 单细胞 RNA、单核 RNA、ATAC、空间 | 单细胞 RNA、同核 RNA+ATAC | 单核 RNA、基因型 | 单细胞 RNA、单核 RNA、基因型 |
| **2 · 多少人** | 三份单细胞数据合计 71 人（35 健康、19 CKD、17 AKI） | 论文共 58 人（81 份样本：36 份对照，45 份 CKD，其中 20 糖尿病肾病、25 高血压肾病）；GEO 单细胞数据里有其中 44 人（21 名对照） | 19 名健康供体，33 份正常皮质 | 4 名病人（冷冻肾活检） | 3 个品系小鼠（CAST、BL6、SvImJ）混在一个通道 |
| **3 · 组织来源** | 病人：大多是 KPMP 活检（单核数据里有 3 名 CKD 来自肾切除）；健康人：肾切除、死亡供体、活体供体活检；皮质、髓质、乳头 | 剩余的（去标识）肾组织；皮质和外髓 | 肾切除时取的正常皮质；只有皮质 | 冷冻肾活检；没写诊断 | 健康小鼠肾，3 个品系混在一个通道 |
| **4 · 标签** | 除 3,364 个单核外，每个细胞都有细胞类型和正常 / 改变标签 | 细胞类型；每个样本的疾病组 | 细胞类型；每个细胞的测法和供体 | 按 SNP 分出的供体；250 个基因型 doublet（2.2%） | 每个细胞的污染比例（含 95% 置信区间） |
| **5 · 处理到哪一步** | 过滤后的计数；原始 FASTQ 受控，拿不到空液滴 | 已去低质量细胞；用 SoupX 校正了 ambient RNA、用 DoubletFinder 去了 doublet（补充材料）；没有原始数据 | 处理后的矩阵（cellxgene、Zenodo）；原始数据在 dbGaP，要申请 | GEO 上写“raw”的其实已过滤；FASTQ 公开，供体标签要重算 | raw（含空液滴）+ filtered 矩阵 |
| **6 · 许可** | CC BY 4.0 (cellxgene); GEO: not stated | not stated | CC BY 4.0 (data); paper CC BY-NC-ND 4.0 | CC BY 4.0 (paper) | CC BY 4.0 |

几个对比值得注意：

- **Lake 2023 和 Abedini 2024** 都是大规模病人队列。Lake 几乎给每个细胞都标了 reference / altered（少数核没有标）；Abedini 有样本层面的疾病组，加上少数按细胞标的损伤簇（比如 `iPT`），但没有系统的改变态标签。两份数据发布前都已经部分清洗过：Lake 在各测法里都去了 doublet，单细胞数据还用 SoupX 减过 ambient [1]；Abedini 也去了 ambient 和 doublet [2]。
- **mBDRC 2026、Hoeft 2024、Janssen 2023** 人数少，却有实验设计给定的答案：测法、按 SNP 分出的供体、每个细胞的污染比例。我们的理解：找伪影时，它们比大图谱更有用。
- 现成的含空液滴 raw 矩阵文件，只有 **Janssen 2023** 有，但它是小鼠。Hoeft 2024 和 Lake 2019 的原始测序（FASTQ）在 SRA 上公开，重新跑一遍比对流程也能拿回空液滴（见各自的数据页）。

## 问题 1 · 测的是什么？

单细胞还是单核？有没有 ATAC？是不是同一个核测了两样（multiome）？测法决定了数据的偏差（模块 5、6）。例：[Lake 2023](../datasets/lake-2023.md) 三种都有，但 RNA + ATAC 只有 7 个健康人；[Abedini 2024](../datasets/abedini-2024.md) 的 RNA 和 ATAC 是分开测的，两张表的行不是同一批细胞。

## 问题 2 · 多少人，不是多少细胞

20 万个细胞听起来很多，但它们来自几十个人。模块 1 讲过：同一个人的细胞高度相关，训练和测试要按人分。所以**真正的样本量是人数**，尤其是健康人和病人各多少。例：[Hoeft 2024](../datasets/hoeft-2024.md) 有一万多个核，但只有 4 个人；我们的理解：只够做验证。

## 问题 3 · 组织从哪来？

活检、肾切除还是死亡供体？皮质还是髓质？取法会带来缺血应激，部位决定细胞组成（模块 3、4）。例：[mBDRC](../datasets/mbdrc-2026.md) 只有皮质；[Lake 2019](../datasets/lake-2019.md) 没有活检。

## 问题 4 · 标签是什么、有多可信？

有没有细胞类型、细胞状态、供体、测法这些标签？它们是**实验设计给定的**（例如同一个人换测法、按 SNP 分出的供体），还是**专家聚类后判读的**？前者可以当真值，后者要小心（模块 2）。例：[Lake 2023](../datasets/lake-2023.md) 的 altered 状态是专家判读的；[Janssen 2023](../datasets/janssen-2023.md) 每个细胞的污染比例是按基因型算出来的。

## 问题 5 · 数据被处理到哪一步？

- **raw 还是 filtered：**raw 矩阵含空液滴，才能估计 ambient；filtered 只剩细胞。例：[Janssen 2023](../datasets/janssen-2023.md) 有 raw；[Hoeft 2024](../datasets/hoeft-2024.md) GEO 上写"raw"的其实是 filtered。
- **伪影是不是已经被去掉了：**例：[Abedini 2024](../datasets/abedini-2024.md) 已经做过 SoupX 和 DoubletFinder [2]，计数不再是整数；[Lake 2023](../datasets/lake-2023.md) 的单细胞数据也用 SoupX 校正过 [1]。
- **有没有删掉什么：**例：[Lake 2019](../datasets/lake-2019.md) 的公开矩阵删掉了线粒体基因，没法直接算线粒体比例。

## 问题 6 · 能不能拿到、能不能发布？

- **公开还是受控：**处理后的数据通常在 GEO / cellxgene / Zenodo，直接下载；人的原始测序通常在 dbGaP / EGA，要申请（本站的例外：Hoeft 2024 和 Lake 2019 的 FASTQ 在 SRA 上公开，见数据页）。
- **许可：**CC BY 可以自由使用和发布派生结果；没写许可的（例如 [Abedini 2024](../datasets/abedini-2024.md)）要先确认才能发布派生标签。
- **大小和格式：**h5ad 用 Python 直接读（模块 1）；RDS / h5Seurat 是 R 的格式，要转换。

!!! tip "计算机类比"
    这六个问题就像接手一个别人的数据集时的 code review：数据来源（谁采的、怎么采的）、样本量（独立样本有多少）、标签质量（ground truth 还是 weak label）、预处理历史（做过哪些清洗）、访问权限和许可。

## 自测

??? question "1. 一份数据有 50 万个细胞、6 个人，另一份有 10 万个细胞、40 个人。哪份更适合评估方法能不能泛化到新病人？"
    40 个人那份。按人划分时，6 个人分不出可靠的训练集和测试集。

??? question "2. 想估计真实的 ambient 污染，最需要数据里有什么？"
    含空液滴的 raw 矩阵，最好还有基因型信息：对覆盖到 SNP 的那部分 RNA 分子，能看出它来自哪个个体，从而估出每个细胞的污染比例（例如 Janssen 2023 [3]）。

??? question "3. 为什么 Abedini 2024 的数据不适合直接拿来测"找伪影"的方法？"
    它已经用 SoupX 去过 ambient、用 DoubletFinder 去过 doublet [2]，伪影被提前洗掉了一部分。同样的问题在 Lake 2023 里也部分存在：它也去过 doublet，单细胞数据也做过 SoupX [1]；只有 Lake 的单核计数还是原始整数。

## 参考文献

1. Lake BB, Menon R, Winfree S, et al. An atlas of healthy and injured cell states and niches in the human kidney. *Nature* 2023;619:585–594. [doi:10.1038/s41586-023-05769-3](https://doi.org/10.1038/s41586-023-05769-3) — Methods "Quality control of sequencing data" (snCv3: "doublets were identified using the DoubletDetection software… and removed"; scCv3: "The ambient mRNA contamination was corrected using SoupX"; SNARE2: doublets removed). Deep-read: [Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md).
2. Abedini A, Levinsohn J, Klötzer KA, et al. Single-cell multi-omic and spatial profiling of human kidneys implicates the fibrotic microenvironment in kidney disease progression. *Nat Genet* 2024;56:1712–1724. [doi:10.1038/s41588-024-01802-x](https://doi.org/10.1038/s41588-024-01802-x) — Supplementary Information, "Data Processing and Computational Analyses" ("Ambient RNA was corrected using SoupX (v1.5.0) and doublets were removed by DoubletFinder (v2.0)"). Deep-read: [Abedini 2024](../papers/abedini-kidney-atlas-natgenet-2024/index.md).
3. Janssen P, Kliesmete Z, Vieth B, et al. The effect of background noise and its removal on the analysis of single-cell expression data. *Genome Biol* 2023;24:140. [doi:10.1186/s13059-023-02978-x](https://doi.org/10.1186/s13059-023-02978-x) — Results (contamination estimated from strain-specific SNPs, per cell). Deep-read: [Janssen 2023](../papers/janssen-ambient-noise-genomebiol-2023/index.md).

## 本模块名词

| 中文 | English | 一句话 |
|---|---|---|
| [KPMP（肾脏精准医学项目）](glossary.md#kpmp) | KPMP (Kidney Precision Medicine Project) | 美国 NIH 的联盟项目，收集 AKI 和 CKD 病人的肾活检，用单细胞、空间和成像方法测；Lake 2023 的主要数据来源。 |
| [CELLxGENE 数据平台](glossary.md#cellxgene) | CZ CELLxGENE | Chan Zuckerberg 的单细胞数据平台，把整理好的数据集统一成 h5ad 文件和标准标签提供下载；下载 Lake 2023 和 mBDRC 的方便途径。列名和作者在 GEO 上的标签表不同（如 donor_id），X 是归一化后的值、原始计数在 raw.X，Lake 的单核和单细胞文件里没有作者的 state 标签。 |
| [GEO / SRA 公共数据库](glossary.md#geo-sra) | GEO / SRA | NCBI 的公共数据库：GEO 放处理后的数据（计数矩阵、标签表），SRA 放原始测序读段（FASTQ）；免费下载。 |
| [dbGaP / EGA（受控访问）](glossary.md#dbgap) | dbGaP / EGA (controlled access) | 存放可识别个人的人类原始测序数据的受控数据库；要提交申请并签数据使用协议才能下载。 |

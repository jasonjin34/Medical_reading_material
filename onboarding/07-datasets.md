# 7 · 怎么读懂一份数据集 / 7 · How to read a dataset

<!-- ZH -->
!!! abstract "读完能回答"
    - 拿到一份单细胞数据，要先问哪几个问题？
    - 为什么"人数"比"细胞数"更重要？
    - raw 和 filtered、公开和受控，分别影响你能做什么？
<!-- EN -->
!!! abstract "After this module you can answer"
    - Which questions do you ask first about a single-cell dataset?
    - Why does the number of people matter more than the number of cells?
    - How do raw vs filtered and open vs controlled limit what you can do?

<!-- ZH -->
每份数据的具体信息在 **[数据集](../datasets/index.md)** 标签页。这一模块不逐个介绍，只讲**看任何一份数据时都要问的六个问题**，并用那些数据集当例子。读完以后，去数据集页面时你就知道该看哪几行。
<!-- EN -->
The facts about each dataset are under the **[Datasets](../datasets/index.md)** tab. This module does not go through them one by one; it gives **six questions to ask of any dataset**, with those datasets as examples. Afterwards you will know which lines of a dataset page to look at.

## 问题 1 · 测的是什么？ / Question 1 · What was measured?

<!-- ZH -->
单细胞还是单核？有没有 ATAC？是不是同一个核测了两样（multiome）？测法决定了数据的偏差（模块 5、6）。例：[Lake 2023](../datasets/lake-2023.md) 三种都有，但 RNA + ATAC 只有 7 个健康人；[Abedini 2024](../datasets/abedini-2024.md) 的 RNA 和 ATAC 是分开测的，两张表的行不是同一批细胞。
<!-- EN -->
Single-cell or single-nucleus? Is there ATAC? Were two things measured in the same nucleus (multiome)? The assay sets the biases (modules 5 and 6). Example: [Lake 2023](../datasets/lake-2023.md) has all three, but RNA + ATAC only for 7 healthy donors; [Abedini 2024](../datasets/abedini-2024.md) measured RNA and ATAC separately, so the two tables do not describe the same cells.

## 问题 2 · 多少人，不是多少细胞 / Question 2 · How many people, not how many cells

<!-- ZH -->
20 万个细胞听起来很多，但它们来自几十个人。模块 1 讲过：同一个人的细胞高度相关，训练和测试要按人分。所以**真正的样本量是人数**，尤其是健康人和病人各多少。例：[Hoeft 2024](../datasets/hoeft-2024.md) 有 11,490 个核，但只有 4 个人，只够做验证。
<!-- EN -->
200,000 cells sounds like a lot, but they come from a few dozen people. As module 1 explained, cells from one person are strongly correlated and splits go by person, so **the real sample size is the number of people**, especially how many are healthy and how many are patients. Example: [Hoeft 2024](../datasets/hoeft-2024.md) has 11,490 nuclei but only 4 people, enough for validation only.

## 问题 3 · 组织从哪来？ / Question 3 · Where did the tissue come from?

<!-- ZH -->
活检、肾切除还是死亡供体？皮质还是髓质？取法会带来缺血应激，部位决定细胞组成（模块 3、4）。例：[mBDRC](../datasets/mbdrc-2026.md) 只有皮质；[Lake 2019](../datasets/lake-2019.md) 没有活检。
<!-- EN -->
Biopsy, nephrectomy or deceased donor? Cortex or medulla? Procurement brings ischaemic stress, and region sets the cell mix (modules 3 and 4). Example: [mBDRC](../datasets/mbdrc-2026.md) is cortex only; [Lake 2019](../datasets/lake-2019.md) has no biopsies.

## 问题 4 · 标签是什么、有多可信？ / Question 4 · What are the labels, and how far can you trust them?

<!-- ZH -->
有没有细胞类型、细胞状态、供体、测法这些标签？它们是**实验设计给定的**（例如同一个人换测法、按 SNP 分出的供体），还是**专家聚类后判读的**？前者可以当真值，后者要小心（模块 2）。例：[Lake 2023](../datasets/lake-2023.md) 的 altered 状态是专家判读的；[Janssen 2023](../datasets/janssen-2023.md) 每个细胞的污染比例是按基因型算出来的。
<!-- EN -->
Are there cell-type, cell-state, donor or assay labels? Are they **fixed by the experimental design** (one donor measured by several assays, donors assigned by SNPs) or **read off clusters by experts**? The first kind can serve as ground truth; the second needs care (module 2). Example: [Lake 2023](../datasets/lake-2023.md)'s altered states are expert calls; [Janssen 2023](../datasets/janssen-2023.md)'s per-cell contamination is computed from genotypes.

## 问题 5 · 数据被处理到哪一步？ / Question 5 · How far has the data been processed?

<!-- ZH -->
- **raw 还是 filtered：**raw 矩阵含空液滴，才能估计 ambient；filtered 只剩细胞。例：[Janssen 2023](../datasets/janssen-2023.md) 有 raw；[Hoeft 2024](../datasets/hoeft-2024.md) GEO 上写"raw"的其实是 filtered。
- **伪影是不是已经被去掉了：**例：[Abedini 2024](../datasets/abedini-2024.md) 已经做过 SoupX 和 DoubletFinder，计数不再是整数。
- **有没有删掉什么：**例：[Lake 2019](../datasets/lake-2019.md) 的公开矩阵删掉了线粒体基因，没法直接算线粒体比例。
<!-- EN -->
- **Raw or filtered:** a raw matrix contains empty droplets, which you need to estimate ambient RNA; a filtered one has cells only. Example: [Janssen 2023](../datasets/janssen-2023.md) has raw; the "raw" file of [Hoeft 2024](../datasets/hoeft-2024.md) on GEO is in fact filtered.
- **Have artifacts already been removed:** example: [Abedini 2024](../datasets/abedini-2024.md) already ran SoupX and DoubletFinder, so counts are no longer integers.
- **Was anything dropped:** example: [Lake 2019](../datasets/lake-2019.md) removed mitochondrial genes from the public matrix, so mitochondrial fractions cannot be computed directly.

## 问题 6 · 能不能拿到、能不能发布？ / Question 6 · Can you get it, and can you publish from it?

<!-- ZH -->
- **公开还是受控：**处理后的数据通常在 GEO / cellxgene / Zenodo，直接下载；人的原始测序在 dbGaP / EGA，要申请。
- **许可：**CC BY 可以自由使用和发布派生结果；没写许可的（例如 [Abedini 2024](../datasets/abedini-2024.md)）要先确认才能发布派生标签。
- **大小和格式：**h5ad 用 Python 直接读；RDS / h5Seurat 是 R 的格式，要转换（模块 1）。
<!-- EN -->
- **Open or controlled:** processed data usually sit on GEO / cellxgene / Zenodo and download directly; human raw sequencing sits in dbGaP / EGA and needs an application.
- **Licence:** CC BY allows free use and publishing derived results; where no licence is stated (for example [Abedini 2024](../datasets/abedini-2024.md)), confirm before releasing derived labels.
- **Size and format:** h5ad reads directly in Python; RDS / h5Seurat are R formats and need converting (module 1).

<!-- ZH -->
!!! tip "计算机类比"
    这六个问题就像接手一个别人的数据集时的 code review：数据来源（谁采的、怎么采的）、样本量（独立样本有多少）、标签质量（ground truth 还是 weak label）、预处理历史（做过哪些清洗）、访问权限和许可。
<!-- EN -->
!!! tip "Computer analogy"
    These six questions are a code review for someone else's dataset: provenance (who collected it and how), sample size (how many independent samples), label quality (ground truth or weak labels), preprocessing history (what cleaning was done), and access and licence.

## 自测 / Self-check

<!-- ZH -->
??? question "1. 一份数据有 50 万个细胞、6 个人，另一份有 10 万个细胞、40 个人。哪份更适合评估方法能不能泛化到新病人？"
    40 个人那份。按人划分时，6 个人分不出可靠的训练集和测试集。

??? question "2. 想估计真实的 ambient 污染，最需要数据里有什么？"
    含空液滴的 raw 矩阵，最好还有能分清每条 RNA 来自谁的基因型信息（例如 Janssen 2023）。

??? question "3. 为什么 Abedini 2024 的数据不适合直接拿来测"找伪影"的方法？"
    它已经用 SoupX 去过 ambient、用 DoubletFinder 去过 doublet，伪影被提前洗掉了一部分。
<!-- EN -->
??? question "1. One dataset has 500,000 cells from 6 people, another 100,000 cells from 40 people. Which is better for testing whether a method generalises to new patients?"
    The one with 40 people. Splitting by person, 6 people cannot give a reliable training and test set.

??? question "2. To estimate real ambient contamination, what do you most need in the data?"
    A raw matrix with empty droplets, ideally plus genotypes that show where each RNA came from (as in Janssen 2023).

??? question "3. Why is Abedini 2024 a poor choice for testing artifact-detection methods directly?"
    Ambient RNA was already removed with SoupX and doublets with DoubletFinder, so part of the artifacts is gone.

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

## 先看全貌：五份数据放在一起 / The big picture: five datasets side by side

<!-- ZH -->
单看一份数据，很难知道它哪里特别。下面把五份有代表性的数据放在一起，每一行是后面的一个问题。先扫一眼，注意它们**在哪些行上差别最大**；后面每个问题都会回到这张表。
<!-- EN -->
One dataset on its own hardly shows what is special about it. Below, five representative datasets sit side by side, one row per question that follows. Skim it first and notice **which rows differ most**; each question below comes back to this table.

<!-- ZH/EN --> @@DATASETS-COMPARE lake-2023 abedini-2024 mbdrc-2026 hoeft-2024 janssen-2023@@

<!-- ZH -->
几个对比值得注意：

- **Lake 2023 和 Abedini 2024** 都是大规模病人队列。Lake 几乎给每个细胞都标了 reference / altered（少数核没有标）；Abedini 有样本层面的疾病组，加上少数按细胞标的损伤簇（比如 `iPT`），但没有系统的改变态标签。两份数据发布前都已经部分清洗过：Lake 在各测法里都去了 doublet，单细胞数据还用 SoupX 减过 ambient [1]；Abedini 也去了 ambient 和 doublet [2]。
- **mBDRC 2026、Hoeft 2024、Janssen 2023** 人数少，却有实验设计给定的答案：测法、按 SNP 分出的供体、每个细胞的污染比例。我们的理解：找伪影时，它们比大图谱更有用。
- 现成的含空液滴 raw 矩阵文件，只有 **Janssen 2023** 有，但它是小鼠。Hoeft 2024 和 Lake 2019 的原始测序（FASTQ）在 SRA 上公开，重新跑一遍比对流程也能拿回空液滴（见各自的数据页）。
<!-- EN -->
A few contrasts worth noticing:

- **Lake 2023 and Abedini 2024** are both large patient cohorts. Lake gives almost every cell a reference / altered label (a small number of nuclei are unlabelled); Abedini has per-sample disease groups plus a few per-cell injury clusters (such as `iPT`), but no systematic altered-state label. Both were partly cleaned before release: Lake removed doublets in every assay and subtracted ambient RNA with SoupX in its single-cell data [1]; Abedini also corrected ambient RNA and removed doublets [2].
- **mBDRC 2026, Hoeft 2024 and Janssen 2023** have few people but carry answers fixed by the design: the assay, donors assigned by SNPs, per-cell contamination. Our reading: for finding artifacts they are more useful than a big atlas.
- Only **Janssen 2023** provides ready-made raw matrices with empty droplets, and it is mouse. The raw sequencing (FASTQ) of Hoeft 2024 and Lake 2019 is open on SRA, so re-running the alignment pipeline can recover the empty droplets (see their dataset pages).

## 问题 1 · 测的是什么？ / Question 1 · What was measured?

<!-- ZH -->
单细胞还是单核？有没有 ATAC？是不是同一个核测了两样（multiome）？测法决定了数据的偏差（模块 5、6）。例：[Lake 2023](../datasets/lake-2023.md) 三种都有，但 RNA + ATAC 只有 7 个健康人；[Abedini 2024](../datasets/abedini-2024.md) 的 RNA 和 ATAC 是分开测的，两张表的行不是同一批细胞。
<!-- EN -->
Single-cell or single-nucleus? Is there ATAC? Were two things measured in the same nucleus (multiome)? The assay sets the biases (modules 5 and 6). Example: [Lake 2023](../datasets/lake-2023.md) has all three, but RNA + ATAC only for 7 healthy donors; [Abedini 2024](../datasets/abedini-2024.md) measured RNA and ATAC separately, so the two tables do not describe the same cells.

## 问题 2 · 多少人，不是多少细胞 / Question 2 · How many people, not how many cells

<!-- ZH -->
20 万个细胞听起来很多，但它们来自几十个人。模块 1 讲过：同一个人的细胞高度相关，训练和测试要按人分。所以**真正的样本量是人数**，尤其是健康人和病人各多少。例：[Hoeft 2024](../datasets/hoeft-2024.md) 有一万多个核，但只有 4 个人；我们的理解：只够做验证。
<!-- EN -->
200,000 cells sounds like a lot, but they come from a few dozen people. As module 1 explained, cells from one person are strongly correlated and splits go by person, so **the real sample size is the number of people**, especially how many are healthy and how many are patients. Example: [Hoeft 2024](../datasets/hoeft-2024.md) has over ten thousand nuclei but only 4 people; our reading: enough for validation only.

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
- **伪影是不是已经被去掉了：**例：[Abedini 2024](../datasets/abedini-2024.md) 已经做过 SoupX 和 DoubletFinder [2]，计数不再是整数；[Lake 2023](../datasets/lake-2023.md) 的单细胞数据也用 SoupX 校正过 [1]。
- **有没有删掉什么：**例：[Lake 2019](../datasets/lake-2019.md) 的公开矩阵删掉了线粒体基因，没法直接算线粒体比例。
<!-- EN -->
- **Raw or filtered:** a raw matrix contains empty droplets, which you need to estimate ambient RNA; a filtered one has cells only. Example: [Janssen 2023](../datasets/janssen-2023.md) has raw; the "raw" file of [Hoeft 2024](../datasets/hoeft-2024.md) on GEO is in fact filtered.
- **Have artifacts already been removed:** example: [Abedini 2024](../datasets/abedini-2024.md) already ran SoupX and DoubletFinder [2], so counts are no longer integers; [Lake 2023](../datasets/lake-2023.md)'s single-cell data was corrected with SoupX too [1].
- **Was anything dropped:** example: [Lake 2019](../datasets/lake-2019.md) removed mitochondrial genes from the public matrix, so mitochondrial fractions cannot be computed directly.

## 问题 6 · 能不能拿到、能不能发布？ / Question 6 · Can you get it, and can you publish from it?

<!-- ZH -->
- **公开还是受控：**处理后的数据通常在 GEO / cellxgene / Zenodo，直接下载；人的原始测序通常在 dbGaP / EGA，要申请（本站的例外：Hoeft 2024 和 Lake 2019 的 FASTQ 在 SRA 上公开，见数据页）。
- **许可：**CC BY 可以自由使用和发布派生结果；没写许可的（例如 [Abedini 2024](../datasets/abedini-2024.md)）要先确认才能发布派生标签。
- **大小和格式：**h5ad 用 Python 直接读（模块 1）；RDS / h5Seurat 是 R 的格式，要转换。
<!-- EN -->
- **Open or controlled:** processed data usually sit on GEO / cellxgene / Zenodo and download directly; human raw sequencing usually sits in dbGaP / EGA and needs an application (exceptions on this site: the FASTQ of Hoeft 2024 and Lake 2019 are open on SRA; see the dataset pages).
- **Licence:** CC BY allows free use and publishing derived results; where no licence is stated (for example [Abedini 2024](../datasets/abedini-2024.md)), confirm before releasing derived labels.
- **Size and format:** h5ad reads directly in Python (module 1); RDS / h5Seurat are R formats and need converting.

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
    含空液滴的 raw 矩阵，最好还有基因型信息：对覆盖到 SNP 的那部分 RNA 分子，能看出它来自哪个个体，从而估出每个细胞的污染比例（例如 Janssen 2023 [3]）。

??? question "3. 为什么 Abedini 2024 的数据不适合直接拿来测"找伪影"的方法？"
    它已经用 SoupX 去过 ambient、用 DoubletFinder 去过 doublet [2]，伪影被提前洗掉了一部分。同样的问题在 Lake 2023 里也部分存在：它也去过 doublet，单细胞数据也做过 SoupX [1]；只有 Lake 的单核计数还是原始整数。
<!-- EN -->
??? question "1. One dataset has 500,000 cells from 6 people, another 100,000 cells from 40 people. Which is better for testing whether a method generalises to new patients?"
    The one with 40 people. Splitting by person, 6 people cannot give a reliable training and test set.

??? question "2. To estimate real ambient contamination, what do you most need in the data?"
    A raw matrix with empty droplets, ideally plus genotypes: for the RNA molecules that cover a SNP, they show which individual the molecule came from, which gives each cell's contamination fraction (as in Janssen 2023 [3]).

??? question "3. Why is Abedini 2024 a poor choice for testing artifact-detection methods directly?"
    Ambient RNA was already removed with SoupX and doublets with DoubletFinder [2], so part of the artifacts is gone. The same partly applies to Lake 2023: it also removed doublets and ran SoupX on its single-cell data [1]; only Lake's single-nucleus counts are still raw integers.

## 参考文献 / References

1. Lake BB, Menon R, Winfree S, et al. An atlas of healthy and injured cell states and niches in the human kidney. *Nature* 2023;619:585–594. [doi:10.1038/s41586-023-05769-3](https://doi.org/10.1038/s41586-023-05769-3) — Methods "Quality control of sequencing data" (snCv3: "doublets were identified using the DoubletDetection software… and removed"; scCv3: "The ambient mRNA contamination was corrected using SoupX"; SNARE2: doublets removed). Deep-read: [Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md).
2. Abedini A, Levinsohn J, Klötzer KA, et al. Single-cell multi-omic and spatial profiling of human kidneys implicates the fibrotic microenvironment in kidney disease progression. *Nat Genet* 2024;56:1712–1724. [doi:10.1038/s41588-024-01802-x](https://doi.org/10.1038/s41588-024-01802-x) — Supplementary Information, "Data Processing and Computational Analyses" ("Ambient RNA was corrected using SoupX (v1.5.0) and doublets were removed by DoubletFinder (v2.0)"). Deep-read: [Abedini 2024](../papers/abedini-kidney-atlas-natgenet-2024/index.md).
3. Janssen P, Kliesmete Z, Vieth B, et al. The effect of background noise and its removal on the analysis of single-cell expression data. *Genome Biol* 2023;24:140. [doi:10.1186/s13059-023-02978-x](https://doi.org/10.1186/s13059-023-02978-x) — Results (contamination estimated from strain-specific SNPs, per cell). Deep-read: [Janssen 2023](../papers/janssen-ambient-noise-genomebiol-2023/index.md).

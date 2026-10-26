# 肾脏单细胞组学异常检测基准 / A Benchmark for Anomaly Detection in Kidney Single-Cell Omics

> <!-- ZH --> 课题 1 · 现状：方向和核心问题已定；数据和任务在讨论中；代码还没开始。所有结果等代码跑出来再写。
> <!-- EN --> Topic 1 · Status: direction and core question decided; data and tasks under discussion; code not started. No results are reported until the code produces them.

## 研究问题 / The question

<!-- ZH -->
**一个看起来异常的细胞，是病造成的，还是测量造成的？**

肾脏单细胞和单核数据里，有些细胞和健康组织对不上。它可能真的病了，也可能是测量过程造成的（doublet、ambient RNA、低质量细胞、取样或消化时的应激），而这两种情况看起来很像。现有方法会把两者都标成"异常"，但还没有一个带已知答案的数据集，能检验它们分不分得清、误报有多少。所以，建立在这些"异常细胞"之上的发现到底有多可信，现在说不清。
<!-- EN -->
**Is an abnormal-looking cell caused by disease, or by measurement?**

In kidney single-cell and single-nucleus data, some cells do not match healthy tissue. They may be diseased, or their abnormality may come from how they were measured (doublets, ambient RNA, low-quality cells, stress during procurement or dissociation), and the two look alike. Current methods flag both as "anomalous", but no dataset with known answers exists to test whether they can tell the two apart, or how many false alarms they raise. So we cannot say how far findings built on these anomalous cells can be trusted.

## 为什么重要 / Why it matters

<!-- ZH -->
- **测量问题造出过假的生物学结论。**在人脑单核数据里，一个被注释为"未成熟少突胶质细胞"的群，后来发现是被神经元 ambient RNA 污染的胶质细胞。doublet 会制造样本里并不存在的"中间状态"。
- **肾脏数据尤其容易受影响。**小鼠肾的混合品系实验里，单核样本的背景污染明显高于配对的单细胞样本（[Janssen 2023](../papers/janssen-ambient-noise-genomebiol-2023/index.md)：35% 对 11%、17% 对 3%）。而单核正是肾脏活检最常用的测法。
- **病和测量的信号本来就重叠。**Lake 2023 挑候选损伤状态时，部分依据是"基因少、线粒体转录多"，这也是低质量细胞的典型特征（我们的解读）；健康参考组织里也有 altered 状态，作者认为可能来自取样缺血或正常衰老（[Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md)）。我们自己从 GEO 标签表里也数到：单核数据里健康人有 26% 的核是 altered。
<!-- EN -->
- **Measurement effects have produced false biology.** In human brain single-nucleus data, a population annotated as "immature oligodendrocytes" turned out to be glia contaminated with neuronal ambient RNA, and doublets create "intermediate states" that do not exist in the sample.
- **Kidney data are especially exposed.** In mixed-strain mouse kidney, background contamination was clearly higher in single-nucleus than in matched single-cell samples ([Janssen 2023](../papers/janssen-ambient-noise-genomebiol-2023/index.md): 35% vs 11%, 17% vs 3%), and single-nucleus is the usual assay for kidney biopsies.
- **Disease and measurement signals overlap.** Lake 2023 picked candidate injury states partly by few genes detected and many mitochondrial transcripts, which are also the usual signs of a low-quality cell (our reading); altered states also occur in healthy reference tissue, which the authors attribute possibly to ischaemia during acquisition or normal ageing ([Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md)). From the GEO label table we counted that 26% of nuclei from healthy donors are altered.

## 为什么还没解决 / Why it is unsolved

<!-- ZH -->
- **伪影基准没有"病"这一维。**doublet 和 ambient 各有自己的基准（如 [ambient 去除基准](../papers/ambient-rna-bench-biorxiv-2026/index.md)），但每个只管一种伪影，不含疾病状态。
- **找疾病状态的方法不区分伪影。**用健康参考找"改变的细胞状态"的方法（如 [Dann 2023](../papers/healthy-ref-natgenet-2023/index.md)）目标是找疾病状态，本身不判断报出来的细胞是不是伪影。
- **没有误报控制。**常见的注释流程不给统计保证；conformal 方法能界定误报率（[Bates 2023](../papers/conformal-outliers-annstat-2023/index.md)、[单细胞 conformal](../papers/conformal-scrna-bioinformatics-2025/index.md)），但还没在肾脏数据上系统检验过。
- **没有测试平台。**通用异常检测基准里没有单细胞或组学表达数据；我们没找到肾脏组学的异常检测基准（2026 年 10 月检索）。
<!-- EN -->
- **Artifact benchmarks have no disease axis.** Doublets and ambient RNA have their own benchmarks (for example the [ambient-removal benchmark](../papers/ambient-rna-bench-biorxiv-2026/index.md)), but each covers one artifact and no disease states.
- **Disease-state detection does not separate artifacts.** Methods that find altered cell states against a healthy reference (for example [Dann 2023](../papers/healthy-ref-natgenet-2023/index.md)) aim at disease states and do not judge whether a flagged cell is an artifact.
- **There is no error control.** Common annotation pipelines give no statistical guarantee; conformal methods can bound the false-alarm rate ([Bates 2023](../papers/conformal-outliers-annstat-2023/index.md), [conformal for single-cell](../papers/conformal-scrna-bioinformatics-2025/index.md)) but have not been tested systematically on kidney data.
- **There is no test bed.** General anomaly-detection benchmarks contain no single-cell or omics expression data, and we found no anomaly-detection benchmark for kidney omics (search, October 2026).

## 要做出什么 / What we will produce

<!-- ZH -->
**主角是数据集和基准，不是方法。**

1. **一个带已知答案的肾脏数据集**：每个细胞标成"病"、"测量造成"或"健康"，并注明这个标签有多可靠。
2. **一套基准**：几个任务、统一的划分和指标，把十几种经典异常检测方法和单细胞常用的 QC 工具放在一起比。
3. **一个参考方法**：健康参考 + 最近邻打分 + 按供体校准的误报控制 + "病还是测量"的判断。它只是给基准一个起点，不是贡献本身。
4. **公开代码**：处理脚本、按供体的划分文件、伪影注入代码、标签和跑基准的代码。原始数据不再分发。
<!-- EN -->
**The dataset and benchmark are the lead; the method is not.**

1. **A kidney dataset with known answers**: every cell labelled as diseased, measurement-caused or healthy, with a statement of how reliable that label is.
2. **A benchmark**: a few tasks with fixed splits and metrics, comparing a dozen classic anomaly-detection methods and the usual single-cell QC tools.
3. **A reference method**: a healthy reference, a nearest-neighbour score, donor-level calibration with false-alarm control, and a disease-or-measurement call. It gives the benchmark a starting point; it is not the contribution.
4. **Released code**: processing scripts, donor splits, artifact-injection code, labels and benchmark code. Raw data are not redistributed.

## 用到的数据 / Data

<!-- ZH -->
只用公开的肾脏数据：人为主，小鼠只用来校准。每份数据测了什么、多少人、怎么下载，见 [数据集](../datasets/index.md)；这里只写它在本课题里干什么。按它能提供哪一边的答案分组：
<!-- EN -->
Public kidney data only: human first, mouse only for calibration. What each dataset measures, on how many people, and how to download it is in [Datasets](../datasets/index.md); here we only say what it does in this topic. Grouped by which side of the answer it provides:

| Dataset / 数据 | Answers / 提供哪一边 | Role / 在基准里干什么 |
|---|---|---|
| [Lake 2023](../datasets/lake-2023.md) | disease / 病 | healthy reference + disease-state labels / 健康参考 + 疾病状态标签 |
| [mBDRC 2026](../datasets/mbdrc-2026.md) | measurement / 测量 | same donors measured by three assays: any "anomaly" between them is a false alarm / 同一人三种测法，之间报出的"异常"一定是误报 |
| [Abedini 2024](../datasets/abedini-2024.md) | disease / 病 | second lab and cohort: do false alarms stay under control? / 换实验室、换一批人，误报能不能控住 |
| [Janssen 2023](../datasets/janssen-2023.md) | measurement / 测量 | mouse; real ambient measured by genotype, used to calibrate injection / 小鼠；按基因型测出的真实 ambient，用来校准注入 |
| [Hoeft 2024](../datasets/hoeft-2024.md) | measurement / 测量 | under discussion: real human-kidney doublets and ambient from pooled donors / 讨论中：多人混样得到的真实人肾 doublet 和 ambient |
| [Lake 2019](../datasets/lake-2019.md) | measurement / 测量 | under discussion: same patients, different storage and processing / 讨论中：同一病人、不同保存和处理方式 |

<!-- ZH -->
**划分：**按供体划分，不按细胞，同一个人不会同时出现在训练和测试里；划分文件随数据集一起发布。
<!-- EN -->
**Splits:** by donor, not by cell, so no person appears in both training and testing; the split files ship with the dataset.

## 任务和答案 / Tasks and ground truth

<!-- ZH -->
答案按可靠程度分三级：**一级**是我们自己注入的伪影，完全确定；**二级**是实验设计给定的，例如同一个人换测法；**三级**是专家标注，例如 Lake 的 altered 状态。
<!-- EN -->
Ground truth comes in three tiers: **tier 1** is artifacts we inject ourselves, known exactly; **tier 2** is fixed by experimental design, such as one donor measured by several assays; **tier 3** is expert annotation, such as Lake's altered states.

| Task / 任务 | Question / 问什么 | Ground truth / 答案 | Metric / 指标 |
|---|---|---|---|
| T1 | find diseased cells / 找出病细胞 | tier 3 / 三级 | AUROC, AUPRC |
| T2 | find measurement errors / 找出测量错误 | tier 1 / 一级 | AUROC, AUPRC |
| T2b | is an assay change flagged as anomalous? / 换测法会不会被当成异常 | tier 2 / 二级 | false-alarm rate ≤ α / 误报率 ≤ α |
| T3 | separate disease from measurement / 分清病和测量错误 | tiers 1–3 / 一到三级 | macro-F1, confusion matrix / 宏平均 F1、混淆矩阵 |
| T4 | do false alarms stay controlled in a new lab? / 换实验室后误报控不控得住 | every call on healthy donors is false / 健康人身上报出的全算误报 | observed rate vs α / 实际误报率 vs 设定的 α |

<!-- ZH -->
!!! warning "已知的坑"
    直接拿 Lake 的 altered 标签当"病"的答案会循环：单核数据里，最大的 altered 组（degenerative）基因数不到正常细胞的一半、线粒体比例约是 5 倍，一个只看 QC 指标的打分器就可能拿到高分。所以基准里必须有"只用 QC 指标"的基线，并且按状态（degenerative / adaptive）分开报结果。
<!-- EN -->
!!! warning "A known trap"
    Using Lake's altered labels directly as disease ground truth is circular: in the single-nucleus data the largest altered group (degenerative) has less than half the genes of normal nuclei and about five times the mitochondrial fraction, so a scorer that looks only at QC metrics could score well. The benchmark therefore needs a QC-only baseline and reports results per state (degenerative / adaptive).

## 还没定的 / Open questions

<!-- ZH -->
- T2b 单独成一个任务，还是并进 T4？
- Hoeft 2024 和 Lake 2019 要不要进主线？
- Lake 的 altered 细胞怎么分组：有独立证据的、只靠 QC 类特征判出来的、健康人身上的，各自怎么用。
- Abedini 2024 的健康供体人数和许可（决定 T4 的规模、能不能发布派生标签）。
- 要比较的方法清单。
<!-- EN -->
- Should T2b be its own task or part of T4?
- Should Hoeft 2024 and Lake 2019 join the main line?
- How to split Lake's altered cells: those with independent evidence, those called only from QC-like features, and those in healthy donors.
- The number of healthy donors in Abedini 2024 and its licence (sets the size of T4 and whether derived labels can be released).
- The list of methods to compare.

## 阅读路线 / Reading path

<!-- ZH -->
先读完 [入门](../onboarding/index.md)，然后按这个顺序：

1. [Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md)：肾脏图谱和 altered 状态
2. [Janssen 2023](../papers/janssen-ambient-noise-genomebiol-2023/index.md)：真实 ambient 污染有多大
3. [Dann 2023](../papers/healthy-ref-natgenet-2023/index.md)：用健康参考找改变的细胞状态
4. [Bates 2023](../papers/conformal-outliers-annstat-2023/index.md)：conformal p 值和误报控制
5. [PatchCore](../papers/patchcore-cvpr-2022/index.md)：图像异常检测里的最近邻思路

<!-- EN -->
Finish [Onboarding](../onboarding/index.md) first, then read in this order:

1. [Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md): the kidney atlas and its altered states
2. [Janssen 2023](../papers/janssen-ambient-noise-genomebiol-2023/index.md): how large real ambient contamination is
3. [Dann 2023](../papers/healthy-ref-natgenet-2023/index.md): finding altered states against a healthy reference
4. [Bates 2023](../papers/conformal-outliers-annstat-2023/index.md): conformal p-values and false-alarm control
5. [PatchCore](../papers/patchcore-cvpr-2022/index.md): the nearest-neighbour idea from image anomaly detection

<!-- ZH -->
再往后，看 [知识图谱](../knowledge-map.md) 里"课题 1"视图的必读论文，以及 [方法 × 数据矩阵](../knowledge-map.md)：虚线格就是这个课题要补的空白。
<!-- EN -->
After that, see the must-reads in the "Topic 1" view of the [knowledge map](../knowledge-map.md) and the [method × data matrix](../knowledge-map.md), whose dashed cells are the gaps this topic fills.

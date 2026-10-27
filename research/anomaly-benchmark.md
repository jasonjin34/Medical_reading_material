# 肾脏单细胞组学异常检测基准 / A Benchmark for Anomaly Detection in Kidney Single-Cell Omics

> <!-- ZH --> 课题 1 · 现状：方向和核心问题已定；数据和任务在讨论中；基准代码还没开始。[入门模块 9](../onboarding/09-hands-on.md) 里有一条教学用的最小流程（kNN 对比只数基因的基线），结果见那里；它不是基准本身的结果。基准的结果等代码跑出来再写。
> <!-- EN --> Topic 1 · Status: direction and core question decided; data and tasks under discussion; benchmark code not started. [Onboarding module 9](../onboarding/09-hands-on.md) has a minimal teaching pipeline (kNN against a gene-count baseline) with its results; those are not benchmark results. Benchmark results are reported only once the code produces them.

## 研究问题 / The question

<!-- ZH -->
**一个看起来异常的细胞，是病造成的，还是测量造成的？**

肾脏单细胞和单核数据里，有些细胞和健康组织对不上。它可能真的病了，也可能是测量过程造成的（doublet、ambient RNA、低质量细胞、取样或消化时的应激），而这两种情况看起来很像。我们的理解（截至 2026 年 10 月）：现有方法会把两者都标成"异常"，而我们没找到一个带已知答案的数据集，能检验它们分不分得清、误报有多少。所以，建立在这些"异常细胞"之上的发现到底有多可信，现在说不清。
<!-- EN -->
**Is an abnormal-looking cell caused by disease, or by measurement?**

In kidney single-cell and single-nucleus data, some cells do not match healthy tissue. They may be diseased, or their abnormality may come from how they were measured (doublets, ambient RNA, low-quality cells, stress during procurement or dissociation), and the two look alike. Our reading (as of 2026-10): current methods flag both as "anomalous", and we found no dataset with known answers to test whether they can tell the two apart, or how many false alarms they raise. So we cannot say how far findings built on these anomalous cells can be trusted.

## 为什么重要 / Why it matters

<!-- ZH -->
- **测量问题造出过假的生物学结论。**在人脑单核数据里，以前被注释为"未成熟少突胶质细胞"的核，后来发现是被神经元 ambient RNA 污染的胶质细胞（[Caglayan et al., Neuron 2022](https://doi.org/10.1016/j.neuron.2022.09.010)）。
- **肾脏单核数据的背景污染可以很高。**小鼠肾的混合品系实验里，用冷冻组织做的单核样本，背景污染明显高于来自同一批样本的单细胞样本（[Janssen 2023](../papers/janssen-ambient-noise-genomebiol-2023/index.md)：35% 对 11%、17% 对 3%）。冷冻的肾活检只能做单核（[Hoeft 2024](../papers/hoeft-genotype-multiplexing-natcommun-2024/index.md)："snRNA, but not scRNA, can be performed from frozen tissue"）。
- **病和测量的信号本来就重叠。**Lake 2023 挑候选损伤状态时，部分依据是"基因少、线粒体转录多"，这也是低质量细胞的典型特征（我们的解读）；健康参考组织里也有 altered 状态，作者认为可能来自取样缺血或正常衰老（[Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md)）。我们自己从 GEO 标签表里也数到：单核数据里健康人有 26% 的核是 altered（88,460 个健康人核里的 22,774 个）。
<!-- EN -->
- **Measurement effects have produced false biology.** In human brain single-nucleus data, nuclei previously annotated as "immature oligodendrocytes" turned out to be glia contaminated with neuronal ambient RNA ([Caglayan et al., Neuron 2022](https://doi.org/10.1016/j.neuron.2022.09.010)).
- **Background contamination in kidney single-nucleus data can be high.** In mixed-strain mouse kidney, single-nucleus samples made from frozen tissue had clearly more background contamination than single-cell samples from the same material ([Janssen 2023](../papers/janssen-ambient-noise-genomebiol-2023/index.md): 35% vs 11%, 17% vs 3%). Frozen kidney biopsies can only be profiled by single-nucleus ([Hoeft 2024](../papers/hoeft-genotype-multiplexing-natcommun-2024/index.md): "snRNA, but not scRNA, can be performed from frozen tissue").
- **Disease and measurement signals overlap.** Lake 2023 picked candidate injury states partly by few genes detected and many mitochondrial transcripts, which are also the usual signs of a low-quality cell (our reading); altered states also occur in healthy reference tissue, which the authors attribute possibly to ischaemia during acquisition or normal ageing ([Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md)). From the GEO label table we counted that 26% of nuclei from healthy donors are altered (22,774 of 88,460).

## 为什么还没解决 / Why it is unsolved

<!-- ZH -->
- **伪影基准没有"病"这一维。**我们的理解（截至 2026 年 10 月）：doublet 和 ambient 各有自己的基准，我们找到的每个只管一种伪影，不含疾病状态。例如 [ambient 去除基准](../papers/ambient-rna-bench-biorxiv-2026/index.md) 用的是模拟数据、物种混合和基因型混合实验。
- **找疾病状态的方法不区分伪影。**用健康参考找"改变的细胞状态"的方法（如 [Dann 2023](../papers/healthy-ref-natgenet-2023/index.md)）目标是找疾病状态；我们的理解：方法本身不判断报出来的细胞是不是伪影。doublet 和低质量细胞只在预处理时去掉（去掉一个疑似 doublet 的簇、只保留至少 1,000 个分子的细胞），没有 ambient 的处理；作者提醒的技术性误报来源是残余批次效应（Extended Data Fig. 7b,c）。
- **没有误报控制。**现有注释流程里，带"拒判"选项的那些通常也只靠人为设定的条件，不给统计保证（[单细胞 conformal](../papers/conformal-scrna-bioinformatics-2025/index.md)："do not provide statistical guarantees"）；conformal 方法能界定误报率（[Bates 2023](../papers/conformal-outliers-annstat-2023/index.md)），但前提是参考和查询数据可交换：单细胞 conformal 那篇里，查询来自肺肿瘤病人时，误报率保证就不成立了。我们的理解（截至 2026 年 10 月）：还没有人在肾脏数据上系统检验过。
- **没有测试平台。**我们的理解（截至 2026 年 10 月）：我们看过的通用异常检测基准里没有单细胞表达数据，也没找到肾脏组学的异常检测基准。
<!-- EN -->
- **Artifact benchmarks have no disease axis.** Our reading (as of 2026-10): doublets and ambient RNA have their own benchmarks, and each one we found covers one artifact and no disease states. For example, the [ambient-removal benchmark](../papers/ambient-rna-bench-biorxiv-2026/index.md) uses simulated data, species-mixing and genotype-mixing experiments.
- **Disease-state detection does not separate artifacts.** Methods that find altered cell states against a healthy reference (for example [Dann 2023](../papers/healthy-ref-natgenet-2023/index.md)) aim at disease states. Our reading: the method itself does not judge whether a flagged cell is an artifact. Doublets and low-quality cells are only removed in preprocessing (one suspected doublet cluster dropped, only cells with at least 1,000 molecules kept), with no ambient-RNA step; the technical source of false positives the authors warn about is residual batch effects (Extended Data Fig. 7b,c).
- **There is no error control.** Annotation pipelines that offer a reject option usually rely on arbitrary assumptions and give no statistical guarantee ([conformal for single-cell](../papers/conformal-scrna-bioinformatics-2025/index.md): they "do not provide statistical guarantees"). Conformal methods can bound the false-alarm rate ([Bates 2023](../papers/conformal-outliers-annstat-2023/index.md)), but only when reference and query are exchangeable: in the single-cell conformal paper, the false-alarm guarantee failed when the query came from lung-tumour patients. Our reading (as of 2026-10): this has not been tested systematically on kidney data.
- **There is no test bed.** Our reading (as of 2026-10): the general anomaly-detection benchmarks we looked at contain no single-cell expression data, and we found no anomaly-detection benchmark for kidney omics.

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
| [Lake 2023](../datasets/lake-2023.md) | disease / 病 | healthy reference + disease-state labels; `state.l1/l2` and `percent.mt` come from the GEO label table, since the cellxgene file has neither (mitochondrial genes were removed) / 健康参考 + 疾病状态标签；`state.l1/l2` 和 `percent.mt` 要从 GEO 标签表里取，cellxgene 文件里两者都没有（线粒体基因已删） |
| [mBDRC 2026](../datasets/mbdrc-2026.md) | measurement / 测量 | 11 of 18 donors measured by two or three assays (3 have all three; cellxgene file): an "anomaly" flagged only between assays of the same donor is treated as a false alarm (our design choice; tissue pieces and preservation also differ) / 18 名供体里有 11 人用两到三种方法测过（3 人三种都有；cellxgene 文件）：同一人只因换测法报出的"异常"按误报处理（这是我们的设定；组织块和保存方式也不同） |
| [Abedini 2024](../datasets/abedini-2024.md) | disease / 病 | second lab and cohort: do false alarms stay under control? GEO holds 44 people (21 controls). Ambient RNA and doublets were already removed before release (SoupX, DoubletFinder), so it cannot test the measurement side / 换实验室、换一批人，误报能不能控住。GEO 上有 44 人（21 名对照）。发布前已经用 SoupX、DoubletFinder 去过 ambient 和 doublet，所以测不了测量这一侧 |
| [Janssen 2023](../datasets/janssen-2023.md) | measurement / 测量 | mouse; real ambient measured by genotype, used to calibrate injection / 小鼠；按基因型测出的真实 ambient，用来校准注入 |
| [Hoeft 2024](../datasets/hoeft-2024.md) | measurement / 测量 | under discussion: real human-kidney doublets and ambient from pooled donors. Genotypes reveal only cross-donor doublets; two nuclei from the same donor in one droplet are invisible, so the 250 genotype doublets are a lower bound (partly known tier-2 truth) / 讨论中：多人混样得到的真实人肾 doublet 和 ambient。基因型只能看出跨供体的 doublet，同一个人的两个核进了同一个液滴看不出来，所以 250 个基因型 doublet 只是下限（只部分已知的二级答案） |
| [Lake 2019](../datasets/lake-2019.md) | measurement / 测量 | under discussion: tissue from the same person kept and processed in different ways / 讨论中：同一个人的组织，用不同方式保存和处理 |

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
| T4 | do false alarms stay controlled in a new lab? / 换实验室后误报控不控得住 | every call on a healthy donor is counted as a false alarm (our design choice; healthy tissue also carries altered cells, see above) / 健康人身上报出的都按误报算（这是我们的设定；健康组织里也有 altered 细胞，见上文） | observed rate vs α / 实际误报率 vs 设定的 α |

<!-- ZH -->
!!! warning "已知的坑"
    我们的理解：直接拿 Lake 的 altered 标签当"病"的答案，有一部分是循环的（作者也用了损伤标记基因和 AKI / CKD 富集，不只看 QC 特征）：单核数据里，最大的 altered 组（degenerative）基因数不到正常细胞的一半、线粒体比例约是 5 倍，一个只看 QC 指标的打分器就可能拿到高分。所以基准里必须有"只用 QC 指标"的基线，并且按状态（degenerative / adaptive）分开报结果。[入门模块 9](../onboarding/09-hands-on.md) 的教学流程初步看到了这一点：在 degenerative 核上，kNN 的 AUROC 是 0.76–0.81，只数基因的基线是 0.76–0.85，5 次划分里 kNN 有 4 次更差（只是教学结果，不是基准结果）。
<!-- EN -->
!!! warning "A known trap"
    Our reading: using Lake's altered labels directly as disease ground truth is partly circular (the authors also used injury markers and AKI / CKD enrichment, not only QC features): in the single-nucleus data the largest altered group (degenerative) has less than half the genes of normal nuclei and about five times the mitochondrial fraction, so a scorer that looks only at QC metrics could score well. The benchmark therefore needs a QC-only baseline and reports results per state (degenerative / adaptive). The teaching pipeline in [onboarding module 9](../onboarding/09-hands-on.md) already shows a first sign of this: on degenerative nuclei kNN reaches AUROC 0.76–0.81 and the gene-count baseline 0.76–0.85, with kNN worse in 4 of 5 splits (a teaching result, not a benchmark result).

## 还没定的 / Open questions

<!-- ZH -->
- T2b 单独成一个任务，还是并进 T4？
- Hoeft 2024 和 Lake 2019 要不要进主线？
- Lake 的 altered 细胞怎么分组：有独立证据的、只靠 QC 类特征判出来的、健康人身上的，各自怎么用。
- Abedini 2024 的数据许可（我们没找到写明的许可，决定能不能发布派生标签）。健康人数已核实：GEO 上 21 名对照。
- 要比较的方法清单。
- 要不要把 [NIH 肾脏 AI 挑战赛](../papers/nih-kidney-ai-challenge-2026/index.md) 当作相关机会：它要在 KPMP 肾活检全切片病理图像里找新的异常，提交窗口 2026-11-05 到 2027-04-29。它考的是图像，不是本课题的单细胞组学，所以只能算图像方向的扩展；现金奖只发给美国公民、永久居民或美国机构。
<!-- EN -->
- Should T2b be its own task or part of T4?
- Should Hoeft 2024 and Lake 2019 join the main line?
- How to split Lake's altered cells: those with independent evidence, those called only from QC-like features, and those in healthy donors.
- The licence of Abedini 2024 (we found no stated licence; it decides whether derived labels can be released). The number of healthy donors is checked: 21 controls on GEO.
- The list of methods to compare.
- Whether to treat the [NIH Kidney AI challenge](../papers/nih-kidney-ai-challenge-2026/index.md) as a related opportunity: it asks for new anomalies in KPMP kidney-biopsy whole-slide images, with submissions open 2026-11-05 to 2027-04-29. It tests images, not this topic's single-cell omics, so it would be an extension towards images; cash prizes go only to US citizens, permanent residents or US entities.

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
再往后，看 [知识图谱](../knowledge-map.md) 里"课题 1"视图的必读论文，以及 [方法 × 数据矩阵](../knowledge-map.md)：虚线格是课题 1 打算补上的地方（有的格子里已经有论文，格子里的说明写了还缺什么）。
<!-- EN -->
After that, see the must-reads in the "Topic 1" view of the [knowledge map](../knowledge-map.md) and the [method × data matrix](../knowledge-map.md), whose dashed cells mark what Topic 1 plans to add (some already hold papers; the note in each cell says what is still missing).

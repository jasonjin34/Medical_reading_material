# 8 · 我们在解决什么问题 / 8 · What we are working on

<!-- ZH -->
!!! abstract "读完能回答"
    - 组里的研究课题各在问什么？
    - 为什么直接在 Lake 上跑异常检测会"假成功"？
    - 前面七个模块的知识，在各个课题里用在哪里？
<!-- EN -->
!!! abstract "After this module you can answer"
    - What does each of the group's research topics ask?
    - Why would running anomaly detection directly on Lake give a false success?
    - Where is the knowledge from modules 1–7 used in each topic?

<!-- ZH -->
前七个模块讲的是数据。这一模块把它们拼起来，写成一个计算机人熟悉的问题，再说明为什么这个问题比看上去难。每个课题的完整设计在 **[研究课题](../research/index.md)** 标签页，这里只讲问题的形状。

本页的数字来自 Lake 2023 在 GEO 上的标签表和模块 9 的代码，都是我们自己跑出来的。
<!-- EN -->
Modules 1–7 were about the data. This module puts them together as a problem a computer scientist knows, then explains why it is harder than it looks. The full design of each topic is under the **[Research topics](../research/index.md)** tab; this page only gives the shape of the problem.

Numbers on this page come from Lake 2023's GEO label table and the code in module 9, run by us.

## 第 1 步 · 一句话说异常检测 / Step 1 · Anomaly detection in one sentence

<!-- ZH -->
**只用正常样本训练，给新样本打一个"有多不正常"的分，分高的就报异常。**

图像里的经典例子：只给模型看完好的螺丝照片，测试时它要把有划痕的螺丝挑出来。训练时没见过任何划痕，所以叫**单类分类**（one-class classification）。

放到我们的数据上：
<!-- EN -->
**Train only on normal samples, give each new sample a score for how abnormal it is, and flag the high scores.**

The classic image example: the model only sees photos of good screws, and at test time it must pick out the scratched ones. It never saw a scratch during training, hence **one-class classification**.

On our data:

| Image anomaly detection / 图像异常检测 | Our data / 我们的数据 |
|---|---|
| one image / 一张图 | one cell = one row of X / 一个细胞 = X 的一行 |
| photos of good screws / 完好螺丝的照片 | **healthy reference**: `reference`-state cells from healthy donors / **健康参考**：健康人身上 `reference` 状态的细胞 |
| scratched screw / 有划痕的螺丝 | `altered`-state cell (`state.l1`, module 2) / `altered` 状态的细胞（`state.l1`，模块 2） |
| anomaly score / 异常分 | e.g. distance to the nearest healthy cells / 比如离最近的健康细胞有多远 |
| AUROC on the test set / 测试集上的 AUROC | same, with Lake's labels as the answer / 一样，拿 Lake 的标签当答案 |

<!-- ZH -->
**AUROC** 可以这样理解：随便拿一个异常细胞和一个正常细胞，模型给异常细胞打分更高的概率。0.5 等于抛硬币，1 是完美。
<!-- EN -->
**AUROC** can be read as: pick one anomalous and one normal cell at random; it is the chance the model scores the anomalous one higher. 0.5 is a coin flip, 1 is perfect.

<!-- ZH -->
!!! tip "计算机类比"
    这和监控里的异常检测一样：只用平时正常运行的日志建一个基线，偏离基线的就报警。难的从来不是"算距离"，而是**基线干不干净、报警是不是真问题、换一台机器基线还准不准**。下面三步讲的正是这三件事。
<!-- EN -->
!!! tip "Computer analogy"
    It is the same as anomaly detection in monitoring: build a baseline from normal logs and alert on anything that drifts from it. The hard part is never computing a distance; it is **whether the baseline is clean, whether an alert is a real problem, and whether the baseline still holds on another machine**. The next three steps are about exactly these three things.

## 第 2 步 · 坑一：高分不等于学会了"病" / Step 2 · Trap 1: a high score does not mean it learned disease

<!-- ZH -->
模块 2 讲过，Lake 的 `state` 标签是专家看聚类和标记基因后判的。最大的一类 altered 细胞 degenerative，恰好也有低质量细胞的特征。我们从 GEO 标签表数的中位数：
<!-- EN -->
Module 2 explained that Lake's `state` labels were assigned by experts reading clusters and marker genes. The largest altered group, degenerative, also has the signs of a low-quality cell. Medians we counted from the GEO label table:

| state.l2 | Genes detected / 检出基因数 | `percent.mt` |
|---|---|---|
| reference | 1,736 | 0.63 |
| degenerative | 791 | 2.95 |

<!-- ZH -->
基因数不到一半，线粒体比例约是 4.7 倍。这不全是巧合：Lake 2023 当初就是把"测到的基因少、线粒体转录本多、内质网相关转录本多、损伤标记基因升高、或者在 AKI / CKD 样本里富集"的簇先标成可能的改变态（Methods）。也就是说，"基因少、线粒体高"有一部分是标签定义本身带进来的（模块 2、模块 6）。所以**一个只数基因的"打分器"**，什么生物学都不懂，也能在 degenerative 上拿到不错的 AUROC。

模块 9 里我们在近端小管（PT）上试了一个最简单的健康参考方法（离最近的 10 个健康细胞的平均距离），按供体换了 5 种划分：
<!-- EN -->
Fewer than half the genes, about 4.7 times the mitochondrial fraction. This is not a coincidence: Lake 2023 first flagged as possible altered states the clusters with "low genes detected, a high number of mitochondrial transcripts, a high number of endoplasmic-reticulum-associated transcripts, upregulation of injury markers… or enrichment in AKI or CKD samples" (Methods). Part of "few genes, high mito" was built into the labels themselves (modules 2 and 6). So **a "scorer" that only counts genes**, knowing no biology at all, can get a decent AUROC on degenerative cells.

In module 9 we tried the simplest healthy-reference method on proximal tubule (PT) cells (mean distance to the 10 nearest healthy cells), over 5 different donor splits:

| On held-out donors / 在没见过的供体上 | kNN to healthy reference / 健康参考 kNN | Gene count only / 只数基因 |
|---|---|---|
| degenerative vs reference | 0.76 – 0.81 | 0.76 – 0.85 |
| adaptive – epi vs reference | 0.53 – 0.71 | 0.30 – 0.34 |

<!-- ZH -->
在 degenerative 上，kNN 并不比"只数基因"好，5 次里有 4 次更差。也就是说，**在 Lake 上报一个漂亮的 AUROC，可能只说明方法学会了"基因少"**，这就是"假成功"。反过来，adaptive 细胞基因反而更多，只数基因的分数低于 0.5。这说明 altered 不是一种东西，结果必须按状态分开报。
<!-- EN -->
On degenerative cells the kNN score is no better than counting genes, and worse in 4 of the 5 splits. So **a good AUROC on Lake may only show that a method learned "few genes"**: the false success. In the other direction, adaptive cells have more genes, so the gene-count score falls below 0.5. Altered is not one thing; results have to be reported per state.

## 第 3 步 · 坑二：异常有两种来源 / Step 3 · Trap 2: anomalies have two sources

<!-- ZH -->
模块 6 讲过，一行看起来异常，可能是病，也可能是测量伪影：doublet、ambient RNA、低质量细胞、解离应激。异常检测方法只回答"离健康参考远不远"，**不回答"为什么远"**。

而 Lake 的标签只有"病"这一边，没有"这是伪影"的标签。所以在 Lake 上，你没法知道方法报出来的细胞里有多少其实是伪影。要回答这个问题，得用**实验设计本身给了答案**的数据：多人混测后按基因型分出的 doublet（只是下限：同一个人的两个细胞进了一个油滴，基因型看不出来，见模块 6）、按品系测出的 ambient、同一个人的组织换测法（模块 6 第 3 步、模块 7）。
<!-- EN -->
Module 6 showed that an abnormal-looking row may be disease or a measurement artifact: doublets, ambient RNA, low-quality cells, dissociation stress. An anomaly detector only answers "is it far from the healthy reference?", **not "why is it far?"**

Lake's labels cover only the disease side; nothing says "this one is an artifact". So on Lake you cannot tell how many of the flagged cells are actually artifacts. Answering that needs data where **the experimental design itself gives the answer**: doublets found by genotype after pooling donors (a lower bound: two cells from the same person stay invisible, module 6), ambient RNA measured through mouse strains, the same donor's tissue measured by several assays (module 6 step 3, module 7).

## 第 4 步 · 坑三：换一批人、换一种测法，基线就偏 / Step 4 · Trap 3: new donors or a new assay shift the baseline

<!-- ZH -->
实际使用时，你要先定一个阈值：分数超过多少就报异常。常见做法是在一批健康人身上取 95% 分位数，希望在别的健康人身上也只有 5% 误报。

模块 9 里，阈值在 3 个健康供体上定，再拿到另外几个没见过的健康人身上检验：5 种划分里，实际误报率在 **0.9% 到 6.3%** 之间，不是稳定的 5%。只是换了几个人就这样；我们预计换实验室、换测法时会偏得更多（还没测过；依据是 [mBDRC 2026](../datasets/mbdrc-2026.md) 里测法解释的表达差异比供体大得多）。这类训练和使用时数据分布不同的问题，叫**分布偏移**（domain shift）。
<!-- EN -->
In practice you must pick a threshold: above which score do you raise an alarm? A common choice is the 95th percentile on some healthy donors, hoping for 5% false alarms on other healthy donors too.

In module 9 the threshold was set on 3 healthy donors and checked on other, unseen healthy donors: across 5 splits the observed false-alarm rate ranged from **0.9% to 6.3%**, not a steady 5%. That is from changing a few people; we expect a new lab or assay to shift it more (not yet measured; in [mBDRC 2026](../datasets/mbdrc-2026.md) the assay explains far more expression variance than the donor). When training and deployment data differ like this, it is called **domain shift**.

## 第 5 步 · 各个课题在问什么 / Step 5 · What each topic asks

<!-- ZH -->
上面三个坑，正是组里课题的出发点。每个课题一句话，细节点进去看：

- **[课题 1 · 肾脏单细胞组学异常检测基准](../research/anomaly-benchmark.md)**：做一个带已知答案的数据集和基准，答案既有"病"也有"测量造成"，检验方法能不能分清两者、误报控不控得住。三个坑分别对应它的"只用 QC 的基线"、"病还是测量"任务和"换实验室后的误报"任务。
- **[课题 2 · 生物医学分析 agent 的结论核查](../research/agent-claims.md)**：AI agent 分析数据后报告"发现了一个新的损伤细胞群"，我们要追溯这条结论有没有代码、数据或文献支撑。坑二在这里换了个形式：agent 可能把 doublet 或低质量细胞说成了病。
<!-- EN -->
These three traps are where the group's topics start. One line per topic; the topic pages have the details:

- **[Topic 1 · A Benchmark for Anomaly Detection in Kidney Single-Cell Omics](../research/anomaly-benchmark.md)**: build a dataset and benchmark with known answers, on both the disease side and the measurement side, to test whether methods can tell the two apart and keep false alarms under control. The three traps map onto its QC-only baseline, its disease-or-measurement task, and its false-alarms-in-a-new-lab task.
- **[Topic 2 · Verifying the Claims of Biomedical Analysis Agents](../research/agent-claims.md)**: when an AI agent analyses data and reports "a new injured cell population", trace whether that claim is backed by code, data or the literature. Trap 2 appears here in another form: the agent may describe doublets or low-quality cells as disease.

## 第 6 步 · 前面的模块用在哪 / Step 6 · Where the earlier modules come in

| Module / 模块 | What you need it for / 用在哪 |
|---|---|
| 1 · X and obs / X 和 obs | split by donor, never by cell; know where labels live / 按供体划分，不按细胞；知道标签在哪一列 |
| 2 · Cells and RNA / 细胞和 RNA | an anomaly is a wrong **state** within a cell type, so score per type / 异常是同一类细胞里的**状态**不对，所以按细胞类型打分 |
| 3 · Kidney / 肾脏 | PT and TAL hold 80% of altered nuclei (our count); know where to look / altered 核有 80% 在 PT 和 TAL（我们数的），知道该看哪里 |
| 4 · Patients and tissue / 病人和取材 | "healthy donor" does not mean "every cell is normal" / "健康人"不等于"每个细胞都正常" |
| 5 · Assays / 测法 | single-nucleus vs single-cell, pooling and genotypes: sources of shift and of ground truth / 单核和单细胞、混样和基因型：偏移的来源，也是答案的来源 |
| 6 · Artifacts / 伪影 | the second source of anomalies; why QC is part of the question / 异常的第二种来源；为什么质控本身就是问题的一部分 |
| 7 · Datasets / 数据集 | which dataset gives which side of the answer / 哪份数据提供哪一边的答案 |

## 自测 / Self-check

<!-- ZH -->
??? question "1. 一个方法在 Lake 的 degenerative 细胞上 AUROC 是 0.8，能说明它学会了识别病变吗？"
    不能。只数基因的打分器在同样的数据上也能到 0.76–0.85。至少要和"只用 QC 指标"的基线比，并按状态分开报。

??? question "2. 为什么光用 Lake 没法评估方法会不会把伪影当成病？"
    Lake 的标签只有"病"这一边，没有哪个细胞被标成伪影。需要实验设计给出伪影答案的数据，比如多人混测后按基因型分出的 doublet（只是下限，同一个人的 doublet 看不出来）。

??? question "3. 阈值在一批健康人身上定成 5% 误报，换一批健康人还是 5% 吗？"
    不一定。模块 9 里换几个人就在 0.9% 到 6.3% 之间变化；换实验室或测法，我们预计偏得更多（分布偏移）。
<!-- EN -->
??? question "1. A method reaches AUROC 0.8 on Lake's degenerative cells. Does that show it learned to recognise disease?"
    No. A scorer that only counts genes reaches 0.76–0.85 on the same data. Compare against a QC-only baseline at least, and report per state.

??? question "2. Why can't Lake alone show whether a method mistakes artifacts for disease?"
    Lake's labels cover only the disease side; no cell is labelled as an artifact. You need data where the design gives the artifact answer, such as doublets found by genotype after pooling donors (a lower bound: same-person doublets stay hidden).

??? question "3. A threshold set for 5% false alarms on some healthy donors: is it still 5% on other healthy donors?"
    Not necessarily. In module 9, changing a few people moved it between 0.9% and 6.3%; we expect a new lab or assay to move it more (domain shift).

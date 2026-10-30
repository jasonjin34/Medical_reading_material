# 8 · 从数据到研究问题 / 8 · From data to research questions

<!-- ZH -->
!!! abstract "读完能回答"
    - 组里的大方向是什么？为什么第一步是"找出不正常的细胞"？
    - 把这一步写成机器学习问题，输入、输出、评价指标分别是什么？
    - 为什么这个问题比看上去难？
<!-- EN -->
!!! abstract "After this module you can answer"
    - What is the group's overall direction, and why is the first step "find the abnormal cells"?
    - Written as a machine-learning problem, what are the input, the output and the metric?
    - Why is this problem harder than it looks?

<!-- ZH -->
模块 1–7 讲的是数据：它从哪来、长什么样、有哪些坑。这一模块换个角度：**拿着这些数据，机器学习要解决什么问题，难点在哪。**
<!-- EN -->
Modules 1–7 were about the data: where it comes from, what it looks like, where its traps are. This module changes the angle: **given this data, what problem does machine learning solve, and where is it hard?**

## 第 1 步 · 大方向：检测 → 建模 → 逆转 / Step 1 · The direction: detect → model → revert

<!-- ZH -->
组里的长期方向可以分成三步：

1. **检测**（detect）：在组织里找出被疾病或药物改变了的细胞。在数据里，就是在 X 里找出"不正常"的行。
2. **建模**（model）：把组织做成一个可以在电脑上改动、预测的"虚拟组织"（virtual tissue）。
3. **逆转**（revert）：预测改动哪些基因能把异常细胞拉回正常，再交给湿实验（wet lab）验证。

后两步都建立在第一步上：如果连"哪些细胞不正常"都判断错了，后面建的模型和预测的基因就都没有意义。所以目前组里的工作集中在第一步，以及**怎么确认一个分析结论是可靠的**。本页只讲第一步。
<!-- EN -->
The group's long-term direction has three steps:

1. **Detect**: find the cells that disease or a drug has changed. In the data, that means finding the "abnormal" rows of X.
2. **Model**: turn the tissue into a "virtual tissue" that can be changed and queried on a computer.
3. **Revert**: predict which gene changes would bring abnormal cells back to normal, then test that in the wet lab.

Steps 2 and 3 build on step 1: if we get "which cells are abnormal" wrong, the model and the predicted genes mean nothing. So the group's current work is on step 1, and on **how to tell whether an analysis result can be trusted**. This page covers step 1 only.

## 第 2 步 · 把"检测"写成机器学习问题 / Step 2 · Detection as a machine-learning problem

<!-- ZH -->
最自然的写法是**异常检测**（anomaly detection）：**只用正常样本训练，给新样本打一个"有多不正常"的分，分高的就报异常。**

图像里的经典例子：只给模型看完好的螺丝照片，测试时让它把有划痕的挑出来。训练时没见过划痕，所以也叫**单类分类**（one-class classification）。为什么不直接训练一个"正常 vs 病"的分类器？因为病变的样子很多，很难每一种都有标注；健康样本反而容易拿到。

对照到我们的数据：
<!-- EN -->
The natural framing is **anomaly detection**: **train only on normal samples, give each new sample a score for how abnormal it is, and flag the high scores.**

The classic image example: show a model only photos of good screws, then ask it to pick out the scratched ones. It never saw a scratch in training, hence **one-class classification**. Why not train a "normal vs disease" classifier? Disease takes many forms and few of them come with labels; healthy samples are much easier to get.

Mapped onto our data:

| Image anomaly detection / 图像异常检测 | Our data / 我们的数据 |
|---|---|
| one image / 一张图 | one cell = one row of X / 一个细胞 = X 的一行 |
| photos of good screws / 完好螺丝的照片 | **healthy reference**: `reference`-state cells from healthy donors / **健康参考**：健康人身上 `reference` 状态的细胞 |
| scratched screw / 有划痕的螺丝 | `altered`-state cell (`state.l1`, module 2) / `altered`（改变态）细胞（`state.l1`，模块 2） |
| anomaly score / 异常分 | e.g. distance to the nearest healthy cells / 比如离最近的健康细胞有多远 |
| how good is it? / 好不好怎么算 | AUROC, with Lake's labels as the answer / AUROC，拿 Lake 的标签当答案 |

<!-- ZH -->
**AUROC**（ROC 曲线下面积）可以这样理解：随便拿一个异常细胞和一个正常细胞，模型给异常细胞打分更高的概率。0.5 等于抛硬币，1 是完美。

真正用的时候还要定一个**阈值**（threshold）：分数超过多少就报异常。常见做法是在一批健康人身上取 95% 分位数（percentile），希望在别的健康人身上也只有 5% 误报（false alarm）。
<!-- EN -->
**AUROC** can be read as: pick one abnormal and one normal cell at random; it is the chance the model scores the abnormal one higher. 0.5 is a coin flip, 1 is perfect.

In real use you also need a **threshold**: above which score do you raise an alarm? A common choice is the 95th percentile on some healthy donors, hoping for 5% false alarms on other healthy donors too.

<!-- ZH -->
!!! tip "计算机类比"
    这和运维监控（monitoring）一样：用平时正常运行的日志建一个基线（baseline），偏离基线就报警（alert）。难的从来不是"算距离"，而是三件事：**分数高是不是因为真有问题？报警的原因到底是什么？换一台机器，基线还准不准？** 下一步正好对应这三件事。
<!-- EN -->
!!! tip "Computer analogy"
    It is like monitoring: build a baseline from normal logs and alert on anything that drifts from it. The hard part is never computing a distance; it is three things: **is a high score caused by a real problem? what is the alert actually about? does the baseline still hold on another machine?** The next step covers exactly these three.

## 第 3 步 · 为什么比看上去难 / Step 3 · Why it is harder than it looks

### 难点一：分数高，不一定是学会了"病" / Difficulty 1: a high score may not mean it learned disease

<!-- ZH -->
Lake 的 altered 标签是专家看聚类（cluster）后判的，判的时候也参考了"测到的基因少、线粒体比例高"这类质量信号（模块 2、模块 6）。结果是，最大的一类 altered 细胞 degenerative（退行性）和低质量细胞长得很像。我们从 GEO 标签表数的中位数（median）：
<!-- EN -->
Lake's altered labels were assigned by experts reading clusters, partly using quality signals such as "few genes detected, high mitochondrial fraction" (modules 2 and 6). As a result, the largest altered group, degenerative, looks a lot like low-quality cells. Medians we counted from the GEO label table:

| state.l2 | Genes detected / 检出基因数 | `percent.mt` |
|---|---|---|
| reference | 1,736 | 0.63 |
| degenerative | 791 | 2.95 |

<!-- ZH -->
所以一个**什么生物学都不懂、只数基因个数的打分器**，也能在 degenerative 上拿到不错的 AUROC。模块 9 里你会亲手跑一遍：正经的 kNN（k 近邻）方法并不比它好。

**启示：**AUROC 高不代表方法学会了"病"。评价时一定要和"只用质控指标"的简单基线比，并且按细胞状态分开报。
<!-- EN -->
So a **scorer that knows no biology and only counts genes** can reach a decent AUROC on degenerative cells. In module 9 you will run this yourself: a proper kNN method does no better.

**Takeaway:** a high AUROC does not mean a method learned disease. Always compare against a simple QC-only baseline, and report each cell state separately.

### 难点二：一行"不正常"，原因不止是病 / Difficulty 2: an abnormal row has more causes than disease

<!-- ZH -->
模块 6 讲过，一行看起来不正常，可能是病，也可能是测量伪影（measurement artifact，比如双细胞 doublet、游离 RNA 污染 ambient RNA）、处理带来的变化（解离应激 dissociation stress），或者批次效应（batch effect）。异常检测只回答"离健康参考远不远"，**不回答"为什么远"**。

而 Lake 只标了"病"这一边，没有哪个细胞被标成"伪影"。所以光用 Lake，没法知道方法报出来的细胞里有多少其实是伪影。

**启示：**要回答"为什么远"，需要另一类数据：**实验设计本身就给出答案**的数据，比如多人混测（pooling）后按基因型找出的 doublet（模块 5.2、模块 6、模块 7）。
<!-- EN -->
Module 6 showed that an abnormal-looking row may be disease, a measurement artifact (doublets, ambient RNA), a handling change (dissociation stress) or a batch effect. Anomaly detection only answers "is it far from the healthy reference?", **not "why is it far?"**

Lake labels only the disease side; no cell is labelled as an artifact. So Lake alone cannot tell you how many flagged cells are really artifacts.

**Takeaway:** answering "why is it far?" needs a different kind of data, where **the experimental design itself gives the answer**, such as doublets found by genotype after pooling donors (modules 5.2, 6 and 7).

### 难点三：换一批人、换一种测法，基线就偏 / Difficulty 3: new donors or a new assay shift the baseline

<!-- ZH -->
阈值是在一批健康人身上定的。换一批健康人，误报率还是 5% 吗？模块 9 里你会看到：只是换了几个人，误报率就在 **0.9% 到 6.3%** 之间跳。换实验室、换测法，我们预计偏得更多（还没测过；[mBDRC 2026](../datasets/mbdrc-2026.md) 里测法造成的表达差异比供体大得多）。训练和使用时数据分布不同，叫**分布偏移**（domain shift，名词表里叫域偏移）。

**启示：**一个方法在一份数据上好用，不代表换一份数据还好用。评价时要在没见过的供体（donor）上测，最好也在别的实验室、别的测法上测。
<!-- EN -->
The threshold is set on one group of healthy donors. On a different group of healthy donors, is the false-alarm rate still 5%? In module 9 you will see that changing just a few people moves it anywhere from **0.9% to 6.3%**. We expect a new lab or assay to shift it more (not yet measured; in [mBDRC 2026](../datasets/mbdrc-2026.md) the assay explains far more expression variance than the donor). When training and deployment data differ like this, it is called **domain shift**.

**Takeaway:** a method that works on one dataset may not work on the next. Test on unseen donors, and ideally on other labs and other assays.

## 第 4 步 · 组里的课题从这里出发 / Step 4 · Where the group's topics start

<!-- ZH -->
上面三个难点，是组里现有课题共同的出发点。每个课题要回答什么、做出什么、进行到哪，在 **[研究课题](../research/index.md)** 标签页，这里不重复。读的时候可以带着一个问题：**这个课题在处理哪一个难点？**
<!-- EN -->
These three difficulties are the common starting point of the group's current topics. What each topic asks, what it will produce and where it stands are under the **[Research topics](../research/index.md)** tab, not repeated here. Read them with one question in mind: **which difficulty is this topic dealing with?**

## 第 5 步 · 前面的模块用在哪 / Step 5 · Where the earlier modules come in

| Module / 模块 | What you need it for / 用在哪 |
|---|---|
| 1 · X and obs / X 和 obs | split by donor, never by cell; know where labels live / 按供体划分，不按细胞；知道标签在哪一列 |
| 2 · Cells and RNA / 细胞和 RNA | an anomaly is a wrong **state** within a cell type, so score per type / 异常是同一类细胞里的**状态**不对，所以按细胞类型打分 |
| 3 · Kidney / 肾脏 | PT and TAL hold 80% of altered nuclei (our count); know where to look / altered 核有 80% 在 PT 和 TAL（我们数的），知道该看哪里 |
| 4 · Patients and tissue / 病人和取材 | "healthy donor" does not mean "every cell is normal" / "健康人"不等于"每个细胞都正常" |
| 5 · Assays / 测法 | sources of shift, and of known answers (pooling, genotypes) / 偏移的来源，也是已知答案的来源（混样、基因型） |
| 6 · Artifacts / 伪影 | difficulty 2: the other causes of an abnormal row / 难点二：一行不正常的其他原因 |
| 7 · Datasets / 数据集 | which dataset gives which kind of answer / 哪份数据提供哪一类答案 |

## 自测 / Self-check

<!-- ZH -->
??? question "1. 为什么组里先做\"检测\"，而不是直接做\"逆转\"？"
    逆转要预测"改哪些基因能把异常细胞拉回正常"，前提是知道哪些细胞真的异常。检测错了，后面全错。

??? question "2. 一个方法在 Lake 的 degenerative 细胞上 AUROC 是 0.8，能说明它学会了识别病变吗？"
    不能。degenerative 细胞基因少、线粒体比例高，只数基因的打分器也能拿到差不多的分。要和"只用质控指标"的基线比，并按状态分开报。

??? question "3. 阈值在一批健康人身上定成 5% 误报，换一批健康人还是 5% 吗？"
    不一定。换几个人就可能在 0.9% 到 6.3% 之间变化；换实验室或测法，预计偏得更多（分布偏移）。
<!-- EN -->
??? question "1. Why does the group start with detection rather than going straight to reversion?"
    Reversion predicts which gene changes bring abnormal cells back to normal, which assumes we know which cells are truly abnormal. Get detection wrong and everything after it is wrong.

??? question "2. A method reaches AUROC 0.8 on Lake's degenerative cells. Does that show it learned to recognise disease?"
    No. Degenerative cells have few genes and a high mitochondrial fraction, so a scorer that only counts genes gets about the same score. Compare against a QC-only baseline and report per state.

??? question "3. A threshold set for 5% false alarms on some healthy donors: is it still 5% on other healthy donors?"
    Not necessarily. Changing a few people can move it between 0.9% and 6.3%; a new lab or assay is expected to move it more (domain shift).

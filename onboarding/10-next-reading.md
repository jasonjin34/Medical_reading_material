# 10 · 接下来读什么 / 10 · What to read next

<!-- ZH -->
!!! abstract "读完能回答"
    - 一篇精读怎么在 20 分钟内读完？
    - 先读哪 3 篇精读？
    - 各个课题的阅读路线、知识图谱、文献综述分别在哪，怎么用？
<!-- EN -->
!!! abstract "After this module you can answer"
    - How do you get through a deep-read in 20 minutes?
    - Which three deep-reads come first?
    - Where are each topic's reading path, the knowledge map and the literature review, and how do you use them?

<!-- ZH -->
入门到这里就结束了。之后的阅读都在**论文**标签页：每篇论文有一页中英对照的**精读**（论文精读），还有把它们串起来的文献综述和知识图谱。这一模块告诉你从哪里开始、按什么顺序读。
<!-- EN -->
Onboarding ends here. From now on you read under the **Papers** tab: every paper has a bilingual **deep-read** page, plus a literature review and a knowledge map that tie them together. This module tells you where to start and in what order.

## 第 1 步 · 一篇精读怎么读 / Step 1 · How to read a deep-read

<!-- ZH -->
每篇精读的结构都一样。不用从头读到尾，按这个顺序，20 分钟左右能读完一篇：

1. **一句话**：这篇做了什么；
2. **与本研究方向的关系**：它和我们的课题有什么关系，**最重要的一节**；
3. **数据**：用了什么数据、多少人（模块 7 的六个问题这时就用上了）；
4. **主要结果**：只看和第 2 节有关的那几条；
5. **局限**：它没解决什么，往往就是我们要做的；
6. 需要时再看**方法**和**可复用资产**（代码、数据、模型的链接）。

页头的 `status` 标明这篇读的是什么：`complete` 是读了全文；`abstract-only` 是只能读到摘要（比如付费墙），内容会更少，也更谨慎。论文列表里标 ★ 的是和我们方向高度相关的。
<!-- EN -->
Every deep-read has the same structure. Do not read it top to bottom; in this order one takes about 20 minutes:

1. **One-liner**: what the paper did;
2. **Relation to our direction**: how it connects to our topics, **the most important section**;
3. **Data**: which data and how many people (module 7's six questions come in here);
4. **Key results**: only the ones that matter for section 2;
5. **Limitations**: what it leaves open, which is often what we work on;
6. **Method** and **Reusable assets** (links to code, data, models) when you need them.

The `status` in the page header says what was read: `complete` means the full text; `abstract-only` means only the abstract was available (a paywall, for example), so the notes are shorter and more cautious. Papers marked ★ in the paper list are highly relevant to our direction.

<!-- ZH -->
!!! tip "计算机类比"
    把精读当成读别人的设计文档：先看 summary 和"跟我们的系统有什么关系"，再挑跟你手上问题相关的章节看，最后才看实现细节。
<!-- EN -->
!!! tip "Computer analogy"
    Read a deep-read like someone else's design doc: summary and "how it relates to our system" first, then the sections relevant to your problem, and implementation details last.

## 第 2 步 · 所有人都先读的三篇 / Step 2 · Three deep-reads for everyone

<!-- ZH -->
不管你在哪个课题，先读这三篇。它们分别对应模块 8 的三个坑，读的时候带着括号里的问题：

1. **[Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md)**：你在模块 9 用的就是它的数据。（altered 状态是怎么判出来的？哪些依据和 QC 指标重合？）
2. **[Janssen 2023](../papers/janssen-ambient-noise-genomebiol-2023/index.md)**：用小鼠品系的 DNA 差异，测出每个细胞里有多少 ambient 污染。（为什么"实验设计给的答案"比表达谱更可靠？）
3. **[Dann 2023](../papers/healthy-ref-natgenet-2023/index.md)**：用健康参考找疾病改变的细胞状态，参考该怎么选。（参考和查询数据来源不同时，误报为什么会变多？）

三篇大约 1 小时。
<!-- EN -->
Whatever your topic, read these three first. Each matches one of module 8's traps; read with the question in brackets:

1. **[Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md)**: the data you used in module 9. (How were the altered states called? Which of the criteria overlap with QC metrics?)
2. **[Janssen 2023](../papers/janssen-ambient-noise-genomebiol-2023/index.md)**: uses DNA differences between mouse strains to measure how much ambient contamination each cell carries. (Why is an answer given by the experimental design more reliable than the expression profile?)
3. **[Dann 2023](../papers/healthy-ref-natgenet-2023/index.md)**: finding disease-altered cell states against a healthy reference, and how to choose that reference. (Why do false positives rise when reference and query come from different sources?)

About 1 hour for the three.

## 第 3 步 · 你所在课题的阅读路线 / Step 3 · Your topic's reading path

<!-- ZH -->
每个课题页的最后一节是**阅读路线**：按顺序排好的 5 篇左右精读，并说明每篇为什么读。打开你的课题页，从那里接着读：

- [课题 1 · 肾脏单细胞组学异常检测基准](../research/anomaly-benchmark.md)
- [课题 2 · 生物医学分析 agent 的结论核查](../research/agent-claims.md)

上面三篇里已经读过的就跳过。
<!-- EN -->
The last section of every topic page is a **reading path**: about five deep-reads in order, each with a reason. Open your topic page and continue from there:

- [Topic 1 · A Benchmark for Anomaly Detection in Kidney Single-Cell Omics](../research/anomaly-benchmark.md)
- [Topic 2 · Verifying the Claims of Biomedical Analysis Agents](../research/agent-claims.md)

Skip any you already read in step 2.

## 第 4 步 · 用知识图谱找下一篇 / Step 4 · Use the knowledge map to find the next paper

<!-- ZH -->
读完阅读路线以后，用 **[知识图谱](../knowledge-map.md)** 自己往下找。它有几种视图：

- **每个课题一个视图**：论文按主题分组（课题 1 有"通用异常检测方法""图谱与疾病状态""质控与伪影"等 7 组）。组默认折叠，点开看组里的论文；双击论文打开精读。知识图谱页上的"流程图"一节把这些组排成课题的流程（课题 1 是"公开肾脏图谱 → 质控与去伪影 → 健康组织模型 → 异常 / OOD 打分 → 跨模态验证 → 对照专家评测"）。
- **桥**：不止一个课题要读的论文。
- **方法 × 数据矩阵**：行是异常检测的方法类型，列从通用数据一直到肾脏组学；箭头表示一个方法被搬到了另一类数据上，**虚线格是课题 1 打算补上的地方**（有的格子里已经有论文，课题 1 要做的是那里还缺的部分，见格子里的说明）。

一个好用的读法：在矩阵里找到你最熟悉的那一格（比如图像异常检测里的最近邻方法 PatchCore），顺着箭头看它被搬到了哪些数据上，以及在到达肾脏组学之前断在了哪里。
<!-- EN -->
After the reading path, find further papers yourself with the **[knowledge map](../knowledge-map.md)**. It has several views:

- **One view per topic**: papers grouped by theme (Topic 1 has 7 groups such as "General AD methods", "Atlases & disease states", "QC & artifacts"). Groups start collapsed; click to open one, double-click a paper to open its deep-read. The "Pipelines" section of the knowledge-map page lays these groups out as the topic's pipeline (Topic 1: public kidney atlases → QC & artifact removal → model of healthy tissue → anomaly / OOD score → cross-modal check → evaluation vs. experts).
- **Bridge**: papers that more than one topic needs.
- **Method × data matrix**: rows are kinds of anomaly-detection method, columns go from general data to kidney omics; arrows show a method carried over to another kind of data, and **dashed cells mark what Topic 1 plans to add** (some already hold papers; the note in each cell says what is still missing).

A useful way in: find the cell you know best in the matrix (for example PatchCore, the nearest-neighbour method from image anomaly detection) and follow its arrows to see which kinds of data it has reached, and where the chain stops before kidney omics.

## 第 5 步 · 文献综述 / Step 5 · The literature review

<!-- ZH -->
**[文献综述](../literature-review.md)** 是论文库早期写的一篇综述，覆盖最早的 18 篇（以病理、空间组学、基础模型、虚拟细胞为主，另有两篇医学影像、一篇单细胞扰动），按"检测 → 建模 → 逆转"三个阶段讲，倒数第二节是**综合与空白**。它还没有收入肾脏组学、通用异常检测和 agent 方面的论文，所以和两个课题的阅读路线重合很少；把它当作整个方向的背景来读。
<!-- EN -->
The **[literature review](../literature-review.md)** is an early essay covering the library's first 18 items (mostly histopathology, spatial omics, foundation models and virtual cells, plus two medical-imaging papers and one single-cell perturbation paper), organised by the three stages "detect → model → revert", with **Synthesis & gaps** as its second-to-last section. It does not yet include the kidney-omics, general anomaly-detection or agent papers, so it overlaps little with the two topics' reading paths; read it as background on the wider direction.

## 第 6 步 · 发现新论文怎么办 / Step 6 · When you find a new paper

<!-- ZH -->
论文库是组里一起维护的。发现值得读的新论文，告诉负责维护的人，或者按仓库 `CLAUDE.md` 里的流程自己加：一条命令建好论文目录，再写中英对照的精读。规则只有两条最重要：**精读要基于原文，不凭记忆写；读不到全文就标 `abstract-only`**。
<!-- EN -->
The paper library is maintained by the group. When you find a paper worth reading, tell whoever maintains the library, or add it yourself with the workflow in the repository's `CLAUDE.md`: one command creates the paper folder, then you write the bilingual deep-read. Two rules matter most: **base the deep-read on the paper itself, never on memory; if you cannot get the full text, mark it `abstract-only`**.

## 自测 / Self-check

<!-- ZH -->
??? question "1. 时间只够读精读的一节，读哪一节？"
    "与本研究方向的关系"。它说明这篇和我们的课题有什么关系，决定你要不要继续读下去。

??? question "2. 想知道课题 1 还有哪些空白，看哪里？"
    知识图谱里的方法 × 数据矩阵，虚线格是课题 1 要补的地方；课题 1 页面的"为什么还没解决"和"还没定的"两节也写了。

??? question "3. 一篇精读的页头写着 `abstract-only`，读的时候要注意什么？"
    它只基于摘要和公开信息，没读到全文。具体数字和方法细节可能不全，引用前最好找到原文核对。
<!-- EN -->
??? question "1. You only have time for one section of a deep-read. Which one?"
    "Relation to our direction". It says how the paper connects to our topics, which decides whether to keep reading.

??? question "2. Where do you look to see what gaps Topic 1 still has?"
    The method × data matrix in the knowledge map, where dashed cells mark what Topic 1 adds; also the "Why it is unsolved" and "Open questions" sections of the Topic 1 page.

??? question "3. A deep-read's header says `abstract-only`. What should you keep in mind?"
    It is based on the abstract and public information only, not the full text. Numbers and method details may be incomplete; check the original before citing it.

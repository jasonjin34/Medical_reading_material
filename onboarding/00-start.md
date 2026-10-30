# 从这里开始 / Start here

<!-- ZH -->
这是组里的入门材料，组里各个[研究课题](../research/index.md)共用，写给刚加入的学生和同事，尤其是**计算机背景、没学过生物**的人。读完以后，你应该能看懂肾脏单细胞数据是怎么来的、长什么样、有哪些坑，以及我们到底在解决什么问题。之后再去读论文库里的精读，就不会卡在背景知识上。
<!-- EN -->
This is the group's onboarding material, shared by all of the group's [research topics](../research/index.md), written for new students and colleagues, especially those with a **computer-science background and no biology**. After reading it you should understand how kidney single-cell data is made, what it looks like, where its traps are, and what problem we are working on. The deep-reads in the paper library will then be readable without getting stuck on background.

## 路线图 / Roadmap

<!-- ZH -->
第 1 天大约 6 小时，读完就能看懂数据；第 2 天可选，动手跑代码、开始读论文。每个模块都可以单独读，但建议按顺序来。
<!-- EN -->
Day 1 takes about 6 hours and gets you to the point of understanding the data. Day 2 is optional: run code and start on the papers. Each module stands on its own, but reading in order is easiest.

| Module / 模块 | Time / 时间 | You will be able to answer / 读完能回答 |
|---|---|---|
| [1 · Two tables: X and obs](01-two-tables.md) / [1 · 两张表：X 和 obs](01-two-tables.md) | 30 min / 30 分钟 | What is a row, a column, a label? / 行、列、标签分别是什么？ |
| [2 · Cells and RNA](02-cells-rna.md) / [2 · 细胞和 RNA](02-cells-rna.md) | 30 min / 30 分钟 | Where is RNA in a cell; cell type vs cell state? / RNA 在细胞哪里；细胞类型和细胞状态有什么区别？ |
| [3 · The kidney](03-kidney.md) / [3 · 肾脏](03-kidney.md) | 45 min / 45 分钟 | What are PT and TAL, and why do they get injured first? / PT、TAL 是什么，为什么最先受伤？ |
| [4 · Patients and tissue](04-patients-tissue.md) / [4 · 病人和取材](04-patients-tissue.md) | 30 min / 30 分钟 | Why do healthy donors also have "abnormal" cells? / 为什么健康人身上也有"异常"细胞？ |
| [5.1 · Assays: tissue to matrix](05-1-assays-rna.md) / [5.1 · 测法：从组织到矩阵](05-1-assays-rna.md) | 45 min / 45 分钟 | How do barcodes and UMIs turn tissue into X, and what does single-cell vs single-nucleus cost? / barcode 和 UMI 怎么把组织变成 X，单细胞和单核各有什么代价？ |
| [5.2 · Assays: ATAC, multiome, spatial](05-2-assays-more.md) / [5.2 · 测法：ATAC、多模态、空间](05-2-assays-more.md) | 45 min / 45 分钟 | What other matrices exist besides RNA, and how are pooled people told apart? / 除了 RNA 还有哪些矩阵，混在一起的人怎么分开？ |
| [6 · Artifacts](06-artifacts.md) / [6 · 伪影](06-artifacts.md) | 60 min / 60 分钟 | Is an abnormal row disease, a measurement artifact, handling or batch? / 一行不正常，是病、测量伪影、处理还是批次？ |
| [7 · How to read a dataset](07-datasets.md) / [7 · 怎么读懂一份数据集](07-datasets.md) | 40 min / 40 分钟 | Which questions decide whether a dataset is usable? / 判断一份数据能不能用，要问哪几个问题？ |
| [8 · From data to research questions](08-our-problem.md) / [8 · 从数据到研究问题](08-our-problem.md) | 25 min / 25 分钟 | What problem does machine learning solve here, and why is it hard? / 机器学习在这里解决什么问题，难在哪？ |
| [9 · Hands-on](09-hands-on.md) / [9 · 动手](09-hands-on.md) | Day 2, 3 h / 第 2 天，3 小时 | Load the data and reproduce a first result / 读入数据，复现第一个结果 |
| [10 · What to read next](10-next-reading.md) / [10 · 接下来读什么](10-next-reading.md) | Day 2, 3 h / 第 2 天，3 小时 | Which papers to read, in which order / 读哪些论文、按什么顺序 |

## 每个模块怎么读 / How each module is laid out

<!-- ZH -->
- 开头一个框写着**读完能回答**的问题，先看一眼，带着问题读。
- 正文**一步一步讲**，每个概念都会说明它最后落在数据的哪里：矩阵的哪一行、哪一列，或者标签表里的哪个字段。
- **计算机类比**框把生物概念翻成你熟悉的东西（源代码、进程、batch、ID 冲突……）。
- **生物学提示**框解释正文里顺带出现的生物名词（比如基因名），并给出想深入时可以查的链接。
- 结尾有 2–3 道**自测题**，点开才看到答案；还有**本模块名词**表，每个词都链接到[名词表](glossary.md)。
- 数字都来自我们实际核对过的数据（比如从 GEO 下载的标签表），不凭记忆写；图片只用 CC 授权的原图，注明作者。
<!-- EN -->
- Each module opens with the questions you will **be able to answer**. Skim them first and read with them in mind.
- The text goes **step by step**, and every concept says where it ends up in the data: which rows or columns of the matrix, or which field of the label table.
- **Computer analogy** boxes translate biology into things you already know (source code, processes, batches, ID collisions…).
- **Biology note** boxes explain biology terms that come up in passing (such as gene names), with links for reading further.
- Each module ends with 2–3 **self-check questions** (answers hidden until you open them) and a **terms in this module** table, linked to the [glossary](glossary.md).
- Numbers come from data we checked ourselves (for example the label tables downloaded from GEO), not from memory. Figures are CC-licensed originals with their authors named.

## 这里没有什么 / What is not here

<!-- ZH -->
入门只讲**背景知识**。每份数据的具体信息在 **[数据集](../datasets/index.md)** 标签页，各个课题在做什么在 **[研究课题](../research/index.md)** 标签页，论文精读、文献综述、知识图谱在**论文**标签页；入门的第 10 模块会告诉你按什么顺序去读。
<!-- EN -->
Onboarding covers **background** only. Facts about each dataset are under **[Datasets](../datasets/index.md)**, what each topic is doing is under **[Research topics](../research/index.md)**, and deep-reads, the literature review and the knowledge map are under **Papers**; module 10 tells you what to read and in which order.

# 6 · 伪影，以及长得像伪影的生物状态 / 6 · Artifacts, and biology that looks like one

<!-- ZH -->
!!! abstract "读完能回答"
    - doublet、ambient、低质量细胞、解离应激分别是怎么来的？
    - 它们在数据里长什么样，为什么会被当成病？
    - 哪些真实的生物状态反过来会被当成伪影？
<!-- EN -->
!!! abstract "After this module you can answer"
    - How do doublets, ambient RNA, low-quality cells and dissociation stress arise?
    - What do they look like in the data, and why can they pass for disease?
    - Which real biological states can pass for artifacts?

<!-- ZH -->
这一模块只回答一个问题：**X 里一行看起来不正常，是病造成的，还是别的原因？**

"别的原因"分三类，后面会逐个讲：

- **测量伪影**（artifact）：细胞本身没事，是测量过程让这一行不能代表这个细胞。
- **处理诱发的变化**：细胞真的变了，但起因是实验室里的处理，不是病。
- **批次效应**（batch effect）：不是某一行的问题，而是整批数据一起偏移。

难点在于它们和真实的病变在数据里经常长得一样。所以我们分三步走：

1. **非疾病的变化从哪来**：数据的生成过程默认了什么，每种变化打破了哪一条；
2. **按看到的现象排查**：每种现象都同时列出非疾病的解释和生物的解释，以及靠什么分辨；
3. **这对质控意味着什么**：常规的过滤步骤会删掉什么。
<!-- EN -->
This module answers one question: **when a row of X looks abnormal, is it disease, or something else?**

"Something else" comes in three kinds, covered one by one below:

- **Measurement artifacts**: the cell was fine, but the measurement left a row that does not represent it.
- **Handling-induced changes**: the cell really changed, but lab handling caused it, not disease.
- **Batch effects**: not a problem of one row, but a whole batch of data shifted together.

The difficulty is that they often look just like real disease in the data. So we go in three steps:

1. **Where non-disease changes come from**: what the data-making process assumes, and which assumption each change breaks;
2. **Check by what you see**: for each pattern, the non-disease reading and the biology reading side by side, and what tells them apart;
3. **What this means for QC**: what the usual filtering steps remove.

## 第 1 步 · 非疾病的变化从哪来 / Step 1 · Where non-disease changes come from

<!-- ZH -->
数据是这样产生的（模块 5 详细讲）：组织被消化成单个细胞（或提取出细胞核），仪器把它们一个个包进小油滴，每个油滴一个 **barcode**，最后 **一个 barcode = X 的一行**。

这一套默认了几件事：**油滴里正好一个细胞、这个细胞是完好的、读到的 RNA 只来自它自己、处理过程不改变细胞、每批数据的测量方式一样**。下表按三类列出每种变化打破了哪一条：
<!-- EN -->
The data is made like this (module 5 has the details): tissue is digested into single cells (or nuclei are extracted), an instrument wraps them one by one into tiny oil droplets, each droplet gets a **barcode**, and in the end **one barcode = one row of X**.

This assumes several things: **each droplet holds exactly one cell, the cell is intact, the RNA read comes only from that cell, handling does not change the cell, and every batch is measured the same way**. The table lists, by kind, which assumption each change breaks:

| Kind / 类别 | Change / 变化 | Assumption broken / 被打破的假设 | What happened / 发生了什么 |
|---|---|---|---|
| measurement artifact / 测量伪影 | empty droplet / 空液滴 | exactly one cell / 正好一个细胞 | no cell, only RNA floating in the liquid / 没装细胞，只有漂在液体里的 RNA |
| measurement artifact / 测量伪影 | doublet / 双细胞 | exactly one cell / 正好一个细胞 | two cells in one droplet, sharing a barcode / 两个细胞进了同一个油滴 |
| measurement artifact / 测量伪影 | low-quality cell / 低质量细胞 | the cell is intact / 细胞完好 | the cell broke and lost part of its RNA / 细胞破了，漏掉一部分 RNA |
| measurement artifact / 测量伪影 | ambient RNA / 游离 RNA 污染 | RNA only from this cell / RNA 只来自它自己 | RNA released by broken cells, the "soup", gets into every droplet / 破细胞释放的 RNA 形成一锅"汤"，每个油滴都舀进一点 |
| handling-induced / 处理诱发 | dissociation stress / 解离应激 | handling does not change the cell / 处理不改变细胞 | digestion at 37 °C makes the cell switch on stress genes / 37 °C 消化时细胞真的打开了应激基因 |
| batch / 批次 | batch effect / 批次效应 | every batch measured the same way / 每批测法一样 | a different date, reagent lot or assay shifts a whole batch / 换日期、试剂批号或测法，整批数据一起偏移 |

<!-- ZH -->
三类的区别：

- **测量伪影**只影响个别行，这一行不代表细胞的真实状态，严格意义上的"伪影"指的就是这一类。
- **解离应激**里，RNA 的变化是真实发生的，只是发生在组织离开身体之后。文献里常把它也叫作"解离伪影"（dissociation artifact），因为它不是我们想测的那个状态。
- **批次效应**影响一整批的所有行。它里面既有纯技术的偏移，也可能有真实的差别（比如单核和单细胞测法本来就抓到不同部分的 RNA，模块 5）。它更像一个**混杂因素**：怕的是它和"病"恰好重合。

还有一种不属于这三类、但到处都在的噪声：**技术性丢失**（dropout）。模块 1 讲过 X 里大部分是 0，其中很多只是没抓到，不是不表达。所以单个基因是 0，不能当证据。

!!! tip "计算机类比"
    把每个油滴想成一个日志文件，本该只记一台服务器。

    - **测量伪影**：**空液滴**（empty droplet）是空文件；**双细胞**（doublet）是两台服务器写进了同一个文件；**低质量细胞**（low-quality cell）是服务器写到一半崩了；**游离 RNA 污染**（ambient RNA）是共享磁盘上的残留日志混进了每个文件。
    - **处理诱发**：**解离应激**（dissociation stress）是监控探针本身把服务器的 CPU 拉高了。CPU 是真的高，但原因是探针，不是业务。
    - **批次效应**（batch effect）：换了一版日志格式或采集脚本，整批文件都变了样。
<!-- EN -->
How the three kinds differ:

- **Measurement artifacts** affect individual rows; the row does not represent the cell's real state. This is what "artifact" means in the strict sense.
- In **dissociation stress**, the RNA change really happened, only after the tissue left the body. The literature often calls it a "dissociation artifact" too, because it is not the state we want to measure.
- A **batch effect** affects every row of a batch. It contains purely technical shifts and possibly real differences (single-nucleus and single-cell assays capture different parts of the RNA, module 5). It acts more like a **confounder**: the danger is when it lines up with disease.

One more kind of noise fits none of the three but is everywhere: **technical dropout**. As module 1 said, most of X is 0, and many of those zeros mean "not caught", not "not expressed". A single gene at 0 is not evidence.

!!! tip "Computer analogy"
    Think of each droplet as a log file meant for one server.

    - **Measurement artifacts**: an **empty droplet** is an empty file; a **doublet** is two servers writing to the same file; a **low-quality cell** is a server that crashed halfway; **ambient RNA** is leftover logs on a shared disk leaking into every file.
    - **Handling-induced**: **dissociation stress** is the monitoring probe itself driving the server's CPU up. The CPU really is high, but the probe caused it, not the workload.
    - **Batch effect**: a new log format or collection script changes a whole batch of files.

## 第 2 步 · 按看到的现象排查 / Step 2 · Check by what you see

<!-- ZH -->
实际分析时，你先看到的是一行数据的**现象**，不知道原因。下面按现象排，每种都有两个解释：非疾病的，和生物（病变）的。
<!-- EN -->
In practice you first see a **pattern** in a row, not its cause. Below, the patterns are listed one by one, each with two readings: non-disease and biological (disease).

### 现象 A · 基因少、线粒体比例高 / Pattern A · Few genes, high mitochondrial fraction

<!-- ZH -->
- **非疾病的解释**：低质量细胞（low-quality cell）或空液滴（empty droplet）。细胞破了，胞质里的 RNA 漏掉，`nCount_RNA`、`nFeature_RNA` 都低；留下来的多是线粒体 RNA，`percent.mt` 偏高。
- **生物的解释**：受损、退化的细胞也是这样。Lake 2023 单核数据里，degenerative 状态的核正是基因更少、线粒体更高（见 [Lake 2023 数据页](../datasets/lake-2023.md)的"已知问题"）。
- **怎么分辨**：只看总数分不开。要看损伤相关的基因有没有升高，而不只是"什么都变少了"。
<!-- EN -->
- **Non-disease reading**: a low-quality cell or an empty droplet. The cell broke and lost cytoplasmic RNA, so `nCount_RNA` and `nFeature_RNA` are low; what stays is mostly mitochondrial RNA, so `percent.mt` is high.
- **Biology reading**: injured, degenerating cells look the same. In Lake 2023's single-nucleus data, degenerative nuclei have exactly fewer genes and more mitochondrial RNA (see the known issues on the [Lake 2023 dataset page](../datasets/lake-2023.md)).
- **What tells them apart**: totals alone cannot. Check whether injury-related genes go up, rather than everything going down.

### 现象 B · 一行里有两类细胞的标记基因 / Pattern B · Markers of two cell types in one row

<!-- ZH -->
比如一个核同时有 PT 的 `LRP2` 和 TAL 的 `UMOD`。

- **非疾病的解释**：双细胞（doublet，PT 和 TAL 两个核进了同一个油滴），或游离 RNA 污染（ambient RNA，TAL 核从"汤"里沾上了 PT 的 RNA；汤里最多的是数量最多那类细胞的 RNA）。单核数据通常比单细胞污染更重，见 [Janssen 2023](../datasets/janssen-2023.md)。
- **生物的解释**：真实的过渡态或修复中的细胞，本来就同时表达两种状态的基因。
- **怎么分辨**：只看表达很难。最可靠的是**基因型**：几个人的样本混在一起测时，一个油滴里出现两个人的 DNA 差异（SNP），才是真 doublet。
<!-- EN -->
For example, one nucleus with both PT's `LRP2` and TAL's `UMOD`.

- **Non-disease reading**: a doublet (a PT and a TAL nucleus in one droplet), or ambient RNA (a TAL nucleus picked up PT RNA from the soup, which is dominated by the most common cell type). Single-nucleus data is usually more contaminated than single-cell data; see [Janssen 2023](../datasets/janssen-2023.md).
- **Biology reading**: real transitioning or repairing cells express genes of both states.
- **What tells them apart**: expression alone hardly can. The most reliable signal is **genotype**: when several people's samples are pooled, only a droplet carrying two people's DNA differences (SNPs) is a true doublet.

<!-- ZH -->
Hoeft 2024 就这样做过：4 个病人的核混在一起测，再按 SNP 分出每个核来自谁。下图右半是结果：按表达被聚成"Mixed/Doublets"的簇里，绝大部分核其实只来自一个人，真正的 doublet（深灰色）很少。**只看表达判断伪影，很容易判错。**具体数字见 [Hoeft 2024 数据页](../datasets/hoeft-2024.md)。
<!-- EN -->
Hoeft 2024 did exactly this: nuclei from 4 patients were pooled, then assigned to people by SNPs. The right half of the figure shows the result: in the cluster that expression called "Mixed/Doublets", most nuclei come from a single person, and true doublets (dark grey) are few. **Judging artifacts from expression alone is easy to get wrong.** The numbers are on the [Hoeft 2024 dataset page](../datasets/hoeft-2024.md).

<!-- ZH/EN --> ![Hoeft 2024 Fig. 2 i–j: expression clusters vs genotype-based donor assignment / 表达聚类和按基因型分人的对照](img/hoeft2024_fig2ij.jpg)

<!-- ZH -->
图：Hoeft 2024 Fig. 2 i–j（肾部分，已截取）。左：混合肾样本的表达聚类；右：每个簇里各病人、doublet（深灰）和未分配核（浅灰）的比例，看最左边 SoupLadle 那一组即可。Hoeft K et al., Nat Commun 2024，CC BY 4.0。
<!-- EN -->
Figure: Hoeft 2024 Fig. 2 i–j (kidney part, cropped). Left: expression clusters of the pooled kidney sample; right: share of each patient, doublets (dark grey) and unassigned nuclei (light grey) per cluster; the left-hand SoupLadle group is enough. Hoeft K et al., Nat Commun 2024, CC BY 4.0.

### 现象 C · RNA 特别多 / Pattern C · Very many RNA molecules

<!-- ZH -->
- **非疾病的解释**：doublet，两个细胞的 RNA 加在一起。
- **生物的解释**：多倍体（polyploidy）或多核细胞。损伤后，一些小管细胞的 DNA 会多出几份，一些足细胞会变成双核，RNA 也就更多。
- **怎么分辨**：同样靠基因型；再看细胞类型，这种细胞主要出现在损伤后的小管和足细胞里。
<!-- EN -->
- **Non-disease reading**: a doublet, two cells' RNA added together.
- **Biology reading**: polyploid or multinucleated cells. After injury, some tubular cells carry extra DNA copies and some podocytes become binucleated, so they have more RNA.
- **What tells them apart**: genotype again; also the cell type, since such cells occur mainly in tubules and podocytes after injury.

### 现象 D · 应激基因高 / Pattern D · Stress genes up

<!-- ZH -->
- **非疾病的解释**：解离应激（dissociation stress）。37 °C 消化时细胞打开 `FOS`、`JUN`、热休克蛋白这类基因；脆弱的细胞（比如足细胞）还会在消化中大量丢失。
- **生物的解释**：组织损伤，或取材时的缺血（模块 4），也会打开同一类基因。Lake 2023 的 degenerative 状态里就有 `FOS` / `JUN`；健康人身上也有不少 altered 细胞，作者认为部分可能来自取样缺血或正常衰老。
- **怎么分辨**：靠只改处理方式的对照实验。同样的小鼠肾，冰上冷消化时应激基因低得多，见 [Denisenko 2020](../datasets/denisenko-2020.md)；人肾上也看到过类似的应激簇，见 [Lake 2019](../datasets/lake-2019.md)。
<!-- EN -->
- **Non-disease reading**: dissociation stress. Digestion at 37 °C switches on `FOS`, `JUN` and heat-shock genes; fragile cells (podocytes, for example) are also largely lost during digestion.
- **Biology reading**: tissue injury, or ischaemia during collection (module 4), switches on the same family of genes. Lake 2023's degenerative state includes `FOS` / `JUN`; healthy donors carry many altered cells too, which the authors suggest may partly come from procurement ischaemia or normal ageing.
- **What tells them apart**: a control experiment that changes only the handling. The same mouse kidney digested cold on ice has far lower stress genes; see [Denisenko 2020](../datasets/denisenko-2020.md). Similar stress clusters have been seen in human kidney; see [Lake 2019](../datasets/lake-2019.md).

### 现象 E · 同一类细胞按批次分成几团 / Pattern E · One cell type splits by batch

<!-- ZH -->
- **非疾病的解释**：批次效应（batch effect）。不同 `library`、不同测法各自偏移。
- **生物的解释**：如果病人和健康人恰好分批测，"批次"和"病"混在一起，分不清哪个是哪个。
- **怎么分辨**：靠实验设计，同一块组织换测法或分批测。[mBDRC 2026](../datasets/mbdrc-2026.md) 就是同一批健康组织用三种测法测：测法带来的差异比人和人之间的差异还大。
<!-- EN -->
- **Non-disease reading**: a batch effect; each `library` or assay is shifted on its own.
- **Biology reading**: if patients and healthy donors happened to be run in separate batches, "batch" and "disease" are mixed up and cannot be told apart.
- **What tells them apart**: the experimental design, measuring the same tissue with several assays or in several batches. [mBDRC 2026](../datasets/mbdrc-2026.md) did this with healthy tissue and three assays: the assay made a bigger difference than the person did.

## 第 3 步 · 汇总 / Step 3 · Summary

| Pattern / 现象 | Non-disease reading / 非疾病的解释 | Biology reading / 生物的解释 | What tells them apart / 靠什么分辨 |
|---|---|---|---|
| A · few genes, high `percent.mt` / 基因少、线粒体高 | low-quality cell, empty droplet / 低质量细胞、空液滴 | injured, degenerating cell / 受损、退化的细胞 | injury genes up, not just counts down / 损伤基因是否升高 |
| B · markers of two cell types / 两类细胞的标记基因 | doublet, ambient RNA / doublet、ambient | transitioning, repairing cell / 过渡、修复中的细胞 | genotype when donors are pooled / 多人混测时看基因型 |
| C · very many RNA molecules / RNA 特别多 | doublet | polyploid, binucleated cell / 多倍体、双核细胞 | genotype; cell type / 基因型；细胞类型 |
| D · stress genes up / 应激基因高 | dissociation stress / 解离应激 | injury, ischaemia / 损伤、缺血 | same tissue, cold vs warm digestion / 同一组织冷热消化对照 |
| E · one cell type splits by batch / 同类细胞按批次分团 | batch effect / 批次效应 | disease, if confounded with batch / 病（如果和批次混在一起） | same tissue, several assays or batches / 同一组织换测法或批次 |

<!-- ZH -->
看最后一列：**能真正分辨的，几乎都是实验设计给的信息**（基因型、换测法、冷热消化对照），而不是表达谱本身。这就是为什么[数据集](../datasets/index.md)页里专门有一组"测量对照"数据。
<!-- EN -->
Look at the last column: **what really tells them apart is almost always information from the experimental design** (genotypes, several assays, cold vs warm digestion), not the expression profile itself. That is why the [Datasets](../datasets/index.md) tab has a group of "measurement control" datasets.

## 第 4 步 · 这对质控意味着什么 / Step 4 · What this means for QC

<!-- ZH -->
大多数分析流程一上来就做**质控**（QC），用模块 1 里那三列删掉可疑的行。对照上面的现象：

- `nFeature_RNA` 太低、`percent.mt` 太高 → 删掉（现象 A），**受损细胞也一起删了**；
- `nCount_RNA` 太高，或 doublet 工具打分高 → 删掉（现象 B、C），**多倍体和过渡态细胞也可能被删**；
- 用工具估计并减掉 ambient（现象 B）。

阈值没有统一标准，每个数据集、每种测法都不一样。
<!-- EN -->
Most analysis pipelines start with **quality control** (QC), using the three columns from module 1 to remove suspicious rows. Matched to the patterns above:

- `nFeature_RNA` too low or `percent.mt` too high → removed (pattern A), **and injured cells go with them**;
- `nCount_RNA` too high, or a high doublet-tool score → removed (patterns B and C), **and polyploid or transitioning cells may go too**;
- a tool estimates and subtracts the ambient counts (pattern B).

There are no universal thresholds; they differ by dataset and assay.

<!-- ZH -->
!!! warning "对我们的问题，质控本身就是问题的一部分"
    常规流程把 QC 当成清洗，删掉就完事。但上面每一条过滤规则，都可能把我们最想找的病变细胞一起删掉。所以我们不能默认"QC 之后的数据就是干净的"：分清非疾病的变化和真实病变，正是我们要解决的问题（模块 8）。
<!-- EN -->
!!! warning "For our problem, QC is part of the question"
    Standard pipelines treat QC as cleaning: remove and move on. But every filtering rule above may also remove the diseased cells we most want to find. So we cannot assume that data after QC is clean: telling non-disease changes from real disease is exactly the problem we work on (module 8).

## 自测 / Self-check

<!-- ZH -->
??? question "1. 一个核同时有 PT 的 `LRP2` 和 TAL 的 `UMOD`，可能是哪几种情况？怎么判断？"
    测量伪影：双细胞（doublet）或游离 RNA 污染（ambient RNA）。生物：真实的过渡态。只看表达很难分；如果样本是多人混测，可以用基因型判断是不是 doublet。

??? question "2. 为什么在我们的问题里，不能直接用常规 QC 阈值过滤完再做异常检测？"
    受损、退化的细胞像低质量细胞（基因少、线粒体高），损伤后的多倍体细胞像 doublet。一刀切的阈值会把我们要找的病变细胞一起删掉。

??? question "3. 解离应激和组织损伤都会让 `FOS` 升高。什么样的数据能帮你分清？"
    只改处理方式、其他条件相同的对照实验，比如同一个肾分别用 37 °C 和冰上消化（Denisenko 2020）。
<!-- EN -->
??? question "1. A nucleus has both PT's `LRP2` and TAL's `UMOD`. What could it be, and how would you tell?"
    Artifacts: a doublet or ambient RNA. Biology: a real transitioning cell. Expression alone can hardly tell; if donors were pooled, genotypes show whether it is a doublet.

??? question "2. Why can't we simply apply standard QC thresholds and then run anomaly detection?"
    Injured, degenerating cells look like low-quality cells (fewer genes, more mitochondrial RNA), and polyploid cells after injury look like doublets. A hard threshold removes the diseased cells we want to find.

??? question "3. Both dissociation stress and tissue injury raise `FOS`. What data helps you tell them apart?"
    A controlled experiment that changes only the handling, for example the same kidney digested at 37 °C and on ice (Denisenko 2020).

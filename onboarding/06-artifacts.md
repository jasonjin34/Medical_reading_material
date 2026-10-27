# 6 · 伪影，以及长得像伪影的生物状态 / 6 · Artifacts, and biology that looks like one

<!-- ZH -->
!!! abstract "读完能回答"
    - doublet（双细胞）、ambient（游离 RNA 污染）、低质量细胞（low-quality cell）、解离应激（dissociation stress）分别是怎么来的？
    - 它们在数据里长什么样，为什么会被当成病？
    - 哪些真实的生物状态反过来会被当成伪影（artifact）？
<!-- EN -->
!!! abstract "After this module you can answer"
    - How do doublets, ambient RNA, low-quality cells and dissociation stress arise?
    - What do they look like in the data, and why can they pass for disease?
    - Which real biological states can pass for artifacts?

<!-- ZH -->
这一模块只回答一个问题：**X 里一行看起来不正常，是病造成的，还是别的原因？**

"别的原因"分三类，后面会逐个讲：

- **测量伪影**（measurement artifact）：细胞本身没事，是测量过程让这一行不能代表这个细胞。
- **处理诱发的变化**（handling-induced change）：细胞真的变了，但起因是实验室里的处理，不是病。
- **批次效应**（batch effect）：不是某一行的问题，而是整批数据一起偏移。

难点在于它们和真实的病变在数据里经常长得一样。所以我们分三步走：

1. **非疾病的变化从哪来**：数据的生成过程默认了什么，每种变化打破了哪一条；
2. **按看到的现象排查**：每种现象都同时列出非疾病的解释和生物的解释，以及靠什么分辨；
3. **这对质控（quality control，QC）意味着什么**：常规的过滤步骤会删掉什么。
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
数据是这样产生的（模块 5 详细讲）：组织被消化（digestion）成单个细胞（或提取出细胞核），仪器把它们一个个包进小油滴（droplet），每个油滴一个 **barcode**，最后 **一个 barcode = X 的一行**。

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
- **批次效应**影响一整批的所有行。它里面既有纯技术的偏移，也可能有真实的差别（比如单核和单细胞测法本来就抓到不同部分的 RNA，模块 5）。它更像一个**混杂因素**（confounder）：怕的是它和"病"恰好重合。

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
实际分析时，你先看到的是一行数据的**现象**（pattern），不知道原因。下面按现象排，每种都有两个解释：非疾病的，和生物（病变）的。
<!-- EN -->
In practice you first see a **pattern** in a row, not its cause. Below, the patterns are listed one by one, each with two readings: non-disease and biological (disease).

### 现象 A · 基因少、线粒体比例高 / Pattern A · Few genes, high mitochondrial fraction

<!-- ZH -->
- **非疾病的解释**：低质量细胞或空液滴。完整细胞的膜破了，胞质（cytoplasm）里的 RNA 漏掉，`nCount_RNA`、`nFeature_RNA` 都低；留下来的多是线粒体里的 RNA，`percent.mt` 偏高 [1]。细胞核不一样：线粒体 RNA 不在核里表达（模块 2），单核数据里测到的线粒体转录本（mitochondrial transcripts），Lake 2019 认为来自贴在核膜（nuclear membrane）上的线粒体，其多少也反映组织处理的质量 [10]。所以单核数据的 `percent.mt` 本来就低得多（Lake 2023 单核中位 0.81%，单细胞中位 23% [3]）。Lake 2019 还发现，TAL 和 PT 的 S3 段这类耗能高、容易缺血（ischaemia）的细胞线粒体转录本更多，和肾切除（nephrectomy）时的热缺血（warm ischaemia）一致 [10]。
- **生物的解释**：受损（injured）、退化（degenerating）的细胞也可能这样。Lake 2023 单核数据里，degenerative 状态的核确实基因更少、线粒体更高（见 [Lake 2023 数据页](../datasets/lake-2023.md)的"已知问题"）。但这不能当独立证据：Lake 2023 当初就是把"测到的基因少、线粒体转录本多、内质网（endoplasmic reticulum）相关转录本多、损伤标记基因（injury marker）升高、或者主要来自 AKI / CKD 样本"的簇（cluster）先标成可能的改变态（altered state）[2]。也就是说，"基因少、线粒体高"有一部分是标签定义带进来的。
- **怎么分辨**：只看总数分不开。要看损伤相关的基因有没有升高，而不只是"什么都变少了"。
<!-- EN -->
- **Non-disease reading**: a low-quality cell or an empty droplet. A whole cell whose membrane broke loses its cytoplasmic RNA, so `nCount_RNA` and `nFeature_RNA` are low; what stays is mostly the RNA inside mitochondria, so `percent.mt` is high [1]. Nuclei differ: mitochondrial transcripts are not expressed in the nucleus (module 2); Lake 2019 reads those found in single-nucleus data as "indicative of mitochondrial association with the nuclear membranes", with levels that also reflect tissue quality during processing [10]. Single-nucleus `percent.mt` is therefore much lower to begin with (median 0.81% in Lake 2023's single-nucleus data vs 23% in its single-cell data [3]). Lake 2019 also found more mitochondrial transcripts in TAL and S3 proximal tubule, regions with high metabolic demand and prone to ischaemia, "consistent with the nephrectomy procedure-related warm ischemia" [10].
- **Biology reading**: injured, degenerating cells can look the same. In Lake 2023's single-nucleus data, degenerative nuclei do have fewer genes and more mitochondrial RNA (see the known issues on the [Lake 2023 dataset page](../datasets/lake-2023.md)). But this is not independent evidence: Lake 2023 first flagged as possible altered states the clusters with "low genes detected, a high number of mitochondrial transcripts, a high number of endoplasmic-reticulum-associated transcripts, upregulation of injury markers… or enrichment in AKI or CKD samples" [2]. Part of "few genes, high mito" was built into the labels.
- **What tells them apart**: totals alone cannot. Check whether injury-related genes go up, rather than everything going down.

### 现象 B · 一行里有两类细胞的标记基因 / Pattern B · Markers of two cell types in one row

<!-- ZH -->
比如一个核同时有 PT 的 `LRP2` 和 TAL 的 `UMOD`。

- **非疾病的解释**：双细胞（PT 和 TAL 两个核进了同一个油滴），或游离 RNA 污染（TAL 核从"汤"里沾上了 PT 的 RNA）。汤的成分因实验而异，可以从空液滴里估计出来 [4]。在一项小鼠肾的研究里，冻存组织做的单核数据比新鲜组织做的单细胞数据污染重得多，见 [Janssen 2023](../datasets/janssen-2023.md)；那里单核和冻存是绑在一起的，所以不能直接推广成"单核一定更脏"。
- **生物的解释**：真实的过渡态（transitioning state）或修复中（repairing）的细胞，本来就同时表达两种状态的基因。
- **怎么分辨**：只看表达很难。**基因型**（genotype）能给出一部分答案：几个人的样本混在一起测时，一个油滴里出现两个人的 DNA 差异（SNP，单核苷酸多态性），就肯定是 doublet [5]。但同一个人的两个细胞进了同一个油滴，基因型看不出来：混 N 个人时，能看出来的 doublet 约占 1 − 1/N [5]，4 个人等量混合时约有四分之一看不出来。所以基因型给的是 doublet 的下限，不是全部。
<!-- EN -->
For example, one nucleus with both PT's `LRP2` and TAL's `UMOD`.

- **Non-disease reading**: a doublet (a PT and a TAL nucleus in one droplet), or ambient RNA (a TAL nucleus picked up PT RNA from the soup). The soup's make-up varies from experiment to experiment and can be estimated from empty droplets [4]. In one mouse-kidney study, single-nucleus data from frozen tissue was far more contaminated than single-cell data from fresh tissue; see [Janssen 2023](../datasets/janssen-2023.md). There, nucleus and frozen tissue go together, so it does not show that single-nucleus data is always dirtier.
- **Biology reading**: real transitioning or repairing cells express genes of both states.
- **What tells them apart**: expression alone hardly can. **Genotype** gives part of the answer: when several people's samples are pooled, a droplet carrying two people's DNA differences (SNPs) is certainly a doublet [5]. Two cells from the same person in one droplet are invisible to genotype: with N people pooled, the detectable share of doublets is about 1 − 1/N [5], so with 4 people in equal shares about a quarter are missed. Genotype gives a lower bound on doublets, not the full list.

<!-- ZH -->
Hoeft 2024 就这样做过：4 个病人的核混在一起测，再按 SNP 分出每个核来自谁 [6]。下图右半是结果：按表达被聚成"Mixed/Doublets"的簇里，大部分核按 SNP 只来自一个人，基因型判出的 doublet（深灰色）很少。同一个人的 doublet 基因型看不出来，所以这不能证明那个簇里没有 doublet；但它说明很多被表达判成"混合"的核其实不是两个人的混合。我们的理解：只看表达判断伪影，很容易判错。具体数字见 [Hoeft 2024 数据页](../datasets/hoeft-2024.md)。
<!-- EN -->
Hoeft 2024 did exactly this: nuclei from 4 patients were pooled, then assigned to people by SNPs [6]. The right half of the figure shows the result: in the cluster that expression called "Mixed/Doublets", most nuclei are assigned to a single person by SNPs, and genotype-called doublets (dark grey) are few. Same-person doublets are invisible to genotype, so this does not prove the cluster is free of doublets; but it shows that many nuclei called "mixed" by expression are not a mix of two people. Our reading: judging artifacts from expression alone is easy to get wrong. The numbers are on the [Hoeft 2024 dataset page](../datasets/hoeft-2024.md).

<!-- ZH/EN --> ![Hoeft 2024 Fig. 2 i–j: expression clusters vs genotype-based donor assignment / 表达聚类和按基因型分人的对照](img/hoeft2024_fig2ij.jpg)

<!-- ZH -->
图：Hoeft 2024 Fig. 2 i–j（肾部分，已截取）[6]。左：示意图，混合肾样本的 UMAP（把高维表达压到二维画图的降维方法）分别按表达聚类和三种按 SNP 分人的方法上色；右：每个簇里各病人、doublet（深灰）和未分配核（unassigned nuclei，浅灰）的比例，看最左边 SoupLadle 那一组即可。Hoeft K et al., Nat Commun 2024，CC BY 4.0。
<!-- EN -->
Figure: Hoeft 2024 Fig. 2 i–j (kidney part, cropped) [6]. Left: a schematic of the pooled kidney UMAP coloured by expression cluster and by three SNP-based donor assignments; right: share of each patient, doublets (dark grey) and unassigned nuclei (light grey) per cluster; the left-hand SoupLadle group is enough. Hoeft K et al., Nat Commun 2024, CC BY 4.0.

### 现象 C · RNA 特别多 / Pattern C · Very many RNA molecules

<!-- ZH -->
- **非疾病的解释**：doublet，两个细胞的 RNA 加在一起。
- **生物的解释**：多倍体（polyploidy）或多核（multinucleated）细胞。急性损伤后，一些小管细胞复制 DNA 却不分裂，变成多倍体（小鼠实验，也在 AKI 后 CKD 病人的活检（biopsy）里看到）[7]；病变肾小球里的足细胞会出现双核（binucleation）[8]。DNA 多了，RNA 也可能更多。我们的理解：双核这一条主要影响单细胞数据；单核数据里两个核一般会被分开测。
- **怎么分辨**：同样靠基因型（只能看出两个人的 doublet）；再看细胞类型，这种细胞主要出现在损伤后的小管和足细胞里。
<!-- EN -->
- **Non-disease reading**: a doublet, two cells' RNA added together.
- **Biology reading**: polyploid or multinucleated cells. After acute injury, some tubular cells copy their DNA without dividing and become polyploid (mouse experiments, also seen in biopsies of patients with CKD after AKI) [7]; podocytes in diseased glomeruli can become binucleated [8]. More DNA can mean more RNA. Our reading: binucleation matters mainly for single-cell data; in single-nucleus data the two nuclei would normally be measured separately.
- **What tells them apart**: genotype again (it only sees two-person doublets); also the cell type, since such cells occur mainly in tubules and podocytes after injury.

### 现象 D · 应激基因高 / Pattern D · Stress genes up

<!-- ZH -->
- **非疾病的解释**：解离应激。37 °C 消化时细胞打开 `Fos`、`Jun`、热休克蛋白（heat-shock protein）这类基因；脆弱的细胞（比如足细胞）还会在消化中大量丢失（小鼠肾）[9]。
- **生物的解释**：组织损伤，或取材时的缺血（模块 4），也可能打开同一类基因。Lake 2023 的 degenerative 状态有共同的 FOS/JUN 信号特征（signature）；健康人身上也有不少 altered 细胞，作者认为可能来自取样时的缺血应激或正常衰老（ageing）[2]。
- **怎么分辨**：靠只改处理方式的对照实验（control experiment）。同窝小鼠（littermate mice）的肾，冰上冷消化（cold dissociation）时应激基因低得多 [9]，见 [Denisenko 2020](../datasets/denisenko-2020.md)；人肾上也看到过类似的应激信号 [10]，见 [Lake 2019](../datasets/lake-2019.md)。
<!-- EN -->
- **Non-disease reading**: dissociation stress. Digestion at 37 °C switches on `Fos`, `Jun` and heat-shock genes; fragile cells (podocytes, for example) are also largely lost during digestion (mouse kidney) [9].
- **Biology reading**: tissue injury, or ischaemia during collection (module 4), can switch on the same family of genes. Lake 2023's degenerative states share a FOS/JUN signalling signature; healthy donors carry many altered cells too, which the authors suggest might arise from ischaemic stress during sample acquisition or normal ageing [2].
- **What tells them apart**: a control experiment that changes only the handling. Kidneys from littermate mice digested cold on ice show far lower stress genes [9]; see [Denisenko 2020](../datasets/denisenko-2020.md). A similar stress signal has been seen in human kidney [10]; see [Lake 2019](../datasets/lake-2019.md).

### 现象 E · 同一类细胞按批次分成几团 / Pattern E · One cell type splits by batch

<!-- ZH -->
- **非疾病的解释**：批次效应。不同 `library`、不同测法各自偏移。
- **生物的解释**：如果病人和健康人恰好分批测，"批次"和"病"混在一起，分不清哪个是哪个。
- **怎么分辨**：靠实验设计（experimental design），同一个人的组织换测法或分批测。[mBDRC 2026](../datasets/mbdrc-2026.md) 用不同测法测了同一批健康供者（donor）的组织（不是每个人都测了所有测法）：比较单细胞和单核 RNA 时，测法解释的表达差异（variance explained）比供者之间的差异大得多 [11]。
<!-- EN -->
- **Non-disease reading**: a batch effect; each `library` or assay is shifted on its own.
- **Biology reading**: if patients and healthy donors happened to be run in separate batches, "batch" and "disease" are mixed up and cannot be told apart.
- **What tells them apart**: the experimental design, measuring the same person's tissue with several assays or in several batches. [mBDRC 2026](../datasets/mbdrc-2026.md) measured tissue from the same healthy donors with different assays (not every donor with every assay): comparing single-cell with single-nucleus RNA, the assay explained much more of the expression variance than the donor did [11].

## 第 3 步 · 汇总 / Step 3 · Summary

| Pattern / 现象 | Non-disease reading / 非疾病的解释 | Biology reading / 生物的解释 | What tells them apart / 靠什么分辨 |
|---|---|---|---|
| A · few genes, high `percent.mt` / 基因少、线粒体高 | low-quality cell, empty droplet / 低质量细胞、空液滴 | injured, degenerating cell / 受损、退化的细胞 | injury genes up, not just counts down / 损伤基因是否升高 |
| B · markers of two cell types / 两类细胞的标记基因 | doublet, ambient RNA / doublet、ambient | transitioning, repairing cell / 过渡、修复中的细胞 | genotype when donors are pooled (two-person doublets only) / 多人混测时看基因型（只能看出两个人的 doublet） |
| C · very many RNA molecules / RNA 特别多 | doublet | polyploid, binucleated cell / 多倍体、双核细胞 | genotype; cell type / 基因型；细胞类型 |
| D · stress genes up / 应激基因高 | dissociation stress / 解离应激 | injury, ischaemia / 损伤、缺血 | same tissue, cold vs warm digestion / 同一组织冷热消化对照 |
| E · one cell type splits by batch / 同类细胞按批次分团 | batch effect / 批次效应 | disease, if confounded with batch / 病（如果和批次混在一起） | same tissue, several assays or batches / 同一组织换测法或批次 |

<!-- ZH -->
看最后一列：**能真正分辨的，几乎都是实验设计给的信息**（基因型、换测法、冷热消化对照），而不是表达谱（expression profile）本身。这就是为什么[数据集](../datasets/index.md)页里专门有一组"测量对照"数据。
<!-- EN -->
Look at the last column: **what really tells them apart is almost always information from the experimental design** (genotypes, several assays, cold vs warm digestion), not the expression profile itself. That is why the [Datasets](../datasets/index.md) tab has a group of "measurement control" datasets.

## 第 4 步 · 这对质控意味着什么 / Step 4 · What this means for QC

<!-- ZH -->
大多数分析流程一上来就做**质控**，用模块 1 里那三列删掉可疑的行。对照上面的现象：

- `nFeature_RNA` 太低、`percent.mt` 太高 → 删掉（现象 A），**受损细胞也一起删了**；
- `nCount_RNA` 太高，或 doublet 工具打分高 → 删掉（现象 B、C），**多倍体和过渡态细胞也可能被删**；
- 用工具估计并减掉 ambient（现象 B）[4]。

阈值（threshold）没有统一标准，每个数据集、每种测法都不一样；常见建议是阈值尽量放宽，免得误删真实的细胞群 [1]。Lake 2023 自己对单核和单细胞数据就用了不同的阈值 [2]。
<!-- EN -->
Most analysis pipelines start with **quality control** (QC), using the three columns from module 1 to remove suspicious rows. Matched to the patterns above:

- `nFeature_RNA` too low or `percent.mt` too high → removed (pattern A), **and injured cells go with them**;
- `nCount_RNA` too high, or a high doublet-tool score → removed (patterns B and C), **and polyploid or transitioning cells may go too**;
- a tool estimates and subtracts the ambient counts (pattern B) [4].

There are no universal thresholds; they differ by dataset and assay, and a common recommendation is to keep them as permissive as possible so as not to remove real cell populations [1]. Lake 2023 itself used different thresholds for its single-nucleus and single-cell data [2].

<!-- ZH -->
!!! warning "对我们的问题，质控本身就是问题的一部分"
    常规流程把 QC 当成清洗，删掉就完事。但上面每一条过滤规则，都可能把我们最想找的病变细胞一起删掉。所以我们不能默认"QC 之后的数据就是干净的"：分清非疾病的变化和真实病变，正是我们要解决的问题（模块 8）。
<!-- EN -->
!!! warning "For our problem, QC is part of the question"
    Standard pipelines treat QC as cleaning: remove and move on. But every filtering rule above may also remove the diseased cells we most want to find. So we cannot assume that data after QC is clean: telling non-disease changes from real disease is exactly the problem we work on (module 8).

## 自测 / Self-check

<!-- ZH -->
??? question "1. 一个核同时有 PT 的 `LRP2` 和 TAL 的 `UMOD`，可能是哪几种情况？怎么判断？"
    测量伪影：双细胞或游离 RNA 污染。生物：真实的过渡态。只看表达很难分；如果样本是多人混测，基因型能认出两个人的 doublet，但认不出同一个人的 doublet。

??? question "2. 为什么在我们的问题里，不能直接用常规 QC 阈值过滤完再做异常检测（anomaly detection）？"
    受损、退化的细胞像低质量细胞（基因少、线粒体高；在 Lake 2023 里这甚至是判 altered 的依据之一），损伤后的多倍体细胞像 doublet。一刀切的阈值会把我们要找的病变细胞一起删掉。

??? question "3. 解离应激和组织损伤都会让 `FOS` 升高。什么样的数据能帮你分清？"
    只改处理方式、其他条件相同的对照实验，比如同窝小鼠的肾分别用 37 °C 和冰上消化（Denisenko 2020）。
<!-- EN -->
??? question "1. A nucleus has both PT's `LRP2` and TAL's `UMOD`. What could it be, and how would you tell?"
    Artifacts: a doublet or ambient RNA. Biology: a real transitioning cell. Expression alone can hardly tell; if donors were pooled, genotypes reveal two-person doublets, but not doublets of two cells from the same person.

??? question "2. Why can't we simply apply standard QC thresholds and then run anomaly detection?"
    Injured, degenerating cells look like low-quality cells (fewer genes, more mitochondrial RNA; in Lake 2023 this was even one of the criteria for calling a state altered), and polyploid cells after injury look like doublets. A hard threshold removes the diseased cells we want to find.

??? question "3. Both dissociation stress and tissue injury raise `FOS`. What data helps you tell them apart?"
    A controlled experiment that changes only the handling, for example kidneys from littermate mice digested at 37 °C and on ice (Denisenko 2020).

## 参考文献 / References

1. Luecken MD, Theis FJ. Current best practices in single-cell RNA-seq analysis: a tutorial. *Mol Syst Biol* 2019;15:e8746. [doi:10.15252/msb.20188746](https://doi.org/10.15252/msb.20188746) — section "Quality control" ("cytoplasmic mRNA has leaked out through a broken membrane, and thus, only mRNA located in the mitochondria is still conserved"; thresholds "as permissive as possible"). See also Ilicic T, et al. Classification of low quality cells from single-cell RNA-seq data. *Genome Biol* 2016;17:29, [doi:10.1186/s13059-016-0888-1](https://doi.org/10.1186/s13059-016-0888-1).
2. Lake BB, Menon R, Winfree S, et al. An atlas of healthy and injured cell states and niches in the human kidney. *Nature* 2023;619:585–594. [doi:10.1038/s41586-023-05769-3](https://doi.org/10.1038/s41586-023-05769-3) — Methods "Clustering snCv3" (altered-state criteria, quoted above); Methods "Quality control of sequencing data" (per-assay thresholds); Results ("common expression and regulatory signature across cell types associated with FOS/JUN signalling"; "in reference tissues in which they might arise from ischaemic stress during sample acquisition or normal ageing"). Deep-read: [Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md).
3. GEO GSE183277 (single-nucleus) and GSE183276 (single-cell) metadata tables of Lake 2023 ([GEO](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE183nnn/)) — median `percent.mt`, counted by us.
4. Young MD, Behjati S. SoupX removes ambient RNA contamination from droplet-based single-cell RNA sequencing data. *GigaScience* 2020;9:giaa151. [doi:10.1093/gigascience/giaa151](https://doi.org/10.1093/gigascience/giaa151) — abstract ("ubiquitous, with experiment-specific variations in composition and magnitude"); Results ("Estimate the ambient mRNA expression profile from empty droplets").
5. Kang HM, Subramaniam M, Targ S, et al. Multiplexed droplet single-cell RNA-sequencing using natural genetic variation. *Nat Biotechnol* 2018;36:89–94. [doi:10.1038/nbt.4042](https://doi.org/10.1038/nbt.4042) — Results ("the probability that a doublet contains cells from different individuals is very high (1 – 1/N…)").
6. Hoeft K, Bleckwehl T, Schumacher D, et al. Label-free single-cell RNA multiplexing leveraging genetic variability. *Nat Commun* 2024;15:10612. [doi:10.1038/s41467-024-54270-6](https://doi.org/10.1038/s41467-024-54270-6) (CC BY 4.0) — Fig. 2 i–j and legend ("i Conceptual cartoon showing UMAP representations of kidney nuclei…"). Deep-read: [Hoeft 2024](../papers/hoeft-genotype-multiplexing-natcommun-2024/index.md); data facts: [Hoeft 2024 dataset page](../datasets/hoeft-2024.md).
7. Lazzeri E, Angelotti ML, Peired A, et al. Endocycle-related tubular cell hypertrophy and progenitor proliferation recover renal function after acute kidney injury. *Nat Commun* 2018;9:1344. [doi:10.1038/s41467-018-03753-4](https://doi.org/10.1038/s41467-018-03753-4) — Results (polyploid ≥4C tubular cells after IRI in mice; "Endocycle is detected in kidneys of patients with CKD after AKI").
8. Liapis H, Romagnani P, Anders HJ. New insights into the pathology of podocyte loss: mitotic catastrophe. *Am J Pathol* 2013;183:1364–1374. [doi:10.1016/j.ajpath.2013.06.033](https://doi.org/10.1016/j.ajpath.2013.06.033) — Table 1 (mitotic catastrophe: "Binucleation, micronuclei" in human glomerular disease).
9. Denisenko E, Guo BB, Jones M, et al. Systematic assessment of tissue dissociation and storage biases in single-cell and single-nucleus RNA-seq workflows. *Genome Biol* 2020;21:130. [doi:10.1186/s13059-020-02048-6](https://doi.org/10.1186/s13059-020-02048-6) — mouse kidney, littermates; Results ("immediate-early genes Fosb, Fos, Jun, Junb, Atf3, and Egr1 and heat shock proteins Hspa1a and Hspa1b"; "only three podocytes were detected in warm-dissociated samples… compared to 330… in the cold-dissociated samples"). Deep-read: [Denisenko 2020](../papers/denisenko-dissociation-bias-genomebiol-2020/index.md).
10. Lake BB, Chen S, Hoshi M, et al. A single-nucleus RNA-sequencing pipeline to decipher the molecular anatomy and pathophysiology of human kidneys. *Nat Commun* 2019;10:2832. [doi:10.1038/s41467-019-10861-2](https://doi.org/10.1038/s41467-019-10861-2) — Results (mitochondrial transcripts "not expressed in nuclei"; "fewest MTs and stress-induced artifacts in cryoR samples compared to… fresh dissociated samples"; MT enrichment in TAL and S3 PT "consistent with the nephrectomy procedure-related warm ischemia"). Deep-read: [Lake 2019](../papers/lake-snrna-pipeline-natcommun-2019/index.md).
11. Acera-Mateos M, et al. *Genome Biol* 2026;27:64. [doi:10.1186/s13059-026-04002-4](https://doi.org/10.1186/s13059-026-04002-4) — Results (variance explained by cell type, donor and assay; 3′ scRNA-seq vs snRNA-seq, 5 donors). Deep-read: [mBDRC 2026](../papers/kidney-multimodal-genomebiol-2026/index.md); design and numbers: [mBDRC 2026 dataset page](../datasets/mbdrc-2026.md).

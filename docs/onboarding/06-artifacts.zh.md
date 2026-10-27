# 6 · 伪影，以及长得像伪影的生物状态

> ⏱ 约 1 小时 · 第 1 天 · 读懂

!!! abstract "读完能回答"
    - doublet、ambient、低质量细胞、解离应激分别是怎么来的？
    - 它们在数据里长什么样，为什么会被当成病？
    - 哪些真实的生物状态反过来会被当成伪影？

这一模块只回答一个问题：**X 里一行看起来不正常，是病造成的，还是别的原因？**

"别的原因"分三类，后面会逐个讲：

- **测量伪影**（artifact）：细胞本身没事，是测量过程让这一行不能代表这个细胞。
- **处理诱发的变化**：细胞真的变了，但起因是实验室里的处理，不是病。
- **批次效应**（batch effect）：不是某一行的问题，而是整批数据一起偏移。

难点在于它们和真实的病变在数据里经常长得一样。所以我们分三步走：

1. **非疾病的变化从哪来**：数据的生成过程默认了什么，每种变化打破了哪一条；
2. **按看到的现象排查**：每种现象都同时列出非疾病的解释和生物的解释，以及靠什么分辨；
3. **这对质控意味着什么**：常规的过滤步骤会删掉什么。

## 第 1 步 · 非疾病的变化从哪来

数据是这样产生的（模块 5 详细讲）：组织被消化成单个细胞（或提取出细胞核），仪器把它们一个个包进小油滴，每个油滴一个 **barcode**，最后 **一个 barcode = X 的一行**。

这一套默认了几件事：**油滴里正好一个细胞、这个细胞是完好的、读到的 RNA 只来自它自己、处理过程不改变细胞、每批数据的测量方式一样**。下表按三类列出每种变化打破了哪一条：

| 类别 | 变化 | 被打破的假设 | 发生了什么 |
|---|---|---|---|
| 测量伪影 | 空液滴 | 正好一个细胞 | 没装细胞，只有漂在液体里的 RNA |
| 测量伪影 | 双细胞 | 正好一个细胞 | 两个细胞进了同一个油滴 |
| 测量伪影 | 低质量细胞 | 细胞完好 | 细胞破了，漏掉一部分 RNA |
| 测量伪影 | 游离 RNA 污染 | RNA 只来自它自己 | 破细胞释放的 RNA 形成一锅"汤"，每个油滴都舀进一点 |
| 处理诱发 | 解离应激 | 处理不改变细胞 | 37 °C 消化时细胞真的打开了应激基因 |
| 批次 | 批次效应 | 每批测法一样 | 换日期、试剂批号或测法，整批数据一起偏移 |

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

## 第 2 步 · 按看到的现象排查

实际分析时，你先看到的是一行数据的**现象**，不知道原因。下面按现象排，每种都有两个解释：非疾病的，和生物（病变）的。

### 现象 A · 基因少、线粒体比例高

- **非疾病的解释**：低质量细胞（low-quality cell）或空液滴（empty droplet）。完整细胞的膜破了，胞质里的 RNA 漏掉，`nCount_RNA`、`nFeature_RNA` 都低；留下来的多是线粒体里的 RNA，`percent.mt` 偏高 [1]。细胞核不一样：线粒体 RNA 不在核里表达（模块 2），单核数据里测到的线粒体转录本，Lake 2019 认为来自贴在核膜上的线粒体，其多少也反映组织处理的质量 [10]。所以单核数据的 `percent.mt` 本来就低得多（Lake 2023 单核中位 0.81%，单细胞中位 23% [3]）。Lake 2019 还发现，TAL 和 PT 的 S3 段这类耗能高、容易缺血的细胞线粒体转录本更多，和肾切除时的热缺血一致 [10]。
- **生物的解释**：受损、退化的细胞也可能这样。Lake 2023 单核数据里，degenerative 状态的核确实基因更少、线粒体更高（见 [Lake 2023 数据页](../datasets/lake-2023.md)的"已知问题"）。但这不能当独立证据：Lake 2023 当初就是把"测到的基因少、线粒体转录本多、内质网相关转录本多、损伤标记基因升高、或者主要来自 AKI / CKD 样本"的簇先标成可能的改变态 [2]。也就是说，"基因少、线粒体高"有一部分是标签定义带进来的。
- **怎么分辨**：只看总数分不开。要看损伤相关的基因有没有升高，而不只是"什么都变少了"。

### 现象 B · 一行里有两类细胞的标记基因

比如一个核同时有 PT 的 `LRP2` 和 TAL 的 `UMOD`。

- **非疾病的解释**：双细胞（doublet，PT 和 TAL 两个核进了同一个油滴），或游离 RNA 污染（ambient RNA，TAL 核从"汤"里沾上了 PT 的 RNA）。汤的成分因实验而异，可以从空液滴里估计出来 [4]。在一项小鼠肾的研究里，冻存组织做的单核数据比新鲜组织做的单细胞数据污染重得多，见 [Janssen 2023](../datasets/janssen-2023.md)；那里单核和冻存是绑在一起的，所以不能直接推广成"单核一定更脏"。
- **生物的解释**：真实的过渡态或修复中的细胞，本来就同时表达两种状态的基因。
- **怎么分辨**：只看表达很难。**基因型**能给出一部分答案：几个人的样本混在一起测时，一个油滴里出现两个人的 DNA 差异（SNP），就肯定是 doublet [5]。但同一个人的两个细胞进了同一个油滴，基因型看不出来：混 N 个人时，能看出来的 doublet 约占 1 − 1/N [5]，4 个人等量混合时约有四分之一看不出来。所以基因型给的是 doublet 的下限，不是全部。

Hoeft 2024 就这样做过：4 个病人的核混在一起测，再按 SNP 分出每个核来自谁 [6]。下图右半是结果：按表达被聚成"Mixed/Doublets"的簇里，大部分核按 SNP 只来自一个人，基因型判出的 doublet（深灰色）很少。同一个人的 doublet 基因型看不出来，所以这不能证明那个簇里没有 doublet；但它说明很多被表达判成"混合"的核其实不是两个人的混合。我们的理解：只看表达判断伪影，很容易判错。具体数字见 [Hoeft 2024 数据页](../datasets/hoeft-2024.md)。

![Hoeft 2024 Fig. 2 i–j: expression clusters vs genotype-based donor assignment / 表达聚类和按基因型分人的对照](img/hoeft2024_fig2ij.jpg)

图：Hoeft 2024 Fig. 2 i–j（肾部分，已截取）[6]。左：示意图，混合肾样本的 UMAP 分别按表达聚类和三种按 SNP 分人的方法上色；右：每个簇里各病人、doublet（深灰）和未分配核（浅灰）的比例，看最左边 SoupLadle 那一组即可。Hoeft K et al., Nat Commun 2024，CC BY 4.0。

### 现象 C · RNA 特别多

- **非疾病的解释**：doublet，两个细胞的 RNA 加在一起。
- **生物的解释**：多倍体（polyploidy）或多核细胞。急性损伤后，一些小管细胞复制 DNA 却不分裂，变成多倍体（小鼠实验，也在 AKI 后 CKD 病人的活检里看到）[7]；病变肾小球里的足细胞会出现双核 [8]。DNA 多了，RNA 也可能更多。我们的理解：双核这一条主要影响单细胞数据；单核数据里两个核一般会被分开测。
- **怎么分辨**：同样靠基因型（只能看出两个人的 doublet）；再看细胞类型，这种细胞主要出现在损伤后的小管和足细胞里。

### 现象 D · 应激基因高

- **非疾病的解释**：解离应激（dissociation stress）。37 °C 消化时细胞打开 `Fos`、`Jun`、热休克蛋白这类基因；脆弱的细胞（比如足细胞）还会在消化中大量丢失（小鼠肾）[9]。
- **生物的解释**：组织损伤，或取材时的缺血（模块 4），也可能打开同一类基因。Lake 2023 的 degenerative 状态有共同的 FOS/JUN 信号特征；健康人身上也有不少 altered 细胞，作者认为可能来自取样时的缺血应激或正常衰老 [2]。
- **怎么分辨**：靠只改处理方式的对照实验。同窝小鼠的肾，冰上冷消化时应激基因低得多 [9]，见 [Denisenko 2020](../datasets/denisenko-2020.md)；人肾上也看到过类似的应激信号 [10]，见 [Lake 2019](../datasets/lake-2019.md)。

### 现象 E · 同一类细胞按批次分成几团

- **非疾病的解释**：批次效应（batch effect）。不同 `library`、不同测法各自偏移。
- **生物的解释**：如果病人和健康人恰好分批测，"批次"和"病"混在一起，分不清哪个是哪个。
- **怎么分辨**：靠实验设计，同一个人的组织换测法或分批测。[mBDRC 2026](../datasets/mbdrc-2026.md) 用不同测法测了同一批健康供者的组织（不是每个人都测了所有测法）：比较单细胞和单核 RNA 时，测法解释的表达差异比供者之间的差异大得多 [11]。

## 第 3 步 · 汇总

| 现象 | 非疾病的解释 | 生物的解释 | 靠什么分辨 |
|---|---|---|---|
| 基因少、线粒体高 | 低质量细胞、空液滴 | 受损、退化的细胞 | 损伤基因是否升高 |
| 两类细胞的标记基因 | doublet, ambient RNA / doublet、ambient | 过渡、修复中的细胞 | 多人混测时看基因型（只能看出两个人的 doublet） |
| RNA 特别多 | doublet | 多倍体、双核细胞 | 基因型；细胞类型 |
| 应激基因高 | 解离应激 | 损伤、缺血 | 同一组织冷热消化对照 |
| 同类细胞按批次分团 | 批次效应 | 病（如果和批次混在一起） | 同一组织换测法或批次 |

看最后一列：**能真正分辨的，几乎都是实验设计给的信息**（基因型、换测法、冷热消化对照），而不是表达谱本身。这就是为什么[数据集](../datasets/index.md)页里专门有一组"测量对照"数据。

## 第 4 步 · 这对质控意味着什么

大多数分析流程一上来就做**质控**（QC），用模块 1 里那三列删掉可疑的行。对照上面的现象：

- `nFeature_RNA` 太低、`percent.mt` 太高 → 删掉（现象 A），**受损细胞也一起删了**；
- `nCount_RNA` 太高，或 doublet 工具打分高 → 删掉（现象 B、C），**多倍体和过渡态细胞也可能被删**；
- 用工具估计并减掉 ambient（现象 B）[4]。

阈值没有统一标准，每个数据集、每种测法都不一样；常见建议是阈值尽量放宽，免得误删真实的细胞群 [1]。Lake 2023 自己对单核和单细胞数据就用了不同的阈值 [2]。

!!! warning "对我们的问题，质控本身就是问题的一部分"
    常规流程把 QC 当成清洗，删掉就完事。但上面每一条过滤规则，都可能把我们最想找的病变细胞一起删掉。所以我们不能默认"QC 之后的数据就是干净的"：分清非疾病的变化和真实病变，正是我们要解决的问题（模块 8）。

## 自测

??? question "1. 一个核同时有 PT 的 `LRP2` 和 TAL 的 `UMOD`，可能是哪几种情况？怎么判断？"
    测量伪影：双细胞（doublet）或游离 RNA 污染（ambient RNA）。生物：真实的过渡态。只看表达很难分；如果样本是多人混测，基因型能认出两个人的 doublet，但认不出同一个人的 doublet。

??? question "2. 为什么在我们的问题里，不能直接用常规 QC 阈值过滤完再做异常检测？"
    受损、退化的细胞像低质量细胞（基因少、线粒体高；在 Lake 2023 里这甚至是判 altered 的依据之一），损伤后的多倍体细胞像 doublet。一刀切的阈值会把我们要找的病变细胞一起删掉。

??? question "3. 解离应激和组织损伤都会让 `FOS` 升高。什么样的数据能帮你分清？"
    只改处理方式、其他条件相同的对照实验，比如同窝小鼠的肾分别用 37 °C 和冰上消化（Denisenko 2020）。

## 参考文献

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

## 本模块名词

| 中文 | English | 一句话 |
|---|---|---|
| [伪影（技术伪影）](glossary.md#technical-artifact) | Artifact (technical artifact) | 数据里不来自细胞在体内真实状态的变化，比如空液滴、doublet、低质量细胞、ambient RNA；广义上也包括解离应激这类由处理诱发的变化。 |
| [空液滴](glossary.md#empty-droplet) | Empty droplet | 没装细胞的油滴；里面只有漂在液体里的 RNA，所以正好是 ambient 的样本。raw 矩阵里有，filtered 矩阵里被去掉。 |
| [双细胞假象(doublet)](glossary.md#doublet) | Doublet | 两个细胞或细胞核被同一条形码捕获、当作一个细胞分析的技术假象,产生嵌合表达谱,可能被误认为一种新的细胞状态。 |
| [低质量细胞](glossary.md#low-quality-cell) | Low-quality cell | 快死或破损的细胞：RNA 分子和基因数少、线粒体比例高；通常按 QC 阈值过滤掉，但受损细胞也可能长得很像。 |
| [游离 RNA 污染(ambient RNA)](glossary.md#ambient-rna) | Ambient RNA | 破裂细胞释放的游离转录本被计入其他液滴,形成背景信号,使本不相关的细胞看起来彼此相似。 |
| [解离应激](glossary.md#dissociation-stress) | Dissociation stress | 组织在 37 °C 消化时细胞启动的应激基因（FOS、JUN、热休克蛋白等）；让细胞看起来受了伤，其实伤是在实验室里造成的。 |
| [批次效应](glossary.md#batch-effect) | Batch effect | 不同机构、时间或平台采集的数据集之间的系统性非生物学差异,若不校正会混淆分析。 |
| [混杂因素](glossary.md#confounder) | Confounder (confounding) | 和标签一起变化的因素，模型分不清自己学到的是哪个；比如病人和健康人分批测，批次就和'病'混在了一起。 |
| [技术性丢失(假零)](glossary.md#technical-dropout) | Technical dropout (false zero) | 计数矩阵中因捕获失败而非真的不表达所产生的零;由于真零与假零无法区分,稀疏性同时既是生物学也是噪声。 |
| [线粒体比例](glossary.md#mitochondrial-fraction) | Mitochondrial fraction (percent.mt) | 一个细胞的 RNA 里来自线粒体基因的比例；标准 QC 指标。完整细胞里偏高，提示细胞破损或快死了；细胞核本身不表达线粒体转录本，所以数值本来就低得多，偏高反映的是粘在核上的线粒体或组织处理的影响。 |
| [质控（QC）](glossary.md#quality-control) | Quality control (QC) | 大多数单细胞分析的第一步：删掉基因太少、线粒体比例太高或 RNA 分子太多的行，并减掉 ambient 计数；阈值因数据而异，也可能把受损细胞一起删掉。 |
| [多倍体 / 多核](glossary.md#polyploidy) | Polyploidy / multinucleation | DNA 拷贝多出来或有不止一个核的细胞；损伤后一些小管细胞会变成多倍体，一些足细胞会变成双核。在单细胞数据里，这类细胞可能看起来像 doublet。 |

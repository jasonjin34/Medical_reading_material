# Benchmarking computational decontamination of ambient RNA

> **文献键** `Cargnelli_2026` · **来源** bioRxiv(2026) · **类别** single-cell · **相关度** medium · **获取** open
> **链接** <https://doi.org/10.64898/2026.01.13.699237> · `status: complete`

---

## 一句话
一个独立基准,用模拟数据、三种复杂度的物种混合实验、小鼠肾脏品系(基因型)混合实验和无污染负对照,评测 7 种 ambient RNA 去污染方法(CellBender、DecontX、FastCAR、scAR、scCDC、SoupX、CellClear)「去掉多少外源 RNA、保留多少内源 RNA、对下游解读有何影响」;结论是没有通吃的方法,推荐 CellBender、DecontX(full 模式)或 SoupX(reduced 模式),并警告在无污染数据上默认去污染会过度校正。

## 研究问题
单细胞/单核 RNA-seq(sxRNA-seq)中的 ambient RNA —— 解离、剪切或去垢剂导致细胞裂解释放的 RNA,以及多路复用中的条形码交换、孔间交叉污染、试剂污染 —— 会扭曲细胞分类与基因层面推断。已有多种去污染方法,却没有覆盖所有方法、多个数据集的独立基准;而 nf-core 等标准流程已把去污染作为常规步骤,**降低了「未经数据特异评估就做概率背景校正」的门槛**,增加过度校正风险。

## 方法
**Ground truth 构造**:物种混合实验中,次要物种基因的 UMI 记为 ambient、主要物种的为内源(只保留 ≥75% UMI 来自单一物种的细胞);小鼠品系混合中按基因型特异 SNP(≥2 计数)判定;模拟数据由三种细胞系拟合的负二项分布生成,按设定的 ambient 比例从其他细胞类型分布中抽样污染 UMI;负对照为 Smart-seq2 胰岛数据与无污染模拟数据。**两项核心分数**:ambient 去除分数(ARS)与内源保留分数(ERS),均在 0–1 之间。**下游评测**:细胞邻域质量(Milo 邻域纯度、LISI)、标志基因选择性(熵、Moran's I、Gini)、Harmony 批次整合(bASW、batch LISI、PCR、ARI)、Azimuth 标签迁移(高置信比例、ARI、cASW、RMSE)。所有方法默认参数;SoupX/DecontX 另测只用过滤矩阵的 reduced 模式;scAR full 模式因计算量过大未完成。

## 数据
7 个数据集、66 个样本、135,314 个细胞:低复杂度物种混合(10x 人 293T + 鼠 3T3)、中复杂度(人胰岛 + 人 Jurkat + 鼠 32D 掺入,GSE147203)、高复杂度(人胰岛异种移植到小鼠肾),**小鼠肾脏三品系混合**(C57BL/6、129S1/SvImJ、CAST/EiJ,GSE218853),Smart-seq2 胰岛负对照(E-MTAB-5061),以及模拟数据。全部为公开数据。

## 主要结果
- **ambient RNA 普遍存在**:49 个真实样本、97,357 个细胞/核中,81.56% 含有一定 ambient RNA;**单核样本平均 10.59%,单细胞 5.21%**;细胞间、样本间、研究间差异都很大(平均 QCD 0.314 / 0.319 / 0.171)。
- **来源**:基因的 ambient 负荷与其在空液滴中的表达高度相关(平均 R = 0.857);表达最频繁的 10% 基因贡献平均 82.30% 的 ambient RNA —— 主要是普遍表达的成熟胞质 mRNA。常用 QC 指标(外显子比例、线粒体/核糖体比例)与单细胞 ambient 负荷关联很弱;即使在 UMI 最多的 10% 细胞中,也有 2.64% 受到严重影响(>10% UMI 为 ambient)—— **靠严格 QC 无法根除**。
- **去除 vs 保留**:去除 ambient 最多的是 scAR(平均 ARS 0.679)与 CellBender(0.604),但 **scAR 同时去掉约 0.445 的内源信号**(主要是低表达基因);各方法在无污染负对照上去掉的内源信号与有污染数据相当。SoupX reduced 模式去除更多而保留相近;DecontX reduced 模式去除略少但保留更多。
- **下游解读**:在最高污染的模拟样本中,只有 CellBender 改善无监督聚类恢复真实细胞类型;DecontX 与 scAR 使标志基因模块评分接近真值(但在无污染数据上也「改善」,提示偏向细胞类型特异表达);CellBender、scAR、SoupX、DecontX 改善邻域质量且对负对照影响可忽略;**scAR 恶化批次整合,并显著影响负对照的整合和标签迁移**。scCDC 与 FastCAR 主要从高表达基因去除,未见下游收益;CellClear 去除的内源计数与 ambient 计数相当。
- **推荐**:算力充足 → CellBender(需 GPU、耗时长、内存高,且自带细胞调用);需扩展性或特定细胞调用 → DecontX full 模式;无污染先验或只有过滤矩阵 → SoupX reduced 模式(在无污染时最不易过度校正)。污染先验可来自实验(snRNA 通常污染更多)或计算工具(如 AmbiQuant)。

## 创新点
- 首个覆盖 7 种方法、多种 ground-truth 设计的独立基准,且显式包含**无污染负对照**以测量过度校正。
- 把「去除」与「保留」拆成两个分数(ARS/ERS),并揭示方法对高/低表达基因的系统性偏向。
- 给出可执行的选择决策(算力、可用矩阵、污染先验)。

## 局限
- 所有方法默认参数,未做参数调优;scAR full 模式未跑完。
- 负对照只有 3 个 Smart-seq2 样本(其余未能跑通全部方法)。
- 物种/品系混合的 ground truth 只能观察跨物种/跨基因型的污染,同物种同基因型内的污染不可见;模拟只用三种细胞系。
- 预印本,未经同行评审;摘要版本间对推荐方法的表述不一致(见页首);代码仓库在文中写为「将会」开放。

## 与本研究方向的关系
对 **伪影注入课题**:肾活检组学常用 **snRNA**(单核),本文显示单核数据的 ambient 污染约为单细胞的两倍(10.59% vs 5.21%),而且污染主要来自表达最普遍的 mRNA —— 在肾脏中这通常意味着丰富的小管细胞转录本会「渗进」所有细胞类型。这会直接制造假异常(例如免疫细胞或足细胞「表达」PT 标志),因此 ambient RNA 应作为 KidneyAnomalyBench 中「技术伪影」类的一个明确来源。可用的设计:**(1)** 本文的 ARS/ERS + 负对照框架可直接改造成「去伪影后异常是否稳定、在干净数据上是否引入假异常」的评测;**(2)** 本文的小鼠肾脏品系混合数据(GSE218853)提供了**肾脏中 ambient RNA 的真实 ground truth**,可用来标定异常检测器对 ambient 伪影的敏感度;**(3)** 跨模态一致性 —— 配对的 snATAC 不受同一 RNA 释放机制影响,若一个「异常」只在 snRNA 中出现而在同一核的 ATAC 中无对应可及性,可提示其为 ambient 伪影(这一推论是本方向的假设,本文未测 ATAC)。**过度校正同样危险**:本文显示部分方法会人为增强细胞类型特异性,这可能把真正的混合/过渡状态(如损伤 PT)「清理」掉。对 **Agent 可信度课题**:「流程里默认开启去污染、未检查是否有污染」是一个非常具体的 agent 失败模式;本文的决策规则(先判断污染先验、按可用矩阵选方法)可以直接写成验证器的检查项。

## 可复用资产
- **代码:** 基准代码仓库(文中称将开放,含全部脚本与数据集列表)。
<https://github.com/madsen-lab/AmbientRemovalBenchmark>
- **数据:** 小鼠肾脏品系混合(GSE218853)—— 肾脏 ambient RNA 的 ground truth;物种混合 GSE147203;负对照 E-MTAB-5061。
<https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE218853>
- **评测协议:** ARS/ERS 双分数 + 负对照 + 四类下游任务。

## 待读
- CellBender、DecontX、SoupX 原文;AmbiQuant(样本级污染估计)。
- GSE218853 的原始研究(小鼠肾品系混合)及其如何定义 ambient ground truth。
- 与空间转录组中的溢出/扩散校正(`resolvi-natmethods-2026`、`xenium-split-natmethods-2026`)对照:同为「信号来自错误的细胞」,但机制不同。

## 引用
```bibtex
@article{Cargnelli_2026, title={Benchmarking computational decontamination of ambient RNA}, url={http://dx.doi.org/10.64898/2026.01.13.699237}, DOI={10.64898/2026.01.13.699237}, journal={bioRxiv}, publisher={openRxiv}, author={Cargnelli, Cecilie Bøgh and Nielsen, Jakob Vennike and Skat Madsen, Jesper Grud}, year={2026}, month=Jan }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

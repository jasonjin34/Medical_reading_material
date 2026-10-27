# Analysis of individual patient pathway coordination in a cross-species single-cell kidney atlas

> **文献键** `Klotzer_2025` · **来源** Nature Genetics(2025) · **类别** single-cell · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1038/s41588-025-02285-0> · `status: complete`

---

## 一句话
两件事:(1) **SISKA 1.0** —— 人、小鼠、大鼠 > 100 万细胞、> 140 个样本的跨物种单细胞(snRNA)肾脏图谱,21 个主要细胞类型、近 80 个跨物种保守的细胞状态;(2) **CellSpectra** —— 一个**单样本**统计工具:对每个细胞类型 × 通路,用参照样本伪 bulk 矩阵的 SVD 第一主轴作为"协调模式",把待测样本回归上去,R² 降低 + χ² 检验即判为该样本该通路"协调性丢失";据此生成**患者级单细胞功能画像报告**、为患者选择最匹配的啮齿类模型,并在叶酸肾损伤模型中由 CellSpectra 提名的 TNF 通路用 etanercept 干预改善了肾功能。

## 研究问题
单细胞数据要进入临床,需要能在**单个患者**层面找出细胞类型特异、可干预的分子改变,并知道哪个动物模型最像这个患者。现有通路分析多基于单基因均值/方差变化再汇总(如 GSEA),受单细胞稀疏性、技术变异和单样本统计困难所限;而动物模型与患者的对应关系缺乏量化。

## 方法
**SISKA 整合**:基于约 12k 一对一直系同源基因,用 scVI 整合人(H-CKD、DKD、AKI、健康)、小鼠(AKI 时间序列、DKD、叶酸)与大鼠(ZSF1 糖尿病、DOCA 高血压)snRNA-seq;MetaMarker 找跨物种保守 marker,MetaNeighbor 做相关性独立验证;以"至少在两个物种中出现"来决定细胞状态分辨率。**CellSpectra**:对给定细胞类型与基因集,构建样本 × 基因的伪 bulk 矩阵(每样本该类型 ≥ 10 个细胞,归一化 + log);在参照组上做 SVD,第一个基因载荷向量 v* 视为"eigensample";把每个查询样本回归到 v* 得 R²;参照分布用**留一法**得到(避免 double-dipping);显著性用参数化检验 —— 假设残差 ε_sg ~ N(0, σ_g²),σ_g 由参照残差估计,查询样本的标准化残差平方和服从自由度 G−1 的 χ²,每个基因贡献上限 CHISQ.MAX = 4 以抗离群;FDR 校正。**On-the-fly 参照**:为每个查询样本按其总 counts 对参照细胞下采样(3 个伪重复),消除细胞数/捕获率造成的假阳性。**驱动基因**:按标准化残差排序(report_genes())。**质量报告**:LOO R² 均值/中位数/标准差与 v* 解释方差。

## 数据
SISKA:> 100 万细胞、> 140 个样本、三物种;扩展人图谱:150 个健康与疾病样本、> 70 万细胞(含 Penn 肾内科活检与 KPMP 数据),用 scANVI 转移标签;功能画像比较 > 100 个患者样本与 47 个健康参照。公开数据:KPMP、GSE211785、GSE209821(ZSF1 大鼠)、GSE183839(DOCA 大鼠)、GSE184652(DKD 小鼠)、GSE139107(小鼠 AKI 时间序列)、新数据 GSE291551;NSCLC 图谱(CELLxGENE)。

## 主要结果
- **图谱**:21 个主要细胞类型,> 900 个跨物种保守 marker(852 个仅属于单一细胞类型),近 80 个跨物种保守细胞状态;人肾 PTS3 细胞明显更少。
- **协调性**:多数功能基因集中 v* 解释方差 > 75%;"Regulation of glomerular filtration" 在啮齿类足细胞上与人高度一致(R² 高),其他细胞类型则低;PEC 中 "Regulation of protein kinase C signaling" 大鼠比小鼠更像人;**没有一个啮齿类模型在所有功能上都最优**。
- **单样本检测**:小鼠 AKI 时间序列中 PT "Response to ischemia" 在再灌注后 4 h 与 12 h 协调性显著下降,后期与糖尿病小鼠无变化;更重的 db/db + AAV-Renin 模型受影响通路数多于 db/db。
- **治疗效应**:糖尿病大鼠足细胞的协调性改变几乎被 sGC 激活剂完全逆转,sGC 刺激剂则不能(与原研究的表型结果一致);足细胞 "SMAD protein signal transduction" 仅被激活剂恢复。
- **实验验证**:叶酸模型中显著改变的基因集数量与 PT 组织学损伤一致;CellSpectra 在多数样本检出 mTOR 与 TNF 信号改变,而 GSEA 几乎检不出;**etanercept(TNF 抑制剂)显著降低叶酸损伤小鼠的 BUN**(每组 n = 5)。作者强调 CellSpectra 本身不给出变化方向。
- **患者画像**:PT "Vasculature Development" 在 > 70% 疾病样本中改变;高血压患者 DCT_CNT_CD "Sodium Ion Transport" 协调性改变(SCN3A、SLC23A2、SLC24A1、SCNN1B;NEDD4L),非高血压者无;ADPKD 中 TNF 与 mTOR 改变最常见,"Water Transport" 与 CFTR/水通道蛋白改变相符(与 tolvaptan 疗效一致);肺癌中恶性细胞协调性改变远多于非恶性上皮,LUSC 多于 LUAD。

## 创新点
- **单样本、带统计置信度**的通路级偏离检验:不是"上调/富集",而是"基因间相对表达模式是否偏离参照"。
- 用跨物种保守性来决定细胞状态分辨率,并用协调性 R² 量化动物模型与患者的功能相似度。
- On-the-fly 参照下采样控制细胞数/捕获深度这一技术混杂;每次查询自带质量报告。
- 从计算提名到动物干预(etanercept)闭环验证。

## 局限
- 线性假设(SVD + 回归),可能漏掉非线性关系;多层计算有过拟合风险(作者自述)。
- 只检测"协调性丢失",**不给方向**;依赖 GO/KEGG 等并非为协调性设计的基因集;稀有细胞类型受稀疏性影响。
- 跨物种只用约 12k 直系同源基因;人类预测大多尚无干预验证;缺少用药等临床元数据,参照尚未按年龄/性别匹配。
- 一个 sample × 通路 × 细胞类型的检验在成千上万组合上进行,多重检验与依赖结构使"显著通路数"作为严重度指标需谨慎。

## 与本研究方向的关系
CellSpectra 本质上是一个**单样本、细胞类型 × 通路粒度的异常检测器**:参照 = 健康样本的协调模式,异常 = 查询样本相对参照的标准化残差(χ² 检验),再加上驱动基因解释 —— 这几乎就是 **课题 1** 想要的"可解释、带置信度的患者级异常报告"在单细胞层面的现成版本。可直接借用:(1) **作为课题 1 的强基线**:在待测肾样本(或 KPMP / Lake 2023 疾病样本)的 snRNA 上跑 CellSpectra(以 KPMP/Lake 健康样本为参照),我们的方法应在专家验证的异常上优于它,或至少提供它没有的空间/跨模态维度;(2) **on-the-fly 参照下采样**直接回应"细胞数/捕获率差异造成假异常"这一技术伪影 —— 应纳入 KidneyAnomalyBench 的必测混杂;(3) 它的 χ² 单样本检验 + 质量报告,是"校准的异常分数"的一个可比较实现;(4) **跨模态扩展**是我们的增量:CellSpectra 只看 snRNA,而同一患者的其他模态(如染色质可及性或空间组学)若一致偏离,才更可能是疾病而非伪影。对 **detect → model → revert**,它完整走了一遍:检测协调性丢失(detect)→ 跨物种选择匹配模型(model)→ 在模型中用 etanercept 阻断 TNF 并改善 BUN(revert 的湿实验验证);sGC 激活剂"逆转"足细胞协调性则示范了**用协调性恢复作为 revert 读数**。对 **课题 2**:Functional Profiling Report 是 agent 很可能被要求生成/解释的产物;它自陈"不给方向",正是 claim-to-evidence verifier 需要拦截的一类过度声明(例如 agent 把"协调性改变"说成"通路激活")。

## 可复用资产
- **代码:** CellSpectra R 包与教程;SISKA 整合与复现代码。
<https://github.com/kloetzerka/CellSpectra> · <https://github.com/susztaklab/SISKA>
- **数据:** 5 个单细胞图谱(SISKA、人扩展、人/鼠/大鼠单物种)与未发表人活检 snRNA 均存于 Zenodo(见论文 ref. 97);GEO:GSE211785、GSE209821、GSE183839、GSE184652、GSE139107、GSE291551。
- **网页工具:** 跨物种基因表达与 R² 分布浏览。
<http://www.susztaklab.com>

## 待读
- Dumoulin 2026 DKD 空间图谱(同组),考虑把 CellSpectra 推广到 niche/microenvironment 层面的协调性。
- 与 Padvitski 2026 的连续损伤分数(PDS)比较:监督式损伤方向 vs 无方向的协调性偏离。
- MetaNeighbor / MetaMarker 原文;单样本通路方法(如 singscore、GSVA)的对照。

## 引用
```bibtex
@article{Klotzer_2025, title={Analysis of individual patient pathway coordination in a cross-species single-cell kidney atlas}, volume={57}, ISSN={1546-1718}, url={http://dx.doi.org/10.1038/s41588-025-02285-0}, DOI={10.1038/s41588-025-02285-0}, number={8}, journal={Nature Genetics}, publisher={Springer Science and Business Media LLC}, author={Klötzer, Konstantin A. and Abedini, Amin and Li, Shen and Balzer, Michael S. and Liang, Xiujie and Levinsohn, Jonathan and Ha, Eunji and Dumoulin, Bernhard and Hogan, Jonathan J. and Quinn, Ghazal and Bloom, Roy D. and Schuller, Max and Eller, Kathrin and Halmos, Balazs and Zhang, Nancy R. and Susztak, Katalin}, year={2025}, month=Aug, pages={1922–1934} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

# Virtual Cell Challenge

> **文献键** `virtual-cell-challenge` · **来源** Arc Institute (competition; companion paper in Cell)(2025) · **类别** competition · **相关度** medium · **获取** open
> **链接** <https://virtualcellchallenge.org/> · `status: complete`

---

## 一句话
Arc Institute 主办的年度公开竞赛,要求参赛模型预测单基因 CRISPR 扰动在一个"留出细胞类型"(H1 人胚胎干细胞)中引起的单细胞基因表达变化,并用统一的三指标标准化评测——本质是"virtual cell 的图灵测试"。

## 研究问题
扰动响应预测(perturbation response prediction)领域缺乏严格、公开、可比的评测标准,导致"AI virtual cell"模型的真实进展难以判断。挑战聚焦最难的现实任务——**context generalization**:能否把在其它细胞/扰动上学到的规律,泛化到一个全新的细胞语境和未见过的扰动基因上。核心科学动机是:若能准确模拟扰动→表达的映射,就能 in silico 筛选把病态细胞状态"revert"回正常的基因靶点。

## 方法
竞赛设定:给定 H1 hESC 未扰动细胞的转录组参考 + 训练集(150 个基因扰动的单细胞谱),参赛者构建模型,对留出的扰动基因预测扰动后的单细胞表达谱。评测用 **三指标复合分**:(1) Differential Expression Score / DES——预测差异表达基因的准确度;(2) Perturbation Discrimination Score / PDS——区分不同扰动效应的能力;(3) Mean Absolute Error / MAE——全基因预测表达与真值的绝对误差。官方基线是 Arc 的 **STATE** 模型(State Transition 双向 transformer + State Embedding),并对比 cell-mean、linear、GEARS 等朴素/已有基线。

## 数据
首届自建单细胞转录组(Perturb-seq)数据集:约 **300,000 个 H1 hESC 细胞 × 300 个基因扰动**,扰动选择覆盖广谱表型响应。划分为:未扰动参考集;训练集 150 个扰动基因(~150,000 细胞);验证集 50 个扰动基因(驱动实时排行榜);最终测试集 100 个留出扰动。允许外部数据:Arc Virtual Cell Atlas(>5 亿细胞)、scBaseCount、Tahoe-100M、X-Atlas/Orion(目前最大公开 Perturb-seq)。

## 主要结果
参与规模:114 国 5,000+ 注册,1,200+ 队提交,300+ 队最终提交。基线水平:在未见单基因扰动上,STATE 相对 cell-mean 基线提升 **26%**,优于 linear(19%)与 GEARS(22%)。关键结论:**纯 AI 方法并未稳定超过统计基线**;几乎所有模型在 MAE 上都不如朴素基线;结合深度学习与统计特征的混合模型胜出,蛋白质 embedding 等多模态特征有增益。获奖:1st BM_xTVC(BioMap,xTrimoSCPerturb,scFoundation+蛋白嵌入);2nd XLearning Lab(度量驱动条件生成 + ESM-2);3rd Outlier(TransPert,跨参考细胞系相似度聚合);Generalist Prize 归 Altos Labs(go-with-the-flow,flow-matching 生成)。

## 创新点
- 为单细胞扰动预测确立**公开、标准化的三指标评测协议**(DES/PDS/MAE)与留出细胞语境的泛化任务框架。
- 发布高质量的新数据资产:300K H1 hESC × 300 扰动的 Perturb-seq 数据集 + STATE 官方基线。
- 通过大规模社区参与,产出"当前 SOTA 到底在哪"的实证结论(混合模型 > 纯神经网络)。

## 局限
- 单一细胞类型(H1 hESC)、单基因扰动、纯转录组模态——尚不覆盖组合扰动、空间/多模态或组织尺度。
- MAE 上模型普遍不敌朴素基线,说明"绝对表达量"预测仍未真正解决;指标本身仍在演化。
- 竞赛结论是"预测扰动效应",不直接回答"哪些基因能 revert 病态"这一逆问题。

## 与本研究方向的关系
直接对应我们 pipeline 的**第二/第三环**:"virtual tissue 建模"与"预测可 revert anomaly 的基因扰动"。挑战给出的正是**扰动→单细胞表达的正向模拟器**——这正是 revert 逆问题的核心引擎:一旦有可靠的 perturbation 模型,就能对"病态 vs 正常"的目标状态做 in-silico 基因扫描,挑出把细胞推回正常的靶点。可复用的还有:(1) STATE 作为预训练 virtual cell 基线;(2) DES/PDS/MAE 作为我们自建 revert 评测的现成协议;(3) "纯 AI 未超统计基线、混合模型更强"的经验教训,提示我们在方法设计上保留统计/生物先验。局限是它停在单细胞、非组织/空间尺度,与我们的 virtual **tissue** 目标间还需空间转录组学的桥接。

## 可复用资产
- **STATE 模型**(Arc 的 virtual cell 模型,State Transition + State Embedding)——预训练基线,可作我们扰动模拟的起点。<https://arcinstitute.org/news/virtual-cell-model-state>
- **挑战数据集**:300K H1 hESC × 300 扰动 Perturb-seq + 官方 splits/leaderboard,<https://virtualcellchallenge.org/>(evaluation page:`/evaluation`)。
- **评测协议**:DES / PDS / MAE 复合评分——可直接移植为 revert 任务评测。
- **外部语料**:Arc Virtual Cell Atlas(>5 亿细胞)、scBaseCount、Tahoe-100M、X-Atlas/Orion Perturb-seq。
- **配套论文**:"Virtual Cell Challenge: Toward a Turing test for the virtual cell," *Cell*, 2025——任务/指标的权威描述。

## 待读
- STATE 模型论文与代码(State Transition / State Embedding 架构细节)。
- 获奖方案:xTrimoSCPerturb(BioMap)、TransPert、Altos "go-with-the-flow" flow-matching——混合与生成式思路。
- 独立基准论文 "Benchmarking virtual cell models for in-the-wild perturbation response" 与 "The Baseline Gap" (Research Square),审视指标可靠性。
- X-Atlas/Orion Perturb-seq 数据说明,评估作为额外训练/迁移语料的价值。

## 引用
```bibtex
% no BibTeX fetched
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

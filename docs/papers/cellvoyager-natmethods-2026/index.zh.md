# CellVoyager: AI CompBio agent generates new insights by autonomously analyzing biological data

> **文献键** `Alber_2026` · **来源** Nature Methods(2026) · **类别** agents · **相关度** high · **获取** paywall
> **链接** <https://doi.org/10.1038/s41592-026-03029-6> · `status: complete`

---

## 一句话
CellVoyager(Stanford Zou 组)是一个在 Jupyter notebook 里自主探索 scRNA-seq 数据的 agent:输入一篇已发表论文和它的数据,先提取"已做过哪些分析",再生成**与之不同**的假设与分析计划(exploration blueprint)、自我批评、写代码执行、用视觉语言模型读图、重新规划;在 CellBench 上比底座 LLM 更会"猜作者做了什么分析",在三个真实再分析案例中由原文作者打分,提出了 CD8+ T 细胞 pyroptosis 评分升高、SVZ 衰老与转录噪声等新假设。

## 研究问题
现有单细胞 agent(CellAgent、CompBioAgent、AutoBA、BIA)主要是"执行用户指令",受限于用户自己的想象力,也不考虑研究者已经做过的分析,因此难以作为真正的合作者去补充已有工作。海量已发表 scRNA-seq 数据很可能还藏着未被分析的信号,但人工系统性再分析不可行。问题是:agent 能否**以既有分析为条件**,自主提出并执行新的、有生物学意义的分析?

## 方法
**输入**:处理好的 scRNA-seq 数据(AnnData)、一份背景报告(本文用已发表论文全文)、Python 环境说明(scanpy、scvi-tools、celltypist 等)。agent 先把论文摘要成"生物学背景 / 已做分析 / 数据细节"三部分,之后只用摘要。**探索循环**:生成 blueprint(假设 + 分步计划 + 第一步代码)→ 自我批评并改进(本文只做一轮)→ 逐步把代码写入 notebook 单元执行;报错则最多修 3 次,仍失败就改换路线;成功则把文本和图像输出交给 VLM 解读,解读写回 markdown 单元并据此重规划;每个分析最多 8 步(案例研究中典型 5–8 步)。分析之间串行,后一个分析以"已做假设列表"为条件避免重复;最后挑出最有前景的结果写报告。**CellBench**:用 gemini-2.5-pro-preview 从论文中抽取背景与全部单细胞分析,仅给背景,让模型/agent 预测作者做了哪些分析,用 LLM 评审判断是否命中(两位博士生对 47 条输出的人工复核与评审一致率 89% 与 85%);评测 CellVoyager 时只运行其构思阶段,不写代码。

## 数据
**CellBench**(预印本):50 篇主要分析 scRNA-seq 的已发表论文,共 483 项分析;正式版摘要称扩到 76 篇研究。**案例**:(1) COVID-19 PBMC 图谱(7 例重症 + 6 例健康对照);(2) 人子宫内膜月经周期图谱(73,180 个细胞、29 位供体,Fluidigm C1 + 10x);(3) 成年小鼠脑室下区(SVZ)跨年龄 scRNA-seq 与单细胞衰老时钟。每个案例生成 8 个分析,按代码成功执行比例选 5 个交给原文一位作者按量表评审。

## 主要结果
**CellBench(预印本)**:以 GPT-4o 为引擎时,CellVoyager 比 GPT-4o 本身 micro 平均准确率高 **16%**(p<0.01)、macro 高 **19.33%**(p<0.001);o3-mini 引擎略低但差异不显著,案例中采用 o3-mini。正式版摘要:76 篇研究上比 GPT-4o 与 o3-mini 最多高 **23%**。**专家评审(15 个分析)**:创造性平均 **2.8/4**(COVID 2.8、子宫内膜 3.4、SVZ 2.4);**12/15** 个假设被认为值得深入研究(预印本摘要称 80%);"有生物学意义"的分别为 3/5、2/5、3/5。**具体发现**:COVID-19 中 CD8+ T 细胞 pyroptosis 基因评分显著升高(p=0.001;作者接受了原文作者"应先按供体 pseudobulk"的反馈后重做);子宫内膜中按作者反馈扩展到 40 对配体-受体相关性,TGF-β 与 FGF2–FGFR1 排前;SVZ 中 astrocyte-qNSC 转录噪声与年龄只有边际相关(r=0.047, p=0.0135),但扩展到全细胞类型的年轻/老年对比后,少突胶质、小胶质、壁细胞的转录噪声显著更高(p<0.001)。对照:Google Colab Data Science Agent 在同样输入下未产出有意义结果。每个分析约 30 分钟。

## 创新点
- **以"已做分析"为条件的探索**:把论文当作"已覆盖区域"的地图,让 agent 去找空白处——这是自主再分析公共数据的清晰问题定义。
- Notebook 原生的可审计轨迹:每一步 = 描述 + 代码 + 输出 + VLM 解读,整本 notebook 就是完整报告。
- CellBench:用"预测作者做过的分析"衡量构思质量的可扩展基准。
- 由原文作者参与的评审 + 人在回路反馈(1–2 条反馈即可显著改进分析)。

## 局限
- 评审规模小:3 篇论文 × 5 个分析、每篇仅 1 位作者评审,无盲法、无对照 agent 的同等评审;"新发现"均未实验验证,且有的结论本身很弱(SVZ r=0.047)。
- **统计严谨性依赖人类纠正**:最初的 COVID 分析在细胞层面做检验,原文作者指出应按供体 pseudobulk——这是单细胞分析里典型的伪重复(pseudo-replication)错误,agent 自己没发现。
- CellBench 以 LLM 抽取 + LLM 评审为主,只衡量构思而不衡量执行正确性。
- 串行运行、每个分析约 30 分钟;主要依赖 scanpy 等热门包,对冷门/内部工具适应差;只做 scRNA-seq。HeurekaBench 的独立评测中,它因固定步数与有限的修代码能力,在开放题上落后于 Biomni 与 BixBench-Agent。

## 与本研究方向的关系
CellVoyager 的设定——"给定已发表论文和它的数据,找作者没做过的分析"——与 **课题 1** 的一个子问题同构:在 KPMP / Lake 肾脏图谱等公共数据上,系统性地寻找原文没报告的异常细胞态或疾病相关程序。但它恰恰示范了这种"自主发现"最需要被约束的地方:它会把细胞当独立样本做检验(伪重复)、会报告 r=0.047 这样的弱信号作为"发现"、新颖性只由原作者主观打分。对 **课题 2** 这是一个很好的**被审计对象**:它的 notebook 轨迹天然把"声明(markdown 解读)"和"证据(代码 + 输出 + 图)"并排放置,正适合做声明-证据核查——检查每条 VLM 解读是否被对应输出支持、统计单位是否正确(细胞 vs 供体)、多次重跑是否给出相同结论。这些错误类型(伪重复、效应量夸大、单模态推断、把 VLM 读图当证据)可直接成为组学失败分类的条目。对 detect → model → revert 主链,它属于"从数据到假设"那一环,其输出应先经过数据层可信度(QC、批次、环境 RNA)与 verifier 过滤,才能进入扰动/逆转候选的排序。

## 可复用资产
- **代码 + CellBench:** 案例研究运行代码与 CellBench 评测数据。
<https://github.com/zou-group/CellVoyager>
- **预印本全文:** 含全部 prompt(附录图 3–17)。
<https://doi.org/10.1101/2025.06.03.657517>
- **评审量表:** 创造性(1–4)/ 生物学有用 / 方法正确 / 值得跟进(附录图 1),可改造成课题 2 的人工标注量表。

## 待读
- 正式版(Nature Methods)的扩展:76 篇研究的 CellBench 与"专家一致评为有创造性且科学合理"的评审细节。
- HeurekaBench 中对 CellVoyager 的失败分析(固定步数、修代码能力)。
- 用于对比的 CellAgent、BIA、AutoBA 等单细胞 agent。

## 引用
```bibtex
@article{Alber_2026, title={CellVoyager: AI CompBio agent generates new insights by autonomously analyzing biological data}, volume={23}, ISSN={1548-7105}, url={http://dx.doi.org/10.1038/s41592-026-03029-6}, DOI={10.1038/s41592-026-03029-6}, number={4}, journal={Nature Methods}, publisher={Springer Science and Business Media LLC}, author={Alber, Samuel and Chen, Bowen and Sun, Eric and Isakova, Alina and Wilk, Aaron J. and Zou, James}, year={2026}, month=Mar, pages={749–759} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

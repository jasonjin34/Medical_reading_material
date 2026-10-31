# SpatialAgent: An autonomous AI agent for spatial biology

> **文献键** `Wang2025_SpatialAgent` · **来源** bioRxiv(2025) · **类别** agents · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1101/2025.04.03.646459> · `status: complete`

---

## 一句话
SpatialAgent 是 Genentech/Regev 组面向空间组学的专用 agent:Plan-Act-Conclude 架构 + 72 个工具 / 17 个可复用 skill 的动态检索 + 图像解读 + **报告与验证子 agent(逐条审计数值与视觉声明)**,覆盖基因 panel 设计、细胞/niche 注释、轨迹、细胞通讯、插补与假设生成;在 DLPFC panel 设计、胎儿心脏 MERFISH 注释上胜过既有方法并与专家持平或更优,并在前瞻性小鼠前列腺癌 Xenium 实验中设计了 100 基因附加 panel(实测 4.2M 细胞、21 个样本)。

## 研究问题
空间组学分析流程碎片化、依赖专家:要在分子、细胞、多细胞相互作用多个尺度上推理,还要整合组织学/解剖图像,固定 pipeline 难以泛化到新组织、新平台、新问题。作者想要一个能从实验设计(选基因 panel)一路做到注释与假设生成、既能全自主又能与科学家 co-pilot 的 agent,并且明确提出要把"执行成功"与"科学推理可靠"区分开。

## 方法
**架构**:LangGraph 状态机实现 Plan(检索 skill/工具、分解步骤、按观察更新计划)→ Act(执行代码、数据库/文献检索、专用工具,持久 Python 环境)→ Conclude(合成回答/报告,可调用报告与验证子 agent)。每会话最多 50 步,执行错误作为观察回传。**工具与 skill**:注册 72 个带类型签名与失败模式描述的工具(13 类:数据访问、空间统计、空间映射、domain 检测、去卷积、轨迹、多模态整合、细胞通讯等),每次查询只检索 5–20 个;17 个 skill 编码常见多步流程(panel 设计、空间 domain、条件感知 CCC、轨迹),作为"结构化指导"而非固定脚本。**可审计性**:每个动作写入 JSONL 日志(代码、工具调用、输出、错误、产物指针);新生成的图由视觉模型自动解读回填进观察流。**验证子 agent**:把数值声明与已保存输出对照、重看图来核对视觉声明,返回逐条评估与修改建议。**后端**:可插拔(Claude/GPT/Gemini 与本地 Qwen、Ministral);基于后端、温度、skill 消融,默认 Claude Sonnet 4.5、T=0.5。

## 数据
基准任务:人 DLPFC Visium(3 位供体 12 张切片)用于 panel 设计;发育中人心脏 scRNA-seq + MERFISH(6 个样本、9–16 周,142,946 个 scRNA 谱 + >1.5M MERFISH 细胞)用于细胞与 niche 注释。开放案例:内部健康人 tonsil CosMx(邻域、B 细胞分化轨迹、Tangram 插补);DSS 小鼠结肠炎 MERFISH(健康 / DSS3 / DSS9 / DSS21,多轮 co-pilot)。湿实验:小鼠前列腺癌 Xenium 5k Pan-Tissue + 100 基因附加 panel,4.2M 细胞、21 个样本(野生型、腺癌、转移),另有治疗后队列(anti-gp120、JAK 抑制剂、anti-PD1、联合)。人类对照:10 位科学家做 panel(50/100/150 基因),8 位做注释,均禁止用 LLM。

## 主要结果
**Panel 设计(DLPFC)**:相对 HVG/GeneBasis/PERSIST/Spapros,细胞类型预测准确率提升 **15.9–45.2%**,空间坐标预测 R² 提升最高 **178.1%**;30 组人机配对中胜过人类设计 26/30(准确率)与 29/30(y 坐标 R²);用 agent 精修人类 panel 后 27/30 与 29/30 优于原版;agent 精修的人类 panel 在 10/30 与 16/30 中超过 agent 自己从零设计——人机互补。运行约 **12.2 分钟、约 $1.8/次**,对比 Spapros 3.8 小时/$123.2、人类中位 4.0 小时/$212.8。**细胞注释(心脏 MERFISH)**:总体准确率 **0.853**,优于 PopV 0.262、scTab 0.157、**Biomni 0.394**、GPTCellType 0.811;GPTCellType 把 98.1% 心外膜、85.5% 免疫、96.9% 神经细胞判成成纤维细胞;SpatialAgent 心外膜仍主要误判为成纤维细胞(82.2%,仅 14.5% 正确);8 位人类专家 0.459–0.834。**Niche 注释**:准确率 **0.661**,人类 0.108–0.873;传导系统、流出道、瓣膜等薄小结构是主要误差(最佳专家对传导系统也仅 37.8%)。**Tonsil**:验证子 agent 发现主 agent 把 "LQ"(低质量细胞)标签误读为滤泡亚区、相关性分析只覆盖部分视野且相关强度仅弱到中等;Tangram 插补留出重建余弦相似度细胞级约 0.5、基因级约 0.3。**结肠炎**:复现原文主要结论,另提出 7 条邻域轨迹(含 FOL2→FOL1→FOL3 滤泡成熟)及分阶段治疗假设(未验证)。**Xenium 前瞻实验**:100 基因附加集细胞类型/恶性状态预测准确率 **0.896**(随机 100 基因 0.516、5k panel 0.929、全部 5.1k 基因 0.950);附加基因 Moran's I 更高;治疗条件预测 0.459(随机 0.371、5k 0.581、全部 0.592)。

## 创新点
- 第一个覆盖"实验设计 → 注释 → 假设"全链条的空间组学专用 agent,且有**前瞻性湿实验**(agent 设计的 panel 真正上机)。
- **报告与验证子 agent**:把"主 agent 的声明"与"保存的输出/图"逐条对照——这是本仓库里最接近声明-证据核查的工程实现之一,且在 tonsil 案例中确实抓到了真实错误。
- Skill 库作为"可靠性层":消融显示 skill 在注释任务上提升最大,减少 label collapse、流程不完整、稀有类丢失等失败。
- 系统的后端/温度/skill 消融与成本-延迟记录;每个基因给出带出处的选择理由。

## 局限
- 作者自陈:性能依赖精心策划的 skill/工具,临时 LLM 规划与代码生成在专业分析上很脆弱;agent 可能产出看似合理却掩盖方法学错误(基准选择、数据泄漏、指标误用、事后选择偏倚)的结果。
- 验证子 agent 只做定性审计,**没有校准置信度或量化的验证准确率**;结肠炎多轮案例中验证 agent 未启用。
- 基准以作者标注为金标准,单数据集、单组织为主;开放案例的新假设(TLS 成熟轨迹、治疗靶点)均未实验验证;作者大多为 Genentech 员工,前列腺数据为内部项目。
- 心外膜细胞等组织特异细胞态仍难识别——LLM 倾向默认常见标签,而非利用数据集特有上下文。

## 与本研究方向的关系
这是本批里与两条论文计划**贴得最近**的一篇。**对伪影注入课题**:它的数据形态(MERFISH/CosMx/Xenium + scRNA 参考 + 解剖图像)与 snRNA + snATAC + Xenium + H&E 这类多模态设计同构;它报告的失败恰好是异常检测要面对的:**稀有/组织特异细胞态被吞进常见类别**(心外膜 82.2% 被判为成纤维细胞)、薄小解剖结构(传导系统)最难——在肾脏里对应的就是罕见损伤态(如 failed-repair PT、炎症性 PT)和小结构(肾小球、JGA)。这提醒我们:异常分数若建立在 agent 或参考映射的标签之上,会系统性低估真正的病灶;同时"低质量细胞标签被误读为生物亚区"正是伪影注入课题想用跨模态一致性(snRNA vs Xenium vs H&E)分离**伪影与疾病**的反例。它的 Xenium 附加 panel 设计也可直接借鉴:为肾脏损伤态/修复态定制附加基因,作为 detect → revert 链条中"为验证异常而设计测量"的一环。**对 Agent 可信度课题**:验证子 agent 是我们 calibrated verifier 的直接前身——它证明了"重读输出与图逐条审计声明"可行且有用,但只停留在定性;Agent 可信度课题的增量正是把它量化(声明级精确率/召回、校准、重跑稳定性),并把 tonsil 案例中出现的失败(误读 QC 标签、只用子集却报告整体、相关强度被夸大、插补结果被当作定量)整理进组学特有失败分类。其 JSONL 执行日志也是我们做 trace 级审计所需的输入格式范本。

## 可复用资产
- **代码:** SpatialAgent 实现、教程 notebook 与假设生成的 agent trace。
<https://github.com/Genentech/SpatialAgent>
- **数据:** 人类科学家与基线方法在 panel 设计/注释任务上的结果。
<https://huggingface.co/datasets/hansen7/spatialagent_human>
- **评测协议:** panel 评估(逻辑回归细胞类型 + Lasso 坐标回归,80/20 × 10 次)、注释评估(accuracy/precision/F1/ARI)、Xenium 附加 panel 的三轴评估(判别力、Moran's I 空间结构、治疗条件预测)。

## 待读
- 补充材料 1.5(报告/验证子 agent 的 prompt 与输出格式)——直接对照 Agent 可信度课题 verifier 设计。
- v1 与 v2 结果差异(GPT-4o → Sonnet 4.5),作为"同一 agent 换底座后结论是否稳定"的案例。
- 引用 39(agent 掩盖方法学失败的讨论)及作者提到的 AI-scientist 评估工作。

## 引用
```bibtex
@article{Wang2025_SpatialAgent, title={SpatialAgent: An autonomous AI agent for spatial biology}, url={http://dx.doi.org/10.1101/2025.04.03.646459}, DOI={10.1101/2025.04.03.646459}, journal={bioRxiv}, publisher={openRxiv}, note={Version 2 posted 2026-08-12}, author={Wang, Hanchen and He, Yichun and Coelho, Paula P. and Bucci, Matthew and Nazir, Abbas and Chen, Bob and Trinh, Linh T. and Zhang, Serena and Lu, Ziyu and Huang, Kexin and Chandrasekar, Vineethkrishna and Chung, Douglas C. and Hao, Minsheng and Leote, Ana Carolina and Lee, Yongju and Li, Bo and Liu, Tianyu and Liu, Jin and Lopez, Romain and Tawaun, Lucas and Ma, Mingyu and Makarov, Nikita and McGinnis, Lisa and Peng, Linna and Ra, Stephen and Scalia, Gabriele and Singh, Avtar and Tao, Liming and Uehara, Masatoshi and Wang, Chenyu and Wei, Runmin and Copping, Ryan and Rozenblatt-Rosen, Orit and Leskovec, Jure and Regev, Aviv}, year={2025}, month=Apr }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

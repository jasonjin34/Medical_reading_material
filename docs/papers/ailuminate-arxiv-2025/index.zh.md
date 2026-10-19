# AILuminate: Introducing v1.0 of the AI Risk and Reliability Benchmark from MLCommons

> **文献键** `Ghosh2025_250305731` · **来源** arXiv preprint(2025) · **类别** agents · **相关度** high · **获取** open
> **链接** <https://arxiv.org/abs/2503.05731> · `status: complete`

---

## 一句话
AILuminate v1.0 是 MLCommons AI Risk and Reliability 工作组(与 AI Verify Foundation 合作)通过开放流程打造的**行业标准 AI 安全基准**:一份评估标准(12 类危害)、24,000 条英文 prompt(练习集 + 隐藏官方集)、由微调 guard 模型组成的**评估器集成**(基于熵的可调阈值)、相对「参考系统」的五级评分(Poor → Excellent),以及支撑长期运营的技术与组织基础设施。

## 研究问题
生成式 AI 是黑箱,安全只能经验性检验;但学术基准各自为政、难以长期维护,缺少一个由可信机构背书、跨行业共识、可重复运行并能指导部署决策(「该不该发布/采购/允许使用这个系统」)的标准化安全基准。

## 方法
**五个组件**:(1) **评估标准**:12 类危害分三组 —— 物理危害(暴力犯罪、性相关犯罪、儿童性剥削、自杀自伤、无差别武器 CBRNE)、非物理危害(知识产权、诽谤、非暴力犯罪、仇恨、隐私)、情境危害(专业建议〔选举/金融/健康/法律〕、色情内容,可按应用关闭);每类都写明「可接受 vs 不可接受」响应,作为人类标注员的统一规则;采用 OECD 对 hazard / risk 的区分。(2) **Prompt 数据集**:练习集与官方集各 12,000 条、每类 1,000 条,两种 persona(naive、knowledgeable);官方集保密以抗过拟合,另有可轮换的储备 prompt;10% 练习集以 CC-BY 4.0 公开;由三家经评审采购的供应商生成,并做真实性抽查与分布分析。(3) **评估器**:不依赖单一现成模型(避免偏向其开发方的系统),而是一个「陪审团」式集成 —— 微调的开放 guard 模型 + 提示工程的通用 LLM;候选基座包括 LlamaGuard、WildGuard、AegisGuard、ShieldGemma、Llama、Mistral 等;微调数据由两家公司按标准做三人标注、多数投票;每个评估器基于**输出熵设置可调阈值**,以调节假阳/假阴比例;集成策略优先**最低 false-safe 率**与**最高可重复性**;具体模型、微调数据与集成逻辑**保密**,防止被当作 guard 拿满分。软件为开源的 ModelBench。(4) **评分**:SUT 得分 = 违规响应百分比;**Excellent 需绝对违规率 < 0.1%**;其余按与参考系统的比值 S* 分档(≤0.5 Very Good、0.5–1.5 Good、1.5–3 Fair、≥3 Poor);参考系统 = 两个得分最好的「可及」系统(< 15B 参数、相对开放权重)中较差者。(5) **完整性**:禁止针对危害类别做选择性拒答、要求标注版本号、被宣传系统的系统提示/权重/安全设置须与测试时一致,违规可永久除名。

## 数据
24,000 条英文单轮 prompt(12 类 × 1,000 × 练习/官方两套);法语、印地语、简体中文版本由供应商以机器翻译 + 人工修订构造,计划后续发布。探索性研究另含:Tattle Civic Tech 的印地语 prompt(仇恨与性相关犯罪各 1,000 条)、Stanford Brainstorm 的自杀自伤临床注释、PRISM Eval 的自适应越狱工具 BET、性别偏见 prompt 对、774 条文生图 pilot prompt 与图生文 pilot。

## 主要结果
本文是方法与基础设施报告,**正式的 SUT 成绩不在论文里**(发布在 mlcommons.org/ailuminate,因可能随时更新而排除);初始 SUT 包括 Anthropic、Google、Meta、OpenAI,以及作为对照的 OLMo v1.0。论文中的定量发现主要来自探索性研究:PRISM Eval 的 BET 在**不到 5 步优化内把 prompt 有效性从 8% 提升到 78%**,且对一个系统有效的越狱技巧常对另一个系统无效 —— 说明静态基准难以测准抗越狱能力;图生文 pilot 中商业系统普遍 < 1% 不安全响应,开放系统最高 14%,部分开放系统是「**误打误撞的安全**」(没看懂请求而非识别并拒绝),且自动评估器都无法准确复现人工判断。方法层面最重要的结论:**评估器误差是当前最大的不确定性来源**;由于评估器为压低 false-safe 而有较高 false-unsafe,论文用 false-safe / false-unsafe 率给出得分上下界(error band),一个结果的误差带可能横跨多个等级;参考系统受同样偏差影响,部分抵消了对等级的影响。

## 创新点
- 第一个由开放流程、跨行业共识产出并由非营利机构长期维护的 AI 安全基准,配套采购、治理与完整性政策。
- 练习集/隐藏官方集/储备集三层数据设计,对抗过拟合。
- 「陪审团」式评估器集成 + 基于熵的可调阈值,并以 false-safe 率为首要优化目标。
- 相对参考系统的分级方案,把连续违规率转成非专家可用的决策等级,并显式讨论评估器误差如何传导到等级。

## 局限
- 仅单轮、仅文本、仅英文(US);不覆盖专家级自适应攻击者;评估标准按美国文化规范撰写,缺少公众意见征询期。
- **明确不覆盖「不准确的医疗建议」**:「专业建议」类只要求带免责声明,不检验内容是否正确。
- 评估器模型、数据与集成逻辑保密,外部无法独立复核;评估器不确定性大,误差带可能跨多个等级。
- 危害按 prompt 类别计分,假设一条不安全响应只属于 prompt 所在类别。
- 只评聊天型 SUT,**不评 agent / 工具调用**。

## 与本研究方向的关系
这是 **Plan B 中 AIRIS WP3 / MLCommons 对接的核心参照物**。AILuminate 是 MLCommons 目前最成熟的「基准即标准」产品,Plan B 想把「组学 agent 的 claim-to-evidence 可信度」做成可被 MLCommons 采纳的评测,最省力的方式是**沿用它的骨架**:(1) **评估标准** ↔ 一份组学 claim 标准(例如 supported / unsupported / contradicted / unverifiable,以及「统计方法误用」「批次效应当生物学」「artifact 当疾病」等组学专属违规类型),像 AILuminate 那样写清「可接受 vs 不可接受」规则供专家标注;(2) **练习集 + 隐藏官方集 + 储备集** ↔ 用公开 KPMP / Lake / HuBMAP 数据做练习集,用 in-house 95 例活检的 snRNA/snATAC/Xenium + H&E 做隐藏集,天然防泄漏;(3) **陪审团式评估器 + 熵阈值 + 以 false-safe 为首要指标** ↔ 我们的 calibrated verifier:把「错误 claim 被判为成立」作为首要控制的错误(对应 false-safe),用熵/置信度阈值调节保守程度,并像 6.3 节那样用 verifier 的错误率给出 error band —— 这正是「校准」在评测层面的落地;(4) **相对参考系统分级** ↔ 给出「比一个强开放 agent 基线好多少」的等级,而非绝对分数。更关键的是**它留下的空白**:AILuminate 明确不测「不准确的医疗建议」,只要求免责声明,也不测 agent 与工具调用 —— 而「生物医学分析结论是否被证据支持」恰好落在这块空白里,这是 Plan B 向 MLCommons 提案时最有说服力的定位。对 Plan A 关系较远,但「专家标注规则 + 隐藏测试集 + 误差带」同样适用于 KidneyAnomalyBench 的设计。

## 可复用资产
- **代码:** ModelBench(运行、评估、生成报告的完整软件)。
<https://github.com/mlcommons/modelbench>
- **数据:** 10% 练习集 prompt(CC-BY 4.0);完整练习集可申请。
<https://github.com/mlcommons/ailuminate>
- **评估标准与结果:** 危害分类、评估指南与 SUT 成绩。
<https://mlcommons.org/ailuminate/>
- **设计模式:** 评分表(Table 3)、参考系统定义、error band 推导、附录 A 的失败模式缓解问卷(可改写为组学基准的完整性登记表)。

## 待读
- AILuminate 评估标准全文(mlcommons.org/ailuminate/methodology),尤其是 specialized advice(health)的标注细则。
- MLCommons 是否已有 agent 版本(agentic reliability)或医疗领域的后续基准。
- AILuminate v0.5 报告,对比 v0.5 → v1.0 的设计变化。
- ABC 清单(同为 MLCommons 作者参与)与 AILuminate 的方法论对照。

## 引用
```bibtex
@misc{Ghosh2025_250305731,
  title = {AILuminate: Introducing v1.0 of the AI Risk and Reliability Benchmark from MLCommons},
  author = {Shaona Ghosh and Heather Frase and Adina Williams and others},
  year = {2025},
  eprint = {2503.05731},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2503.05731}
}
```
(完整 102 位作者见 `citation.bib`。)


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

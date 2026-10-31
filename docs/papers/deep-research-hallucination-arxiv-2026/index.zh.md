# Why Your Deep Research Agent Fails? On Hallucination Evaluation in Full Research Trajectory

> **文献键** `Zhan2026_260122984` · **来源** arXiv preprint(2026) · **类别** agents · **相关度** high · **获取** open
> **链接** <https://arxiv.org/abs/2601.22984> · `status: complete`

---

## 一句话
从「只看最终报告」转向「审计整条 plan–search–summarize 轨迹」:提出 **PING 分类法**(Propagation 传播、Intent 意图、Noise-induced 噪声、Grounding 落地)把 deep research agent(DRA)的幻觉按失效位置分四类,配套把轨迹拆成原子 action/claim/sub-query 的评估框架,并筛出 100 道高幻觉倾向题构成 **DeepHalluBench**;六个 DRA 无一在所有维度上都低幻觉,失效可追溯到**幻觉传播**与「锚定效应」「同质化偏差」等认知偏差。

## 研究问题
现有 DRA 基准要么是有标准答案的闭式题(GAIA、BrowseComp),要么是用参考报告/rubric 评长报告的开放题,**几乎都是结果导向、把研究过程当黑箱**。由此带来两大问题:(1) 中间幻觉(如误导性计划)检测不全;(2) 无法把失败归因到具体阶段。落地过程级评估有三重障碍:缺 DRA 专用幻觉分类法;专有 DRA 没有经济的 API 或结构化日志;多阶段轨迹的评估本身很复杂。

## 方法
**PING 分类法**(把搜索引擎视为外部信息源,只评 plan 与 summarize 阶段由 LLM 引起的幻觉):**Grounding**(来源级)= 捏造(轨迹中无证据)+ 错误归因(引用的文档不支持,而别的已检索文档可能支持);**Noise-induced**(上下文级)= 已检索到相关证据却未被利用;**Intent**(查询级)= 限制条件被忽略(如忽略「全职」)+ 行动偏离用户意图;**Propagation**(轨迹级)= 后续动作建立在早先的幻觉内容上。**数据获取**:自研 HTML 解析器 + LLM 把网页 UI 的轨迹重建为结构化 plan–search–summarize 循环,并对照渲染 HTML 人工核对。**评估**:两轮 claim 核验(NLI→LLM 级联的检索后核验;不被支持的再做错误归因检查/反思检查);噪声分数用语义聚类 + 相关性排序,对「大、排名高、却被跳过而低排名簇被使用」的簇加重惩罚 P_c = S_c × N_inv / R_c,并按最坏情况归一化;行动核验结合历史与 Claim Memory 识别偏离与传播;限制检查把 sub-query 当原子限制,用肘部法判断哪些被执行。**可靠性**:claim 核验在 FEVER 上 95.2%、SciFact-Open 上 87.3%;20 条轨迹约 8,800 个原子单元的双人审计,原始 κ=0.83。

## 数据
**DeepHalluBench** 100 题,开放/闭式各半:从 Mind2Web2、ReportEval、BrowseComp 汇集候选,用两个开源 DRA(gpt-researcher、MiroThinker)作探针生成完整轨迹,取平均幻觉分最高的 75 题(每源 25);再对可解闭式题做原子扰动(如改时间限制)合成 **25 道「无答案」对抗题**,人工确认不可解。被评系统:Gemini、OpenAI、Perplexity、Qwen、Grok 五个专有 DRA + Salesforce Deep Research(开源)。

## 主要结果
**六项指标(表 2,越低越好)**:捏造率 Grok 最高 0.1509、OpenAI 0.1463,Perplexity 最低 0.0978;错误归因 Salesforce 最高 0.2136(捏造却很少);噪声分 Grok 0.4813、Perplexity 0.3905 最高,Salesforce 0.0988 最低(检索范围窄、上下文竞争少);限制忽略 OpenAI 最低 0.0416、Salesforce 最高 0.2847;传播率整体很低(0.0021–0.0176)。Grok 不暴露规划轨迹,只评可观测指标。**闭式题(50 题,各跑两次)**:三类画像 —— **过度自信**(Gemini、Grok:对抗题准确率 0.00 / 0.08,无法拒答)、**过度保守**(Salesforce、Qwen:对抗题 0.80 / 0.72,但可答题 0.00)、**平衡但挣扎**(OpenAI 三项都是 0.28,Perplexity);两次运行每个 DRA 最多 3 题不同。**失效机制**:Gemini 与 OpenAI 超过 57% 的源头错误出现在早期(早期级联),Salesforce 超过 40% 的错误在后期(长上下文崩溃);闭式题中,中间摘要阶段的捏造常是最终答错的前兆;无幻觉轨迹里开源 DRA 倾向拒答,专有 DRA 倾向编造答案。**认知偏差**:「锚定效应」—— 后期被利用的 chunk 数骤降,即便后期检索质量更高;「同质化偏差」—— 相关性相当时小簇在每个 DRA 中都更容易被忽略(Δ 0.064–0.124)。换更强底座后这些模式依旧存在。

## 创新点
- PING:按「失效位置」(来源/上下文/查询/轨迹)组织的 DRA 幻觉分类法,把「漏用证据」与「错误传播」纳入幻觉范畴。
- 从网页 UI 重建专有 DRA 轨迹的解析流程 —— 解决「没有日志就没法做过程评估」的现实障碍。
- 「无答案」对抗题:直接测量 agent 是否会拒答不可解问题,区分过度自信与过度保守。
- 把幻觉映射为 DAG 做根因与时间分布分析;识别锚定效应与同质化偏差。

## 局限
- 只诊断工作流中「在哪里」出错,不解释底座 LLM 的内在参数化原因。
- 只处理文本轨迹;多模态网页内容未覆盖。
- 原子级评估重深度轻规模,成本远高于端到端指标;基准仅 100 题且为「高幻觉倾向」筛选的压力测试集,不代表平均情况。
- 轨迹是厂商暴露过程的「可观测代理」,并非真实内部过程;Grok 无规划轨迹;四个维度异质不可直接相加。

## 与本研究方向的关系
这是 **Agent 可信度课题「组学专用失效分类法」最该对标的过程级框架**。分析肾脏组学的 agent 同样是 plan(选择 QC 阈值、聚类分辨率、比较组)–act(运行代码)–summarize(写结论)的循环,PING 的四类可以一一映射:**Grounding** → 结论与 agent 自己的分析输出不符或引用错产物;**Noise-induced** → 已经算出却被忽略的关键结果(例如 snATAC 与 snRNA 不一致的信号被跳过 —— 这恰恰是伪影注入课题用来区分伪影与疾病的跨模态信号);**Intent** → 忽略用户限制(只看 PT 细胞、只用 DKD 样本)或擅自改变分析问题;**Propagation** → 早期错误(错误的细胞注释、批次效应未校正)被后续每一步继承。三点直接可借:(1) **「无答案」对抗题** —— 在 KidneyAnomalyBench / Agent 可信度课题中加入数据里根本不存在信号的任务(如对纯伪影区域问「疾病机制是什么」),测试 agent 能否拒答;(2) **早期级联**提示 verifier 应在早期步骤(QC、注释)而非只在最终报告处设检查点;(3) 两次运行最多 3/50 不同的稳定性报告方式,是 Agent 可信度课题「重复运行稳定性」的最小可行模板。锚定效应与同质化偏差也提示:agent 会偏爱早期、量大的证据,稀有细胞状态或小病灶的信号最容易被忽略 —— 而这正是异常检测最关心的。

## 可复用资产
- **代码与数据(DeepHalluBench):**
<https://github.com/yuhao-zhan/DeepHalluBench>
- **指标公式:** H_G(式 1–2)、H_N 噪声惩罚(式 3–4)、H_P(式 5)、H_I(式 6–7)。
- **基准构造流程:** 多探针筛选高幻觉题 + 原子扰动合成不可解题。
- **核验器验证:** FEVER、SciFact-Open 作为 claim 核验模块的外部校准集。

## 待读
- TRACE(Chen et al., 2026)与 MiroEval(Ye et al., 2026):其它过程感知的 DRA 评估。
- Hao et al. (2025) 意图幻觉;Ma et al. (2024) RAG 中的事实遗漏 —— PING 的 Intent 与 Noise 两类的来源。
- 附录 D.2(换底座消融)与 E.1(传播 DAG 构造)。
- 与本仓库 mast-neurips-2025、trail-arxiv-2025(多 agent / 轨迹失效分类)对读。

## 引用
```bibtex
@misc{Zhan2026_260122984,
  title = {Why Your Deep Research Agent Fails? On Hallucination Evaluation in Full Research Trajectory},
  author = {Yuhao Zhan and Tianyu Fan and Linxuan Huang and Zirui Guo and Chao Huang},
  year = {2026},
  eprint = {2601.22984},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2601.22984}
}
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

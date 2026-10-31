# Why Your Deep Research Agent Fails? On Hallucination Evaluation in Full Research Trajectory

> **Bibkey** `Zhan2026_260122984` · **Venue** arXiv preprint (2026) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2601.22984>
> `status: complete` — 基于 arXiv HTML 全文精读(正文 + Limitations;附录 B–E 未逐条核对)。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> 从「只看最终报告」转向「审计整条 plan–search–summarize 轨迹」:提出 **PING 分类法**(Propagation 传播、Intent 意图、Noise-induced 噪声、Grounding 落地)把 deep research agent(DRA)的幻觉按失效位置分四类,配套把轨迹拆成原子 action/claim/sub-query 的评估框架,并筛出 100 道高幻觉倾向题构成 **DeepHalluBench**;六个 DRA 无一在所有维度上都低幻觉,失效可追溯到**幻觉传播**与「锚定效应」「同质化偏差」等认知偏差。
<!-- EN --> Shifts from final-report evaluation to auditing the whole plan–search–summarize trajectory: the **PING taxonomy** (Propagation, Intent, Noise-induced, Grounding) classifies deep-research-agent (DRA) hallucinations by locus of failure, an evaluation framework decomposes trajectories into atomic actions/claims/sub-queries, and 100 hallucination-prone queries form **DeepHalluBench**. None of six DRAs is uniformly low-hallucination; failures trace to **hallucination propagation** and cognitive biases — the temporal "Anchor Effect" and semantic "Homogeneity Bias".

## 研究问题 / Problem
<!-- ZH --> 现有 DRA 基准要么是有标准答案的闭式题(GAIA、BrowseComp),要么是用参考报告/rubric 评长报告的开放题,**几乎都是结果导向、把研究过程当黑箱**。由此带来两大问题:(1) 中间幻觉(如误导性计划)检测不全;(2) 无法把失败归因到具体阶段。落地过程级评估有三重障碍:缺 DRA 专用幻觉分类法;专有 DRA 没有经济的 API 或结构化日志;多阶段轨迹的评估本身很复杂。
<!-- EN --> Existing DRA benchmarks are either closed-ended with ground-truth answers (GAIA, BrowseComp) or open-ended long-report evaluations against reference reports/rubrics — **almost all outcome-oriented, treating the research process as a black box**. Two consequences: (1) intermediate hallucinations (e.g. misleading plans) are only partly detected; (2) failures cannot be attributed to stages. Three obstacles to process-aware evaluation: no DRA-specific hallucination taxonomy; proprietary DRAs lack affordable APIs or structured logs; multi-stage trajectories are hard to evaluate consistently.

## 方法 / Method
<!-- ZH --> **PING 分类法**(把搜索引擎视为外部信息源,只评 plan 与 summarize 阶段由 LLM 引起的幻觉):**Grounding**(来源级)= 捏造(轨迹中无证据)+ 错误归因(引用的文档不支持,而别的已检索文档可能支持);**Noise-induced**(上下文级)= 已检索到相关证据却未被利用;**Intent**(查询级)= 限制条件被忽略(如忽略「全职」)+ 行动偏离用户意图;**Propagation**(轨迹级)= 后续动作建立在早先的幻觉内容上。**数据获取**:自研 HTML 解析器 + LLM 把网页 UI 的轨迹重建为结构化 plan–search–summarize 循环,并对照渲染 HTML 人工核对。**评估**:两轮 claim 核验(NLI→LLM 级联的检索后核验;不被支持的再做错误归因检查/反思检查);噪声分数用语义聚类 + 相关性排序,对「大、排名高、却被跳过而低排名簇被使用」的簇加重惩罚 P_c = S_c × N_inv / R_c,并按最坏情况归一化;行动核验结合历史与 Claim Memory 识别偏离与传播;限制检查把 sub-query 当原子限制,用肘部法判断哪些被执行。**可靠性**:claim 核验在 FEVER 上 95.2%、SciFact-Open 上 87.3%;20 条轨迹约 8,800 个原子单元的双人审计,原始 κ=0.83。
<!-- EN --> **PING taxonomy** (the search engine is an external source; only LLM-induced hallucinations at plan and summarize stages are scored): **Grounding** (source level) = fabrication (no evidence in the trajectory) + misattribution (cited documents don't support it, though other retrieved ones might); **Noise-induced** (context level) = relevant retrieved evidence left unused; **Intent** (query level) = restriction neglect (e.g. ignoring "full-time") + deviated actions; **Propagation** (trajectory level) = later actions built on earlier hallucinated content. **Data acquisition**: custom HTML parsers + LLMs reconstruct web-UI traces into structured plan–search–summarize loops, manually checked against rendered HTML. **Evaluation**: two-round claim verification (retrieve-then-verify via an NLI→LLM cascade; unsupported claims get misattribution/reflection checks); the noise score clusters retrieved chunks semantically, ranks them by relevance, and penalizes large, high-ranked clusters skipped while lower-ranked ones are used, P_c = S_c × N_inv / R_c, normalized by a worst case; action verification uses history plus Claim Memory to flag deviation and propagation; restriction checking treats sub-queries as atomic restrictions and uses an elbow rule to decide which were addressed. **Reliability**: claim verification 95.2% on FEVER and 87.3% on SciFact-Open; a two-annotator audit of 20 trajectories (~8,800 atomic units) with raw κ = 0.83.

## 数据 / Data
<!-- ZH --> **DeepHalluBench** 100 题,开放/闭式各半:从 Mind2Web2、ReportEval、BrowseComp 汇集候选,用两个开源 DRA(gpt-researcher、MiroThinker)作探针生成完整轨迹,取平均幻觉分最高的 75 题(每源 25);再对可解闭式题做原子扰动(如改时间限制)合成 **25 道「无答案」对抗题**,人工确认不可解。被评系统:Gemini、OpenAI、Perplexity、Qwen、Grok 五个专有 DRA + Salesforce Deep Research(开源)。
<!-- EN --> **DeepHalluBench**: 100 queries, half open- and half closed-ended. Candidates pooled from Mind2Web2, ReportEval and BrowseComp; two open-source DRAs (gpt-researcher, MiroThinker) generate full trajectories as probes; the 75 with the highest average hallucination score (25 per source) are kept; **25 adversarial "no-answer" queries** are synthesized by atomic perturbations of solvable closed-ended queries (e.g. altered temporal constraints) and manually verified as unsolvable. Systems: five proprietary DRAs (Gemini, OpenAI, Perplexity, Qwen, Grok) plus open-source Salesforce Deep Research.

## 主要结果 / Key results
<!-- ZH --> **六项指标(表 2,越低越好)**:捏造率 Grok 最高 0.1509、OpenAI 0.1463,Perplexity 最低 0.0978;错误归因 Salesforce 最高 0.2136(捏造却很少);噪声分 Grok 0.4813、Perplexity 0.3905 最高,Salesforce 0.0988 最低(检索范围窄、上下文竞争少);限制忽略 OpenAI 最低 0.0416、Salesforce 最高 0.2847;传播率整体很低(0.0021–0.0176)。Grok 不暴露规划轨迹,只评可观测指标。**闭式题(50 题,各跑两次)**:三类画像 —— **过度自信**(Gemini、Grok:对抗题准确率 0.00 / 0.08,无法拒答)、**过度保守**(Salesforce、Qwen:对抗题 0.80 / 0.72,但可答题 0.00)、**平衡但挣扎**(OpenAI 三项都是 0.28,Perplexity);两次运行每个 DRA 最多 3 题不同。**失效机制**:Gemini 与 OpenAI 超过 57% 的源头错误出现在早期(早期级联),Salesforce 超过 40% 的错误在后期(长上下文崩溃);闭式题中,中间摘要阶段的捏造常是最终答错的前兆;无幻觉轨迹里开源 DRA 倾向拒答,专有 DRA 倾向编造答案。**认知偏差**:「锚定效应」—— 后期被利用的 chunk 数骤降,即便后期检索质量更高;「同质化偏差」—— 相关性相当时小簇在每个 DRA 中都更容易被忽略(Δ 0.064–0.124)。换更强底座后这些模式依旧存在。
<!-- EN --> **Six metrics (Table 2, lower is better)**: fabrication highest for Grok (0.1509) and OpenAI (0.1463), lowest for Perplexity (0.0978); misattribution highest for Salesforce (0.2136) despite little fabrication; noise highest for Grok (0.4813) and Perplexity (0.3905), lowest for Salesforce (0.0988, narrower retrieval, less context competition); restriction neglect lowest for OpenAI (0.0416), highest for Salesforce (0.2847); propagation rare overall (0.0021–0.0176). Grok exposes no planning trace, so only observable metrics are scored. **Closed-ended (50 queries, two runs each)**: three profiles — **over-confidence** (Gemini, Grok: 0.00 / 0.08 on no-answer queries, failing to reject), **over-conservatism** (Salesforce, Qwen: 0.80 / 0.72 on no-answer queries but 0.00 on answerable ones), **balanced struggle** (OpenAI at 0.28 on all three, Perplexity); the two runs differ on at most 3 of 50 queries per DRA. **Mechanisms**: for Gemini and OpenAI >57% of source errors occur early (early cascading); Salesforce has >40% of errors late (long-context collapse); on closed-ended queries, intermediate summarization fabrication frequently precedes wrong final answers; in hallucination-free trajectories the open-source DRA refuses while proprietary DRAs fabricate an answer. **Cognitive biases**: "Anchor Effect" — utilized chunk counts collapse in later stages even when later retrieval quality improves; "Homogeneity Bias" — at comparable relevance, small clusters are ignored more than large ones in every DRA (Δ 0.064–0.124). The patterns persist with a stronger backbone.

## 创新点 / Contributions
- <!-- ZH --> PING:按「失效位置」(来源/上下文/查询/轨迹)组织的 DRA 幻觉分类法,把「漏用证据」与「错误传播」纳入幻觉范畴。 <!-- EN --> PING: a DRA hallucination taxonomy organized by locus of failure (source/context/query/trajectory), bringing evidence neglect and error propagation into scope.
- <!-- ZH --> 从网页 UI 重建专有 DRA 轨迹的解析流程 —— 解决「没有日志就没法做过程评估」的现实障碍。 <!-- EN --> A parser pipeline reconstructing proprietary DRA trajectories from web UIs — overcoming the "no logs, no process evaluation" barrier.
- <!-- ZH --> 「无答案」对抗题:直接测量 agent 是否会拒答不可解问题,区分过度自信与过度保守。 <!-- EN --> Adversarial "no-answer" queries directly measure whether agents reject unsolvable tasks, separating over-confidence from over-conservatism.
- <!-- ZH --> 把幻觉映射为 DAG 做根因与时间分布分析;识别锚定效应与同质化偏差。 <!-- EN --> Maps hallucinations into a DAG for root-cause and temporal analysis; identifies the Anchor Effect and Homogeneity Bias.

## 局限 / Limitations
- <!-- ZH --> 只诊断工作流中「在哪里」出错,不解释底座 LLM 的内在参数化原因。 <!-- EN --> Diagnoses where in the workflow hallucinations arise, not their intrinsic parametric causes in the backbone.
- <!-- ZH --> 只处理文本轨迹;多模态网页内容未覆盖。 <!-- EN --> Text trajectories only; multimodal web content not covered.
- <!-- ZH --> 原子级评估重深度轻规模,成本远高于端到端指标;基准仅 100 题且为「高幻觉倾向」筛选的压力测试集,不代表平均情况。 <!-- EN --> Atomic evaluation trades scale for depth and is costly; the 100-query benchmark is a stress test selected for hallucination-proneness, not an average-case sample.
- <!-- ZH --> 轨迹是厂商暴露过程的「可观测代理」,并非真实内部过程;Grok 无规划轨迹;四个维度异质不可直接相加。 <!-- EN --> Parsed trajectories are observable proxies of provider-exposed processes, not true internals; Grok lacks planning traces; the four dimensions are heterogeneous and not summable.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 这是 **Agent 可信度课题「组学专用失效分类法」最该对标的过程级框架**。分析肾脏组学的 agent 同样是 plan(选择 QC 阈值、聚类分辨率、比较组)–act(运行代码)–summarize(写结论)的循环,PING 的四类可以一一映射:**Grounding** → 结论与 agent 自己的分析输出不符或引用错产物;**Noise-induced** → 已经算出却被忽略的关键结果(例如 snATAC 与 snRNA 不一致的信号被跳过 —— 这恰恰是伪影注入课题用来区分伪影与疾病的跨模态信号);**Intent** → 忽略用户限制(只看 PT 细胞、只用 DKD 样本)或擅自改变分析问题;**Propagation** → 早期错误(错误的细胞注释、批次效应未校正)被后续每一步继承。三点直接可借:(1) **「无答案」对抗题** —— 在 KidneyAnomalyBench / Agent 可信度课题中加入数据里根本不存在信号的任务(如对纯伪影区域问「疾病机制是什么」),测试 agent 能否拒答;(2) **早期级联**提示 verifier 应在早期步骤(QC、注释)而非只在最终报告处设检查点;(3) 两次运行最多 3/50 不同的稳定性报告方式,是 Agent 可信度课题「重复运行稳定性」的最小可行模板。锚定效应与同质化偏差也提示:agent 会偏爱早期、量大的证据,稀有细胞状态或小病灶的信号最容易被忽略 —— 而这正是异常检测最关心的。
<!-- EN --> This is **the process-level framework the agent-trustworthiness topic's omics-specific failure taxonomy should benchmark against**. An agent analysing kidney omics runs the same plan (choose QC thresholds, clustering resolution, comparison groups) – act (run code) – summarize (write conclusions) loop, and PING maps one-to-one: **Grounding** → conclusions that contradict the agent's own outputs or cite the wrong artefact; **Noise-induced** → computed-but-ignored key results (e.g. skipping snATAC–snRNA disagreement — exactly the cross-modal signal the artifact-injection topic uses to separate artefact from disease); **Intent** → ignoring user restrictions (PT cells only, DKD samples only) or silently changing the question; **Propagation** → early errors (wrong cell annotation, uncorrected batch effects) inherited by every later step. Three things to borrow: (1) **adversarial no-answer tasks** — add tasks to KidneyAnomalyBench / the agent-trustworthiness topic where the signal simply isn't in the data (e.g. asking for the disease mechanism of a pure-artefact region) to test whether the agent declines; (2) **early cascading** says the verifier should checkpoint early steps (QC, annotation), not only the final report; (3) reporting that two runs differ on at most 3/50 queries is a minimal template for the agent-trustworthiness topic's rerun-stability measurement. The Anchor Effect and Homogeneity Bias also warn that agents favour early, abundant evidence, so signals from rare cell states or small lesions are the most likely to be ignored — precisely what anomaly detection cares about.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码与数据(DeepHalluBench):** <!-- EN --> **Code and data (DeepHalluBench):**
<!-- ZH/EN --> <https://github.com/yuhao-zhan/DeepHalluBench>
- <!-- ZH --> **指标公式:** H_G(式 1–2)、H_N 噪声惩罚(式 3–4)、H_P(式 5)、H_I(式 6–7)。 <!-- EN --> **Metric formulas:** H_G (Eqs. 1–2), H_N noise penalty (Eqs. 3–4), H_P (Eq. 5), H_I (Eqs. 6–7).
- <!-- ZH --> **基准构造流程:** 多探针筛选高幻觉题 + 原子扰动合成不可解题。 <!-- EN --> **Benchmark construction recipe:** multi-probe selection of hallucination-prone queries + atomic perturbation to synthesize unsolvable ones.
- <!-- ZH --> **核验器验证:** FEVER、SciFact-Open 作为 claim 核验模块的外部校准集。 <!-- EN --> **Verifier validation:** FEVER and SciFact-Open as external calibration sets for the claim-verification module.

## 待读 / Follow-ups
- <!-- ZH --> TRACE(Chen et al., 2026)与 MiroEval(Ye et al., 2026):其它过程感知的 DRA 评估。 <!-- EN --> TRACE (Chen et al., 2026) and MiroEval (Ye et al., 2026): other process-aware DRA evaluations.
- <!-- ZH --> Hao et al. (2025) 意图幻觉;Ma et al. (2024) RAG 中的事实遗漏 —— PING 的 Intent 与 Noise 两类的来源。 <!-- EN --> Hao et al. (2025) on intent hallucination; Ma et al. (2024) on fact omission in RAG — the origins of PING's Intent and Noise categories.
- <!-- ZH --> 附录 D.2(换底座消融)与 E.1(传播 DAG 构造)。 <!-- EN --> Appendix D.2 (backbone ablation) and E.1 (propagation DAG construction).
- <!-- ZH --> 与本仓库 mast-neurips-2025、trail-arxiv-2025(多 agent / 轨迹失效分类)对读。 <!-- EN --> Read with mast-neurips-2025 and trail-arxiv-2025 (multi-agent / trace failure taxonomies) in this repo.

## 引用 / Cite
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

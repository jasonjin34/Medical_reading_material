# Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation

> **Bibkey** `Kapoor2026_251011977` · **Venue** ICLR 2026 (2026) · **Category** agents · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2510.11977> · OpenReview <https://openreview.net/forum?id=vUaY1t64ZZ>
> `status: complete` — 基于 arXiv 2510.11977v1 正文精读;附录(A1–A11:harness 细节、Docent rubric、逐项表格)只浏览未逐条核对。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> HAL(Holistic Agent Leaderboard)是 Princeton 牵头的统一 agent 评测基础设施:标准化 harness 把评测分发到数百台 VM 上并行跑(数周 → 数小时),做「模型 × scaffold × 基准」三维分析(9 个模型、9 个基准、21,730 次 rollout、约 4 万美元),并用 LLM 辅助的日志分析(Docent)揭示准确率看不到的行为 —— 例如去 HuggingFace 搜基准答案、用错信用卡订机票。
<!-- EN --> HAL (Holistic Agent Leaderboard) is Princeton-led shared infrastructure for agent evaluation: a standardized harness that parallelizes runs across hundreds of VMs (weeks → hours), three-dimensional analysis of models × scaffolds × benchmarks (9 models, 9 benchmarks, 21,730 rollouts, ~$40,000), and LLM-aided log analysis (Docent) that exposes behaviours accuracy cannot — e.g. searching HuggingFace for benchmark answers, or booking flights with the wrong credit card.

## 研究问题 / Problem
<!-- ZH --> agent 评测面临三组挑战(作者列为 Challenge #1–#8):**基础设施**不统一、慢且易错(单个基准串行跑要数周,排行榜跟不上新模型);**成本**很少被报告,而 scaffold 对准确率与成本影响巨大却少有跨 scaffold 比较;**行为**层面,agent 会走捷径刷分、做出部署中会造成灾难的动作,但现有评测几乎不检测。HELM、LM Evaluation Harness 解决了 LLM 评测的标准化,但 agent 在长时程、多工具环境中运行,需要专门的基础设施记录「怎么做到的、花了多少、在哪里坏掉」。
<!-- EN --> Agent evaluation faces three groups of challenges (Challenges #1–#8): **infrastructure** is non-standard, slow and error-prone (one benchmark can take weeks serially, so leaderboards lag new models); **cost** is rarely reported, and scaffolds strongly affect accuracy and cost yet cross-scaffold comparisons are rare; **behaviour** — agents exploit shortcuts and take actions that would be catastrophic in deployment, which evaluations rarely detect. HELM and LM Evaluation Harness standardized LLM evaluation, but agents act over long horizons with many tools and need purpose-built infrastructure that records how they succeeded, what it cost and where they broke.

## 方法 / Method
<!-- ZH --> **Harness**:scaffold 只需暴露 `run(input) → dict(responses)` 的最小 Python 接口,与基准执行解耦;集成 Weave 做全量日志与成本追踪、LiteLLM 做跨厂商模型调用;支持本地 / Docker / Azure VM 三种执行层;自建 Azure VM 编排层(自动开机、配置、回收,CPU/GPU 分配,信号量并发控制);一条命令从评测直到排行榜更新。工程中修了 Weave 与 LiteLLM 的若干 bug,并发现**厂商会在同一 endpoint 背后悄悄换权重、聚合商(OpenRouter)默认可能提供不同量化版本**。**实验设计**:9 个基准跨四个领域 —— Web 导航(Online Mind2Web、AssistantBench、GAIA)、编码(SWE-bench Verified Mini、USACO)、科学研究(CORE-Bench Hard、ScienceAgentBench、SciCode)、客服(TAU-bench Airline);9 个模型(o3、GPT-4.1、GPT-5、Claude Sonnet 3.7、Opus 4.1、DeepSeek V3/R1、o4-mini、Gemini 2.0 Flash),部分模型做不同 reasoning effort 对比;每个基准用前人的任务专用 scaffold,另有一个基于 smolagents 的**通用 generalist scaffold**用于三个基准;所有基准报告**准确率–成本 Pareto 前沿**(美元与 token 两种)。**日志分析**:用 Docent(LLM 扫描 transcript)按六类 rubric 标注 —— 违反指令、工具调用失败、自我纠错、验证、环境障碍、捷径/刷分;人工抽查 Docent 标记以验证精度。
<!-- EN --> **Harness**: scaffolds expose a minimal `run(input) → dict(responses)` Python API, decoupled from benchmark execution; Weave for full logging and cost tracking, LiteLLM for cross-provider calls; three execution tiers (local / Docker / Azure VMs); a home-built Azure VM orchestration layer (provisioning, configuration, teardown, CPU/GPU allocation, semaphore concurrency); a single command runs everything through to leaderboard updates. Along the way the team fixed bugs in Weave and LiteLLM and found that **providers silently swap weights behind the same endpoint and aggregators (OpenRouter) may serve different quantizations by default**. **Design**: 9 benchmarks in four domains — web navigation (Online Mind2Web, AssistantBench, GAIA), coding (SWE-bench Verified Mini, USACO), scientific research (CORE-Bench Hard, ScienceAgentBench, SciCode) and customer service (TAU-bench Airline); 9 models (o3, GPT-4.1, GPT-5, Claude Sonnet 3.7, Opus 4.1, DeepSeek V3/R1, o4-mini, Gemini 2.0 Flash), some at different reasoning efforts; task-specific scaffolds from prior work per benchmark plus a **generalist scaffold** (smolagents) on three benchmarks; **accuracy–cost Pareto frontiers** (dollars and tokens) for every benchmark. **Log analysis**: Docent (LLM scanning of transcripts) with six rubrics — instruction violations, tool-use failures, self-correction, verification, environmental barriers and shortcuts/gaming — with manual spot checks of Docent's flags for precision.

## 数据 / Data
<!-- ZH --> 21,730 次 agent rollout,超过 25 亿 token 的 LLM 调用日志,全部公开在 HuggingFace;Docent rubric 分析覆盖 AssistantBench、SciCode、CORE-Bench 上 36 个模型–scaffold 组合的 1,634 条 transcript。HAL 是 CORE-Bench Hard 与 ScienceAgentBench 的官方排行榜。
<!-- EN --> 21,730 agent rollouts and over 2.5B tokens of LLM-call logs, all released on HuggingFace; the Docent rubric analysis covers 1,634 transcripts from 36 model–scaffold pairs on AssistantBench, SciCode and CORE-Bench. HAL is the official leaderboard for CORE-Bench Hard and ScienceAgentBench.

## 主要结果 / Key results
<!-- ZH --> **多维结果**:(1) **更高 reasoning effort 不一定更好** —— 36 个「模型–scaffold–基准」组合中 21 个,提高推理强度后准确率持平或下降;(2) Pareto 前沿陡且稀疏:9 个基准中只有 1 个上最贵的模型位于前沿;平均不到三分之一的模型在前沿上;最常在前沿的是 Gemini 2.0 Flash(7/9)、GPT-5(4/9)、o4-mini Low(4/9);(3) 6/9 基准上 token 用量与准确率正相关,推理时扩展尚未带来效率;(4) 按 token 与按美元的 Pareto 图差别很大(Opus 4.1 在 token 前沿出现 3/8 次,在成本前沿只 1 次),而价格波动大(o3 自发布后降价 80%);(5) **scaffold 影响巨大**:Online Mind2Web 上 SeeAct+GPT-5 Medium 花 $171,Browser-Use+Claude Sonnet 4 花 $1,577,成本差 9 倍而准确率只差 2 个百分点;(6) 通用 scaffold 牺牲明显准确率(CORE-Bench Hard 上任务专用 scaffold 12 次中赢 9 次,SWE-bench Verified Mini 12 次中赢 11 次);(7) 基准运行成本差几个数量级(ScienceAgentBench 平均 $13,Online Mind2Web 平均超过 $450)。**日志分析**:agent 常走捷径(8 例直接在 HuggingFace 或 arXiv 找到 gold answer;CORE-Bench、SciCode 上硬编码「看似合理」的解以通过单元测试);出现部署中会造成灾难的动作(用错信用卡订票);最强模型也几乎无法零失败地使用工具;**中途成功纠错的 agent 成功概率高 1.5–4 倍;主动验证(写单元测试、交叉核对搜索结果)的 agent 成功概率高 13%–87%**;AssistantBench 与 CORE-Bench 失败任务中超过 60% 违反了明确指令;约 40% 的失败任务遇到环境障碍;**发现 TAU-bench 官方 few-shot agent 把基准样例混进了 few-shot 数据(数据泄漏)**,只能事后剔除。
<!-- EN --> **Multi-dimensional results**: (1) **higher reasoning effort does not reliably help** — in 21 of 36 model–scaffold–benchmark combinations, more reasoning gave equal or lower accuracy; (2) Pareto frontiers are steep and sparse: in only 1 of 9 benchmarks is the most expensive model on the frontier; on average fewer than a third of models are on it; most frequent are Gemini 2.0 Flash (7/9), GPT-5 (4/9) and o4-mini Low (4/9); (3) on 6/9 benchmarks token usage correlates positively with accuracy — inference-time scaling has not yet yielded efficiency; (4) token-based and dollar-based Pareto views differ sharply (Opus 4.1 is on the token frontier 3/8 times but on the cost frontier once), while prices are volatile (o3 dropped 80%); (5) **scaffolds matter enormously**: on Online Mind2Web, SeeAct + GPT-5 Medium costs $171 vs Browser-Use + Claude Sonnet 4 at $1,577 — 9× cost for a two-point accuracy difference; (6) the generalist scaffold loses substantial accuracy (task-specific wins 9/12 runs on CORE-Bench Hard, 11/12 on SWE-bench Verified Mini); (7) benchmark run costs differ by orders of magnitude (ScienceAgentBench ~$13 vs Online Mind2Web > $450 on average). **Log analysis**: agents take shortcuts (8 cases of finding gold answers on HuggingFace or arXiv; hard-coding "plausible" solutions to pass unit tests on CORE-Bench and SciCode); they take deployment-catastrophic actions (wrong credit card for a booking); even the strongest models rarely finish without a tool-call failure; **agents that self-correct mid-run are 1.5–4× more likely to succeed, and those that explicitly verify (writing unit tests, cross-referencing search results) are 13–87% more likely to succeed**; over 60% of failed AssistantBench and CORE-Bench tasks violate an explicit instruction; ~40% of failed tasks hit an environmental barrier; and **the official TAU-bench few-shot agent leaked benchmark examples into its few-shot data**, discovered only after the runs and excluded.

## 创新点 / Contributions
- <!-- ZH --> 开源、框架无关、可分布式并行的 agent 评测 harness,并系统记录了跨厂商评测中真实遇到的工程陷阱。 <!-- EN --> An open, framework-agnostic, distributed agent-evaluation harness, with a systematic record of real engineering pitfalls in cross-provider evaluation.
- <!-- ZH --> 以成本–准确率 Pareto 前沿而非单一准确率作为排行榜主视图。 <!-- EN --> Cost–accuracy Pareto frontiers rather than single accuracy as the leaderboard's main view.
- <!-- ZH --> 把**日志分析**确立为 agent 评测的必要组成,并公开 25 亿 token 的轨迹数据。 <!-- EN --> Establishes **log analysis** as a necessary part of agent evaluation and releases 2.5B tokens of traces.

## 局限 / Limitations
- <!-- ZH --> 每个配置基本只跑一次,论文主体没有给出 rerun 方差或置信区间;大规模并行使延迟数据不具代表性(作者自承)。 <!-- EN --> Configurations are essentially single-run, with no rerun variance or confidence intervals in the main text; massive parallelism makes latency data unrepresentative (acknowledged).
- <!-- ZH --> 日志分析依赖 Docent 的 LLM 判断,只做了抽样人工核验精度,未报告召回。 <!-- EN --> Log analysis relies on Docent's LLM judgements, validated only by precision spot checks; recall is not reported.
- <!-- ZH --> 领域不全(未含网络安全、零售);科学类基准偏代码复现与数据分析,不含湿实验或组学专属任务。 <!-- EN --> Domain coverage is partial (no cybersecurity or retail); the science benchmarks emphasize code reproduction and data analysis, not wet-lab or omics-specific tasks.
- <!-- ZH --> 成本结论受价格快速变动影响,需要持续维护。 <!-- EN --> Cost conclusions depend on rapidly changing prices and need ongoing maintenance.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 主要服务 **课题 2**。(1) **rerun 稳定性**:HAL 的 harness 正好是做「同一组学分析任务跑 N 次、看结论是否一致」的现成底座 —— 而 HAL 自己恰恰**没做** rerun 方差,这是课题 2 可以补上的明确空白;(2) **claim-to-evidence 验证**:HAL 发现「主动验证的 agent 成功率高 13–87%」「agent 会硬编码看似合理的解」「会去网上找 gold answer」—— 这三条分别对应 verifier 的价值、组学 agent 可能伪造的「看似合理的 DE 结果」、以及组学基准必须隔离公开结论(KPMP / Lake 论文);(3) **日志分析作为基础设施**:Docent 式 rubric(违反指令、工具失败、环境障碍、捷径)可作为组学专属失败分类的起点,再加入「统计误用」「批次混淆」「artifact 当生物学」等组学类别;(4) 「供应商悄悄换权重/量化」直接威胁可复现性,课题 2 的 rerun 协议必须锁定模型版本并记录。对课题 1 关系间接:若用 agent 驱动 KidneyAnomalyBench 上的分析,成本–准确率 Pareto 是比较方案的合适视图。HAL 与 ABC 作者高度重叠(Kapoor、Kang、Zhu、Liang),两篇应配套引用。
<!-- EN --> Mainly serves **Topic 2**. (1) **Rerun stability**: HAL's harness is a ready substrate for "run the same omics-analysis task N times and check whether conclusions agree" — and HAL itself does **not** report rerun variance, a clear gap Topic 2 can fill; (2) **claim-to-evidence verification**: HAL finds that verifying agents succeed 13–87% more often, that agents hard-code plausible-looking solutions, and that they look up gold answers online — respectively the value of a verifier, the risk of omics agents fabricating plausible DE results, and the need to isolate omics benchmarks from published conclusions (KPMP / Lake papers); (3) **log analysis as infrastructure**: Docent-style rubrics (instruction violations, tool failures, environmental barriers, shortcuts) are a starting point for an omics failure taxonomy, extended with categories like statistical misuse, batch confounding, artifact-as-biology; (4) silent weight/quantization swaps by providers threaten reproducibility, so Topic 2's rerun protocol must pin and log model versions. Relation to Topic 1 is indirect: if agents drive analyses on KidneyAnomalyBench, cost–accuracy Pareto is the right comparison view. HAL and ABC share many authors (Kapoor, Kang, Zhu, Liang) and should be cited together.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码:** HAL harness。 <!-- EN --> **Code:** the HAL harness.
<!-- ZH/EN --> <https://github.com/princeton-pli/hal-harness>
- <!-- ZH --> **排行榜:** 全部结果。 <!-- EN --> **Leaderboard:** all results.
<!-- ZH/EN --> <https://hal.cs.princeton.edu>
- <!-- ZH --> **数据:** 全部 agent 轨迹(25 亿 token)。 <!-- EN --> **Data:** all agent traces (2.5B tokens).
<!-- ZH/EN --> <https://huggingface.co/datasets/agent-evals/hal_traces>
- <!-- ZH --> **Rubric:** 附录 Table A5 的 Docent rubric(六类行为)可改写为组学 agent 日志审计表。 <!-- EN --> **Rubrics:** the Docent rubrics in Appendix Table A5 (six behaviour classes) can be adapted into an omics-agent log-audit form.

## 待读 / Follow-ups
- <!-- ZH --> Docent(Meng et al., 2025)与附录 A7 的实现细节。 <!-- EN --> Docent (Meng et al., 2025) and implementation details in Appendix A7.
- <!-- ZH --> CORE-Bench 与 ScienceAgentBench 原文:最接近「科学分析 agent」的两个基准。 <!-- EN --> The CORE-Bench and ScienceAgentBench papers — the two benchmarks closest to "scientific-analysis agents".
- <!-- ZH --> 附录 A4 的局限与维护计划;附录 A5 的 TAU-bench 数据泄漏细节。 <!-- EN --> Appendix A4 (limitations and maintenance plan) and A5 (the TAU-bench leakage details).

## 引用 / Cite
```bibtex
@inproceedings{Kapoor2026_251011977,
  title = {Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation},
  author = {Sayash Kapoor and Benedikt Stroebl and Peter Kirgis and Nitya Nadgir and Zachary S Siegel and Boyi Wei and others},
  booktitle = {International Conference on Learning Representations (ICLR 2026)},
  year = {2026},
  eprint = {2510.11977},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2510.11977}
}
```
<!-- ZH --> (完整 31 位作者见 `citation.bib`。)
<!-- EN --> (Full list of 31 authors in `citation.bib`.)

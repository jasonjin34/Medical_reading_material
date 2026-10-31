# Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation

> **文献键** `Kapoor2026_251011977` · **来源** ICLR 2026(2026) · **类别** agents · **相关度** medium · **获取** open
> **链接** <https://arxiv.org/abs/2510.11977> · `status: complete`

---

## 一句话
HAL(Holistic Agent Leaderboard)是 Princeton 牵头的统一 agent 评测基础设施:标准化 harness 把评测分发到数百台 VM 上并行跑(数周 → 数小时),做「模型 × scaffold × 基准」三维分析(9 个模型、9 个基准、21,730 次 rollout、约 4 万美元),并用 LLM 辅助的日志分析(Docent)揭示准确率看不到的行为 —— 例如去 HuggingFace 搜基准答案、用错信用卡订机票。

## 研究问题
agent 评测面临三组挑战(作者列为 Challenge #1–#8):**基础设施**不统一、慢且易错(单个基准串行跑要数周,排行榜跟不上新模型);**成本**很少被报告,而 scaffold 对准确率与成本影响巨大却少有跨 scaffold 比较;**行为**层面,agent 会走捷径刷分、做出部署中会造成灾难的动作,但现有评测几乎不检测。HELM、LM Evaluation Harness 解决了 LLM 评测的标准化,但 agent 在长时程、多工具环境中运行,需要专门的基础设施记录「怎么做到的、花了多少、在哪里坏掉」。

## 方法
**Harness**:scaffold 只需暴露 `run(input) → dict(responses)` 的最小 Python 接口,与基准执行解耦;集成 Weave 做全量日志与成本追踪、LiteLLM 做跨厂商模型调用;支持本地 / Docker / Azure VM 三种执行层;自建 Azure VM 编排层(自动开机、配置、回收,CPU/GPU 分配,信号量并发控制);一条命令从评测直到排行榜更新。工程中修了 Weave 与 LiteLLM 的若干 bug,并发现**厂商会在同一 endpoint 背后悄悄换权重、聚合商(OpenRouter)默认可能提供不同量化版本**。**实验设计**:9 个基准跨四个领域 —— Web 导航(Online Mind2Web、AssistantBench、GAIA)、编码(SWE-bench Verified Mini、USACO)、科学研究(CORE-Bench Hard、ScienceAgentBench、SciCode)、客服(TAU-bench Airline);9 个模型(o3、GPT-4.1、GPT-5、Claude Sonnet 3.7、Opus 4.1、DeepSeek V3/R1、o4-mini、Gemini 2.0 Flash),部分模型做不同 reasoning effort 对比;每个基准用前人的任务专用 scaffold,另有一个基于 smolagents 的**通用 generalist scaffold**用于三个基准;所有基准报告**准确率–成本 Pareto 前沿**(美元与 token 两种)。**日志分析**:用 Docent(LLM 扫描 transcript)按六类 rubric 标注 —— 违反指令、工具调用失败、自我纠错、验证、环境障碍、捷径/刷分;人工抽查 Docent 标记以验证精度。

## 数据
21,730 次 agent rollout,超过 25 亿 token 的 LLM 调用日志,全部公开在 HuggingFace;Docent rubric 分析覆盖 AssistantBench、SciCode、CORE-Bench 上 36 个模型–scaffold 组合的 1,634 条 transcript。HAL 是 CORE-Bench Hard 与 ScienceAgentBench 的官方排行榜。

## 主要结果
**多维结果**:(1) **更高 reasoning effort 不一定更好** —— 36 个「模型–scaffold–基准」组合中 21 个,提高推理强度后准确率持平或下降;(2) Pareto 前沿陡且稀疏:9 个基准中只有 1 个上最贵的模型位于前沿;平均不到三分之一的模型在前沿上;最常在前沿的是 Gemini 2.0 Flash(7/9)、GPT-5(4/9)、o4-mini Low(4/9);(3) 6/9 基准上 token 用量与准确率正相关,推理时扩展尚未带来效率;(4) 按 token 与按美元的 Pareto 图差别很大(Opus 4.1 在 token 前沿出现 3/8 次,在成本前沿只 1 次),而价格波动大(o3 自发布后降价 80%);(5) **scaffold 影响巨大**:Online Mind2Web 上 SeeAct+GPT-5 Medium 花 $171,Browser-Use+Claude Sonnet 4 花 $1,577,成本差 9 倍而准确率只差 2 个百分点;(6) 通用 scaffold 牺牲明显准确率(CORE-Bench Hard 上任务专用 scaffold 12 次中赢 9 次,SWE-bench Verified Mini 12 次中赢 11 次);(7) 基准运行成本差几个数量级(ScienceAgentBench 平均 $13,Online Mind2Web 平均超过 $450)。**日志分析**:agent 常走捷径(8 例直接在 HuggingFace 或 arXiv 找到 gold answer;CORE-Bench、SciCode 上硬编码「看似合理」的解以通过单元测试);出现部署中会造成灾难的动作(用错信用卡订票);最强模型也几乎无法零失败地使用工具;**中途成功纠错的 agent 成功概率高 1.5–4 倍;主动验证(写单元测试、交叉核对搜索结果)的 agent 成功概率高 13%–87%**;AssistantBench 与 CORE-Bench 失败任务中超过 60% 违反了明确指令;约 40% 的失败任务遇到环境障碍;**发现 TAU-bench 官方 few-shot agent 把基准样例混进了 few-shot 数据(数据泄漏)**,只能事后剔除。

## 创新点
- 开源、框架无关、可分布式并行的 agent 评测 harness,并系统记录了跨厂商评测中真实遇到的工程陷阱。
- 以成本–准确率 Pareto 前沿而非单一准确率作为排行榜主视图。
- 把**日志分析**确立为 agent 评测的必要组成,并公开 25 亿 token 的轨迹数据。

## 局限
- 每个配置基本只跑一次,论文主体没有给出 rerun 方差或置信区间;大规模并行使延迟数据不具代表性(作者自承)。
- 日志分析依赖 Docent 的 LLM 判断,只做了抽样人工核验精度,未报告召回。
- 领域不全(未含网络安全、零售);科学类基准偏代码复现与数据分析,不含湿实验或组学专属任务。
- 成本结论受价格快速变动影响,需要持续维护。

## 与本研究方向的关系
主要服务 **Agent 可信度课题**。(1) **rerun 稳定性**:HAL 的 harness 正好是做「同一组学分析任务跑 N 次、看结论是否一致」的现成底座 —— 而 HAL 自己恰恰**没做** rerun 方差,这是 Agent 可信度课题可以补上的明确空白;(2) **claim-to-evidence 验证**:HAL 发现「主动验证的 agent 成功率高 13–87%」「agent 会硬编码看似合理的解」「会去网上找 gold answer」—— 这三条分别对应 verifier 的价值、组学 agent 可能伪造的「看似合理的 DE 结果」、以及组学基准必须隔离公开结论(KPMP / Lake 论文);(3) **日志分析作为基础设施**:Docent 式 rubric(违反指令、工具失败、环境障碍、捷径)可作为组学专属失败分类的起点,再加入「统计误用」「批次混淆」「artifact 当生物学」等组学类别;(4) 「供应商悄悄换权重/量化」直接威胁可复现性,Agent 可信度课题的 rerun 协议必须锁定模型版本并记录。对伪影注入课题关系间接:若用 agent 驱动 KidneyAnomalyBench 上的分析,成本–准确率 Pareto 是比较方案的合适视图。HAL 与 ABC 作者高度重叠(Kapoor、Kang、Zhu、Liang),两篇应配套引用。

## 可复用资产
- **代码:** HAL harness。
<https://github.com/princeton-pli/hal-harness>
- **排行榜:** 全部结果。
<https://hal.cs.princeton.edu>
- **数据:** 全部 agent 轨迹(25 亿 token)。
<https://huggingface.co/datasets/agent-evals/hal_traces>
- **Rubric:** 附录 Table A5 的 Docent rubric(六类行为)可改写为组学 agent 日志审计表。

## 待读
- Docent(Meng et al., 2025)与附录 A7 的实现细节。
- CORE-Bench 与 ScienceAgentBench 原文:最接近「科学分析 agent」的两个基准。
- 附录 A4 的局限与维护计划;附录 A5 的 TAU-bench 数据泄漏细节。

## 引用
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
(完整 31 位作者见 `citation.bib`。)


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

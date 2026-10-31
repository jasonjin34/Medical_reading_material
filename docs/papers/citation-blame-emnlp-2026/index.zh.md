# Who is the Agent to Blame? Localizing Faithfulness and Citation Mistakes in Agentic Deep Research

> **文献键** `Hirsch2026_260824306` · **来源** EMNLP 2026(2026) · **类别** agents · **相关度** high · **获取** open
> **链接** <https://arxiv.org/abs/2608.24306> · `status: complete`

---

## 一句话
多智能体 deep research(DR)系统里,信息像「传话游戏」一样逐层传递,内容和引用都会在途中被损坏。本文提出**局部测试每一次 agent 调用相对其自身输入的忠实性与可验证性**,从而把最终报告里的每个引用错误**追溯到引入它的那个 agent**,并按四类分型(幻觉、依赖未引用输入、输出无引用、引用不足);在 Nvidia AI-Q 上 84.7% 的最终报告错误源自 orchestrator,据此做的两个简单干预使引用召回率提升约 5 个百分点且不损失质量。

## 研究问题
引用是评估 DR 报告真实性的主要机制,标准指标是 citation recall(被引来源支持的 claim 比例),而现有 DR 系统的 citation recall 很差。传统评估是**全局**的:拿最终报告句子对照所有源文档,只能告诉你「错了」,不能告诉你「谁错了、错在哪类」。DR 系统由 searcher、researcher、orchestrator 等多个 agent 组成,信息跨越 agent 边界时常被压缩,开发者缺少定位故障组件的工具。

## 方法
**单次 agent 调用评估**(核心构件):抽取该调用收到的全部输入和产出的全部输出;假设输入本身忠实且已被其引用支持,只问该 agent 是否「忠实于**有引用的**输入并完整携带引用」。对合成输出逐句跑五步(全为 attribution / entailment 测试):**Step 1 忠实性** —— LLM 从输入中抽取支持目标句的 span(要求逐字出现、并集须蕴含目标句,失败带 self-critique 重试),若不能完全支持 → **hallucination**;**Step 2–3** —— 识别每个输入 span 的引用,去掉无引用的 span 后若不再蕴含 → **uncited input reliance**;**Step 4–5** —— 识别目标句自身的引用,若没有 → **uncited output**;若有,只保留引用是目标句引用子集的 span 再测蕴含,不支持 → **insufficient citations**;否则正确。对抽取式 snippet 只做一次「源文档是否支持整段 snippet」测试(失败 → snippet missing context)。Prompt 均改自已有工作(LAQuer 的 span 抽取、DEER 的引用识别、LongCite 的蕴含与「是否需要引用」),judge 为 gpt-5-mini-2025-08-07。**两级评估**:(a) agent 级 —— 每个 agent 类型抽样句子统计错误率与错误分布;(b) 系统级 —— 先在最终报告上算全局 citation recall,对有错的句子从 orchestrator 开始**递归**:本地测试发现错误则归咎于该 agent,否则沿支持 span 回溯到产生它的上游调用,直到找到错误或到达原始文档。用 tracing 日志构建已检索 URL 真值表过滤幻觉 URL,并从日志中取原文(no-crawl),避开重爬不一致。**人工验证**:50 句,双人标注 + 第三人仲裁,标注者间 κ = 0.71;方法 vs 仲裁标签 76% 完全一致,κ = 0.62;支持 span 定位与人工一致 75%。

## 数据
系统:DeepResearch Bench 开源榜(2026 年 5 月)前三 —— **Nvidia AI-Q**(planner 与 orchestrator 用前沿模型,researcher 用小型开源模型)、**MS-Agent**(按深度分配模型:searcher GPT-5 nano → reporter GPT-5 mini → orchestrator GPT-5)、**TrajectoryKit**(全程 gpt-oss-20b)。agent 级与系统级分析用 DeepResearch Bench 的 20 个例子,每 agent 每例最多 10 句,约每 agent 200 句;干预实验用全部 50 个英文查询,报告 RACE 质量分、citation recall 与 citation precision。只评估正文句子,表格内容排除。

## 主要结果
**Agent 级错误率(Table 1)**:AI-Q —— orchestrator 30.9%、planner 22.0%、researcher **70.8%**、searcher 合成摘要 62.0%、searcher snippet **3.8%**;MS-Agent —— orchestrator 16.8%、reporter 61.6%、researcher 46.6%、searcher 合成 0.9%、snippet 6.4%;TrajectoryKit —— orchestrator **92.5%**、researcher 50.0%、searcher 合成 14.9%。**只摘要单篇文档的 agent 错误最少**;AI-Q searcher 对一次查询的全部文档做摘要时错误率升到 62.0%;同样是单文档摘要,gpt-oss-20b(14.9%)比 MS-Agent(0.9%)差一个数量级。**越深的 agent 越少幻觉**:AI-Q orchestrator 的错误中幻觉占 31%,researcher 占 79%;MS-Agent orchestrator 0%,reporter 78%,researcher 92% —— 作者认为主要是因为深层 agent 用了更强的模型(观察性结论);TrajectoryKit 全程同一小模型,各层均以幻觉为主。**系统级**:全局 citation recall AI-Q 58.7%、MS-Agent 28.5%、TrajectoryKit 7.1%;最终报告错误归因 —— AI-Q orchestrator **84.7%** / researcher 14.8% / searcher 0.4%;MS-Agent orchestrator 52.6% / reporter 47.4%;TrajectoryKit orchestrator 100%。orchestrator 的 agent 级错误率在 AI-Q 和 MS-Agent 里是最低之一,却是最终错误的主要来源 —— 说明系统级评估不可替代。最终错误多为引用类(AI-Q orchestrator 70%、MS-Agent 99%);AI-Q 约 31% 是幻觉;TrajectoryKit **95% 是幻觉**,典型是 orchestrator 给某来源安上一个它并未陈述的精确统计数字,尽管其 RACE 质量与 MS-Agent 相当。错误传播案例:searcher 编造 → researcher 与 orchestrator 忠实转述;未被支持的统计数字带着从不支持它的引用原样传递。**干预(AI-Q,50 例)**:RACE 52.6 不变;citation recall 64.5 → **69.7**(用原始 snippet 替换 researcher 笔记)/ **69.6**(orchestrator prompt 加一句「不要使用没有引用支持的信息」);citation precision 87.6 → 94.1 / 91.0。引导后 orchestrator 的错误占比 84.7% → 77.0%,其引用类错误 70% → 60%。

## 创新点
- **局部(per-invocation)测试**替代全局引用评估:可把错误归咎到具体 agent,且只需对照该 agent 的输入,比对照上百篇源文档更可行。
- 跨 agent 边界的**四类错误分型**(+ snippet 缺上下文),把「幻觉」与「引用簿记错误」分开。
- agent 级(单元测试)与系统级(递归溯源)两级互补的诊断。
- 证明诊断可直接转化为有效修复(一句 prompt 即提升引用召回约 5 个百分点)。

## 局限
- 依赖 LLM-as-judge(gpt-5-mini);人工验证仅 50 句,方法与人类 κ = 0.62,并非完美。
- 「错误类型由模型能力决定」是观察性结论,未做同一模型跨角色的对照实验。
- 只评估正文句子,表格中的数字与引用被排除 —— 而数字恰是科学报告中最容易被编造的内容。
- 假设每个 agent 的输入本身忠实;只验证「是否忠实于输入」,不验证源文档本身是否正确。
- 只在通用 web DR(DeepResearch Bench)上评估,样本较小(20 例诊断、50 例干预),无生物医学领域。

## 与本研究方向的关系
这是 **Agent 可信度课题** 方法论上最直接可借用的论文之一。**(1) 局部验证 + 递归溯源**的思路可以几乎原样迁移到「分析肾脏 omics 的 agent」:把 agent 流水线拆成调用(载入数据 → QC → 聚类/注释 → 差异分析 → 文献解读 → 报告),每一步的 claim 只对照**该步的输入**(数据表、上一步输出、检索到的文献)做 claim-to-evidence 检查,最终报告中的错误结论即可归咎到具体步骤 —— 这正是 omics 专用 failure taxonomy 所需的「错误发生在哪一层」维度。**(2) 四类分型**可扩展为 omics 版本:除了文本幻觉/引用簿记错误,还要加「数值与所跑代码输出不一致」「结论依赖未经 QC 的数据(类比 uncited input reliance)」「跨模态矛盾被忽略」。**(3)** 它最引人注意的发现 —— 小模型系统 95% 的错误是**给来源安上编造的精确统计数字**,而它恰恰**排除了表格中的数字** —— 正是我们在 omics 场景必须补的:数字型 claim(p 值、细胞比例、log2FC)要对照实际计算结果核验。**(4)** 它的 judge 未做校准、无覆盖保证;Agent 可信度课题的 calibrated verifier(如 citation-faithfulness-arxiv-2026 的 split-conformal guard)可以叠加在这套定位框架上。与伪影注入课题关系较远,但对 detect → model → revert 末端「向湿实验提名基因」时的证据链可审计性直接相关。

## 可复用资产
- **代码:**
<https://github.com/eranhirs/who-is-the-agent-to-blame>
- **算法:** 五步局部验证(附录 A 伪代码)、递归溯源、全部 prompt(附录 B)、标注指南(附录 E)。
- **工程技巧:** 用 tracing 日志构建检索 URL 真值表过滤幻觉 URL;no-crawl 取原文。
- **被评测系统:** Nvidia AI-Q、MS-Agent、TrajectoryKit(均开源)。

## 待读
- DeepResearch Bench(Du et al.)及 DeepResearch Bench II、DEER(arXiv 2512.17776)、LongCite、LAQuer。
- "LLMs corrupt your documents when you delegate"(Laban et al. 2026,arXiv 2604.15597)—— 传话游戏现象的另一证据。
- 与 citation-faithfulness-arxiv-2026 对照:后者指出 verifier 本身严格度会让未支持引用率在 3%–18% 间变化 —— 本文的定位结论对 judge 选择有多敏感?

## 引用
```bibtex
@misc{Hirsch2026_260824306,
  title = {Who is the Agent to Blame? Localizing Faithfulness and Citation Mistakes in Agentic Deep Research},
  author = {Eran Hirsch and David Wan and Han Wang and Elias Stengel-Eskin and Mohit Bansal and Ido Dagan},
  year = {2026},
  eprint = {2608.24306},
  archivePrefix = {arXiv},
  note = {Accepted to EMNLP 2026 (Main Conference)},
  url = {https://arxiv.org/abs/2608.24306}
}
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

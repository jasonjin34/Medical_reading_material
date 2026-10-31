# The Ideation-Execution Gap: Execution Outcomes of LLM-Generated versus Human Research Ideas

> **Bibkey** `ideation-execution-gap-arxiv-2025` · **Venue** arXiv preprint (2025) · **Category** agents · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2506.20803>
> `status: complete` — 全文精读(arXiv HTML + PDF 中的表 4/5 数值)。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> Si 等人此前发现 LLM 生成的 NLP 研究 idea 被专家评为比人类 idea 更新颖;这篇做了预注册的盲法随机对照**执行研究**:43 位专家各花 100 小时左右把随机分配的 idea 做成 4 页论文,再由 58 位评审盲审 —— 执行后 LLM idea 的分数在所有指标上下降显著更多,排名甚至翻转,即「ideation-execution gap」。
<!-- EN --> Si et al. had found LLM-generated NLP research ideas rated more novel than human-expert ideas; this pre-registered, blinded RCT **execution study** has 43 experts each spend ~100 hours turning a randomly assigned idea into a 4-page paper, blind-reviewed by 58 reviewers — after execution, LLM ideas' scores fall significantly more on every metric and the ranking even flips: the "ideation-execution gap".

## 研究问题 / Problem
<!-- ZH --> 一个好 idea 不应只是「看起来新颖」,还应在执行后产出更好的研究。此前 LLM idea 的评估几乎都停在 idea 本身(LLM 评委或小规模人评),执行验证最多一两个案例,无法得出统计结论。问题:LLM idea 执行后是否仍优于人类 idea?ideation 阶段的评估能否预测执行结果?
<!-- EN --> A good idea should not merely appear novel; it should yield better research when executed. Prior evaluation of LLM ideas stopped at the idea (LLM judges or small human studies), with at most one or two executed cases — no statistical conclusions. Do LLM ideas still beat human ideas after execution? Does ideation-stage evaluation predict execution outcomes?

## 方法 / Method
<!-- ZH --> 预注册(OSF)的盲法 RCT,沿用 Si et al. (2025) ideation 研究中的 idea 及其执行前评分。每位执行者先选偏好主题(7 个 NLP 主题:Bias、Coding、Safety、Multilingual、Factuality、Math、Uncertainty),再在主题内**随机**分配一个匿名 idea,来源为人类专家或基于 Claude-3.5-Sonnet 的 LLM agent。三个月期限,需实现全部实验、提交可复现代码库和 ≥4 页 ACL 格式论文。规则:不允许实质性改动方法,只允许改实验细节(数据集、基线、模型、超参等),所有改动需申报并人工审核。执行后由专家评审对代码 + 论文盲审,评 novelty、excitement、soundness、effectiveness、overall,外加 faithfulness 与 codebase quality 两个控制指标。核心度量是「执行后分数 − 执行前分数」的差(gap),用来抵消 idea 质量本身的高异质性。
<!-- EN --> Pre-registered (OSF) blinded RCT reusing the ideas and pre-execution scores from Si et al.'s (2025) ideation study. Each executor states preferred topics among seven NLP topics (Bias, Coding, Safety, Multilingual, Factuality, Math, Uncertainty) and is **randomly** assigned an anonymised idea within them, sourced either from a human expert or a Claude-3.5-Sonnet-based LLM agent. Three months to implement all experiments and submit a reproducible codebase plus a ≥4-page ACL-format paper. Rule: no substantive change to the method, only to experimental details (datasets, baselines, models, hyper-parameters), all changes declared and manually reviewed. Expert reviewers then blind-review code + paper on novelty, excitement, soundness, effectiveness, overall, plus faithfulness and codebase quality as controls. The key measure is the gap "post-execution score − pre-execution score", which removes the high heterogeneity in idea quality.

## 数据 / Data
<!-- ZH --> 66 人入组、43 人完成(人类 idea 19 个、AI idea 24 个);执行者平均 15.3 / 14.3 篇论文,平均用时 112.6 / 93.7 小时;58 位评审写了 181 份评审(每个项目 4–5 份),评审平均被引 596.8 次,每份平均 52.5 分钟;参与者来自 40 个机构。只有一个项目因 idea 过于模糊被终止并排除。Stanford IRB 批准。
<!-- EN --> 66 onboarded, 43 completed (19 human ideas, 24 AI ideas); executors average 15.3 / 14.3 papers and 112.6 / 93.7 hours; 58 reviewers wrote 181 reviews (4–5 per project), averaging 596.8 citations and 52.5 minutes per review; participants from 40 institutions. One project was terminated and excluded because the idea was too vague. Stanford IRB approved.

## 主要结果 / Key results
<!-- ZH -->
- **执行前**(按 idea 平均,人类 N=19 / AI N=24):AI idea 在四项上均显著更高 —— novelty 5.778 vs 4.912、excitement 5.653 vs 4.404、effectiveness 6.003 vs 4.833、overall 5.382 vs 4.596(FDR p = 0.035 / 0.004 / 0.001 / 0.035)。
- **执行后**:AI 4.729 / 3.896 / 4.125 / 3.406,人类 4.903 / 4.482 / 4.782 / 3.968 —— **排名翻转**,但按 idea 计差异不显著(p 0.175–0.586)。按评审计(N=181)时,人类在 excitement、effectiveness、soundness、overall 上显著更高,novelty 不显著。
- **Gap(核心结果)**:人类 idea 几乎不掉分(novelty −0.010、excitement +0.078、effectiveness −0.052、overall −0.628);AI idea 大幅下降(−1.049、−1.760、−1.879、−1.976);人类−AI 差 1.039 / 1.835 / 1.827 / 1.348,FDR p = 0.025 / 0.001 / 0.003 / 0.004。
- **控制指标相同**:faithfulness(6.48 vs 6.42)与代码质量(3.58 vs 3.58)无差别,说明两组执行质量相当。
- **ideation 分与执行分弱相关**;AI idea 的 excitement 甚至中度负相关。
- **为何掉分**:改动都集中在实验细节(人类平均 2.9 处、AI 3.1 处);一个特殊来源是 AI idea 爱提议大规模人工评测,6 个 AI idea 被执行者改成 LLM-as-judge —— 但剔除这 6 个后结论不变。主要原因是执行评审考虑的因素更多:实证表现、实验严谨性、缺失基线与消融、资源开销、可推广性,这些在 ideation 阶段几乎被忽略,ideation 评审常常「假设实验会成功」。
<!-- EN -->
- **Pre-execution** (per-idea means, human N=19 / AI N=24): AI ideas score significantly higher on all four — novelty 5.778 vs 4.912, excitement 5.653 vs 4.404, effectiveness 6.003 vs 4.833, overall 5.382 vs 4.596 (FDR p = 0.035 / 0.004 / 0.001 / 0.035).
- **Post-execution**: AI 4.729 / 3.896 / 4.125 / 3.406 vs human 4.903 / 4.482 / 4.782 / 3.968 — **the ranking flips**, though not significantly per idea (p 0.175–0.586). Per review (N=181), human ideas are significantly higher on excitement, effectiveness, soundness and overall, but not novelty.
- **The gap (headline)**: human ideas barely move (novelty −0.010, excitement +0.078, effectiveness −0.052, overall −0.628); AI ideas drop sharply (−1.049, −1.760, −1.879, −1.976); human−AI difference 1.039 / 1.835 / 1.827 / 1.348, FDR p = 0.025 / 0.001 / 0.003 / 0.004.
- **Controls match**: faithfulness (6.48 vs 6.42) and codebase quality (3.58 vs 3.58) are equal, so execution quality is comparable.
- **Ideation and execution scores correlate weakly**; for AI ideas excitement is even moderately negatively correlated.
- **Why scores drop**: changes concentrate on experimental details (2.9 per human idea, 3.1 per AI idea); one AI-specific source is proposing large human evaluations, which executors replaced with LLM-as-judge in 6 AI ideas — but excluding those 6 leaves conclusions unchanged. The main reason is that execution reviews weigh more factors — empirical performance, rigour, missing baselines/ablations, resource cost, generalisability — that ideation reviews largely ignore, often "assuming the experiments work".

## 创新点 / Contributions
- <!-- ZH --> 首个规模足以得出统计显著结论的 LLM idea **执行**研究(43 个项目、>4,000 小时专家劳动)。 <!-- EN --> First execution study of LLM ideas large enough for statistically significant conclusions (43 projects, >4,000 expert hours).
- <!-- ZH --> 预注册、随机分配、双盲的 RCT 设计,配合「不改方法只改实验细节」的规则与改动审计。 <!-- EN --> Pre-registered, randomised, blinded RCT with a "change details, not the method" rule and audited changes.
- <!-- ZH --> 用「执行前后分数差」控制 idea 异质性,揭示 ideation 评估无法预测执行结果。 <!-- EN --> Uses the pre/post score difference to control idea heterogeneity, showing ideation evaluation fails to predict execution outcomes.

## 局限 / Limitations
- <!-- ZH --> idea 范围被限定在三个月可完成的 NLP prompting 类方法,对需要复杂建模、大规模数据采集或训练的研究以及 AI 以外学科的推广性未知。 <!-- EN --> Ideas are restricted to three-month NLP prompting methods; generalisation to research requiring complex modelling, large data collection or training, or to non-AI fields, is unknown.
- <!-- ZH --> 样本量有限(19 vs 24),按 idea 计的直接比较统计功效不足;个别执行者差异影响大。 <!-- EN --> Modest sample (19 vs 24); per-idea direct comparisons are underpowered and sensitive to individual executors.
- <!-- ZH --> 执行由人完成而非 agent;LLM idea 来自 2024 年的 Claude-3.5-Sonnet agent,更新模型未测。 <!-- EN --> Execution is human, not agentic; LLM ideas come from a 2024 Claude-3.5-Sonnet agent — newer models untested.
- <!-- ZH --> 评审为招募的付费评审,而非真实会议评审。 <!-- EN --> Reviewers are recruited and paid rather than real conference reviewers.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 对我们最核心的启示是:**「看起来好」的提名在执行(湿实验)前不可信**。detect → model → revert 的最后一步正是「预测哪些基因/扰动能回正异常」并送湿实验验证 —— 本文用 NLP 场景量化了这一步的风险:AI 产出的想法在纸面评估中占优,但执行后优势消失甚至反转,且纸面评分与执行结果弱相关、AI 的 excitement 甚至负相关。对 **Agent 可信度课题**:(1) 评估分析肾脏组学的 agent 时,不能只看 agent 报告或 LLM/专家对报告的打分,必须有「执行后」的可验证信号 —— 计算层面是重跑与数据回溯(claim-to-evidence),湿实验层面是 revert 预测的实验结果;(2) 「执行前后分数差」这种自身对照设计,可以借用来度量 agent 结论在验证前后的可信度落差;(3) AI idea 偏好「宏大但不可行」的人工评测这一发现,对应 Agent 可信度课题失败分类中「不可执行/资源不现实的分析计划」一类。伪影注入课题关系较弱。
<!-- EN --> The core lesson for us: **"looks good" nominations are untrustworthy before execution (the wet lab)**. The last step of detect → model → revert is exactly "predict which genes/perturbations revert the anomaly" and send them to wet-lab validation — this paper quantifies that step's risk in an NLP setting: AI ideas win on paper, but the advantage vanishes or reverses after execution, paper scores correlate weakly with execution outcomes, and AI excitement even correlates negatively. For **the agent-trustworthiness topic**: (1) evaluating agents that analyse kidney omics cannot rely only on agent reports or LLM/expert scores of those reports — there must be post-execution, verifiable signals: re-running and tracing back to data computationally (claim-to-evidence), and wet-lab outcomes for revert predictions; (2) the pre/post self-controlled difference can be reused to measure how much an agent conclusion's credibility drops between claim and verification; (3) AI ideas' preference for grand but infeasible human evaluations maps to an agent-trustworthiness-topic failure-taxonomy class: "infeasible / resource-unrealistic analysis plans". Relation to the artifact-injection topic is weak.

## 可复用资产 / Reusable assets
- <!-- ZH --> **数据:** 全部 idea、执行项目、评审数据。 <!-- EN --> **Data:** all ideas, executed projects and reviews.
<!-- ZH/EN --> <https://github.com/NoviScl/AI-Researcher>
- <!-- ZH --> **预注册方案:** <!-- EN --> **Pre-registration:**
<!-- ZH/EN --> <https://osf.io/ckxtp>
- <!-- ZH --> **评审表**(附录 A)与「改动类型」分类(数据集/指标/人评→自动评/模型/超参/基线/分析/prompt)。 <!-- EN --> **Review form** (Appendix A) and the change-type taxonomy (dataset / metric / human→auto eval / model / hyper-parameters / baseline / analysis / prompt).

## 待读 / Follow-ups
- <!-- ZH --> Si et al. (2025) 原 ideation 研究(「Can LLMs generate novel research ideas?」)。 <!-- EN --> The original Si et al. (2025) ideation study ("Can LLMs generate novel research ideas?").
- <!-- ZH --> 作者提出的未来方向:自动执行 agent、用历史执行结果训练 proxy reward model、执行反馈闭环。 <!-- EN --> The authors' proposed directions: automated execution agents, proxy reward models trained on historical execution outcomes, and execution-feedback loops.
- <!-- ZH --> `robin-nature-2026`、`co-scientist-nature-2026`:带湿实验验证的生物医学 AI scientist。 <!-- EN --> `robin-nature-2026`, `co-scientist-nature-2026` — biomedical AI scientists with wet-lab validation.

## 引用 / Cite
```bibtex
@misc{ideation-execution-gap-arxiv-2025, title={The Ideation-Execution Gap: Execution Outcomes of LLM-Generated versus Human Research Ideas}, author={Si, Chenglei and Hashimoto, Tatsunori and Yang, Diyi}, year={2025}, eprint={2506.20803}, archivePrefix={arXiv}, primaryClass={cs.CL}, url={https://arxiv.org/abs/2506.20803}, doi={10.48550/arXiv.2506.20803} }
```

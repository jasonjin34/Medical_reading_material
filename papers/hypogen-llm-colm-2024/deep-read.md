# Large Language Models as Biomedical Hypothesis Generators: A Comprehensive Evaluation

> **Bibkey** `Qi_2024` · **Venue** COLM 2024 (2024) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2407.08940>
> `status: complete` — 基于 arXiv 全文(v2,COLM 2024 camera-ready,扩展自 arXiv:2311.05965)精读;附录(数据分布、逐模型数值表、case study)未逐项精读,部分图中数值(Fig. 3/4/6b)只能读出趋势。PI 推荐。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> 用**按发表时间切分**(2023 年 1 月前 = 训练/seen,2023 年 8 月 = unseen)的生物医学「背景知识 → 假设」配对数据集,系统评测 LLM 在 zero-shot / few-shot / 微调 / 工具调用 / 多智能体设置下的假设生成能力,提出 Novelty、Relevance、Significance、Verifiability 四维评分(GPT-4 打分并与人类专家对齐),发现 LLM 在未见文献上也能提出新颖且后来被验证的假设,而"不确定性"(SelfBLEU 衡量)在新颖性与可验证性之间形成权衡。
<!-- EN --> Using a biomedical background → hypothesis dataset **split by publication date** (pre-Jan-2023 = train/seen, Aug-2023 = unseen), the paper systematically evaluates LLM hypothesis generation in zero-shot, few-shot, fine-tuned, tool-use and multi-agent settings, introduces four rubric metrics (Novelty, Relevance, Significance, Verifiability; scored by GPT-4 and checked against human experts), and finds LLMs can propose novel, later-validated hypotheses even on unseen literature — with "uncertainty" (measured by SelfBLEU) trading novelty against verifiability.

## 研究问题 / Problem
<!-- ZH --> 用 LLM 做科学假设生成的工作越来越多,但几乎都无法保证**测试数据未被模型训练见过**(训练语料不可追溯),因此无法判断模型是在"发现"还是在"背诵"。另外,假设本身没有唯一正确答案,BLEU/ROUGE 这类重叠指标不足以评价质量。作者要回答:LLM 能否真正 zero-shot 地提出假设?外部知识(few-shot、领域适配、指令微调、工具检索)与多智能体协作是帮忙还是添乱?
<!-- EN --> Work on LLM hypothesis generation cannot usually guarantee that **test data was unseen in training** (training corpora are untraceable), so "discovery" cannot be told from "recall". Moreover, hypotheses have no single correct answer, so overlap metrics like BLEU/ROUGE are insufficient. The questions: can LLMs truly generate hypotheses zero-shot, and do external knowledge (few-shot, domain adaptation, instruction tuning, tool retrieval) and multi-agent collaboration help or hurt?

## 方法 / Method
<!-- ZH --> **任务形式化**:给定指令 I 与从论文抽取的背景知识 X,让模型生成假设 Y,作为文本补全任务。**数据构建**(仿 Self-Instruct 流程):按主题组织 PubMed 论文集 → 用 ChatGPT/GPT-4 总结文献 → 生成「背景–假设」对 → 过滤低质量数据 → 按发表时间切分。**评测模型**:仅选训练语料截止于 2023 年 3 月前的模型以避免污染 —— gpt-3.5-turbo;Alpaca Eval 榜单上的通用指令模型(Vicuna-33B、Llama-2-70B-chat、WizardLM-13B/70B、Openchat-v3.2-super);医学领域模型 PMC-LLaMA-13B、MedAlpaca-13B;并在训练集上微调 WizardLM-13B-V1.2。**提示**:zero-shot、5-shot 随机采样、5-shot 相似度检索(记为 5-shot*)。**指标**:有 ground truth 时用 BLEU/ROUGE;无 ground truth 时用 GPT-4 按四个维度 0–3 打分并给出逐步理由;用 **SelfBLEU** 作为生成集合"不确定性/多样性"的廉价代理(越低越多样)。**多智能体框架**:Analyst(抽取关键词/主题)→ Engineer(用 PubMed 检索,并过滤 2023 年 1 月后的文献以保持 unseen)→ Scientist(综合提出假设)→ Critic(评估并反馈,可回环),可选人类介入;工具调用对比 ReAct 与 OpenAI function calling。
<!-- EN --> **Task**: given instruction I and background knowledge X extracted from a paper, generate hypothesis Y — framed as text completion. **Data** (Self-Instruct-style pipeline): compose topic-based PubMed paper sets → summarize with ChatGPT/GPT-4 → generate background–hypothesis pairs → filter low quality → split by publication date. **Models**: only those trained on corpora before March 2023 — gpt-3.5-turbo; general instruction models from the Alpaca Eval leaderboard (Vicuna-33B, Llama-2-70B-chat, WizardLM-13B/70B, Openchat-v3.2-super); medical models PMC-LLaMA-13B and MedAlpaca-13B; plus WizardLM-13B-V1.2 fine-tuned on the training pairs. **Prompts**: zero-shot, 5-shot random, 5-shot similarity-retrieved (5-shot*). **Metrics**: BLEU/ROUGE against gold; without gold, GPT-4 scores four dimensions on 0–3 with step-by-step justifications; **SelfBLEU** as a cheap proxy for uncertainty/diversity of generations (lower = more diverse). **Multi-agent framework**: Analyst (keywords/topics) → Engineer (PubMed search, filtering out literature after Jan 2023 to keep the test unseen) → Scientist (formulates hypotheses) → Critic (evaluates, loops back), optional human-in-the-loop; tool use compared via ReAct vs OpenAI function calling.

## 数据 / Data
<!-- ZH --> **Seen 数据集**:2,700 对(2023 年 1 月前文献),分为训练 2,500 与验证/seen 测试 200;**Unseen 数据集**:200 对,来自 2023 年 8 月发表的论文。起点是约 10,000 篇 PubMed 医学论文(Fig. 2b)。人类评估:3 位生物医学专家对 unseen 测试集中 100 个样本打分。数据与代码开源。
<!-- EN --> **Seen**: 2,700 pairs (literature before Jan 2023), split into 2,500 train and 200 validation/seen-test; **Unseen**: 200 pairs from papers published in Aug 2023. Source pool of ~10,000 PubMed medical papers (Fig. 2b). Human evaluation: three biomedical experts score 100 unseen-test examples. Data and code released.

## 主要结果 / Key results
- <!-- ZH --> **Zero-shot 更新颖,few-shot 更可验证**:几乎所有模型(尤其 WizardLM 系列与 Openchat-v3.2-super)在 zero-shot 下 Novelty 更高,而 few-shot(尤其检索式 5-shot*)提高 Verifiability 与 BLEU/ROUGE、但降低新颖性 —— 一个明确的 novelty–verifiability 权衡。 <!-- EN --> **Zero-shot is more novel, few-shot more verifiable**: nearly all models (notably WizardLM and Openchat-v3.2-super) score higher Novelty zero-shot, while few-shot (especially retrieval-based 5-shot*) raises Verifiability and BLEU/ROUGE but lowers novelty — an explicit novelty–verifiability trade-off.
- <!-- ZH --> **Unseen 反而更好**:与"seen 集靠记忆会更好"的预期相反,模型在 unseen 测试集上 BLEU 更高;作者推测假设生成的复杂性妨碍模型利用参数化的 "dark knowledge"。 <!-- EN --> **Better on unseen**: contrary to the memorization expectation, models score higher BLEU on the unseen split; the authors speculate the task's complexity hinders use of parametric "dark knowledge".
- <!-- ZH --> **外部知识不总有益**:领域适配(PMC-LLaMA、MedAlpaca)提升重叠指标与 few-shot 利用,但削弱 zero-shot 能力;指令微调提升记忆、BLEU/ROUGE 与可验证性,但降低新颖性与重要性(微调 WizardLM-13B 的人评 Novelty 仅 0.85)。 <!-- EN --> **External knowledge is not always helpful**: domain adaptation (PMC-LLaMA, MedAlpaca) improves overlap and few-shot use but weakens zero-shot ability; instruction tuning improves retention, BLEU/ROUGE and verifiability but reduces novelty and significance (fine-tuned WizardLM-13B human Novelty only 0.85).
- <!-- ZH --> **不确定性分析**:zero-shot 生成 SelfBLEU 更低(更不确定)且 Novelty 更高;few-shot 不确定性更低、Verifiability 更高。 <!-- EN --> **Uncertainty**: zero-shot generations have lower SelfBLEU (more uncertain) and higher Novelty; few-shot has lower uncertainty and higher Verifiability.
- <!-- ZH --> **人类评估(Table 1)**:GPT-4 平均分与人类平均分高度相关(Pearson 0.73–0.97,Spearman 0.73–0.94,均 > 0.7);人评平均最高为 Llama-2-70b-chat 5-shot(2.33),gpt-3.5-turbo 0-shot 为 2.02。 <!-- EN --> **Human evaluation (Table 1)**: GPT-4 and human average scores correlate strongly (Pearson 0.73–0.97, Spearman 0.73–0.94, all > 0.7); best human average is Llama-2-70b-chat 5-shot (2.33), gpt-3.5-turbo 0-shot 2.02.
- <!-- ZH --> **工具与多智能体**:单纯工具调用(PubMed)帮助很小,ReAct 略差于 OpenAI function calling,LLM 难以从检索结果中识别有用信息;多智能体分工通过引入不确定性显著提升假设生成,且工具在多智能体框架中能进一步增益(Fig. 6b,具体数值未在正文列出)。 <!-- EN --> **Tools and multi-agent**: tool use alone (PubMed) helps little, ReAct slightly worse than OpenAI function calling, and LLMs struggle to pick useful information from results; multi-agent division of labour significantly improves generation by introducing uncertainty, and tools add further gains inside the multi-agent setup (Fig. 6b; exact numbers not given in the main text).

## 创新点 / Contributions
- <!-- ZH --> **按发表日期切分**来控制可见性,而非用熵-准确率相关间接估计污染 —— 是评测"发现"而非"记忆"的简单而关键的设计。 <!-- EN --> **Publication-date splitting** to control visibility, rather than indirectly estimating contamination — a simple but key design for evaluating discovery rather than recall.
- <!-- ZH --> 四维假设质量量表(新颖/相关/重要/可验证),并验证 GPT-4 评审与人类专家的一致性。 <!-- EN --> A four-dimension hypothesis rubric (novelty/relevance/significance/verifiability), with GPT-4-as-judge validated against human experts.
- <!-- ZH --> 把"不确定性"作为解释 zero-shot vs few-shot、外部知识效应的统一视角。 <!-- EN --> "Uncertainty" as a unifying lens for zero-shot vs few-shot and external-knowledge effects.
- <!-- ZH --> Analyst–Engineer–Scientist–Critic 四角色多智能体框架原型,检索端同样做时间过滤以防泄漏。 <!-- EN --> A four-role Analyst–Engineer–Scientist–Critic multi-agent prototype, with time-filtered retrieval to prevent leakage.

## 局限 / Limitations
- <!-- ZH --> 背景–假设对由 ChatGPT/GPT-4 自动抽取,作者承认抽取准确性与偏差需进一步评估、应人工标注子集。 <!-- EN --> Background–hypothesis pairs are extracted automatically by ChatGPT/GPT-4; the authors concede extraction accuracy/bias needs evaluation and manual annotation of a subset.
- <!-- ZH --> 规模小:unseen 测试仅 200 对,人评仅 100 例(作者称约 5% 抽样);GPT-4 评审本身可能偏好特定风格。 <!-- EN --> Small scale: 200 unseen pairs, 100 human-rated examples (described as ~5% sampling); GPT-4-as-judge may have its own stylistic bias.
- <!-- ZH --> "Verifiability" 是**评审者打分**的"可被检验",并非真正做实验或核对后续文献得到的验证;Fig. 1 的"后来被证实"是个案。 <!-- EN --> "Verifiability" is a *judge-rated* "could be tested", not actual experimental or literature verification; the "later confirmed" example in Fig. 1 is anecdotal.
- <!-- ZH --> SelfBLEU 只是不确定性的粗糙代理;未研究幻觉对假设质量的影响(作者列为未来工作);模型均为 2023 年代模型。 <!-- EN --> SelfBLEU is a crude uncertainty proxy; impact of factual hallucination on hypotheses is left to future work; all models are 2023-era.
- <!-- ZH --> 纯文本、只依赖文献背景,不接触任何实验数据或组学分析。 <!-- EN --> Text-only, literature-background only — no experimental data or omics analysis.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 对 **Plan B(可信生物医学 agent)** 是一篇方法学上的"前置参照":(1) **时间切分防泄漏**是我们评测 agent 时必须照搬的规范 —— 若让 agent 分析肾脏组学并"提出新机制",要证明它不是在复述训练语料里的 KPMP/Lake 2023 结论,就需要以发表时间(或数据发布时间)为界构建 seen/unseen,并对检索工具做同样的时间过滤;(2) 它的四维量表把"可验证性"交给 LLM 评审打分,而 Plan B 恰恰要把这一步**落到 claim-to-evidence 的实际核对**上(某条结论是否被 agent 自己跑出的数据/统计支持),并用校准的 verifier 替代"GPT-4 给 0–3 分";(3) novelty–verifiability 权衡与"不确定性"视角,可直接转化为 Plan B 的 **rerun stability** 指标:同一任务多次运行得到的结论分布(而非 SelfBLEU)才是更有意义的不确定性度量;(4) 它观察到"工具检索帮助很小、LLM 难以识别有用信息",正好是 omics-specific failure taxonomy 中"检索/证据选择失败"一类的早期证据。对 detect → model → **revert** 主链,它对应链尾"提名可回退异常的基因/扰动"之后的**假设生成与筛选**环节:Plan A 检测出的异常与 virtual tissue 给出的候选,需要以可验证假设的形式交付湿实验,这篇给出了如何评价这些假设的最低限度框架。
<!-- EN --> For **Plan B (trustworthy biomedical agents)** this is a methodological baseline: (1) **temporal splitting against leakage** is a protocol to copy — if an agent analysing kidney omics "proposes a new mechanism", proving it is not regurgitating KPMP/Lake-2023 conclusions requires seen/unseen splits by publication (or data-release) date, with the same time filter on retrieval tools; (2) its rubric hands "verifiability" to an LLM judge, whereas Plan B moves that step to **actual claim-to-evidence checking** (is the claim supported by the data/statistics the agent itself produced?) with a calibrated verifier instead of "GPT-4 gives 0–3"; (3) the novelty–verifiability trade-off and uncertainty lens translate into Plan B's **rerun stability** metric — the distribution of conclusions across repeated runs is a more meaningful uncertainty measure than SelfBLEU; (4) its finding that "tool retrieval helps little and LLMs struggle to identify useful information" is early evidence for the "retrieval/evidence-selection failure" class of an omics-specific failure taxonomy. On the detect → model → **revert** chain it sits after target nomination — the **hypothesis generation and triage** step: anomalies from Plan A and candidates from the virtual tissue must be delivered to the wet lab as verifiable hypotheses, and this paper gives a minimal framework for judging them.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码与数据:** LLM4BioHypoGen(背景–假设对、seen/unseen 切分、评测脚本)。 <!-- EN --> **Code & data:** LLM4BioHypoGen (background–hypothesis pairs, seen/unseen splits, evaluation scripts).
<!-- ZH/EN --> <https://github.com/TsinghuaC3I/LLM4BioHypoGen>
- <!-- ZH --> **评测协议:** 时间切分 + 检索端时间过滤;四维 0–3 量表 + GPT-4 逐步理由;SelfBLEU 多样性;GPT-4 与人类的 Pearson/Spearman 一致性检验。 <!-- EN --> **Eval protocol:** temporal split + time-filtered retrieval; four-dimension 0–3 rubric with GPT-4 step-by-step rationales; SelfBLEU diversity; Pearson/Spearman agreement between GPT-4 and humans.
- <!-- ZH --> **Agent 原型:** Analyst / Engineer / Scientist / Critic 角色设计。 <!-- EN --> **Agent prototype:** Analyst / Engineer / Scientist / Critic role design.

## 待读 / Follow-ups
- <!-- ZH --> 原始短版 arXiv:2311.05965。 <!-- EN --> The original short version, arXiv:2311.05965.
- <!-- ZH --> TruthHypo(IJCAI 2025)—— 同一团队方向上对"假设真实性/幻觉"的后续评测。 <!-- EN --> TruthHypo (IJCAI 2025) — follow-up evaluation of hypothesis truthfulness/hallucination along this line.
- <!-- ZH --> 把时间切分思路用于肾脏组学:以 Lake 2023 / KPMP 数据发布为界,检验 agent 结论是否只是复述已发表结果。 <!-- EN --> Apply temporal splitting to kidney omics: use Lake 2023 / KPMP releases as the boundary to test whether agent conclusions merely restate published results.

## 引用 / Cite
```bibtex
@inproceedings{Qi_2024,
  title = {Large Language Models as Biomedical Hypothesis Generators: A Comprehensive Evaluation},
  author = {Qi, Biqing and Zhang, Kaiyan and Tian, Kai and Li, Haoxiang and Chen, Zhang-Ren and Zeng, Sihang and Hua, Ermo and Hu, Jin-Fang and Zhou, Bowen},
  booktitle = {First Conference on Language Modeling (COLM)},
  year = {2024},
  eprint = {2407.08940},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2407.08940}
}
```

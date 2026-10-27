# Large Language Models as Biomedical Hypothesis Generators: A Comprehensive Evaluation

> **Bibkey** `Qi_2024` · **Venue** COLM 2024 (2024) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2407.08940>
> `status: complete` — 基于 arXiv v2 全文(COLM 2024 camera-ready,含附录 Tables 2–6)精读;Fig. 3/4/5/6b 只能读出趋势,具体数值以附录表格为准。PI 推荐。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> 作者从 PubMed 文献中自动抽取「背景知识 → 假设」配对,**按发表时间切分**(2023 年 1 月前 = 训练/seen,2023 年 8 月 = unseen)以避免测试数据被模型训练见过,系统评测 2023 年代 LLM 在 zero-shot、few-shot、微调、工具调用和多智能体设置下提出生物医学假设的能力,用 Novelty / Relevance / Significance / Verifiability 四个 0–3 分维度(LLM 评审 + 人类专家)打分(Abstract;§2–4)。
<!-- EN --> The authors automatically extract "background → hypothesis" pairs from PubMed papers, **split them by publication date** (before Jan 2023 = train/seen, Aug 2023 = unseen) so test data cannot have been seen in training, and systematically evaluate 2023-era LLMs at proposing biomedical hypotheses zero-shot, few-shot, fine-tuned, with tools and as a multi-agent system, scoring Novelty / Relevance / Significance / Verifiability on 0–3 (LLM judge + human experts) (Abstract; §2–4).

## 要点 / Takeaways
- <!-- ZH --> **时间切分是本文最可复用的设计**:只评测训练语料早于 2023 年 3 月的模型,unseen 测试集来自 2023 年 8 月的论文,检索工具也过滤掉 2023 年 1 月后的文献(§2.2、§3.1、§4.1)。 <!-- EN --> **Temporal splitting is the most reusable design**: only models trained on pre-March-2023 corpora are evaluated, the unseen test set comes from Aug-2023 papers, and the retrieval tool also filters out post-Jan-2023 literature (§2.2, §3.1, §4.1).
- <!-- ZH --> **novelty 与 verifiability 此消彼长**:zero-shot 更新颖,few-shot(尤其相似度检索的 5-shot*)更可验证;例如 gpt-3.5-turbo 的 Novelty 从 0-shot 1.42 降到 5-shot* 1.02,Verifiability 从 1.97 升到 2.36(Fig. 4;附录 Table 2)。 <!-- EN --> **Novelty and verifiability trade off**: zero-shot is more novel, few-shot (especially similarity-retrieved 5-shot*) more verifiable; e.g. gpt-3.5-turbo Novelty drops from 1.42 (0-shot) to 1.02 (5-shot*) while Verifiability rises from 1.97 to 2.36 (Fig. 4; Appendix Table 2).
- <!-- ZH --> **"Verifiability" 只是评审打分的"能否被检验"**,不是真的去做实验或核对后续文献;"后来被证实"只有 Fig. 1 一个个例(§3.1;Fig. 1)。 <!-- EN --> **"Verifiability" is a judge's rating of "could this be tested"**, not an actual experiment or literature check; "later confirmed" rests on the single example in Fig. 1 (§3.1; Fig. 1).
- <!-- ZH --> **LLM 评审与人类评审相关性高**:10 个模型/设置上 Pearson 0.73–0.97、Spearman 0.73–0.94;而 BLEU/ROUGE-L 与人评相关性很低甚至为负(Table 1;附录 Table 5)。 <!-- EN --> **LLM judge agrees with humans**: across 10 model/prompt settings Pearson 0.73–0.97, Spearman 0.73–0.94, whereas BLEU/ROUGE-L correlate weakly or even negatively with human scores (Table 1; Appendix Table 5).
- <!-- ZH --> **工具调用反而降分**:单个 ChatGPT 平均 1.92,加 PubMed 工具后 ReAct 1.56、OpenAI function calling 1.49;多智能体 2.09,多智能体 + 工具 2.07(附录 Table 6)。正文说"工具能进一步提升多智能体",但表中只有 Novelty(1.35 → 1.52)上升,平均分没有升。 <!-- EN --> **Tool use lowered scores**: single ChatGPT averages 1.92; with the PubMed tool, ReAct 1.56 and OpenAI function calling 1.49; multi-agent 2.09, multi-agent + tools 2.07 (Appendix Table 6). The text says tools "further enhance" the multi-agent system, but in the table only Novelty rises (1.35 → 1.52), not the average.

## 研究问题 / Problem
<!-- ZH --> 用 LLM 生成科学假设的工作依赖 ChatGPT、GPT-4 等模型,但它们的训练数据无法追溯,因此无法保证测试数据没被模型见过,也就无法在 zero-shot 条件下评估"知识发现"(Introduction)。此外,假设没有唯一正确答案,只用词重叠指标无法全面评价(§3.1)。作者要问:LLM 能否真正 zero-shot 地提出假设?few-shot 示例、领域适配、指令微调、工具调用和多智能体协作分别有什么影响(§3–4)?
<!-- EN --> Hypothesis-generation work relies on models like ChatGPT and GPT-4 whose training data cannot be traced, so test/train non-overlap cannot be guaranteed and "knowledge discovery" cannot be assessed zero-shot (Introduction). Hypotheses also have no single correct answer, so word-overlap metrics alone are insufficient (§3.1). The questions: can LLMs truly generate hypotheses zero-shot, and what do few-shot examples, domain adaptation, instruction tuning, tool use and multi-agent collaboration each contribute (§3–4)?

## 方法 / Method
<!-- ZH --> **第 1 步 任务定义**:给定指令 I 和从论文中抽取的背景知识 X,让模型生成假设 Y,形式化为文本补全(§2.1)。
<!-- ZH --> **第 2 步 数据构建**(仿 Self-Instruct 流程):按主题和内容组成论文集 → 用 ChatGPT 和 GPT-4 总结文献 → 生成「背景–假设」对 → 过滤低质量数据 → 按发表时间切分(§2.2)。附录实际给出两套数据,分别由 GPT-3.5 和 GPT-4 构建(附录 Tables 2–3;Fig. 8b)。
<!-- ZH --> **第 3 步 选模型**:只选训练语料早于 2023 年 3 月的模型 —— API 模型 gpt-3.5-turbo;Alpaca Eval 榜单(2023 年 9 月前)上的通用指令模型 Vicuna-33B-v1.3、Llama-2-70B-chat、WizardLM-13B-V1.2、WizardLM-70B-V1.0、Openchat-v3.2-super;医学模型 PMC-LLaMA-13B、MedAlpaca-13B(§3.1;附录 Table 4)。
<!-- ZH --> **第 4 步 提示与微调**:zero-shot;5-shot 随机采样(5-shot);5-shot 相似度检索(5-shot*),示例都取自 2023 年 1 月前的训练集。另在训练对上微调 WizardLM-13B-V1.2:3 个 epoch、batch size 8、最大长度 2048、学习率 3e-5,按 seen 测试集早停(§3.1;附录 F.4)。
<!-- ZH --> **第 5 步 评价**:有参考答案时用 BLEU / ROUGE;无参考答案时让 LLM 评审对 Novelty(是否有新信息)、Relevance(是否切题)、Significance(对理解问题的影响)、Verifiability(能否用现有方法或数据检验)各打 0–3 分并给出逐步理由。正文说用 GPT-4 评审,附录的评审 prompt 与 Table 1 表头写的是 "ChatGPT"(§3.1;附录 F.3)。人类评估:3 位生物医学专家对 unseen 测试集 100 个样本打分(§3.4)。
<!-- ZH --> **第 6 步 不确定性**:用 SelfBLEU(一组生成之间的相互 BLEU,越低越多样)作为生成"不确定性"的廉价代理,分析它与 Novelty、Verifiability 的关系(§3.3;Fig. 5)。
<!-- ZH --> **第 7 步 多智能体与工具**:Analyst(从背景中抽关键词/主题)→ Engineer(用 PubMed 检索并整理,排除 2023 年 1 月后的文献)→ Scientist(结合检索结果与背景提出假设)→ Critic(评估并反馈,可回到前面的角色),可选人类参与;工具调用对比 ReAct 与 OpenAI function calling,在 unseen 测试集上评估(§4.1;Fig. 6)。
<!-- EN --> **Step 1 Task**: given instruction I and background X extracted from a paper, generate hypothesis Y — framed as text completion (§2.1).
<!-- EN --> **Step 2 Data** (Self-Instruct-style): compose paper sets by topic → summarize with ChatGPT and GPT-4 → generate background–hypothesis pairs → filter low quality → split by publication date (§2.2). The appendix reports two dataset versions, built by GPT-3.5 and by GPT-4 (Appendix Tables 2–3; Fig. 8b).
<!-- EN --> **Step 3 Models**: only models trained on corpora before March 2023 — API gpt-3.5-turbo; general instruction models from the Alpaca Eval leaderboard (pre-Sept-2023) Vicuna-33B-v1.3, Llama-2-70B-chat, WizardLM-13B-V1.2, WizardLM-70B-V1.0, Openchat-v3.2-super; medical models PMC-LLaMA-13B and MedAlpaca-13B (§3.1; Appendix Table 4).
<!-- EN --> **Step 4 Prompts and fine-tuning**: zero-shot; 5-shot random (5-shot); 5-shot similarity-retrieved (5-shot*), examples drawn from the pre-Jan-2023 training set. WizardLM-13B-V1.2 is also fine-tuned on the training pairs: 3 epochs, batch size 8, max length 2048, LR 3e-5, early-stopped on the seen test set (§3.1; Appendix F.4).
<!-- EN --> **Step 5 Evaluation**: BLEU / ROUGE against the reference; without a reference, an LLM judge scores Novelty (new information?), Relevance (on topic?), Significance (impact on the problem), Verifiability (testable with existing methods or data?) on 0–3 each, with step-by-step reasons. The text says GPT-4 is the judge; the appendix judge prompts and the Table 1 header say "ChatGPT" (§3.1; Appendix F.3). Human evaluation: three biomedical experts score 100 unseen-test examples (§3.4).
<!-- EN --> **Step 6 Uncertainty**: SelfBLEU (BLEU among a set of generations; lower = more diverse) is a cheap proxy for generation "uncertainty", related to Novelty and Verifiability (§3.3; Fig. 5).
<!-- EN --> **Step 7 Multi-agent and tools**: Analyst (keywords/topics from the background) → Engineer (PubMed search and organisation, excluding post-Jan-2023 papers) → Scientist (hypothesis from findings + background) → Critic (evaluates, loops back), optional human in the loop; tool use compared via ReAct vs OpenAI function calling, evaluated on the unseen test set (§4.1; Fig. 6).

## 方法图 / Method diagram
```mermaid
flowchart LR
  P["PubMed papers"] --> E["GPT-3.5 / GPT-4 extract background-hypothesis pairs"]
  E --> T["Split by publication date: seen before Jan 2023, unseen Aug 2023"]
  T --> M["LLMs: 0-shot, 5-shot, fine-tuned, tools, multi-agent"]
  M --> J["LLM judge: novelty, relevance, significance, verifiability"]
  M --> W["BLEU / ROUGE and SelfBLEU"]
  J --> H["Check against 3 human experts"]
```

## 数据 / Data
<!-- ZH --> **Seen 数据集**:2,700 对背景–假设,来自 2023 年 1 月前的文献,分为训练 2,500 对和验证 200 对(同时作为 seen 测试集)。**Unseen 数据集**:200 对,来自 2023 年 8 月发表的论文(§2.2)。论文池为约 10,000 篇 PubMed 医学论文(Fig. 2b)。用 OpenAI embedding + t-SNE 可视化,seen 与 unseen 测试集分布差异很小(附录 C.1;Fig. 8a)。人类评估:3 位生物医学专家,unseen 测试集 100 例(§3.4)。数据与代码开源(Abstract)。
<!-- EN --> **Seen**: 2,700 background–hypothesis pairs from literature before Jan 2023, split into 2,500 train and 200 validation (also the seen test set). **Unseen**: 200 pairs from papers published in Aug 2023 (§2.2). Source pool: about 10,000 PubMed medical papers (Fig. 2b). OpenAI embeddings + t-SNE show little difference between seen and unseen test sets (Appendix C.1; Fig. 8a). Human evaluation: three biomedical experts, 100 unseen-test examples (§3.4). Data and code released (Abstract).

## 主要结果 / Key results
- <!-- ZH --> **zero-shot 更新颖、few-shot 更可验证**:几乎所有模型(尤其 WizardLM 系列和 Openchat-v3.2-super)zero-shot 时 Novelty 更高,给 few-shot 示例后 Verifiability 更高(§3.2.1;Fig. 4)。例:WizardLM-70B-V1.0 Novelty 0-shot 1.57 → 5-shot* 0.97(附录 Table 2,GPT-3.5 数据集)。 <!-- EN --> **Zero-shot more novel, few-shot more verifiable**: nearly all models (notably the WizardLM series and Openchat-v3.2-super) score higher Novelty zero-shot and higher Verifiability with few-shot examples (§3.2.1; Fig. 4). E.g. WizardLM-70B-V1.0 Novelty 1.57 (0-shot) → 0.97 (5-shot*) (Appendix Table 2, GPT-3.5 dataset).
- <!-- ZH --> **unseen 上 BLEU 反而更高**:作者原以为 seen 集会因记忆而更好,但 Fig. 3 显示模型在 unseen 集上往往更好;例如 gpt-3.5-turbo 0-shot BLEU seen 13.93、unseen 15.52(附录 Table 2)。作者推测是假设生成的复杂性妨碍模型利用参数化的 "dark knowledge"(§3.2.1)。 <!-- EN --> **Higher BLEU on unseen**: the authors expected seen to win through memorization, but Fig. 3 shows models tend to do better on unseen; e.g. gpt-3.5-turbo 0-shot BLEU 13.93 seen vs 15.52 unseen (Appendix Table 2). They speculate the task's complexity hinders use of parametric "dark knowledge" (§3.2.1).
- <!-- ZH --> **外部知识不总有益**:领域适配(MedAlpaca、PMC-LLaMA)提高词重叠指标,并提高利用 few-shot 的能力,但削弱 zero-shot 能力;指令微调提高 BLEU/ROUGE 和可验证性,但降低新颖性和重要性(§3.2.2)。微调后的 WizardLM-13B-V1.2 人评 Novelty 只有 0.85、Significance 1.23(Table 1)。 <!-- EN --> **External knowledge is not always helpful**: domain adaptation (MedAlpaca, PMC-LLaMA) improves word overlap and few-shot use but weakens zero-shot ability; instruction tuning improves BLEU/ROUGE and verifiability but reduces novelty and significance (§3.2.2). Fine-tuned WizardLM-13B-V1.2 has human Novelty 0.85 and Significance 1.23 (Table 1).
- <!-- ZH --> **不确定性**:zero-shot 生成的 SelfBLEU 更低(更不确定/更多样)且 Novelty 更高;few-shot 不确定性更低而 Verifiability 更高(§3.3;Fig. 5)。 <!-- EN --> **Uncertainty**: zero-shot generations have lower SelfBLEU (more uncertain/diverse) and higher Novelty; few-shot has lower uncertainty and higher Verifiability (§3.3; Fig. 5).
- <!-- ZH --> **人类评估**:LLM 评审与人类平均分的相关系数 Pearson 0.73–0.97、Spearman 0.73–0.94(均 > 0.7);人评平均最高为 Llama-2-70b-chat 5-shot 2.33,gpt-3.5-turbo 0-shot 2.02(Table 1)。BLEU 与人评相关性在 −0.58 到 0.32 之间(附录 Table 5)。 <!-- EN --> **Human evaluation**: LLM-judge vs human average correlations Pearson 0.73–0.97, Spearman 0.73–0.94 (all > 0.7); best human average Llama-2-70b-chat 5-shot 2.33, gpt-3.5-turbo 0-shot 2.02 (Table 1). BLEU–human correlations range from −0.58 to 0.32 (Appendix Table 5).
- <!-- ZH --> **工具与多智能体(unseen 测试集,LLM 评审平均分)**:ChatGPT 1.92;+ ReAct 工具 1.56;+ OpenAI function calling 1.49;多智能体 2.09;多智能体 + 工具 2.07(附录 Table 6)。正文结论是"工具帮助很小、LLM 难以从检索结果中识别有用信息;多智能体通过引入不确定性显著提升"(§4.2)。 <!-- EN --> **Tools and multi-agent (unseen test, LLM-judge average)**: ChatGPT 1.92; + ReAct tools 1.56; + OpenAI function calling 1.49; multi-agent 2.09; multi-agent + tools 2.07 (Appendix Table 6). The text concludes that tools help little and LLMs struggle to identify useful information, while multi-agent collaboration "significantly" improves generation by introducing uncertainty (§4.2).
- <!-- ZH --> **正文与附录表不一致的地方**:§4.2 说 ReAct 略差于 OpenAI function calling,但 Table 6 中 ReAct(2a)平均 1.56 高于 function calling(2b)1.49;§4.2 说工具能进一步提升多智能体,但 Table 6 平均分 2.09 → 2.07 略降。 <!-- EN --> **Text vs appendix mismatches**: §4.2 says ReAct is slightly worse than OpenAI function calling, yet in Table 6 ReAct (2a) averages 1.56 vs 1.49 for function calling (2b); §4.2 says tools further enhance the multi-agent system, yet the Table 6 average goes 2.09 → 2.07.

## 创新点 / Contributions
- <!-- ZH --> **按发表日期直接控制可见性**,而不是像以往那样用题目熵与准确率的相关性间接估计污染(§2.2)。 <!-- EN --> **Controls visibility directly by publication date**, instead of estimating contamination indirectly from question entropy vs accuracy as earlier work did (§2.2).
- <!-- ZH --> 四维假设评分量表,并检验 LLM 评审与人类专家的一致性(§3.1、§3.4)。 <!-- EN --> A four-dimension hypothesis rubric, with LLM-judge agreement checked against human experts (§3.1, §3.4).
- <!-- ZH --> 用"不确定性"(SelfBLEU)作为解释 zero-shot / few-shot / 外部知识效应的统一视角(§3.3)。 <!-- EN --> "Uncertainty" (SelfBLEU) as a single lens for zero-shot / few-shot / external-knowledge effects (§3.3).
- <!-- ZH --> Analyst–Engineer–Scientist–Critic 多智能体原型,检索端同样做时间过滤(§4.1)。 <!-- EN --> An Analyst–Engineer–Scientist–Critic multi-agent prototype with time-filtered retrieval (§4.1).

## 局限 / Limitations
- <!-- ZH --> 作者自述:背景–假设对由 ChatGPT/GPT-4 自动抽取,其准确性和引入的偏差需要进一步评估,应人工标注一个子集(§2.2)。 <!-- EN --> Authors: pairs are extracted automatically by ChatGPT/GPT-4; extraction accuracy and bias need evaluation, ideally by manually annotating a subset (§2.2).
- <!-- ZH --> 作者自述:LLM 的事实性幻觉对假设生成的影响需要深入研究;目前只用 Web 搜索和 PubMed,未来想接入生物信息学分析工具和知识图谱(§6)。 <!-- EN --> Authors: the effect of factual hallucination on hypotheses needs study; only web search and PubMed are used, with bioinformatics tools and knowledge graphs left for future work (§6).
- <!-- ZH --> 作者自述:由于成本只做了部分人类评估,作者称采用 5% 抽样率(§3.4)。我们的理解:100 例占 unseen 测试集 200 对的一半,"5%"与文中其他数字对不上,原文未解释。 <!-- EN --> Authors: human evaluation was partial because of cost; they describe a 5% sampling rate (§3.4). Our reading: 100 examples are half of the 200 unseen pairs, so "5%" does not match the other numbers, and the paper does not explain it.
- <!-- ZH --> 我们的理解:Verifiability 是评审打分,不是事实验证;评审用的是 ChatGPT/GPT-4,而数据也是 ChatGPT/GPT-4 抽取的,存在同源偏差;SelfBLEU 只是多样性的粗糙代理;所有模型都是 2023 年代模型;规模小(unseen 200 对)。 <!-- EN --> Our reading: Verifiability is a rating, not a fact check; the judge (ChatGPT/GPT-4) is from the same family that extracted the data, so same-source bias is possible; SelfBLEU is a crude diversity proxy; all models are 2023-era; the scale is small (200 unseen pairs).
- <!-- ZH --> 我们的理解:正文对工具与多智能体的描述和附录 Table 6 的数字不完全一致(见主要结果),引用这部分结论时应以表格为准。 <!-- EN --> Our reading: the text's description of tools and multi-agent results does not fully match Appendix Table 6 (see Key results); cite the table, not the prose.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 对 **课题 2(生物医学分析 agent 的结论核查)**,这篇是"假设评分"一环的早期参照。我们的理解:(1) **时间切分防泄漏**可以直接照搬:若 agent 分析肾脏数据后"提出新机制",要排除它只是在复述已发表结论,就需要按论文或数据发布时间划 seen/unseen,并对检索工具做同样的时间过滤。(2) 它把"可验证性"交给 LLM 打 0–3 分,而课题 2 要做的是**把结论真正追溯到证据**(agent 自己的代码、数据或引用的文献是否支持),并用专家标注校准 —— 它的人类–LLM 一致性检验(Table 1)是一个最低限度的校准方案,但只在 100 例、模型平均分层面做了相关。(3) novelty–verifiability 权衡提醒我们:一个只奖励"有证据"的核查器可能会惩罚真正新颖的假设,评分要把"无证据"与"新但可检验"分开。(4) "工具检索反而降分、LLM 难以从检索结果中挑出有用信息"(§4.2;Table 6)是"证据选择失败"这一类失败的早期证据。
<!-- ZH --> 在 detect → model → revert 链条上,我们的理解:它对应 revert 之后"把候选基因/扰动写成可检验假设并排序"的环节;但它只用文献背景,不接触任何实验或组学数据。
<!-- EN --> For **Topic 2 (verifying the claims of biomedical analysis agents)** this is an early reference for the hypothesis-scoring step. Our reading: (1) **temporal splitting against leakage** can be copied directly: to rule out that an agent analysing kidney data merely restates published conclusions when it "proposes a new mechanism", split seen/unseen by paper or data-release date and apply the same time filter to retrieval tools. (2) It hands "verifiability" to an LLM rating of 0–3, whereas Topic 2 wants to **trace each claim to actual evidence** (is it supported by the agent's own code, data or cited papers?) calibrated against expert labels — its human–LLM agreement check (Table 1) is a minimal calibration, done only on 100 examples and at the level of model-average scores. (3) The novelty–verifiability trade-off warns that a verifier rewarding only "supported" claims may penalise genuinely novel hypotheses; scoring should separate "unsupported" from "new but testable". (4) "Tool retrieval lowered scores and LLMs struggle to pick useful information from results" (§4.2; Table 6) is early evidence for an "evidence-selection failure" class.
<!-- EN --> On the detect → model → revert chain, our reading: it corresponds to the step after revert — writing candidate genes/perturbations as testable hypotheses and ranking them; but it uses literature background only and touches no experimental or omics data.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码与数据:** LLM4BioHypoGen(Abstract 给出的链接)。 <!-- EN --> **Code & data:** LLM4BioHypoGen (link given in the Abstract).
<!-- ZH/EN --> <https://github.com/TsinghuaC3I/LLM4BioHypoGen>
- <!-- ZH --> **评测协议:** 时间切分 + 检索端时间过滤;四维 0–3 评分 prompt(附录 Tables 14–17);SelfBLEU 多样性;LLM 评审与人类的 Pearson/Spearman 一致性。 <!-- EN --> **Eval protocol:** temporal split + time-filtered retrieval; four-dimension 0–3 judge prompts (Appendix Tables 14–17); SelfBLEU diversity; Pearson/Spearman agreement between LLM judge and humans.
- <!-- ZH --> **Agent 原型:** Analyst / Engineer / Scientist / Critic 角色 prompt(附录 Tables 12–13)。 <!-- EN --> **Agent prototype:** Analyst / Engineer / Scientist / Critic role prompts (Appendix Tables 12–13).

## 待读 / Follow-ups
- <!-- ZH --> TruthHypo(本仓库 `truthhypo-ijcai-2025`)—— 关注假设的真实性与幻觉,正好补本文 §6 留下的问题。 <!-- EN --> TruthHypo (`truthhypo-ijcai-2025` in this repo) — on hypothesis truthfulness and hallucination, the question §6 leaves open.
- <!-- ZH --> 把时间切分用到肾脏组学:以已发表的肾脏单细胞图谱为界,检验 agent 的结论是否只是复述已有结果。 <!-- EN --> Apply temporal splitting to kidney omics: use published kidney single-cell atlases as the boundary and test whether agent conclusions only restate known results.

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

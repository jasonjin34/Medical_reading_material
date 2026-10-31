# Toward Reliable Scientific Hypothesis Generation: Evaluating Truthfulness and Hallucination in Large Language Models

> **Bibkey** `truthhypo-ijcai-2025` · **Venue** IJCAI 2025 (2025) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2505.14599>
> `status: complete` — 全文精读(arXiv HTML 全文 + 附录;arXiv 注明 "Accepted to IJCAI 2025")。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> TruthHypo 用 PubTator 3.0 知识图按时间切分(2023 前「已见」、2024 后「未见」)构造生物医学假设生成基准,检验 LLM 能否提出**真实**的新关系;配套的 KnowHD 把假设及其推理拆成原子论断,逐条对照文献/知识图判断是否 grounded —— groundedness 越高的假设越可能为真,用它在 5 个候选中选优可提升准确率。
<!-- EN --> TruthHypo builds a biomedical hypothesis-generation benchmark from a temporally split PubTator 3.0 knowledge graph (pre-2023 "seen", post-2024 "unseen") to test whether LLMs propose **truthful** new relations; the companion KnowHD decomposes each hypothesis and its rationale into atomic claims and checks each against literature and/or the KG — higher groundedness predicts truthfulness, and selecting the most grounded of five candidates improves accuracy.

## 研究问题 / Problem
<!-- ZH --> LLM 生成科研假设的工作大多追求新颖性和多样性,却很少评估**真实性**:验证一个假设要花大量时间和资源,而幻觉会产出「看起来合理但错误」的假设。作者要回答两件事:(1) LLM 生成真实生物医学假设的能力到底如何,外部知识(KG、文献)帮不帮得上?(2) 能否在不做实验的前提下,用「推理过程是否有已有知识支撑」作为信号,提前筛掉不可信的假设?
<!-- EN --> Most LLM hypothesis-generation work optimises novelty and diversity but rarely evaluates **truthfulness**: verifying a hypothesis is costly, and hallucination yields plausible-but-wrong hypotheses. Two questions: (1) how well do LLMs generate truthful biomedical hypotheses, and do external knowledge sources (KG, literature) help? (2) Without running experiments, can "is the reasoning supported by existing knowledge" serve as a signal to filter out untrustworthy hypotheses in advance?

## 方法 / Method
<!-- ZH --> **TruthHypo 基准**:基于 PubTator 3.0 的文献抽取关系,以 PMID 对应的发表年份切分为「seen」(2023 年前)与「unseen」(2024 年后,代表新发现);删除 unseen 中与 seen 共享头尾实体的边,且只保留被多篇文章支持的关系。三类任务:Chemical & Gene、Disease & Gene、Gene & Gene;并按每类平均标签数加入 `no_relation` 负样本以测假阳性。输入是两个实体,LLM 需假设其关系。四种知识设置:仅参数知识;+KG(把实体映射到 seen 图并取多跳链路转成文本);+文献(BM25 在 PubMed 中检索,仅限时间切分前的文章,即 RAG);+KG+文献。指标:link-level 的 precision/recall/F1(是否存在关系),relation-level accuracy(具体关系是否正确)。**KnowHD**:用 LLM 把假设及其推理链拆成原子论断;对每条论断,文献模式下用 BM25 取 2023 前 PubMed 的 top-k 相关文档,KG 模式下取论断所含实体之间的 seen 图边;再由 LLM 判断上下文是否蕴含该论断。假设的 groundedness = 被支持的原子论断比例。
<!-- EN --> **TruthHypo**: relations extracted from literature in PubTator 3.0, split by publication year of the source PMID into "seen" (pre-2023) and "unseen" (post-2024, representing new discoveries); unseen edges sharing head and tail entities with seen ones are removed, and only relations supported by multiple articles are kept. Three tasks: Chemical & Gene, Disease & Gene, Gene & Gene, with `no_relation` negatives added (sized to the per-label average) to test false positives. Input is an entity pair; the LLM hypothesises their relation. Four knowledge settings: parametric only; +KG (entities mapped to the seen graph, multi-hop link chains verbalised); +literature (BM25 over PubMed restricted to pre-split articles, i.e. RAG); +KG+literature. Metrics: link-level precision/recall/F1 (does a relation exist) and relation-level accuracy (is the specific relation right). **KnowHD**: an LLM decomposes each hypothesis and its reasoning chain into atomic claims; for each claim, literature mode retrieves top-k pre-2023 PubMed documents via BM25, KG mode collects seen-graph edges among the claim's entities; an LLM then judges whether the context entails the claim. A hypothesis's groundedness is the fraction of supported atomic claims.

## 数据 / Data
<!-- ZH --> PubTator 3.0 知识图 + PubMed 语料(MedRAG 工具包预处理的分块,BM25 检索)。最终任务规模:Chemical & Gene 1,209 例(positive_correlate 328 / negative_correlate 478 / no_relation 403);Disease & Gene 268 例(stimulate 104 / inhibit 75 / no_relation 89);Gene & Gene 547 例(positive 247 / negative 118 / no_relation 182)。被测 LLM:Llama-3.1-8B、Llama-3.1-70B、GPT-4o-mini、GPT-4o(训练知识均截至 2024 年前)。开放式人类研究使用 Qi et al. (2024) 的公开假设生成数据集。
<!-- EN --> PubTator 3.0 knowledge graph + PubMed corpus (MedRAG-preprocessed chunks, BM25 retrieval). Final task sizes: Chemical & Gene 1,209 (positive_correlate 328 / negative_correlate 478 / no_relation 403); Disease & Gene 268 (stimulate 104 / inhibit 75 / no_relation 89); Gene & Gene 547 (positive 247 / negative 118 / no_relation 182). Models: Llama-3.1-8B, Llama-3.1-70B, GPT-4o-mini, GPT-4o (all trained on pre-2024 knowledge). The open-ended human study uses the public hypothesis-generation dataset of Qi et al. (2024).

## 主要结果 / Key results
<!-- ZH -->
- **LLM 难以生成真实假设**:只有 GPT-4o 平均准确率超过 60%;link-level F1(约 65–84%)明显高于 relation-level 准确率 —— 能猜到「有关系」,却常猜错「什么关系」。最好成绩是 GPT-4o 在 KG+文献设置下平均 F1 83.55%、准确率 66.95%(参数知识下 61.81%)。
- **规模效应与外部知识利用能力**:加 KG+文献后 GPT-4o-mini 准确率仅 +1.14%,GPT-4o +5.14%;Llama-3.1-8B 反而在 KG+文献下降到 39.62%(参数知识 43.23%)—— 小模型整合内外部信息困难。
- **KnowHD groundedness**(GPT-4o-mini 生成的假设):如 Chemical & Gene 文献增强假设,在文献知识库下有 76.30% 的论断可被验证;KG 增强假设用文献验证只有 51.08%;KG+文献联合验证最高(73–87%)。
- **groundedness 与真实性正相关**:GPT-4o-mini 在 Chemical & Gene(KG+文献)平均准确率 60.96%,groundedness > 80% 的假设准确率升至 72.77%。
- **用 groundedness 选优**:每题生成 5 个候选,选 groundedness 最高者;在有外部知识的设置下一致优于 greedy 与 self-consistency 多数投票 —— KG+文献下 GPT-4o-mini 平均准确率 63.44%,接近 GPT-4o;仅参数知识时多数投票略优(61.86% vs 59.83%)。
- **开放式人类研究**:54 对 groundedness 差异显著(高者比低者高 ≥30%)的假设,两位领域专家(一致率 80%)选高 groundedness 者为更可信的比例 59.26% vs 40.74%;GPT-4o 为 61.11% vs 38.89%。
<!-- EN -->
- **LLMs struggle to generate truthful hypotheses**: only GPT-4o exceeds 60% mean accuracy; link-level F1 (~65–84%) clearly exceeds relation-level accuracy — models guess *that* a relation exists but often not *which*. Best: GPT-4o with KG+literature, mean F1 83.55% and accuracy 66.95% (61.81% parametric only).
- **Scale and the ability to use external knowledge**: KG+literature adds only +1.14% accuracy for GPT-4o-mini but +5.14% for GPT-4o; Llama-3.1-8B actually drops to 39.62% with KG+literature (43.23% parametric) — small models struggle to integrate internal and external information.
- **KnowHD groundedness** (GPT-4o-mini hypotheses): e.g. for literature-augmented Chemical & Gene hypotheses, 76.30% of claims are verifiable against literature; KG-augmented hypotheses verify at only 51.08% against literature; combined KG+literature verification is highest (73–87%).
- **Groundedness tracks truthfulness**: GPT-4o-mini's mean accuracy on Chemical & Gene (KG+lit) is 60.96%, rising to 72.77% for hypotheses with groundedness above 80%.
- **Groundedness-based selection**: generate five candidates, keep the most grounded; with external knowledge this consistently beats greedy decoding and self-consistency majority voting — GPT-4o-mini reaches 63.44% mean accuracy with KG+literature, approaching GPT-4o; with parametric knowledge only, majority voting is slightly better (61.86% vs 59.83%).
- **Open-ended human study**: 54 hypothesis pairs with a ≥30% groundedness gap; two domain experts (80% agreement) picked the highly grounded one as more likely truthful 59.26% vs 40.74%; GPT-4o 61.11% vs 38.89%.

## 创新点 / Contributions
- <!-- ZH --> **时间切分的知识图构造**:用「过去的知识」预测「未来被发表的关系」,给开放式假设生成提供了客观可评的真值。 <!-- EN --> **Temporally split KG construction**: predict "future-published relations" from "past knowledge", giving open-ended hypothesis generation an objective ground truth.
- <!-- ZH --> **KnowHD:原子论断级的 groundedness**,而不是整体打分,能定位推理链里哪一步缺乏支持。 <!-- EN --> **KnowHD: atomic-claim-level groundedness** rather than a holistic score, localising which reasoning step lacks support.
- <!-- ZH --> 把 groundedness 从「诊断」变成「选择器」,在多候选中筛出更可能为真的假设。 <!-- EN --> Turns groundedness from a diagnostic into a selector that filters candidates toward truthful ones.
- <!-- ZH --> 系统比较了参数知识 / KG / 文献 / 二者结合四种设置对不同规模模型的影响。 <!-- EN --> Systematically compares parametric / KG / literature / combined settings across model sizes.

## 局限 / Limitations
- <!-- ZH --> 任务被简化为「两个实体之间的关系分类」(三类关系类型 + 无关系),远窄于真实的开放式科研假设。 <!-- EN --> The task reduces to relation classification between two entities (three relation types plus no-relation), much narrower than real open-ended scientific hypotheses.
- <!-- ZH --> 真值来自 PubTator 的自动文本挖掘关系,本身含抽取噪声;「unseen」只意味着 2024 年后才被文献报道,不等于实验确证。 <!-- EN --> Ground truth comes from PubTator's automated text-mined relations, which carry extraction noise; "unseen" only means first reported after 2024, not experimentally confirmed.
- <!-- ZH --> groundedness 衡量的是与**已有**知识的一致性 —— 天然偏向保守、已知的假设,可能惩罚真正新颖的发现(作者未正面讨论这一张力)。 <!-- EN --> Groundedness measures consistency with **existing** knowledge — inherently favouring conservative hypotheses and potentially penalising genuinely novel discoveries (a tension the paper does not confront directly).
- <!-- ZH --> 蕴含判断由 LLM 完成,未单独校准 verifier 本身的错误率;人类研究只有 54 对、两位专家。 <!-- EN --> Entailment is judged by an LLM whose own error rate is not separately calibrated; the human study has only 54 pairs and two experts.
- <!-- ZH --> 只测了 2024 年前的四个模型;检索仅用 BM25。 <!-- EN --> Only four pre-2024 models; retrieval is BM25 only.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 这是 **Agent 可信度课题「claim-to-evidence verification」最直接的技术原型**之一。KnowHD 的流程 —— 把输出拆成原子论断 → 为每条论断检索证据 → 判断蕴含 → 汇总为分数 —— 几乎就是 Agent 可信度课题校准 verifier 的骨架;区别在于 Agent 可信度课题的证据源不只是文献和 KG,还包括 agent 在肾脏组学数据上实际跑出来的中间产物(差异表达表、细胞注释、空间统计)。三点可借鉴:**(1) 时间切分构造真值** 的思路可以移植到肾脏:用某时间点之前的 KPMP/Lake atlas 与文献作为「已见」,之后发表的肾病关键基因/通路关联作为「未见」,评估 agent 提名的靶点;**(2) groundedness-based selection** 对 detect → model → revert 的 revert 阶段很有用:对候选「回正基因」做多次采样,优先保留证据支持度高的提名再进入湿实验排序;**(3)** 它暴露的张力值得在 Agent 可信度课题里显式处理 —— 「被已有知识支持」≠「对」,也 ≠「新」。Agent 可信度课题的 verifier 应区分「与已有证据矛盾」「无证据支持(可能新颖)」「有证据支持」三类,而不是把无支持一律当幻觉。另外 KnowHD 未校准自身误差,而 Agent 可信度课题强调 **calibrated** verifier,这正是可以补上的一环。
<!-- EN --> One of the most direct **technical prototypes for the agent-trustworthiness topic's claim-to-evidence verification**. KnowHD's pipeline — decompose output into atomic claims → retrieve evidence per claim → judge entailment → aggregate into a score — is essentially the skeleton of the agent-trustworthiness topic's calibrated verifier; the difference is that the agent-trustworthiness topic's evidence includes not only literature and KGs but the intermediate artefacts the agent actually produced on kidney omics (DE tables, cell annotations, spatial statistics). Three transferable ideas: **(1) temporal-split ground truth** ports to kidney — treat KPMP/Lake atlases and literature before a cutoff as "seen" and later-published kidney-disease gene/pathway associations as "unseen" to score agent-nominated targets; **(2) groundedness-based selection** fits the revert step of detect → model → revert: sample candidate "reverting genes" several times and keep the best-supported nominations before wet-lab prioritisation; **(3)** the tension it exposes should be handled explicitly in the agent-trustworthiness topic — "supported by existing knowledge" ≠ "correct", and ≠ "novel". The agent-trustworthiness topic's verifier should distinguish "contradicted by evidence", "unsupported (possibly novel)" and "supported", rather than treating every unsupported claim as hallucination. KnowHD also does not calibrate its own error — the agent-trustworthiness topic's emphasis on a **calibrated** verifier fills exactly that gap.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码与数据:** TruthHypo 基准与 KnowHD 实现。 <!-- EN --> **Code & data:** TruthHypo benchmark and KnowHD implementation.
<!-- ZH/EN --> <https://github.com/Teddy-XiongGZ/TruthHypo>
- <!-- ZH --> **知识源:** PubTator 3.0 知识图;MedRAG 工具包的 PubMed 分块 + BM25 检索。 <!-- EN --> **Knowledge sources:** PubTator 3.0 KG; MedRAG-toolkit PubMed chunks + BM25 retrieval.
- <!-- ZH --> **Prompt 模板:** 原子论断分解、实体抽取、蕴含判断(附录 D 图 5–12)。 <!-- EN --> **Prompt templates:** atomic-claim decomposition, entity extraction, entailment judgement (Appendix D, Figs 5–12).

## 待读 / Follow-ups
- <!-- ZH --> `hypogen-llm-colm-2024`(Qi et al.,本文开放式实验所用数据集的来源)。 <!-- EN --> `hypogen-llm-colm-2024` (Qi et al. — source of the open-ended dataset used here).
- <!-- ZH --> MedRAG / MIRAGE(同作者组的医学 RAG 基准),看检索设置的影响。 <!-- EN --> MedRAG / MIRAGE (same group's medical RAG benchmark) for retrieval-setting effects.
- <!-- ZH --> `medragchecker-arxiv-2026`:同样走原子论断级验证路线,但针对 RAG 回答。 <!-- EN --> `medragchecker-arxiv-2026` — same atomic-claim verification route, applied to RAG answers.

## 引用 / Cite
```bibtex
@inproceedings{truthhypo-ijcai-2025, title={Toward Reliable Scientific Hypothesis Generation: Evaluating Truthfulness and Hallucination in Large Language Models}, author={Xiong, Guangzhi and Xie, Eric and Williams, Corey and Kim, Myles and Shariatmadari, Amir Hassan and Guo, Sikun and Bekiranov, Stefan and Zhang, Aidong}, booktitle={Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence (IJCAI-25)}, year={2025}, eprint={2505.14599}, archivePrefix={arXiv}, primaryClass={cs.CL}, url={https://arxiv.org/abs/2505.14599}, doi={10.48550/arXiv.2505.14599} }
```

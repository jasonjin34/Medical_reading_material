# Language agents achieve superhuman synthesis of scientific knowledge

> **Bibkey** `Skarlinski2024_240913740` · **Venue** arXiv preprint (2024) · **Category** agents · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2409.13740>
> `status: complete` — 全文精读基于 arXiv HTML(v2,2024-09-26)正文与 Methods。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> PaperQA2(FutureHouse)把 RAG 拆成工具交给 agent 编排——Paper Search、Gather Evidence(dense 检索 + **LLM 重排与上下文摘要 RCS**)、Citation Traversal、Generate Answer——在新建的全文检索基准 LitQA2 上精确率超过博士级人类,写出的基因 Wikipedia 式文章(WikiCrow)比真实 Wikipedia 更少"引了但不支持"的陈述,并用 ContraCrow 在生物学文献中大规模检测矛盾。
<!-- EN --> PaperQA2 (FutureHouse) decomposes RAG into agent-orchestrated tools — Paper Search, Gather Evidence (dense retrieval + **LLM reranking and contextual summarisation, RCS**), Citation Traversal, Generate Answer — exceeding PhD-level humans in precision on the new full-text retrieval benchmark LitQA2, writing gene Wikipedia-style articles (WikiCrow) with fewer "cited but unsupported" statements than real Wikipedia, and detecting contradictions in the biology literature at scale (ContraCrow).

## 研究问题 / Problem
<!-- ZH --> LLM 会幻觉、会忽略细节,而现有文献检索基准只用摘要、固定语料或直接给出相关论文,且缺少与人类的直接对比,因此无法判断 LLM agent 是否足以用于真实科研文献任务。作者要建立严格的人-AI 对比方法,覆盖检索问答、综述写作、矛盾检测三类任务。
<!-- EN --> LLMs hallucinate and miss details, while existing literature benchmarks use abstracts only, a fixed corpus, or hand the relevant paper over, and rarely compare against humans — so it is unclear whether LLM agents are fit for real literature research. The authors build a rigorous human-vs-AI methodology across retrieval QA, summary writing and contradiction detection.

## 方法 / Method
<!-- ZH --> **PaperQA2**:agent(编排 LLM 固定为 gpt-4-turbo-2024-04-09)可多次调用四个工具:**Paper Search**(把请求改写成关键词检索,取回全文、解析、分块;WikiCrow 用 Grobid 解析);**Gather Evidence**(top-k=30 dense 检索后,由 LLM 对每个块做**重排 + 针对问题的上下文摘要并打相关分**,注入期刊、引用数等元数据,摘要存入 agent 状态);**Citation Traversal**(沿引用图向前/向后扩展相关论文,作为层级索引);**Generate Answer**(用排名靠前的 5–15 条摘要生成带引用的回答,可选择"信息不足")。温度均为 0,每个配置跑 3 次。**WikiCrow**:按基因的结构、功能、相互作用、临床意义等分节调用 PaperQA2,再拼接成文。**ContraCrow**:先用 LLM 从论文中抽取声明,再逐条交给 PaperQA2 判断文献中是否存在矛盾,输出 11 级 Likert 分(≥8 视为矛盾)。
<!-- EN --> **PaperQA2**: an agent (orchestration LLM fixed to gpt-4-turbo-2024-04-09) can repeatedly call four tools: **Paper Search** (rewrite the request as keyword search, fetch full texts, parse, chunk; Grobid parsing for WikiCrow); **Gather Evidence** (top-k=30 dense retrieval, then an LLM **reranks each chunk and writes a question-specific contextual summary with a relevance score**, injecting journal/citation-count metadata; summaries stored in agent state); **Citation Traversal** (expand along the citation graph forwards/backwards as hierarchical indexing); **Generate Answer** (answer with citations from the top 5–15 summaries, with an "insufficient information" option). Temperature 0, three runs per configuration. **WikiCrow**: section-wise PaperQA2 calls (structure, function, interactions, clinical significance) stitched into an article. **ContraCrow**: an LLM extracts claims from a paper; PaperQA2 then checks each against the literature and emits an 11-point Likert score (≥8 = contradiction).

## 数据 / Data
<!-- ZH --> **LitQA2**:248 道多选题,答案只出现在近期论文正文(不在摘要)且理想情况下全文献中唯一,允许"信息不足"选项;分两批构建(先 147 题,工程改进后再加 101 题用于检验过拟合)。**人类基线**:9 位生物学博士或在读博士,约一周、可用任何在线工具与机构文献、按题有现金激励。**WikiCrow**:240 个已有非 stub Wikipedia 条目的人类蛋白编码基因;盲评 375 条陈述。**ContraDetect**:由 LitQA2 改写为正确/错误陈述;另有 42 条"从未被报道"的陈述;实际应用于 93 篇随机生物学论文。
<!-- EN --> **LitQA2**: 248 multiple-choice questions whose answers appear only in the body (not abstract) of recent papers and ideally only once in the literature, with an "insufficient information" option; built in two stages (147 questions, then 101 more after engineering to test overfitting). **Human baseline**: 9 biology PhDs or PhD students, ~1 week, any online tools and institutional access, per-question cash incentives. **WikiCrow**: 240 human protein-coding genes with non-stub Wikipedia articles; 375 statements blind-graded. **ContraDetect**: LitQA2 rewritten into true/false statements, plus 42 "never-reported" statements; deployed on 93 random biology papers.

## 主要结果 / Key results
<!-- ZH --> **LitQA2**:每题平均解析 14.5 篇论文;精确率 **85.2%±1.1%**、准确率 **66.0%±1.2%**,21.9% 选择"信息不足";人类精确率 73.8%±9.6%、准确率 67.7%±11.9%——**精确率显著超人**(p=0.0036),准确率无显著差异(p=0.66)。PaperQA2 优于 Perplexity、Elicit、原版 PaperQA 及无 RAG 的前沿模型;新旧两批题准确率无显著差异(未过拟合)。**消融**:去掉 agent(固定流程)准确率显著下降(p=0.015);去掉 RCS 显著下降(p<0.001),但用小模型(GPT-3.5-Turbo、Llama3-70B)做 RCS 反而比不做更差——存在"理解力门槛";去掉 Citation Traversal 后 DOI 召回显著下降(p=0.022);top-k 深度 1→10 显著提升,10→30 收益递减;解析器与块大小影响不显著。**WikiCrow**:"引了但不支持"13.5% vs Wikipedia 24.9%(p=0.0075),无引用 3.5% vs 13.6%,精确率 86.1% vs 71.2%;推理类错误 12 vs 26(p=0.0144),归因类错误 10 vs 16(n.s.);每篇约 491.5 秒、$4.48。**ContraCrow**:ContraDetect 上 AUC **0.842**,阈值 8 时准确率 73%、精确率 88%、假阳性率 7%;"无证据"陈述 98% 正确判为无证据;93 篇论文平均每篇 35.16 条声明、**2.34±1.99** 条被判矛盾,专家验证一致 **70%**(折合每篇 1.64 条,F1 0.82)。但在不看模型推理的独立检测任务中,专家彼此一致 75.5%,与 ContraCrow 仅 60.4%(p=0.015),作者推测主要源于模型**过度自信**。
<!-- EN --> **LitQA2**: 14.5 papers parsed per question on average; precision **85.2%±1.1%**, accuracy **66.0%±1.2%**, "insufficient information" in 21.9%; humans 73.8%±9.6% precision and 67.7%±11.9% accuracy — **superhuman precision** (p=0.0036), accuracy not significantly different (p=0.66). PaperQA2 beats Perplexity, Elicit, original PaperQA and non-RAG frontier models; accuracy on old vs. new question batches does not differ (no overfitting). **Ablations**: removing the agent (fixed pipeline) significantly lowers accuracy (p=0.015); removing RCS significantly lowers it (p<0.001), but using small models (GPT-3.5-Turbo, Llama3-70B) for RCS is worse than no RCS — a comprehension threshold; removing Citation Traversal significantly lowers DOI recall (p=0.022); top-k depth 1→10 helps significantly with diminishing returns to 30; parser and chunk size are not significant. **WikiCrow**: "cited and unsupported" 13.5% vs. Wikipedia 24.9% (p=0.0075), uncited 3.5% vs. 13.6%, precision 86.1% vs. 71.2%; reasoning errors 12 vs. 26 (p=0.0144), attribution errors 10 vs. 16 (n.s.); ~491.5 s and $4.48 per article. **ContraCrow**: AUC **0.842** on ContraDetect; at threshold 8, 73% accuracy, 88% precision, 7% false-positive rate; "no evidence" correctly chosen for 98% of never-reported statements; on 93 papers, 35.16 claims and **2.34±1.99** flagged contradictions per paper, with **70%** expert agreement (1.64 per paper, F1 0.82). In an independent detection task without the model's reasoning, experts agree with each other 75.5% but with ContraCrow only 60.4% (p=0.015); the authors suspect model **overconfidence**.

## 创新点 / Contributions
- <!-- ZH --> 把 RAG 变成 agent 任务,并用 **RCS(重排 + 上下文摘要)**显著提升全文检索准确率;引用图遍历作为层级索引。 <!-- EN --> Turns RAG into an agent task, with **RCS (rerank + contextual summary)** substantially improving full-text retrieval, and citation-graph traversal as hierarchical indexing.
- <!-- ZH --> LitQA2:答案只在正文、全文献唯一、可按 DOI 判归因——兼顾准确与**出处正确**的基准设计。 <!-- EN --> LitQA2: answers only in the body, unique in the literature, attribution checkable by DOI — a benchmark that scores both correctness and **correct provenance**.
- <!-- ZH --> 精确率与准确率分开报告、允许拒答——把"知道自己不知道"纳入评价。 <!-- EN --> Separate precision and accuracy with abstention — "knowing what you don't know" is part of the score.
- <!-- ZH --> 声明级的"引用是否支持陈述"人工评估框架(cited-supported / uncited / cited-unsupported),以及大规模文献矛盾检测。 <!-- EN --> A statement-level human evaluation of "does the citation support the statement" (cited-supported / uncited / cited-unsupported), and literature-scale contradiction detection.

## 局限 / Limitations
- <!-- ZH --> 准确率并未超过人类(只有精确率超人);标题"superhuman"主要建立在精确率与 WikiCrow 对比上。 <!-- EN --> Accuracy does not exceed humans (only precision does); the "superhuman" headline rests mainly on precision and the WikiCrow comparison.
- <!-- ZH --> 人类基线小(LitQA2 仅 9 人);部分 LitQA2 题被搜索引擎收录导致第三轮人类测试作废;LitQA2 也是 PaperQA2 的开发集,作者用新批次缓解过拟合疑虑。 <!-- EN --> Small human baseline (9 people for LitQA2); some LitQA2 questions leaked into search indices, invalidating a third human round; LitQA2 also guided PaperQA2's development (a new batch was used to address overfitting).
- <!-- ZH --> ContraCrow 与独立专家一致性仅 60%,存在过度自信;且"矛盾"不等于"错误"(文献随时间更新)。 <!-- EN --> ContraCrow agrees with independent experts only ~60% and is overconfident; a "contradiction" is not necessarily an error (literature evolves).
- <!-- ZH --> 只处理文本;复现依赖作者的内部全文检索基础设施(开源版需自备全文库)。 <!-- EN --> Text only; full reproduction depends on the authors' internal full-text infrastructure (the open package needs your own corpus).

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> PaperQA2 不分析组学数据,但它是 **Agent 可信度课题** 中"证据-声明"一侧的成熟参照:**(1)** WikiCrow 的 cited-supported / uncited / cited-unsupported 三分类,以及"推理错误 vs 归因错误"的再细分,可直接作为我们 claim-to-evidence 核查的标签体系——只是我们的"证据"不是论文段落,而是 agent 自己生成的表格、图和统计量;**(2)** 精确率/准确率分离 + 允许拒答,是我们设计校准 verifier 时应当保留的评估口径("不确定"应当是合法输出);**(3)** ContraCrow 与人类独立判断仅 60% 一致、作者归因于过度自信——这恰恰说明 LLM 当证据审查者时需要校准,是 Agent 可信度课题的直接动机证据。对 detect → model → revert 主链,它属于证据层:当 pipeline 提名一个可逆转肾脏异常的基因时,可以用 PaperQA2 类系统检索文献支持/矛盾,但要按 RCS 消融的教训使用足够强的模型做证据摘要。与 DeepEvidence(结构化知识库 + 证据图)互补:PaperQA2 擅长非结构化全文。
<!-- EN --> PaperQA2 does not analyse omics data, but it is the mature reference for the "evidence–claim" side of **the agent-trustworthiness topic**: **(1)** WikiCrow's cited-supported / uncited / cited-unsupported labels, with the further split into reasoning vs. attribution errors, can serve as our claim-to-evidence label set — except our "evidence" is not a paper passage but the agent's own tables, figures and statistics; **(2)** separating precision from accuracy with abstention is the evaluation framing a calibrated verifier should keep ("uncertain" must be a legal output); **(3)** ContraCrow's ~60% agreement with independent humans, attributed to overconfidence, is direct motivating evidence that LLM evidence-checkers need calibration. On detect → model → revert it belongs to the evidence layer: when the pipeline nominates a gene that would revert a kidney anomaly, a PaperQA2-like system can retrieve supporting/contradicting literature — using a strong enough model for evidence summarisation, per the RCS ablation. It complements DeepEvidence (structured knowledge bases + evidence graph): PaperQA2 is strong on unstructured full text.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码:** 开源 paperqa 包(含实验配置对象;不含 Grobid 解析、全文检索与引用遍历的内部实现)。 <!-- EN --> **Code:** the open paperqa package (with experiment configs; internal Grobid parsing, full-text search and citation traversal not included).
<!-- ZH/EN --> <https://github.com/Future-House/paper-qa>
- <!-- ZH --> **数据:** WikiCrow 生成文章(公开 GCS bucket);LitQA2、评估者回答与矛盾声明见补充材料。 <!-- EN --> **Data:** WikiCrow articles (public GCS bucket); LitQA2, evaluator responses and contradiction claims in the supplement.
<!-- ZH/EN --> <https://storage.googleapis.com/fh-public/wikicrow2/>
- <!-- ZH --> **评估框架:** 陈述级三分类 + 错误再分类;ContraCrow 的 11 级 Likert 量表。 <!-- EN --> **Eval framework:** the three-way statement labels + error sub-typing; ContraCrow's 11-point Likert scale.

## 待读 / Follow-ups
- <!-- ZH --> LAB-Bench(本仓库 `lab-bench-arxiv-2024`,LitQA 的来源)。 <!-- EN --> LAB-Bench (`lab-bench-arxiv-2024`, origin of LitQA).
- <!-- ZH --> FutureHouse 的后续:Robin、Kosmos(本仓库已有条目),看 PaperQA2 如何嵌入更大的发现系统。 <!-- EN --> FutureHouse follow-ups Robin and Kosmos (in this repo) — how PaperQA2 is embedded in larger discovery systems.
- <!-- ZH --> 引用忠实度相关工作(`citation-faithfulness-arxiv-2026`、`sourcecheckup-natcommun-2025`)对"引用支持"的更严格评估。 <!-- EN --> Citation-faithfulness work (`citation-faithfulness-arxiv-2026`, `sourcecheckup-natcommun-2025`) for stricter "citation supports claim" evaluation.

## 引用 / Cite
```bibtex
@misc{Skarlinski2024_240913740,
  title = {Language agents achieve superhuman synthesis of scientific knowledge},
  author = {Skarlinski, Michael D. and Cox, Sam and Laurent, Jon M. and Braza, James D. and Hinks, Michaela and Hammerling, Michael J. and Ponnapati, Manvitha and Rodriques, Samuel G. and White, Andrew D.},
  year = {2024},
  eprint = {2409.13740},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL},
  url = {https://arxiv.org/abs/2409.13740}
}
```

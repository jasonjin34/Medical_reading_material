# BixBench: a Comprehensive Benchmark for LLM-based Agents in Computational Biology

> **Bibkey** `Mitchener2025_250300096` · **Venue** arXiv preprint (2025) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2503.00096>
> `status: complete` — 基于 arXiv v3(2025-10-08)全文精读。注意:v1 摘要写的是「50+ 场景、近 300 题、17% 准确率」;v3 正文为 **61 个 capsule、205 题、最佳 21%**,本笔记以 v3 为准。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> BixBench(FutureHouse + ScienceMachine)是第一批面向**开放式生物信息学数据分析**的 agent 基准:61 个由 PhD 级分析师构建的真实分析「capsule」(数据 + 假设 + 参考 notebook)、205 道开放答案题;agent 在空白 Jupyter notebook 里自主探索数据并作答。GPT-4o 与 Claude 3.5 Sonnet 在开放答案下最高仅 **21%**,MCQ(带「信息不足」选项)下接近随机。
<!-- EN --> BixBench (FutureHouse + ScienceMachine) is one of the first agent benchmarks for **open-ended bioinformatics data analysis**: 61 real analysis "capsules" (data + hypothesis + reference notebook) built by PhD-level analysts, with 205 open-answer questions; the agent explores the data in an empty Jupyter notebook and answers. GPT-4o and Claude 3.5 Sonnet reach at best **21%** open-answer accuracy, and near-random in the MCQ setting with an "insufficient information" option.

## 研究问题 / Problem
<!-- ZH --> 科学 agent 基准正从记忆型问答转向文献综述、实验规划等实用任务,但生物信息学 —— 作者认为最可能率先实现全自动发现的领域 —— 缺少测量「自主探索数据、执行长链多步分析、解读细微结果」能力的大规模基准。已有的数据科学基准要么依赖简单奖励函数(RE-Bench 的训练 loss),要么人为约束产出物与统计选择(BLADE)。
<!-- EN --> Science-agent benchmarks are moving from recall QA to practical tasks like literature review and experiment planning, but bioinformatics — which the authors see as the field where fully autonomous discovery may arrive first — lacks a broad benchmark of an agent's ability to explore datasets, run long multi-step analyses and interpret nuanced results. Existing data-science benchmarks either use a simple reward (training loss in RE-Bench) or artificially constrain artifacts and statistical choices (BLADE).

## 方法 / Method
<!-- ZH --> **Capsule 构建**:招募 PhD(或在读)生物信息分析师,在 Google Colab 模板 notebook 中复现已发表分析或基于自带数据做新分析;每个 capsule 包含研究问题/假设、输入数据、分析代码,外加结果描述与「假设是否成立」的 true/false 答案;经作者与其他分析师审查。**出题**:用 Claude 3.5 Sonnet 读改写后的 notebook + 假设/结果,每 capsule 两轮各 4 道 MCQ 草稿;专家逐题 Approve/Reject 并可编辑(可看到原 capsule);再用 LLM 三次重复做去重(约 95% 一致)。最终 205 题,每 capsule 1–7 题(平均 3.8)。**评测环境**:基于 Aviary(FutureHouse 的语言 agent gym)的 SimpleAgent;预装大量 Python/R/bash 生信包的 Docker 镜像(BixBench-env:v1.0);三个工具 `edit_cell`、`list_workdir`、`submit_answer`;每次改动都全量重跑 notebook。**两种评分**:(1) 开放答案 —— judge LLM(Claude 3.5 Sonnet)将答案与 ground truth 比较,二值打分;每个 capsule 并行跑 5 次;(2) MCQ —— 另一个 LLM 读完整 notebook 和开放答案,从选项中选择,可选「Insufficient information」拒答;对 5 次做多数投票并报告 precision(只算未拒答的)。另设「无 notebook 纯记忆」基线。共 1,220 条轨迹(305 条 × 2 模型 × 有/无图像)。
<!-- EN --> **Capsules**: PhD-level (or candidate) bioinformatics analysts, working in a Google Colab template notebook, recapitulate published analyses or run de novo analyses on data they provide; each capsule has a research question/hypothesis, input data and analysis code, plus a result description and a true/false answer on whether the hypothesis held; reviewed by the authors and other analysts. **Questions**: Claude 3.5 Sonnet drafts MCQs from a modified notebook plus hypothesis/result, two rounds of four per capsule; experts approve/reject with full edit access (seeing the original capsule); an LLM de-duplicates in triplicate (~95% concordance). Final: 205 questions, 1–7 per capsule (mean 3.8). **Environment**: Aviary (FutureHouse's language-agent gym) SimpleAgent; a Docker image pre-loaded with Python/R/bash bioinformatics packages (BixBench-env:v1.0); three tools `edit_cell`, `list_workdir`, `submit_answer`; every edit reruns the whole notebook. **Two scoring regimes**: (1) open-answer — a judge LLM (Claude 3.5 Sonnet) compares the answer with ground truth, binary score, each capsule run 5 times in parallel; (2) MCQ — a second LLM reads the full notebook and open answer and picks an option, optionally an "Insufficient information" refusal; majority vote over 5 runs, with precision over non-refused answers. A "no notebook, pure recall" baseline is also reported. 1,220 trajectories in total (305 × 2 models × with/without images).

## 数据 / Data
<!-- ZH --> 61 个 capsule、205 道题,覆盖多种自选分析类别(论文图 2 直方图,如差异表达、聚类等);数据文件格式与目录结构异构(csv、rds 等),要求 agent 自行导航与选库加载。题目设计为必须完成分析才能回答(而非靠记忆)。数据集公开于 HuggingFace,评测代码开源。
<!-- EN --> 61 capsules and 205 questions spanning a range of self-selected analysis categories (histogram in Fig. 2, e.g. differential expression, clustering); data files are heterogeneous in format and layout (csv, rds, …), so agents must navigate and pick libraries themselves. Questions are designed to require completing an analysis rather than recall. Dataset on HuggingFace; evaluation code open source.

## 主要结果 / Key results
<!-- ZH --> **开放答案**:Claude 3.5 Sonnet **21%** vs GPT-4o **15%**。**MCQ + 拒答选项**:两者都接近随机 —— 模型在复杂分析情境下倾向于选「信息不足」;**MCQ 无拒答选项**:性能上升并高于随机,但作者推测主要来自**模型记忆而非 notebook 中的分析**;且所有设定都**没有超过「不给 notebook 的纯记忆基线」**。5 次多数投票随票数增加没有显著改善。**图像消融**:禁止 agent 画图对结果无显著影响(作者观察到模型对 notebook 中的图解读很差)。推理模型(o1、DeepSeek R1)在初步测试中因长上下文与结构化工具调用而表现不佳,未纳入。未提供人类专家基线。
<!-- EN --> **Open-answer**: Claude 3.5 Sonnet **21%** vs GPT-4o **15%**. **MCQ with refusal**: both near random — models tend to opt out ("insufficient information") in complex analytical contexts; **MCQ without refusal**: performance rises above random, which the authors attribute largely to **answering from recall rather than from the analysis**; and no setting **beats the "no-notebook, pure recall" baseline**. Majority voting over 5 runs gives no significant gain as votes accumulate. **Image ablation**: forbidding plots made no significant difference (the authors note models interpret notebook plots poorly). Reasoning models (o1, DeepSeek R1) struggled in pilot tests with long contexts and structured tool use and were excluded. No human-expert baseline is provided.

## 创新点 / Contributions
- <!-- ZH --> 61 个专家策划、带真实数据与参考 notebook 的开放式生信分析场景 + 205 道开放答案题。 <!-- EN --> 61 expert-curated open-ended bioinformatics scenarios with real data and reference notebooks, plus 205 open-answer questions.
- <!-- ZH --> 开源的 notebook 式 agent 环境(Aviary + Docker + 三工具),可复现地评估 Python/R/bash 分析轨迹。 <!-- EN --> An open-source notebook-style agent environment (Aviary + Docker + three tools) for reproducibly evaluating Python/R/bash trajectories.
- <!-- ZH --> 把**拒答选项**与**纯记忆基线**作为校准手段:揭示 MCQ 分数会被记忆抬高,而在可拒答时模型倾向放弃。 <!-- EN --> Uses a **refusal option** and a **pure-recall baseline** as calibration, revealing that MCQ scores are inflated by recall and that models opt out when allowed.
- <!-- ZH --> 每 capsule 5 次并行重跑,天然提供逐题的重跑一致性数据(附录图 7–8)。 <!-- EN --> Five parallel runs per capsule, providing per-question rerun-consistency data (App. Figs 7–8).

## 局限 / Limitations
- <!-- ZH --> **只打最终答案**(二值),无法区分「方法对答案偏」与「方法错答案碰巧对」—— 这正是 BiomniBench 批评的点。 <!-- EN --> **Final-answer only** (binary), so it cannot separate "sound method, slightly off" from "wrong method, lucky answer" — exactly BiomniBench's critique.
- <!-- ZH --> 题目由 LLM 起草、人工审核,judge 也是 LLM(且与被测模型之一同为 Claude 3.5 Sonnet),未报告 judge 与人工一致性。 <!-- EN --> Questions are LLM-drafted then human-reviewed, and the judge is an LLM (the same Claude 3.5 Sonnet as one evaluated model), with no reported judge–human agreement.
- <!-- ZH --> 只评测两个模型、一个简单 scaffold;无人类基线;覆盖面作者自认远不完整。 <!-- EN --> Only two models and one simple scaffold; no human baseline; coverage is admittedly far from comprehensive.
- <!-- ZH --> 版本间数字变化(v1:50+ 场景/近 300 题/17%;v3:61/205/21%),引用时需注明版本。 <!-- EN --> Numbers changed across versions (v1: 50+ scenarios / ~300 questions / 17%; v3: 61 / 205 / 21%); cite the version.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 对 **Plan B**,BixBench 是「结果级(outcome-level)」评估的代表,恰好可以作为我们 claim-to-evidence 验证的**对照组**:它证明了(1) MCQ 分数会被记忆抬高 —— 带「纯记忆基线」和「拒答选项」的做法应直接纳入我们的协议,用以区分 agent 的结论是来自它跑的 omics 分析,还是来自先验知识;(2) 每题 5 次并行运行的逐题准确率分布(附录图 7–8)是 rerun stability 的早期证据。它的空白:没有检查 notebook 中的中间结论是否被数据支持,也没有 judge 校准 —— 这两点正是 Plan B 的 calibrated verifier 要补的。对 **Plan A**,它的 capsule 结构(假设 + 数据 + 参考 notebook + true/false 结论)是把 KPMP/Lake 公开数据上的分析打包成可复用任务的好模板;将来 KidneyAnomalyBench 若扩展出「agent 分析异常区域」任务,可直接沿用 capsule 格式与 Aviary 环境。对 detect → model → revert 主线,它提示:agent 在生信分析上远未可靠(最佳 21%),在 pipeline 中只能作为需验证的助手。
<!-- EN --> For **Plan B**, BixBench is the archetype of outcome-level evaluation and a natural **control** for our claim-to-evidence verification: it shows (1) MCQ scores are inflated by recall — its pure-recall baseline and refusal option should be adopted in our protocol to tell whether an agent's conclusion comes from the omics analysis it ran or from prior knowledge; (2) its per-question accuracy across five parallel runs (App. Figs 7–8) is early evidence for rerun stability. Its gap: it never checks whether intermediate conclusions in the notebook are supported by the data, and it does not calibrate its judge — precisely what Plan B's calibrated verifier adds. For **Plan A**, its capsule structure (hypothesis + data + reference notebook + true/false conclusion) is a good template for packaging analyses on KPMP/Lake public data as reusable tasks; if KidneyAnomalyBench grows an "agent analyses the anomalous region" track, the capsule format and Aviary environment can be reused directly. For the detect → model → revert line, it says agents are far from reliable at bioinformatics (best 21%) and can only be assistants whose output is verified.

## 可复用资产 / Reusable assets
- <!-- ZH --> **数据集:** BixBench(capsule + 题目)。 <!-- EN --> **Dataset:** BixBench (capsules + questions).
<!-- ZH/EN --> <https://huggingface.co/datasets/futurehouse/BixBench>
- <!-- ZH --> **评测框架与代码:** <!-- EN --> **Eval harness and code:**
<!-- ZH/EN --> <https://github.com/Future-House/BixBench>
- <!-- ZH --> **Agent 环境:** Aviary(SimpleAgent)+ BixBench-env Docker 镜像。 <!-- EN --> **Agent environment:** Aviary (SimpleAgent) + the BixBench-env Docker image.
- <!-- ZH --> **协议设计:** 纯记忆基线、拒答选项、5 次重跑多数投票、precision vs accuracy 的区分。 <!-- EN --> **Protocol ideas:** pure-recall baseline, refusal option, 5-run majority vote, precision vs accuracy.

## 待读 / Follow-ups
- <!-- ZH --> Aviary(arXiv 2412.21154)与 LAB-Bench(lab-bench-arxiv-2024),同一团队的前作。 <!-- EN --> Aviary (arXiv 2412.21154) and LAB-Bench (lab-bench-arxiv-2024), the same team's prior work.
- <!-- ZH --> 后续报告 BixBench 分数的 agent 系统,以及分数如何随模型代际变化。 <!-- EN --> Later agent systems that report BixBench scores, and how scores move with model generations.
- <!-- ZH --> ScienceAgentBench、DiscoveryBench、CORE-Bench(可复现性)作为同类对照。 <!-- EN --> ScienceAgentBench, DiscoveryBench and CORE-Bench (reproducibility) as comparators.

## 引用 / Cite
```bibtex
@misc{Mitchener2025_250300096,
  title = {BixBench: a Comprehensive Benchmark for LLM-based Agents in Computational Biology},
  author = {Ludovico Mitchener and Jon M Laurent and Alex Andonian and Benjamin Tenmann and Siddharth Narayanan and Geemi P Wellawatte and Andrew White and Lorenzo Sani and Samuel G Rodriques},
  year = {2025},
  eprint = {2503.00096},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2503.00096}
}
```

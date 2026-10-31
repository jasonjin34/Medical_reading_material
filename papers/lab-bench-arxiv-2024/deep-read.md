# LAB-Bench: Measuring Capabilities of Language Models for Biology Research

> **Bibkey** `Laurent2024_240710362` · **Venue** arXiv preprint (2024) · **Category** agents · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2407.10362>
> `status: complete` — 基于 arXiv v3(2024-07-17)全文精读(作者注:投稿 NeurIPS 2024 Datasets & Benchmarks,审稿中)。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> LAB-Bench(FutureHouse)是一个面向**实用生物学研究能力**的 2,457 道多选题基准:文献检索与推理(LitQA2、SuppQA)、图表解读(FigQA、TableQA)、数据库查询(DbQA)、实验方案排错(ProtocolQA)、序列理解与操作(SeqQA、Cloning Scenarios);每题都有「信息不足」拒答选项,同时报告 accuracy、precision 与 coverage,并对比 PhD 级人类专家。不带工具的前沿模型整体远逊于人类。
<!-- EN --> LAB-Bench (FutureHouse) is a 2,457-question multiple-choice benchmark of **practical biology-research capabilities**: literature retrieval and reasoning (LitQA2, SuppQA), figure/table interpretation (FigQA, TableQA), database access (DbQA), protocol troubleshooting (ProtocolQA), and sequence comprehension/manipulation (SeqQA, Cloning Scenarios). Every question has an "insufficient information" refusal option; accuracy, precision and coverage are reported against PhD-level human experts. Tool-free frontier models fall well short of humans overall.

## 研究问题 / Problem
<!-- ZH --> 现有科学基准大多测「教科书式」知识回忆与推理,而非科研中真正需要的实用任务(文献检索、方案规划、数据分析)。要开发能当科研助手的 AI 系统,需要衡量这些实际能力的基准,以及人类专家基线。
<!-- EN --> Existing science benchmarks mostly test "textbook" recall and reasoning rather than the practical tasks research requires (literature search, protocol planning, data analysis). Building AI research assistants needs benchmarks for these capabilities, with human-expert baselines.

## 方法 / Method
<!-- ZH --> **出题**:SeqQA、DbQA 的子任务主要程序化生成;LitQA2、SuppQA、FigQA、TableQA、ProtocolQA、Cloning Scenarios 由作者和外包生物学专家手工编写。作者发现一个可推广的出题策略:让前沿模型先生成候选题,找出其中「荒谬」或「选项中没有正确答案」的题,再人工修订 —— 这样常得到模型难以回答的高质量题(作者称之为探测模型推理的「null space」)。**各子集设计**:LitQA2 的答案通常只在一篇较新论文正文中出现一次、摘要中无法得到;SuppQA 只能从补充材料中找到;FigQA/TableQA 只给图/表图像(无图注);DbQA 覆盖多个数据库以防单一 API 通吃;ProtocolQA 把已发表方案改错或删步,问如何修复;Cloning Scenarios 是 41 道「人类也难」的多步克隆题(训练有素的分子生物学家约需 10 分钟以上)。**评测**:0-shot chain-of-thought,从文本补全中解析答案,**不给任何工具(包括联网)**;每题都有拒答选项,报告 accuracy(对/全部)、precision(对/作答)、coverage(作答/全部);三次运行取标准差。约 80% 题目公开,20% 保留以监测污染。人类基线:PhD 级生物学研究者以「quiz」形式作答,可用互联网和日常工具(并提供免费序列软件),要求不用 AI 工具(无法强制),按表现与完成度激励。另做小规模**开放答案**验证(Claude 3.5 Sonnet、GPT-4o)。
<!-- EN --> **Question generation**: SeqQA and DbQA subtasks are mostly programmatic; LitQA2, SuppQA, FigQA, TableQA, ProtocolQA and Cloning Scenarios were hand-written by the authors and contracted biology experts. The authors report a generalizable strategy: have frontier models propose candidate questions, identify nonsensical ones or ones with no correct option, then revise manually — yielding high-quality questions models struggle with (probing the "null space" of model reasoning). **Subset design**: LitQA2 answers are typically attested once in a recent paper's main text and not answerable from abstracts; SuppQA only from supplementary material; FigQA/TableQA give only the figure/table image (no caption); DbQA spans many databases so no single API suffices; ProtocolQA introduces errors into published protocols and asks how to fix them; Cloning Scenarios are 41 "human-hard" multi-step cloning questions (>10 min for a trained molecular biologist). **Evaluation**: 0-shot chain-of-thought, answers parsed from text completions, **no tools at all (including internet)**; a refusal option on every question; accuracy (correct/all), precision (correct/attempted), coverage (attempted/all); SD over three runs. ~80% of questions are public; 20% held back to monitor contamination. Human baseline: PhD-level biologists answering "quizzes" with internet and everyday tools (plus free sequence software), asked (not enforceably) not to use AI tools, incentivized for performance and completion. A small **open-answer** check (Claude 3.5 Sonnet, GPT-4o) is added.

## 数据 / Data
<!-- ZH --> 共 2,457 题(人类覆盖 69%):LitQA2 248、SuppQA 102、FigQA 226、TableQA 305、DbQA 650(10 个子任务)、ProtocolQA 135、SeqQA 750(15 个子任务)、Cloning Scenarios 41。公开子集在 HuggingFace。评测模型:Claude 3.5 Sonnet、Claude 3 Opus、Gemini 1.5 Pro、GPT-4o、GPT-4-turbo、Claude 3 Haiku、Llama-3-70B-Instruct(非多模态,未测 FigQA/TableQA)。
<!-- EN --> 2,457 questions (69% covered by humans): LitQA2 248, SuppQA 102, FigQA 226, TableQA 305, DbQA 650 (10 subtasks), ProtocolQA 135, SeqQA 750 (15 subtasks), Cloning Scenarios 41. Public subset on HuggingFace. Models: Claude 3.5 Sonnet, Claude 3 Opus, Gemini 1.5 Pro, GPT-4o, GPT-4-turbo, Claude 3 Haiku, Llama-3-70B-Instruct (not multimodal; no FigQA/TableQA).

## 主要结果 / Key results
<!-- ZH --> **人类专家在 accuracy 与 precision 上整体大幅领先模型**,且作答覆盖率更高。分项(文本描述;主图为柱状图):**LitQA2** 各模型 precision 约 40%,高于随机,但前沿模型常拒答(有的作答 < 20%),导致 accuracy 低于随机;**SuppQA** 覆盖率最低,模型多数拒答;**FigQA** 最难 —— 除 Claude 3.5 Sonnet 外所有模型 precision 接近随机;**TableQA** 最容易,Claude 3.5 Sonnet accuracy 与人类持平、precision 略超人类;**DbQA** 常拒答、表现差;**SeqQA** precision 约 40–50%,子任务差异大(PCR-seq-enzprimers 等可达 90% 以上;涉及长序列子串、酶切片段数/长度的子任务最差;只给基因名而非序列时性能普遍下降);**ProtocolQA** 各模型约 50–60% precision;**Cloning Scenarios** 远低于人类。ORF-transeff 子任务上 Claude 3.5 Sonnet precision 0.88 vs 人类 0.75。**开放答案**小实验:Cloning Scenarios 两模型 accuracy 仅 0.20(10 题中对的 2 题都是靠猜最常见的酶 BsaI 或抗生素 Ampicillin/Carbenicillin),FigQA 0.30,ProtocolQA Claude 0.30 vs GPT-4o 0.20 —— 说明 MCQ 上高于随机的成绩部分来自**排除干扰项再猜**的应试技巧。
<!-- EN --> **Human experts substantially outperform models on accuracy and precision overall**, with higher coverage. By category (from the text; main figure is a bar chart): **LitQA2** precision ~40% for all models, above random, but frontier models often refuse (some attempt < 20%), pushing accuracy below random; **SuppQA** has the lowest coverage — models mostly refuse; **FigQA** is hardest — near-random precision for all except Claude 3.5 Sonnet; **TableQA** is easiest, Claude 3.5 Sonnet equalling human accuracy and narrowly beating human precision; **DbQA** frequent refusals, poor performance; **SeqQA** precision ~40–50% with large subtask variation (> 90% on e.g. PCR-seq-enzprimers; worst on long-sequence subsequence and restriction-fragment count/length tasks; drops when given a gene name instead of a sequence); **ProtocolQA** ~50–60% precision; **Cloning Scenarios** well below humans. On ORF-transeff, Claude 3.5 Sonnet beats humans (0.88 vs 0.75 precision). **Open-answer** check: Cloning Scenarios accuracy only 0.20 for both models (the two correct of ten were guesses of the most common enzyme BsaI or antibiotic Ampicillin/Carbenicillin), FigQA 0.30, ProtocolQA Claude 0.30 vs GPT-4o 0.20 — so above-random MCQ scores partly reflect **test-taking by eliminating distractors and guessing**.

## 创新点 / Contributions
- <!-- ZH --> 第一个系统覆盖「实用科研技能」的大规模生物学基准,带人类专家基线。 <!-- EN --> The first large biology benchmark systematically covering practical research skills, with human-expert baselines.
- <!-- ZH --> 每题提供拒答选项,并把 accuracy / precision / coverage 分开报告 —— 把「知道自己不知道」纳入评估。 <!-- EN --> A refusal option on every question with accuracy / precision / coverage reported separately — putting "knowing what you don't know" into the evaluation.
- <!-- ZH --> 用开放答案复核 MCQ,揭示高质量干扰项的重要性与「应试」偏差。 <!-- EN --> Open-answer re-checks of MCQs, exposing the importance of good distractors and test-taking bias.
- <!-- ZH --> 保留 20% 私有题监测污染;提出「人类基线将被人类可行性证明(proof-of-possibility)取代」的观点。 <!-- EN --> A 20% private split to monitor contamination; the view that human baselines on hard tasks will give way to human "proofs-of-possibility".

## 局限 / Limitations
- <!-- ZH --> 全是多选题,且本文只评测**不带工具**的模型;LitQA2、SuppQA、DbQA、SeqQA 本应依赖工具,这里测的更像是「拒答倾向 + 记忆」。 <!-- EN --> All MCQ, and this paper evaluates only **tool-free** models; LitQA2, SuppQA, DbQA and SeqQA are meant to be tool-dependent, so results mostly measure refusal tendency + recall.
- <!-- ZH --> 开放答案验证规模很小(每类约 10 题、两个模型)。 <!-- EN --> The open-answer validation is tiny (~10 questions per category, two models).
- <!-- ZH --> 人类基线覆盖 69% 题目,DbQA 仅 35%;人类不使用 AI 工具无法强制。 <!-- EN --> Human baseline covers 69% of questions (DbQA only 35%); the no-AI-tools rule for humans is unenforceable.
- <!-- ZH --> 不含多步数据分析或组学数据处理;任务以分子生物学与文献为主。 <!-- EN --> No multi-step data analysis or omics processing; tasks centre on molecular biology and literature.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 对 **Agent 可信度课题**,LAB-Bench 提供了两条可直接借用的评估纪律:(1) **拒答选项 + accuracy/precision/coverage 三分**,即「选择性预测」的雏形 —— 我们的 calibrated verifier 本质上就是要在 coverage 与 precision 之间做有保证的权衡(何时该说「证据不足」);(2) **用开放答案复核 MCQ**,揭示模型可以靠排除干扰项得到虚高分数 —— 评估 agent 对肾脏 omics 结论的验证时,不能只用多选格式。LitQA2 也是 PaperQA2、DeepEvidence 等文献 agent 的标准评测集,是 claim-to-evidence(文献侧)验证的常用基准。对 **伪影注入课题** 关系较弱:它不涉及组学数据分析或异常检测;但 TableQA/FigQA 显示模型读图能力有限,提醒我们若让 agent 解读 H&E/Xenium 可视化结果,必须有独立验证。对 detect → model → revert 主线,它属于「agent 能否当可靠科研助手」的背景基准。
<!-- EN --> For **the agent-trustworthiness topic**, LAB-Bench offers two directly borrowable evaluation disciplines: (1) **a refusal option with accuracy/precision/coverage split** — a precursor of selective prediction; our calibrated verifier is essentially a guaranteed trade-off between coverage and precision (when to say "insufficient evidence"); (2) **open-answer re-checks of MCQs**, showing models inflate scores by eliminating distractors — so verifying agents' kidney-omics conclusions cannot rely on multiple-choice formats. LitQA2 is also the standard evaluation set for literature agents such as PaperQA2 and DeepEvidence, i.e. a common benchmark for the literature side of claim-to-evidence verification. Its link to **the artifact-injection topic** is weak: no omics analysis or anomaly detection; but TableQA/FigQA show limited figure reading, a reminder that agents interpreting H&E/Xenium visualizations need independent verification. For the detect → model → revert line, it is background on whether agents can be reliable research assistants.

## 可复用资产 / Reusable assets
- <!-- ZH --> **数据集(公开 ~80%):** <!-- EN --> **Dataset (public ~80%):**
<!-- ZH/EN --> <https://huggingface.co/datasets/futurehouse/lab-bench>
- <!-- ZH --> **评测口径:** 拒答选项 + accuracy / precision / coverage;20% 私有集监测污染。 <!-- EN --> **Metric convention:** refusal option + accuracy / precision / coverage; a 20% private split for contamination monitoring.
- <!-- ZH --> **出题方法:** 让模型生成候选题 → 找出荒谬/无解题 → 人工修订。 <!-- EN --> **Question-authoring recipe:** model-generated candidates → flag nonsensical/unanswerable ones → manual revision.

## 待读 / Follow-ups
- <!-- ZH --> LAB-Bench2(Laurent et al. 2026,arXiv 2604.09554)。 <!-- EN --> LAB-Bench2 (Laurent et al. 2026, arXiv 2604.09554).
- <!-- ZH --> PaperQA2(paperqa2-arxiv-2024)在 LitQA2 上的带工具结果。 <!-- EN --> PaperQA2's (paperqa2-arxiv-2024) tool-augmented LitQA2 results.
- <!-- ZH --> 同团队的 BixBench(bixbench-arxiv-2025),从 MCQ 走向开放式数据分析。 <!-- EN --> The same team's BixBench (bixbench-arxiv-2025), moving from MCQ to open-ended data analysis.

## 引用 / Cite
```bibtex
@misc{Laurent2024_240710362,
  title = {LAB-Bench: Measuring Capabilities of Language Models for Biology Research},
  author = {Jon M. Laurent and Joseph D. Janizek and Michael Ruzo and Michaela M. Hinks and Michael J. Hammerling and Siddharth Narayanan and Manvitha Ponnapati and Andrew D. White and Samuel G. Rodriques},
  year = {2024},
  eprint = {2407.10362},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2407.10362}
}
```

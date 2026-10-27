# BixBench: a Comprehensive Benchmark for LLM-based Agents in Computational Biology

> **文献键** `Mitchener2025_250300096` · **来源** arXiv preprint(2025) · **类别** agents · **相关度** high · **获取** open
> **链接** <https://arxiv.org/abs/2503.00096> · `status: complete`

---

## 一句话
BixBench(FutureHouse + ScienceMachine)是第一批面向**开放式生物信息学数据分析**的 agent 基准:61 个由 PhD 级分析师构建的真实分析「capsule」(数据 + 假设 + 参考 notebook)、205 道开放答案题;agent 在空白 Jupyter notebook 里自主探索数据并作答。GPT-4o 与 Claude 3.5 Sonnet 在开放答案下最高仅 **21%**,MCQ(带「信息不足」选项)下接近随机。

## 研究问题
科学 agent 基准正从记忆型问答转向文献综述、实验规划等实用任务,但生物信息学 —— 作者认为最可能率先实现全自动发现的领域 —— 缺少测量「自主探索数据、执行长链多步分析、解读细微结果」能力的大规模基准。已有的数据科学基准要么依赖简单奖励函数(RE-Bench 的训练 loss),要么人为约束产出物与统计选择(BLADE)。

## 方法
**Capsule 构建**:招募 PhD(或在读)生物信息分析师,在 Google Colab 模板 notebook 中复现已发表分析或基于自带数据做新分析;每个 capsule 包含研究问题/假设、输入数据、分析代码,外加结果描述与「假设是否成立」的 true/false 答案;经作者与其他分析师审查。**出题**:用 Claude 3.5 Sonnet 读改写后的 notebook + 假设/结果,每 capsule 两轮各 4 道 MCQ 草稿;专家逐题 Approve/Reject 并可编辑(可看到原 capsule);再用 LLM 三次重复做去重(约 95% 一致)。最终 205 题,每 capsule 1–7 题(平均 3.8)。**评测环境**:基于 Aviary(FutureHouse 的语言 agent gym)的 SimpleAgent;预装大量 Python/R/bash 生信包的 Docker 镜像(BixBench-env:v1.0);三个工具 `edit_cell`、`list_workdir`、`submit_answer`;每次改动都全量重跑 notebook。**两种评分**:(1) 开放答案 —— judge LLM(Claude 3.5 Sonnet)将答案与 ground truth 比较,二值打分;每个 capsule 并行跑 5 次;(2) MCQ —— 另一个 LLM 读完整 notebook 和开放答案,从选项中选择,可选「Insufficient information」拒答;对 5 次做多数投票并报告 precision(只算未拒答的)。另设「无 notebook 纯记忆」基线。共 1,220 条轨迹(305 条 × 2 模型 × 有/无图像)。

## 数据
61 个 capsule、205 道题,覆盖多种自选分析类别(论文图 2 直方图,如差异表达、聚类等);数据文件格式与目录结构异构(csv、rds 等),要求 agent 自行导航与选库加载。题目设计为必须完成分析才能回答(而非靠记忆)。数据集公开于 HuggingFace,评测代码开源。

## 主要结果
**开放答案**:Claude 3.5 Sonnet **21%** vs GPT-4o **15%**。**MCQ + 拒答选项**:两者都接近随机 —— 模型在复杂分析情境下倾向于选「信息不足」;**MCQ 无拒答选项**:性能上升并高于随机,但作者推测主要来自**模型记忆而非 notebook 中的分析**;且所有设定都**没有超过「不给 notebook 的纯记忆基线」**。5 次多数投票随票数增加没有显著改善。**图像消融**:禁止 agent 画图对结果无显著影响(作者观察到模型对 notebook 中的图解读很差)。推理模型(o1、DeepSeek R1)在初步测试中因长上下文与结构化工具调用而表现不佳,未纳入。未提供人类专家基线。

## 创新点
- 61 个专家策划、带真实数据与参考 notebook 的开放式生信分析场景 + 205 道开放答案题。
- 开源的 notebook 式 agent 环境(Aviary + Docker + 三工具),可复现地评估 Python/R/bash 分析轨迹。
- 把**拒答选项**与**纯记忆基线**作为校准手段:揭示 MCQ 分数会被记忆抬高,而在可拒答时模型倾向放弃。
- 每 capsule 5 次并行重跑,天然提供逐题的重跑一致性数据(附录图 7–8)。

## 局限
- **只打最终答案**(二值),无法区分「方法对答案偏」与「方法错答案碰巧对」—— 这正是 BiomniBench 批评的点。
- 题目由 LLM 起草、人工审核,judge 也是 LLM(且与被测模型之一同为 Claude 3.5 Sonnet),未报告 judge 与人工一致性。
- 只评测两个模型、一个简单 scaffold;无人类基线;覆盖面作者自认远不完整。
- 版本间数字变化(v1:50+ 场景/近 300 题/17%;v3:61/205/21%),引用时需注明版本。

## 与本研究方向的关系
对 **课题 2**,BixBench 是「结果级(outcome-level)」评估的代表,恰好可以作为我们 claim-to-evidence 验证的**对照组**:它证明了(1) MCQ 分数会被记忆抬高 —— 带「纯记忆基线」和「拒答选项」的做法应直接纳入我们的协议,用以区分 agent 的结论是来自它跑的 omics 分析,还是来自先验知识;(2) 每题 5 次并行运行的逐题准确率分布(附录图 7–8)是 rerun stability 的早期证据。它的空白:没有检查 notebook 中的中间结论是否被数据支持,也没有 judge 校准 —— 这两点正是课题 2 的 calibrated verifier 要补的。对 **课题 1**,它的 capsule 结构(假设 + 数据 + 参考 notebook + true/false 结论)是把 KPMP/Lake 公开数据上的分析打包成可复用任务的好模板;将来 KidneyAnomalyBench 若扩展出「agent 分析异常区域」任务,可直接沿用 capsule 格式与 Aviary 环境。对 detect → model → revert 主线,它提示:agent 在生信分析上远未可靠(最佳 21%),在 pipeline 中只能作为需验证的助手。

## 可复用资产
- **数据集:** BixBench(capsule + 题目)。
<https://huggingface.co/datasets/futurehouse/BixBench>
- **评测框架与代码:**
<https://github.com/Future-House/BixBench>
- **Agent 环境:** Aviary(SimpleAgent)+ BixBench-env Docker 镜像。
- **协议设计:** 纯记忆基线、拒答选项、5 次重跑多数投票、precision vs accuracy 的区分。

## 待读
- Aviary(arXiv 2412.21154)与 LAB-Bench(lab-bench-arxiv-2024),同一团队的前作。
- 后续报告 BixBench 分数的 agent 系统,以及分数如何随模型代际变化。
- ScienceAgentBench、DiscoveryBench、CORE-Bench(可复现性)作为同类对照。

## 引用
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


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

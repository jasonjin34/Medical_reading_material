# scBench: Evaluating AI Agents on Single-Cell RNA-seq Analysis

> **Bibkey** `Workman2026_260209063` · **Venue** arXiv preprint (2026) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2602.09063>
> `status: complete` — 全文精读基于 arXiv HTML v1(2026-02-09)。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> scBench(LatchBio)是 394 道**可确定性判分**的 scRNA-seq 分析题:每题给出"某个分析步骤之前"的真实数据快照 + 自然语言任务 + 判分器,覆盖 6 个测序平台 × 7 类任务;8 个前沿模型在同一 harness 下准确率仅 29–53%,且**平台差异与模型差异一样大**(冷门平台掉 40+ 个百分点)。
<!-- EN --> scBench (LatchBio) is 394 **deterministically graded** scRNA-seq analysis problems: each gives a real data snapshot taken just before an analysis step, a natural-language task and a grader, across 6 sequencing platforms × 7 task categories. Eight frontier models under one harness reach only 29–53%, and **platform matters as much as model** (40+ pp drops on less-documented platforms).

## 研究问题 / Problem
<!-- ZH --> 现有生物学基准多考记忆、解读或文献式推理,不要求与数据进行经验性交互,也不代表真实分析步骤;因此缺少一个标准、确定性的"数据驱动 scRNA-seq 分析"标尺。作者要回答:前沿 agent 能否在凌乱的真实数据上可靠地恢复关键生物学结果。
<!-- EN --> Existing biology benchmarks test recall, interpretation or literature-style reasoning without requiring empirical interaction with data or reflecting real analysis steps, so there is no standard, deterministic yardstick for data-grounded scRNA-seq analysis. Can frontier agents reliably recover the key biological result from messy real data?

## 方法 / Method
<!-- ZH --> **题目构造**(沿用 SpatialBench):只选满足三条的步骤——日常实践中真会做、答案依赖于给定数据(不能靠教科书或背诵基因列表)、结果是可确定性判分的结构化 JSON。五步流程:按发表流程复现该步 → 定义精确 JSON schema → 选判分器族 → 用多种合理方法/参数跑一遍来**校准容差** → **防捷径**(删除预计算 embedding、缓存标签等)。最后再用三种方式尝试"作弊"——直接读 .obs/.uns、凭先验知识作答、换别的合理方法——任一能解或容差不覆盖则修改或删除。**题型分类**:scientific(只给目标,方法参数自选,容差最宽)、procedural(指定方法,容差可更紧)、observational(解读数据属性)。**五类判分器**:NumericTolerance、MultipleChoice、MarkerGenePrecisionRecall、LabelSetJaccard、DistributionComparison(每个类别都必须在容差内,防止忽略稀有细胞类型)。设计原则 "specify what, not how";刻意避开随机种子敏感(不考精确簇数)与库版本伪差(不考 UMAP 坐标)。**Harness**:所有模型统一用 mini-SWE-agent(提取第一个代码块在 bash 中执行),每题最多 100 步、单命令 300 s、总时长 600 s,不重试;每个模型-题目跑 3 次,两阶段聚合 + t 分布 95% CI。
<!-- EN --> **Problem construction** (following SpatialBench): keep only steps that occur in routine practice, whose answer depends on the provided data (not textbook knowledge or memorised gene lists), and whose result is a deterministically gradable JSON artifact. Five stages: reproduce the step with the published workflow → define an exact JSON schema → pick a grader family → **calibrate tolerances** by running multiple valid methods/parameters → **harden against shortcuts** (remove precomputed embeddings, cached labels). A final check tries to "cheat" three ways — read .obs/.uns directly, answer from priors, use an alternative valid method — and revises or removes problems that fail. **Evaluation types**: scientific (goal only, widest tolerances), procedural (method named, tighter), observational (report a data property). **Five grader families**: NumericTolerance, MultipleChoice, MarkerGenePrecisionRecall, LabelSetJaccard, DistributionComparison (every category must pass, so rare cell types cannot be ignored). Principle: "specify what, not how"; seed-sensitive outputs (exact cluster counts) and version artifacts (UMAP coordinates) are deliberately avoided. **Harness**: all models under mini-SWE-agent (first fenced code block executed in bash), 100-step cap, 300 s per command, 600 s per evaluation, no retries; 3 replicates per model–problem, two-stage aggregation with t-distribution 95% CIs.

## 数据 / Data
<!-- ZH --> 394 题,平台:BD Rhapsody 61、Chromium 60、CSGenetics 42、Illumina 85、MissionBio 81(Tapestri 靶向 DNA+蛋白,用于检验跨模态泛化)、ParseBio 65(无 QC 题)。任务:QC 36、归一化 44、降维 69、聚类 49、细胞分型 118、差异表达 71、轨迹 7。公开 30 道 canonical 题(5 个平台)及其完整 agent 轨迹;完整题库**不公开**以防训练污染。
<!-- EN --> 394 problems; platforms: BD Rhapsody 61, Chromium 60, CSGenetics 42, Illumina 85, MissionBio 81 (Tapestri targeted DNA+protein, a cross-modality stress test), ParseBio 65 (no QC). Tasks: QC 36, normalisation 44, dimensionality reduction 69, clustering 49, cell typing 118, differential expression 71, trajectory 7. Thirty canonical problems (5 platforms) are public with full agent trajectories; the full suite is **withheld** to prevent training contamination.

## 主要结果 / Key results
<!-- ZH --> **总体**:Claude Opus 4.6 **52.8%**(95% CI 48.3–57.2)、Opus 4.5 49.9%、GPT-5.2 45.2%、Sonnet 4.5 44.2%、GPT-5.1 37.9%、Grok-4.1 35.6%、Grok-4 33.9%、Gemini 2.5 Pro **29.2%**;最好与最差相差 23.6 pp。GPT-5.2 在准确率-成本上接近 Pareto 最优。**按任务**:归一化最容易(跨模型均值 70.4%)、QC 55.3%、聚类 38.3%、细胞分型 34.9%、差异表达最难(27.0%,且区分度最大,27.7 pp);8 个模型中 7 个遵循同一难度顺序。**按平台**:跨模型均值从 CSGenetics 59.1% 到 MissionBio 26.4%,**32.7 pp 的平台差超过 23.6 pp 的模型差**;MissionBio 对所有模型都最难,还会颠倒排名;Gemini 在 CSGenetics 52.4% vs MissionBio 10.3%,最稳定的 Opus 4.5 也有 39 pp 波动。**与 SpatialBench 对比**:同 harness 下空间组学更难(最高 38.4% vs 52.8%),但模型排名两端一致。
<!-- EN --> **Overall**: Claude Opus 4.6 **52.8%** (95% CI 48.3–57.2), Opus 4.5 49.9%, GPT-5.2 45.2%, Sonnet 4.5 44.2%, GPT-5.1 37.9%, Grok-4.1 35.6%, Grok-4 33.9%, Gemini 2.5 Pro **29.2%**; a 23.6 pp best–worst spread. GPT-5.2 is near the accuracy–cost Pareto front. **By task**: normalisation easiest (cross-model mean 70.4%), QC 55.3%, clustering 38.3%, cell typing 34.9%, differential expression hardest (27.0%, and most discriminative at 27.7 pp); 7 of 8 models share the same difficulty order. **By platform**: cross-model means range from CSGenetics 59.1% to MissionBio 26.4% — **a 32.7 pp platform gap exceeding the 23.6 pp model gap**; MissionBio is hardest for every model and inverts rankings; Gemini drops from 52.4% (CSGenetics) to 10.3% (MissionBio), and even the most consistent model (Opus 4.5) swings 39 pp. **vs. SpatialBench**: under the same harness spatial is harder (top 38.4% vs. 52.8%), but rankings agree at both ends.

## 创新点 / Contributions
- <!-- ZH --> **可确定性判分 + 容差校准 + 防捷径**的一整套题目工程方法(构造五步、三种作弊检验、linter),可直接迁移到其他组学。 <!-- EN --> A full problem-engineering recipe — **deterministic grading + tolerance calibration + anti-shortcut hardening** (five-stage construction, three cheat checks, a linter) — directly transferable to other omics.
- <!-- ZH --> 平台 × 任务双轴分层,揭示"平台效应 ≥ 模型效应",指向训练数据覆盖不均与记忆化技巧的脆弱性。 <!-- EN --> Platform × task stratification revealing "platform effect ≥ model effect," pointing to uneven training-data coverage and brittle memorised techniques.
- <!-- ZH --> 统一 harness、三次重复、两阶段 CI——在 agent 评测中少见的统计规范。 <!-- EN --> One shared harness, three replicates, two-stage CIs — statistical discipline rare in agent evaluation.
- <!-- ZH --> 与 SpatialBench 组成单细胞 + 空间两大转录组模态的配套诊断。 <!-- EN --> Together with SpatialBench, a paired diagnostic for the two dominant transcriptomic modalities.

## 局限 / Limitations
- <!-- ZH --> 作者自陈:确定性判分把科学判断离散化成可自动检查的小块;每题只快照**单个**流程步骤,不覆盖误差累积、阈值反复修改的长程迭代(后续 scBench-Long 正是补这一点)。 <!-- EN --> Self-reported: deterministic grading discretises scientific judgement into checkable chunks; each problem snapshots a **single** step, missing long-horizon iteration where errors compound (scBench-Long addresses this).
- <!-- ZH --> 只评测"模型 + 一个极简 harness",不代表专门的生物学 agent(Biomni 等)的表现;无温度/种子控制,重复只反映采样随机性。 <!-- EN --> Evaluates models in one minimal harness, not specialised biology agents (Biomni etc.); no temperature/seed control, so replicates reflect sampling noise only.
- <!-- ZH --> 完整题库不公开,外部无法独立复核题目质量;轨迹类任务仅 7 题;MissionBio 并非 RNA-seq,混入总分会影响解读。 <!-- EN --> The full suite is private, so problem quality cannot be independently audited; only 7 trajectory tasks; MissionBio is not RNA-seq yet counts in the aggregate.
- <!-- ZH --> 只判最终 JSON,不判中间步骤是否合理(可能"对的答案、错的理由")。 <!-- EN --> Grades only the final JSON, not whether intermediate steps were sound ("right answer, wrong reason" is possible).

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 对 **Plan B** 这是最该"照抄方法学"的一篇:我们要为分析肾脏组学的 agent 建可信度评估,scBench 给出了**如何把一个分析步骤变成可验证题目**的完整配方——复现 → JSON schema → 判分器族 → 用多种合理方法校准容差 → 删除捷径字段 → 三种作弊检验。这些可以直接用来构造肾脏版题目(在 KPMP/Lake/内部 snRNA 数据上做 QC 阈值、PT 亚型分型、损伤态 marker 差异表达等)。它的两个发现直接关系到我们:**(1) 平台效应 ≥ 模型效应**——我们的数据横跨 snRNA、snATAC、Xenium,预计 Xenium/snATAC 这类文档较少的模态上 agent 会大幅掉分,这本身就是组学特有失败分类的一个维度;**(2) 差异表达与细胞分型最难、最有区分度**——而这恰是"异常细胞态"判定所依赖的步骤。对 **Plan A**,DistributionComparison 的"每个类别都必须通过、不能忽略稀有细胞类型"规则,与 KidneyAnomalyBench 需要防止"稀有病态被平均掉"的设计目标一致;其 scientific/procedural/observational 的题型划分也可用于给专家标注的异常基准分层。需要注意它只判最终答案,Plan B 的 claim-to-evidence 核查和重跑稳定性正是它没有覆盖的部分。
<!-- EN --> For **Plan B** this is the paper whose methodology to copy most directly: building a trustworthiness evaluation for agents that analyse kidney omics requires turning analysis steps into verifiable problems, and scBench gives the full recipe — reproduce → JSON schema → grader family → calibrate tolerances with multiple valid methods → strip shortcut fields → three cheat checks. These transfer directly to kidney problems (QC thresholds, PT subtype calling, injury-state marker DE on KPMP/Lake/in-house snRNA). Two findings matter for us: **(1) platform effect ≥ model effect** — our data span snRNA, snATAC and Xenium, and we should expect large drops on less-documented modalities like Xenium/snATAC, itself a dimension of an omics-specific failure taxonomy; **(2) DE and cell typing are hardest and most discriminative** — exactly the steps that "anomalous cell state" calls depend on. For **Plan A**, DistributionComparison's "every category must pass; rare cell types cannot be ignored" rule matches KidneyAnomalyBench's need to keep rare disease states from being averaged away, and the scientific/procedural/observational split can stratify an expert-annotated anomaly benchmark. Note it grades only final answers; Plan B's claim-to-evidence checking and rerun stability are precisely what it leaves uncovered.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码:** 评测框架、判分器、linter、agent harness;30 道公开题与完整轨迹;支持接入自定义 agent。 <!-- EN --> **Code:** evaluation framework, graders, linter, agent harness; 30 public problems with full trajectories; pluggable custom agents.
<!-- ZH/EN --> <https://github.com/latchbio/scbench>
- <!-- ZH --> **判分器规格:** 附录 C 的五类判分器形式化定义,可直接复用于肾脏任务。 <!-- EN --> **Grader specs:** formal definitions of the five grader families (Appendix C), reusable for kidney tasks.
- <!-- ZH --> **统计设计:** 两阶段聚合 + t 分布 CI 的报告方式。 <!-- EN --> **Statistical design:** two-stage aggregation with t-distribution CIs.

## 待读 / Follow-ups
- <!-- ZH --> SpatialBench(Workman et al., 2025):空间转录组版本,与 Xenium 数据最相关。 <!-- EN --> SpatialBench (Workman et al., 2025): the spatial version, most relevant to our Xenium data.
- <!-- ZH --> scBench-Long(本仓库 `scbench-long-arxiv-2026`):长程、声明级的后续。 <!-- EN --> scBench-Long (`scbench-long-arxiv-2026`): the long-horizon, claim-level follow-up.
- <!-- ZH --> mini-SWE-agent harness;以及专门 agent(Biomni、SpatialAgent)在 scBench 上的成绩(若有)。 <!-- EN --> The mini-SWE-agent harness; and scores of specialised agents (Biomni, SpatialAgent) on scBench, if reported.

## 引用 / Cite
```bibtex
@misc{Workman2026_260209063,
  title = {scBench: Evaluating AI Agents on Single-Cell RNA-seq Analysis},
  author = {Workman, Kenny and Yang, Zhen and Muralidharan, Harihara and Abdulali, Aidan and Le, Hannah},
  year = {2026},
  eprint = {2602.09063},
  archivePrefix = {arXiv},
  primaryClass = {q-bio.GN},
  url = {https://arxiv.org/abs/2602.09063}
}
```

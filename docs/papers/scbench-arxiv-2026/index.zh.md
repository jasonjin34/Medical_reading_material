# scBench: Evaluating AI Agents on Single-Cell RNA-seq Analysis

> **文献键** `Workman2026_260209063` · **来源** arXiv preprint(2026) · **类别** agents · **相关度** high · **获取** open
> **链接** <https://arxiv.org/abs/2602.09063> · `status: complete`

---

## 一句话
scBench(LatchBio)是 394 道**可确定性判分**的 scRNA-seq 分析题:每题给出"某个分析步骤之前"的真实数据快照 + 自然语言任务 + 判分器,覆盖 6 个测序平台 × 7 类任务;8 个前沿模型在同一 harness 下准确率仅 29–53%,且**平台差异与模型差异一样大**(冷门平台掉 40+ 个百分点)。

## 研究问题
现有生物学基准多考记忆、解读或文献式推理,不要求与数据进行经验性交互,也不代表真实分析步骤;因此缺少一个标准、确定性的"数据驱动 scRNA-seq 分析"标尺。作者要回答:前沿 agent 能否在凌乱的真实数据上可靠地恢复关键生物学结果。

## 方法
**题目构造**(沿用 SpatialBench):只选满足三条的步骤——日常实践中真会做、答案依赖于给定数据(不能靠教科书或背诵基因列表)、结果是可确定性判分的结构化 JSON。五步流程:按发表流程复现该步 → 定义精确 JSON schema → 选判分器族 → 用多种合理方法/参数跑一遍来**校准容差** → **防捷径**(删除预计算 embedding、缓存标签等)。最后再用三种方式尝试"作弊"——直接读 .obs/.uns、凭先验知识作答、换别的合理方法——任一能解或容差不覆盖则修改或删除。**题型分类**:scientific(只给目标,方法参数自选,容差最宽)、procedural(指定方法,容差可更紧)、observational(解读数据属性)。**五类判分器**:NumericTolerance、MultipleChoice、MarkerGenePrecisionRecall、LabelSetJaccard、DistributionComparison(每个类别都必须在容差内,防止忽略稀有细胞类型)。设计原则 "specify what, not how";刻意避开随机种子敏感(不考精确簇数)与库版本伪差(不考 UMAP 坐标)。**Harness**:所有模型统一用 mini-SWE-agent(提取第一个代码块在 bash 中执行),每题最多 100 步、单命令 300 s、总时长 600 s,不重试;每个模型-题目跑 3 次,两阶段聚合 + t 分布 95% CI。

## 数据
394 题,平台:BD Rhapsody 61、Chromium 60、CSGenetics 42、Illumina 85、MissionBio 81(Tapestri 靶向 DNA+蛋白,用于检验跨模态泛化)、ParseBio 65(无 QC 题)。任务:QC 36、归一化 44、降维 69、聚类 49、细胞分型 118、差异表达 71、轨迹 7。公开 30 道 canonical 题(5 个平台)及其完整 agent 轨迹;完整题库**不公开**以防训练污染。

## 主要结果
**总体**:Claude Opus 4.6 **52.8%**(95% CI 48.3–57.2)、Opus 4.5 49.9%、GPT-5.2 45.2%、Sonnet 4.5 44.2%、GPT-5.1 37.9%、Grok-4.1 35.6%、Grok-4 33.9%、Gemini 2.5 Pro **29.2%**;最好与最差相差 23.6 pp。GPT-5.2 在准确率-成本上接近 Pareto 最优。**按任务**:归一化最容易(跨模型均值 70.4%)、QC 55.3%、聚类 38.3%、细胞分型 34.9%、差异表达最难(27.0%,且区分度最大,27.7 pp);8 个模型中 7 个遵循同一难度顺序。**按平台**:跨模型均值从 CSGenetics 59.1% 到 MissionBio 26.4%,**32.7 pp 的平台差超过 23.6 pp 的模型差**;MissionBio 对所有模型都最难,还会颠倒排名;Gemini 在 CSGenetics 52.4% vs MissionBio 10.3%,最稳定的 Opus 4.5 也有 39 pp 波动。**与 SpatialBench 对比**:同 harness 下空间组学更难(最高 38.4% vs 52.8%),但模型排名两端一致。

## 创新点
- **可确定性判分 + 容差校准 + 防捷径**的一整套题目工程方法(构造五步、三种作弊检验、linter),可直接迁移到其他组学。
- 平台 × 任务双轴分层,揭示"平台效应 ≥ 模型效应",指向训练数据覆盖不均与记忆化技巧的脆弱性。
- 统一 harness、三次重复、两阶段 CI——在 agent 评测中少见的统计规范。
- 与 SpatialBench 组成单细胞 + 空间两大转录组模态的配套诊断。

## 局限
- 作者自陈:确定性判分把科学判断离散化成可自动检查的小块;每题只快照**单个**流程步骤,不覆盖误差累积、阈值反复修改的长程迭代(后续 scBench-Long 正是补这一点)。
- 只评测"模型 + 一个极简 harness",不代表专门的生物学 agent(Biomni 等)的表现;无温度/种子控制,重复只反映采样随机性。
- 完整题库不公开,外部无法独立复核题目质量;轨迹类任务仅 7 题;MissionBio 并非 RNA-seq,混入总分会影响解读。
- 只判最终 JSON,不判中间步骤是否合理(可能"对的答案、错的理由")。

## 与本研究方向的关系
对 **Agent 可信度课题** 这是最该"照抄方法学"的一篇:我们要为分析肾脏组学的 agent 建可信度评估,scBench 给出了**如何把一个分析步骤变成可验证题目**的完整配方——复现 → JSON schema → 判分器族 → 用多种合理方法校准容差 → 删除捷径字段 → 三种作弊检验。这些可以直接用来构造肾脏版题目(在 KPMP/Lake 等 snRNA 数据上做 QC 阈值、PT 亚型分型、损伤态 marker 差异表达等)。它的两个发现直接关系到我们:**(1) 平台效应 ≥ 模型效应**——肾脏多模态数据常横跨 snRNA、snATAC、Xenium,预计 Xenium/snATAC 这类文档较少的模态上 agent 会大幅掉分,这本身就是组学特有失败分类的一个维度;**(2) 差异表达与细胞分型最难、最有区分度**——而这恰是"异常细胞态"判定所依赖的步骤。对 **伪影注入课题**,DistributionComparison 的"每个类别都必须通过、不能忽略稀有细胞类型"规则,与 KidneyAnomalyBench 需要防止"稀有病态被平均掉"的设计目标一致;其 scientific/procedural/observational 的题型划分也可用于给专家标注的异常基准分层。需要注意它只判最终答案,Agent 可信度课题的 claim-to-evidence 核查和重跑稳定性正是它没有覆盖的部分。

## 可复用资产
- **代码:** 评测框架、判分器、linter、agent harness;30 道公开题与完整轨迹;支持接入自定义 agent。
<https://github.com/latchbio/scbench>
- **判分器规格:** 附录 C 的五类判分器形式化定义,可直接复用于肾脏任务。
- **统计设计:** 两阶段聚合 + t 分布 CI 的报告方式。

## 待读
- SpatialBench(Workman et al., 2025):空间转录组版本,与 Xenium 数据最相关。
- scBench-Long(本仓库 `scbench-long-arxiv-2026`):长程、声明级的后续。
- mini-SWE-agent harness;以及专门 agent(Biomni、SpatialAgent)在 scBench 上的成绩(若有)。

## 引用
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


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

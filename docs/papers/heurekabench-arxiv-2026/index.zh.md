# HeurekaBench: A Benchmarking Framework for AI Co-scientist

> **文献键** `Panigrahi2026_260101678` · **来源** International Conference on Learning Representations (ICLR 2026)(2026) · **类别** agents · **相关度** medium · **获取** open
> **链接** <https://arxiv.org/abs/2601.01678> · `status: complete`

---

## 一句话
HeurekaBench(EPFL Brbić 组)是一个**构造"AI co-scientist"基准的框架**:用多 LLM 流水线从已发表论文及其代码仓库中抽取洞见、匹配并生成代码流程,再由人**实际运行代码、确认能复现论文结果**后才保留,最后转成开放题(OEQ)与选择题(MCQ);在单细胞领域实例化为 sc-HeurekaBench(41 条验证洞见、50 OEQ + 50 MCQ),用原子事实分解的 LLM 评审打分,并用它比较 Biomni、CellVoyager、BixBench-Agent 及 planner / critic / retriever 设计。

## 研究问题
现有数据驱动科学基准大多考"按指令回答一个计算问题"(如 BH 校正后多少 miRNA 显著),而 co-scientist 应当自己规划这些子步骤,并从数据给出开放式结论;最接近的 BaisBench 只靠单个 LLM 出题、没有人工把关,题目可能本身无法回答。缺少一个能**可靠地**评估开放式、数据支撑的科学回答的框架。

## 方法
任务形式化为三元组 (D, Q, A):真实实验数据集、需多步推理的开放研究问题、科学上验证过的答案。**洞见生成**:InsightExtractor(GPT-4o)从论文抽取候选洞见,每条含摘要、使用的实验技术、原文逐字的 grounding text;CodeDescriber 把仓库脚本转成自然语言描述;CodeMatcher 把洞见与相关脚本配对;CodeGenerator(其余模块用 Claude-4-Sonnet)组合成多步流程。**人工验证**:审阅者运行代码(允许小改动,如列名),只有输出的图/统计量与论文 grounding text 相符的洞见才算"验证通过"。**出题**:每条洞见 few-shot 生成 OEQ 与 MCQ 各两道;MCQ 重点设计"看似合理的误读"干扰项;过滤分两步——自动剔除 LLM 靠预训练知识就能答的题,人工剔除幻觉、重复与基于未验证部分的题。**评估**:OEQ 用 G-Eval(GPT-4o)1–5 分,要求评审先把回答与标准答案都**拆成原子事实**(条件、趋势、结论),再看完整/部分/缺失,有矛盾不能拿满分,额外的不冲突发现不扣分;MCQ 报准确率与精确率/召回。另建 sc-HeurekaBench-TU(12 道需要 SCENIC、CellPhoneDB、CellChat 等专用工具的 OEQ)。

## 数据
22 篇 2024–2025 年 Nature/Cell 单细胞论文(有开源代码与开放数据,CellxGene 或论文资源),每篇生成 10 条候选洞见,最终 13 篇(9 Nature + 4 Cell)中的 **41 条**被验证 → 50 OEQ + 50 MCQ。sc-HeurekaBench-Lite:数据集 <750 MB 的子集(22 OEQ + 18 MCQ),以便三个 agent 都能运行。洞见抽取的验证集:FlyBase 50 对"论文-专家结论"、BixBench 21 对;代码匹配验证用 InsightBench(50 条洞见、215 个代码文件)。

## 主要结果
**流水线**:InsightExtractor 在 FlyBase 上 44/50 强相关、2 弱、4 无关;BixBench 上 14/21 强、4 弱、3 无关;CodeMatcher 215 个脚本中正确匹配 158 个,平均每条洞见 74.6% 文件检索正确。**Agent 对比(Lite,均用 Claude-4-Sonnet)**:OEQ 正确性 BixBench-Agent **2.34**、Biomni **2.31**、CellVoyager **2.03**(满分 5);MCQ 准确率 Biomni 50.0%、BixBench-Agent 44.4%、CellVoyager 27.8%。CellVoyager 落后被归因于固定步数、修代码能力有限、难以整合多条反馈;BixBench-Agent 在大数据集上崩溃。**Planner 消融(Biomni,全集)**:Claude-4-Sonnet **2.58±0.05** 最高,GPT-OSS-120B 2.08、Qwen3-235B-thinking 1.85、GPT-4o 1.68、MedGemma-27B 1.53;Qwen 随规模与 thinking 提升。**评审一致性**:GPT-4o 与 Claude-4.5-Sonnet 评审 Spearman 0.84、κ 0.81,与 Gemini-2.5-Pro 0.79、κ 0.71;与 11 位人类专家对 25 个回答:差值 ≤1 的占 92%(众数)/ 96%(中位),Spearman 0.93 / 0.90,κ 0.85。**Critic 消融**:GPT-OSS-120B 加 End-critic 平均 2.04→**2.49**(接近 Claude 的 2.58),低分题提升最大;但 Qwen3-235B-thinking 加 End-critic 反而 1.86→1.81(高分题被拉低);Plan-critic 对两者都有害(-0.13 / -0.19)。**Retriever 消融(TU)**:去掉 Biomni 的工具检索器,GPT-OSS-120B 2.15→1.56。

## 创新点
- **"能跑出论文结果才算真值"**:用论文自带代码复现来过滤洞见,直接解决 LLM 自动出题不可靠的问题。
- 原子事实分解的开放题评审,并做了 LLM 间与人类专家的一致性校验。
- 第一份对现有单细胞 agent(Biomni、CellVoyager、BixBench-Agent)的同底座横向比较,以及 planner / critic / retriever 的受控消融。
- 发现 critic 的**位置**很关键:末端 critic 可救差回答、开头 critic 会打乱推理——且效果因底座而异。

## 局限
- 作者自陈:只评最终回答,不验证中间步骤、不给部分分;扩展到其他领域需要领域专家做人工验证。
- 规模小(41 条洞见、50 OEQ;Lite 仅 22 OEQ);只有约 41/220 条候选洞见能被验证,依赖专用工具的洞见因 CodeGenerator 幻觉而被排除,可能使基准偏向"容易复现"的分析。
- 主评审是 GPT-4o 单模型;开放题绝对分普遍很低(最好 ~2.6/5),agent 间差异在小样本下不一定显著。
- 选 2024–2025 论文只能"部分缓解"记忆污染;没有空间组学与多模态题;没有重跑稳定性或置信度维度。

## 与本研究方向的关系
对 **Plan B**,HeurekaBench 提供了两件可直接借用的东西:**(1) "复现才入库"的真值构造**——与 scBench-Long 的"声明须独立复现"同一思路,但它把流程自动化到"抽洞见 → 匹配仓库代码 → 生成流程 → 人工运行确认",适合批量从肾脏单细胞论文(KPMP、Lake atlas、DKD 空间图谱)构造经过验证的 (D, Q, A);**(2) 原子事实分解的评审**——这本质上就是声明级核查的雏形:把 agent 回答拆成原子声明逐条比对。Plan B 要往前走的一步是:不仅比对"与论文结论是否一致",还要比对"是否被 agent 自己产生的输出支持",并给出校准置信度。它的 critic 消融也值得注意:**critic 的效果依底座而异、甚至会把好答案改坏**——这说明"加一个 LLM 审稿人"本身不可信,正是 Plan B 需要校准 verifier 的理由;评审与人类的高一致(κ 0.85)则可作为我们设计人工标注协议时的对照基线。对 **Plan A** 关系较弱,但其"论文 + 代码 + 数据"三元组的构造方法可用于 KidneyAnomalyBench 中"已知病理结论"那部分的半自动化。

## 可复用资产
- **代码 + 基准:** 框架、agent 推理与评测代码、sc-HeurekaBench 与 TU。
<https://github.com/mlbio-epfl/heurekabench>
- **项目页:**
<https://brbiclab.epfl.ch/projects/heurekabench>
- **Prompt:** InsightExtractor / CodeDescriber / CodeMatcher / CodeGenerator 与出题、评审 rubric(附录 A、B)。

## 待读
- BaisBench 与 BixBench(本仓库 `bixbench-arxiv-2025`)的出题方式对比(附录 C.5)。
- 附录 C.4 中"未能验证的洞见"类型——哪些分析最难被复现。
- G-Eval 原文与原子事实评估(FActScore 一类)方法。

## 引用
```bibtex
@inproceedings{Panigrahi2026_260101678,
  title = {HeurekaBench: A Benchmarking Framework for AI Co-scientist},
  author = {Panigrahi, Siba Smarak and Videnovi{\'c}, Jovana and Brbi{\'c}, Maria},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year = {2026},
  eprint = {2601.01678},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2601.01678}
}
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

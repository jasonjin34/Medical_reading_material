# BiomniBench: Process-level Evaluation of LLM Agents for Real-world Biomedical Research

> **文献键** `Qu_2026` · **来源** bioRxiv(2026) · **类别** agents · **相关度** high · **获取** open
> **链接** <https://doi.org/10.64898/2026.05.12.724604> · `status: complete`

---

## 一句话
BiomniBench 是一个**过程级(process-level)**的生物医学 agent 基准:不只看最终答案,而是用专家(常为原论文作者)编写的、任务特定的 A/B/C 分级 rubric,由 LLM judge 对 agent 的完整分析轨迹(`trace.md` + `answer.txt`)打分;首发 BiomniBench-DA 含 100 个基于 Nature/Cell/Science 级论文公开数据的数据分析任务。最佳配置(Claude Code + Opus 4.7)仅 73.34/100,且 **agent harness 对分数的影响大于模型换代**。

## 研究问题
现有生物医学 agent 基准(HLE、BixBench、BioML-bench、scBench、SpatialBench 等)几乎都只给最终答案打分。作者指出这有两种失败:(1) 正确答案可能来自记忆/数据污染、reward hacking,或是「错误推理碰巧得到对的数」—— agent 可以交出漂亮的火山图和自信的解读,而轨迹里却是错误的标准化、被忽略的 batch effect 和编造的引用;(2) 真实研究是开放式的,多条分析路径都可辩护,只比对参考答案会惩罚合理但不同的做法。在生物学里,这类缺陷会悄无声息地传到湿实验与药物开发决策里。

## 方法
**五阶段策展流程**:(1) 分析开源 Biomni 平台 32,014 条真实用户查询(LLM 分类,多标签):数据分析占 63.3%,高于文献研究 55.0%、实验设计 26.2% 等 → 首发选数据分析;(2) 按任务类型覆盖、疾病多样性、数据公开(GEO/ArrayExpress/补充材料)、高影响期刊四条标准选 21 篇论文;(3) 每篇招募**原作者或 5 年以上经验的领域专家**出题并准备数据,题目不必复现原文,可包括数据能支持但原文未回答的问题;(4) 专家写参考分析轨迹(Jupyter/R Markdown),经多轮独立审查且在公开数据上可运行;(5) 每题 5–10 条 rubric 条目,每条锚定一个关键分析决策点,标注到六个维度之一或多个:**data handling、method selection、statistical rigor、biological interpretation、scientific reasoning、source reliability**;每条三档 A(全对)/B(意图对、有小错,通常半分)/C(跳过或全错,0 分),每档列出多种可接受的替代做法。**评测协议**:任务放进 Harbor 沙箱(Docker,Python 3 + R,2 CPU,联网,1 小时预算),agent 必须写 `trace.md`(含决策理由、真实代码、中间计数、引用)和 `answer.txt`;明确禁止检索源论文。**LLM judge** 对每条只输出 A/B/C(+一句理由),分数由程序按点数表计算。Judge 选型:5 个候选模型对照内部专家在 35 题 597 条 rubric 上的评级,Gemini 3.1 Pro 最佳(exact acc 0.82,linear κ 0.70,quadratic κ 0.73)。每个配置**完整重跑 3 次**,报告均值 ± 跨重跑 SD 与 per-task SD。

## 数据
BiomniBench-DA:100 任务、17 种任务类型、5 个疾病领域 + 一般生物学,来自 21 篇论文(Cancer Cell、Cell、Nature、Nature Medicine、Science、PNAS 等)。疾病分布:肿瘤 47%(结直肠癌、NSCLC、黑色素瘤、泛癌蛋白基因组)、代谢与内分泌 17%、免疫 14%、一般生物学 10%、神经 8%(ALS)、心血管 4%。最常见六类(占 55%):association testing 11%、mutation analysis 10%、multi-omic integration 10%、pathway enrichment 8%、differential expression 8%、clustering 8%;长尾包括生存分析、cell composition、GWAS–eQTL colocalization、TCR repertoire、cell–cell communication 等。**没有肾脏任务。** 数据集公开在 HuggingFace。

## 主要结果
**固定 harness(Terminus-2,9 个模型,3 次重跑)**:Claude Opus 4.7 63.94 ± 0.30、GPT-5.5 63.57 ± 1.79、Opus 4.6 63.16 ± 1.56、Sonnet 4.6 62.35 ± 0.65 —— 前四名相差 1.6 分以内;开源权重 GLM-5.1 60.39、Qwen 3.6 59.47、Kimi K2.6 59.15,仅落后 3–5 分且更便宜(GLM-5.1 $0.58/题 vs Opus 4.7 $0.87);GPT-5.4 55.19;Gemini 3.1 Pro 是离群值 44.27(轨迹最短:中位 4.9 分钟、12 轮)。**per-task SD 7.3–11.5 分**,说明同一题重跑波动很大。**跨 harness**:Claude Code + Opus 4.7 73.34 ± 0.41(最佳)、Claude Code + Opus 4.6 69.51、Codex CLI + GPT-5.4 68.69、Codex CLI + GPT-5.5 67.59、Claude Code + Sonnet 4.6 66.39、Gemini CLI + Gemini 3.1 Pro 49.83。同一模型换 harness:GPT-5.4 在 Codex CLI 比 Terminus-2 高 **13.5 分**,Opus 4.7 在 Claude Code 比 Terminus-2 高 9.4 分,都大于 Opus 4.7 vs 4.6 的代际差(3.8 分)。代价是轮数和成本上升(GPT-5.4 从 13 轮到 82 轮;GPT-5.5 成本 $1.98→$4.58)。**按任务类型**:GWAS–eQTL(最佳 65)与 pathway enrichment(最佳 67)普遍难;cell composition(最高 91)与 mutation analysis(最高 86)接近饱和;cross-cohort comparison 上 harness 差异最大。**按维度**:source reliability 拿到 88–98% 的分,data handling 58–78%,**method selection 最低(44–67%)**,statistical rigor / biological interpretation / scientific reasoning 在 45–74%。三类典型失败:方法选错(用 Kruskal–Wallis 宣称单调趋势,而 Jonckheere–Terpstra 趋势检验 p ≈ 0.40)、生物学解读失焦(没锚定题目点名的疾病表型)、科学推理被简化(把多步正态性检验+加权流程换成一个相关系数)。Judge 失败模式:Opus 4.6 与 Qwen 3.6 偏宽松(39%/43% 的人类 B 判成 A),GPT-5.4 偏严,DeepSeek V3.2 几乎抹掉 B 类。

## 创新点
- 第一个面向生物医学 agent 的**过程级**基准:对完整轨迹按六个维度打分,区分「方法错但答案对」与「方法严谨但略偏」。
- 原作者/资深专家共建任务与 rubric,每档 rubric 显式列出替代做法,避免惩罚合理分歧。
- 用真实用户查询分布(32k 条 Biomni 日志)决定基准覆盖什么,而不是凭空出题。
- 把 judge 本身当作被验证的仪器:5 个候选 judge 对照人类金标准,报告 κ 和各自偏差模式。
- 严格的重跑协议(3 次完整重跑,报告跨重跑与 per-task SD),并量化出 harness 效应大于模型代际效应。

## 局限
- rubric 构建是高成本专家劳动,不可能穷尽所有可辩护路径;rubric 外的正确做法仍可能被扣分。
- LLM judge 与人类整体一致(κ = 0.70),但在最主观的维度上不能替代专家;作者建议高风险评估补充人工审查。
- judge 是对照**构建 rubric 的同一批内部专家**验证的,且只用了 35 题;judge 选型与评分可能共享偏差。
- 只有数据分析任务、一次性(one-shot)执行;肿瘤占近一半,无肾脏、无空间组学专门任务,也无影像。
- 「禁止检索源论文」只靠指令与抽查约束,作者仅称「未见明显证据」使用论文捷径;污染风险未被定量排除。
- source reliability 得分高(88–98%)只说明引用「可识别」,并未逐条核验引文是否真的支持论断。

## 与本研究方向的关系
对 **Plan B(可信生物医学 agent)** 这是最直接的参照系之一。三点可直接接上:**(1) 过程级 rubric 的六维度**(尤其 method selection、statistical rigor)几乎就是 omics 专用 failure taxonomy 的起点 —— 我们可以在它之上补充肾脏 omics 特有的失败类型:ambient RNA / doublet 未处理、snRNA 与 snATAC 跨模态不一致却被忽视、按细胞而非按样本(伪重复)做检验、Xenium 分割伪影被当作生物信号。它的 da-1-1 rubric 第 3 条「按患者聚合比例而非按细胞」正是伪重复问题的样板。**(2) 它报告的 per-task SD 7.3–11.5 分**,是我们「rerun stability」轴的现成证据:同一配置同一题的重跑分数可以差约 10 分,这直接支持把重跑稳定性作为可信度指标。**(3) 它的空白正是 Plan B 的切入口**:source reliability 只检查引用是否「可识别」,不检查**每条 claim 是否被所引证据或所跑数据支持** —— 而 claim-to-evidence 验证 + 校准 verifier 恰好补这一层;它的 judge 也只与构建 rubric 的同一批专家比对,没有校准或覆盖保证。对 **Plan A**,BiomniBench-DA 无肾脏任务,说明一个基于 KPMP/Lake/HuBMAP 公开数据、由肾病理/肾脏专家共建 rubric 的「肾脏版过程级基准」是空白;KidneyAnomalyBench 的专家验证流程可以借用它的五阶段策展(用户需求 → 选文 → 专家出题 → 参考轨迹 → A/B/C rubric)。对实验室 detect → model → revert 主线,它提醒:agent 若要参与「提名逆转靶点」,评估必须看过程(方法选择与生物学解读),而不只看最后的基因列表。

## 可复用资产
- **数据集:** BiomniBench-DA(100 任务、数据、rubric)。
<https://huggingface.co/datasets/phylobio/BiomniBench-DA>
- **执行框架:** Harbor(容器化 agent 评测,支持 Codex CLI / Terminus-2 / Claude Code / Gemini CLI)。
<https://github.com/harbor-framework/harbor>
- **评测协议模板:** `trace.md` 必填结构(目标、数据源、每步决策+理由+代码+中间计数、结果、参考文献)、A/B/C rubric 格式、judge prompt(附录 A.4)、judge 验证表(附录 B)。
- **重跑统计口径:** 3 次完整重跑,区分跨重跑 SD 与 per-task SD —— 可直接用作 rerun-stability 的报告格式。

## 待读
- Biomni 原文(biomni-biorxiv-2025)与 BenchGuard(Tu et al. 2026,arXiv 2604.24955,自动审计 agent 基准的 ground truth 噪声)。
- 同期的 GeneBench、CompBioBench、BioMysteryBench、BioAgent Bench、LAB-Bench2(arXiv 2604.09554)。
- 跟进后续发布的实验设计 / 文献综合任务线,以及是否加入多轮人机协作设定。

## 引用
```bibtex
@article{Qu_2026, title={BiomniBench: Process-level Evaluation of LLM Agents for Real-world Biomedical Research}, url={http://dx.doi.org/10.64898/2026.05.12.724604}, DOI={10.64898/2026.05.12.724604}, publisher={openRxiv}, author={Qu, Yuanhao and Lu, Yingzhou and Tu, Xinming and Zhang, Serena and She, Tianwei and Shaw, Alexander Glenn and Shih, Jou-Ho and Zhao, Bingqing and Shen, Minjie and Yang, Haochen and Yan, Jielin and Zhang, Rongchuan and Wu, Xinze and Li, Tingting and Zhou, Bin and Wang, Ning and Ma, Adam and Cong, Le and Hu, Xiaobo and Jiang, Yuan and Dong, Jiayun and Peng, Tao and Leskovec, Jure and Huang, Kexin}, year={2026}, month=May }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

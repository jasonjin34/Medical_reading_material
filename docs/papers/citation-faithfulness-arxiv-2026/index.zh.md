# Evaluating and Guarding Citation Faithfulness in Agentic Scientific Synthesis

> **文献键** `Goo2026_260720527` · **来源** arXiv preprint(2026) · **类别** agents · **相关度** high · **获取** open
> **链接** <https://arxiv.org/abs/2607.20527> · `status: complete`

---

## 一句话
OpenScholar、PaperQA2 这类文献综合 agent 及其基准都会「检查引用是否成立」,但没人审计这个**检查器本身**是否可靠。本文证明:同一批 agent 输出,仅因 verifier 严格度不同,未支持引用率就在 **约 3% 到约 18%** 之间变动;verifier 们在「哪些被支持」上一致,在「该标记哪些」上却几乎不一致(negative-specific agreement 0.27–0.30)。作者给出**以人工金标准为锚的评估协议** + 一个 **split-conformal 守卫**,对「漏过标记规则的真正未支持引用」给出无分布、有限样本的捕获率保证,并指出保证能否迁移取决于**校准负样本的难度**。

## 研究问题
三个缺口:(G1) 报告的未支持引用率依赖 verifier,单个数字无法跨研究比较;(G2) verifier 在该标记什么上分歧大,没有一组可信的部署标记集;(G3) 没有方法对「某个标记规则漏掉多少真正未支持的引用」给出无分布保证。作者强调贡献不在于「模型评审不完美」这一已知观察,而在于它对基准测试的后果,以及补救方案。

## 方法
**形式化**:把答案拆成 claim–citation 对 (c, pᵢ);verifier 给出二值判定 v(c,p) 及连续分数 s(c,p) ∈ [0,1]（支持概率）;金标签 y(c,p) 只在基准上有。**三处锚定到人工金标准**:(1) 用金标准验证 verifier,而非凭名气选;(2) 用带金标准支持段落的数据测 re-attribution;(3) 在金标准上校准保证。**Verifier 作为可替换仪器**:在**匹配的捕获率**下比较(而非各自默认阈值),若区分度相当就按成本选 —— 选用本地 3B 的 AttrScore。**守卫流程**(每个带引用的句子):verify(AttrScore-3B 检查 claim 与所引段落)→ 若不支持,re-attribute(在其余已提供段落中排序,提出替换指针,**再由 verifier 复核**后才移动指针,句子本身不改)→ 无法修复的**标记为 [N UNVERIFIED] 而非删除**。**Split-conformal 阈值**:在金标准校准集的**未支持类**分数上取 τ = s₍ₖ₎,k = ⌈(n_cal+1)(1−α)⌉;凡 s ≤ τ 即标记,则在可交换性假设下对新的未支持引用有 Pr[s_new ≤ τ] ≥ 1−α(命题 4.1,附证明;离散分数平局按保守方向处理)。保证的是**捕获率(安全轴)**,不是结论正确性。**Re-attribution 排序器**可替换:默认确定性 BM25,对比 verifier 分数与各生成模型的自我归因。

## 数据
**被审计系统**:四个 27–35B 开源指令模型(Gemma-4 两个、Qwen3.6 两个;稠密与 MoE 各二),单 GPU 本地运行;三种管线:bare(无检索下限)、OpenScholar、PaperQA2;**固定检索上下文**并复现各系统已发表的 prompt,只测生成阶段的引用行为;部署输出来自 ScholarQABench 多论文任务。**Verifier(5 个)**:AttrScore-3B(高召回)、OpenScholar post-hoc judge、GPT-4o、RAGAS、DeBERTa-NLI(高特异)。**金标准**:SciFact(208 对测试 + 802 对不相交划分,仅用于 prompt 选择/留出验证);QASA 全测试集 1,375 支持 + 1,375 未支持对(re-attribution 与 conformal 校准);PubMedQA 843(范围对照)。所有头条数字带 bootstrap 或 Wilson 95% CI。

## 主要结果
**Verifier 前沿(SciFact)**:支持类召回 / 特异性 —— AttrScore-3B 0.90 / 0.54、OpenScholar post-hoc 0.50 / 0.92、GPT-4o 0.46 / 0.92、RAGAS 0.30 / 0.96、DeBERTa-NLI 0.25 / 0.97;AttrScore 在留出 802 对上召回 0.94。ROC-AUC 相互重叠:AttrScore 0.88 [0.84, 0.93]、DeBERTa 0.90 [0.85, 0.94]、GPT-4o 0.87 [0.82, 0.92] —— **严格的前沿 judge(GPT-4o)并不带来区分优势**。金标准上分数均值:支持 0.54 vs 未支持 0.20。**未支持率依赖 verifier**:同一输出从高召回 verifier 下 bare 约 3% 单调升到严格 NLI 下约 14–18%;agentic 管线在每个设置下比 bare 高几个点;升高大部分来自严格 verifier **错误拒绝真正被支持的引用**。**分歧**:300 个部署句子上,三 verifier 两两 positive-specific agreement 0.90–0.96,negative-specific 仅 0.27–0.30 —— 一个 verifier 标记的引用中 **60–80%** 被另一个判为支持。**Conformal 保证(QASA)**:目标 0.90/0.94/0.98 → 留出实测 0.90/0.94/0.98;校准量 25 时朴素经验分位数欠覆盖(0.85 @ 0.90 目标)而 conformal 达 0.92,约 200 时两者趋同。**迁移条件**:QASA 校准负样本是容易的论文内干扰段(均值 0.20),而真正的错引(SciFact 人工未支持)均值 0.50 —— 用 QASA 校准、目标 90% 的 τ 只能抓住 **37%** 的难负样本(94%、98% 目标时为 44%、61%);在目标域负样本上重新校准可恢复保证,代价是更高的复核量。**复核预算(90% 保证)**:合并后标记率 bare 2.5%、OpenScholar 3.3%、PaperQA2 6.1%(单格如 PaperQA2 + Qwen3.6-35B 9.5% [6.5, 13.8]),随管线 agency 上升。**Re-attribution(QASA,recall@1)**:Gemma-4-26B 0.76、Gemma-4-31B 0.74、**BM25 0.69(CPU)**、verifier 分数 0.58、Qwen3.6 0.51–0.52、随机 0.03;高词汇重叠半数样本上 BM25 与 Gemma 持平(0.88),最低重叠四分位 BM25 0.31 vs Gemma 0.53。BM25 无法区分支持与反驳(SciFact 上答案与反驳段落的 Jaccard 0.064 vs 0.055),故必须由 verifier 复核(0.83 vs 0.50)。**范围对照**:在 PubMedQA(结论 yes/no)上 κ = 0.02 —— 守卫检验「段落是否支持 claim」,**不检验结论是否正确**。

## 创新点
- 定量证明引用忠实度指标**依赖 verifier 的工作点**,且 verifier 在「标记什么」上几乎不一致 —— 没有命名 verifier 与协议的跨论文比较无效。
- 以人工金标准为锚的评估协议(验证 verifier、测 re-attribution、校准保证都对照金标准而非另一个模型)。
- 用 split-conformal 把一个只有中等一致性的 verifier 变成**有限样本、无分布的捕获率保证**,并给出「声明容忍度 → 预先确定复核预算」的操作方式。
- 明确识别并量化保证迁移的关键条件 —— **校准负样本难度**,给出重新校准方案(作者称此前 conformal-factuality 工作未检验)。
- MIT 许可的单 GPU(80GB)/CPU 开源审计工具包。

## 局限
- 演示的保证在 QASA 上是**分布内**的;对真实错引偏乐观(37% vs 声明 90%),部署必须在目标域负样本上重新校准。
- 保证是**边际**的(对校准抽样平均),单次划分可能低于目标。
- 固定检索,只测生成阶段,不覆盖各 agent 自身检索引入的错误。
- 只检验「单个段落是否支持 claim」,不处理矛盾证据、选择性引用或结论正确性(作者列为下一步)。
- 未考虑 agent 被优化去对抗 verifier 的情形;被审计的只是 27–35B 开源模型。
- 作者提醒:截断段落(只看前缀)会把未支持率虚高数倍,须用滑窗读全文。

## 与本研究方向的关系
这几乎就是 **Plan B「calibrated verifier」** 的原型,而且在方法上与我们的计划高度吻合:**(1) 「verifier 是要被验证的仪器」**这一立场,正是我们在肾脏 omics 场景应采取的 —— 不能只报告「agent 的 claim 中 X% 未被证据支持」,必须同时报告用哪个 verifier、在什么金标准上验证、工作点在哪。**(2) Split-conformal 捕获率保证**可以直接移植:把 claim–citation 对换成 claim–evidence 对(evidence 可以是文献段落,也可以是 agent 实际跑出的统计表/图),在专家标注的金标准上校准 τ,给出「漏检的未支持 claim ≤ α」的保证,并预先声明复核预算。**(3) 校准负样本难度**这一发现对我们特别关键:肾脏 omics 中真正难的错误(如把 ambient RNA 污染导致的信号说成疾病特征、把 Xenium 分割伪影说成细胞状态)与「容易的干扰项」完全不同 —— 金标准负样本必须来自真实 agent 错误(这与 Plan A 中「专家验证的 KidneyAnomalyBench」可以共用标注流程)。**(4) 范围对照的结论**(守卫不检验结论正确性,PubMedQA κ = 0.02)提醒我们:claim-to-evidence 验证与「结论是否为真」是两层问题,Plan B 的 omics verifier 需要第二层 —— 证据本身(数据)是否可靠,即 Plan A 的跨模态一致性正好能提供。与 citation-blame-emnlp-2026 互补:那篇负责**定位**错误发生在哪个 agent,这篇负责对 verifier 的判断**给出统计保证**。

## 可复用资产
- **代码(MIT,单 GPU/CPU 审计工具包):**
<https://github.com/GooTec/citation-guard>
- **方法:** 匹配捕获率下比较 verifier;split-conformal 阈值 τ = s₍⌈(n+1)(1−α)⌉₎(在未支持类上);verify → re-attribute → flag 流程;[N UNVERIFIED] 标记而非删除。
- **报告规范:** 分类别 recall/specificity、negative-specific agreement(而非只报 κ,避开 kappa paradox)、全部带 CI。
- **金标准数据:** SciFact、QASA、PubMedQA;部署输出来自 ScholarQABench。

## 待读
- OpenScholar(Asai et al., Nature 2026)与 PaperQA2(paperqa2-arxiv-2024)的引用评估方式。
- Conformal factuality(Mohri & Hashimoto)、conformal abstention(Abbasi-Yadkori et al. 2024)、AttributionBench、AttrScore。
- 医学引用审计 SourceCheckup(sourcecheckup-natcommun-2025)作为医学领域对照。
- 作者提出的下一步:从「段落是否支持」升级到「全部引用证据是否充分支持结论」,并处理矛盾与选择性引用。

## 引用
```bibtex
@misc{Goo2026_260720527,
  title = {Evaluating and Guarding Citation Faithfulness in Agentic Scientific Synthesis},
  author = {Taewan Goo and Junsik Kim and Kyulhee Han and GwonYul Jo and Jong-Soo Kim and Tae-Hyung Kim},
  year = {2026},
  eprint = {2607.20527},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2607.20527}
}
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

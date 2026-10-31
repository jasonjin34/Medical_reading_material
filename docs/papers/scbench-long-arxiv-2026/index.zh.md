# scBench-Long: Verifiable Benchmarking of Long-Horizon Single-Cell Biology

> **文献键** `Diks2026_260626563` · **来源** arXiv preprint(2026) · **类别** agents · **相关度** high · **获取** open
> **链接** <https://arxiv.org/abs/2606.26563> · `status: complete`

---

## 一句话
scBench-Long(LatchBio)把 scBench 从"单步"推进到"长程":21 个评测、5 个研究系统,要求 agent 从原始或接近原始的单细胞数据出发、不给方法地**恢复一个具体的科学结论**,结论用受控词表确定性判分,另配轨迹 rubric 做诊断;1,068 条轨迹中最强的模型-harness 组合(Claude Opus 4.8 + Claude Code)也只通过 16/63(25.4%),且失败主要不是工具使用失败,而是**科学推理失败**。

## 研究问题
单细胞研究的结论需要经过多步流程、整合元数据、实验设计、辅助证据(TCR、染色质、验证实验)才能得出;已有基准要么考广义知识,要么考可执行流程或局部步骤。长程任务的难点是**可验证的 ground truth 难定义**:同一数据可支持多种合理结论,已发表结果也未必能独立复现。问题是:如何既约束可接受答案的集合,又不惩罚合理但未预料到的分析路径?

## 方法
**以研究系统而非独立数据集组织**:每个系统贡献多道题,从不同角度(细胞身份、状态、调控、组成、机制)反复审问同一实验。**论文声明只作为候选题来源,不自动当作真值**:只有当目标结论能从提供给 agent 的数据中被独立复现、并经审阅、干扰项设计和多模型轨迹检查后才保留。每题打包:精简的科学问题、原始/近原始数据节点、所需辅助资源、受控答案面、复现笔记、轨迹 rubric。**答案面**围绕分析者真正推理的对象:细胞态身份、供体组成、调控因子与方向、克隆型/库声明、配体-受体解释,以及**"机制需谨慎"标签**;干扰项专门用来区分数据支持的结论与常见捷径(经典 marker 先验、按丰度排名、单模态答案、无依据的因果解释)。**判分**:结构化 JSON 上的类型化检查(列表/字典匹配、字段谓词、同义词、对生物学不相容答案的 hard-fail),只判终点、不规定路径。**诊断**:作者在复现后定义"chokepoint",由 4 个 LLM 评审按 rubric 给轨迹打分,但**只作诊断,不作为基准分**。**运行**:17 个模型-harness 组合(PI、Claude Code、OpenAI Codex;Claude、Gemini、GPT、Grok、Kimi、GLM),每题 3 次重复,报告 Wilson CI 与 any/majority/all 三档稳健性。

## 数据
5 个研究系统、21 题:黑色素瘤肿瘤反应性 CD8 T 细胞(5 题;10x 5′ scRNA + 配对 scTCR + 分选门元数据);CD8 RNA+ATAC 调控推断(3 题;10x Multiome);人-猴嵌合胚胎(4 题;Smart-seq2、同源基因映射、发育参考、配体-受体库);KRAS 驱动的肺肿瘤衰老(4 题;Parse Biosciences scRNA、外部衰老 signature);致死性 COVID-19 肺病理(5 题;snRNA-seq、BCR 重建、亚群 DE、免疫组化)。另有一题故意**交换两个元数据标签**(singlet 与 tumor_cluster)而保持表达与 TCR 不变,测试 agent 是否凭数据而非标签下结论。

## 主要结果
**总体**:Claude Opus 4.8 / Claude Code **16/63(25.4%;Wilson 95% CI 16.3–37.3)**,Gemini 3.5 Flash / PI 14/63(22.2%),Opus 4.8 / PI 13/63(20.6%),Gemini 3.1 Pro / PI 17.5%,GPT-5.5(Codex 或 PI)15.9%,其余多在 2–11%,最低 Grok 4.3 / PI 1.6%。全部 1,068 条轨迹中只有 125 条(11.7%)通过。**稳健性**:最强组合有至少一次通过的题 8/21、多数通过 6/21、三次全过仅 **2/21**。**题目差异**:5 题无人通过;最容易的伪时间延迟题 26/51(51.0%)。**Harness 效应**:同一模型换 harness 结果改变——Opus 4.8 在 Claude Code 16 vs PI 13;GPT-5.4 在 PI 6 vs Codex 2;GPT-5.5 两边都是 10/63 但**解出的题不同**;每个配对模型有 3–6/21 题的通过数随 harness 变化。**Rubric 诊断**:4 个评审两两相关均值 0.90(最低 0.87);同一轨迹评审 SD 5.5 分、跨重复 SD 6.3 分;通过轨迹 rubric 均值 75.9% vs 失败 58.7%;与终点的相关仅 Pearson r=0.29、Spearman ρ=0.30、AUC 0.77;最高 rubric 十分位里也只有 47/106 通过——**rubric 分高不等于结论对**。**失败模式**:(1) 熟悉的生物学先验掩盖任务证据(把 CD39/PD-1 高的单细胞当作最具肿瘤反应性,忽略物理结合 + 克隆扩增证据;标签互换题中把结果"改回"预期生物学);(2) 把原始丰度当重要性(嵌合体配体-受体题仅 2/50 通过,GPT-5.5 与 Opus 4.8 共 0/6);(3) 把关联当机制(肿瘤-T 细胞结合体题**无人通过**——免疫应答程序对去污染敏感、方向不可定,模型却给出方向性机制);(4) 不整合多模态(KLF2 题只看 RNA DE 提名 S1pr5、Cd160,或从 Klf2 RNA 而非其靶基因协同行为推断活性)。

## 创新点
- **声明条件化的长程可验证基准**:论文声明 → 独立复现 → 受控答案面 + 捷径干扰项,解决"长程任务没有可判真值"的问题。
- 显式的**"机制需谨慎"答案标签**——把"不该下因果结论"本身变成可判分的正确答案。
- 数据扰动探针(元数据标签互换),检验 agent 是凭数据还是凭标签。
- 量化证明 **rubric/LLM 评审分 ≠ 正确性**(AUC 0.77),并量化 harness 效应——agent 评测应以"模型 + harness"为单位。
- 一份具体的单细胞科学推理失败分类(先验替代证据、丰度当重要性、关联当机制、单模态推断)。

## 局限
- 规模小:21 题、5 个系统,每个组合每题 3 次;Wilson CI 很宽(16–37%),组合间差异多不显著。
- 确定性终点判分会惩罚预设答案面之外的合理声明(作者承认);rubric 依赖 prompt 与评审模型。
- 文中未给出代码、题目或轨迹的公开链接,外部难以复现;作者为 LatchBio(提供生物信息平台的公司)。
- 没有空间组学或组织学模态;没有校准/置信度维度——只问"对不对",不问"agent 知不知道自己可能错"。

## 与本研究方向的关系
这是本批中对 **Agent 可信度课题最核心**的一篇,几乎是 Agent 可信度课题的"上游证据":**(1) 声明级评估**——它评的不是步骤而是"这个结论是否被数据支持",与我们的 claim-to-evidence verification 是同一对象;它的"论文声明只作候选、须独立复现才入库"流程,可以直接用于构造肾脏版声明集(取 KPMP/Lake/DKD 图谱论文中的结论,在我们能拿到的数据上复现后入库)。**(2) 失败分类**——"先验替代证据 / 丰度当重要性 / 关联当机制 / 单模态推断"四类,可作为我们组学特有失败分类的起点,肾脏场景再加上环境 RNA 与批次被当作生物信号、snRNA 与 Xenium 不一致时只信一方、把损伤 marker 当因果驱动等。**(3) rubric 分不等于正确性(AUC 0.77)**——直接支持 Agent 可信度课题的立论:需要一个**校准过的** verifier,而不是再加一个 LLM 评审;评审间高一致(0.90)而与真值弱相关,说明"多评审一致"不是可靠性的代理。**(4) 重复与 harness**——最强组合三次全过仅 2/21,同模型换 harness 解出不同题,正是 Agent 可信度课题 "rerun stability"要量化的现象,也提醒 AIRIS WP3 / MLCommons 式的报告应以"模型 + harness"为单位并给出 any/majority/all 三档。对 **伪影注入课题**,KLF2 题的教训(只看 RNA 会选错调控因子,需 chromatin 支持)与我们"跨模态一致性区分伪影与疾病"的思路同源:snRNA 上的异常若在 snATAC/Xenium 上得不到支持,应降低置信度。

## 可复用资产
- **构造协议:** 声明 → 复现 → 受控答案面 → 捷径干扰项 → hard-fail → chokepoint rubric(Methods),可直接用于构造肾脏声明集。
- **报告规范:** Wilson CI + any/majority/all 稳健性计数 + 配对 harness 比较。
- **探针设计:** 元数据标签互换、去污染敏感程序、"机制需谨慎"标签。
- **代码/数据:** 文中未提供公开链接(结果清单文件名为 `results/scbench-long-results-w-glm.csv`);可关注 LatchBio 的 scBench 仓库。
<https://github.com/latchbio/scbench>

## 待读
- 作者提到的同系列基准(空间生物学、表观基因组、治疗学)以及 BioMysteryBench。
- 五个源研究(黑色素瘤 CD8、CD8 multiome、人-猴嵌合体、KRAS 肺肿瘤衰老、COVID 肺)中哪些题型可迁移到肾脏。
- PI harness 是什么、为何对某些模型更好。

## 引用
```bibtex
@misc{Diks2026_260626563,
  title = {scBench-Long: Verifiable Benchmarking of Long-Horizon Single-Cell Biology},
  author = {Diks, Ian and Yang, Zhen and Banerjee, Arjun and Proctor, Tim and Workman, Kenny},
  year = {2026},
  eprint = {2606.26563},
  archivePrefix = {arXiv},
  primaryClass = {q-bio.GN},
  url = {https://arxiv.org/abs/2606.26563}
}
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

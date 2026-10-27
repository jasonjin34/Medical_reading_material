# SCIRIGOR: Evaluating Open-Ended Scientific Analysis Beyond Final Scores

> **文献键** `scirigor-arxiv-2026` · **来源** arXiv preprint(2026) · **类别** agents · **相关度** high · **获取** open
> **链接** <https://arxiv.org/abs/2609.06192> · `status: complete`

---

## 一句话
SciRigor 把科研分析 agent 的产出(代码、结构化结果、图、原子论断)重建为一张**类型化证据图**,要求每条主要论断都有一条在同一次运行中可验证的「数据→变换→结果→图/论断」完整支撑路径,并按 weakest-link 打分、定位最早断裂的边;在 100 个来自 Nature 等期刊的图级案例上,agent 的论断与自身结果一致率几乎与结果是否正确无关(91.8% vs 91.0%),最好的系统 strict 全链成功率仅 18.0%。

## 研究问题
科研编码 agent 正在执行长程开放式分析,产出彼此依赖的代码、数值、图和结论。现有基准要么评代码/执行,要么评整条工作流是否交付,要么孤立地评图或论断 —— 都没有回答:**一条新生成的论断,是否真的被同一次运行中的数据、计算和可视化所支撑?** 典型失败:回归在 log 尺度上存估计值和置信区间,agent 只变换了点估计,写出「增加 18.0%(95% CI 12.6–23.6%)」这样看似正确的句子,而它自己的区间与图仍在错误尺度上。只看最终输出会接受这种「对的句子、错的证据」,而精确参考匹配又会拒绝合理的替代分析。

## 方法
**任务**:给定科学问题、分析就绪数据与研究背景,agent 必须产出四类相互依赖的产物 —— 可执行分析代码、结构化数值结果、数据绑定的可视化、原子科学论断;重跑代码必须能再生结果、图和论断并暴露 provenance。成功 = 覆盖所需发现 + 每条主要论断至少有一条已验证的计算与视觉支撑路径。**证据图评测**:构建期,策展人执行冻结的作者工作流,把数据视图、变换、统计结果、视觉标记与原子发现规范化为语义槽,每个论断槽链接 ≥1 个计算支撑集和 ≥1 个视觉支撑集(集内联合必需,不同集代表被认可的替代方法/编码),并经人工审计。评测期,评估器从运行时 trace、再生结果与独立数值 oracle、捕获的绘图对象和数组、结构化论断记录中**重建**候选证据图(agent 不提交图),节点(artifact fidelity:transform / result / visual / claim)与边(edge validity:数据→变换→结果、结果↔图、结果/图→论断)分开打分。谱系、数值重算、视觉绑定和图连通性程序化检查;冻结的语义匹配器只处理论断复述与范围匹配,且不能推翻失败的结构/数值/provenance 检查。**打分**:路径内取最小(weakest-link),路径间取最大(接受任一完整的已批准替代路径);输出 evidence-chain precision/recall/F1、执行门控的 SoftECS,以及 Strict(执行成功 + 所有必需论断全支撑 + 无无支撑主论断 + 满足全部硬视觉约束)。不完整的链报告最早断裂层级:contract/execution、Data→Transform、Transform→Result、Transform/Result→Visual、Result/Visual→Claim。

## 数据
100 个证据完整的图级案例,来自 27 篇实证文章(Nature、Science 主刊经 Europe PMC 检索,以及 Nature Portfolio 等开放获取来源),覆盖 6 个领域、17 个子领域:经济与政策 24、计算与信息科学 23、社会与行为科学 22、认知科学 15、**生命与健康科学 9**、物理科学 7。准入要求:作者生成的定量图 + 对应 Results 段落 + 作者公开的完整绘图脚本/notebook + 所有被消费的数据文件;两次干净复现并与论文图一致;非 Python 工作流移植为 Python(GPT-5.6 辅助、策展人逐项核对)。评测 11 个 agent/模型配置(GPT-5.5 / GPT-5.6 / GPT-5.6-Sol 不同推理档、Claude Sonnet 5、Kimi-K3、Qwen3.8-Max、Qwen3-Coder-30B-A3B、Qwen-AgentWorld-35B-A3B)。

## 主要结果

- **最好也只有 18.0% strict**:GPT-5.5(xhigh)执行 100%、SoftECS 62.6%、Strict 18.0%;GPT-5.5(high)16.0%;GPT-5.6-Sol(high)13.0%;其余 ≤11%,Claude Sonnet 5、GPT-5.6(low)及两个 Qwen 小模型为 0。
- **执行本身是瓶颈**:Kimi-K3 执行 79.0%、Qwen3.8-Max 47.0%、Qwen3-Coder-30B-A3B 29.0%、Qwen-AgentWorld-35B-A3B 12.0%;Kimi-K3 从 79.0% 执行跌到 SoftECS 35.0%、Strict 1.0%。
- **自洽掩盖错误**:Result→Claim 一致性在 11 行中总是最高或次高;如 GPT-5.6(low)Result→Claim 97.9%,但 result fidelity 仅 47.2%、claim fidelity 52.5%。
- **自洽与正确几乎无关**:Result→Claim 一致性在结果正确的轨迹上通过 91.8%,在结果错误的轨迹上仍通过 91.0%;Result→Visual 稍敏感,但错误结果下仍通过 82.2%(正确时 97.3%)。
- **断在上游**:936 条未达 strict 的轨迹中,48.2% 最早断在数据选择/变换,30.1% 断在契约/执行门,11.9% 在结果计算,可视化+论断+provenance 合计仅 9.8%(合计 78.3% 断在执行或数据/变换层)。在 718 条成功执行的轨迹中,transform fidelity 失败 59.6%、result fidelity 49.3%、claim fidelity 47.9%,而 Result→Claim 一致性只失败 8.6%。
- **复杂度效应**:GPT-5.6-Sol(xhigh)从 1 个输入资产到 ≥5 个,Strict 从 45.7% 降到 25.0%、F1 从 70.9% 降到 57.8%,而只看论断的分数从 71.7% 仅降到 63.7% —— 复杂度主要伤害链完整性而非论断表面合理性。

## 创新点
- **评分对象 = 已验证的数据→论断支撑路径**,而非程序、阶段或最终输出。
- **节点保真与边有效性分离**:区分「产物本身错」与「产物之间的依赖不成立」。
- **weakest-link + 替代路径**:上游错误不能被下游的漂亮呈现修复,同时接受科学上等价的方法与可视化编码。
- **定位最早断裂边**,把失败归因到具体证据层。
- 用作者公开代码+数据的图级复现构造「证据完整」案例,每例两次干净复现 + 人工审计。

## 局限
- 只评可观察的产物,不看 agent 的推理或动作轨迹,因此无法判断失败源于规划、实现还是无根据生成。
- 案例分布由「是否有图级公开代码 + 完整数据」决定,不是文献的概率平衡样本;生命与健康科学只有 9 例,组学类分析占比很小。
- 冻结替代路径之外的方法需进入专家裁决,自动打分对真正新颖的分析仍可能过严。
- 每个配置单次运行,未报告 rerun 方差;论文中未给出代码或数据链接。

## 与本研究方向的关系
这是 **课题 2 的「claim-to-evidence verification」在计算分析场景下最贴近的评测框架**,几乎可以作为课题 2 评测设计的模板。课题 2 要验证的正是「分析肾脏组学的 agent 说的话,是否被它自己跑出来的数据和计算所支撑」—— SciRigor 把这个问题形式化成证据图 + weakest-link + 最早断裂边。可直接迁移的点:**(1) 证据图的节点类型**(数据资产/变换/统计结果/视觉标记/论断)对应组学分析的 QC 过滤→归一化→聚类/注释→差异表达/空间统计→图→结论;**(2) 「自洽 ≠ 正确」的定量证据**(91.8% vs 91.0%)直接说明课题 2 的 verifier 不能只检查报告内部一致,必须做独立的数值重算(oracle);**(3) 失败集中在数据选择/变换层(48.2%)** —— 这与组学分析中最常见的错误位置(细胞过滤、批次校正、归一化、样本分组)高度吻合,可作为 omics-specific failure taxonomy 的上游大类;**(4) 「替代路径」机制** 解决了组学里「多种合理分析方案」的问题(不同归一化、不同聚类分辨率)。对 **课题 1**,它提醒 KidneyAnomalyBench 若让 agent 产出「异常区域 + 论断」,也应要求可重跑、可回溯的证据路径。缺口:SciRigor 没有组学/空间数据,生命健康类只有 9 例,且不评 rerun 稳定性 —— 这恰是课题 2(肾脏组学 + rerun stability)可以补的空白。

## 可复用资产
- **评测框架设计:** 类型化证据图(式 2)、weakest-link/max-over-paths 打分(式 3)、最早断裂层级定义、提交契约(附录 A 表 3–4)。
- **案例构造协议:** 证据闭合(图+段落+作者代码+全部数据)、两次干净复现、人工审计(附录 B–E)。
- 论文未给出代码/数据仓库链接;需关注后续发布。
<https://arxiv.org/abs/2609.06192>

## 待读
- ScienceAgentBench、BLADE、DiscoveryBench、FIRE-Bench、DataSciBench:SciRigor 对比的科研编码/发现基准。
- FactReview(用文献+执行证据审计论文论断)与 SciVisAgentBench。
- 本仓库 `bixbench-arxiv-2025`、`scbench-arxiv-2026`:生物信息/单细胞场景下有没有类似的证据链评测。

## 引用
```bibtex
@misc{scirigor-arxiv-2026, title={SCIRIGOR:Evaluating Open-Ended Scientific Analysis Beyond Final Scores}, author={Liu, Bowen and Nie, Shuo and Du, Bodong and Li, Xiaomeng}, year={2026}, eprint={2609.06192}, archivePrefix={arXiv}, primaryClass={cs.AI}, url={https://arxiv.org/abs/2609.06192}, doi={10.48550/arXiv.2609.06192} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

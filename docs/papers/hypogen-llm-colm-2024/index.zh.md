# Large Language Models as Biomedical Hypothesis Generators: A Comprehensive Evaluation

> **文献键** `Qi_2024` · **来源** COLM 2024 (Conference on Language Modeling)(2024) · **类别** agents · **相关度** high · **获取** open
> **链接** <https://arxiv.org/abs/2407.08940> · `status: complete`

---

## 一句话
用**按发表时间切分**(2023 年 1 月前 = 训练/seen,2023 年 8 月 = unseen)的生物医学「背景知识 → 假设」配对数据集,系统评测 LLM 在 zero-shot / few-shot / 微调 / 工具调用 / 多智能体设置下的假设生成能力,提出 Novelty、Relevance、Significance、Verifiability 四维评分(GPT-4 打分并与人类专家对齐),发现 LLM 在未见文献上也能提出新颖且后来被验证的假设,而"不确定性"(SelfBLEU 衡量)在新颖性与可验证性之间形成权衡。

## 研究问题
用 LLM 做科学假设生成的工作越来越多,但几乎都无法保证**测试数据未被模型训练见过**(训练语料不可追溯),因此无法判断模型是在"发现"还是在"背诵"。另外,假设本身没有唯一正确答案,BLEU/ROUGE 这类重叠指标不足以评价质量。作者要回答:LLM 能否真正 zero-shot 地提出假设?外部知识(few-shot、领域适配、指令微调、工具检索)与多智能体协作是帮忙还是添乱?

## 方法
**任务形式化**:给定指令 I 与从论文抽取的背景知识 X,让模型生成假设 Y,作为文本补全任务。**数据构建**(仿 Self-Instruct 流程):按主题组织 PubMed 论文集 → 用 ChatGPT/GPT-4 总结文献 → 生成「背景–假设」对 → 过滤低质量数据 → 按发表时间切分。**评测模型**:仅选训练语料截止于 2023 年 3 月前的模型以避免污染 —— gpt-3.5-turbo;Alpaca Eval 榜单上的通用指令模型(Vicuna-33B、Llama-2-70B-chat、WizardLM-13B/70B、Openchat-v3.2-super);医学领域模型 PMC-LLaMA-13B、MedAlpaca-13B;并在训练集上微调 WizardLM-13B-V1.2。**提示**:zero-shot、5-shot 随机采样、5-shot 相似度检索(记为 5-shot*)。**指标**:有 ground truth 时用 BLEU/ROUGE;无 ground truth 时用 GPT-4 按四个维度 0–3 打分并给出逐步理由;用 **SelfBLEU** 作为生成集合"不确定性/多样性"的廉价代理(越低越多样)。**多智能体框架**:Analyst(抽取关键词/主题)→ Engineer(用 PubMed 检索,并过滤 2023 年 1 月后的文献以保持 unseen)→ Scientist(综合提出假设)→ Critic(评估并反馈,可回环),可选人类介入;工具调用对比 ReAct 与 OpenAI function calling。

## 数据
**Seen 数据集**:2,700 对(2023 年 1 月前文献),分为训练 2,500 与验证/seen 测试 200;**Unseen 数据集**:200 对,来自 2023 年 8 月发表的论文。起点是约 10,000 篇 PubMed 医学论文(Fig. 2b)。人类评估:3 位生物医学专家对 unseen 测试集中 100 个样本打分。数据与代码开源。

## 主要结果
- **Zero-shot 更新颖,few-shot 更可验证**:几乎所有模型(尤其 WizardLM 系列与 Openchat-v3.2-super)在 zero-shot 下 Novelty 更高,而 few-shot(尤其检索式 5-shot*)提高 Verifiability 与 BLEU/ROUGE、但降低新颖性 —— 一个明确的 novelty–verifiability 权衡。
- **Unseen 反而更好**:与"seen 集靠记忆会更好"的预期相反,模型在 unseen 测试集上 BLEU 更高;作者推测假设生成的复杂性妨碍模型利用参数化的 "dark knowledge"。
- **外部知识不总有益**:领域适配(PMC-LLaMA、MedAlpaca)提升重叠指标与 few-shot 利用,但削弱 zero-shot 能力;指令微调提升记忆、BLEU/ROUGE 与可验证性,但降低新颖性与重要性(微调 WizardLM-13B 的人评 Novelty 仅 0.85)。
- **不确定性分析**:zero-shot 生成 SelfBLEU 更低(更不确定)且 Novelty 更高;few-shot 不确定性更低、Verifiability 更高。
- **人类评估(Table 1)**:GPT-4 平均分与人类平均分高度相关(Pearson 0.73–0.97,Spearman 0.73–0.94,均 > 0.7);人评平均最高为 Llama-2-70b-chat 5-shot(2.33),gpt-3.5-turbo 0-shot 为 2.02。
- **工具与多智能体**:单纯工具调用(PubMed)帮助很小,ReAct 略差于 OpenAI function calling,LLM 难以从检索结果中识别有用信息;多智能体分工通过引入不确定性显著提升假设生成,且工具在多智能体框架中能进一步增益(Fig. 6b,具体数值未在正文列出)。

## 创新点
- **按发表日期切分**来控制可见性,而非用熵-准确率相关间接估计污染 —— 是评测"发现"而非"记忆"的简单而关键的设计。
- 四维假设质量量表(新颖/相关/重要/可验证),并验证 GPT-4 评审与人类专家的一致性。
- 把"不确定性"作为解释 zero-shot vs few-shot、外部知识效应的统一视角。
- Analyst–Engineer–Scientist–Critic 四角色多智能体框架原型,检索端同样做时间过滤以防泄漏。

## 局限
- 背景–假设对由 ChatGPT/GPT-4 自动抽取,作者承认抽取准确性与偏差需进一步评估、应人工标注子集。
- 规模小:unseen 测试仅 200 对,人评仅 100 例(作者称约 5% 抽样);GPT-4 评审本身可能偏好特定风格。
- "Verifiability" 是**评审者打分**的"可被检验",并非真正做实验或核对后续文献得到的验证;Fig. 1 的"后来被证实"是个案。
- SelfBLEU 只是不确定性的粗糙代理;未研究幻觉对假设质量的影响(作者列为未来工作);模型均为 2023 年代模型。
- 纯文本、只依赖文献背景,不接触任何实验数据或组学分析。

## 与本研究方向的关系
对 **Plan B(可信生物医学 agent)** 是一篇方法学上的"前置参照":(1) **时间切分防泄漏**是我们评测 agent 时必须照搬的规范 —— 若让 agent 分析肾脏组学并"提出新机制",要证明它不是在复述训练语料里的 KPMP/Lake 2023 结论,就需要以发表时间(或数据发布时间)为界构建 seen/unseen,并对检索工具做同样的时间过滤;(2) 它的四维量表把"可验证性"交给 LLM 评审打分,而 Plan B 恰恰要把这一步**落到 claim-to-evidence 的实际核对**上(某条结论是否被 agent 自己跑出的数据/统计支持),并用校准的 verifier 替代"GPT-4 给 0–3 分";(3) novelty–verifiability 权衡与"不确定性"视角,可直接转化为 Plan B 的 **rerun stability** 指标:同一任务多次运行得到的结论分布(而非 SelfBLEU)才是更有意义的不确定性度量;(4) 它观察到"工具检索帮助很小、LLM 难以识别有用信息",正好是 omics-specific failure taxonomy 中"检索/证据选择失败"一类的早期证据。对 detect → model → **revert** 主链,它对应链尾"提名可回退异常的基因/扰动"之后的**假设生成与筛选**环节:Plan A 检测出的异常与 virtual tissue 给出的候选,需要以可验证假设的形式交付湿实验,这篇给出了如何评价这些假设的最低限度框架。

## 可复用资产
- **代码与数据:** LLM4BioHypoGen(背景–假设对、seen/unseen 切分、评测脚本)。
<https://github.com/TsinghuaC3I/LLM4BioHypoGen>
- **评测协议:** 时间切分 + 检索端时间过滤;四维 0–3 量表 + GPT-4 逐步理由;SelfBLEU 多样性;GPT-4 与人类的 Pearson/Spearman 一致性检验。
- **Agent 原型:** Analyst / Engineer / Scientist / Critic 角色设计。

## 待读
- 原始短版 arXiv:2311.05965。
- TruthHypo(IJCAI 2025)—— 同一团队方向上对"假设真实性/幻觉"的后续评测。
- 把时间切分思路用于肾脏组学:以 Lake 2023 / KPMP 数据发布为界,检验 agent 结论是否只是复述已发表结果。

## 引用
```bibtex
@inproceedings{Qi_2024,
  title = {Large Language Models as Biomedical Hypothesis Generators: A Comprehensive Evaluation},
  author = {Qi, Biqing and Zhang, Kaiyan and Tian, Kai and Li, Haoxiang and Chen, Zhang-Ren and Zeng, Sihang and Hua, Ermo and Hu, Jin-Fang and Zhou, Bowen},
  booktitle = {First Conference on Language Modeling (COLM)},
  year = {2024},
  eprint = {2407.08940},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2407.08940}
}
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

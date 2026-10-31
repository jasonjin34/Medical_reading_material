# What Proves You Wrong: Benchmarking Language Models on Falsifiable Research Ideation

> **文献键** `falsifiable-ideation-arxiv-2026` · **来源** arXiv preprint(2026) · **类别** agents · **相关度** medium · **获取** open
> **链接** <https://arxiv.org/abs/2608.22948> · `status: complete`

---

## 一句话
Lit2Test 要求每个研究提案按「六字段契约」写出 —— literature_gap、hypothesis、minimal_test、decisive_metric、supporting_result、falsifying_result —— 即**预先承诺能证伪自己的观测**,使提案质量「可判定」而非「可争辩」;在 200 个真实论文邻域、1,200 对双向盲评上,它对四个前沿模型给出在 10,000 次 bootstrap 中全部复现的严格排名,区分度主要来自最小检验与决定性指标的设计,而非文笔。

## 研究问题
现有评估 LLM 科研 idea 的两种范式都缺乏共享的决策规则:**自由形式的 LLM 评判**会随文风与呈现位置摇摆;**以未来论文为答案**的打分只奖励复现某一条已实现轨迹,惩罚合理的替代方向,还容易被知识截止污染。作者主张:一个提案只有在**事先写明什么结果会推翻它**时才可被实验裁决。问题是:能否把这种可证伪性作为评测单元,并让评测协议自证可靠?

## 方法
**实例**:一个四篇论文组成的真实「邻域」,主题相同但留有跨论文张力(例如 ALR2 与 ChatQA 2 在长上下文 QA 上的分歧),所有模型只拿到同一份固定上下文,不设任何「正确的后续论文」。**六字段契约**:去掉任一字段,成对裁决就失去共同决策结构;`minimal_test` 带「反宏大」条款,奖励小而可执行的设计;`supporting_result` 与 `falsifying_result` 构成双向决策规则(Registered Report 思想的模型版)。**协议**:非参赛评委 Gemini 3.1 Pro(Preview)做匿名成对比较,返回 A/B/TIE;每对在原序与反序下各判一次(2,400 次有序判断),两次结论一致才算 **order-stable**,否则记为 order-sensitive 并单独报告、不进入排名;在 stable 结果上做 Bradley–Terry 与 Condorcet 分析,10,000 次 case-level bootstrap。**诊断对照**:90 对子集的五维结构化重评;隐藏的朴素关键词/模板基线;同内容 schema vs prose 渲染对照;单字段明显损坏检查;带风格匹配 sham 编辑的细微损坏审计;第二评委 Doubao Seed 2.0 Pro 全量复评;以及三名标注者的分层人类校准。

## 数据
200 个邻域,来自 800 篇不重复论文(近期 OpenReview/ICLR 相关文献,分 5 批、每批 40 个,附来源审计)。四个参赛模型 GPT-5.2、Claude Sonnet 4.6、GLM-5、DeepSeek-V3.2 各为每个邻域生成一份原生六字段提案(共 800 份),组成 1,200 对 canonical pair。人类校准:20 个邻域、90 对真实提案 + 4 个隐藏朴素对照,3 名高年级计算机本科生按双语协议盲评。

## 主要结果

- **排名稳健**:2,400 次判断折叠为 950 个 order-stable 与 250 个 order-sensitive 案例;排序 GPT-5.2 > Claude Sonnet 4.6 > GLM-5 > DeepSeek-V3.2,是严格 Condorcet 序,在 10,000 次 bootstrap 中全部复现;按邻域聚类 bootstrap 区间宽 11–27% 但排序不变;第二评委复现同一排序,与主评委在 stable 比较上一致 86.1%。即便把全部 250 个 sensitive 案例做对抗性赋值,「GPT-5.2 与 Claude 在上、GLM-5 与 DeepSeek 在下」的两档结构仍保持。
- **主表(主评委 stable W–L–T)**:GPT-5.2 424–49–127;Claude Sonnet 4.6 347–119–134;GLM-5 118–343–139;DeepSeek-V3.2 61–439–100。人类多数胜率:0.805 / 0.775 / 0.233 / 0.214。
- **区分度来源**:结构化总判与整体判决在 152/180(84.4%)次上一致;8/8 个隐藏朴素对照全部被识别。minimality/feasibility 是区分自然输出最强的维度;falsifiability 只在 33/180 次判断中非平局、仅 1/180 次是唯一决定维度 —— 它是**准入下限**而非区分器。
- **评委跟踪实质而非文风**:单字段明显损坏时,干净提案在每个维度 40/40 次全胜(目标分数平均降 1.73 / 2.00 / 1.95);sham 编辑本身不改变判决(每维 0 胜 40 平 0 胜);扣除 sham 后对干净提案的偏好:grounding 0.550、decisive metric 0.775、falsifiability 0.537,合并 0.621,95% CI 均不含 0。
- **人类印证**:人类识别朴素对照 11/12;60 个 stable 真实对中 39 个有明确人类多数,其中 34/39(87.2%)与评委一致;人类 BT 排名 88.3% 的 bootstrap 与评委排名最多差一次逆序。但标注者间一致性偏低(Krippendorff α 为 modest),人类的 falsifiability 分数无法区分胜负方(差为 0)。

## 创新点
- **把可证伪性变成评测单元**:六字段契约让每个提案自带「什么结果推翻我」,使评判有共同决策结构。
- **前瞻式构造、无答案键**:不以未来论文为标准答案,避免奖励单一轨迹与污染。
- **自审计的评测协议**:双向顺序折叠、把 order-sensitive 案例显式分离、隐藏对照、损坏/sham 审计、第二评委与人类校准组合成「评委可信度包络」。

## 局限
- 人类校准只覆盖 20/200 个邻域、3 名本科生标注者,且标注者间一致性偏低,不能做全基准验证。
- 每个版本只有一个 canonical 评委(虽有第二评委复现)。
- **不执行**:可测试性是下游成功的前提,不是预测器 —— 提案是否真的成功没有被检验。
- 只用 ML 相关文献,生物医学领域未测;细微损坏审计存在 3.9% 泄漏等构造瑕疵。

## 与本研究方向的关系
与 **Agent 可信度课题** 和 revert 阶段都有关,但属于方法论借鉴(relevance: medium)。**(1) revert 阶段的提名格式**:detect → model → revert 末端,agent 提出「扰动基因 X 可把异常肾小管/间质状态拉回正常」时,可以强制用类似六字段契约输出 —— 证据缺口、假设、最小湿实验(如某细胞系/类器官的 knockdown)、决定性读数(如损伤评分或某标志物)、支持结果与**证伪结果**。这样湿实验结果天然可以回填为「通过/被证伪」,给 Agent 可信度课题的 claim-level 验证一个干净的标签。**(2) 评委可靠性审计的工程模板**:Agent 可信度课题若用 LLM verifier,Lit2Test 的「双向顺序折叠 + order-sensitive 单列 + 隐藏朴素对照 + 单字段损坏 + 风格匹配 sham」是一套可直接复用的 verifier 自检清单,也对应 Agent 可信度课题的 rerun-stability 关注。**(3)** 它和 `ideation-execution-gap-arxiv-2025` 一起提醒:可证伪 ≠ 会成功,真正的标签仍需执行(对我们是湿实验)。伪影注入课题关系较弱。

## 可复用资产
- **基准、构造流水线与审计产物:**
<https://github.com/rrustlee/lit2test-benchmark>
- **六字段契约与评分量表**(grounding、hypothesis specificity、minimality/feasibility、decisive metric、falsifiability 五维)。
- **顺序折叠规则 + Bradley–Terry/Condorcet + case-level bootstrap** 的统计流程。

## 待读
- ResearchStudio-Idea(IdeaSpark):生成阶段即要求可证伪预测的并行工作。
- HARPA:带指标与对照、部分通过执行评估的可测试提案生成。
- `co-scientist-nature-2026` 中的 disproof review 机制。

## 引用
```bibtex
@misc{falsifiable-ideation-arxiv-2026, title={What Proves You Wrong: Benchmarking Language Models on Falsifiable Research Ideation}, author={Wang, Ziyue and Yuan, Aomufei and Yao, Yiran and Yao, Linli and Zuo, Hongyao and Gong, Ziwen and Liu, Yuanxin and Li, Shicheng and Cai, Yishuo and Yang, Tong and Sun, Xu and Li, Xiaohui and Bai, Haoli}, year={2026}, eprint={2608.22948}, archivePrefix={arXiv}, primaryClass={cs.CL}, url={https://arxiv.org/abs/2608.22948}, doi={10.48550/arXiv.2608.22948} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

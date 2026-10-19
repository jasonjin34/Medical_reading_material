# A multi-agent system for automating scientific discovery

> **文献键** `Ghareeb_2026` · **来源** Nature(2026) · **类别** agents · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1038/s41586-026-10652-y> · `status: complete`

---

## 一句话
FutureHouse 的 Robin 把文献检索 agent(Crow/Falcon,基于 PaperQA2)与数据分析 agent(Finch)串成一个 lab-in-the-loop 闭环:给定疾病,自动提出机制、体外模型与候选药物,人类按其建议做实验并上传原始数据,Finch 跑 8 条独立分析轨迹取共识,Robin 再据此更新假设;在干性 AMD 上,它提出「增强 RPE 吞噬」策略,找到 ROCK 抑制剂 ripasudil(比 DMSO 提升 1.89 倍)与 KL001,并经 RNA-seq 发现 ABCA1 上调——正文所有假设、实验方向、数据分析与数据图均由 Robin 产生。

## 研究问题
药物重定位史上常见「洞见早已在文献里,却多年后才变成疗法」(dabrafenib 护耳约 10 年、ketamine 22 年、KarXT 13 年)。已有 LLM 系统能生成假设(多 agent 分解、领域微调、工具、人类反馈),但**没有一个系统自动化了科学过程的全部关键智力步骤**——生成假设与实验策略、分析实验结果、再据新数据修正假设。Robin 要把文献驱动的假设生成与实验数据的自主分析连成一个连续反馈系统。

## 方法
**组件**:Crow(简明文献综述)与 Falcon(深度文献报告)均基于 PaperQA2,可访问科学文献、临床试验报告与 Open Targets;Finch 是基于 Aviary 框架、ReAct 风格的 Jupyter 原生数据分析 agent,在预建 Docker(BixBench-env:v1.0)里逐行写并执行 Python/R,只有 edit_cell 与 submit_answer 两个工具。Robin 本体用 OpenAI o4-mini 综合文献与生成假设,用 Claude 3.7 Sonnet 作两两比较评委。**假设生成**:提出疾病一般性问题 → Crow 作答 → 归纳 10 个可能的因果机制 → 为每个机制让 Crow 写体外模型报告 → LLM 评委两两比较排序 → 选最佳体外模型 → 同样流程提出 30 个候选药 → Falcon 为每个写评估报告 → LLM 评委锦标赛排序。≤25 个假设时全配对循环赛,>25 个随机抽 300 对;用 Bradley–Terry–Luce 模型估计强度、降低位置偏差;评委提示由专家两两比较结果交给 Gemini 2.5 Pro 生成。**数据分析**:上传 .FCS(流式)或基因计数(RNA-seq)与分析提示,Finch 并行跑 8 条独立轨迹,最后元分析合成共识结论。作者注意到 agentic 版 Robin 几乎总按相同顺序调用工具,于是改写为确定性的 Jupyter notebook 流程以提高稳定性。

## 数据
**实验体系**:第一轮用 ARPE-19 细胞 + pHrodo 荧光微珠的吞噬流式实验(Robin 原建议用原代/干细胞 RPE 与感光细胞外节,出于可得性改用);RNA-seq(ARPE-19 + Y-27632);第二轮 10 个药物;再用 60 岁以上供者的原代 RPE 干细胞(RPE-SC)+ 荧光标记牛视杆外节(ROS)复筛,加 LDH 细胞毒、ELISA、免疫染色。**评测数据**:BixBench 中与药物发现相关的 170 道题(131 生信、39 生统,38 个数据胶囊)。RNA-seq 原始数据存于 SRA(PRJNA1464762)。

## 主要结果
- **发现链**:综述 151 篇论文提出 10 个 dAMD 机制,选中「增强 RPE 吞噬」与流式吞噬实验;再综述约 400 篇提出 30 个候选。第一轮测前 5(exendin-4、fingolimod、MFGE8 作阳性对照、Y-27632、AICAR+TUDCA),Y-27632 为命中,与人工分析一致。
- **RNA-seq**:Robin 建议对 Y-27632 处理细胞测序;Finch 发现 ABCA1 上调约 3 倍(校正 P = 2.13×10⁻⁸³),8 条轨迹中超过 50% 识别出相同差异基因;GO 富集为肌动蛋白组织、小 GTPase 信号与自噬。
- **第二轮**:测 10 个新候选,ripasudil(日本已批准的青光眼用 ROCK 抑制剂)使吞噬提升 **1.89 倍**(人工分析 1.75 倍),剂量反应上比 Y-27632 更强;在 RPE-SC + ROS 中复现,且 LDH 释放随 ripasudil 剂量升高而下降;KL001(稳定 CRY 的生物钟调节剂)在 RPE-SC 中也是命中;RPE-SC 中 ripasudil 同样上调 ABCA1。
- **消融(参考文献幻觉)**:把 Falcon 或 Crow+Falcon 换成 o4-mini 后,药物提案中的幻觉参考文献显著增加;在 15 个检测方案提案中,Crow 无幻觉引用,o4-mini 的引用 **44.5 ± 6.37%** 为幻觉。LLM 评委锦标赛中三种消融版本质量都显著更差。
- **Finch 评测**:按专家 rubric,第二轮 RNA-seq 任务 86%、流式 100%(各 3 次);BixBench 170 题上 Finch **22.8 ± 1.7%**,裸 Claude 3.7 Sonnet 1.6 ± 1.2%;生统子集 47.9% 远好于生信子集 15.3%(多步流程对参数敏感)。失败模式分为错误答案、匹配干扰项、格式错误、不确定、空/失败五类。
- **对照 OpenAI Deep Research**:同一提示要求 19 个候选,Deep Research 给出 17 个不重复药物,在 RPE-SC 吞噬实验中**零命中**,且没有提出 ROCK 抑制。
- **评委与成本**:LLM 评委的 top-10 平均有 7.25 个与专家 top-10 重合;同一对比较的自一致率 88%,而人类专家仅 61%。一次完整运行(45 次 Crow + 30 次 Falcon)约 US$10.76;约 30 分钟综合 551 篇文献(估计人工约 294 小时),整个发现周期认知工作量从 359–424 人时降到不足 2 小时。

## 创新点
- 第一批把「文献驱动的假设生成」与「实验数据的自主分析」接成连续闭环、并在体外迭代发现候选疗法的系统之一。
- **多轨迹共识分析**:利用 LLM 分析的随机性,8 条独立轨迹 + 元分析,把「每次结果不一样」从缺陷变成稳定性手段。
- 用 BTL 模型 + 分布式两两比较做 LLM 评委排序,并量化评委与专家的一致性与自一致性。
- 有针对性的消融(检索 agent 对参考文献幻觉的作用)和与 Deep Research 的湿实验级对照。

## 局限
- 只是「半自主」:实验由人执行,且实验体系常偏离 Robin 原建议(细胞系、底物);流式数据由 Finch 分析,但 RNA-seq 的去复用与比对由人完成。
- 只输出实验大纲,不产出可直接执行的精确协议;Finch 依赖专家写的任务提示,脱离这些提示时(BixBench)准确率只有 22.8%,多步生信尤其弱。
- 只有一个疾病、体外验证;ripasudil 与 KL001 需体内模型乃至随机对照试验确认;ABCA1 与自噬的机制推断仍待验证。
- 评估中多处依赖 LLM 评委(Claude 3.7 Sonnet),而评委提示本身由 LLM 从专家判断生成。

## 与本研究方向的关系
Robin 是 **revert 环节的「提名 → 湿实验 → 再提名」闭环**的现成样板:疾病表型(RPE 吞噬下降)→ 候选扰动 → 体外读出 → 机制组学(RNA-seq)→ 新靶点(ABCA1)。把它移到我们的方向,就是:detect 阶段给出肾组织的异常区域与异常程序,model 阶段在虚拟组织里预测扰动效果,Robin 式的循环负责把文献证据与扰动预测合并成候选,并在湿实验后由 Finch 式 agent 分析读出。对 **Plan B(可信 agent)** 这篇提供了三组直接可用的实证:**(1) rerun 稳定性**——作者明说 Finch 相同提示相同数据各次结果不同,用 8 条轨迹 + 共识来对冲;这正是 Plan B 要量化的「重跑稳定性」,而且「>50% 轨迹一致」是一个现成的稳定性指标,可以推广为对每条 claim 的一致率;**(2) 引用幻觉**——o4-mini 在方案中 44.5% 的引用是幻觉,而 PaperQA2 类检索 agent 能把它压到零,这给 claim-to-evidence verifier 提供了一个有基准值的子任务(引用存在性/支撑性检查);**(3) 组学特定失败**——BixBench 上生信多步流程(15.3%)远差于单步统计(47.9%),失败被分为错误答案、匹配干扰项、格式、不确定、空/失败五类,可作为我们「组学特定失败分类」的起点,再细化到 snRNA/snATAC/Xenium 特有的错误(如 ambient RNA、doublet、分割错误导致的伪差异表达)。另一个值得注意的点是 LLM 评委自一致 88% vs 专家 61%:「更一致」不等于「更正确」,Plan B 的 verifier 校准评估需要同时报告一致性与准确性。

## 可复用资产
- **代码与示例轨迹:** Robin 与 Finch 的 GitHub 仓库(含 prompts.py)。
<https://github.com/Future-House/robin> · <https://github.com/Future-House/finch>
- **数据:** RNA-seq 原始数据 SRA BioProject PRJNA1464762。
- **评测设计:** 参考文献人工核验协议(盲评、找不到原文即判幻觉)、BTL + 置换检验的消融比较、Finch 的 BixBench 170 题子集与五类失败模式、LLM 评委与专家的 top-10 重合及自一致性。

## 待读
- PaperQA2(`paperqa2-arxiv-2024`)与 BixBench(`bixbench-arxiv-2025`)——Crow/Falcon 与 Finch 的底座与评测。
- 后继系统 Kosmos(`kosmos-arxiv-2025`):world model 取代 Robin 的固定流程,代码量提升 9.8 倍。
- Supplementary Tables 6–9(各消融的逐条引用核验)——可作为引用幻觉检测的标注样本。

## 引用
```bibtex
@article{Ghareeb_2026, title={A multi-agent system for automating scientific discovery}, volume={655}, ISSN={1476-4687}, url={http://dx.doi.org/10.1038/s41586-026-10652-y}, DOI={10.1038/s41586-026-10652-y}, number={8122}, journal={Nature}, publisher={Springer Science and Business Media LLC}, author={Ghareeb, Ali E. and Chang, Benjamin and Mitchener, Ludovico and Yiu, Angela and Szostkiewicz, Caralyn J. and Shved, Dmytro and Gyimesi, Gavin J. and Laurent, Jon M. and Wright, Samantha M. and Razzak, Muhammed T. and White, Andrew D. and Finnemann, Silvia C. and Hinks, Michaela M. and Rodriques, Samuel G.}, year={2026}, month=May, pages={497–505} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

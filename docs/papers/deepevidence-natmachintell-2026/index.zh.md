# Empowering biomedical evidence exploration and synthesis with deep knowledge graph research

> **文献键** `Wang_2026b` · **来源** Nature Machine Intelligence(2026) · **类别** agents · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1038/s42256-026-01266-0> · `status: complete`

---

## 一句话
DeepEvidence 是一个面向生物医学的 deep research agent:用 orchestrator + 子 agent 的多智能体架构,把「广度优先(BFRS)」与「深度优先(DFRS)」两种检索策略编排起来,跨异构知识库与文献做长程探索,并**增量构建一张 evidence graph** 记录实体、关系与出处,使整个研究过程可追踪、可归因、可验证;在四个公开基准与七个新建任务上全面超过通用 agent。

## 研究问题
生物医学证据散落在结构极不相同、且持续演化的资源里 —— PubTator/PKG(文献衍生知识)、KEGG/Gene Ontology(通路与功能注释)、OpenTargets(基因-疾病)、BioThings、ChEMBL、OpenFDA、ClinicalTrials.gov —— 彼此难以互操作,跨资源推理在实践中极难。通用 deep research 系统(OpenAI DeepResearch、Gemini、Perplexity)主要在非结构化网页文本上工作,不适配这种场景;而已有的生物医学 agent(Biomni、ToolUniverse)虽然接了大量知识库 API,却**只做浅层探索**——问几次就回答,且庞大的工具集反而引发 tool confusion,选错工具、走错推理路径。

## 方法
**架构**:一个 orchestrator agent 维护研究计划与内部 evidence graph,把任务分派给两类 research 子 agent —— **BFRS** 做多图查询,快速铺开一跳邻域(例如跨 disease–drug、gene–disease 图找某疾病相关的药物);**DFRS** 在 BFRS 浮出的关键实体上做多跳深挖(例如递归追溯文献引用,构建系统综述所需的证据图)。作者刻意不叫 BFS/DFS:agent 是自主选择遍历步骤,而非遵循固定图论规则,并且能通过识别共享实体或推断跨图关系,在异构知识图之间架 **bridge entities**。**环境**:为异构 Web API 实现统一的实体检索与取数接口,一次药物查询即可并行触发 KEGG、ChEMBL、OpenFDA、OpenTargets 等多源查询;并配一个**执行沙箱**,让 agent 写代码大规模调用 API、把结果落成结构化文件再做下游抽取与分析。**关键设计**:evidence graph 持续更新,保存出处(provenance),支撑透明推理与人工验证。作者强调这**不是 GraphRAG**,也不是把生物医学数据预处理成统一知识图后再遍历 —— 因为底层资源本就碎片化、异构且不断变化。

## 数据
评测分两层。**四个公开基准**:HLE-Medicine(Humanity's Last Exam 医学子集)、LabBench-LitQA2(需检索并综合文献证据)、SuperGPQA-Medicine-Hard(困难机制推理)、TrialPanorama-EvidenceQA(基于真实临床试验的证据推理)。**七个自建任务**:覆盖生物医学发现全生命周期的四个阶段 —— 药物发现、临床前体内实验、临床试验设计、循证医学(EBM)。知识源涵盖 PubMed、ClinicalTrials.gov、KEGG、Gene Ontology、OpenTargets、ChEMBL、OpenFDA、BioThings、PubTator 等。测试集公开在 HuggingFace。

## 主要结果
公平性设定很关键:**所有 agent 系统(含 DeepEvidence)都用同一个底座 LLM(GPT-5)**,基线为带文献检索能力的 GPT-5 与 Sonnet-4.5,以及通用生物医学 agent Biomni 与 ToolUniverse。四个公开基准全线领先:**HLE-Medicine 40.0%**(Biomni 20.0%、ToolUniverse 10.0%、Sonnet-4.5 3.3%、GPT-5 3.3%);**LabBench-LitQA2 64.7%**(Biomni 48.9%、ToolUniverse 25.0%);**SuperGPQA-Medicine-Hard 47.1%**(Biomni 40.7%、Sonnet-4.5 43.6%);**TrialPanorama-EvidenceQA 96.0%**(Biomni 84.0%、Sonnet-4.5 88.0%)。自建任务上同样领先,例如 68%(Biomni 56%、ToolUniverse 40%)、72%(两者均 44%)、80%(Biomni 68%)、52%(Biomni 36%);在八个评估维度中的五至六个上优于 Biomni。作者的解释是:基线并非缺工具,而是**探索太浅 + 工具混淆**,而 BFRS–DFRS 在 evidence graph 引导下做的是结构化、有针对性的深挖,这正是多跳推理与证据综合类任务需要的。

## 创新点
- 把 deep research 范式落到生物医学的异构知识源上,而非通用网页文本。
- BFRS/DFRS 双策略编排:先铺开一跳邻域,再在关键实体上多跳深挖,由 agent 自主决定遍历。
- **显式 evidence graph 作为 agent 记忆**:保存实体、关系与 provenance,让研究过程可追踪、可归因、可被人类专家验证 —— 这是本文最可迁移的一点。
- 执行沙箱让 agent 以写代码的方式大规模调用 API 并做结构化落盘分析。
- 新建七个覆盖发现全流程(药物发现→临床前→试验设计→EBM)的基准任务。

## 局限
- 知识源覆盖仍不完整,现有基准只反映生物医学研究任务的一个子集。
- 目前依赖 KEGG、Gene Ontology 这类 schema 稳定、API 优质的**精心策划**知识库;面对私有或自建源(缺失值、结构不一致、接口残缺)需要 agent 自己造工具。
- **缺乏显式的概率建模或不确定性机制来调和冲突证据**,只能依赖底座 LLM 的参数化推理去权衡 —— 作者自陈这是未来工作(校准置信度、概率推理框架)。
- 只有 BFRS/DFRS 两种策略,作者承认不太可能最优,理想情况应让 agent 自主发现更好的研究策略。
- 尚未达到专家水平;且**只处理文本模态**,影像、结构生物学、蛋白组等多模态数据未纳入。

## 与本研究方向的关系
这篇处在 detect → model → revert 主链**之上的证据层**:当 pipeline 末端提名「哪些基因/扰动可以把异常拉回正常」时,这个提名必须挂着一条可查的证据链,否则无法进入湿实验优先级排序。DeepEvidence 提供的正是这条链的工程形态 —— evidence graph 保存实体、关系与 provenance,使每一步都可归因、可被专家验证。三点可复用:**(1) evidence graph 作为可审计记忆的具体实现**,可直接借用来给靶点提名做出处追踪;**(2) BFRS/DFRS 的策略分工**,对应「先扫一遍候选基因的一跳关联,再对入围者深挖文献与试验证据」这种真实工作流;**(3) 同底座 LLM 的公平对照设定**(所有系统都跑 GPT-5),是评估 agent 时该抄的实验规范 —— 否则分不清赢在 agent 设计还是赢在底座模型。**最有价值的是它自陈的空白**:它没有不确定性建模来调和冲突证据,且只做文本 —— 而本方向手里恰好有两样它没有的东西:一是数据层的可信度概念(证据所依赖的数据本身有多可靠),二是影像与空间组学模态。把「数据可信度 → 证据置信度 → 结论置信度」这条链打通,正是它留下的接口。

## 可复用资产
- **代码:** DeepEvidence 实现(BioDSA 仓库内)。
<https://github.com/RyanWangZf/BioDSA/tree/main/biodsa/agents/deepevidence>
- **数据:** 实验用测试集公开。
<https://huggingface.co/datasets/zifeng-ai/DeepEvidence>
- **评测协议:** 四个公开基准(HLE-Medicine、LabBench-LitQA2、SuperGPQA-Medicine-Hard、TrialPanorama-EvidenceQA)+ 七个自建任务;关键是**所有对比系统统一底座 LLM**。
- **基线系统:** Biomni、ToolUniverse —— 评估生物医学 agent 时的标准对照。

## 待读
- Biomni 与 ToolUniverse 原文(本仓库还没有条目),它们是这条线的默认基线。
- TrialPanorama 与 LabBench 的基准构造方式,看证据类任务怎么出题、怎么定 ground truth。
- 跟进「校准置信度 / 概率推理」这条它标出的未来工作,看有没有已经动手的后续。

## 引用
```bibtex
@article{Wang_2026b, title={Empowering biomedical evidence exploration and synthesis with deep knowledge graph research}, volume={8}, ISSN={2522-5839}, url={http://dx.doi.org/10.1038/s42256-026-01266-0}, DOI={10.1038/s42256-026-01266-0}, number={7}, journal={Nature Machine Intelligence}, publisher={Springer Science and Business Media LLC}, author={Wang, Zifeng and Chen, Zheng and Yang, Ziwei and Wang, Xuan and Jin, Qiao and Peng, Yifan and Lu, Zhiyong and Sun, Jimeng}, year={2026}, month=July, pages={1142–1156} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

# Biomni: A General-Purpose Biomedical AI Agent

> **文献键** `Huang2025_Biomni` · **来源** bioRxiv(2025) · **类别** agents · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1101/2025.05.30.656746> · `status: complete`

---

## 一句话
Biomni 是斯坦福 Leskovec 组的通用生物医学 agent:先用一个 "action discovery agent" 从 2,500 篇 bioRxiv 论文(25 个子领域)里挖出任务/工具/数据库,经人工验证后建成统一环境 **Biomni-E1**(150 个专用工具 + 105 个软件包 + 59 个数据库),再用基于 CodeAct 的 **Biomni-A1**(检索工具子集 → 计划 → 写代码执行 → 迭代)零样本完成跨领域任务,并在一个 CRISPR 克隆案例中做了湿实验验证。它已成为后续生物医学 agent 论文的**默认基线**。

## 研究问题
已有生物医学 agent 多是为窄任务定制的专用 workflow,难以跨子领域泛化;而通用 LLM 缺少一个**显式定义生物医学动作空间**的环境(工具、数据库、软件、实验 protocol),也缺少能在其中自主组合动作、不依赖预设模板的 agent 架构。作者要回答:能否构建一个"虚拟 AI 生物学家",在遗传学、基因组学、药理、微生物、临床基因组学等多个领域零样本工作。

## 方法
**(1) 动作空间发现**:取 bioRxiv 25 个学科类别各最近 100 篇(共 2,500 篇),LLM 分块阅读 PDF,抽取任务、软件、数据库三类可执行要素;过滤到约 1,900 个常见任务后人工去重、剔除"几行代码就能做"的琐碎任务,只保留需领域知识的(湿实验 protocol、AI 预测模型等)。**(2) Biomni-E1**:人类科学家与带网页检索的软件工程 agent 协作实现每个工具,每个工具必须有通过的测试用例,并满足命名/文档/输出为 LLM 友好的研究日志等五项检查;大型关系型数据库(PDB、OpenTargets、ClinVar)各用**一个**自然语言查询函数封装(内部由 LLM 解析 schema 生成查询),无 Web API 的库下载进 data lake 并预处理为 pandas DataFrame;软件装在统一容器里,支持 Python/R/Bash。**(3) Biomni-A1**:基于 CodeAct——先由独立 LLM 做 prompt-based 检索,挑出与问题相关的工具/数据/软件子集(避免长上下文),再生成编号计划,逐步写代码执行、读观察、修正计划,直到收敛。关键设计是**以代码作为统一动作接口**(循环、并行、条件逻辑、非标准函数签名都能表达),而非传统 function-calling。

## 数据
**问答基准**:LAB-Bench 的 DbQA 与 SeqQA(45 题开发集用于调接口,315 题留出测试集,三次运行取平均;作者称因 API 成本只取全基准的 12.5%)、HLE 生物/医学 14 个子学科共 52 题(无开发集)。**8 个自建真实任务**:变异优先级(Open Targets Genetics)、GWAS 因果基因(Shringarpure et al.)、CRISPR 扰动筛选设计(Schmidt et al.,IL-2 screen,18,939 候选基因)、罕见病诊断与患者基因优先级(MyGene2 / Alsentzer et al.)、药物重定位(Huang et al.,以 EHR 中临床医生的 off-label 处方模式为对齐标准)、scRNA-seq 细胞注释(CellxGene 等,20k–50k 细胞)、微生物组差异丰度(5 个数据集)。**案例**:30 人可穿戴数据(458 个 Excel、CGM + 体温,另有 10 人 227 晚睡眠、脂质组 652 / 代谢组 731 / 蛋白组 1,470 特征)、人胚胎骨骼发育 snRNA+snATAC multiome(约 336,000 细胞核,5–11 周)、克隆基准与 B2M sgRNA 湿实验。

## 主要结果
**LAB-Bench**:DbQA **74.4%**(人类专家 74.7%,ReAct+Code 40.8%);SeqQA **81.9%**(人类 78.8%)。**HLE 子集**:**17.3%**(base LLM 6.0%、coding agent 12.8%、literature agent 12.2%)。**8 个真实任务**(底座 Claude Sonnet 3.7):相对 base LLM 平均相对提升 **402.3%**、相对 ReAct+Code **43.0%**、相对自身 ReAct 消融版 **20.4%**——说明"代码式计划 + 环境落地"是主要贡献来源;每个任务平均 6–24 步,调用 0–4 个专用工具、1–8 个软件包、0–3 个 data lake 条目。**案例**:可穿戴数据中报告餐后体温平均升高 2.19°C(中位 1.10°C,个体间 −0.11 到 15.56°C);multiome 上自主跑完 10 步 pySCENIC/GRNBoost2/cisTarget/AUCell + ATAC 过滤的 GRN 流程(约 5 小时),复现 RUNX2 等已知调控,并提出 AUTS2、ZFHX3、PBX1 在多个骨骼谱系中高活性(作者也承认 PBX1 本是已知骨骼调控因子);克隆基准中盲评专家认为 Biomni 与资深人类专家准确度/完整度相当、明显优于受训者;B2M sgRNA 克隆按 Biomni protocol 原样执行,两个挑选克隆 Sanger 测序完全比对。

## 创新点
- **从文献自动挖掘动作空间**,再人工验证成可执行环境——把"环境构建"变成可扩展流程,而非手工列工具。
- 大数据库"一库一函数 + LLM 生成查询"的封装方式,显著压缩工具数量。
- 代码即动作(CodeAct)+ 检索式工具选择 + 自适应计划,在多领域零样本任务上系统性地优于 ReAct 式链式调用。
- 少见的**湿实验闭环验证**(克隆 protocol 原样执行并测序确认)。
- 开源代码、Harvard Dataverse 数据与 Web 界面,降低了作为基线复用的门槛。

## 局限
- 作者自陈:评测任务只覆盖领域的一个子集;动作发现只取"最近"文献,可能遗漏经典方法;在需要临床判断、新实验推理、深度综合的任务上仍不及专家。
- **评测粒度粗**:LAB-Bench 只用了 12.5% 子集;8 个真实任务多为单底座模型,结果主要以相对提升呈现;多个案例的"新发现"(如新 TF、睡眠规律)只经作者"人工核对 trace 和代码",未做独立验证。
- 文中克隆基准规模前后不一(结果部分写 10 个任务、方法部分写 20 个开放问题与三位专家),阅读时需留意。
- **没有不确定性、可复现性或声明-证据核查机制**:agent 输出的结论没有置信度,也没有重跑稳定性分析。
- 后续独立评测显示其上限有限:HeurekaBench 中它虽是三个单细胞 agent 里较强的,开放题正确性也只有约 2.3–2.6/5;SpatialAgent v2 的心脏 MERFISH 注释中它出现 label collapse(偏向内皮细胞,总体准确率 0.394)。

## 与本研究方向的关系
Biomni 处在 detect → model → revert 链条的**分析执行层**:它本身不做异常检测,也不建 virtual tissue,但它是"让 agent 跑完一套组学分析并给出生物学结论"的事实标准基线。对 **Plan B(可信生物医学 agent)** 最直接:它是我们要审计的典型对象——一个会自主写代码分析肾脏 snRNA/snATAC/Xenium、然后输出"新调控因子 / 新规律"式声明的系统,而它恰恰**没有**声明-证据核查、没有校准置信度、没有重跑稳定性评估;其 multiome 案例(snRNA+snATAC GRN、靠人工读 trace 来判断是否幻觉)几乎就是 Plan B 想自动化的那个"verifier"场景,可直接借来构造肾脏版任务:让 Biomni 在 KPMP/Lake 数据上跑 GRN 或差异分析,再用我们的 verifier 逐条检查结论是否被数据支持、多次重跑是否一致,并按组学特有失败类型(批次/环境 RNA 被当成生物信号、单模态推断调控等)建分类。对 **Plan A** 的价值是间接的:Biomni-E1 的"一库一函数"和 data lake 设计可作为把 KidneyAnomalyBench、KPMP/HuBMAP 参考数据接入 agent 环境的工程模板;但要警惕它在空间注释上的 label collapse——在异常检测场景下,这种系统性偏置会把真正的病灶细胞态"吞"进常见类别。对 revert 阶段,它的 CRISPR 筛选设计任务(从 ~19k 基因中选扰动集)和湿实验克隆闭环,是"agent 提名扰动 → 湿实验验证"这条路在工程上可行的一个早期样例。

## 可复用资产
- **代码:** Biomni 开源实现(环境 + agent)。
<https://github.com/snap-stanford/biomni>
- **数据:** Biomni 使用的全部数据(data lake 等)。
<https://doi.org/10.7910/DVN/CE4ZYG>
- **Web 界面:** 在线试用(不可用于受保护健康信息)。
<https://biomni.stanford.edu>
- **评测协议:** 8 个零样本真实任务的 prompt 与指标(见 Methods),可作 Plan B 基线任务模板。

## 待读
- 补充材料中的工具清单(Supp. Tables 1–30)与 trace 分析(Supp. Figs 6–16),看哪些单细胞/空间工具已内置。
- BiomniBench(本仓库 `biomnibench-biorxiv-2026`)与 HeurekaBench 对 Biomni 的独立评测。
- CodeAct 原文,以及 Biomni 的后续版本(是否加入 RL 训练、多模态输入)。

## 引用
```bibtex
@article{Huang2025_Biomni, title={Biomni: A General-Purpose Biomedical AI Agent}, url={http://dx.doi.org/10.1101/2025.05.30.656746}, DOI={10.1101/2025.05.30.656746}, journal={bioRxiv}, publisher={openRxiv}, author={Huang, Kexin and Zhang, Serena and Wang, Hanchen and Qu, Yuanhao and Lu, Yingzhou and Roohani, Yusuf and Li, Ryan and Qiu, Lin and Li, Gavin and Zhang, Junze and Yin, Di and Marwaha, Shruti and Carter, Jennefer N. and Zhou, Xin and Wheeler, Matthew and Bernstein, Jonathan A. and Wang, Mengdi and He, Peng and Zhou, Jingtian and Snyder, Michael and Cong, Le and Regev, Aviv and Leskovec, Jure}, year={2025}, month=June }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

# Why Do Multi-Agent LLM Systems Fail?

> **Bibkey** `Cemri2025_250313657` · **Venue** NeurIPS 2025 Datasets and Benchmarks Track (2025) · **Category** agents · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2503.13657>
> `status: complete` — 基于 arXiv v3(NeurIPS 2025 D&B 版本)正文精读;附录(失败模式定义、案例研究、相关性分析)未逐条核对。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> UC Berkeley 团队用 Grounded Theory 对 150+ 条多智能体系统(MAS)执行轨迹做质性分析,提炼出首个经验性的多智能体失败分类 **MAST**(14 种失败模式、3 大类:系统设计问题 / 智能体间失配 / 任务验证),人工标注一致性 κ = 0.88;再用校准过的 LLM 标注器(o1,κ = 0.77)把它扩展成 1,642 条标注轨迹的 **MAST-Data**,覆盖 7 个 MAS 框架。
<!-- EN --> A UC Berkeley team applies Grounded Theory to 150+ multi-agent-system (MAS) execution traces to derive **MAST**, the first empirical MAS failure taxonomy (14 failure modes in 3 categories: system design issues / inter-agent misalignment / task verification) with human agreement κ = 0.88, then scales it with a calibrated LLM annotator (o1, κ = 0.77) into **MAST-Data**, 1,642 annotated traces across 7 MAS frameworks.

## 研究问题 / Problem
<!-- ZH --> 尽管多智能体系统热度很高,它们在主流基准上相对单 agent 或 best-of-N 采样的提升往往很小;作者测得 7 个开源 SOTA MAS 的失败率为 41%–86.7%。领域对「MAS 为什么失败」缺少系统、细粒度、跨系统的理解,也缺少标准化的失败定义,导致根因难以定位、跨系统难以比较。
<!-- EN --> Despite enthusiasm, MAS often improve little over single agents or best-of-N sampling on popular benchmarks; the authors measure failure rates of 41%–86.7% across 7 open-source SOTA MAS. The field lacks a systematic, fine-grained, cross-system understanding of why MAS fail and standardized failure definitions, making root causes hard to pin down and systems hard to compare.

## 方法 / Method
<!-- ZH --> **(1) Grounded Theory 归纳**:从 5 个 MAS 框架(HyperAgent、AppWorld、AG2、ChatDev、MetaGPT)和两类任务(编程、数学)理论抽样 150 条轨迹(每条平均超过 15,000 行),6 名专家用开放编码、持续比较、备忘录与理论化迭代,直到理论饱和;每位专家标注超过 20 小时。**(2) 标注一致性迭代**:3 名标注员每轮独立标注 5 条随机轨迹,讨论分歧并调整定义(增、删、合并模式),共三轮(仅解决分歧就约 10 小时),最终 Cohen's κ = 0.88。**(3) LLM 标注器**:o1 + MAST 定义 + 人工标注的 few-shot 示例;在留出集上准确率 94%、κ = 0.77。**(4) 泛化验证**:在两个新 MAS(OpenManus、Magentic-One)和两个新基准(MMLU、GAIA)上再做一轮人工 IAA,κ = 0.79,无需修改分类。**MAST 结构**(按执行阶段映射):**FC1 系统设计问题** —— 违反任务规格、违反角色规格、步骤重复、丢失对话历史、不知道终止条件;**FC2 智能体间失配** —— 对话重置、不请求澄清、任务偏离、信息隐瞒、忽略其他 agent 输入、推理–行动不一致;**FC3 任务验证** —— 过早终止、无验证或验证不完整、验证错误。
<!-- EN --> **(1) Grounded Theory induction**: theoretically sample 150 traces (each averaging >15,000 lines) from 5 MAS frameworks (HyperAgent, AppWorld, AG2, ChatDev, MetaGPT) and two task types (programming, math); six experts apply open coding, constant comparison, memoing and theorizing until theoretical saturation, >20 hours of annotation each. **(2) Agreement iteration**: three annotators independently label 5 random traces per round, discuss disagreements and refine definitions (add, remove, merge modes), three rounds (~10 hours just resolving disagreements), reaching Cohen's κ = 0.88. **(3) LLM annotator**: o1 with MAST definitions and few-shot human-annotated examples; on held-out data, 94% accuracy and κ = 0.77. **(4) Generalization**: a further human IAA round on two new MAS (OpenManus, Magentic-One) and two new benchmarks (MMLU, GAIA) gives κ = 0.79 without changing the taxonomy. **MAST structure** (mapped to execution stages): **FC1 system design issues** — disobey task specification, disobey role specification, step repetition, loss of conversation history, unaware of termination conditions; **FC2 inter-agent misalignment** — conversation reset, fail to ask for clarification, task derailment, information withholding, ignored other agent's input, reasoning–action mismatch; **FC3 task verification** — premature termination, no or incomplete verification, incorrect verification.

## 数据 / Data
<!-- ZH --> MAST-Data:1,642 条标注轨迹,7 个 MAS 框架(ChatDev、MetaGPT、HyperAgent、AppWorld、AG2/MathChat、Magentic-One、OpenManus),模型含 GPT-4 系列、Claude 3.7 Sonnet、Qwen2.5-Coder-32B、CodeLlama-7B;任务含 ProgramDev(v1/v2)、SWE-bench Lite、AppWorld Test-C、GSM-Plus、OlympiadBench、MMLU、GAIA。另发布 MAST-Data-human(21 条轨迹,每条三名专家标注)。
<!-- EN --> MAST-Data: 1,642 annotated traces across 7 MAS frameworks (ChatDev, MetaGPT, HyperAgent, AppWorld, AG2/MathChat, Magentic-One, OpenManus), with GPT-4-family, Claude 3.7 Sonnet, Qwen2.5-Coder-32B and CodeLlama-7B models, on ProgramDev (v1/v2), SWE-bench Lite, AppWorld Test-C, GSM-Plus, OlympiadBench, MMLU and GAIA. Also released: MAST-Data-human (21 traces, each annotated by three experts).

## 主要结果 / Key results
<!-- ZH --> **失败分布**(图 1,基于 1,642 条轨迹):系统设计问题 44.2%、智能体间失配 32.3%、任务验证 23.5%;单项最常见的是步骤重复(15.7%)、推理–行动不一致(13.2%)、不知道终止条件(12.4%)、违反任务规格(11.8%)、验证错误(9.1%)、验证不完整(8.2%)。(注:论文图 2 与图 4 基于不同子集,百分比不同,例如图 4 的 210 条轨迹中为 41.8% / 36.9% / 21.3%。)**系统差异**:AppWorld 常过早终止,OpenManus 倾向步骤重复,HyperAgent 主要是步骤重复与验证错误 —— 没有「通用解」。同框架换模型:MetaGPT 上 GPT-4o 比 Claude 3.7 Sonnet 的 FC1 失败少 39%;同基准换框架:MetaGPT 的 FC1、FC2 失败比 ChatDev 少 60–68%,但 FC3 多 1.56 倍。**干预**:仅改进 ChatDev 的角色规格(CEO 拥有最终决定权)使成功率 +9.4%;加入高层任务目标验证步骤使 ProgramDev 成功率 +15.6%;但单点修补无法消除全部失败,完成率仍低。**核心洞见**:(1) MAS 失败不只是底座模型问题,同一模型下更好的设计就有提升;(2) FC2 需要更深的「社会推理/心智理论」,仅靠 MCP、A2A 等通信协议标准化不够;(3) 需要**多层验证** —— 现有 verifier 多只做「能否编译」「有无 TODO」等表层检查。
<!-- EN --> **Failure distribution** (Figure 1, over 1,642 traces): system design issues 44.2%, inter-agent misalignment 32.3%, task verification 23.5%; the most frequent modes are step repetition (15.7%), reasoning–action mismatch (13.2%), unaware of termination conditions (12.4%), disobey task specification (11.8%), incorrect verification (9.1%) and incomplete verification (8.2%). (Figures 2 and 4 use different subsets and report different percentages — e.g. 41.8% / 36.9% / 21.3% for the 210 traces in Figure 4.) **System differences**: AppWorld often terminates prematurely, OpenManus tends to repeat steps, HyperAgent is dominated by step repetition and incorrect verification — no one-size-fits-all fix. Swapping models within MetaGPT, GPT-4o shows 39% fewer FC1 failures than Claude 3.7 Sonnet; swapping frameworks on ProgramDev, MetaGPT has 60–68% fewer FC1/FC2 failures than ChatDev but 1.56× more FC3. **Interventions**: improving ChatDev's role specification alone (CEO has the final say) gives +9.4% success; adding a high-level objective-verification step gives +15.6% on ProgramDev; but point fixes do not remove all failures and completion stays low. **Insights**: (1) MAS failure is not just a base-model problem — better design helps with the same model; (2) FC2 needs deeper "social reasoning / theory of mind", which protocol standardization (MCP, A2A) alone does not provide; (3) **multi-level verification** is needed — current verifiers mostly do superficial checks like "does it compile" or "any TODOs left".

## 创新点 / Contributions
- <!-- ZH --> 第一个经验性、经过严格人工一致性验证的 MAS 失败分类(14 模式 / 3 类 / 按执行阶段映射)。 <!-- EN --> The first empirical MAS failure taxonomy with rigorous human-agreement validation (14 modes / 3 categories / mapped to execution stages).
- <!-- ZH --> 一套可复制的方法:Grounded Theory → 多轮 IAA → 校准 LLM 标注器 → 跨系统泛化检验。 <!-- EN --> A replicable method: Grounded Theory → iterative IAA → calibrated LLM annotator → cross-system generalization check.
- <!-- ZH --> 大规模公开数据集 MAST-Data 与 pip 可装的标注工具(`agentdash`)。 <!-- EN --> A large public dataset (MAST-Data) and a pip-installable annotator (`agentdash`).

## 局限 / Limitations
- <!-- ZH --> 作者明说不保证穷尽所有失败模式;分类偏重推理与协调,缺少 API/资源/编排等执行层错误(TRAIL 的批评)。 <!-- EN --> The authors do not claim exhaustiveness; the taxonomy emphasizes reasoning and coordination and lacks execution-layer errors like API / resource / orchestration (TRAIL's critique).
- <!-- ZH --> 大部分标签来自 LLM 标注器(κ = 0.77,并非完美),标签噪声会影响分布结论;失败「主因」难以唯一确定。 <!-- EN --> Most labels come from the LLM annotator (κ = 0.77, not perfect), so label noise affects distributional conclusions; a unique root cause is often hard to assign.
- <!-- ZH --> 任务以编程、数学、通用助手为主,没有科学数据分析;不同图中百分比基于不同子集,引用时需注明。 <!-- EN --> Tasks are mainly programming, math and general assistance, with no scientific data analysis; percentages differ across figures because they use different subsets, so cite with care.
- <!-- ZH --> 干预研究规模小,只证明「设计改动有用」,未给出系统化的修复方法。 <!-- EN --> Intervention studies are small; they show design changes help but offer no systematic repair method.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 对 **Agent 可信度课题的「组学专属失败分类」** 而言,MAST 最有价值的不是那 14 个模式,而是**造分类的方法学**:理论抽样 → 开放编码到饱和 → 3 名标注员多轮 IAA 直到 κ 足够高 → 用人工标注校准 LLM 标注器 → 在没见过的系统/任务上再测一次 κ。Agent 可信度课题可以原样照做:从 Biomni、CellVoyager、SpatialAgent 等组学 agent 在 KPMP / Lake 数据上的轨迹做理论抽样,由懂肾脏组学的标注员做开放编码,产出组学失败分类,再用 MAST 式 κ 报告其可靠性 —— 这样「失败分类」本身就是一个可发表、可复用的贡献。内容层面也直接相关:(1) **FC3 任务验证(23.5%)正是 claim-to-evidence verifier 要补的位置** —— MAST 发现现有 verifier 只做表层检查,加一个高层目标验证步骤就 +15.6%,这为「独立 verifier 有用」提供了直接证据;(2) 「推理–行动不一致」(13.2%)对应组学 agent 说做了 batch correction 实际没做、说用了 Wilcoxon 实际用了 t-test 这类问题,只能靠对照轨迹与代码检查;(3) 「不请求澄清、带着错误假设继续」对应组学中样本元数据(疾病分期、eGFR、活检类型)含糊时的默认假设。对伪影注入课题关系较远;但 Grounded Theory + IAA 的流程同样适合给 KidneyAnomalyBench 的「异常类型」(技术 artifact vs 疾病 vs 正常变异)建立专家一致的类别定义。
<!-- EN --> For **the agent-trustworthiness topic's omics-specific failure taxonomy**, MAST's main value is less its 14 modes than its **methodology for building a taxonomy**: theoretical sampling → open coding to saturation → three annotators iterating IAA until κ is high → calibrate an LLM annotator on human labels → re-measure κ on unseen systems/tasks. The agent-trustworthiness topic can follow this verbatim: theoretically sample traces from omics agents (Biomni, CellVoyager, SpatialAgent, etc.) on KPMP / Lake data, have kidney-omics-literate annotators do open coding, produce an omics failure taxonomy and report its reliability with MAST-style κ — making the taxonomy itself a publishable, reusable contribution. The content is also directly relevant: (1) **FC3 task verification (23.5%) is exactly where a claim-to-evidence verifier fits** — MAST finds current verifiers do only superficial checks and that adding a high-level objective-verification step gives +15.6%, direct evidence that an independent verifier helps; (2) reasoning–action mismatch (13.2%) corresponds to omics agents claiming batch correction was done when it wasn't, or Wilcoxon when a t-test ran — detectable only by checking trace against code; (3) "proceed with wrong assumptions instead of asking" maps to default assumptions when sample metadata (disease stage, eGFR, biopsy type) are ambiguous. Relation to the artifact-injection topic is looser, but the Grounded Theory + IAA workflow also suits building expert-agreed category definitions for KidneyAnomalyBench anomaly types (technical artifact vs disease vs normal variation).

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码:** MAST 分类与 LLM 标注器(`pip install agentdash`)。 <!-- EN --> **Code:** MAST taxonomy and LLM annotator (`pip install agentdash`).
<!-- ZH/EN --> <https://github.com/multi-agent-systems-failure-taxonomy/MAST>
- <!-- ZH --> **数据:** MAST-Data(1,642 条)与 MAST-Data-human。 <!-- EN --> **Data:** MAST-Data (1,642 traces) and MAST-Data-human.
<!-- ZH/EN --> <https://huggingface.co/datasets/mcemri/MAST-Data>
- <!-- ZH --> **方法模板:** 第 3.1–3.4 节的 GT → IAA → LLM 标注器校准 → 泛化检验流程,可直接作为组学失败分类的研究设计。 <!-- EN --> **Method template:** the GT → IAA → annotator calibration → generalization pipeline of §3.1–3.4, directly usable as the study design for an omics failure taxonomy.

## 待读 / Follow-ups
- <!-- ZH --> 附录 A(14 个失败模式的完整定义)与附录 H(干预案例研究)。 <!-- EN --> Appendix A (full definitions of the 14 modes) and Appendix H (intervention case studies).
- <!-- ZH --> Who&When 数据集(Zhang et al.):把失败归因到具体 agent 与步骤。 <!-- EN --> The Who&When dataset (Zhang et al.): attributing failures to specific agents and steps.
- <!-- ZH --> 与 TRAIL 的分类做逐项映射,合并成组学失败分类的上层结构。 <!-- EN --> Map item-by-item against TRAIL's taxonomy and merge into the upper levels of an omics failure taxonomy.

## 引用 / Cite
```bibtex
@inproceedings{Cemri2025_250313657,
  title = {Why Do Multi-Agent LLM Systems Fail?},
  author = {Mert Cemri and Melissa Z. Pan and Shuyi Yang and Lakshya A. Agrawal and Bhavya Chopra and Rishabh Tiwari and Kurt Keutzer and Aditya Parameswaran and Dan Klein and Kannan Ramchandran and Matei Zaharia and Joseph E. Gonzalez and Ion Stoica},
  booktitle = {NeurIPS 2025 Datasets and Benchmarks Track},
  year = {2025},
  eprint = {2503.13657},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2503.13657}
}
```

# MedAgentBench: A Virtual EHR Environment to Benchmark Medical LLM Agents

> **Bibkey** `Jiang_2025` · **Venue** NEJM AI (2025) · **Category** agents · **Relevance** medium · **Access** paywall
> **Link** <https://doi.org/10.1056/AIdbp2500144>
> `status: complete` — NEJM AI 正式版(2025-08-28,vol. 2 no. 9)页面对脚本访问返回 403,未读到;本笔记基于**公开预印本** arXiv 2501.14654v2(2025-02-12,标题为 "MedAgentBench: A Realistic Virtual EHR Environment to Benchmark Medical LLM Agents")全文。正式版的模型列表与数字可能有更新,引用具体数字前请对照正式版。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> MedAgentBench(Stanford,Andrew Ng / Jonathan Chen 组)是第一个要求 LLM agent **在 FHIR 兼容的虚拟 EHR 里自主读写病历**的基准:300 个由内科医生编写、可验证的临床任务(10 类),100 名基于 Stanford STARR 去标识真实病例的患者档案(约 78.5 万条记录);预印本中最佳模型 Claude 3.5 Sonnet v2 总成功率 **69.67%**,写操作(action)普遍比查询(query)更难。
<!-- EN --> MedAgentBench (Stanford; Andrew Ng / Jonathan Chen groups) is the first benchmark requiring an LLM agent to **autonomously read and write records in a FHIR-compliant virtual EHR**: 300 verifiable clinical tasks (10 categories) written by internal-medicine physicians, over 100 patient profiles derived from de-identified real Stanford STARR cases (~785k records). In the preprint the best model, Claude 3.5 Sonnet v2, reaches **69.67%** overall success; write (action) tasks are generally harder than read (query) tasks.

## 研究问题 / Problem
<!-- ZH --> 医学 QA 基准(MedQA、MedMCQA)已饱和,且考试式评估过度简化真实临床交互;通用 agent 基准(AgentBench、BFCL、tau-bench)不覆盖医疗特有的编码体系(LOINC、SNOMED、NDC、ICD-10)、缩写和纵向病历。医生约只有 27% 时间用于直接诊疗,其余被文书与行政占据,agent 有潜力减负,但缺少在交互式病历环境中测量 agent 能力的标准化基准。
<!-- EN --> Medical QA benchmarks (MedQA, MedMCQA) are saturated, and exam-style evaluation oversimplifies real clinical interaction; general agent benchmarks (AgentBench, BFCL, tau-bench) do not cover healthcare-specific coding systems (LOINC, SNOMED, NDC, ICD-10), abbreviations and longitudinal records. Physicians spend only ~27% of their time on direct care, the rest on documentation and administration, so agents could help — but there is no standardized benchmark of agent ability in an interactive medical-record environment.

## 方法 / Method
<!-- ZH --> **任务**:两位内科医生编写 300 个住院/门诊常见、适合电脑自动化的任务,分 10 个具体类别(归为 7 大类):患者信息检索、化验结果检索、患者数据聚合(如 24 小时平均血糖)、记录数据(如录入血压)、检验开单(如 HbA1C 超过 1 年则重开)、转诊开单、用药开单(如按血钾阈值补钾剂量)等。每个任务由用户「instruction」(临床医生写)+ 医院系统「context」(由 EHR 管理员维护的本院编码,如 LOINC 4548-4、NDC)组成。**患者档案**:从 STARR 去标识数据仓库中随机抽取 100 名在 2023-11-13 早晨有住院血钠检验的患者(血钠作锚点),提取近五年化验、六类生命体征、操作(CPT)、诊断(ICD-10)、医嘱(去 PRN);时间戳按患者抖动;MRN 用「S + 7 位随机数」,姓名电话地址用 Faker 生成。**环境**:基于开源 HAPI FHIR JPA 搭建 FHIR 服务器并打包 Docker 镜像,任何 agent 通过 HTTP 读写。**评测**:基于 AgentBench 框架;简单 orchestrator(仿 BFCL)暴露 9 个 FHIR 函数(condition/lab/vital/medicationrequest/procedure/patient 的 search 与 create);每轮在 GET、POST、finish 三者中选一,**最多 8 轮**;为避免每题重启环境(约 90 秒),POST 只做 JSON 可解析检查并返回成功,真正正确性由人工编写的规则检查器校验 payload。主指标为任务成功率,**只用 pass@1**(医疗场景单次出错即有后果)。温度 0(o3-mini 除外)。
<!-- EN --> **Tasks**: two internal-medicine physicians wrote 300 common inpatient/outpatient tasks suited to computer automation, in 10 specific categories (7 broad groups): patient-information retrieval, lab-result retrieval, data aggregation (e.g. 24-h mean glucose), recording data (e.g. charting a BP), test ordering (e.g. reorder HbA1C if > 1 year old), referral ordering, medication ordering (e.g. potassium repletion by threshold-based dosing), etc. Each task combines a clinician-written "instruction" with hospital-system "context" (site-specific codes maintained by EHR admins, e.g. LOINC 4548-4, an NDC). **Patient profiles**: 100 patients randomly sampled from the de-identified STARR warehouse who had an inpatient sodium test on the morning of 2023-11-13 (sodium as anchor); five years of labs, six vital-sign types, procedures (CPT), diagnoses (ICD-10) and medication orders (PRN removed); patient-level timestamp jitter; MRNs as "S + 7 random digits", names/phones/addresses from Faker. **Environment**: a FHIR server on open-source HAPI FHIR JPA, packaged as a Docker image; any agent interacts via HTTP. **Evaluation**: built on AgentBench; a simple BFCL-inspired orchestrator exposes 9 FHIR functions (search/create on condition, lab, vital, medicationrequest, procedure, patient); each round chooses GET, POST or finish, **max 8 rounds**; to avoid restarting the environment per task (~90 s), POSTs are only checked for JSON-loadability and acknowledged, and correctness is verified by hand-written rule-based checks on the payload. Main metric: task success rate, **pass@1 only** (one wrong action matters clinically). Temperature 0 (except o3-mini).

## 数据 / Data
<!-- ZH --> 100 名患者:平均年龄 58.15 ± 19.82 岁,女性 47%;总记录 785,207 条(Observation 563,426、Procedure 124,969、Condition 74,821、MedicationRequest 21,991)。300 个任务中一半(150)只需 GET 查询,另一半需要 POST 修改病历(常先 GET)。环境 Docker 镜像与代码公开。
<!-- EN --> 100 patients: mean age 58.15 ± 19.82, 47% female; 785,207 records (Observation 563,426, Procedure 124,969, Condition 74,821, MedicationRequest 21,991). Half the 300 tasks (150) need only GET queries; the other half require POST modifications (usually after GETs). The environment Docker image and code are public.

## 主要结果 / Key results
<!-- ZH --> 预印本 Table 3(12 个模型):**Claude 3.5 Sonnet v2 总 SR 69.67%**(query 85.33%、action 54.00%);GPT-4o 64.00%(72.00% / 56.00%);DeepSeek-V3 62.67%;Gemini 1.5 Pro 62.00%(query 52.67%、action 71.33%,是少数 action 强于 query 的模型);GPT-4o-mini 56.33%;o3-mini 51.67%;Qwen2.5-72B 51.33%(action 64.00% > query);Llama 3.3-70B 46.33%;Gemini 2.0 Flash 38.33%;Gemma2-27B 19.33%;Gemini 2.0 Pro 18.00%;Mistral v0.3-7B 4.00%。闭源与开源权重模型之间仍有差距。**常见错误**:不严格遵循输出格式(Gemini 2.0 Flash 54% 的情况输出无效动作,把代码包在 `tool_code`/json 块里);答案给整句而非要求的纯数值(输出 `["value": 5.4]` 而非 `[5.4]`)。
<!-- EN --> Preprint Table 3 (12 models): **Claude 3.5 Sonnet v2 overall SR 69.67%** (query 85.33%, action 54.00%); GPT-4o 64.00% (72.00% / 56.00%); DeepSeek-V3 62.67%; Gemini 1.5 Pro 62.00% (query 52.67%, action 71.33% — one of the few with action > query); GPT-4o-mini 56.33%; o3-mini 51.67%; Qwen2.5-72B 51.33% (action 64.00% > query); Llama 3.3-70B 46.33%; Gemini 2.0 Flash 38.33%; Gemma2-27B 19.33%; Gemini 2.0 Pro 18.00%; Mistral v0.3-7B 4.00%. A closed vs open-weight gap remains. **Common errors**: not following the output format exactly (Gemini 2.0 Flash emits invalid actions in 54% of cases, wrapping code in `tool_code`/json blocks); answering in full sentences instead of the required bare value (`["value": 5.4]` instead of `[5.4]`).

## 创新点 / Contributions
- <!-- ZH --> 第一个要求 agent 与病历环境**自主交互(含写操作)**的医疗基准。 <!-- EN --> The first medical benchmark requiring agents to **autonomously interact with (including write to)** a medical-record environment.
- <!-- ZH --> 用标准 FHIR API 搭环境,任务理论上可迁移到真实 EMR(作者强调该环境无安全与审计,不可直接用于生产)。 <!-- EN --> Built on standard FHIR APIs, so tasks can in principle migrate to live EMRs (the authors stress the environment has no security or enterprise logging and is not for production).
- <!-- ZH --> 真实(去标识+抖动)患者档案 + 医生编写任务 + 规则化可验证评分器。 <!-- EN --> Real (de-identified, jittered) patient profiles + physician-written tasks + rule-based verifiable graders.
- <!-- ZH --> 区分 query SR 与 action SR,并坚持 pass@1。 <!-- EN --> Separates query SR from action SR and insists on pass@1.

## 局限 / Limitations
- <!-- ZH --> 任务短(≤ 8 轮)、多为单患者原子操作,不覆盖多团队协作、长程临床推理。 <!-- EN --> Short tasks (≤ 8 rounds), mostly atomic single-patient operations; no multi-team coordination or long-horizon clinical reasoning.
- <!-- ZH --> 患者全部来自 Stanford,人群代表性有限;只覆盖病历场景,不含外科、护理等。 <!-- EN --> All patients from Stanford, limiting representativeness; record-centric only, no surgery or nursing.
- <!-- ZH --> POST 不真正写入环境(只返回成功),agent 看不到写操作的后果,无法测试写后读一致性。 <!-- EN --> POSTs are not actually applied (just acknowledged), so agents never see consequences of writes and write-then-read consistency is untested.
- <!-- ZH --> 只用一个简单 orchestrator 作为基线;**未测重复运行的一致性** —— 作者把 action 任务的重复可靠性列为未来工作。 <!-- EN --> Only a simple orchestrator baseline; **rerun consistency is untested** — the authors list reliability under repetition of action tasks as future work.
- <!-- ZH --> 本笔记基于预印本;正式版数字可能不同。 <!-- EN --> This note is based on the preprint; published numbers may differ.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 这是 EHR 线的代表论文。对 **Sinai EHR / 患者轨迹项目**:(1) 它的 FHIR 环境 + 患者抽样流程(锚定一个常见化验、提取五年纵向数据、时间抖动、合成标识符)是在 Mount Sinai 去标识数据上搭「虚拟 EHR 沙箱」的现成模板;(2) 它的任务几乎都是单时点原子操作,**没有患者轨迹层面的推理**(趋势、事件序列、预后),这正是轨迹项目可以补的维度 —— 例如「过去 12 个月 eGFR 斜率是否提示 CKD 进展,若是则开肾内科转诊」这类纵向任务。对 **心-代谢-肾(cardiometabolic-kidney)方向的 agent / 基础模型**:任务里已有 HbA1C 重开、补钾等代谢/电解质任务,扩展出 eGFR、UACR、血钾-ACEi/ARB 联动这类肾脏相关的 action 任务很自然,且血钾补充本身就是肾功能依赖的高风险医嘱。对 **Agent 可信度课题**:它坚持 pass@1 并自承未测重复可靠性,正好留出 rerun-stability 的空位;它的规则化 payload 校验是「claim/action-to-evidence」验证的结构化版本 —— agent 声称「已按阈值补钾」,检查器核对剂量是否真由化验值推出。
<!-- EN --> This is the representative paper on the EHR line. For the **Sinai EHR / patient-trajectory project**: (1) its FHIR environment plus patient-sampling recipe (anchor on a common lab, extract five years of longitudinal data, jitter time, synthesize identifiers) is a ready template for a "virtual EHR sandbox" on Mount Sinai de-identified data; (2) its tasks are almost all single-timepoint atomic operations with **no trajectory-level reasoning** (trends, event sequences, prognosis) — exactly the dimension the trajectory project can add, e.g. "does the 12-month eGFR slope indicate CKD progression; if so, place a nephrology referral". For **cardiometabolic-kidney agents / foundation models** in general: it already has metabolic/electrolyte tasks (HbA1C reorder, potassium repletion), so extending to kidney-relevant action tasks — eGFR, UACR, potassium vs ACEi/ARB interplay — is natural, and potassium repletion is itself a renal-function-dependent high-risk order. For **the agent-trustworthiness topic**: it insists on pass@1 and admits rerun reliability is untested, leaving a clear slot for rerun stability; its rule-based payload checks are a structured form of claim/action-to-evidence verification — the agent claims "repleted potassium per threshold", and the checker verifies the dose actually follows from the lab value.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码:** MedAgentBench 评测框架(基于 AgentBench)。 <!-- EN --> **Code:** the MedAgentBench evaluation framework (built on AgentBench).
<!-- ZH/EN --> <https://github.com/stanfordmlgroup/MedAgentBench>
- <!-- ZH --> **环境:** FHIR 服务器 Docker 镜像(HAPI FHIR JPA + 100 名患者档案)。 <!-- EN --> **Environment:** FHIR server Docker image (HAPI FHIR JPA + 100 patient profiles).
<!-- ZH/EN --> <https://hub.docker.com/r/jyxsu6/medagentbench>
- <!-- ZH --> **预印本:** arXiv 2501.14654(开放全文)。 <!-- EN --> **Preprint:** arXiv 2501.14654 (open full text).
<!-- ZH/EN --> <https://arxiv.org/abs/2501.14654>

## 待读 / Follow-ups
- <!-- ZH --> 取得 NEJM AI 正式版,核对模型列表与成功率是否更新。 <!-- EN --> Obtain the NEJM AI version and check whether models and success rates were updated.
- <!-- ZH --> AgentClinic、CRAFT-MD、tau-bench 作为临床/工具交互 agent 评测的对照。 <!-- EN --> AgentClinic, CRAFT-MD and tau-bench as comparators for clinical / tool-interaction agent evaluation.
- <!-- ZH --> 后续工作是否加入 action 任务的重复运行可靠性,以及纵向(轨迹级)任务。 <!-- EN --> Whether follow-ups add rerun reliability for action tasks and longitudinal (trajectory-level) tasks.

## 引用 / Cite
```bibtex
@article{Jiang_2025, title={MedAgentBench: A Virtual EHR Environment to Benchmark Medical LLM Agents}, volume={2}, ISSN={2836-9386}, url={http://dx.doi.org/10.1056/AIdbp2500144}, DOI={10.1056/aidbp2500144}, number={9}, journal={NEJM AI}, publisher={Massachusetts Medical Society}, author={Jiang, Yixing and Black, Kameron C. and Geng, Gloria and Park, Danny and Zou, James and Ng, Andrew Y. and Chen, Jonathan H.}, year={2025}, month=Aug }
```

# Same Patient, Different Order: Action-Level Reliability of Clinical LLM Agents Under Repeated Runs

> **Bibkey** `clinical-agent-reruns-arxiv-2026` · **Venue** arXiv preprint (2026) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2609.13582>
> `status: complete` — 全文精读(arXiv HTML 正文 + 附录)。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> 作者提出「same-input rerun」协议:在 MedAgentBench 上把同一任务、同一患者、全部输入固定重跑 5 次,比较的不是分数而是 agent 实际下达的**医嘱**(FHIR 写请求)—— 结果显示动作层面的分歧普遍存在且常常不被 benchmark 的判分记录:Llama-3.1-8B 在 0.7 温度下 43/43 个下单任务组每次下达的医嘱集合都不同,其中 22 组的 benchmark 判定却完全相同。
<!-- EN --> The authors propose a "same-input rerun" protocol: replay each MedAgentBench task five times with patient and all inputs fixed, and compare not the score but the **orders** (FHIR write requests) the agent actually issues. Action-level divergence is pervasive and often invisible to the benchmark's verdict: for Llama-3.1-8B at temperature 0.7, all 43 ordering groups emit a different order set across five identical runs, yet in 22 of them the benchmark reports the same verdict.

## 研究问题 / Problem
<!-- ZH --> 临床 agent 已经在下检验单、开药、转诊,但基准通常每个任务只跑一次、报告准确率,很少问「同样的输入是否产生同样的动作」。准确率记录 agent 是否对,不记录它是否**一致**。难点有三:(i) 判定两个医嘱何时「是同一医嘱」(时间戳、状态字段、参数顺序不同不算变化);(ii) MedAgentBench 不真正执行写请求、只做 JSON 解析就回复「成功」,运行内无法区分会被服务器接受还是拒绝的医嘱;(iii) 在 5 次重跑上测得的比率如何在研究之外仍有意义(重跑次数、分母、非独立性)。
<!-- EN --> Clinical agents now order tests, prescribe and refer, yet benchmarks usually run each task once and report accuracy, rarely asking whether identical inputs produce identical actions. Accuracy records whether the agent was right, not whether it was **consistent**. Three difficulties: (i) deciding when two orders are the same order (timestamps, status fields, parameter order vary without the order varying); (ii) MedAgentBench never executes writes — it JSON-parses the payload and replies "success" — so within a run one cannot tell an order the server would create from one it would refuse; (iii) making a rate measured over five reruns meaningful outside the study (budget, denominators, non-independence).

## 方法 / Method
<!-- ZH --> **Same-input rerun**:固定任务、模型和解码配置,把 benchmark 的 agent 循环跑 5 次,在三层比较 —— 动作(医嘱)、轨迹、判定。**六个指标**:(1) **order-set divergence**:以「目标 endpoint + 完整 payload」为规范形式,5 次运行中不同医嘱集合数 >1 即分歧(未下单记为空集);另报告与重跑次数无关的 **pairwise disagreement**(组内运行对中医嘱集合不同的比例);(2) **omission split**:有的运行下了单、有的没下(最「沉默」的失败);(3) **endpoint divergence**:下单运行之间到达的 endpoint 不同;(4) **clinical-content divergence**:比较资源编码、记录值、药物编码、剂量/单位/速率/途径等临床字段(排除时间戳、状态与编码的人类可读 label);(5) **trajectory first-divergence**:首次分歧的轮次;(6) **verdict instability**:benchmark 自身判定在 5 次中是否一致。动作类指标只在「至少一次下过单」的 ordering groups 上计算。统计:Wilson 95% 区间;同模型两温度间做 exact paired McNemar(Holm 校正);按任务家族做 cluster bootstrap。**对照**:噪声底线(18 个 cell × 20 次相同调用);以及把 endpoint 分歧拿到 benchmark 自带的 HAPI FHIR 服务器上实测。
<!-- EN --> **Same-input rerun**: for a fixed task, model and decoding configuration, run the benchmark's agent loop five times and compare at three layers — action (orders), trajectory, verdict. **Six metrics**: (1) **order-set divergence**: canonical form = destination endpoint + whole payload; a group diverges if its five runs yield >1 distinct order set (no order = empty set); also reported as budget-independent **pairwise disagreement** (share of run pairs whose order sets differ); (2) **omission split**: some runs order, some do not (the most silent failure); (3) **endpoint divergence**: ordering runs reach different endpoints; (4) **clinical-content divergence**: compares clinical fields — resource code and text, recorded value, medication code and text, dose value/unit/rate/route (excluding timestamps, status and the human-readable code label); (5) **trajectory first-divergence**: the first turn where runs differ; (6) **verdict instability**: whether the benchmark's own pass/fail changes across the five runs. Action metrics are computed over ordering groups (groups that order at least once). Statistics: Wilson 95% intervals; exact paired McNemar between temperatures (Holm-corrected); family-level cluster bootstrap. **Controls**: a noise floor (20 identical calls × 18 cells), and testing endpoint divergence against the benchmark's own HAPI FHIR server.

## 数据 / Data
<!-- ZH --> MedAgentBench(300 个临床任务、10 个家族、FHIR 服务器约 100 名去标识化患者);选用 5 个可写家族(记录观测、下服务申请、三个依赖化验值或其时效的条件家族),每家族按 benchmark 自身 ID 顺序取前 10 个任务,共 50 个任务组。两个本地部署、4-bit 量化的开源模型 Qwen3-4B 与 Llama-3.1-8B;温度 0.05(近贪心)与 0.7(nucleus);每任务 5 次 → 每臂 250 次、共 1,000 次运行(加上 8-bit Qwen 重跑共 1,250 条记录)。轮数上限 8,沿用原 scaffold。
<!-- EN --> MedAgentBench (300 clinical tasks, 10 families, a FHIR server with ~100 de-identified patients); the five write-capable families (record an observation, place a service request, three families conditional on a lab value or its age), taking the first 10 tasks per family by the benchmark's own ID order — 50 task groups. Two locally served, 4-bit-quantised open-weight models, Qwen3-4B and Llama-3.1-8B; temperatures 0.05 (near-greedy) and 0.7 (nucleus); five runs per task → 250 runs per arm, 1,000 total (1,250 records including an 8-bit Qwen rerun). Round limit 8, original scaffold.

## 主要结果 / Key results
<!-- ZH -->
- **动作分歧在每一臂都存在,且随温度上升**:order-set divergence —— Qwen 0.05: 3/20、Qwen 0.7: 10/20、Llama 0.05: 11/21、Llama 0.7: **43/43**;pairwise 形式 0.08 → 0.29(Qwen)、0.33 → 0.78(Llama)。omission split:0/20、4/20、1/21、26/43。endpoint divergence:3/20、8/20、8/21、12/43。
- **临床内容分歧**:只出现在 Llama 0.7 一臂,但高达 28/43 组 —— 23 组资源编码不同、18 组记录值不同、5 组药物不同、3 组剂量不同(可重叠);这无法用路由或解析错误解释。8-bit Qwen 重跑中也出现内容分歧,使「纯量化所致」的解释变复杂。
- **医嘱变了、判定不变**:Llama 0.7 中 43 个分歧组里有 22 组 benchmark 判定相同(覆盖全部 5 个写家族);Llama 0.05 为 3/11;Qwen 0.7 为 10/10。38 个这样的组里 36 个是 5 次全失败 —— 分数掩盖的不是成功,而是「每次失败方式都不同」。全网格 251 次通过的运行中没有一次发往会被服务器拒绝的 endpoint。
- **Endpoint 不是表面差异**:同一 ServiceRequest payload 发到 `/fhir/ServiceRequest` 返回 201 Created,发到集合根 `/fhir/` 返回 400 Bad Request(HAPI-0450)—— 一个下单成功,一个没下;但 agent 收到的永远是「成功」。
- **机制**:误路由与「payload 解析失败后重试仍重复同一错误构造」导致丢单;Llama 26 个 split 组中 72 次未下单的运行,61 次是 agent 自己宣布完成,7 次为格式错误动作,4 次触达轮数上限。分歧是即时的:中位首次分歧轮次在 4 臂中 3 臂为 0。
- **统计**:McNemar 显示两模型在轨迹、order-set、判定分歧上随温度上升均显著(100 个不一致对中 96 个朝更多分歧方向,Holm 后六项均显著);但按家族聚类后只有 Llama 0.7 一臂的区间站得住。作者明确:研究**证明动作分歧存在且可能不被分数记录,而不声称任何比率可推广**。
- **噪声底线**:单请求串行时贪心解码完全可复现;但在有并发流量的共享服务器上,温度 0 的确定性被打破(12 个贪心 cell 中 4 个返回多于 1 种输出)。
<!-- EN -->
- **Action divergence appears in every arm and rises with temperature**: order-set divergence — Qwen 0.05: 3/20, Qwen 0.7: 10/20, Llama 0.05: 11/21, Llama 0.7: **43/43**; pairwise form 0.08 → 0.29 (Qwen), 0.33 → 0.78 (Llama). Omission split: 0/20, 4/20, 1/21, 26/43. Endpoint divergence: 3/20, 8/20, 8/21, 12/43.
- **Clinical-content divergence**: only in the Llama 0.7 arm, but in 28/43 groups — 23 differ on resource code, 18 on recorded value, 5 on medication, 3 on dose (overlapping); no routing or parsing account explains this. The 8-bit Qwen rerun also shows content divergence, complicating a pure-quantisation explanation.
- **Orders move, verdict holds**: in Llama 0.7, 22 of 43 divergent groups keep the same verdict (spanning all five write families); 3/11 at Llama 0.05; 10/10 at Qwen 0.7. Of 38 such groups, 36 fail on all five runs — the score hides not success but that the agent failed differently each time. None of the 251 passing runs posted to an endpoint the server would refuse.
- **Endpoints are not cosmetic**: the same ServiceRequest payload sent to `/fhir/ServiceRequest` returns 201 Created; sent to the collection root `/fhir/` it returns 400 Bad Request (HAPI-0450) — one places the order, the other does not; yet the agent is always told "success".
- **Mechanisms**: misrouting, and lost orders after a malformed payload whose retry repeats the same construction; of 72 non-emitting runs in Llama's 26 split groups, 61 ended with the agent declaring itself finished, 7 on a malformed action, 4 at the round limit. Divergence is immediate: median first-divergence turn is 0 in three of four arms.
- **Statistics**: McNemar finds the temperature rise significant for both models on trajectory, order-set and verdict divergence (96 of 100 discordant pairs toward more divergence; all six survive Holm), but under family clustering only the Llama 0.7 arm holds. The authors are explicit: the study **establishes that action divergence exists and can pass unrecorded by the score, not that any rate generalises**.
- **Noise floor**: serial greedy decoding is exactly reproducible; on a shared server with concurrent traffic, temperature-0 determinism breaks (4 of 12 greedy cells return more than one completion).

## 创新点 / Contributions
- <!-- ZH --> **把评测单元从「一次尝试」改为「一组相同输入的重跑」**,并以 ordering groups 作为动作类比率的分母。 <!-- EN --> **Changes the evaluation unit from one attempt to a group of identical reruns**, with ordering groups as the denominator for action-level rates.
- <!-- ZH --> **判定之下的测量层**:六个可从既有 transcript 计算的指标,并给出与重跑预算无关的 pairwise 形式。 <!-- EN --> **A measurement layer beneath the verdict**: six metrics computable from transcripts benchmarks already keep, with a budget-independent pairwise form.
- <!-- ZH --> **走出 benchmark 回到真实服务器**:证明 endpoint 分歧决定医嘱是否真的被创建,揭示「环境反馈不忠实」问题。 <!-- EN --> **Leaves the benchmark loop to test against the real server**, showing endpoint divergence decides whether an order is created and exposing unfaithful environment feedback.
- <!-- ZH --> 三条可独立采纳的基准设计建议:R1 重跑并声明;R2 报告动作级稳定性;R3 让环境像真实系统一样回应。 <!-- EN --> Three independently adoptable design recommendations: R1 rerun and say so; R2 report an action-level stability measure; R3 make the environment answer as the real system would.

## 局限 / Limitations
- <!-- ZH --> 只测「发出的」医嘱而非「被执行的」医嘱;不声称临床 agent 不安全。 <!-- EN --> Measures orders emitted, not received; makes no claim that clinical agents are unsafe to deploy.
- <!-- ZH --> 模型面板很小:两个 <10B、4-bit 量化开源模型,一个 benchmark、一个推理栈;非前沿模型,失败多为「失败得不一致」,未证明「成功得不一致」。 <!-- EN --> Tiny panel: two <10B 4-bit open models, one benchmark, one serving stack; not frontier; shows inconsistent failure, not inconsistent success.
- <!-- ZH --> 使用 MedAgentBench 原始 scaffold(第二版已移除手写 HTTP 请求这一主要失败来源);任务取前缀而非随机样本。 <!-- EN --> Uses MedAgentBench's original scaffold (v2 removes hand-built HTTP requests, the mechanism behind many failures); tasks are a prefix, not a random sample.
- <!-- ZH --> 任务组按家族聚类,聚类后显著性大多消失;协议可迁移,比率不可迁移。 <!-- EN --> Task groups cluster by family and most significance vanishes under clustering; the protocol transfers, the rates do not.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 这篇几乎就是 **课题 2 中「rerun stability」一项的现成方法学**,只是领域从肾脏组学换成了 EHR 写操作。可直接借用:**(1) 协议**:同输入重跑 N 次、以任务组为单位、比较「动作」而非分数。对分析肾脏组学的 agent,「动作」可以定义为它选择的分析步骤与参数(QC 阈值、归一化方法、聚类分辨率、差异表达检验)、它最终提名的基因/细胞状态、它下的结论;**(2) 指标模板**:order-set divergence ↔ 结论集合分歧;omission split ↔ 某次重跑漏掉某个关键发现;endpoint divergence ↔ 走了不同的分析分支;clinical-content divergence ↔ 同一结论里具体基因/效应值不同;pairwise 形式便于跨研究比较;**(3) 「判定不变、行为在变」** 的发现直接支持课题 2 的论点:只报告 benchmark 准确率会掩盖不稳定性;**(4) R3「环境要如实反馈」** 对应课题 2 的另一个关注 —— agent 工具调用返回的「成功」是否真实(组学工具静默失败)。另外,对 **Sinai EHR / 患者轨迹项目** 和心-代谢-肾方向的 agent,它提供了在 FHIR 环境下评估临床写操作稳定性的直接参照,以及「本地部署小模型 + 量化」这一隐私场景下的风险证据。与 AIRIS WP3 / MLCommons 式的基准规范工作高度相关(报告标准、重跑次数、分母定义)。
<!-- EN --> Essentially a ready-made methodology for **Topic 2's "rerun stability" component**, with the domain switched from kidney omics to EHR write actions. Directly reusable: **(1) Protocol**: rerun identical inputs N times, treat the task group as the unit, compare actions not scores. For a kidney-omics agent, "actions" can be its chosen analysis steps and parameters (QC thresholds, normalisation, clustering resolution, DE test), the genes/cell states it nominates, and its conclusions; **(2) Metric templates**: order-set divergence ↔ divergence in the conclusion set; omission split ↔ a rerun silently missing a key finding; endpoint divergence ↔ taking a different analysis branch; clinical-content divergence ↔ same conclusion but different genes/effect sizes; the pairwise form keeps studies comparable; **(3) "verdict holds while behaviour moves"** directly supports Topic 2's argument that benchmark accuracy alone hides instability; **(4) R3 "faithful environment feedback"** maps to another Topic 2 concern — whether a tool call's "success" is real (silent failures in omics tools). For the **Sinai EHR / patient-trajectory project** and cardiometabolic-kidney agents in general, it is a direct reference for evaluating clinical write-action stability in FHIR environments, and evidence on the risks of locally deployed, quantised small models in privacy-constrained settings. Highly relevant to AIRIS WP3 / MLCommons-style benchmark specification work (reporting standards, rerun counts, denominator definitions).

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码、rerun harness、分析脚本、环境复现脚本与全部 1,250 条运行记录:** <!-- EN --> **Code, rerun harness, analysis scripts, environment reproduction script and all 1,250 run records:**
<!-- ZH/EN --> <https://github.com/rohithreddybc/clinical-agent-action-reliability>
- <!-- ZH --> **匿名只读镜像:** <!-- EN --> **Anonymised read-only mirror:**
<!-- ZH/EN --> <https://anonymous.4open.science/r/clinical-agent-action-reliability>
- <!-- ZH --> **指标定义**(第 4 节)与统计方案(Wilson 区间、paired McNemar + Holm、family cluster bootstrap)。 <!-- EN --> **Metric definitions** (Section 4) and statistics (Wilson intervals, paired McNemar + Holm, family cluster bootstrap).
- <!-- ZH --> **基准环境:** MedAgentBench(本仓库 `medagentbench-nejmai-2025`)。 <!-- EN --> **Benchmark environment:** MedAgentBench (this repo: `medagentbench-nejmai-2025`).

## 待读 / Follow-ups
- <!-- ZH --> MedAgentBench v2(Chen et al., 2026):新 scaffold 下动作稳定性是否改善。 <!-- EN --> MedAgentBench v2 (Chen et al., 2026) — does action stability improve under the new scaffold?
- <!-- ZH --> Mokssit et al. (2026):在可重置 FHIR 服务器上真正执行写操作的临床沙箱。 <!-- EN --> Mokssit et al. (2026) — a clinical sandbox executing writes against a resettable server.
- <!-- ZH --> τ-bench 的 pass^k 及其临床应用(Liu et al., 2026);Atil et al. (2024)、Yuan et al. (2025) 关于确定性解码下的非确定性。 <!-- EN --> τ-bench's pass^k and its clinical use (Liu et al., 2026); Atil et al. (2024) and Yuan et al. (2025) on nondeterminism under "deterministic" decoding.

## 引用 / Cite
```bibtex
@misc{clinical-agent-reruns-arxiv-2026, title={Same Patient, Different Order: Action-Level Reliability of Clinical LLM Agents Under Repeated Runs}, author={Bellibatlu, Rohith Reddy and Singh, Manpreet and Han, Zhoutian and Zhang, Wenbin}, year={2026}, eprint={2609.13582}, archivePrefix={arXiv}, primaryClass={cs.CL}, url={https://arxiv.org/abs/2609.13582}, doi={10.48550/arXiv.2609.13582} }
```

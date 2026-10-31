# 研究课题 / Research topics

<!-- ZH -->
组里的研究课题都放在这里，每个课题一页，用同一个模板：要回答什么、做出什么、现在到哪一步。目前的课题都用肾脏单细胞组学数据，背景知识在 **[入门](../onboarding/index.md)** 里，每份数据的信息在 **[数据集](../datasets/index.md)** 里。以后有新课题，按同样的模板加一页。
<!-- EN -->
The group's research topics live here, one page each with the same template: what it asks, what it will produce, and where it stands. The current topics all use kidney single-cell omics data; the background is in **[Onboarding](../onboarding/index.md)** and the facts about each dataset in **[Datasets](../datasets/index.md)**. New topics get a page in the same format.

<!-- ZH/EN --> <div class="grid cards" markdown>

<!-- ZH -->
-   __用伪影注入增强肾脏单细胞异常检测__

    ---

    肾脏单细胞数据里，一个看起来异常的细胞，是真的病了，还是测量造成的？我们做一条 pipeline，往任意单细胞数据里注入已知的伪影，用它增强现有模型（包括开源基础模型），再用公开数据里的真实答案检验模型分不分得清两者、误报控不控得住。

    **现状：**2026-10-28 方向调整为 pipeline + 模型；设计细节在讨论中，代码还没开始。

    [:octicons-arrow-right-24: 课题页](anomaly-benchmark.md)

-   __肾脏组学上假设验证 agent 的可信度__

    ---

    让 agent 拿公开的原始肾脏组学数据去证明或推翻一条 CKD 假设时，它什么时候会给出不可信的结论？我们做一个答案靠构造得到的基准（反事实数据、注入伪影、测不了的假设），测假支持、伪影当病、不弃答、编数字、重跑不一致这些安全失败，并请肾内科医生核对。

    **现状：**方向已定，做过文献调研和一个纸面试点，代码还没开始。

    [:octicons-arrow-right-24: 课题页](agent-claims.md)
<!-- EN -->
-   __Artifact Injection to Boost Anomaly Detection in Kidney Single-Cell Omics__

    ---

    In kidney single-cell data, is an abnormal-looking cell diseased, or is its abnormality caused by measurement? We build a pipeline that injects known artifacts into any single-cell dataset, use it to boost current models (open foundation models included), and test on real answers from public data whether they can tell the two apart and keep false alarms under control.

    **Status:** on 2026-10-28 the direction changed to pipeline + models; design details under discussion, code not started.

    [:octicons-arrow-right-24: Topic page](anomaly-benchmark.md)

-   __Trustworthiness of Hypothesis-Testing Agents on Kidney Omics__

    ---

    When an agent uses public raw kidney omics data to prove or refute a CKD hypothesis, when does its verdict become untrustworthy? We build a benchmark whose answers are known by construction (counterfactual data, injected artifacts, untestable hypotheses) and measure safety failures: false support, artifacts taken for disease, missing abstention, untraceable numbers, rerun instability, with nephrologists checking verdicts.

    **Status:** direction decided; literature survey and a desk pilot done; no code yet.

    [:octicons-arrow-right-24: Topic page](agent-claims.md)

<!-- ZH/EN --> </div>

## 课题之间的联系 / How the topics connect

<!-- ZH -->
伪影注入课题要弄清楚"数据里哪些异常是真的"，并让模型学会分辨，Agent 可信度课题要弄清楚"agent 说的哪些话是真的"。两者打算用同一类数据和同一套已知答案：比如 Lake 2023 的细胞状态标签，在伪影注入课题里是"病"的答案，在 Agent 可信度课题里可以用来检查 agent 有没有把伪影说成疾病。知识图谱里的 **[桥](../knowledge-map.md)** 视图列出了不止一个课题要读的论文。
<!-- EN -->
The artifact-injection topic asks which anomalies in the data are real and teaches models to tell; the agent-trustworthiness topic asks which statements an agent makes are true. They are planned to use the same kind of data and the same known answers: Lake 2023's cell-state labels, for example, are the disease ground truth in the artifact-injection topic and can be used in the agent-trustworthiness topic to check whether an agent reports artifacts as disease. The **[Bridge](../knowledge-map.md)** view of the knowledge map lists the papers more than one topic needs.

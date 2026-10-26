# 研究课题 / Research topics

<!-- ZH -->
组里的研究课题都放在这里，每个课题一页，用同一个模板：要回答什么、做出什么、现在到哪一步。目前的课题都用肾脏单细胞组学数据，背景知识在 **[入门](../onboarding/index.md)** 里，每份数据的信息在 **[数据集](../datasets/index.md)** 里。以后有新课题，按同样的模板加一页。
<!-- EN -->
The group's research topics live here, one page each with the same template: what it asks, what it will produce, and where it stands. The current topics all use kidney single-cell omics data; the background is in **[Onboarding](../onboarding/index.md)** and the facts about each dataset in **[Datasets](../datasets/index.md)**. New topics get a page in the same format.

<!-- ZH/EN --> <div class="grid cards" markdown>

<!-- ZH -->
-   __课题 1 · 肾脏单细胞组学异常检测基准__

    ---

    肾脏单细胞数据里，一个看起来异常的细胞，是真的病了，还是测量造成的？我们用公开数据搭一个有已知答案的基准，检验现有方法能不能分清两者、误报能不能控住。

    **现状：**方向和核心问题已定；数据和任务在讨论中。

    [:octicons-arrow-right-24: 课题页](anomaly-benchmark.md)

-   __课题 2 · 生物医学分析 agent 的结论核查__

    ---

    让 AI agent 分析单细胞数据并给出结论时，哪些结论真的有代码、数据或文献支撑？我们要做一套方法和基准，把每条结论追溯到证据，并用专家标注来校准。

    **现状：**方向已定，具体设计还没开始。

    [:octicons-arrow-right-24: 课题页](agent-claims.md)
<!-- EN -->
-   __Topic 1 · A Benchmark for Anomaly Detection in Kidney Single-Cell Omics__

    ---

    In kidney single-cell data, is an abnormal-looking cell diseased, or is its abnormality caused by measurement? We build a benchmark with known answers from public data to test whether current methods can tell the two apart and keep false alarms under control.

    **Status:** direction and core question decided; data and tasks under discussion.

    [:octicons-arrow-right-24: Topic page](anomaly-benchmark.md)

-   __Topic 2 · Verifying the Claims of Biomedical Analysis Agents__

    ---

    When an AI agent analyses single-cell data and reports conclusions, which of them are actually backed by its code, its data or the literature? We want methods and a benchmark that trace each claim to its evidence, calibrated against expert labels.

    **Status:** direction decided; detailed design not started.

    [:octicons-arrow-right-24: Topic page](agent-claims.md)

<!-- ZH/EN --> </div>

## 课题之间的联系 / How the topics connect

<!-- ZH -->
课题 1 要弄清楚"数据里哪些异常是真的"，课题 2 要弄清楚"agent 说的哪些话是真的"。两者共用同一批数据和同一套已知答案：比如 Lake 2023 的细胞状态标签，在课题 1 里是"病"的答案，在课题 2 里可以用来检查 agent 有没有把伪影说成疾病。知识图谱里的 **[桥](../knowledge-map.md)** 视图列出了不止一个课题要读的论文。
<!-- EN -->
Topic 1 asks which anomalies in the data are real; Topic 2 asks which statements an agent makes are true. They share the same data and the same known answers: Lake 2023's cell-state labels, for example, are the disease ground truth in Topic 1 and can be used in Topic 2 to check whether an agent reports artifacts as disease. The **[Bridge](../knowledge-map.md)** view of the knowledge map lists the papers more than one topic needs.

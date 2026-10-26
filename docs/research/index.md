# Research topics

The group's research topics live here, one page each with the same template: what it asks, what it will produce, and where it stands. The current topics all use kidney single-cell omics data; the background is in **[Onboarding](../onboarding/index.md)** and the facts about each dataset in **[Datasets](../datasets/index.md)**. New topics get a page in the same format.

<div class="grid cards" markdown>

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

</div>

## How the topics connect

Topic 1 asks which anomalies in the data are real; Topic 2 asks which statements an agent makes are true. They share the same data and the same known answers: Lake 2023's cell-state labels, for example, are the disease ground truth in Topic 1 and can be used in Topic 2 to check whether an agent reports artifacts as disease. The **[Bridge](../knowledge-map.md)** view of the knowledge map lists the papers more than one topic needs.

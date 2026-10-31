# Research topics

The group's research topics live here, one page each with the same template: what it asks, what it will produce, and where it stands. The current topics all use kidney single-cell omics data; the background is in **[Onboarding](../onboarding/index.md)** and the facts about each dataset in **[Datasets](../datasets/index.md)**. New topics get a page in the same format.

<div class="grid cards" markdown>

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

</div>

## How the topics connect

The artifact-injection topic asks which anomalies in the data are real and teaches models to tell; the agent-trustworthiness topic asks which statements an agent makes are true. They are planned to use the same kind of data and the same known answers: Lake 2023's cell-state labels, for example, are the disease ground truth in the artifact-injection topic and can be used in the agent-trustworthiness topic to check whether an agent reports artifacts as disease. The **[Bridge](../knowledge-map.md)** view of the knowledge map lists the papers more than one topic needs.

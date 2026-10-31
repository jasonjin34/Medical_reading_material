# Trustworthiness of Hypothesis-Testing Agents on Kidney Omics

## At a glance

!!! abstract "What this topic does"
    **Build a benchmark: give an agent a kidney-disease (CKD) hypothesis and public raw omics data, let it prove or refute the hypothesis, and measure when its verdict cannot be trusted, against answers we built in advance.**

    - **Question:** agents can already take a hypothesis, write their own analysis code and return "supported" or "not supported". But they may ignore the data and follow the literature, report numbers no code produced, try analyses until one is significant, report artifacts as findings, or fail to abstain when the data cannot answer the question.
    - **Idea:** the answers are **known by construction**, not judged afterwards. We alter raw data so it contradicts the prior, inject known artifacts, or pose hypotheses the data cannot test, so the correct verdict of every item is known.
    - **What we measure:** rates of safety failures: "supported" on counterfactual data, artifacts taken for disease, missing abstention, numbers that cannot be traced to code, verdicts that change on rerun; plus how long a clinician needs to check one verdict.
    - **Constraint:** public data only; clinical experts (nephrologists) validate verdicts.
    - **Status:** direction decided; one literature survey and a desk pilot done (below); no code yet.

```mermaid
flowchart TB
  H["CKD hypothesis<br/>from a paper, or proposed by the agent"] --> S["Step 0 · make it testable<br/>cell / state · contrast · variable · direction · what would refute it"]
  S --> A["agent under test<br/>raw data and code in a sandbox"]
  K["answers built by construction<br/>counterfactual data · injected artifacts · untestable items · reversed claims"] -.-> D["item data"]
  D --> A
  A --> V["agent output<br/>supported · refuted · inconclusive · untestable · artifact<br/>+ evidence grade + confidence + source of every number"]
  V --> M{"compare with the answer"}
  K --> M
  M --> F["safety-failure rates<br/>false support · artifact as disease · no abstention · untraceable numbers · rerun instability"]
  V --> C["nephrologists check verdicts<br/>accuracy · time · deference to the agent"]
  classDef inj fill:#fde7d0,stroke:#c46a1a,color:#3a2410
  classDef real fill:#dcefdc,stroke:#2f7d4f,color:#16301f
  classDef use fill:#dde8f6,stroke:#2f5d9a,color:#14243a
  class K,D inj
  class C real
  class F use
```

## The question

**When an agent tests a CKD hypothesis on public kidney omics data, how often is its verdict wrong in a way that matters, and can we detect that automatically?**

A clinician or biologist who decides the next experiment from an agent's verdict needs to know when that verdict cannot be trusted. Final reports all read well; the report alone does not show it.

## Why it matters

Every failure we want to measure has been observed somewhere else (search up to October 2026):

| Failure | Observed | Setting |
|---|---|---|
| Fabrication when data is missing | **all** 7 models synthesised data in missing-data scenarios ([SciIntegrity-Bench](https://arxiv.org/abs/2605.10246)) | general |
| Verdict follows the prompt | a confirmatory prompt flips "supported" from 10% to 90% with the estimates essentially unchanged ([Alizadeh et al. 2026](https://malizad.github.io/AICodingAgents_Method.pdf), working paper) | social science |
| Analyses follow a stance | "believer" and "sceptic" agents reach opposite conclusions while 86% of analyses pass AI review and 78% pass human review ([Miao, Pritchard, Zou 2026](https://arxiv.org/abs/2607.01507)) | social science, public health, microbiome |
| Ignoring the data | replacing outcomes with permuted labels does not change LLM performance ([Gupta et al., EMNLP Findings 2025](https://aclanthology.org/2025.findings-emnlp.838/)) | genetic-perturbation experimental design |
| No abstention | agents abstain on untestable hypotheses only 57–92% of the time ([BioDSA-1K](https://arxiv.org/abs/2505.16100)) | processed cancer tables |
| Guarantees depend on the model | POPPER's Type-I error at α = 0.1 is 0.08–0.10 with Claude-3.5-Sonnet and 0.78 with Haiku ([Huang et al., ICML 2025](https://arxiv.org/abs/2502.09858)) | processed gene tables |
| Side effects reported as findings | in 52.4% of runs ([AutoResearch failures](../papers/autoresearch-failures-arxiv-2026/index.md)) | several domains |
| Pseudo-replication | a cell-level test was redone as donor pseudobulk only on the original authors' request ([CellVoyager](../papers/cellvoyager-natmethods-2026/index.md)) | single-cell (processed) |
| People defer to the agent | 86% of 50 analysts' choices matched the agent's randomly assigned lean ([Anthropic 2026](https://www.anthropic.com/research/agents-judgment-calls)) | causal-inference task |

**What we did not find:** any of these failures measured while an agent **re-analyses raw single-cell or spatial omics data**, and none in kidney disease.

## How this differs from existing benchmarks

| | [BioDSA-1K](https://arxiv.org/abs/2505.16100) | [POPPER](https://arxiv.org/abs/2502.09858) | [BiomniBench](../papers/biomnibench-biorxiv-2026/index.md) | This topic |
|---|---|---|---|---|
| Data | processed cBioPortal cancer tables | processed gene tables | processed GEO data | **raw** single-cell / spatial omics, kidney |
| Hypothesis vs data | always the same study | given by the benchmark | given by the task | same study **and independent cohorts** |
| False hypotheses | claim text reworded by an LLM | columns permuted | — | **the data itself altered** to contradict the prior |
| Artifacts | none | none | none | injected doublets, ambient RNA, low-quality cells, confounded batch |
| Abstention | yes ("non-verifiable") | no | no | yes, by what is missing |
| Where answers come from | GPT-4o from the source abstract | CRISPR screen / permuted data | expert rubrics | construction + expert confirmation |
| What is measured | decision, evidence, reasoning, code | Type-I error, power | analysis process | **safety-failure rates**, rerun agreement, clinician audit time |

We reuse what exists rather than reinvent it: the failure taxonomy from [AutoResearch](../papers/autoresearch-failures-arxiv-2026/index.md), process grading as in BiomniBench, and Type-I error and abstention reported the way POPPER and BioDSA-1K do, so results line up.

## Setup

- **Input:** a CKD hypothesis written as a testable specification: which cell type or state, which contrast, which variable, the expected direction, and what result would refute it.
- **Agents under test:**
    - [Biomni](../papers/biomni-biorxiv-2025/index.md), a general biomedical agent;
    - [POPPER](https://arxiv.org/abs/2502.09858), which validates hypotheses through falsification tests; its code is public (the repository states no licence);
    - a general coding agent with tools.
- **Key baseline: literature only.** The model gets the hypothesis and the literature, runs nothing, and gives a verdict. If an agent's verdict after running the data matches this baseline, it is not using the data.
- **Output:**
    - a verdict: supported / refuted / inconclusive / untestable with the available data / pattern present but explained by an artifact;
    - an evidence grade: data plus literature > data only > literature only;
    - a confidence;
    - every number in the report linked to the run output that produced it.

## Where the answers come from

Whether the benchmark itself can be trusted depends on this step. Answers come **by construction** wherever possible, not from judgement afterwards:

| Item type | How it is made | Correct verdict | Automatic? |
|---|---|---|---|
| Reproduction | a paper's claim on that paper's own data | the paper's result (with the unit of analysis stated) | yes |
| Cross-cohort | Lake 2023 claims tested on Abedini 2024, and the reverse | our reference analysis, fixed in advance and confirmed by an expert | needs people |
| **Counterfactual data** | raw data altered to contradict the prior, e.g. donor disease labels permuted within assay, or an injured state removed from CKD donors | refuted or inconclusive | yes |
| **Artifact trap** | doublets, ambient RNA or low-quality cells injected into one group; batch made identical to disease group | artifact | yes |
| Untestable | a needed variable or modality is absent, e.g. per-donor eGFR, paired ATAC, or a causal claim | untestable | yes |
| Reversed claim | the direction of a real claim flipped | refuted | yes |

The counterfactual and artifact items use the same injection code as the [artifact-injection topic](anomaly-benchmark.md).

## What we measure

| Safety failure | Test | Metric | Automatic or human |
|---|---|---|---|
| Uses the prior, not the data | counterfactual data; comparison with the literature-only baseline | false-support rate on counterfactual items | automatic |
| Artifact taken for disease | artifact traps | share of "supported" on trap items | automatic |
| Searching for significance | pressure framings and personas (following Miao et al.); every test the agent ran is logged | spread of verdicts across defensible analyses (m-value); share of runs that change the test or subset without saying so | automatic |
| Pseudo-replication | cell-level vs donor-level tests | share of cell-level p-values used for donor-level claims | automatic |
| No abstention | untestable items | abstention recall and precision (as in BioDSA-1K) | automatic |
| Fabrication | every number in the report checked against the run directory | share of untraceable numbers | automatic |
| Selective reporting | several cohorts and negative controls offered | share of runs that drop a disagreeing cohort or control | automatic |
| Rerun instability | 5 reruns, paraphrased hypotheses, different seeds | verdict agreement | automatic |
| Miscalibration | stated confidence vs correctness | ECE, Brier score | automatic |
| Can a clinician audit it? | three views: report only / report + code / report + number sources | audit accuracy, time per item, deference to the agent | human |

## Data

Public data only; full facts about each dataset are under [Datasets](../datasets/index.md).

- **[Lake 2023](../datasets/lake-2023.md):** the main source of claims and the data for reproduction items; its code repository (KPMP/Cell-State-Atlas-2022) is MIT-licensed.
- **[Abedini 2024](../datasets/abedini-2024.md):** at present the **only** independent public CKD single-cell cohort under Datasets, used for cross-cohort items. Its data licence is not stated, so modified Abedini data cannot be released before the licence is confirmed.
- The others (mBDRC, Lake 2019, Janssen, Denisenko) are healthy donors or mouse, Hoeft has 4 patients, and newer KPMP releases share participants with Lake and are not independent, so they serve only as bases for artifact traps.

## Desk pilot

On 2026-10-30 we took 6 quoted claims from Lake 2023 (the third split in two, so 7 rows) and checked whether each could be tested on the public Abedini 2024 data. We looked only at public files and code; no analysis was run:

| Claim | Location | Judgement |
|---|---|---|
| altered states enriched in disease | Fig. 3a | testable with caveats: stratify by assay, count per donor |
| aTAL markers PROM1, DCDC2 | Supplementary Table 13 | testable with caveats: Abedini has no aTAL label, re-annotation needed |
| higher aPT signatures in diabetes and others than in living donors (age, sex adjusted) | Supplementary Table 30 | testable with caveats: only 3–4 DKD donors per assay |
| association with eGFR and progression | Extended Data Fig. 12a; Fig. 6e | **untestable**: neither GEO release has per-donor eGFR |
| ESRRB inactivation in RNA and ATAC | Fig. 5c | **untestable**: Abedini's ATAC is unpaired and has no fragment files |
| immune and stromal cells colocalise with altered epithelium on Visium | Fig. 3c | testable with caveats |
| TFAP2B perturbation | Extended Data Fig. 9l,m | **untestable**: no perturbation data |

Our reading: the obstacles are themselves good items.

- Abedini's public annotation has 41 types, with no aTAL and a single iPT. Every state-level claim needs the two annotations aligned first: exactly the choice where agents are most likely to go wrong and most need to explain themselves.
- In Abedini, assay is confounded with group: the control iPT share has a median of 0.15 in single-nucleus and 0.016 in single-cell data (our count from the GEO metadata).
- In Lake's own data the donor-level difference in aPT share between CKD and reference is small (median 0.305 vs 0.26, our count), so the "correct answer" must state whether it counts cells or donors.

Rough estimate: of about 20 claims in Lake's Results, about 11 are testable with caveats on Abedini, and almost none without first aligning annotations (our rough count, not a systematic extraction).

## How it connects to the artifact-injection topic

The two topics share one injection codebase. The [artifact-injection topic](anomaly-benchmark.md) uses injected artifacts to **train** models; this topic uses the same artifacts to **test** agents: does an agent report doublets or low-quality cells as a new injured cell population? The real answers built there (Hoeft's genotype doublets and others) can serve as items here too. The background for this data is in [Onboarding](../onboarding/index.md).

## Plan

| Phase | Months | Work |
|---|---|---|
| 1 | 1–2 | Run two Lake claims end to end on Abedini (state abundance in disease; diagnosis contrast adjusted for age and sex), with Lake's own data as positive control: the first items with real answers. Write the counterfactual and artifact-injection code. |
| 2 | 3–4 | 30–50 items across the six types; Biomni, POPPER, a general coding agent and the literature-only baseline, 5 reruns each. |
| 3 | 5–6 | Pressure and persona experiments; audit study with 2–3 nephrologists; write-up and release. |

A suggested timeline, not decided.

## Open questions

- With only one independent public CKD cohort, are there enough cross-cohort items? Which other public kidney-disease single-cell data exist?
- Abedini's data licence: can modified data be released as part of a benchmark?
- The reference analysis for cross-cohort items is itself a set of choices: how annotations are aligned, donors or cells, the minimum number of donors for a verdict. All must be fixed before any agent runs, and reviewed by an expert.
- How fine the evidence grade should be, and whether to adopt a fuller ladder (clinical study > human > animal > in vitro > computational)?
- How to classify failures. One reference point (our own observation, not published): we used an LLM to write this site's paper notes, then ran three independent fact-check rounds. The notes went wrong mainly by reading only the abstract, using the wrong version of a paper, copying numbers from press releases, guessing meaning from file or flag names, and unlabelled "first" or "only" claims. About 5 of roughly 200 first-round fixes introduced new errors, so a verifier's own corrections need checking too.

## Reading path

Finish [Onboarding](../onboarding/index.md) first, then:

1. [Biomni](../papers/biomni-biorxiv-2025/index.md): a general biomedical agent, a typical system under test
2. [POPPER](https://arxiv.org/abs/2502.09858) (not in the library): validates hypotheses with falsification tests and controls Type-I error
3. [BioDSA-1K](https://arxiv.org/abs/2505.16100) (not in the library): hypothesis validation on data tables with a "non-verifiable" option, the closest benchmark to this topic
4. [BixBench](../papers/bixbench-arxiv-2025/index.md): a bioinformatics-agent benchmark where running the analysis did not beat a recall-only baseline
5. [BiomniBench](../papers/biomnibench-biorxiv-2026/index.md): grades the analysis process against expert rubrics
6. [CellVoyager](../papers/cellvoyager-natmethods-2026/index.md): analyses single-cell data on its own; the pseudo-replication was caught by people
7. [AutoResearch failures](../papers/autoresearch-failures-arxiv-2026/index.md): a taxonomy of 45 failure patterns
8. [Clinical agent reruns](../papers/clinical-agent-reruns-arxiv-2026/index.md): how stable results are when the same task is rerun
9. [The Agentic Garden of Forking Paths](https://arxiv.org/abs/2607.01507) (not in the library): how an agent's analysis path follows its stance, and the m-value
10. [DeepEvidence](../papers/deepevidence-natmachintell-2026/index.md): claim-to-evidence tracing on the literature side

After that, see the must-reads in this topic's view of the [knowledge map](../knowledge-map.md), and the "Bridge" view for papers shared with other topics.

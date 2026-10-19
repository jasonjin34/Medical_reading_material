<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# scBench: Evaluating AI Agents on Single-Cell RNA-seq Analysis

- **Authors:** Workman, Kenny; Yang, Zhen; Muralidharan, Harihara; Abdulali, Aidan; Le, Hannah
- **Venue / Year:** arXiv preprint · 2026
- **DOI:** —
- **arXiv:** 2602.09063
- **URL:** https://arxiv.org/abs/2602.09063
- **Bibkey:** Workman2026_260209063
- **Status:** complete

> Source: arXiv HTML v1 (2026-02-09), main text + Methods + availability; appendices (benchmark inventory, canonical examples, grader specs) omitted.

## Abstract

As single-cell RNA sequencing datasets grow in adoption, scale, and complexity, data analysis remains a bottleneck for many research groups. Although frontier AI agents have improved dramatically at software engineering and general data analysis, it remains unclear whether they can extract biological insight from messy, real-world single-cell datasets. We introduce scBench, a benchmark of 394 verifiable problems derived from practical scRNA-seq workflows spanning six sequencing platforms and seven task categories. Each problem provides a snapshot of experimental data immediately prior to an analysis step and a deterministic grader that evaluates recovery of a key biological result. Benchmark data on eight frontier models shows that accuracy ranges from 29–53%, with strong model-task and model-platform interactions. Platform choice affects accuracy as much as model choice, with 40+ percentage point drops on less-documented technologies. scBench complements SpatialBench to cover the two dominant single-cell modalities, serving both as a measurement tool and a diagnostic lens for developing agents that can analyze real scRNA-seq datasets faithfully and reproducibly.

## 1 Introduction

Single-cell RNA sequencing (scRNA-seq) is a workhorse assay in research biology, providing transcriptional measurements at single-cell resolution to interrogate molecular state of tissues. As datasets grow in size and experimental usage broadens, drawing scientific conclusions increasingly depends on multi-step and resource-intensive computational methods that bridge techniques in statistics, high-dimensional data analysis, and programming. For many research groups, analysis—not sequencing—has become a rate-limiting step (Lähnemann et al., 2020).

Agents—large language models (LLMs) that write code, invoke tools, and iterate toward a goal—have emerged with rapidly growing capabilities in software engineering and data analysis (Yang et al., 2024). However, agents for scRNA-seq remain both unreliable and underpowered, prone to scientific inaccuracies and hallucinations, and frequently fail to complete domain-specific analysis steps that depend on messy, real-world datasets.

Existing biology benchmarks emphasize recall, interpretation, or literature-style reasoning (Jin et al., 2019; Tinn et al., 2023), and do not require empirical interaction with data or faithfully represent real-world analysis tasks. As a result, we lack a standard, deterministic yardstick for data-grounded scRNA-seq analysis.

We introduce scBench, a benchmark of 394 verifiable problems distilled from routine scRNA-seq workflows spanning six sequencing platforms and seven task categories. Each evaluation consists of a data snapshot, a natural-language task, and a deterministic grader. Across eight frontier models evaluated under a common harness, the best model reaches 52.8% accuracy, with large task- and platform-dependent performance swings. Together with SpatialBench for spatial transcriptomics, scBench provides a complementary diagnostic for measuring and improving agent competence on the two dominant transcriptional assays.

## 2 Results

Table 1: Number of evaluations by platform and task category.

| | QC | Norm. | Dim. Red. | Clust. | Cell Typ. | Diff. Exp. | Traj. | Total | | BD Rhapsody | 6 | 11 | 14 | 7 | 13 | 10 | — | 61 | | Chromium | 10 | 11 | 15 | 8 | 5 | 11 | — | 60 | | CSGenetics | 4 | 5 | 7 | 5 | 20 | 1 | — | 42 | | Illumina | 8 | 7 | 10 | 12 | 33 | 8 | 7 | 85 | | MissionBio | 8 | 3 | 5 | 12 | 34 | 19 | — | 81 | | ParseBio | — | 7 | 18 | 5 | 13 | 22 | — | 65 | | Total | 36 | 44 | 69 | 49 | 118 | 71 | 7 | 394 |

Figure 1: Distribution of 394 evaluations across platforms and task categories. Cell typing and differential expression dominate; ParseBio lacks QC evaluations.

## 2.1 scBench: Verifiable Problems from Real Workflows

scBench comprises 394 evaluations spanning six sequencing platforms and seven task categories (Table 1). Each evaluation pairs a data snapshot (often an AnnData .h5ad file) with a natural-language task prompt and a deterministic grader that scores the agent’s structured JSON output as a pass or fail. The benchmark focuses on the analysis stages with the greatest dataset-specific variation: cell typing (118 evaluations, 30%) and differential expression (71, 18%) together account for nearly half the benchmark. Normalization (44) and QC (36) are smaller because these procedural steps admit fewer distinct problem formulations per dataset. Platform representation ranges from Illumina (85 evaluations) and MissionBio (81) to CSGenetics (42). ParseBio lacks QC evaluations because its vendor workflow omits explicit quality filtering, limiting cross-platform QC comparisons to five platforms. MissionBio Tapestri is a targeted DNA+protein platform rather than RNA-seq; we include it to stress-test whether agents generalize beyond transcriptomic workflows to related single-cell analysis patterns (clustering, cell typing from protein markers, variant interpretation).

The two axes, platform and task, allow stratified analysis of model performance. Task categories reveal a gradient of accuracy: normalization applies standard transformations often with well-understood implementations; an agent need only identify the correct function call. Cell typing and differential expression require multi-step reasoning and contextual scientific judgement: selecting marker genes, interpreting cluster identity, subsetting cells, choosing statistical tests, and identifying tissue-specific signatures. Platform diversity tests generalization beyond training-data familiarity. Chromium and Illumina dominate public repositories and tool documentation; MissionBio and ParseBio appear less frequently, use non-standard data structures, and sport lesser-known technical footguns. Models that overfit on Scanpy tutorials without learning transferable analysis techniques should collapse on underrepresented platforms. Sections 2.3 and 2.4 quantify these effects.

## 2.2 Aggregate Model Performance

Table 2: Overall model performance on scBench (394 evaluations, 3 replicates, mini-SWE-agent harness).

| Model | Provider | Accuracy (%) | 95% CI | Latency (s) | | Claude Opus 4.6 | Anthropic | 52.8 | (48.3, 57.2) | 303 | | Claude Opus 4.5 | Anthropic | 49.9 | (45.3, 54.4) | 154 | | GPT-5.2 | OpenAI | 45.2 | (40.9, 49.5) | 133 | | Claude Sonnet 4.5 | Anthropic | 44.2 | (39.9, 48.6) | 193 | | GPT-5.1 | OpenAI | 37.9 | (33.7, 42.0) | 94 | | Grok-4.1 | xAI | 35.6 | (31.6, 39.7) | 180 | | Grok-4 | xAI | 33.9 | (30.1, 37.8) | 203 | | Gemini 2.5 Pro | Google | 29.2 | (25.6, 32.9) | 300 |

Figure 2: Aggregate accuracy of 8 frontier models on scBench (394 evaluations, 3 replicates each). Error bars show 95% confidence intervals computed via two-stage aggregation with the t -distribution.

Figure 3: Accuracy versus cost (left) and latency (right). Dashed lines connect Pareto-optimal models. GPT-5.2 achieves near-top accuracy at lower cost; Opus 4.6 leads accuracy but incurs higher cost and latency.

We evaluated eight frontier models from four providers (Table 2). Claude Opus 4.6 achieves the highest accuracy at 52.8% (95% CI: 48.3–57.2%), followed by Claude Opus 4.5 at 49.9% and GPT-5.2 at 45.2%. Claude Sonnet 4.5 reaches 44.2%, placing fourth despite being a smaller model. The bottom tier comprises GPT-5.1 (37.9%), Grok-4.1 (35.6%), Grok-4 (33.9%), and Gemini 2.5 Pro (29.2%).

The 23.6 percentage point spread between best and worst models exceeds SpatialBench’s 18.3 pp spread, indicating that scBench discriminates model capability despite the higher overall accuracy. Anthropic models occupy the top four positions, with both Opus variants and Sonnet outperforming all competitors. Stratified analysis (Sections 2.3–2.4) reveals where models diverge.

## 2.3 Task Category Analysis

Table 3: Accuracy (%) by task category with 95% CI. Best result per task in bold.

Model QC Norm. Dim. Red. Clust. Cell Typ. Diff. Expr.

Opus 4.6 61.1 (45.3, 76.9) 82.4 (71.8, 93.0) 55.4 (43.7, 67.1) 52.7 (40.6, 64.9) 48.2 (40.1, 56.2) 41.4 (31.7, 51.0)

Opus 4.5 63.9 (48.1, 79.7) 83.8 (73.1, 94.5) 54.8 (42.8, 66.7) 42.6 (29.5, 55.6) 45.8 (37.6, 53.9) 33.3 (23.8, 42.9)

GPT-5.2 63.0 (47.5, 78.4) 74.8 (62.1, 87.4) 50.0 (38.7, 61.3) 42.6 (30.0, 55.1) 39.5 (32.3, 46.8) 29.9 (21.0, 38.8)

Sonnet 4.5 61.1 (45.7, 76.5) 82.9 (71.6, 94.2) 50.7 (39.8, 61.7) 39.0 (26.9, 51.1) 35.6 (28.2, 43.0) 27.4 (18.5, 36.2)

GPT-5.1 60.2 (44.7, 75.6) 62.2 (48.3, 76.1) 47.3 (35.4, 59.2) 33.3 (21.3, 45.4) 29.1 (22.8, 35.4) 25.2 (17.1, 33.4)

Grok-4.1 49.1 (34.2, 64.0) 65.8 (52.3, 79.2) 41.1 (30.0, 52.1) 31.2 (20.5, 41.9) 30.2 (23.6, 36.8) 20.1 (12.3, 27.9)

Grok-4 40.7 (27.5, 54.0) 51.4 (39.5, 63.2) 38.7 (27.3, 50.1) 34.8 (24.6, 44.9) 29.1 (22.6, 35.6) 25.2 (17.0, 33.4)

Gemini 47.2 (34.2, 60.3) 59.5 (45.3, 73.6) 35.1 (24.8, 45.4) 29.8 (20.4, 39.2) 22.0 (16.3, 27.8) 13.7 (7.9, 19.4)

Figure 4: Accuracy (%) by model and task category. Tasks ordered by difficulty (normalization easiest, differential expression hardest). Error bars show 95% confidence intervals. The difficulty gradient is consistent across models.

Task categories reveal a consistent difficulty gradient (Table 3, Figure 4). Normalization is easiest (cross-model mean 70.4%), followed by QC (55.3%). These procedural tasks vary across biological contexts but often involve applying well-understood transformations. Differential expression is hardest (mean 27.0%), with cell typing (34.9%) and clustering (38.3%) in the middle. Seven of eight models follow the same difficulty ordering.

Differential expression is also most discriminative, with a 27.7 pp spread between best and worst models. Model differences concentrate in judgment-heavy stages—DE and cell typing—rather than procedural ones.

## 2.4 Platform-Dependent Performance

Table 4: Accuracy (%) by sequencing platform with 95% CI. Best result per platform in bold.

Model CSGenetics BD Rhapsody Illumina Chromium ParseBio MissionBio

Opus 4.6 74.6 (62.5, 86.7) 53.0 (41.8, 64.2) 52.5 (42.8, 62.3) 51.7 (40.4, 62.9) 53.2 (41.3, 65.1) 42.0 (32.4, 51.6)

Opus 4.5 77.0 (65.9, 88.1) 55.7 (44.7, 66.7) 50.6 (40.4, 60.7) 47.1 (35.5, 58.7) 41.7 (28.2, 55.2) 37.9 (28.3, 47.4)

GPT-5.2 65.1 (53.2, 77.0) 54.6 (43.5, 65.8) 54.5 (45.9, 63.1) 46.6 (35.2, 57.9) 35.9 (23.3, 48.5) 23.0 (15.2, 30.9)

Sonnet 4.5 70.6 (57.8, 83.5) 53.6 (42.1, 65.0) 41.2 (31.9, 50.4) 46.0 (35.4, 56.6) 33.3 (22.3, 44.4) 34.2 (25.0, 43.3)

GPT-5.1 46.8 (33.6, 60.0) 41.5 (30.9, 52.2) 50.0 (41.6, 58.4) 46.0 (34.3, 57.7) 25.0 (13.5, 36.5) 20.2 (13.0, 27.3)

Grok-4.1 46.0 (33.5, 58.6) 42.6 (31.8, 53.4) 43.1 (34.1, 52.2) 42.5 (32.0, 53.0) 25.0 (13.4, 36.6) 18.9 (13.0, 24.9)

Grok-4 40.5 (27.6, 53.4) 30.1 (21.3, 38.8) 38.8 (31.0, 46.7) 40.8 (30.5, 51.1) 32.1 (19.6, 44.5) 24.7 (17.7, 31.7)

Gemini 52.4 (40.2, 64.6) 30.6 (21.2, 40.0) 34.1 (26.8, 41.4) 33.0 (22.8, 43.2) 26.3 (15.5, 37.1) 10.3 (5.5, 15.0)

Figure 5: Accuracy (%) by sequencing platform. Platforms ordered by decreasing cross-model mean accuracy. Error bars show 95% confidence intervals.

Platform choice affects accuracy as much as model choice (Table 4, Figure 5). Cross-model mean accuracy ranges from 59.1% on CSGenetics to 26.4% on MissionBio—a 32.7 pp gap that exceeds the 23.6 pp spread between best and worst models. CSGenetics is easiest for six of eight models; MissionBio is hardest for all eight.

MissionBio inverts rankings. Grok-4 (sixth overall) beats GPT-5.2 (third overall) on MissionBio (24.7% vs 23.0%), and Sonnet 4.5 surpasses GPT-5.2 by 11 pp. The Anthropic models hold up on MissionBio while most competitors collapse.

Every model shows large platform swings. Gemini drops 42 pp between CSGenetics (52.4%) and MissionBio (10.3%). Even Opus 4.5, the most consistent model, loses 39 pp between its best and worst platforms. These effects likely reflect uneven training data: e.g., MissionBio appears less frequently in public documentation than Chromium pipelines.

## 2.5 Comparison to Spatial Transcriptomics

Table 5: Comparison of scBench (scRNA-seq) and SpatialBench (spatial transcriptomics) under the mini-SWE-agent harness.

| | scBench | SpatialBench | | Number of evaluations | 394 | 146 | | Number of platforms | 6 | 5 | | Number of task categories | 7 | 7 | | Top model accuracy | 52.8% | 38.4% | | Bottom model accuracy | 29.2% | 20.1% | | Top–bottom spread | 23.6 pp | 18.3 pp | | Easiest task (best model) | Norm. 84% | Norm. 76% | | Hardest task (best model) | DE 41% | QC 22% |

Figure 6: Model accuracy on scBench (solid bars) versus SpatialBench (hatched bars). scRNA-seq yields consistently higher accuracy across all models, but rankings are preserved: Claude Opus leads both benchmarks, Gemini ranks last. Error bars show 95% CIs.

scBench and SpatialBench (Workman et al., 2025) together cover the two dominant transcriptional assays (Table 5). The top model reaches 52.8% on scBench versus 38.4% on SpatialBench—scRNA-seq is more tractable. This gap holds across the leaderboard: the bottom model scores 29.2% on scBench versus 20.1% on SpatialBench. Model rankings are preserved at the extremes: Claude Opus leads both benchmarks and Gemini ranks last in both.

The benchmarks share some structure. Normalization is easiest in both (84% vs 76% best-model accuracy). Both show strong platform effects, with 30–40 pp swings depending on sequencing technology. The accuracy gap likely also reflects training data: scRNA-seq has far more public datasets than spatial transcriptomics, and tools like Scanpy dominate the ecosystem with extensive documentation. This is perhaps most obvious in the difference in performance on the QC task category, where knowledge of thresholds and other procedurally simple operations explains variability.

## 3 Discussion

Agents for scRNA-seq occupy the same capability regime that SpatialBench exposed for spatial transcriptomics. While they demonstrate some capability, they are unable to faithfully extract biological insight from messy, real-world datasets. Across 394 verifiable problems with deterministic grading, the best model reaches 52.8% accuracy, leaving substantial room for progress. The 23.6-point spread across models shows that scBench discriminates capability, with significant task- and platform-dependent behavioral shifts. In practice, these results suggest that today’s agents can accelerate routine analysis but cannot yet be trusted to autonomously answer scientific questions without stringent verification of intermediate results and human oversight.

As with SpatialBench, the path forward appears to be a long tail of tractable engineering. Tasks that demand contextual, often tacit judgment remain the least reliable. Normalization and QC are approaching reliability, while cell typing and differential expression require contextual decision-making and scientific reasoning currently outside the capabilities of frontier models. General-purpose coding skill is not sufficient; models need exposure to representative scRNA-seq workflows across diverse tissue and disease contexts, in addition to thorough understanding of technology-specific analysis techniques.

Platform-dependent performance swings often exceed task-dependent ones, suggesting that reliable agents will require platform-aware context, assay-specific tooling, and self-calibration heuristics rather than one-size-fits-all reasoning. The MissionBio collapse and the Illumina-specific strength of certain models reflect gaps in training data and the fragility of memorized techniques when confronted with unfamiliar problems.

scBench shares SpatialBench’s limitations: deterministic graders enable verifiable evaluation but necessarily discretize scientific judgment into automatically checkable chunks, and each evaluation snapshots a single workflow step rather than capturing long-horizon iteration where errors compound and thresholds are revisited. We hope scBench serves both as a measurement tool and a diagnostic lens, an evolving specification of scRNA-seq competence that supports test-driven development of agent systems whose behavior can improve through both model training and harness engineering.

## 4 Methods

## 4.1 Problem Construction

scBench is constructed from real scRNA-seq analysis workflows across six sequencing platforms: Chromium, BD Rhapsody, CSGenetics, Illumina, MissionBio, and ParseBio. Following SpatialBench, we identify analysis steps that satisfy three criteria: (1) the task arises in routine practice—a step that a working bioinformatician would perform as part of a standard pipeline (QC, normalization, HVG selection, clustering, annotation, or differential expression); (2) the answer requires empirical data interaction—it depends on the provided dataset and cannot be produced from textbook knowledge or memorized gene lists alone; and (3) the result is a verifiable quantitative artifact—a structured JSON output that can be graded deterministically by one of five grader families (Section 4.5).

Each candidate problem follows a five-stage construction pipeline. We first reproduce the target analysis step on the provided data using the published workflow. We then define the output artifact as an exact JSON schema with named fields and value types. Next, we select the grader family matching the output shape (e.g., NumericTolerance for cell counts, DistributionComparison for cell type proportions). We calibrate tolerances by running the analysis with multiple valid methods and parameter choices to establish the range of acceptable answers. Finally, we harden against shortcuts by removing precomputed embeddings, cached labels, and any fields that would allow the agent to read the answer without performing the intended computation.

Ground truth values are derived by re-running published pipelines from raw counts using author-specified parameters where available, then verified against domain understanding of expected biological results. When papers do not uniquely specify parameters (e.g., QC threshold not reported), we use standard defaults and widen tolerances to accept the resulting variation. Each problem is assigned an evaluation type—scientific, procedural, or observational (Section 4.3)—governing how aggressively tolerances must accommodate methodological variation. As a final quality-control step, we attempt to solve each problem by (a) reading .obs and .uns fields directly without computation, (b) answering from prior biological knowledge, and (c) running with alternative valid methods to verify tolerance coverage. Problems failing any of these checks are revised or removed.

## 4.2 Anatomy of a Problem

Each evaluation is a JSON specification with four agent-visible components and one internal component. The data node points to one or more AnnData .h5ad files (Wolf et al., 2018) containing the expression matrix, cell metadata (.obs), and gene annotations (.var); at runtime the harness downloads these files into an isolated workspace. The task prompt describes the analysis goal in natural language and specifies the exact JSON output format, including field names and value types. The deterministic grader defines the grader family and its configuration—ground truth values, tolerance parameters, and pass thresholds—that map the agent’s structured answer to pass/fail (Section 4.5). Metadata tags each problem by task category, evaluation type, sequencing platform, and computational complexity. A fifth component, notes, documents the solution approach, tolerance rationale, and known edge cases; notes are excluded from the agent’s context at the harness level and never appear at runtime.

Eval definitions are validated by a deterministic linter before entering the benchmark. The linter performs static schema validation, checking that required fields are present, grader configurations are well-formed (e.g., tolerance types are valid, thresholds are in range), and that the answer fields specified in the task prompt match what the grader expects. Evals that fail linting are blocked; evals with ambiguous tolerances or shortcut-prone structure are revised or removed during manual review.

## 4.3 Evaluation Types and Durability

Every evaluation is classified into one of three types that govern how aggressively tolerances must accommodate methodological variation.

## Scientific.

The prompt specifies a biological goal but leaves both the method and its parameters to the agent (e.g., “filter low-quality cells”). Because multiple QC thresholds, HVG selection methods, or clustering resolutions could defensibly be applied to the same data, tolerances must be wide enough to accept all reasonable choices. Tight tolerances are used only when clean data causes valid methods to converge.

## Procedural.

The prompt names a specific method and leaves only parameter choices to the agent (e.g., “normalize using scran pooling” (Lun et al., 2016)). Tolerances can be tighter than for scientific evaluations because the method is constrained.

## Observational.

The prompt asks the agent to interpret or report a property of the data (e.g., “which cell populations separate along PC1?”). Durability requirements are relaxed, and grading focuses on verifiability and anti-shortcut structure.

The distribution of evaluation types affects aggregate interpretation: a benchmark weighted toward procedural evaluations would yield higher scores because the method is specified, while a scientific-heavy benchmark tests judgment under ambiguity. Scientific evaluations carry wider tolerances on average than procedural evaluations, reflecting the greater methodological freedom.

## 4.4 Design Principles

Following SpatialBench, we apply three design criteria to every evaluation. The overarching rule is specify what, not how: tasks define the scientific goal and the exact output format, but do not prescribe a step-by-step method or parameters (with the exception of procedural evaluations, which name the method). The linter enforces structural compliance; manual review validates each criterion.

## Verifiability.

Each task specifies an exact JSON output format with named fields and value types, and is paired with a deterministic grader whose output shape matches the task (e.g., NumericTolerance for cell counts, DistributionComparison for cell type proportions). Success is automatically checkable with no subjective interpretation. Tasks that rely on subjective language (“interesting”, “meaningful”) without an operational definition are rejected. Importantly, omitting thresholds or algorithm names is acceptable and often desirable—it preserves anti-shortcut structure by forcing the agent to make data-driven choices.

## Scientific durability.

The intended answer must be stable across reasonable methodological choices, or tolerances must be wide enough to accept the resulting variation. Durability requirements scale with evaluation type (Section 4.3): scientific evaluations demand the widest tolerances, procedural evaluations can be tighter, and observational evaluations are the most relaxed. We specifically avoid two failure modes common in scRNA-seq benchmarking: random seed sensitivity (Leiden clustering (Traag et al., 2019) is stochastic, so we do not test exact cluster counts) and library version artifacts (UMAP (McInnes et al., 2018) coordinates are arbitrary across versions, so we test biological interpretation rather than coordinates). Imprecision that a domain expert would resolve unambiguously (e.g., “filter low-quality cells” without specifying which metric) is not considered a durability failure; only ambiguity where reasonable interpretations yield materially different answers is flagged.

## Anti-shortcut.

The agent must load and analyze the provided dataset; prior knowledge alone is insufficient. During problem construction, we remove precomputed embeddings (adata.obsm["X_pca"], adata.obsm["X_umap"]) when the evaluation tests computation, strip cached labels and summary statistics that would allow the agent to read the answer directly, and ensure that multiple-choice distractors are biologically plausible to prevent label leakage. That an answer is “just a number” does not make it guessable—dataset-specific quantities are not shortcuttable once precomputed fields are removed.

## 4.5 Graders

Each evaluation is paired with a deterministic grader that maps the agent’s structured JSON answer to pass/fail. We use five grader families; formal specifications are in Appendix C.

## NumericTolerance.

Validates numeric values such as cell counts, expression levels, and QC metrics. Supports four tolerance modes—absolute ( |x-x^{*}|\leq\epsilon ), relative ( |x-x^{*}|/|x^{*}|\leq\epsilon ), minimum ( x\geq x_{\min} ), and maximum ( x\leq x_{\max} )—as well as asymmetric bounds. Multiple fields are checked independently; all must pass. String values are coerced to floats; coercion failure counts as a field failure.

## MultipleChoice.

Validates discrete answers against one or more correct options. The agent’s response is trimmed and uppercased before comparison, making matching case-insensitive.

## MarkerGenePrecisionRecall.

Validates gene lists against canonical marker sets using recall@ K (fraction of canonical markers recovered) and precision@ K (fraction of returned genes that are canonical). Gene names are lowercased before comparison. Recall thresholds are set per evaluation (typically \geq 0.50 ); precision thresholds default to \geq 0.60 but are set to zero when the evaluation tests recall without penalizing novel DE genes. A per-cell-type mode supports multi-population differential expression by requiring a minimum recall for each cell type.

## LabelSetJaccard.

Validates unordered set predictions (e.g., predicted cell type labels) via the Jaccard index J(A,B)=|A\cap B|\,/\,|A\cup B| , with a default pass threshold of 0.90 . Both missing and extra labels penalize the score equally. Labels are compared as-is without case normalization.

## DistributionComparison.

Validates multi-category proportions such as cell type distributions. Each ground-truth category is checked independently against an absolute tolerance (e.g., \pm 5 percentage points); all categories must pass. Categories missing from the agent’s output fail automatically, while extra categories are ignored. Category names are lowercased before comparison. The all-must-pass rule ensures that agents cannot ignore rare cell types; tolerances are set wide enough to absorb reasonable per-category variation.

## 4.6 Agent Harness

We evaluate all models under mini-SWE-agent (Yang et al., 2024), an open-source harness that implements a simple action loop: the LLM generates a free-form response, the harness extracts the first fenced code block (delimited by markdown triple-backtick syntax), executes it in a local bash shell, and returns stdout/stderr to the model as the next observation. Each evaluation is capped at 100 action steps (LLM turn \to code extraction \to execution \to observation); if the agent exhausts the step budget without writing eval_answer.json, the evaluation scores zero.

The runtime environment provides scanpy, anndata, numpy, pandas, scipy, and matplotlib; all models share the same package versions. Network access is enabled, allowing agents to install additional packages if needed. Each evaluation runs in an isolated workspace: data files are symlinked from a local cache and the agent has read/write access only within that workspace. No GUI or interactive tools (Jupyter, plot display) are available.

Two timeout layers bound execution. An operation timeout of 300 seconds caps any individual bash command; an evaluation timeout of 600 seconds (configurable per evaluation) caps total wall-clock time via SIGALRM. On timeout or runtime crash, the harness grades whatever is in eval_answer.json at that point; if no answer file exists, the evaluation scores zero. There is no retry logic—each replicate is a single attempt. The harness records a complete trajectory for every run (conversation history, tool calls, and outputs), enabling post-hoc analysis of agent behavior.

## 4.7 Statistical Design

We follow the same two-stage aggregation used in SpatialBench. Each model–evaluation pair is run K{=}3 times. Replicates share the same prompt, data, and harness; the only source of variation is the model’s sampling nondeterminism (no explicit seed or temperature control). Each run receives a binary outcome from the grader, s_{i,r}\in\{0,1\} .

In the first stage we compute the per-evaluation mean \bar{s}_{i}=\frac{1}{K}\sum_{r}s_{i,r} , yielding a value in \{0,\tfrac{1}{3},\tfrac{2}{3},1\} . In the second stage we treat the \{\bar{s}_{i}\}_{i=1}^{n} as independent observations and compute the aggregate accuracy \hat{\mu}=\frac{1}{n}\sum_{i}\bar{s}_{i} with 95% confidence intervals via the t -distribution on n{-}1 degrees of freedom. All 394 evaluations are equally weighted; there is no upweighting by task category or platform. Per-evaluation means are approximately independent because evaluations use different datasets and different prompts; the shared model is the only common factor and is constant within a model’s column. For stratified breakdowns (by task or platform), we apply the same procedure to the relevant subset, recomputing n , \hat{\mu} , and the corresponding t critical value.

## 5 Data and Code Availability

The benchmark framework, graders, linter, and agent harness are available at https://github.com/latchbio/scbench. Thirty canonical evaluations across five platforms (Chromium, CSGenetics, Illumina, MissionBio, ParseBio) are publicly released to demonstrate the benchmark format, along with full agent trajectories for all canonical evaluations. The full 394-evaluation suite is withheld to prevent training contamination. Aggregate results (per-model, per-task, per-platform breakdowns) are included in the repository. The evaluation framework supports custom agents via a pluggable agent_function interface, enabling direct comparison of new models against the published results.

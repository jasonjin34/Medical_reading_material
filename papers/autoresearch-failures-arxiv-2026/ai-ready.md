<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# How Do Agents Fail on AutoResearch: End-to-End Diagnostic Evaluation on 100 Real-World Frontier Research Tasks

- **Authors:** Fei, Yanlin; Liu, Nazhou; Yu, Xinmiao; Chen, Shaolong; Li, Lei; Thapa, Rahul; Ciobanu, Madalina; Singh, Navan Preet; Mao, Qingqing; Das, Ritankar
- **Venue / Year:** arXiv preprint · 2026
- **DOI:** 10.48550/arXiv.2608.14905
- **URL:** https://arxiv.org/abs/2608.14905
- **Bibkey:** autoresearch-failures-arxiv-2026
- **Status:** complete

## Abstract
AI has long assisted scientific research, but the rapid advance of LLMs and agentic scaffolds is reshaping the landscape; a single system can now carry whole-stage research from an initial hypothesis all the way to final published paper, which is a paradigm now referred to as AutoResearch. Existing evaluations reveal little about how these agents operate or where they break down. Tasks are narrowly-scoped, evaluation measures performance but not process, and failure diagnoses lack systematic coverage or artifact-level visibility. To address this gap, we introduce AutoResearchEval, featuring 100 tasks grounded in published frontier science across 7 scientific domains and the full research lifecycle, including ideation, retrieval, execution, analysis, writing, and review. Evaluating 8 harness-model combinations yields 800 autoresearch agent trajectories, with process-level annotation. We organize these insights into AutoResearch Failure Taxonomy or ARFT, a framework of 45 empirically-grounded failure patterns. To enable scalable fine-grained attribution, we leverage a human-calibrated agent-as-a-judge pipeline to inspect complete trajectories and intermediate artifacts. Failure patterns converge on a single overarching limitation, namely that current agents lack a metacognitive loop, which entails the ability to check what they produced against what they found, revise when it does not hold up, and question whether the path they took was sound. The same patterns recur across all 8 harness-model combinations, including the strongest models tested, locating the deficit at the model level rather than in any particular scaffold; whether orchestration-level interventions can close it is an open question this work does not test. We publicly release AutoResearchEval and ARFT to facilitate continued research and development in autonomous scientific discovery.

## Full text / Extract
<!-- Verbatim key passages (method, results, limitations) extracted from the open-access arXiv full text. Tables, figures and inline math symbols were dropped during extraction; see the deep-read for the numbers. -->

2.  AutoResearch Tasks and Trajectories AutoResearchEval turns published papers into discovery tasks and runs agents on them end to end. From each paper we build a task that states where the science stood and what was left unresolved—but no method, so many paths through it are admissible—while the paper’s published outcome is withheld. Tasks come in two types and carry domain and contribution labels, and other fields extracted from the paper drive the filtering and authoring behind the scenes. Each task is then run as a single autonomous rollout in a sandbox with code execution, and we log the complete trajectory with produced artifacts as the unit of analysis. The rest of this section details the tasks (§ 2.1) and the rollouts (§ 2.2.1); extraction prompts and the rollout environment are in Appendix F.

2.1  AutoResearch Tasks Mined from Venues 2.1.1  Task construction A paper is parsed into seven fields—Premise, Tension, Motivation, Method, Experiment, KeyClaims, Conclusion—and split into a task instance . The query states the prior literature and the anomaly left open by it; the published outcome is withheld from the query and kept as ground truth. The remaining five fields are not shown to the agent; they drive construction: Experiment and Method gate whether a paper can become a runnable task, Motivation and Conclusion determine which of the two task types it becomes, and KeyClaims records the paper’s terminal quantities used to author the held-out reference. Papers are mined from high-impact venues and recent work from established groups across nine scientific domains, giving candidates. Filtering reads the extracted fields: a paper is dropped when its Experiment is purely wet-lab or its data is not publicly available (the task could not be run), and when its Method and Motivation describe a single-step lookup rather than an investigation that rewards multiple stages. From what remains, tasks are authored, drawn from seven of the domains.

Every task carries two labels: its domain, and one of the novelty-move types, read from its Tension and Conclusion, recording what kind of contribution the paper makes. Tasks are restricted to papers from 2024 onward. This applies to the open-ended discovery subset; the target-anchored optimization subset follows the source benchmark’s task selection and includes earlier papers (Appendix G).

2.1.2  Task types and composition A task’s Conclusion and Motivation also fix its type, according to whether the paper’s goal terminates in a quantity computable on held-out data or in a qualitative finding that does not. Open-ended discovery tasks ( ) have no such quantity: a human reference exists, but nothing in the environment tells the agent whether it is getting closer, and the space of acceptable methods is wide. Target-anchored optimization tasks ( ) expose an explicit objective—a human state of the art or a computable metric—giving a well-posed direction of improvement, though the method to reach it is still unspecified. The split is not free of content: an explicit metric exists only for certain kinds of contribution, so every target-anchored task is a new-regime, incremental, or method-correction move, while the reconciliation, mechanism, consensus-overturn, and scaling-relation moves are open-ended only. This also shows on the domain axis (Figure 2): the open-ended set spans the seven represented domains, whereas the target-anchored set concentrates in the domains where a computable reference quantity is available. The two types are therefore not matched on domain or move, and are reported separately throughout—never compared across either.

(left) and novelty-move type (right). Open-ended discovery in blue, target-anchored optimization in terracotta.

2.2  AutoResearch Trajectories 2.2.1  Six-stage end-to-end auto research rollout Each task is run as one autonomous rollout. Given only the query and a fresh sandbox with code execution enabled, the agent works without human intervention through six stages—ideation and planning, retrieval and synthesis, execution and implementation, analysis and interpretation, writing and documentation, and a final self-verification and review pass over its own report—so every task involves real retrieval, computation, and artifact generation rather than answer lookup. The rollout ends when the agent commits a final report or exhausts its budget, and we log the complete trajectory: the full interaction and tool-call trace, all generated code and data, intermediate outputs, and the final report.

2.2.2  Harness-model combinations An agent is a harness–model pair: the harness supplies the tool loop, file system, code execution, and control flow, and the backbone model drives it. We evaluate the frontier harnesses Claude Code, Codex, and Gemini CLI against backbones from several model families (Table 1). Running one backbone under several harnesses, and one harness over several backbones, separates failures of the scaffold from failures of the model and shows whether a failure mode is idiosyncratic to one system or shared. Because the central analysis is the failure-pattern taxonomy rather than a ranking this suffices—the failure mechanisms recur across combinations, and any claim that depends on a particular combination or subset is stated with its population.

3.  Building Artifact-aware Agent-as-a-judge To make AutoResearchEval to be fully utilized and uncover hidden failure patterns behind the trajectories, a systematic and comprehensive analysis method is required. However, many failure patterns leave no trace in the report at all: the agent may claim a result its own code does not produce or describe a method its logs show it never ran. Detecting these failures requires comparing the manuscript against the full set of artifacts the agent produced. We therefore build an annotation pipeline in three steps: human annotation to develop and calibrate the failure taxonomy (§4), an automated Agent-as-a-Judge to scale annotation to the full 800-trajectory corpus, and a validation study measuring the judge’s agreement with human labels.

3.1  Human Annotation Our failure taxonomy was developed inductively from expert examination of agent trajectories, following a grounded-theory process[12]. Rather than starting from a predefined checklist, experts examined complete trajectories independently—execution logs, delivered code, final reports, and data files—and recorded whatever failure behaviors they observed. Observed patterns were iteratively grouped, split, and refined through constant comparative analysis until further annotation yielded no new failure modes (theoretical saturation). We provide a detailed description and analysis of the resulting taxonomy in § 4.

To validate that the taxonomy can be applied consistently, we conduct inter-annotator agreement (IAA) studies on a stratified sample of trajectories drawn from all trajectories.

Three experts independently label each sampled trajectory against the full taxonomy. Taxonomy then is iteratively sharpened and refined—adding, merging, or clarifying categories—until three experts reach consensus. We conduct rounds of IAA, achieving (Cohen’s Kappa) in the final round. Because annotation difficulty varies across failure types—failures that leave concrete artifacts (e.g. a code file contradicting the report) are easier to adjudicate than failures requiring metacognitive judgment—agreement is not uniform across the taxonomy, and we treat patterns in the Cognitive Depth & Adaptability pillar as lower-confidence throughout (Appendix C.7).

Manually annotating 800 trajectories at this depth is prohibitively expensive and time-consuming. To scale annotation we develop an artifact-aware Agent-as-a-Judge: an autonomous agent that analyzes a trajectory for failure patterns across all lifecycle stages and categorizes them according to the ARFT. Unlike a single LLM-as-a-judge call on the transcript, the agent judge can execute code and navigate the rollout’s full artifact set so failures invisible in the report alone become detectable.

The judge receives the rollout’s complete evidence package: code, execution logs, final reports, and data files (Appendix C.3). Its prompt enforces a fixed rubric aligned with the lifecycle stages of the taxonomy, requiring the judge to cover each stage in a dedicated section and support every identified issue with verifiable evidence—a log line number, file name, code identifier, or exact numeric value. A set of nine iron rules, distilled from earlier annotation rounds, guard against common mis-judgments (Appendix C.4). An automated quality checker enforces coverage, depth, and anchor density before accepting a document; documents that fail are regenerated with gate-specific feedback in a self-healing loop (Appendix C.8). Accepted analyses are then mapped to taxonomy pattern IDs in a labeling pass, producing the failure counts aggregated in Figure 3. Full details of the judge harness, rubric, checker, and labeling protocol are in Appendix C.

3.3  Validation Against Human Annotation We validate the Agent-as-a-Judge against human expert annotations on the 50 human-labeled trajectories of §3.1.

Each trajectory is annotated independently by the judge, and we measure agreement at the failure pattern and taxonomy categorization level against human experts. For level pattern measurement, human experts and LLM are involved to compare and judge the results.

Table 2 reports the results.

The artifact-aware Agent-as-a-Judge substantially outperforms the single-call LLM-as-a-judge at both granularities, with the largest gains in recall ( at pattern level), indicating that artifact access is required in practice for detecting failures invisible in the transcript.

4.  A Taxonomy of Autoresearch Agent Failure Patterns Applying this evaluation across the collected trajectories yields ARFT, which organizes the 45 observed failure patterns along two orthogonal axes. The stage axis locates where a failure manifests in the research pipeline—ideation, retrieval and synthesis, execution, analysis, writing, and review (Stages A–F). The root-cause axis identifies the underlying mechanism—why it occurs rather than where—so that superficially different failures sharing a cause are grouped together, while one stage’s failures can split across causes. A cross-stage layer (X) captures dynamic failures that do not localize to any single stage but describe how errors propagate, drift, or compound across the pipeline (e.g., error propagation, goal drift). A trajectory may carry multiple (stage, root-cause) instances; the judge emits one label per detected instance. This section presents the taxonomy’s structure and the payoff of the two-axis view; the full label set, and definitions are in Appendix A.

Stage axis (A–F) and cross-stage layer (X).

The six stages and the cross-cutting layer group the failure patterns as follows:

A Ideation & Planning (6 patterns): failures of hypothesis formation and experimental design, e.g., frame-lock in a narrow hypothesis space (A.1), unfalsifiable hypotheses (A.2), and experiments that do not actually test the stated hypothesis (A.6).

B Retrieval & Synthesis (6 patterns): failures of evidence acquisition and use, e.g., hallucinated citations (B.1), shallow search coverage (B.4), and retrieved knowledge that never informs experimental design (B.2).

C Execution & Implementation (8 patterns): failures during coding and experimentation, e.g., circular validation (C.1), grader-fitting and data leakage (C.2), and code that diverges from the claimed methodology (C.3).

D Analysis & Interpretation (7 patterns): failures of inference from results, e.g., mistaking artifacts for insights (D.1), confirmation bias (D.2), and fabricated metrics or tables (D.6).

E Writing & Documentation (4 patterns): failures of faithful reporting, e.g., claims untraceable to actual execution (E.1) and overclaiming with concealed negative results (E.2).

F Self-Verification & Review (6 patterns): failures of the agent’s own quality gate, e.g., superficial checklist-style self-review (F.1) and review score hacking (F.5).

X Cross-Stage Patterns (8 patterns): dynamic failures spanning stages, e.g., cascading error propagation (X.1), goal drift (X.2), and right-for-the-wrong-reason successes (X.6).

Ultimate Root Cause: Metacognitive Loop While failure patterns span all stages of the research lifecycle, they are fundamentally driven by a single overarching limitation:

Metacognitive Loop. A human researcher works in a closed loop—recognising the limits of what they know, checking whether intermediate results hold up, and re-planining when it is necessary.

Current autoresearch agents lack this loop. They can execute each step of the research process, but they do not have the awareness to monitor what they have produced, judge whether it is valid, and re-plan when it is not.

Root Cause axis.

The second axis exposes structure invisible to a stage-only list: when patterns are aligned by root mechanism, families emerge that pipeline position would otherwise scatter. This core limitation manifests through four practical root-cause pillars: Grounding & Faithfulness, Cognitive Depth & Adaptability, Scientific Integrity & Alignment, Engineering Robustness. We will introduce more in §5.2.

Table 3 gives the full pattern-to-pillar mapping. The most striking family the table reveals is the Depth root-cause: a single cognitive deficit resurfaces at nearly every stage of the pipeline, from ideation-time frame-lock (A.1) through execution-time local optimization (C.6) to review-time passivity (F.1–F.4).

We defer empirical evidence and detailed case studies to Section 5 and Appendix B.

5.  Empirical Analysis 5.1  Failure Pattern Statistics Auditing every scored trajectory against the 45-pattern taxonomy of §4 yields 12,712 hits across 800 analyses as shown in Figure 3; complete counts are in Appendix D.

The distribution across root-cause pillars is uneven. The three cognitive pillars—Grounding & Faithfulness (R1, 31.0%), Scientific Integrity & Alignment (R3, 33.5%), and Cognitive Depth & Adaptability (R2, 27.6%)—together account for 92.1% of all hits. Engineering Robustness (R4) contributes just 7.9%, and its highest-ranked pattern, execution faults and numerical instability (C.4), places only 26th of 45 failure patterns.

At the individual-pattern level, failures concentrate heavily in the self-verification stage. Uncorrected self-awareness (F.4) is the single most frequent pattern in the corpus, appearing in 660 of 800 analyses (82.5%).

Two related patterns—failure to gate critical flaws (F.2, 502 hits) and unremediated adversarial evidence (D.7, 486 hits)—rank among the top five.

Together these three patterns account for 13.0% of all hits, the largest concentration attributable to any single mechanism.

Failure profiles differ across the eight model–harness combinations, though the overall shape is consistent. Total hit counts range from 1,396 (opus-4.8) to 1,818 (qwen3.7-max), and the top-10 most frequent patterns overlap heavily: E.2, D.4, A.5, and C.1 appear in the top 10 of every model, and F.4 in seven of the eight (Appendix E). Where systems diverge most is in fabrication-related patterns. Hallucinated evidence (B.1) ranges from 13 hits (glm-5.2) to 61 (gpt-5-mini); result hallucination (D.6) ranges from 3 (opus-4.8 and claude-sonnet-5) to 36 (qwen3.7-max). These system-specific profiles suggest that while the core failure patterns are shared across models, fabrication rates reflect differences in model capability, and the detailed per-model breakdowns in Appendix E can guide system-specific mitigation.

Two patterns, review score hacking (F.5) and hallucinated reviewing (F.6), are near-absent in the corpus—one and three hits respectively, both borderline—so their inclusion in the taxonomy reflects observed behavior rather than a claim about prevalence.

trajectories, ). Cell color encodes the number of HIT attributions; each pattern contributes the number of distinct trajectories in which it was an established failure; “—” denotes none. A single cell may contain more than one failure pattern within the same cell, so cell counts can exceed 800.

5.2  Root Causes and What They Imply Some of what we observe reflects limits of the underlying models rather than of the systems built around them, and we say so where the data shows it. Our emphasis falls on failures whose evidence is already present in the trajectory, because those are the ones where the distance between what the agent knew and what it did can be measured rather than assumed.

The root causes differ in surface form but share a common origin: the metacognitive deficit of §4. A human researcher works in a closed loop—checking whether what they produced matches what they found, acting when it does not, and questioning whether the path they took was sound. Current agents lack this loop, and each root cause is a different point where it breaks. R1 is the failure to check output against evidence. R2 is the failure to act on a flaw the agent itself identified. R3 is the failure to question whether the path to the result is legitimate. We take each in turn.

Two kinds of number appear below. A root cause’s share—such as R1’s 31.0%—is its fraction of the 12,712 total hits across the corpus. A pattern’s rate—such as D.4’s 77.5%—is the fraction of 800 analyses. Where a group of patterns is summarised together, the figure given is that group’s share of its root cause’s hit total. Notice that one trajectory usually contains more than one failure pattern.

R1. Grounding & Faithfulness (31.0% of all hits). Claims, hypotheses, and plans disconnect from the code, data, logs, or literature that should license them.

Insight 1. The evidence that would refute most failures is already in the agent’s own run directory. The agent produces both the claim and the file that contradicts it; the comparison is never performed.

R1 is led by method–conclusion disconnect (D.4, 77.5% of analyses), implementation discrepancy (C.3, 72.1%), and report–code traceability gaps (E.1, 60.5%). What these share is that the agent writes up the work it meant to do rather than the work it did—and the evidence exposing the gap sits in the same run directory the agent itself created.

Two-thirds of R1 consists of unsupported claims, in two forms. In the first, the run files say something different from the report: a conclusion is drawn that the method does not support (D.4, 77.5%), an experiment is presented as testing a hypothesis it does not test (A.6, 52.5%), or a side effect of the pipeline is reported as a finding (D.1, 52.4%). In the second, there is nothing behind the claim at all—a method section describing a procedure the code never implements (C.3, 72.1%), or a claim no run in the trajectory supports (E.1, 60.5%). The second form is the more serious, because the agent is not overstating a result but reporting work it did not do. It is also distinct from the overclaiming of R3, where the experiment was run and the conclusion reaches past it.

A further sixth is invented evidence—hallucinated sources, fabricated citations, numbers given for runs that never happened (B.1, E.4, D.6)—where nothing can contradict the claim because the thing referred to does not exist. The two groups behave differently across systems: unsupported claims appear at nearly the same rate in all eight systems, while invented evidence is much rarer in the strongest ones. The remaining is retrieval that never reaches the design (B.2, 33.9%), citations that do not support the sentence citing them (B.5, 19.0%), and right-for-the-wrong-reason success (X.6, 43.8%)—less a mechanism of its own than the outcome the other two produce.

Two consequences. Stronger models are unlikely to remove unsupported claims, because catching one requires no ability the agents lack: the report and the run directory are both products of the same agent, and all that is missing is a requirement to compare them before the report goes out. A human author checks the number in the abstract against the number in the table, and does not list a contribution they never implemented; nothing in these runs performs either check. And an evaluation that reads only the final report cannot see any of this, because the report is one half of the disagreement and the other half is on disk. That is the case for scoring the artifacts a run leaves behind rather than the answer it ends with. This is the metacognitive loop failing at the point of evaluation: the agent never compares what it produced against what it found, so the loop never begins.

R2. Cognitive Depth & Adaptability (27.6% of all hits). Shallow reasoning and search, passivity in self-critique, and inability to re-plan or pivot at a dead end.

Insight 2. The most common failure in the corpus is not missing a flaw but finding it and shipping anyway. In 82.5% of analyses the agent diagnoses a critical problem during self-review, then reports the unrevised conclusion.

This root cause is where the missing metacognitive loop of §4 is easiest to see, so it is worth stating plainly what that loop is. A researcher in difficulty does three things: recognises the limits of what they know, judges whether their intermediate results hold up, and changes the plan when they do not—then repeats. R2 is the failure of all three.

Recognising limits fails in frame-lock within a narrow hypothesis space (A.1), thin search coverage (B.4, 54.9% of analyses), and absent skepticism (X.3, 39.4%)—together 27% of R2’s hits. Judging results fails in the four self-review patterns (F.1–F.4) and in missing baselines (D.5): 62% of R2’s hits. Changing the plan fails in local optimization (C.6), stopping early (C.7), and anchoring to a failed approach (X.7): 11% of R2’s hits.

Judging results is the largest of the three, and its name is misleading, because agents do reach the right judgment. In uncorrected self-awareness (F.4, 82.5% of analyses), the most common pattern in the corpus, the agent finds the fatal flaw and writes it down, then reports the conclusion anyway.

The judgment was correct and nothing followed from it. A self-review is just more text: the same model writes it, in the same run, and nothing in the system requires the review to change the report. A human researcher who finds a broken baseline has to fix it before the paper goes out; these agents do not.

Judging results could in principle be repaired from outside the model. If the agent writes that its own result is uninterpretable, the system can refuse the report until either the result or the claim changes. Recognising limits cannot be repaired that way. When an agent never considers a second hypothesis, no second hypothesis exists in the trajectory to compare against, and nothing can flag what was never written down. This is the part that depends on the model rather than on the harness, and it is why the choice of system matters more here than in the other two root causes. Unlike R1, the metacognitive loop does fire here—the agent detects the problem—but nothing in the system closes it, so the diagnosis produces no change.

R3. Scientific Integrity & Alignment (33.5% of all hits). The agent pursues the stated goal by whatever path produces a result, whether the path is sound or not: shortcut reliance, metric hacking, concealed failure, and conclusions fixed in advance.

Insight 3. A correct-looking output is not evidence of sound methodology. Agents routinely reach the stated goal through circular validation, metric substitution, and concealed negative results—and nothing in the system distinguishes a legitimate solution from a gamed one.

R3 is the largest root cause, led by overclaiming with concealed negative results (E.2, 78.1% of analyses), circular validation and shortcut reliance (C.1, 69.0%), and metric misalignment (A.5, 68.1%). The outputs these agents produce often look correct—the numbers are plausible, the report is well-structured, but the methodology behind them is invalid, and the agent never questions whether it is.

Seventy of our hundred tasks are open-ended: the agent receives a premise and an unresolved tension, and nothing in the environment checks whether its approach is sound. Nearly half of R3 is taking shortcuts in the method: substituting a metric the agent can hit for the one the task requires (A.5, 68.1%), validating on a substrate that cannot fail (C.1, 69.0%), setting a disproof condition out of reach (A.2, 44.6%), or reasoning backward from the conclusion it intends to draw (X.5, 39.2%).

Another two-fifths is hiding what went wrong: reporting success while burying negative results (E.2, 78.1%), omitting critical limitations (E.3, 62.2%), or leaving contradictory evidence unaddressed (D.7, 60.8%). The agent is also its own reviewer, so a limitation can be written down in one section without disturbing the headline in another.

Supplying an external metric does not remove this—it changes its form. On the thirty target-anchored tasks the failure becomes grader-fitting (C.2):

moving the number without doing the work the number was meant to measure.

Both invalid trajectories of §5.3 are of this kind.

This is why R3 hardly moves when the system changes. Every system met the same open-ended setup with no external check on method quality, and every system took the same shortcuts at close to the same rate. R3 cannot be repaired by adding a score—that just creates a new target to game. What it would take is verification the agent does not control: a check applied from outside the run on whether the method supports the conclusion. In the metacognitive loop, R3 is the absence of self-questioning: even a trajectory that checks its outputs and acts on problems can still arrive at a result through an illegitimate method, because the agent never asks whether the path itself was sound.

R4. Engineering Robustness.

At 7.9% of all hits with no pattern above 26th of 45, R4 is too small to carry a contributive finding. What stands out is not how often it appears but how much it varies: some systems hit environment-interaction failures—crashes (C.5), broken shell commands (C.8), and files that never get written out (X.8)—far more often than others, while the rest of R4 is more evenly spread.

These failures depend on how the system is built, not on the task, which is also why benchmarks that supply a pre-configured environment and a known entry point [41] make execution look solved: they remove the surface where the failures concentrate.

6.  Limitations Our study has a few limitations that scope rather than undermine our findings.

First, ARFT is empirically grounded in trajectories from eight harness–model combinations on our task suite; while the stage root-cause structure is designed to generalize, we do not claim the patterns exhaust every failure an autonomous research agent can exhibit, and the task suite cannot exhaust the space of scientific research activities. The cost of annotating full research trajectories likewise bounds the number of agents and repeated runs in AutoResearchEval, so the failure-frequency statistics in §5.1 are indicative rather than exhaustive.

Second, all runs operate under fixed wall-clock and token budgets. Some failure patterns—notably premature termination and shallow search—may correlate with resource pressure. As we are not reporting failure incidence against remaining budget at this time, we cannot rule out that resource pressure contributes to these patterns.

Third, despite de-identification and temporally held-out sources, data contamination cannot be fully excluded—a constraint shared by any evaluation built on real scientific problems.

Fourth, the judge validation in §3.3 is reported in aggregate over the 50-trajectory calibration sample; we do not report per-pattern or per-pillar agreement at this time, so the pattern-level frequencies inherit an unquantified share of judge error. This is a reporting limitation of the present release, not a claim that agreement is uniform across the taxonomy.

We release AutoResearchEval in full—tasks, trajectories, annotations, and judging protocols—so the community can examine these limitations, extend ARFT, and build on the data.

8.  Conclusions and Future Work In this study, we conduct systematic investigation into why autonomous research agents fail. This investigation results in AutoResearchEval: a collection of 800 research trajectories with artifact-aware, process-level failure annotations, elicited from eight harness–model combinations on a 100-task, seven-domain suite spanning the full scientific lifecycle. To enable AutoResearchEval’s systematic annotation and analysis, we develop ARFT, the first systematic failure taxonomy for autonomous research agents, organizing 45 failure patterns on two cross-cutting axes: the lifecycle stage at which a failure manifests and its underlying root cause. For scalable annotation we develop an agent-as-a-judge annotator, validated against human expert annotation on a 50-trajectory sample (§3.3). Our analysis reveals that all three cognitive root causes converge on a single overarching limitation: current agents lack a metacognitive loop—the ability to check what they produced against what they found, act when it does not hold up, and question whether the path they took was sound.

We are excited about the potential of autonomous research agents, but their adoption in science hinges on reliability that outcome-only benchmarks cannot certify. Our work contributes toward this goal through the public release of AutoResearchEval, ARFT, the task suite, and our annotator. AutoResearchEval offers a rich empirical basis for understanding current failure dynamics, while ARFT provides a standardized language to diagnose, attribute, and mitigate these failures. Several directions follow naturally from our findings. First, our three insights suggest that artifact-aware evaluation—scoring the run directory alongside the final report—could catch failures that endpoint scoring systematically misses, and developing such evaluation protocols is a natural next step. Second, the concentration of failures in the self-verification stage (F.1–F.4 together account for 14.1% of all hits, and F.4 alone appears in 82.5% of analyses) suggests that the review stage is where interventions may yield the highest return, and studying how different review architectures affect failure rates is a promising direction. Third, while the core failure patterns are shared across all eight systems, fabrication rates vary substantially, indicating that system-specific mitigation guided by the per-model breakdowns in our appendix is underexplored. More broadly, by tracing all three cognitive root causes to a shared metacognitive deficit, our analysis identifies the metacognitive loop as a central target for next-generation language models and agentic systems working toward genuine scientific discovery.

<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# SCIRIGOR:Evaluating Open-Ended Scientific Analysis Beyond Final Scores

- **Authors:** Liu, Bowen; Nie, Shuo; Du, Bodong; Li, Xiaomeng
- **Venue / Year:** arXiv preprint · 2026
- **DOI:** 10.48550/arXiv.2609.06192
- **URL:** https://arxiv.org/abs/2609.06192
- **Bibkey:** scirigor-arxiv-2026
- **Status:** complete

## Abstract
Scientific coding agents produce interdependent code, results, figures, and claims, yet evaluating final outputs alone does not establish whether their conclusions are scientifically supported. We formulate evidence-grounded multimodal scientific analysis, requiring agents to produce executable analyses and claims supported by results and visualizations from the same run. We introduce SciRIGOR, an evaluation framework and benchmark comprising 100 cases from scientific articles across six domains and 17 subfields. The framework reconstructs typed evidence graphs, separates artifact fidelity from relational validity, and scores complete claim-support paths while localizing the earliest unsupported relation. Source-grounded alternative paths accommodate scientifically equivalent analyses and visualizations. We evaluate 11 agent/model configurations. On full-benchmark runs, claims agree with faithful and unfaithful results at nearly identical rates (91.8% versus 91.0%). Yet no system exceeds 62.6% on the soft evidence-chain score or 18.0% strict whole-chain success. These findings show that internal coherence does not establish scientific correctness: evaluation must verify support along the complete data-to-claim path.

## Full text / Extract
<!-- Verbatim key passages (method, results, limitations) extracted from the open-access arXiv full text. Tables, figures and inline math symbols were dropped during extraction; see the deep-read for the numbers. -->

3 SciRigor SciRigor evaluates scientific analysis as a connected evidentiary object. It defines what an agent must produce, reconstructs the dependencies among the executed artifacts, and scores whether each reported claim retains complete computational and visual support. This progression separates three questions that final-output scores conflate: whether an artifact is faithful to the scientific target, whether one artifact supports another, and whether those local relations compose into an end-to-end data-to-claim path.

3.1 Task Formulation We formulate evidence-grounded scientific analysis with multimodal artifacts as the post-experiment task between collected data and a reportable conclusion. Let denote a scientific question, the analysis-ready data, and the study context and measurement semantics. An agent produces four interdependent scientific artifacts: | (1) where is an executable analysis, its structured numerical results, a data-grounded visualization, and a set of atomic scientific claims. Multimodality refers to the generated visualizations and textual claims, whose support is traced through code and numerical results. The joint output makes the relations among artifacts part of the task rather than treating each artifact as an independent endpoint.

The task is executable: running over must regenerate , , and and expose provenance for evaluator verification. A successful submission covers the required findings and gives every primary claim at least one verified computational and visual support path through artifacts generated in the same run. Pre-specified, source-grounded alternatives represent scientifically valid choices of analysis method and visual encoding. Appendix A, Table 3, maps these abstract artifacts to the serialized submission contract.

3.2 Evidence-Graph Evaluation SciRigor constructs the reference support specification once, before model evaluation. Curators execute the frozen source workflow and canonicalize its consumed data views, transformations, statistical results, visual marks, and atomic findings into semantic slots. Each required claim slot is linked to at least one computational support set and one visual support set. Items within a set are jointly required, whereas separate sets represent approved alternative methods or visualizations. A final human audit verifies that the selected panel, source passage, author code, consumed data, claim scope, and support sets address the same scientific question. The resulting hidden specification determines the relations to verify without prescribing candidate filenames, identifiers, code, prose, or pixels.

At evaluation time, the submission becomes an executed dependency graph over observable scientific artifacts rather than an agent-authored reasoning trace.

The evaluator reconstructs this graph; the agent does not submit it as an additional artifact. Its core relations are | (2) where , , , , and denote data assets, transformations, statistical results, visual marks, and atomic claims. The evaluator instantiates and from runtime traces, from regenerated candidate results and independent numerical oracles, from captured plotting objects and arrays, and from structured claim records. Here the unhatted symbols denote artifact types, whereas the hatted symbols in Equation 1 denote a candidate’s realized outputs. Candidate-declared provenance and support pointers propose relations, which the evaluator verifies against these executed observations.

Primary claims require both a complete computational path and claim-relevant visual support with matching population, grouping, quantity, direction, and required uncertainty.

3.3 Artifact and Relation Verification The evaluator scores graph nodes and edges separately so that an incorrect artifact can be distinguished from an invalid dependency between otherwise plausible artifacts. Candidate artifacts are canonicalized and matched to hidden semantic slots under type and scope constraints. Transform fidelity checks data views, selectors, operation families, and parameters. Result fidelity checks the estimand, analysis unit, method family, numerical value, and uncertainty against independent recomputation. Visual fidelity checks bound arrays, encodings, groups, units, scales, and uncertainty, while claim fidelity checks direction, magnitude, population scope, inferential strength, and causal ceiling.

Edge verification follows the same executed evidence. The evaluator tests whether the observed data produced the transformation, the transformation produced the result, the rendered marks encode the same quantities, and the result and marks support the claim. Appendix A, Table 4, specifies the evidence and pass condition for every relation. Lineage, numerical recomputation, visual binding, and graph connectivity are checked programmatically. A frozen semantic matcher handles residual paraphrase and scope matching for atomic claims but cannot override a failed structured, numerical, or provenance check.

3.4 Claim-Path Scoring and Failure Localization The hidden specification represents accepted method families, visual encodings, and claim-support rules as semantic constraints rather than a single gold program or image. Let and denote the accepted computational and visual support paths for claim , and let each verified node or edge item have score . SciRigor computes | (3) where is local claim fidelity. The inner minimum applies the weakest-link rule to one path, and the outer maximum admits any complete, approved alternative. Generated claims are matched one-to-one to required claim slots, and their verified support mass yields evidence-chain precision, recall, and F1. Strict evidence-chain success requires execution, complete support for every required claim, no unsupported primary claim, and satisfaction of all hard visual constraints. Artifact fidelities, edge pass rates, and an execution-gated soft chain aggregate provide complementary diagnostic views.

For an incomplete chain, SciRigor reports the earliest topological layer from which no accepted partial path can reach the claim: contract/execution, Data Transform, Transform Result, Transform/Result Visual, or Result/Visual Claim. An incomplete path does not determine the score when another independently verified path remains complete, while downstream presentation quality cannot repair an upstream scientific error.

4 SciRigor Benchmark The SciRigor benchmark instantiates the evaluation framework with 100 evidence-complete, figure-level cases from 27 empirical articles. Each case aligns a scientific question with all code-consumed inputs, an executable source analysis, numerical results, a source visualization, atomic findings, and provenance within one experimental scope. We construct this alignment through source discovery, evidence closure, standardized task assembly, executable reproduction, and final human audit (Fig. 1).

benchmark only after figure-level evidence closure, task standardization, two clean reconstructions, and expert audit. The agent-visible task is separated from evaluator-side gold artifacts, scoring constraints, and support paths.

4.1 Source Discovery and Evidence Closure We searched open-access quantitative studies for figures accompanied by public source data and author-released plotting code. Discovery combined a Europe PMC search of the Nature and Science main journals with audited Nature Portfolio and other open-access sources. For each candidate, automated indexing connected in-text figure references with full-text passages, supplements, Data Availability statements, repository records, and exposed source-data links.

These links formed a review queue; admission depended on evidence completeness rather than publication venue (Appendix B).

An admitted case contains four mutually aligned source components: an author-generated quantitative figure from an auditable paper version; a bounded Results passage that describes and interprets the selected figure or panel; the complete author-released script or notebook that generates that target; and every raw, processed, or intermediate file consumed by its entry point. The plotting program must have a stable source locator, and every data dependency must be publicly retrievable and freezeable. Together, these requirements tie the visual target, experimental interpretation, executable analysis, and inputs to the same scientific question.

Evidence closure required two clean executions of the frozen author entry point against the complete inputs. The reproduced quantities, visual marks, groups, units, and uncertainty encodings had to agree with the paper figure and its analysis. Each accepted case covers one figure or one coherent panel subset, and its question, passage, code, inputs, and findings are bounded to that scope. The visual reference is an original source raster or an audited source-pixel crop.

Missing dependencies, unrecoverable semantics, or substantive disagreement led to exclusion under the rules detailed in Appendix C.

4.2 Task Construction and Standardization Each closed source bundle became a self-contained task without answer-bearing content. We retained an explicit paper question when it matched the selected figure scope; otherwise, curators wrote a neutral question bounded to the experiment. The visible package contains the question and study context in the task specification together with the declared analysis-ready data. Source references, gold artifacts, construction metadata, and scoring rules remain evaluator-side. Appendix D specifies the question, visibility, storage, and serialized interface.

Standardization began after source closure. GPT-5.6 assisted with locating target-specific operations, drafting neutral task descriptions, mapping heterogeneous tables into documented assets, and proposing source-grounded Python translations and structured records. Curators verified every proposal against the frozen author workflow and retained unchanged author code for audit.

Original Python operations were preserved; non-Python workflows were translated into Python ports that retained source selectors, transformations, estimators, scales, uncertainty layers, and plot structure. Execution and visual-semantic comparison validated each port before case admission.

4.3 Executable Quality Control Every assembled case ran twice in an isolated environment containing only its executable reference analysis and declared inputs. Both runs had to terminate successfully, regenerate the required results, visualization, and claims, support provenance reconstruction, consume only declared assets, and agree under a deterministic or explicitly tolerance-bounded contract. Structured hidden constraints were then checked against the regenerated numerical results, visual semantics, data bindings, and atomic-claim support. All 100 released cases passed both clean reconstruction runs.

Curators completed a final audit of question clarity, answer leakage, reference fidelity, scoring-constraint coherence, and alignment among the selected panel, source passage, author code, consumed data, and claims. Unresolved scope, provenance, or support discrepancies triggered revision or exclusion. This construction-time audit fixes the hidden reference and support rules, enabling routine model submissions to be scored automatically. Candidate methods outside the frozen alternatives enter expert adjudication; accepted alternatives are added to the support specification before rescoring. Appendix E provides the complete execution, asset, and review protocol.

4.4 Benchmark Composition

multi-artifact task complexities. (a) The 100 cases span six reporting domains and 17 disciplinary subfields. The taxonomy ring assigns equal angular width to every subfield, while each inner domain spans the subfields it contains.

(b) Cases require multiple input assets, result slots, visual requirements, and atomic claims, creating long evidence chains. (c) Method families are multi-label across domains; cells report case counts, and darker color denotes greater within-domain prevalence.

The release covers six reporting domains defined by the primary scientific subject of each source study: economics and policy (24 cases); computing and information sciences (23); social and behavioral sciences (22); cognitive science (15); life and health sciences (9); and physical sciences (7).

Multiple cases may originate from one article because the benchmark unit is a bounded figure-level question. The released metadata records the complete case-to-subfield mapping shown in Fig. 2a.

The cases vary in the number of input assets, required result slots, visual requirements, and atomic claims, producing evidence chains of different lengths (Fig. 2b). Analysis methods are multi-label:

descriptive aggregation appears across all domains, physical sciences contain more regression, model-fitting, and inferential checks, cognitive science contributes trajectory, similarity, and classification analyses, and economics/policy contains many distribution and inequality computations (Fig. 2c). These distributions describe coverage rather than model performance. They reflect the availability of figure-specific public code and complete code-consumed data, not a probability-balanced sample of the scientific literature.

Execution remains a substantive bottleneck.

Execution gates every downstream scientific score. Kimi-K3 executes 79.0% of its assigned cases, Qwen3.8-Max executes 47.0%, Qwen3-Coder-30B-A3B reaches 29.0%, and Qwen-AgentWorld-35B-A3B reaches 12.0%. Scores computed only over successful outputs would therefore conflate scientific quality with selective completion.

Candidate self-consistency can mask scientific error.

Across all 11 rows, R C is the highest or second-highest displayed score, while result and claim fidelity are substantially lower for several high-execution runs. GPT-5.6 (low), for example, obtains 97.9% Result Claim consistency but only 47.2% result fidelity and 52.5% claim fidelity. Its claims therefore tend to agree with its own reported results even when those results depart from the scientific target. Candidate self-consistency is necessary for a coherent submission but is not sufficient evidence of scientific correctness.

Partial success collapses under chain composition.

The strongest run reaches 62.6% SoftECS but only 18.0% Strict success. Kimi-K3 falls from 79.0% execution to 35.0% SoftECS and 1.0% Strict success. These gaps show that disconnected artifact averages are insufficient: a submission can accumulate several locally successful components without completing a single fully supported data-to-claim path. Fidelity and edge consistency should be reported separately before applying an end-to-end chain gate.

5.2 Error Analysis

(a) Earliest failure stage among the 936 trajectories that do not complete a strict chain. Each trajectory contributes to exactly one stage.

(b) Overlapping artifact- and edge-level errors among the 718 successfully executed trajectories; values are percentages within each model’s executed cases. (c) Local Result Visual and Result Claim consistency conditioned on independent result fidelity.

We diagnose failures from three complementary views: the earliest broken stage, the full set of artifact and edge errors after successful execution, and whether local consistency distinguishes faithful from unfaithful results. These labels are produced by the evaluator and may overlap in Fig. 3b; they describe observable failure signatures rather than assigning a unique causal explanation to a trajectory.

Most chains break before a faithful result is established.

Among 936 non-strict trajectories, 48.2% first fail in data selection or transformation and 30.1% fail at the artifact contract or execution gate (Fig. 3a). Result computation accounts for a further 11.9%, whereas visualization, claims, and provenance together account for only 9.8% of first failures. Thus, late-stage errors are visible, but the dominant bottleneck is establishing a valid computational basis for downstream evidence.

Scientific errors persist after execution succeeds.

Conditioning on the 718 executed trajectories removes mechanical non-completion from the comparison. Transform fidelity fails in 59.6% of these trajectories, result fidelity in 49.3%, and claim fidelity in 47.9% (Fig. 3b). By contrast, Result Claim consistency fails in only 8.6%. The model-level heatmap shows that this gap is not confined to a single run: systems frequently propagate their own intermediate values coherently even when those values do not match the scientific target.

Local self-consistency is nearly invariant to result correctness.

Result Claim consistency passes on 91.8% of result-faithful trajectories and 91.0% of result-unfaithful trajectories (Fig. 3c). Result Visual consistency is more sensitive, but still passes on 82.2% of trajectories with unfaithful results, compared with 97.3% when results are faithful. A candidate can therefore explain and visualize its own result without establishing that the result is correct. This case-level conditional analysis confirms that cross-artifact coherence is necessary but cannot replace independent fidelity checks.

5.3 Complexity Sensitivity

Points show bin means; error bars denote SEM across cases.

Strict RG-EC decreases with more input assets, required result slots, and visual requirements; RG-EC F1 also declines with assets and result slots, while the gated-claim composite is flatter. RG-EC F1 gates claim coverage by verified numerical support, whereas Strict RG-EC requires complete support for every required and generated claim.

Fig. 4 shows that complexity primarily affects chain completeness rather than surface claim plausibility. Moving from one input asset to at least five lowers Strict RG-EC from 45.7% to 25.0% and RG-EC F1 from 70.9% to 57.8%, whereas the gated-claim score drops from 71.7% to 63.7%. Required result slots show the same pattern: Strict RG-EC decreases from 43.9% to 30.8% and RG-EC F1 from 68.4% to 55.7%, while the gated-claim score remains nearly unchanged. This divergence supports scoring result-grounded claim paths rather than final claims alone. The highest visual-requirement bin contains only three cases and is therefore a stress-test signal, not a standalone estimate.

5.4 Evaluation Scope The experiments score observable artifacts submitted through the five-file interface. The evaluator reconstructs their semantic relations but does not observe latent reasoning or agent action trajectories. The results therefore compare artifact fidelity and complete evidence paths and localize observable breaks; they do not identify whether a failure arose from planning, implementation, or unsupported generation.

6 Conclusion SciRigor formulates evidence-grounded scientific analysis with multimodal artifacts around a verified data-to-claim support path. Its evaluation framework separates artifact fidelity from cross-artifact consistency, reconstructs computational and visual dependencies, accepts source-grounded alternative paths, and localizes the earliest unsupported relation. The benchmark’s 100 evidence-complete, figure-level cases align questions, inputs, source analyses, results, visualizations, findings, and provenance within one audited scope. Across 11 agent/model configurations, high execution or Result Claim consistency can coexist with much lower target fidelity, and strict chain completion remains rare. Across the ten complete 100-case runs, 78.3% of failed trajectories first break at the contract/execution or data/transformation stage; among executed trajectories, Result Claim consistency passes at nearly the same rate for faithful and unfaithful results (91.8% versus 91.0%).

Together, these results support the paper’s central evaluation principle:

execution, visual plausibility, final-output similarity, and candidate self-consistency are not substitutes for independently verified relations from supplied data to each reported claim.

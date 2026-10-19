# SCIRIGOR: Evaluating Open-Ended Scientific Analysis Beyond Final Scores

> **Bibkey** `scirigor-arxiv-2026` · **Venue** arXiv preprint (2026) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2609.06192> · `status: complete`

---

## One-liner
SciRigor reconstructs a scientific-analysis agent's outputs (code, structured results, a figure, atomic claims) as a **typed evidence graph**, requires every primary claim to keep a complete, same-run verifiable "data → transform → result → visual/claim" support path, scores it by weakest link and localises the earliest broken edge. On 100 figure-level cases from Nature and other journals, agents' claims agree with their own results at nearly the same rate whether those results are right or wrong (91.8% vs 91.0%), and the best system achieves only 18.0% strict whole-chain success.

## Problem
Scientific coding agents now run long-horizon open-ended analyses producing interdependent code, numbers, figures and conclusions. Existing benchmarks score code/execution, workflow delivery, or figures/claims in isolation — none asks: **is a newly generated claim actually supported by the data, computation and visualisation produced in the same run?** Typical failure: a regression stores an estimate and CI on a log scale; the agent back-transforms only the estimate and writes a correct-looking "18.0% increase (95% CI 12.6–23.6%)" while its structured interval and plotted band stay on the wrong scale. Final-output scoring accepts such "right sentence, wrong evidence", while exact-reference matching rejects defensible alternative analyses.

## Method
**Task**: given a question, analysis-ready data and study context, the agent must produce four interdependent artefacts — executable analysis code, structured numerical results, a data-grounded visualisation and atomic claims; re-running the code must regenerate results, figure and claims and expose provenance. Success = required findings covered + every primary claim has at least one verified computational and visual support path. **Evidence-graph evaluation**: at construction, curators execute the frozen author workflow and canonicalise data views, transforms, statistical results, visual marks and atomic findings into semantic slots; each claim slot links to ≥1 computational and ≥1 visual support set (items within a set jointly required; separate sets are approved alternative methods/encodings), human-audited. At evaluation, the evaluator **reconstructs** the candidate graph from runtime traces, regenerated results with independent numerical oracles, captured plotting objects/arrays and structured claim records (the agent does not submit the graph); nodes (artifact fidelity: transform / result / visual / claim) and edges (data→transform→result, result↔visual, result/visual→claim) are scored separately. Lineage, numerical recomputation, visual binding and connectivity are checked programmatically; a frozen semantic matcher handles only paraphrase/scope matching and cannot override a failed structural, numerical or provenance check. **Scoring**: minimum within a path (weakest link), maximum across approved complete paths; reports evidence-chain precision/recall/F1, an execution-gated SoftECS, and Strict (execution + complete support for every required claim + no unsupported primary claim + all hard visual constraints). Incomplete chains report the earliest broken layer: contract/execution, Data→Transform, Transform→Result, Transform/Result→Visual, Result/Visual→Claim.

## Data
100 evidence-complete figure-level cases from 27 empirical articles (Nature and Science main journals via Europe PMC, plus Nature Portfolio and other open-access sources), spanning 6 domains and 17 subfields: economics & policy 24, computing & information sciences 23, social & behavioural 22, cognitive science 15, **life & health sciences 9**, physical sciences 7. Admission requires an author-generated quantitative figure + its Results passage + complete author-released plotting script/notebook + every consumed data file; two clean reproductions agreeing with the paper figure; non-Python workflows ported to Python (GPT-5.6-assisted, curator-verified). Eleven agent/model configurations evaluated (GPT-5.5 / GPT-5.6 / GPT-5.6-Sol at several reasoning levels, Claude Sonnet 5, Kimi-K3, Qwen3.8-Max, Qwen3-Coder-30B-A3B, Qwen-AgentWorld-35B-A3B).

## Key results

- **Best is only 18.0% strict**: GPT-5.5 (xhigh) executes 100%, SoftECS 62.6%, Strict 18.0%; GPT-5.5 (high) 16.0%; GPT-5.6-Sol (high) 13.0%; others ≤11%, with Claude Sonnet 5, GPT-5.6 (low) and two small Qwen models at 0.
- **Execution is itself a bottleneck**: Kimi-K3 executes 79.0%, Qwen3.8-Max 47.0%, Qwen3-Coder-30B-A3B 29.0%, Qwen-AgentWorld-35B-A3B 12.0%; Kimi-K3 falls from 79.0% execution to 35.0% SoftECS and 1.0% Strict.
- **Self-consistency masks error**: Result→Claim consistency is the highest or second-highest score in all 11 rows; e.g. GPT-5.6 (low) has 97.9% Result→Claim consistency but only 47.2% result fidelity and 52.5% claim fidelity.
- **Consistency is nearly independent of correctness**: Result→Claim consistency passes on 91.8% of result-faithful and 91.0% of result-unfaithful trajectories; Result→Visual is more sensitive but still passes 82.2% with unfaithful results (97.3% faithful).
- **Chains break upstream**: of 936 non-strict trajectories, 48.2% first fail at data selection/transformation, 30.1% at the contract/execution gate, 11.9% at result computation, and only 9.8% at visualisation + claims + provenance (78.3% at execution or data/transform). Among 718 executed trajectories, transform fidelity fails 59.6%, result fidelity 49.3%, claim fidelity 47.9%, while Result→Claim consistency fails only 8.6%.
- **Complexity**: for GPT-5.6-Sol (xhigh), going from 1 to ≥5 input assets lowers Strict from 45.7% to 25.0% and F1 from 70.9% to 57.8%, while a claims-only score drops only from 71.7% to 63.7% — complexity hurts chain completeness, not surface claim plausibility.

## Contributions
- **The scored object is a verified data-to-claim support path**, not a program, stage or final output.
- **Separates artifact fidelity from edge validity**: distinguishes "the artefact is wrong" from "the dependency between artefacts does not hold".
- **Weakest-link + alternative paths**: downstream polish cannot repair an upstream error, while scientifically equivalent methods and visual encodings are admitted.
- **Localises the earliest broken edge**, attributing failure to a specific evidence layer.
- Builds "evidence-complete" cases from figure-level reproductions with author code + data, each passing two clean reproductions and human audit.

## Limitations
- Scores observable artefacts only — not reasoning or action trajectories — so it cannot tell whether a failure stems from planning, implementation or unsupported generation.
- Case distribution reflects availability of figure-level public code + complete data, not a balanced sample; life & health sciences contribute only 9 cases, with little omics-style analysis.
- Methods outside the frozen alternatives require expert adjudication; automated scoring may still be too strict for genuinely novel analyses.
- One run per configuration, no rerun variance reported; no code or data link is given in the paper.

## Relation to our direction
The closest evaluation framework to **Plan B's claim-to-evidence verification** for computational analysis — nearly a template for Plan B's evaluation design. Plan B asks precisely whether what a kidney-omics agent says is supported by the data and computation it actually produced; SciRigor formalises this as an evidence graph + weakest link + earliest broken edge. Directly transferable: **(1) evidence-graph node types** (data assets / transforms / statistical results / visual marks / claims) map onto omics steps: QC filtering → normalisation → clustering/annotation → DE / spatial statistics → figure → conclusion; **(2) quantitative evidence that self-consistency ≠ correctness** (91.8% vs 91.0%) means Plan B's verifier cannot just check internal consistency of a report — it needs independent numerical recomputation (oracles); **(3) failures concentrate in data selection/transformation (48.2%)** — matching where omics analyses most often go wrong (cell filtering, batch correction, normalisation, sample grouping), a natural upstream class for the omics-specific failure taxonomy; **(4) the alternative-path mechanism** handles omics' "multiple defensible pipelines" (different normalisations, clustering resolutions). For **Plan A**, if KidneyAnomalyBench asks agents for "anomalous regions + claims", it should likewise require re-runnable, traceable evidence paths. Gaps: SciRigor has no omics/spatial data, only 9 life-and-health cases, and no rerun-stability evaluation — exactly what Plan B (kidney omics + rerun stability) can supply.

## Reusable assets
- **Evaluation design:** typed evidence graph (Eq. 2), weakest-link / max-over-paths scoring (Eq. 3), earliest-failure layers, submission contract (Appendix A, Tables 3–4).
- **Case-construction protocol:** evidence closure (figure + passage + author code + all data), two clean reproductions, human audit (Appendices B–E).
- No code/data repository link is given; watch for a release.
<https://arxiv.org/abs/2609.06192>

## Follow-ups
- ScienceAgentBench, BLADE, DiscoveryBench, FIRE-Bench, DataSciBench — the comparator benchmarks.
- FactReview (auditing paper claims with literature + execution evidence) and SciVisAgentBench.
- This repo's `bixbench-arxiv-2025`, `scbench-arxiv-2026` — is there an analogous evidence-chain evaluation for bioinformatics / single-cell?

## Cite
```bibtex
@misc{scirigor-arxiv-2026, title={SCIRIGOR:Evaluating Open-Ended Scientific Analysis Beyond Final Scores}, author={Liu, Bowen and Nie, Shuo and Du, Bodong and Li, Xiaomeng}, year={2026}, eprint={2609.06192}, archivePrefix={arXiv}, primaryClass={cs.AI}, url={https://arxiv.org/abs/2609.06192}, doi={10.48550/arXiv.2609.06192} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

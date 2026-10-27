# Why Your Deep Research Agent Fails? On Hallucination Evaluation in Full Research Trajectory

> **Bibkey** `Zhan2026_260122984` · **Venue** arXiv preprint (2026) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2601.22984> · `status: complete`

---

## One-liner
Shifts from final-report evaluation to auditing the whole plan–search–summarize trajectory: the **PING taxonomy** (Propagation, Intent, Noise-induced, Grounding) classifies deep-research-agent (DRA) hallucinations by locus of failure, an evaluation framework decomposes trajectories into atomic actions/claims/sub-queries, and 100 hallucination-prone queries form **DeepHalluBench**. None of six DRAs is uniformly low-hallucination; failures trace to **hallucination propagation** and cognitive biases — the temporal "Anchor Effect" and semantic "Homogeneity Bias".

## Problem
Existing DRA benchmarks are either closed-ended with ground-truth answers (GAIA, BrowseComp) or open-ended long-report evaluations against reference reports/rubrics — **almost all outcome-oriented, treating the research process as a black box**. Two consequences: (1) intermediate hallucinations (e.g. misleading plans) are only partly detected; (2) failures cannot be attributed to stages. Three obstacles to process-aware evaluation: no DRA-specific hallucination taxonomy; proprietary DRAs lack affordable APIs or structured logs; multi-stage trajectories are hard to evaluate consistently.

## Method
**PING taxonomy** (the search engine is an external source; only LLM-induced hallucinations at plan and summarize stages are scored): **Grounding** (source level) = fabrication (no evidence in the trajectory) + misattribution (cited documents don't support it, though other retrieved ones might); **Noise-induced** (context level) = relevant retrieved evidence left unused; **Intent** (query level) = restriction neglect (e.g. ignoring "full-time") + deviated actions; **Propagation** (trajectory level) = later actions built on earlier hallucinated content. **Data acquisition**: custom HTML parsers + LLMs reconstruct web-UI traces into structured plan–search–summarize loops, manually checked against rendered HTML. **Evaluation**: two-round claim verification (retrieve-then-verify via an NLI→LLM cascade; unsupported claims get misattribution/reflection checks); the noise score clusters retrieved chunks semantically, ranks them by relevance, and penalizes large, high-ranked clusters skipped while lower-ranked ones are used, P_c = S_c × N_inv / R_c, normalized by a worst case; action verification uses history plus Claim Memory to flag deviation and propagation; restriction checking treats sub-queries as atomic restrictions and uses an elbow rule to decide which were addressed. **Reliability**: claim verification 95.2% on FEVER and 87.3% on SciFact-Open; a two-annotator audit of 20 trajectories (~8,800 atomic units) with raw κ = 0.83.

## Data
**DeepHalluBench**: 100 queries, half open- and half closed-ended. Candidates pooled from Mind2Web2, ReportEval and BrowseComp; two open-source DRAs (gpt-researcher, MiroThinker) generate full trajectories as probes; the 75 with the highest average hallucination score (25 per source) are kept; **25 adversarial "no-answer" queries** are synthesized by atomic perturbations of solvable closed-ended queries (e.g. altered temporal constraints) and manually verified as unsolvable. Systems: five proprietary DRAs (Gemini, OpenAI, Perplexity, Qwen, Grok) plus open-source Salesforce Deep Research.

## Key results
**Six metrics (Table 2, lower is better)**: fabrication highest for Grok (0.1509) and OpenAI (0.1463), lowest for Perplexity (0.0978); misattribution highest for Salesforce (0.2136) despite little fabrication; noise highest for Grok (0.4813) and Perplexity (0.3905), lowest for Salesforce (0.0988, narrower retrieval, less context competition); restriction neglect lowest for OpenAI (0.0416), highest for Salesforce (0.2847); propagation rare overall (0.0021–0.0176). Grok exposes no planning trace, so only observable metrics are scored. **Closed-ended (50 queries, two runs each)**: three profiles — **over-confidence** (Gemini, Grok: 0.00 / 0.08 on no-answer queries, failing to reject), **over-conservatism** (Salesforce, Qwen: 0.80 / 0.72 on no-answer queries but 0.00 on answerable ones), **balanced struggle** (OpenAI at 0.28 on all three, Perplexity); the two runs differ on at most 3 of 50 queries per DRA. **Mechanisms**: for Gemini and OpenAI >57% of source errors occur early (early cascading); Salesforce has >40% of errors late (long-context collapse); on closed-ended queries, intermediate summarization fabrication frequently precedes wrong final answers; in hallucination-free trajectories the open-source DRA refuses while proprietary DRAs fabricate an answer. **Cognitive biases**: "Anchor Effect" — utilized chunk counts collapse in later stages even when later retrieval quality improves; "Homogeneity Bias" — at comparable relevance, small clusters are ignored more than large ones in every DRA (Δ 0.064–0.124). The patterns persist with a stronger backbone.

## Contributions
- PING: a DRA hallucination taxonomy organized by locus of failure (source/context/query/trajectory), bringing evidence neglect and error propagation into scope.
- A parser pipeline reconstructing proprietary DRA trajectories from web UIs — overcoming the "no logs, no process evaluation" barrier.
- Adversarial "no-answer" queries directly measure whether agents reject unsolvable tasks, separating over-confidence from over-conservatism.
- Maps hallucinations into a DAG for root-cause and temporal analysis; identifies the Anchor Effect and Homogeneity Bias.

## Limitations
- Diagnoses where in the workflow hallucinations arise, not their intrinsic parametric causes in the backbone.
- Text trajectories only; multimodal web content not covered.
- Atomic evaluation trades scale for depth and is costly; the 100-query benchmark is a stress test selected for hallucination-proneness, not an average-case sample.
- Parsed trajectories are observable proxies of provider-exposed processes, not true internals; Grok lacks planning traces; the four dimensions are heterogeneous and not summable.

## Relation to our direction
This is **the process-level framework Topic 2's omics-specific failure taxonomy should benchmark against**. An agent analysing kidney omics runs the same plan (choose QC thresholds, clustering resolution, comparison groups) – act (run code) – summarize (write conclusions) loop, and PING maps one-to-one: **Grounding** → conclusions that contradict the agent's own outputs or cite the wrong artefact; **Noise-induced** → computed-but-ignored key results (e.g. skipping snATAC–snRNA disagreement — exactly the cross-modal signal Topic 1 uses to separate artefact from disease); **Intent** → ignoring user restrictions (PT cells only, DKD samples only) or silently changing the question; **Propagation** → early errors (wrong cell annotation, uncorrected batch effects) inherited by every later step. Three things to borrow: (1) **adversarial no-answer tasks** — add tasks to KidneyAnomalyBench / Topic 2 where the signal simply isn't in the data (e.g. asking for the disease mechanism of a pure-artefact region) to test whether the agent declines; (2) **early cascading** says the verifier should checkpoint early steps (QC, annotation), not only the final report; (3) reporting that two runs differ on at most 3/50 queries is a minimal template for Topic 2's rerun-stability measurement. The Anchor Effect and Homogeneity Bias also warn that agents favour early, abundant evidence, so signals from rare cell states or small lesions are the most likely to be ignored — precisely what anomaly detection cares about.

## Reusable assets
- **Code and data (DeepHalluBench):**
<https://github.com/yuhao-zhan/DeepHalluBench>
- **Metric formulas:** H_G (Eqs. 1–2), H_N noise penalty (Eqs. 3–4), H_P (Eq. 5), H_I (Eqs. 6–7).
- **Benchmark construction recipe:** multi-probe selection of hallucination-prone queries + atomic perturbation to synthesize unsolvable ones.
- **Verifier validation:** FEVER and SciFact-Open as external calibration sets for the claim-verification module.

## Follow-ups
- TRACE (Chen et al., 2026) and MiroEval (Ye et al., 2026): other process-aware DRA evaluations.
- Hao et al. (2025) on intent hallucination; Ma et al. (2024) on fact omission in RAG — the origins of PING's Intent and Noise categories.
- Appendix D.2 (backbone ablation) and E.1 (propagation DAG construction).
- Read with mast-neurips-2025 and trail-arxiv-2025 (multi-agent / trace failure taxonomies) in this repo.

## Cite
```bibtex
@misc{Zhan2026_260122984,
  title = {Why Your Deep Research Agent Fails? On Hallucination Evaluation in Full Research Trajectory},
  author = {Yuhao Zhan and Tianyu Fan and Linxuan Huang and Zirui Guo and Chao Huang},
  year = {2026},
  eprint = {2601.22984},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2601.22984}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

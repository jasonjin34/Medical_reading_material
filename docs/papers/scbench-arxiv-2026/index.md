# scBench: Evaluating AI Agents on Single-Cell RNA-seq Analysis

> **Bibkey** `Workman2026_260209063` · **Venue** arXiv preprint (2026) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2602.09063> · `status: complete`

---

## One-liner
scBench (LatchBio) is 394 **deterministically graded** scRNA-seq analysis problems: each gives a real data snapshot taken just before an analysis step, a natural-language task and a grader, across 6 sequencing platforms × 7 task categories. Eight frontier models under one harness reach only 29–53%, and **platform matters as much as model** (40+ pp drops on less-documented platforms).

## Problem
Existing biology benchmarks test recall, interpretation or literature-style reasoning without requiring empirical interaction with data or reflecting real analysis steps, so there is no standard, deterministic yardstick for data-grounded scRNA-seq analysis. Can frontier agents reliably recover the key biological result from messy real data?

## Method
**Problem construction** (following SpatialBench): keep only steps that occur in routine practice, whose answer depends on the provided data (not textbook knowledge or memorised gene lists), and whose result is a deterministically gradable JSON artifact. Five stages: reproduce the step with the published workflow → define an exact JSON schema → pick a grader family → **calibrate tolerances** by running multiple valid methods/parameters → **harden against shortcuts** (remove precomputed embeddings, cached labels). A final check tries to "cheat" three ways — read .obs/.uns directly, answer from priors, use an alternative valid method — and revises or removes problems that fail. **Evaluation types**: scientific (goal only, widest tolerances), procedural (method named, tighter), observational (report a data property). **Five grader families**: NumericTolerance, MultipleChoice, MarkerGenePrecisionRecall, LabelSetJaccard, DistributionComparison (every category must pass, so rare cell types cannot be ignored). Principle: "specify what, not how"; seed-sensitive outputs (exact cluster counts) and version artifacts (UMAP coordinates) are deliberately avoided. **Harness**: all models under mini-SWE-agent (first fenced code block executed in bash), 100-step cap, 300 s per command, 600 s per evaluation, no retries; 3 replicates per model–problem, two-stage aggregation with t-distribution 95% CIs.

## Data
394 problems; platforms: BD Rhapsody 61, Chromium 60, CSGenetics 42, Illumina 85, MissionBio 81 (Tapestri targeted DNA+protein, a cross-modality stress test), ParseBio 65 (no QC). Tasks: QC 36, normalisation 44, dimensionality reduction 69, clustering 49, cell typing 118, differential expression 71, trajectory 7. Thirty canonical problems (5 platforms) are public with full agent trajectories; the full suite is **withheld** to prevent training contamination.

## Key results
**Overall**: Claude Opus 4.6 **52.8%** (95% CI 48.3–57.2), Opus 4.5 49.9%, GPT-5.2 45.2%, Sonnet 4.5 44.2%, GPT-5.1 37.9%, Grok-4.1 35.6%, Grok-4 33.9%, Gemini 2.5 Pro **29.2%**; a 23.6 pp best–worst spread. GPT-5.2 is near the accuracy–cost Pareto front. **By task**: normalisation easiest (cross-model mean 70.4%), QC 55.3%, clustering 38.3%, cell typing 34.9%, differential expression hardest (27.0%, and most discriminative at 27.7 pp); 7 of 8 models share the same difficulty order. **By platform**: cross-model means range from CSGenetics 59.1% to MissionBio 26.4% — **a 32.7 pp platform gap exceeding the 23.6 pp model gap**; MissionBio is hardest for every model and inverts rankings; Gemini drops from 52.4% (CSGenetics) to 10.3% (MissionBio), and even the most consistent model (Opus 4.5) swings 39 pp. **vs. SpatialBench**: under the same harness spatial is harder (top 38.4% vs. 52.8%), but rankings agree at both ends.

## Contributions
- A full problem-engineering recipe — **deterministic grading + tolerance calibration + anti-shortcut hardening** (five-stage construction, three cheat checks, a linter) — directly transferable to other omics.
- Platform × task stratification revealing "platform effect ≥ model effect," pointing to uneven training-data coverage and brittle memorised techniques.
- One shared harness, three replicates, two-stage CIs — statistical discipline rare in agent evaluation.
- Together with SpatialBench, a paired diagnostic for the two dominant transcriptomic modalities.

## Limitations
- Self-reported: deterministic grading discretises scientific judgement into checkable chunks; each problem snapshots a **single** step, missing long-horizon iteration where errors compound (scBench-Long addresses this).
- Evaluates models in one minimal harness, not specialised biology agents (Biomni etc.); no temperature/seed control, so replicates reflect sampling noise only.
- The full suite is private, so problem quality cannot be independently audited; only 7 trajectory tasks; MissionBio is not RNA-seq yet counts in the aggregate.
- Grades only the final JSON, not whether intermediate steps were sound ("right answer, wrong reason" is possible).

## Relation to our direction
For **Plan B** this is the paper whose methodology to copy most directly: building a trustworthiness evaluation for agents that analyse kidney omics requires turning analysis steps into verifiable problems, and scBench gives the full recipe — reproduce → JSON schema → grader family → calibrate tolerances with multiple valid methods → strip shortcut fields → three cheat checks. These transfer directly to kidney problems (QC thresholds, PT subtype calling, injury-state marker DE on KPMP/Lake/in-house snRNA). Two findings matter for us: **(1) platform effect ≥ model effect** — our data span snRNA, snATAC and Xenium, and we should expect large drops on less-documented modalities like Xenium/snATAC, itself a dimension of an omics-specific failure taxonomy; **(2) DE and cell typing are hardest and most discriminative** — exactly the steps that "anomalous cell state" calls depend on. For **Plan A**, DistributionComparison's "every category must pass; rare cell types cannot be ignored" rule matches KidneyAnomalyBench's need to keep rare disease states from being averaged away, and the scientific/procedural/observational split can stratify an expert-annotated anomaly benchmark. Note it grades only final answers; Plan B's claim-to-evidence checking and rerun stability are precisely what it leaves uncovered.

## Reusable assets
- **Code:** evaluation framework, graders, linter, agent harness; 30 public problems with full trajectories; pluggable custom agents.
<https://github.com/latchbio/scbench>
- **Grader specs:** formal definitions of the five grader families (Appendix C), reusable for kidney tasks.
- **Statistical design:** two-stage aggregation with t-distribution CIs.

## Follow-ups
- SpatialBench (Workman et al., 2025): the spatial version, most relevant to our Xenium data.
- scBench-Long (`scbench-long-arxiv-2026`): the long-horizon, claim-level follow-up.
- The mini-SWE-agent harness; and scores of specialised agents (Biomni, SpatialAgent) on scBench, if reported.

## Cite
```bibtex
@misc{Workman2026_260209063,
  title = {scBench: Evaluating AI Agents on Single-Cell RNA-seq Analysis},
  author = {Workman, Kenny and Yang, Zhen and Muralidharan, Harihara and Abdulali, Aidan and Le, Hannah},
  year = {2026},
  eprint = {2602.09063},
  archivePrefix = {arXiv},
  primaryClass = {q-bio.GN},
  url = {https://arxiv.org/abs/2602.09063}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

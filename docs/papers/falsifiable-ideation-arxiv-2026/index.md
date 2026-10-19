# What Proves You Wrong: Benchmarking Language Models on Falsifiable Research Ideation

> **Bibkey** `falsifiable-ideation-arxiv-2026` · **Venue** arXiv preprint (2026) · **Category** agents · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2608.22948> · `status: complete`

---

## One-liner
Lit2Test requires every research proposal to follow a six-field contract — literature_gap, hypothesis, minimal_test, decisive_metric, supporting_result, falsifying_result — i.e. to **precommit the observation that would prove it wrong**, making proposal quality decidable rather than arguable. Across 200 real-paper neighbourhoods and 1,200 pairs judged blind in both orders, it recovers a strict ranking of four frontier models in all 10,000 bootstrap replicates, with separation driven by minimal-test and decisive-metric design rather than fluency.

## Problem
Both prevailing paradigms for judging LLM research ideas lack a shared decision rule: **free-form LLM judging** sways with style and presentation position; **future-paper-as-answer** scoring rewards recovery of one realised trajectory, penalises valid alternatives and invites knowledge-cutoff contamination. The authors argue a proposal becomes adjudicable only when it **states in advance what result would reject it**. Can falsifiability be made the evaluation unit, with a protocol that audits its own reliability?

## Method
**Instance**: a real four-paper "neighbourhood" sharing a topic but leaving a cross-paper tension (e.g. ALR2 vs ChatQA 2 on long-context QA); every model gets the same fixed context and no future paper is designated the correct continuation. **Six-field contract**: remove any field and a pairwise verdict loses its common decision structure; `minimal_test` carries an anti-grandiosity clause rewarding small, executable designs; `supporting_result` and `falsifying_result` form a bidirectional decision rule (a model-facing Registered Report). **Protocol**: a non-participant judge, Gemini 3.1 Pro (Preview), compares anonymised pairs and returns A/B/TIE; each pair is judged in both orders (2,400 ordered judgments) and is **order-stable** only if both agree — otherwise order-sensitive, reported separately and excluded from ranking; Bradley–Terry and Condorcet analysis on stable cases with a 10,000-replicate case-level bootstrap. **Diagnostic controls**: five-dimension structured re-judging on a 90-pair subset; hidden naive keyword/template baselines; same-content schema-vs-prose rendering; single-field clear corruption; subtle corruption with style-matched sham edits; full re-judging by a second judge (Doubao Seed 2.0 Pro); and a stratified three-annotator human calibration.

## Data
200 neighbourhoods from 800 unique papers (recent OpenReview/ICLR-adjacent literature, five batches of 40, provenance-audited). Four participants — GPT-5.2, Claude Sonnet 4.6, GLM-5, DeepSeek-V3.2 — each produce one native six-field proposal per neighbourhood (800 proposals), forming 1,200 canonical pairs. Human calibration: 20 neighbourhoods, 90 real pairs plus 4 hidden naive controls, three senior CS undergraduates following a bilingual protocol, blind to model identity.

## Key results

- **Robust ordering**: 2,400 judgments fold into 950 order-stable and 250 order-sensitive cases; ordering GPT-5.2 > Claude Sonnet 4.6 > GLM-5 > DeepSeek-V3.2 is a strict Condorcet order recovered in all 10,000 bootstrap replicates; a neighbourhood-cluster bootstrap widens intervals 11–27% but keeps the ranking; a second judge reproduces it with 86.1% agreement on stable comparisons. Even adversarial assignment of all 250 sensitive cases preserves the two-tier split (GPT-5.2 and Claude above GLM-5 and DeepSeek).
- **Main table (primary judge, stable W–L–T)**: GPT-5.2 424–49–127; Claude Sonnet 4.6 347–119–134; GLM-5 118–343–139; DeepSeek-V3.2 61–439–100. Human majority win rates: 0.805 / 0.775 / 0.233 / 0.214.
- **What separates models**: structured overall verdicts agree with holistic ones on 152/180 (84.4%); all 8/8 hidden naive controls are caught. Minimality/feasibility is the strongest separating dimension among natural outputs; falsifiability is non-tied in only 33/180 judgments and the sole decisive dimension in 1/180 — an **admissibility floor**, not a separator.
- **Judge tracks substance, not style**: with one field clearly corrupted, clean proposals win 40/40 per dimension (mean target-score drops 1.73 / 2.00 / 1.95); sham edits alone do not move verdicts (0 wins, 40 ties, 0 sham wins per dimension); sham-adjusted preference for the clean proposal is 0.550 (grounding), 0.775 (decisive metric), 0.537 (falsifiability), pooled 0.621, all CIs excluding zero.
- **Human corroboration**: humans catch the naive control 11/12 times; of 60 stable real pairs, 39 yield a decisive human majority, and 34/39 (87.2%) agree with the judge; 88.3% of human-BT bootstrap rankings are within one inversion of the judge ranking. Inter-annotator agreement is only modest, and human falsifiability scores do not separate winners from losers (margin 0).

## Contributions
- **Falsifiability as the evaluation unit**: the six-field contract makes each proposal carry "what would refute me", giving judgments a common decision structure.
- **Prospective construction with no answer key**: avoids rewarding a single realised trajectory and contamination.
- **Self-auditing protocol**: order folding, explicit isolation of order-sensitive cases, hidden controls, corruption/sham audits, a second judge and human calibration jointly give a bounded reliability envelope.

## Limitations
- Human calibration covers 20/200 neighbourhoods with three undergraduate annotators and modest inter-annotator agreement — not benchmark-wide validation.
- One canonical judge per version (though a second judge reproduces the ordering).
- **No execution**: measured testability is a prerequisite for downstream success, not a predictor of it.
- ML-adjacent literature only, biomedicine untested; the subtle-corruption audit has construction imperfections (e.g. 3.9% leakage).

## Relation to our direction
Relevant to **Plan B** and the revert step, as methodology (relevance: medium). **(1) Nomination format at the revert step**: at the end of detect → model → revert, when an agent proposes "perturbing gene X reverts the abnormal tubular/interstitial state", it can be forced to output a six-field-style contract — evidence gap, hypothesis, minimal wet-lab test (e.g. knockdown in a cell line/organoid), decisive readout (e.g. an injury score or marker), supporting and **falsifying** outcomes. Wet-lab results then map naturally to "passed / falsified", giving Plan B clean claim-level labels. **(2) An engineering template for judge-reliability audits**: if Plan B uses an LLM verifier, Lit2Test's order folding + separate order-sensitive reporting + hidden naive controls + single-field corruption + style-matched sham edits is a ready-made verifier self-check list, aligned with Plan B's rerun-stability concern. **(3)** Together with `ideation-execution-gap-arxiv-2025` it reminds us that falsifiable ≠ successful; the real label still requires execution (for us, the wet lab). Relation to Plan A is weak.

## Reusable assets
- **Benchmark, construction pipeline and audit artefacts:**
<https://github.com/rrustlee/lit2test-benchmark>
- **Six-field contract and rubric** (five dimensions: grounding, hypothesis specificity, minimality/feasibility, decisive metric, falsifiability).
- **Order-folding rule + Bradley–Terry/Condorcet + case-level bootstrap** statistics.

## Follow-ups
- ResearchStudio-Idea (IdeaSpark) — concurrent work requiring falsification predictions at generation time.
- HARPA — testable proposal generation with required metrics/controls, partly evaluated by execution.
- The disproof-review mechanism in `co-scientist-nature-2026`.

## Cite
```bibtex
@misc{falsifiable-ideation-arxiv-2026, title={What Proves You Wrong: Benchmarking Language Models on Falsifiable Research Ideation}, author={Wang, Ziyue and Yuan, Aomufei and Yao, Yiran and Yao, Linli and Zuo, Hongyao and Gong, Ziwen and Liu, Yuanxin and Li, Shicheng and Cai, Yishuo and Yang, Tong and Sun, Xu and Li, Xiaohui and Bai, Haoli}, year={2026}, eprint={2608.22948}, archivePrefix={arXiv}, primaryClass={cs.CL}, url={https://arxiv.org/abs/2608.22948}, doi={10.48550/arXiv.2608.22948} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

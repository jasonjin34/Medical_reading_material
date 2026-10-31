# The Ideation-Execution Gap: Execution Outcomes of LLM-Generated versus Human Research Ideas

> **Bibkey** `ideation-execution-gap-arxiv-2025` · **Venue** arXiv preprint (2025) · **Category** agents · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2506.20803> · `status: complete`

---

## One-liner
Si et al. had found LLM-generated NLP research ideas rated more novel than human-expert ideas; this pre-registered, blinded RCT **execution study** has 43 experts each spend ~100 hours turning a randomly assigned idea into a 4-page paper, blind-reviewed by 58 reviewers — after execution, LLM ideas' scores fall significantly more on every metric and the ranking even flips: the "ideation-execution gap".

## Problem
A good idea should not merely appear novel; it should yield better research when executed. Prior evaluation of LLM ideas stopped at the idea (LLM judges or small human studies), with at most one or two executed cases — no statistical conclusions. Do LLM ideas still beat human ideas after execution? Does ideation-stage evaluation predict execution outcomes?

## Method
Pre-registered (OSF) blinded RCT reusing the ideas and pre-execution scores from Si et al.'s (2025) ideation study. Each executor states preferred topics among seven NLP topics (Bias, Coding, Safety, Multilingual, Factuality, Math, Uncertainty) and is **randomly** assigned an anonymised idea within them, sourced either from a human expert or a Claude-3.5-Sonnet-based LLM agent. Three months to implement all experiments and submit a reproducible codebase plus a ≥4-page ACL-format paper. Rule: no substantive change to the method, only to experimental details (datasets, baselines, models, hyper-parameters), all changes declared and manually reviewed. Expert reviewers then blind-review code + paper on novelty, excitement, soundness, effectiveness, overall, plus faithfulness and codebase quality as controls. The key measure is the gap "post-execution score − pre-execution score", which removes the high heterogeneity in idea quality.

## Data
66 onboarded, 43 completed (19 human ideas, 24 AI ideas); executors average 15.3 / 14.3 papers and 112.6 / 93.7 hours; 58 reviewers wrote 181 reviews (4–5 per project), averaging 596.8 citations and 52.5 minutes per review; participants from 40 institutions. One project was terminated and excluded because the idea was too vague. Stanford IRB approved.

## Key results

- **Pre-execution** (per-idea means, human N=19 / AI N=24): AI ideas score significantly higher on all four — novelty 5.778 vs 4.912, excitement 5.653 vs 4.404, effectiveness 6.003 vs 4.833, overall 5.382 vs 4.596 (FDR p = 0.035 / 0.004 / 0.001 / 0.035).
- **Post-execution**: AI 4.729 / 3.896 / 4.125 / 3.406 vs human 4.903 / 4.482 / 4.782 / 3.968 — **the ranking flips**, though not significantly per idea (p 0.175–0.586). Per review (N=181), human ideas are significantly higher on excitement, effectiveness, soundness and overall, but not novelty.
- **The gap (headline)**: human ideas barely move (novelty −0.010, excitement +0.078, effectiveness −0.052, overall −0.628); AI ideas drop sharply (−1.049, −1.760, −1.879, −1.976); human−AI difference 1.039 / 1.835 / 1.827 / 1.348, FDR p = 0.025 / 0.001 / 0.003 / 0.004.
- **Controls match**: faithfulness (6.48 vs 6.42) and codebase quality (3.58 vs 3.58) are equal, so execution quality is comparable.
- **Ideation and execution scores correlate weakly**; for AI ideas excitement is even moderately negatively correlated.
- **Why scores drop**: changes concentrate on experimental details (2.9 per human idea, 3.1 per AI idea); one AI-specific source is proposing large human evaluations, which executors replaced with LLM-as-judge in 6 AI ideas — but excluding those 6 leaves conclusions unchanged. The main reason is that execution reviews weigh more factors — empirical performance, rigour, missing baselines/ablations, resource cost, generalisability — that ideation reviews largely ignore, often "assuming the experiments work".

## Contributions
- First execution study of LLM ideas large enough for statistically significant conclusions (43 projects, >4,000 expert hours).
- Pre-registered, randomised, blinded RCT with a "change details, not the method" rule and audited changes.
- Uses the pre/post score difference to control idea heterogeneity, showing ideation evaluation fails to predict execution outcomes.

## Limitations
- Ideas are restricted to three-month NLP prompting methods; generalisation to research requiring complex modelling, large data collection or training, or to non-AI fields, is unknown.
- Modest sample (19 vs 24); per-idea direct comparisons are underpowered and sensitive to individual executors.
- Execution is human, not agentic; LLM ideas come from a 2024 Claude-3.5-Sonnet agent — newer models untested.
- Reviewers are recruited and paid rather than real conference reviewers.

## Relation to our direction
The core lesson for us: **"looks good" nominations are untrustworthy before execution (the wet lab)**. The last step of detect → model → revert is exactly "predict which genes/perturbations revert the anomaly" and send them to wet-lab validation — this paper quantifies that step's risk in an NLP setting: AI ideas win on paper, but the advantage vanishes or reverses after execution, paper scores correlate weakly with execution outcomes, and AI excitement even correlates negatively. For **the agent-trustworthiness topic**: (1) evaluating agents that analyse kidney omics cannot rely only on agent reports or LLM/expert scores of those reports — there must be post-execution, verifiable signals: re-running and tracing back to data computationally (claim-to-evidence), and wet-lab outcomes for revert predictions; (2) the pre/post self-controlled difference can be reused to measure how much an agent conclusion's credibility drops between claim and verification; (3) AI ideas' preference for grand but infeasible human evaluations maps to an agent-trustworthiness-topic failure-taxonomy class: "infeasible / resource-unrealistic analysis plans". Relation to the artifact-injection topic is weak.

## Reusable assets
- **Data:** all ideas, executed projects and reviews.
<https://github.com/NoviScl/AI-Researcher>
- **Pre-registration:**
<https://osf.io/ckxtp>
- **Review form** (Appendix A) and the change-type taxonomy (dataset / metric / human→auto eval / model / hyper-parameters / baseline / analysis / prompt).

## Follow-ups
- The original Si et al. (2025) ideation study ("Can LLMs generate novel research ideas?").
- The authors' proposed directions: automated execution agents, proxy reward models trained on historical execution outcomes, and execution-feedback loops.
- `robin-nature-2026`, `co-scientist-nature-2026` — biomedical AI scientists with wet-lab validation.

## Cite
```bibtex
@misc{ideation-execution-gap-arxiv-2025, title={The Ideation-Execution Gap: Execution Outcomes of LLM-Generated versus Human Research Ideas}, author={Si, Chenglei and Hashimoto, Tatsunori and Yang, Diyi}, year={2025}, eprint={2506.20803}, archivePrefix={arXiv}, primaryClass={cs.CL}, url={https://arxiv.org/abs/2506.20803}, doi={10.48550/arXiv.2506.20803} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

# On the Limits of LLM-as-Judge for Scientific Novelty Assessment

> **Bibkey** `rq-bench-arxiv-2026` · **Venue** arXiv preprint (2026) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2606.12071> · `status: complete`

---

## One-liner
RQ-Bench reconstructs 1,434 "author-anchored" research questions (RQs) from 746 recent arXiv CS papers and uses them to test whether LLM-as-judge can reliably assess scientific novelty: LLM judges consistently rate model-generated RQs as more novel (a "novelty mirage"), and side-by-side comparison amplifies the preference — but domain experts reach the opposite conclusion and prefer the author RQs, with human–LLM agreement as low as 22%.

## Problem
In "AI scientist" pipelines LLMs both generate and judge ideas, so the whole chain's credibility rests on LLM-as-judge being reliable. Full-idea evaluation is hard (method, feasibility, experiments, impact), so the authors step back to a cleaner upstream object — the research question (RQ): it precedes a method, commits to no answer, and can be compared against questions real papers actually pursued. Core questions: are LLM novelty judgments of RQs stable? Do they agree with experts? Are generated RQs narrow or source-bound?

## Method
**Construction**: from ~200K arXiv CS papers (2025-01-01 to 2026-04-10), keep the top 10% by citations per subfield with LaTeX source and a conference/journal venue indexed by Semantic Scholar. qwen3.5-27b-thinking classifies each citation (using citation count, section, and local context) as inspiration / competitor / irrelevant-or-canonical; the first two count as influential. gemini-3.1-pro extracts ideas and contributions; gemini-3-flash extracts, per influential citation independently, the gaps the authors identified and addressed; gemini-3.1-pro then synthesises author-anchored RQs from gaps + contributions. Verification: gemini-3.1-pro judged 98% of RQs answered by the full source paper; humans approved 100% of 50 sampled. **Evaluation**: models get the background papers, must extract gaps and write exactly five RQs. Each RQ is scored 0–3 on three novelty metrics — originality, gap addressing, non-obviousness (not summed) — and two narrowness metrics — source-boundedness (stuck to one paper/dataset/metric/ablation) and diagnostic framing. Two settings: standalone (scored alone) and comparative (reference plus five generated RQs in one context). A "metric-level Pass@5" compares the best of five against the reference (win/tie/lose); a combined win requires both judges (gemini-3.1-pro, deepseek-v4-pro; temperature 0, high thinking). A 0–4 author-anchor overlap score diagnoses memorisation/recovery.

## Data
RQ-Bench: 1,434 RQs from 746 source papers across 13 arXiv CS subfields; 2,464 RQ–citation links to 1,375 cited papers; 3,151 grounded gap statements. 1.92 RQs per source paper on average; 1.72 cited references per RQ (52.4% grounded in a single reference); mean RQ length 24.7 words. Six models evaluated: qwen3-30b-a3b-thinking-2507, gpt-oss-20b, gemma-4-31b-it, deepseek-v4-pro, gemini-3.1-pro, gpt-5.5. Human study: 50 samples from cs.CL / cs.LG, two same-field experts blind-rating non-obviousness.

## Key results

- **Low author-anchor overlap**: all models fall in 1.0–1.33 (gpt-5.5 highest at 1.33), i.e. "same broad topic, different question" — models generate alternatives rather than recovering the author question (and are not simply memorising).
- **Standalone**: nearly all models' Best@5 scores exceed the reference on all three metrics (e.g. gemini judge: gpt-5.5 non-obviousness 1.98 vs reference 1.41), but ties dominate; under the two-judge combined rule gpt-5.5's strict win rate is only 27.2% on non-obviousness and 38.4% on originality.
- **Comparative amplifies preference**: gpt-5.5 combined non-obviousness win rate jumps from 27.2% to 49.1% and ties fall from 59.1% to 36.8%; with the gemini judge alone gpt-5.5 wins 79.3% (non-obv), 74.0% (orig), 88.9% (gap).
- **Sharp human–LLM disagreement** (50 samples, comparative non-obviousness, gpt-5.5 vs reference): Expert 1 picks the reference 78%, Expert 2 56%; gemini-3.1-pro picks gpt-5.5 82%, deepseek-v4-pro 52%. Expert–expert agreement 60%, LLM–LLM 52%, expert–LLM only 22–40%.
- **Narrowness is what judges miss**: two-judge combined source-boundedness is 0.47 for the reference vs 0.90 (gemini-3.1-pro) and 1.17 (gpt-5.5); gpt-5.5 loses to the reference 71.7% standalone and 85.4% comparative. When LLMs are explicitly asked to rate source-boundedness, their verdicts agree with expert non-obviousness judgments 72–76% of the time. Embedding similarity (Qwen3-Embedding-4B, all-mpnet-base-v2) does not capture narrowness — counter-intuitively, reference RQs are *more* similar to background papers.
- **Prompt trade-off**: removing constraining instructions lowers gemini-3.1-pro's source-boundedness from 1.00 to 0.47 (matching the reference), but LLM-judged non-obviousness/originality drop too; experts still prefer the reference (62% / 56%) and expert–judge agreement stays at 30–40%. LLM-judged "novelty" is conflated with narrowness, in the opposite direction to humans.

## Contributions
- Moves novelty evaluation to a cleaner upstream object (the RQ) and reconstructs author-anchored reference points from real papers — explicitly not as the only valid answer.
- Systematically contrasts standalone vs comparative judging and quantifies how comparative formats amplify preference for generated content.
- Uses a blinded expert study to expose the "novelty mirage": LLM judges and experts point in opposite directions.
- Proposes **scope/narrowness (source-boundedness)** as a first-class novelty dimension, showing it aligns with expert non-obviousness where embedding similarity does not.

## Limitations
- Only recent arXiv CS papers; transfer to biomedicine or other sciences is untested.
- Small human study: 50 samples, two experts, non-obviousness only; expert–expert agreement itself is only 54–60%.
- Construction itself relies on LLMs (qwen / gemini) to extract citations, gaps and RQs, and gemini-3.1-pro is simultaneously a builder, a judge and an evaluated model — a potential self-preference confound.
- Uses recent rather than strictly unseen papers; contamination is diagnosed only indirectly via the overlap score.
- No code/data release link is given in the paper.

## Relation to our direction
A cautionary "the judge itself is unreliable" paper that lands directly on **Plan B (trustworthy biomedical agents)** verifier design. Plan B plans a calibrated verifier for claims made by agents analysing kidney omics; if that verifier is an LLM, three lessons apply: **(1) judging format changes the verdict** — standalone vs comparative win rates differ by 20+ points, so the KidneyAnomalyBench / Plan B protocol must fix the format and report format sensitivity; **(2) use multiple judges with agreement reporting**, anchored by a small blinded expert set (the 50-sample design is a usable minimal human-calibration template); **(3) there are dimensions LLM judges systematically miss but experts weigh** — here, narrowness/source-boundedness. On the detect → model → revert chain the analogous risk sits in the revert step: a nominated "reverting gene/perturbation" that is merely a tweak of one source paper or a known pathway (source-bound) may still receive high LLM scores. "Does the claim merely restate its input evidence?" is a candidate new class for Plan B's omics-specific failure taxonomy. Relation to Plan A is weaker, but if KidneyAnomalyBench uses an LLM to judge whether an anomaly is novel or biologically meaningful, expert labels must remain ground truth and LLM verdicts treated as signals to calibrate.

## Reusable assets
- **Eval protocol:** metric-level Pass@5 with per-judge and combined-judge win/tie/lose definitions; standalone vs comparative formats.
- **Rubrics:** 0–3 rubrics for originality / gap-addressing / non-obviousness and source-boundedness / diagnostic framing (Appendix A.1–A.2), plus the 0–4 author-anchor overlap rubric.
- **Construction pipeline:** "influential-citation detection → contribution extraction → per-citation gap extraction → RQ synthesis" is transferable to biomedical literature. The paper gives no code or data link.
<https://arxiv.org/abs/2606.12071>

## Follow-ups
- Si et al.'s ideation and execution studies (this repo: `ideation-execution-gap-arxiv-2025`) — expert review vs execution outcomes.
- `llm-judge-healthcare-arxiv-2026` — scoping evidence on LLM-as-judge human alignment in healthcare.
- Downstream idea benchmarks (IdeaBench, ResearchBench, LiveIdeaBench) — do their judges share the same bias?

## Cite
```bibtex
@misc{rq-bench-arxiv-2026, title={On the Limits of LLM-as-Judge for Scientific Novelty Assessment}, author={Sinhahajari, Soumitra and Majumder, Navonil and Poria, Soujanya}, year={2026}, eprint={2606.12071}, archivePrefix={arXiv}, primaryClass={cs.DL}, url={https://arxiv.org/abs/2606.12071}, doi={10.48550/arXiv.2606.12071} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

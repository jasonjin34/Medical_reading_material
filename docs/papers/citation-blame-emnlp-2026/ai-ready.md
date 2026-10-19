<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# Who is the Agent to Blame? Localizing Faithfulness and Citation Mistakes in Agentic Deep Research

- **Authors:** Hirsch, Eran; Wan, David; Wang, Han; Stengel-Eskin, Elias; Bansal, Mohit; Dagan, Ido
- **Affiliations:** Bar-Ilan University; UNC Chapel Hill; University of Texas at Austin
- **Venue / Year:** EMNLP 2026 (Main Conference; accepted) · arXiv preprint 2026 (v1 2026-08-25)
- **arXiv:** 2608.24306
- **URL:** https://arxiv.org/abs/2608.24306
- **Code:** https://github.com/eranhirs/who-is-the-agent-to-blame
- **Bibkey:** Hirsch2026_260824306
- **Status:** complete (extract from arXiv v1 full text)

## Abstract
Deep research (DR) systems produce long-form cited reports by orchestrating multiple agents that search and synthesize information from the web. Citations are the primary mechanism for evaluating the faithfulness of these reports, yet current DR systems exhibit poor citation recall. Moreover, improving citation recall is challenging because DR systems are complex multi-agent architectures where information passes through agents like a telephone game, and both content and citations can get corrupted along the way. We propose an evaluation method that pinpoints which agent introduced each error by locally testing agent invocations for faithfulness and verifiability relative to their own inputs. Furthermore, we propose a four-type taxonomy to categorize the discovered errors: hallucination, uncited input reliance, uncited output, or insufficient citations. Applying our method to three top-ranked open-source DR systems, we obtain actionable diagnostics. Almost every agent makes a lot of mistakes with the exception being those that summarize a single document. We find that the dominant error type varies systematically across agents, where the orchestrator mistakes are mostly citation-related. We find that 84.7% of final-report errors in AI-Q originate at the orchestrator, roughly 31% of them hallucinations and the rest citation mistakes. Guided by these insights, we demonstrate that two simple interventions raise citation recall by 5% without degrading output quality.

## Full text / Extract

### Error taxonomy (per agent invocation, relative to its own inputs)
For synthesized outputs: (1) **hallucination** — output unfaithful to the input; (2) **uncited input reliance** — faithful, but draws on input that was itself uncited; (3) **uncited output** — faithful to cited input but carries no citations; (4) **insufficient citations** — has citations but not the complete set of the input it relied on. For extracted snippets: **snippet missing context** — the source does not support the entire snippet.

### Local evaluation algorithm (per sentence)
- Step 1 (faithfulness): LLM extracts all supporting spans from the agent's inputs (spans must appear verbatim; their union must entail the target; retry with self-critique on failure, else "evaluation failed" and filtered). Not fully supported → hallucination.
- Steps 2–3 (uncited input reliance): identify each input span's citations; remove uncited spans; if remaining cited spans no longer entail the target → uncited input reliance.
- Steps 4–5 (citation alignment): identify the target's citations; none → uncited output; otherwise keep only input spans whose citations are a subset of the target's and re-test entailment; not supported → insufficient citations; else correct.
- Prompts: span extraction from LAQuer (Hirsch et al. 2025); citation identification from DEER (Han et al. 2026); entailment and "is citation needed" from LongCite (Zhang et al. 2025). Judge: gpt-5-mini-2025-08-07.

### Human validation
50 sentences from AI-Q, each annotated by two of four graduate-student annotators with arbitration. Inter-annotator κ = 0.71. Method vs arbitrated labels: 76% exact match, κ = 0.62. Supporting-span localization agrees with annotators on 75% of relevant sentences.

### Systems and setup
Nvidia AI-Q (#1), MS-Agent (#2), TrajectoryKit (#3) on the DeepResearch Bench open-source leaderboard (May 2026). AI-Q: frontier model at planner/orchestrator, small open-weights model at researcher. MS-Agent: GPT-5 nano searcher, GPT-5 mini reporter, GPT-5 orchestrator. TrajectoryKit: gpt-oss-20b throughout. Diagnostics on 20 DeepResearch Bench examples, up to 10 sentences per agent per example (~200 per agent).

### Agent-level results (Table 1)
| System | Component | # | Correct % | Mistakes % |
|---|---|---|---|---|
| AI-Q | Orchestrator | 193 | 69.1 | 30.9 |
| AI-Q | Planner (uncited output not counted) | 121 | 78.0 | 22.0 |
| AI-Q | Researcher | 200 | 29.2 | 70.8 |
| AI-Q | Searcher (Synthesized) | 192 | 38.0 | 62.0 |
| AI-Q | Searcher (Snippets) | 189 | 96.2 | 3.8 |
| MS-Agent | Orchestrator | 183 | 83.2 | 16.8 |
| MS-Agent | Reporter | 190 | 38.4 | 61.6 |
| MS-Agent | Researcher | 170 | 53.4 | 46.6 |
| MS-Agent | Searcher (Synthesized) | 110 | 99.1 | 0.9 |
| MS-Agent | Searcher (Snippets) | 110 | 93.6 | 6.4 |
| TrajectoryKit | Orchestrator | 176 | 7.5 | 92.5 |
| TrajectoryKit | Researcher | 200 | 50.0 | 50.0 |
| TrajectoryKit | Searcher (Synthesized) | 154 | 85.1 | 14.9 |

Single-document summarizers make the fewest mistakes. Deeper agents hallucinate less: hallucinations are 31% of AI-Q orchestrator mistakes vs 79% for its researcher; MS-Agent orchestrator 0% vs reporter 78% and researcher 92%. Plausibly due to model capability (deeper agents run stronger LLMs); TrajectoryKit (same model everywhere) shows no shift.

### System-level results
Global citation recall: AI-Q 58.7%, MS-Agent 28.5%, TrajectoryKit 7.1%. Error-origin distribution (Table 2): AI-Q orchestrator 84.7%, researcher 14.8%, searcher (synthesized) 0.4%; MS-Agent orchestrator 52.6%, reporter 47.4%; TrajectoryKit orchestrator 100%. Final-output mistakes are mostly citation-related (AI-Q orchestrator 70%, MS-Agent 99%); hallucinations ~31% of AI-Q final-report errors (30% of orchestrator's 200 errors, 37% of researcher's 35), ~11% for MS-Agent. TrajectoryKit: 95% hallucinations — recurring failure where the orchestrator attaches a fabricated precise statistic to a source that does not state it, despite competitive RACE quality. Hallucinated URLs filtered using a ground-truth list from tracing logs; raw documents taken from logs (no-crawl).

### Interventions on AI-Q (50 English DeepResearch Bench queries; ± SEM)
| System | RACE | Citation recall | Citation precision |
|---|---|---|---|
| AI-Q | 52.6 ± 0.4 | 64.5 ± 3.9 | 87.6 ± 3.0 |
| + replace researcher notes with source snippets | 52.4 ± 0.7 | 69.7 ± 4.1 | 94.1 ± 2.0 |
| + citation guidance ("do NOT use information which is not backed by citations") | 52.6 ± 0.6 | 69.6 ± 3.2 | 91.0 ± 2.3 |

After citation guidance, the orchestrator's share of errors drops from 84.7% to 77.0% (researcher 14.8% → 23.0%), and orchestrator citation-related errors from 70% to 60%.

### Limitations (authors)
LLM-as-judge reliability (mitigated by prior-work prompts and the human study); the model-capability explanation is observational; only running-text sentences are evaluated — tabular numeric cells with citations are excluded.

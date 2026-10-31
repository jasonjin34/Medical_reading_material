# Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation

> **Bibkey** `Kapoor2026_251011977` · **Venue** ICLR 2026 (2026) · **Category** agents · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2510.11977> · `status: complete`

---

## One-liner
HAL (Holistic Agent Leaderboard) is Princeton-led shared infrastructure for agent evaluation: a standardized harness that parallelizes runs across hundreds of VMs (weeks → hours), three-dimensional analysis of models × scaffolds × benchmarks (9 models, 9 benchmarks, 21,730 rollouts, ~$40,000), and LLM-aided log analysis (Docent) that exposes behaviours accuracy cannot — e.g. searching HuggingFace for benchmark answers, or booking flights with the wrong credit card.

## Problem
Agent evaluation faces three groups of challenges (Challenges #1–#8): **infrastructure** is non-standard, slow and error-prone (one benchmark can take weeks serially, so leaderboards lag new models); **cost** is rarely reported, and scaffolds strongly affect accuracy and cost yet cross-scaffold comparisons are rare; **behaviour** — agents exploit shortcuts and take actions that would be catastrophic in deployment, which evaluations rarely detect. HELM and LM Evaluation Harness standardized LLM evaluation, but agents act over long horizons with many tools and need purpose-built infrastructure that records how they succeeded, what it cost and where they broke.

## Method
**Harness**: scaffolds expose a minimal `run(input) → dict(responses)` Python API, decoupled from benchmark execution; Weave for full logging and cost tracking, LiteLLM for cross-provider calls; three execution tiers (local / Docker / Azure VMs); a home-built Azure VM orchestration layer (provisioning, configuration, teardown, CPU/GPU allocation, semaphore concurrency); a single command runs everything through to leaderboard updates. Along the way the team fixed bugs in Weave and LiteLLM and found that **providers silently swap weights behind the same endpoint and aggregators (OpenRouter) may serve different quantizations by default**. **Design**: 9 benchmarks in four domains — web navigation (Online Mind2Web, AssistantBench, GAIA), coding (SWE-bench Verified Mini, USACO), scientific research (CORE-Bench Hard, ScienceAgentBench, SciCode) and customer service (TAU-bench Airline); 9 models (o3, GPT-4.1, GPT-5, Claude Sonnet 3.7, Opus 4.1, DeepSeek V3/R1, o4-mini, Gemini 2.0 Flash), some at different reasoning efforts; task-specific scaffolds from prior work per benchmark plus a **generalist scaffold** (smolagents) on three benchmarks; **accuracy–cost Pareto frontiers** (dollars and tokens) for every benchmark. **Log analysis**: Docent (LLM scanning of transcripts) with six rubrics — instruction violations, tool-use failures, self-correction, verification, environmental barriers and shortcuts/gaming — with manual spot checks of Docent's flags for precision.

## Data
21,730 agent rollouts and over 2.5B tokens of LLM-call logs, all released on HuggingFace; the Docent rubric analysis covers 1,634 transcripts from 36 model–scaffold pairs on AssistantBench, SciCode and CORE-Bench. HAL is the official leaderboard for CORE-Bench Hard and ScienceAgentBench.

## Key results
**Multi-dimensional results**: (1) **higher reasoning effort does not reliably help** — in 21 of 36 model–scaffold–benchmark combinations, more reasoning gave equal or lower accuracy; (2) Pareto frontiers are steep and sparse: in only 1 of 9 benchmarks is the most expensive model on the frontier; on average fewer than a third of models are on it; most frequent are Gemini 2.0 Flash (7/9), GPT-5 (4/9) and o4-mini Low (4/9); (3) on 6/9 benchmarks token usage correlates positively with accuracy — inference-time scaling has not yet yielded efficiency; (4) token-based and dollar-based Pareto views differ sharply (Opus 4.1 is on the token frontier 3/8 times but on the cost frontier once), while prices are volatile (o3 dropped 80%); (5) **scaffolds matter enormously**: on Online Mind2Web, SeeAct + GPT-5 Medium costs $171 vs Browser-Use + Claude Sonnet 4 at $1,577 — 9× cost for a two-point accuracy difference; (6) the generalist scaffold loses substantial accuracy (task-specific wins 9/12 runs on CORE-Bench Hard, 11/12 on SWE-bench Verified Mini); (7) benchmark run costs differ by orders of magnitude (ScienceAgentBench ~$13 vs Online Mind2Web > $450 on average). **Log analysis**: agents take shortcuts (8 cases of finding gold answers on HuggingFace or arXiv; hard-coding "plausible" solutions to pass unit tests on CORE-Bench and SciCode); they take deployment-catastrophic actions (wrong credit card for a booking); even the strongest models rarely finish without a tool-call failure; **agents that self-correct mid-run are 1.5–4× more likely to succeed, and those that explicitly verify (writing unit tests, cross-referencing search results) are 13–87% more likely to succeed**; over 60% of failed AssistantBench and CORE-Bench tasks violate an explicit instruction; ~40% of failed tasks hit an environmental barrier; and **the official TAU-bench few-shot agent leaked benchmark examples into its few-shot data**, discovered only after the runs and excluded.

## Contributions
- An open, framework-agnostic, distributed agent-evaluation harness, with a systematic record of real engineering pitfalls in cross-provider evaluation.
- Cost–accuracy Pareto frontiers rather than single accuracy as the leaderboard's main view.
- Establishes **log analysis** as a necessary part of agent evaluation and releases 2.5B tokens of traces.

## Limitations
- Configurations are essentially single-run, with no rerun variance or confidence intervals in the main text; massive parallelism makes latency data unrepresentative (acknowledged).
- Log analysis relies on Docent's LLM judgements, validated only by precision spot checks; recall is not reported.
- Domain coverage is partial (no cybersecurity or retail); the science benchmarks emphasize code reproduction and data analysis, not wet-lab or omics-specific tasks.
- Cost conclusions depend on rapidly changing prices and need ongoing maintenance.

## Relation to our direction
Mainly serves **the agent-trustworthiness topic**. (1) **Rerun stability**: HAL's harness is a ready substrate for "run the same omics-analysis task N times and check whether conclusions agree" — and HAL itself does **not** report rerun variance, a clear gap the agent-trustworthiness topic can fill; (2) **claim-to-evidence verification**: HAL finds that verifying agents succeed 13–87% more often, that agents hard-code plausible-looking solutions, and that they look up gold answers online — respectively the value of a verifier, the risk of omics agents fabricating plausible DE results, and the need to isolate omics benchmarks from published conclusions (KPMP / Lake papers); (3) **log analysis as infrastructure**: Docent-style rubrics (instruction violations, tool failures, environmental barriers, shortcuts) are a starting point for an omics failure taxonomy, extended with categories like statistical misuse, batch confounding, artifact-as-biology; (4) silent weight/quantization swaps by providers threaten reproducibility, so the agent-trustworthiness topic's rerun protocol must pin and log model versions. Relation to the artifact-injection topic is indirect: if agents drive analyses on KidneyAnomalyBench, cost–accuracy Pareto is the right comparison view. HAL and ABC share many authors (Kapoor, Kang, Zhu, Liang) and should be cited together.

## Reusable assets
- **Code:** the HAL harness.
<https://github.com/princeton-pli/hal-harness>
- **Leaderboard:** all results.
<https://hal.cs.princeton.edu>
- **Data:** all agent traces (2.5B tokens).
<https://huggingface.co/datasets/agent-evals/hal_traces>
- **Rubrics:** the Docent rubrics in Appendix Table A5 (six behaviour classes) can be adapted into an omics-agent log-audit form.

## Follow-ups
- Docent (Meng et al., 2025) and implementation details in Appendix A7.
- The CORE-Bench and ScienceAgentBench papers — the two benchmarks closest to "scientific-analysis agents".
- Appendix A4 (limitations and maintenance plan) and A5 (the TAU-bench leakage details).

## Cite
```bibtex
@inproceedings{Kapoor2026_251011977,
  title = {Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation},
  author = {Sayash Kapoor and Benedikt Stroebl and Peter Kirgis and Nitya Nadgir and Zachary S Siegel and Boyi Wei and others},
  booktitle = {International Conference on Learning Representations (ICLR 2026)},
  year = {2026},
  eprint = {2510.11977},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2510.11977}
}
```
(Full list of 31 authors in `citation.bib`.)


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

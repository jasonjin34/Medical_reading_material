# Who is the Agent to Blame? Localizing Faithfulness and Citation Mistakes in Agentic Deep Research

> **Bibkey** `Hirsch2026_260824306` · **Venue** EMNLP 2026 (2026) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2608.24306> · `status: complete`

---

## One-liner
In multi-agent deep-research (DR) systems information passes through agents like a "telephone game", and both content and citations can be corrupted along the way. This paper **locally tests each agent invocation for faithfulness and verifiability relative to its own inputs**, so every citation error in the final report can be **traced to the agent that introduced it**, and typed into four classes (hallucination, uncited input reliance, uncited output, insufficient citations). In Nvidia AI-Q, 84.7% of final-report errors originate at the orchestrator; two simple interventions guided by this raise citation recall by ~5 points without hurting quality.

## Problem
Citations are the main mechanism for judging DR-report factuality; the standard metric, citation recall (share of claims supported by their cited sources), is poor for current DR systems. Standard evaluation is **global** — final-report sentences against all source documents — so it says *that* something is wrong but not *who* or *what kind*. DR systems chain searchers, researchers and orchestrators, compressing information across agent boundaries, and developers lack tools to localize the failing component.

## Method
**Evaluating one agent invocation** (the building block): extract all inputs the invocation received and all outputs it produced; assume inputs are faithful and supported by their citations, and ask only whether the agent stayed faithful to **cited** input and carried all citations forward. For synthesized outputs, each sentence goes through five steps (all attribution/entailment tests): **Step 1 faithfulness** — an LLM extracts input spans supporting the target sentence (verbatim, union must entail the target; retry with self-critique on failure); if not fully supported → **hallucination**; **Steps 2–3** — identify each input span's citations, drop uncited spans; if the rest no longer entails → **uncited input reliance**; **Steps 4–5** — identify the target's own citations; none → **uncited output**; otherwise keep only spans whose citations are a subset of the target's and re-test; not supported → **insufficient citations**; else correct. Extracted snippets get one test (does the source support the whole snippet? fail → snippet missing context). Prompts are adapted from prior work (LAQuer span extraction, DEER citation identification, LongCite entailment and "citation needed"); judge gpt-5-mini-2025-08-07. **Two levels**: (a) agent level — sample sentences per agent type for error rate and error distribution; (b) system level — compute global citation recall on the final report, then for each erroneous sentence **recurse** from the orchestrator: a local test that finds an error blames that agent; otherwise follow supporting spans to the upstream invocation that produced them, until an error or a raw document is reached. Tracing logs give a ground-truth list of retrieved URLs (filtering hallucinated URLs) and the raw documents (no-crawl design). **Human validation**: 50 sentences, two annotators + arbiter, inter-annotator κ = 0.71; method vs arbitrated labels 76% exact match, κ = 0.62; span localization agrees with annotators on 75%.

## Data
Systems: the top three of the DeepResearch Bench open-source leaderboard (May 2026) — **Nvidia AI-Q** (frontier model at planner and orchestrator, small open-weights model at researcher), **MS-Agent** (model capability grows with depth: GPT-5 nano searcher → GPT-5 mini reporter → GPT-5 orchestrator), **TrajectoryKit** (gpt-oss-20b throughout). Agent- and system-level analyses use 20 DeepResearch Bench examples, up to 10 sentences per agent per example (~200 per agent); interventions use all 50 English queries, reporting RACE quality, citation recall and citation precision. Running-text sentences only; tables excluded.

## Key results
**Agent-level error rates (Table 1)**: AI-Q — orchestrator 30.9%, planner 22.0%, researcher **70.8%**, searcher synthesized 62.0%, searcher snippets **3.8%**; MS-Agent — orchestrator 16.8%, reporter 61.6%, researcher 46.6%, searcher synthesized 0.9%, snippets 6.4%; TrajectoryKit — orchestrator **92.5%**, researcher 50.0%, searcher synthesized 14.9%. **Agents summarizing a single document err least**; AI-Q's searcher, summarizing all documents for a query, rises to 62.0%; for identical per-document summaries gpt-oss-20b (14.9%) is an order of magnitude worse than MS-Agent (0.9%). **Deeper agents hallucinate less**: hallucinations are 31% of AI-Q orchestrator errors vs 79% for its researcher; MS-Agent orchestrator 0% vs reporter 78% and researcher 92% — attributed (observationally) to deeper agents running stronger models; TrajectoryKit, one small model throughout, hallucinates at every stage. **System level**: global citation recall AI-Q 58.7%, MS-Agent 28.5%, TrajectoryKit 7.1%; final-report error origin — AI-Q orchestrator **84.7%** / researcher 14.8% / searcher 0.4%; MS-Agent orchestrator 52.6% / reporter 47.4%; TrajectoryKit orchestrator 100%. The orchestrator has one of the lowest agent-level error rates in AI-Q and MS-Agent yet causes most final errors — system-level evaluation is not replaceable by unit tests. Final errors are mostly citation-related (AI-Q orchestrator 70%, MS-Agent 99%); ~31% of AI-Q's are hallucinations; TrajectoryKit's are **95% hallucinations**, typically the orchestrator attaching a fabricated precise statistic to a source that does not state it, despite RACE quality comparable to MS-Agent. Propagation chains: a searcher fabricates and the researcher and orchestrator faithfully pass it on; unsupported statistics travel verbatim with a citation that never supported them. **Interventions (AI-Q, 50 examples)**: RACE unchanged at 52.6; citation recall 64.5 → **69.7** (replace researcher notes with raw snippets) / **69.6** (add "do NOT use information which is not backed by citations" to the orchestrator prompt); citation precision 87.6 → 94.1 / 91.0. After guidance the orchestrator's error share drops 84.7% → 77.0% and its citation-related errors 70% → 60%.

## Contributions
- **Local, per-invocation tests** instead of global citation evaluation: errors are attributable to a specific agent, and checking against an agent's own inputs is far more tractable than against hundreds of sources.
- A **four-type taxonomy** across agent boundaries (+ snippet missing context), separating hallucination from citation bookkeeping errors.
- Complementary agent-level (unit-test) and system-level (recursive tracing) diagnostics.
- Shows diagnostics translate into effective fixes (a one-sentence prompt raises citation recall by ~5 points).

## Limitations
- Relies on LLM-as-judge (gpt-5-mini); human validation is only 50 sentences, method–human κ = 0.62.
- "Error type tracks model capability" is observational; no controlled same-model-across-roles experiment.
- Running text only; numbers and citations in tables are excluded — yet numbers are what is most often fabricated in scientific reports.
- Assumes each agent's inputs are faithful; verifies fidelity to inputs, not whether sources themselves are right.
- Evaluated only on general web DR (DeepResearch Bench), small samples (20 diagnostic, 50 intervention examples), no biomedical domain.

## Relation to our direction
One of the most directly borrowable methodology papers for **Topic 2**. **(1) Local verification + recursive tracing** transfers almost as-is to agents analysing kidney omics: split the pipeline into invocations (load data → QC → clustering/annotation → differential analysis → literature interpretation → report), check each step's claims only against **that step's inputs** (data tables, previous outputs, retrieved papers), and blame a wrong final conclusion on a specific step — exactly the "which layer did it fail at" axis our omics-specific failure taxonomy needs. **(2) The four-type taxonomy** extends to an omics version: beyond textual hallucination and citation bookkeeping, add "number disagrees with the executed code's output", "conclusion relies on non-QC'd data (analogue of uncited input reliance)", "cross-modal contradiction ignored". **(3)** Its most striking finding — 95% of the small-model system's errors are **fabricated precise statistics attached to a source**, while the paper **excludes numbers in tables** — is exactly what we must add for omics: numeric claims (p-values, cell proportions, log2FC) verified against actual computed results. **(4)** Its judge is uncalibrated, with no coverage guarantee; Topic 2's calibrated verifier (e.g. the split-conformal guard in citation-faithfulness-arxiv-2026) can sit on top of this localization framework. Weaker link to Topic 1, but directly relevant to auditable evidence chains when the detect → model → revert pipeline nominates genes for the wet lab.

## Reusable assets
- **Code:**
<https://github.com/eranhirs/who-is-the-agent-to-blame>
- **Algorithm:** five-step local verification (pseudo-code App. A), recursive tracing, all prompts (App. B), annotation guidelines (App. E).
- **Engineering tricks:** a ground-truth retrieved-URL list from tracing logs to filter hallucinated URLs; no-crawl raw-document extraction.
- **Systems evaluated:** Nvidia AI-Q, MS-Agent, TrajectoryKit (all open source).

## Follow-ups
- DeepResearch Bench (Du et al.) and DeepResearch Bench II, DEER (arXiv 2512.17776), LongCite, LAQuer.
- "LLMs corrupt your documents when you delegate" (Laban et al. 2026, arXiv 2604.15597) — more evidence on the telephone-game effect.
- Contrast with citation-faithfulness-arxiv-2026, which shows verifier strictness alone moves unsupported-citation rates from 3% to 18% — how sensitive are this paper's localization results to the judge?

## Cite
```bibtex
@misc{Hirsch2026_260824306,
  title = {Who is the Agent to Blame? Localizing Faithfulness and Citation Mistakes in Agentic Deep Research},
  author = {Eran Hirsch and David Wan and Han Wang and Elias Stengel-Eskin and Mohit Bansal and Ido Dagan},
  year = {2026},
  eprint = {2608.24306},
  archivePrefix = {arXiv},
  note = {Accepted to EMNLP 2026 (Main Conference)},
  url = {https://arxiv.org/abs/2608.24306}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

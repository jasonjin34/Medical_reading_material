# DeepTRACE: Auditing Deep Research AI Systems for Tracking Reliability Across Citations and Evidence

> **Bibkey** `NarayananVenkit2025_250904499` · **Venue** arXiv preprint (2025) · **Category** agents · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2509.04499> · `status: complete`

---

## One-liner
DeepTRACE turns community-identified failure cases of generative search engines and deep-research agents (from a prior user study) into **eight computable metrics** spanning answer text, sources and citations, built on two matrices — a **citation matrix** (which sources each statement cites) and a **factual-support matrix** (which sources actually support it). Across 303 questions × 9 public systems: deep-research modes reduce overconfidence but remain highly one-sided on debate queries, leave large fractions of statements unsupported, and reach only 40–80% citation accuracy.

## Problem
GSEs and DR agents promise source-grounded synthesis, yet users hit overconfidence, weak sourcing and confusing citations; LLMs hallucinate, retrieval often mis-cites, parametric knowledge is hard to separate from retrieved content, and systems are **sycophantic** toward the query's implied stance. Existing benchmarks evaluate isolated components (retrieval or summarization) or, like DeepResearch Bench and BrowseComp-Plus, task completion — with criteria set solely by researchers, without end-user input. The authors take a sociotechnical stance: start from 16 failure cases identified by real users and audit end-to-end how systems reason with, cite and use evidence.

## Method
**Pre-processing**: browser automation scripts capture query, answer, inline citations and source URLs; an LLM (GPT-5) decomposes answers into statements tagged for **Query Relevance** and **Pro/Con** (debate queries only); an LLM judge rates **Answer Confidence** 1–5; Jina Reader scrapes source full text (~15% fail due to paywalls/404 and are excluded); the citation matrix and factual-support matrix are built (an LLM judge labels each statement–source pair). **Eight metrics**: I One-Sided Answer (no both-sides coverage on debate queries); II Overconfident Answer (one-sided and confidence = 5); III Relevant Statement ratio; IV Uncited Sources (listed but never cited); V Unsupported Statements (relevant statements supported by no source); VI **Source Necessity** (the support matrix as a bipartite graph; Hopcroft–Karp minimum vertex cover gives the fraction of necessary sources); VII **Citation Accuracy** = Σ(citation ⊙ support)/Σcitation; VIII **Citation Thoroughness** = Σ(citation ⊙ support)/Σsupport. Each metric is graded acceptable/borderline/problematic using thresholds derived from the user study.

## Data
The DeepTRACE dataset has 303 questions: **168 debate questions** (from the non-partisan ProCon.org) and **135 expertise questions** (contributed by user-study experts in meteorology, medicine, HCI, etc., needing multi-hop search). Nine systems: GSEs You.com, BingChat/Copilot, Perplexity, GPT-4.5; DRs GPT-5 Deep Research, YouChat DR, Perplexity DR, Copilot Think Deeper, Gemini DR, plus GPT-5 web search. 2,727 samples in total (as of 2025-08-27); ~80,000 factual-support judgments. Judge validation: Pearson r = 0.72 with humans for confidence and r = 0.62 for factual support (100 items each, two annotators).

## Key results
**GSEs**: one-sided on ~50–90% of debate queries (Perplexity 83.4%, GPT-4.5 90.4%), Perplexity overconfident 81.6%; unsupported statements 23.1–47.0%; citation accuracy 39.8–68.3%; BingChat lists 4.0 sources on average but 36.2% are uncited and only about half necessary. **DRs**: still one-sided 54.7–94.8% (GPT-5 DR 54.67%, Copilot TD 94.8%), but overconfidence is uniformly <20% (their one relative strength); relevant statements <50% for all but GPT-5 DR (87.5%; Gemini DR 12.4%); **unsupported statements** 12.5% for GPT-5 DR vs 53.6% (Gemini) to 97.5% (Perplexity DR) for others; citation accuracy 31.4–79.1%; citation thoroughness 87.5% (GPT-5 DR) and 83.5% (YouChat DR), others 9.1–27.1%. GPT-5 DR leads on most dimensions, showing near-ideal reliability is achievable. **Cross-system**: more sources and longer answers do not yield better grounding and cause "search fatigue"; DR systems answer both pro- and con-framed versions of the same debate one-sidedly — sycophancy. (Note: the text gives Gemini DR citation accuracy as 40.3% while the table shows 50.3%; the table value is used here and the discrepancy flagged.)

## Contributions
- Formalizing the citation matrix × factual-support matrix: Citation Accuracy (are citations right?) and Thoroughness (are supporting sources cited?) form a precision/recall-like pair.
- Source Necessity uses minimum vertex cover to flag padding sources — separating "listed many" from "actually needed".
- Metrics and thresholds derived from a user study (sociotechnical evaluation) rather than researcher fiat.
- Brings one-sidedness, overconfidence and sycophancy into deep-research reliability auditing.

## Limitations
- Factual-support labels come from an LLM judge with only moderate human correlation (r = 0.62) — acknowledged as a limiting factor.
- System outputs are scraped via UI scripts that break with interface changes; ~15% of sources are unscrapable and excluded; results are a snapshot as of 2025-08.
- Interface-level findings from the user study are not operationalized; thresholds come from a single user study.
- Occasional text/table inconsistencies (see above); oriented to general/debate information seeking, not biomedicine.

## Relation to our direction
For **Topic 2** the value lies in **metric design**, not conclusions. Both matrices transfer directly to "an agent's report after analysing kidney omics": rows = atomic conclusions in the report, columns = analysis artefacts the agent produced (DE tables, clusterings, spatial statistics, cited literature); the citation matrix records what the agent claims to rely on, the support matrix what a verifier judges actually supports it. Then **Citation Accuracy** measures whether cited artefacts truly support the conclusion, **Thoroughness** catches evidence that exists but is uncited, **Unsupported Statements** is exactly Topic 2's core "unevidenced conclusion" rate, and **Source Necessity** flags redundant analyses attached to look rigorous. The one-sidedness/sycophancy metrics map onto an omics-specific failure: asked "is this region caused by disease?", an agent reports only supporting evidence and ignores artefact explanations — precisely what cross-modal agreement in Topic 1 is meant to rule out. Its judge–human correlation of only 0.62 is also a warning for Topic 2: the verifier itself must be calibrated before deployment. No direct bearing on Topic 1.

## Reusable assets
- **Dataset:** DeepTRACE's 303 questions (168 debate + 135 expertise), stated as released (no repository link in the main text).
- **Metric definitions:** formulas for the eight metrics (Eqs. 1–8) and the threshold table (Appendix B).
- **Tools:** Jina Reader for source full text; Hopcroft–Karp minimum vertex cover.
<https://jina.ai/reader/>

## Follow-ups
- Narayanan Venkit et al. (2025), the original user study — source of the 16 failure cases and design recommendations.
- Liu et al. (2023) verifiability audit of generative search engines.
- Read with deep-research-hallucination-arxiv-2026 (process-level) in this repo: DeepTRACE audits only the final report.

## Cite
```bibtex
@misc{NarayananVenkit2025_250904499,
  title = {DeepTRACE: Auditing Deep Research AI Systems for Tracking Reliability Across Citations and Evidence},
  author = {Narayanan Venkit, Pranav and Laban, Philippe and Zhou, Yilun and Huang, Kung-Hsiang and Mao, Yixin and Wu, Chien-Sheng},
  year = {2025},
  eprint = {2509.04499},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2509.04499}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

# Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents

> **Bibkey** `Rao2026_260403173` · **Venue** arXiv preprint (2026) · **Category** agents · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2604.03173> · `status: complete`

---

## One-liner
Quantifies citation-URL reliability across 10 models/agents on DRBench (53,090 URLs) and 3 models on ExpertQA (168,021 URLs, 32 fields): **3–13% of cited URLs are hallucinated** (no Wayback Machine record — likely never existed) and 5–18% are non-resolving; deep research agents cite the most and hallucinate the most. The authors release `urlhealth`, an 83-line tool that, used for agentic self-correction, cuts non-resolving URLs 6–79× to under 1%.

## Problem
Every major provider offers a deep-research mode with inline citations and users treat them as evidence, yet citation-URL reliability had never been measured systematically across models, providers and fields, and no reusable detection/mitigation tooling existed. The attribution literature asks "does the source support the claim?"; this paper asks the **logically prior question: does the source exist?** — if 3–13% of URLs are fabricated, support metrics systematically overestimate reliability. Six RQs: prevalence, system type, field variation, failure composition (fabrication vs link rot), quantity vs quality, mitigation.

## Method
**Operational definitions**: non-resolving = HTTP 4xx/5xx or connection failure (**403 excluded** as mostly bot-blocking; a headless-browser audit finds 99.7% of 403s live); hallucinated = non-resolving with no Wayback snapshot at any time; stale = non-resolving but archived (natural link rot). Because Wayback coverage is incomplete, hallucination rates are **conservative lower bounds**. **Pipeline**: extract URLs by regex (DRBench) or provider API structures (ExpertQA) → HEAD request (GET fallback on 405/403/501, browser UA) → Wayback lookup for non-resolving URLs. **urlhealth** classifies URLs as LIVE / DEAD (404, archived) / LIKELY_HALLUCINATED (404, unarchived) / UNKNOWN; shipped as a pip package and an agentskills.io skill. **Self-correction**: 435 ExpertQA questions (20% sample); Claude Sonnet 4.5 and GPT-5.1 call urlhealth as a function tool alongside web search in the same turn; Gemini 2.5 Pro uses a two-phase setup because its API forbids combining grounding with custom tools.

## Data
**DRBench** (Du et al., 2025): 100 multilingual (Chinese/English) research queries in finance, science and technology with pre-collected outputs from 23 models; 10 from Google/OpenAI/Anthropic are analysed (2 deep-research agents + 8 search-augmented LLMs). **ExpertQA** (Malaviya et al., 2024): 2,177 expert questions across 32 fields; the authors regenerate structured answers with numbered citations from claude-sonnet-4-5, gemini-2.5-pro and gpt-5.1.

## Key results
**RQ1**: on DRBench, non-resolving ranges from 5.4% (gpt-4.1) to 18.5% (gemini-2.5-pro-deepresearch) and hallucinated from 3.0% (claude-3-5-sonnet-search) to 13.3% (gemini-2.5-pro-deepresearch); ExpertQA overall non-resolving is 8.22% (gpt-5.1 8.47%, claude-sonnet-4-5 9.38%, gemini-2.5-pro 4.20%). **RQ2**: pooled hallucination 10.7% for the two deep-research agents vs 4.8% for eight search-augmented models; non-resolving 16.2% vs 6.8%. gemini-2.5-pro-deepresearch cites 113.1 URLs/query; openai-deepresearch 41.2, with only 3.5% hallucinated but 10.1% non-resolving (65% stale). **RQ3**: 5.4% (Business) to 11.4% (Theology); Claude Sonnet 4.5 ranges 4.0% (Mathematics) to 17.4% (Healthcare/Medicine), 4.3×; **Healthcare/Medicine is elevated for all three** (Claude 17.4%, GPT 7.1%, Gemini 5.3%). **RQ4**: four OpenAI search-augmented models have zero stale URLs — every failing URL is fabricated; Claude and the deep-research agents show substantial stale fractions, consistent with genuine retrieval over a partly stale index. **RQ5**: more citations ≠ more reliable (gpt-5.1 cites 46.4 URLs/question with 2× Gemini's failure rate). **RQ6**: with urlhealth as a tool, non-resolving drops GPT-5.1 16.0% → 0.6%, Gemini 6.1% → 0.1%, Claude 4.9% → 0.8% (all p < 0.001), but 10–20% remain UNKNOWN (bot-blocking/paywalls) — a practical ceiling. **Tool-use competence matters**: gpt-5-nano called the tool but ignored its results (7.5% NOT_LIVE; 48 hallucinated URLs persisted over up to 14 rounds).

## Contributions
- Uses the Wayback Machine to split failures into **fabrication vs link rot**, which require different mitigations (better grounding vs fresher indices / post-hoc validation).
- The largest URL-validity measurement in retrieval-augmented settings to date (220K+ URLs), qualifying SourceCheckup's "RAG avoids URL hallucination" conclusion.
- A minimal, model-agnostic open tool plus agentic self-correction experiments showing existence verification is correctable in practice.

## Limitations
- Hallucination labels depend on Wayback coverage (stale/hallucinated misclassification both ways); liveness is a point-in-time measurement affected by bot-blocking.
- URL citations only; fabricated snippets and invented bibliographic metadata (wrong authors, fake DOIs) are documented only qualitatively.
- **Measures existence, not support**: a LIVE URL may still not support the statement.
- Three providers, two English-dominated benchmarks; self-correction on a 20% subset (API quota limits).

## Relation to our direction
For **the agent-trustworthiness topic** this is **layer 0 of the claim-to-evidence chain: does the evidence exist?** In an omics-agent setting the analogue of a URL is a **file path, figure, table, cell output, dataset accession (GEO/KPMP) or gene ID** cited in the agent's report — any of which can be "fabricated" (the report cites a `de_results.csv` that was never produced) or "stale" (an intermediate file overwritten, notebook state lost). The taxonomy ports directly into one branch of an omics-specific failure taxonomy — **artefact-fabricated / artefact-stale / artefact-live-but-unsupported** — and urlhealth's LIVE/DEAD/HALLUCINATED/UNKNOWN scheme can become an existence check over the agent's working directory and provenance log. Two findings transfer: (1) long-horizon multi-step systems hallucinate **more** — expect similar error accumulation in multi-step analysis agents; (2) "having a tool ≠ using it" — small models ignore verification results, so a verifier-in-the-loop design must measure whether the agent actually acts on verifier feedback, not merely whether it calls it. No direct bearing on the artifact-injection topic.

## Reusable assets
- **Tool:** `urlhealth` (83 lines of Python; pip package + agentskills.io skill, MIT; the paper says tool and data are public but gives no repository link in the main text).
- **Benchmarks:** DRBench, ExpertQA.
- **Verification protocol:** HEAD→GET fallback, 403 exclusion, Wayback archive test, headless-browser audit of UNKNOWNs.
<https://archive.org/help/wayback_api.php>

## Follow-ups
- GhostCite (Xu et al., 2026), CiteAudit (Yuan et al., 2026), CiteGuard (Choi et al., 2026) — parallel citation-verification work.
- DRACO (Zhong et al., 2026): citation-quality and factual-accuracy axes for deep research.
- Read with sourcecheckup-natcommun-2025 and deeptrace-arxiv-2025: existence → support → end-to-end audit.

## Cite
```bibtex
@misc{Rao2026_260403173,
  title = {Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents},
  author = {Delip Rao and Eric Wong and Chris Callison-Burch},
  year = {2026},
  eprint = {2604.03173},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2604.03173}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

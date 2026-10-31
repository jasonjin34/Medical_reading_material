# An automated framework for assessing how well LLMs cite relevant medical references

> **Bibkey** `Wu_2025` · **Venue** Nature Communications (2025) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1038/s41467-025-58551-6> · `status: complete`

---

## One-liner
SourceCheckup is a fully automated agent pipeline — generate medical questions → have an LLM answer with sources → parse into independently verifiable statements → download URL contents → have GPT-4o judge each statement–source pair. Across 7 models, 800 questions and ~58K statement–source pairs, **50–90% of responses are not fully supported by the sources they cite**; even web-enabled GPT-4o (RAG) is fully supported in only 55% of responses. The automated verifier agrees with a three-doctor consensus 88.7% of the time, above the 86.1% average inter-doctor agreement.

## Problem
LLMs now cite sources on request and RAG systems search in real time, but **whether the cited sources actually support their medical statements** had not been systematically measured. Expert annotation is costly, hard to replicate and cannot keep pace with model releases; clinicians cite the inability to provide reliable sources as a top reason for distrust, and regulators such as the FDA need auditable provenance. The authors deliberately evaluate whether statements are grounded in verifiable sources rather than whether they are true, because medical ground truth is often contested (e.g. several overlapping answers for the typical age of tennis elbow).

## Method
Four modules, all with GPT-4o as backbone: **(1) Question generation** — one question from each of 400 MayoClinic pages plus 400 real Reddit r/AskDocs queries, 800 total (avoiding memorization of fixed sets like MedQA/PubMedQA); **(2) LLM answering** — short answer plus a structured source list (GPT-4o RAG had to be explicitly told to use Bing); **(3) Statement and URL parsing** — split into independently verifiable statements, download URLs (HTTP 200 only, PDFs converted, >128K-token pages dropped, ~0.1%); **(4) Source Verification** — all M×N statement–source pairs judged one-to-one; a statement is supported if at least one source supports it. Three metrics extending AIS: **Source URL Validity**, **Statement-level Support**, **Response-level Support** (every statement supported). Plus a **SourceCleanup** agent that removes or rewrites unsupported statements to fit their source, and a full replication with Claude Sonnet 3.5 to test GPT-4o bias.

## Data
800 questions (400 MayoClinic-generated + 400 Reddit r/AskDocs); ~58K statement–source pairs (from 800+ reference documents); 400 doctor-annotated pairs; an extra 300 HealthSearchQA questions and a 100-question end-to-end human evaluation. Models: GPT-4o (RAG), GPT-4o (API), Claude v2.1, Mistral Medium, Gemini Ultra 1.0 (RAG), Gemini Pro (API), plus Mixtral-8x7b; Llama-2-70b and Meditron-7b were dropped from main results for almost never producing URLs (<5%, <1%).

## Key results
**The verifier is reliable**: 88.7% agreement with doctor consensus vs 86.1% average inter-doctor agreement, no significant difference (p = 0.21); Claude Sonnet 3.5 as verifier reaches 87.0% (not different from GPT-4o, p = 0.52) and agrees with GPT-4o 90.1%; open-source Llama 3.1 70B only 79.3%. Doctors judged 100/100 generated questions valid and 330/330 and 329/330 parsed statements correct. **Model results**: GPT-4o (RAG) is best but **only 55% response-level support**; Gemini Ultra 1.0 (RAG) 34.5%; Gemini Pro API ~10%; offline models produce valid URLs only 40–70% of the time (GPT-4o API ~70%). GPT-4o (RAG) gives no sources in >20% of responses even when asked. On 110 GPT-4o (RAG) pairs judged unsupported, doctors agreed 95.8% (105/110 confirmed). **Question-source effect**: GPT-4o (RAG) response-level support is ~80% on MayoClinic but ~30% on Reddit questions (p < 0.001); on HealthSearchQA, 75.7% statement-level and 38.4% response-level; end-to-end human eval 40.4% vs SourceCheckup 42.4%. Merging sources leaves 95.1% of unsupported statements still unsupported. **SourceCleanup**: of 150 unsupported statements, 34.7% removed and 85.7% of the remaining 98 fixed — 90.7% removed or correctly edited. ~92% of cited URLs are US-based.

## Contributions
- Makes "does the citation support the statement?" an **automated, reproducible, doctor-validated** measurement rather than a one-off manual audit.
- A three-tier metric (URL valid → statement supported → whole response supported) separates link existence, sentence grounding and full-answer trust.
- Shows RAG is no silver bullet: web access removes URL hallucination but not unsupported content.
- Releases 800 questions, 58K pairs and doctor annotations; SourceCleanup demonstrates a verify-then-repair loop.

## Limitations
- Errors accumulate across automated modules (generation, parsing, citation extraction, verification); doctors themselves disagree, so individual data points are noisy.
- One-to-one statement–source mapping ignores support that only emerges from combining sources (checked: 95.1% remain unsupported after merging).
- Measures support, not correctness; a model could trivially max it by quoting sources verbatim, so it must be paired with quality metrics.
- Models are dated (early 2024); questions are US-centric; 404s and paywalls affect URL validity across institutions.
- The verifier is GPT-4o itself, with potential same-family bias (partly mitigated by the Claude replication).

## Relation to our direction
For **the agent-trustworthiness topic**, SourceCheckup supplies the **validation paradigm** for a claim-to-evidence verifier — more worth copying than the method itself: (1) first show the automated verifier agrees with an expert panel **at least as well as experts agree with each other**, then use it at scale — exactly the argument structure the agent-trustworthiness topic's calibrated verifier needs, with kidney pathology/omics experts as the panel and the agent's analysis artefacts plus KPMP/Lake reference data as the "sources"; (2) the three-tier metric maps directly onto an omics version: **artefact exists** (did the cited file/figure/table actually get produced?) → **single conclusion supported** (is it reproducible from the artefacts?) → **whole report supported**; (3) the large Reddit-vs-MayoClinic gap says **open-ended, multi-source questions** — exactly the artifact-injection topic-style "is this anomalous region disease or artefact?" — are where unsupported statements concentrate, so a benchmark should deliberately include them. SourceCleanup's verify-then-edit loop is a baseline for agent self-correction. It does not address numerical/statistical conclusions or rerun stability, the two gaps the agent-trustworthiness topic must fill.

## Reusable assets
- **Code and all prompts:**
<https://github.com/kevinwu23/SourceCheckup>
<https://doi.org/10.5281/zenodo.15015209>
- **Data:** 800 questions, responses, parsed statements, ~58K statement–source pairs and doctor annotations (Google Drive, non-commercial research use; raw web pages excluded for licensing).
<https://drive.google.com/drive/folders/1a-i974g3XzLCtZLpTLBbqAwK0olpd5JY>
- **Eval protocol:** Source URL Validity / Statement-level Support / Response-level Support; verifier-vs-panel agreement benchmarked against inter-doctor agreement.

## Follow-ups
- ALCE (Gao et al.), AttributedQA, AIS (Rashkin et al.) — foundational attribution definitions.
- reference-hallucination-arxiv-2026 in this repo qualifies this paper's "RAG models don't hallucinate URLs" conclusion — read together.
- Supplementary Tables 4/8/10 (full per-model numbers, sample sizes, fraction of unused URLs).

## Cite
```bibtex
@article{Wu_2025, title={An automated framework for assessing how well LLMs cite relevant medical references}, volume={16}, ISSN={2041-1723}, url={http://dx.doi.org/10.1038/s41467-025-58551-6}, DOI={10.1038/s41467-025-58551-6}, number={1}, journal={Nature Communications}, publisher={Springer Science and Business Media LLC}, author={Wu, Kevin and Wu, Eric and Wei, Kevin and Zhang, Angela and Casasola, Allison and Nguyen, Teresa and Riantawan, Sith and Shi, Patricia and Ho, Daniel and Zou, James}, year={2025}, month=Apr }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

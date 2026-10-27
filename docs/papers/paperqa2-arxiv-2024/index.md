# Language agents achieve superhuman synthesis of scientific knowledge

> **Bibkey** `Skarlinski2024_240913740` · **Venue** arXiv preprint (2024) · **Category** agents · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2409.13740> · `status: complete`

---

## One-liner
PaperQA2 (FutureHouse) decomposes RAG into agent-orchestrated tools — Paper Search, Gather Evidence (dense retrieval + **LLM reranking and contextual summarisation, RCS**), Citation Traversal, Generate Answer — exceeding PhD-level humans in precision on the new full-text retrieval benchmark LitQA2, writing gene Wikipedia-style articles (WikiCrow) with fewer "cited but unsupported" statements than real Wikipedia, and detecting contradictions in the biology literature at scale (ContraCrow).

## Problem
LLMs hallucinate and miss details, while existing literature benchmarks use abstracts only, a fixed corpus, or hand the relevant paper over, and rarely compare against humans — so it is unclear whether LLM agents are fit for real literature research. The authors build a rigorous human-vs-AI methodology across retrieval QA, summary writing and contradiction detection.

## Method
**PaperQA2**: an agent (orchestration LLM fixed to gpt-4-turbo-2024-04-09) can repeatedly call four tools: **Paper Search** (rewrite the request as keyword search, fetch full texts, parse, chunk; Grobid parsing for WikiCrow); **Gather Evidence** (top-k=30 dense retrieval, then an LLM **reranks each chunk and writes a question-specific contextual summary with a relevance score**, injecting journal/citation-count metadata; summaries stored in agent state); **Citation Traversal** (expand along the citation graph forwards/backwards as hierarchical indexing); **Generate Answer** (answer with citations from the top 5–15 summaries, with an "insufficient information" option). Temperature 0, three runs per configuration. **WikiCrow**: section-wise PaperQA2 calls (structure, function, interactions, clinical significance) stitched into an article. **ContraCrow**: an LLM extracts claims from a paper; PaperQA2 then checks each against the literature and emits an 11-point Likert score (≥8 = contradiction).

## Data
**LitQA2**: 248 multiple-choice questions whose answers appear only in the body (not abstract) of recent papers and ideally only once in the literature, with an "insufficient information" option; built in two stages (147 questions, then 101 more after engineering to test overfitting). **Human baseline**: 9 biology PhDs or PhD students, ~1 week, any online tools and institutional access, per-question cash incentives. **WikiCrow**: 240 human protein-coding genes with non-stub Wikipedia articles; 375 statements blind-graded. **ContraDetect**: LitQA2 rewritten into true/false statements, plus 42 "never-reported" statements; deployed on 93 random biology papers.

## Key results
**LitQA2**: 14.5 papers parsed per question on average; precision **85.2%±1.1%**, accuracy **66.0%±1.2%**, "insufficient information" in 21.9%; humans 73.8%±9.6% precision and 67.7%±11.9% accuracy — **superhuman precision** (p=0.0036), accuracy not significantly different (p=0.66). PaperQA2 beats Perplexity, Elicit, original PaperQA and non-RAG frontier models; accuracy on old vs. new question batches does not differ (no overfitting). **Ablations**: removing the agent (fixed pipeline) significantly lowers accuracy (p=0.015); removing RCS significantly lowers it (p<0.001), but using small models (GPT-3.5-Turbo, Llama3-70B) for RCS is worse than no RCS — a comprehension threshold; removing Citation Traversal significantly lowers DOI recall (p=0.022); top-k depth 1→10 helps significantly with diminishing returns to 30; parser and chunk size are not significant. **WikiCrow**: "cited and unsupported" 13.5% vs. Wikipedia 24.9% (p=0.0075), uncited 3.5% vs. 13.6%, precision 86.1% vs. 71.2%; reasoning errors 12 vs. 26 (p=0.0144), attribution errors 10 vs. 16 (n.s.); ~491.5 s and $4.48 per article. **ContraCrow**: AUC **0.842** on ContraDetect; at threshold 8, 73% accuracy, 88% precision, 7% false-positive rate; "no evidence" correctly chosen for 98% of never-reported statements; on 93 papers, 35.16 claims and **2.34±1.99** flagged contradictions per paper, with **70%** expert agreement (1.64 per paper, F1 0.82). In an independent detection task without the model's reasoning, experts agree with each other 75.5% but with ContraCrow only 60.4% (p=0.015); the authors suspect model **overconfidence**.

## Contributions
- Turns RAG into an agent task, with **RCS (rerank + contextual summary)** substantially improving full-text retrieval, and citation-graph traversal as hierarchical indexing.
- LitQA2: answers only in the body, unique in the literature, attribution checkable by DOI — a benchmark that scores both correctness and **correct provenance**.
- Separate precision and accuracy with abstention — "knowing what you don't know" is part of the score.
- A statement-level human evaluation of "does the citation support the statement" (cited-supported / uncited / cited-unsupported), and literature-scale contradiction detection.

## Limitations
- Accuracy does not exceed humans (only precision does); the "superhuman" headline rests mainly on precision and the WikiCrow comparison.
- Small human baseline (9 people for LitQA2); some LitQA2 questions leaked into search indices, invalidating a third human round; LitQA2 also guided PaperQA2's development (a new batch was used to address overfitting).
- ContraCrow agrees with independent experts only ~60% and is overconfident; a "contradiction" is not necessarily an error (literature evolves).
- Text only; full reproduction depends on the authors' internal full-text infrastructure (the open package needs your own corpus).

## Relation to our direction
PaperQA2 does not analyse omics data, but it is the mature reference for the "evidence–claim" side of **Topic 2**: **(1)** WikiCrow's cited-supported / uncited / cited-unsupported labels, with the further split into reasoning vs. attribution errors, can serve as our claim-to-evidence label set — except our "evidence" is not a paper passage but the agent's own tables, figures and statistics; **(2)** separating precision from accuracy with abstention is the evaluation framing a calibrated verifier should keep ("uncertain" must be a legal output); **(3)** ContraCrow's ~60% agreement with independent humans, attributed to overconfidence, is direct motivating evidence that LLM evidence-checkers need calibration. On detect → model → revert it belongs to the evidence layer: when the pipeline nominates a gene that would revert a kidney anomaly, a PaperQA2-like system can retrieve supporting/contradicting literature — using a strong enough model for evidence summarisation, per the RCS ablation. It complements DeepEvidence (structured knowledge bases + evidence graph): PaperQA2 is strong on unstructured full text.

## Reusable assets
- **Code:** the open paperqa package (with experiment configs; internal Grobid parsing, full-text search and citation traversal not included).
<https://github.com/Future-House/paper-qa>
- **Data:** WikiCrow articles (public GCS bucket); LitQA2, evaluator responses and contradiction claims in the supplement.
<https://storage.googleapis.com/fh-public/wikicrow2/>
- **Eval framework:** the three-way statement labels + error sub-typing; ContraCrow's 11-point Likert scale.

## Follow-ups
- LAB-Bench (`lab-bench-arxiv-2024`, origin of LitQA).
- FutureHouse follow-ups Robin and Kosmos (in this repo) — how PaperQA2 is embedded in larger discovery systems.
- Citation-faithfulness work (`citation-faithfulness-arxiv-2026`, `sourcecheckup-natcommun-2025`) for stricter "citation supports claim" evaluation.

## Cite
```bibtex
@misc{Skarlinski2024_240913740,
  title = {Language agents achieve superhuman synthesis of scientific knowledge},
  author = {Skarlinski, Michael D. and Cox, Sam and Laurent, Jon M. and Braza, James D. and Hinks, Michaela and Hammerling, Michael J. and Ponnapati, Manvitha and Rodriques, Samuel G. and White, Andrew D.},
  year = {2024},
  eprint = {2409.13740},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL},
  url = {https://arxiv.org/abs/2409.13740}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

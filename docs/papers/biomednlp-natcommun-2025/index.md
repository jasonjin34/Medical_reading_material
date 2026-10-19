# Benchmarking large language models for biomedical natural language processing applications and recommendations

> **Bibkey** `Chen_2025` · **Venue** Nature Communications (2025) · **Category** other · **Relevance** medium · **Access** open
> **Link** <https://doi.org/10.1038/s41467-025-56989-2> · `status: abstract-only`

---

## One-liner
A systematic evaluation of four LLMs (GPT and LLaMA representatives) across 12 BioNLP benchmarks and six applications — zero-shot, few-shot and fine-tuned — against traditionally fine-tuned BERT/BART. The verdict: **traditional fine-tuning still beats zero- and few-shot LLMs on most tasks**; GPT-4 leads only on reasoning-type tasks such as medical QA; open-source LLMs need fine-tuning to close the gap. Missing information and hallucination are documented systematically.

## Problem
The growth of biomedical literature outstrips manual curation, and BioNLP automates it. LLMs shine in general domains, but **their actual effectiveness on BioNLP tasks is unclear** — benchmarks, practical guidelines, and quantification of cost and failure modes are all missing.

## Method
Four LLMs (GPT and LLaMA representatives) are evaluated in three usage modes — zero-shot, few-shot and fine-tuned — against traditionally fine-tuned BERT/BART baselines. Beyond accuracy, the study explicitly examines three failure modes — **inconsistency, missing information and hallucination** — and performs a cost analysis, which is what turns it from a leaderboard into a set of recommendations.

## Data
12 BioNLP benchmarks spanning six application families (named-entity recognition, relation extraction, text classification, question answering, summarization and related biomedical NLP tasks).

## Key results
① **Traditional fine-tuning outperforms zero-/few-shot LLMs on most tasks** — a domain-specific small model plus labelled data remains a strong baseline. ② Closed-source LLMs (GPT-4) excel on **reasoning-type tasks** such as medical QA. ③ Open-source LLMs still require fine-tuning to close the gap. ④ **Missing information and hallucination** appear throughout LLM outputs. ⑤ Cost analysis indicates LLM-based solutions are often not the economical choice.

## Contributions
- A broad systematic BioNLP evaluation (12 benchmarks × 6 applications × 3 usage modes) that yields practical recommendations, not just scores.
- Elevates **hallucination and missing information** to first-class, explicitly quantified evaluation targets.
- Includes cost analysis, separating "does it work" from "is it worth it".
- Keeps traditional fine-tuning baselines in the comparison, providing an honest control.

## Limitations
- Models move fast; the 2025-specific conclusions (especially closed-model scores) date quickly.
- Covers text-only BioNLP tasks; no imaging or omics.
- Hallucination and missing-information judgments depend on human assessment and task definitions, limiting cross-task comparability.

## Relation to our direction
No topical overlap with the main chain, but it supplies **an argument this direction keeps needing**: on annotated specialist tasks, a **domain fine-tuned small model still beats a general large one** — i.e. the bottleneck is usually data and task definition, not model capacity. That is the same conclusion PathBench reaches on the imaging side ("scale does not predict performance"), and the two corroborate each other. Methodologically transferable: its treatment of **hallucination and missing information as explicit evaluation dimensions**. If we later evaluate an evidence-citing agent, "what it omitted" and "what it fabricated" must sit alongside accuracy as metrics, not in a footnote.

## Reusable assets
- **Eval protocol:** 12 BioNLP benchmarks × zero-shot / few-shot / fine-tune × traditional fine-tuning baselines, plus hallucination, missing-information and cost as analysis dimensions.
- **Paper (open access):**
<https://doi.org/10.1038/s41467-025-56989-2>

## Follow-ups
- Get the full text for the exact list of 12 benchmarks and the hallucination criteria, useful when designing failure-mode metrics for biomedical agents.
- Read alongside this repo's DeepEvidence entry: that one raises evidence-task performance with agent architecture, this one establishes the floor without agents.

## Cite
```bibtex
@article{Chen_2025, title={Benchmarking large language models for biomedical natural language processing applications and recommendations}, volume={16}, ISSN={2041-1723}, url={http://dx.doi.org/10.1038/s41467-025-56989-2}, DOI={10.1038/s41467-025-56989-2}, number={1}, journal={Nature Communications}, publisher={Springer Science and Business Media LLC}, author={Chen, Qingyu and Hu, Yan and Peng, Xueqing and Xie, Qianqian and Jin, Qiao and Gilson, Aidan and Singer, Maxwell B. and Ai, Xuguang and Lai, Po-Ting and Wang, Zhizheng and Keloth, Vipina K. and Raja, Kalpana and Huang, Jimin and He, Huan and Lin, Fongci and Du, Jingcheng and Zhang, Rui and Zheng, W. Jim and Adelman, Ron A. and Lu, Zhiyong and Xu, Hua}, year={2025}, month=Apr }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

# SemNovel – A new approach to detecting semantic novelty of biomedical publications using embeddings of large language models

> **Bibkey** `Peng_2025` · **Venue** Journal of Biomedical Informatics (2025) · **Category** other · **Relevance** medium · **Access** open
> **Link** <https://doi.org/10.1016/j.jbi.2025.104952> · `status: abstract-only`

---

## One-liner
SemNovel projects all of PubMed into a "semantic universe" using LLM embeddings and scores a paper's **semantic novelty** by its distance from prior literature; the score correlates positively with future citations and separates Nobel-Prize-winning work from ordinary papers.

## Problem
Literature is exploding, yet there is **no widely accepted measure of novelty**. Existing approaches quantify it from isolated article features (keywords, MeSH terms, references), discarding the context and nuance carried by the semantic content of the text.

## Method
A semantic universe is built with LLM-embedder (`BAAI/llm-embedder`, Llama2-7B-Chat as foundation, BGE base as embedding backbone), into which the whole PubMed library is projected; t-SNE gives 2D visualization; each article's SemNovel score is its distance from prior publications. Validation runs two ways: correlation with future impact (citations), and ability to distinguish groundbreaking studies. An interactive interface is provided for analyzing scores.

## Data
The full PubMed corpus; citation counts as the future-impact label; Nobel-Prize-winning studies as "groundbreaking" positives; plus a longitudinal case study in the PD-1/PD-L1 field and an analysis of interdisciplinary collaboration.

## Key results
The SemNovel score correlates positively with future citations (Spearman ρ = 0.1782, p < 0.001), **independent of journal impact factor, publication year and author count**, outperforming prior semantic-novelty indicators; it separates highly novel papers including Nobel-Prize studies (Kolmogorov–Smirnov test, p < 0.001); it traces research evolution in the PD-1/PD-L1 field and links interdisciplinary collaboration to higher novelty.

## Contributions
- Moves novelty measurement from feature counting to semantic-embedding distance, preserving textual meaning.
- Builds and visualizes a "semantic universe" at full-PubMed scale.
- Dual external validation against Nobel-Prize studies and citation impact, not just internal consistency.
- Ships an interactive interface, turning the metric into a usable tool.

## Limitations
- Correlation with citations is weak (ρ ≈ 0.18): statistically significant but of **limited power for predicting any individual paper's impact**.
- "Novel" is not "correct" or "valuable" — distance can also mean off-topic or low quality.
- Tied to one embedding model; score stability under a different backbone is unknown.
- Nobel Prizes as the "groundbreaking" label carry hindsight bias and field skew.

## Relation to our direction
Not on the detect → model → revert chain, but effectively an **instantiation of the anomaly-detection idea in literature space**: build an embedding distribution of what already exists, then flag points far from it as novel — methodologically isomorphic to this direction's "learn normal, score by deviation," with tissue swapped for papers. Two transferable pieces: (1) the **distance-as-score plus external-label validation** design (citations and Nobel Prizes ≈ expert annotation in histology); (2) its honesty — reporting a weak ρ ≈ 0.18 rather than hiding behind significance, the reporting discipline anomaly scoring needs. It is also an off-the-shelf tool if we later need to judge how novel an agent-generated hypothesis is.

## Reusable assets
- **Code:** the official SemNovel repository (Xu Lab).
<https://github.com/BIDS-Xu-Lab/SemNovel>
- **Model:** the LLM-embedder backbone.
<https://huggingface.co/BAAI/llm-embedder>
- **Eval design:** partial correlation with citations (controlling JIF, year, author count) plus a KS test against Nobel-Prize studies.

## Follow-ups
- Get the full text to confirm how the semantic universe is built and how the score is defined (distance metric, neighbourhood size).
- Compare against the original papers on prior novelty indicators (MeSH/reference-combination based).

## Cite
```bibtex
@article{Peng_2025, title={SemNovel – A new approach to detecting semantic novelty of biomedical publications using embeddings of large language models}, volume={172}, ISSN={1532-0464}, url={http://dx.doi.org/10.1016/j.jbi.2025.104952}, DOI={10.1016/j.jbi.2025.104952}, journal={Journal of Biomedical Informatics}, publisher={Elsevier BV}, author={Peng, Xueqing and Xie, Yutong and He, Huan and Ondov, Brian and Raja, Kalpana and Liu, Qijia and Mei, Qiaozhu and Xu, Hua}, year={2025}, month=Dec, pages={104952} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

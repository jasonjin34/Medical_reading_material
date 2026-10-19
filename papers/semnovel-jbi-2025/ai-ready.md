<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# SemNovel – A new approach to detecting semantic novelty of biomedical publications using embeddings of large language models

- **Authors:** Peng, Xueqing; Xie, Yutong; He, Huan; Ondov, Brian; Raja, Kalpana; Liu, Qijia; Mei, Qiaozhu; Xu, Hua
- **Venue / Year:** Journal of Biomedical Informatics · 2025
- **DOI:** 10.1016/j.jbi.2025.104952
- **URL:** https://doi.org/10.1016/j.jbi.2025.104952
- **Bibkey:** Peng_2025
- **Status:** complete

## Abstract
OBJECTIVE
The rapid growth of scientific literature necessitates robust methods to identify novel contributions. However, there is currently no widely-recognized measurement of novelty in biomedical research. Existing approaches typically quantify novelty using isolated article features, such as keywords, MeSH terms, or references, potentially losing important context and nuance from the semantic content of the text.


METHODS
We propose SemNovel, a semantic novelty detection framework that leverages embeddings from Large Language Models (LLMs) to capture richer semantic content. Specifically, we adopt LLM-embedder (BAAI/llm-embedder) for semantic universe construction, a unified embedding model that integrates Llama2-7B-Chat as its foundation and BGE base as the embedding backbone. We employ t-distributed Stochastic Neighbor Embedding (t-SNE) for 2D visualization and project the entire PubMed library into a "semantic universe". A SemNovel score is calculated for each article based on its distance from prior publications. We validated SemNovel's effectiveness through its correlation with future research impact and its ability to distinguish groundbreaking studies. We further explored its potential for analyzing trends in research trajectories and interdisciplinary collaboration. To enhance usability, we developed an interactive interface for users to analyze SemNovel scores.


RESULTS
The SemNovel score exhibited a positive correlation with future research impact, as measured by citation counts (ρ = 0.1782, p < 0.001, Spearman rank correlation), independent of factors such as journal impact factors (JIFs), publication years, and author counts, and outperformed previous semantic novelty indicators. It effectively identified highly novel papers, including Nobel Prize-winning studies (p < 0.001, Kolmogorov-Smirnov test). SemNovel also revealed trends in the evolution of scientific research, exemplified in the PD-1/PD-L1 field, and underscored the role of interdisciplinary collaboration in enhancing biomedical research novelty.


CONCLUSION
SemNovel represents a scalable and robust method for quantifying semantic novelty in biomedical literature. It provides a powerful tool for uncovering groundbreaking research, tracking scientific progress, and analyzing trends in innovation.

## Full text / Extract
<!-- Full cleaned text for open-access; for paywalled leave the note below. -->
> status: abstract-only — full text behind paywall. Drop `source.pdf` into this folder and re-run extraction to enrich.

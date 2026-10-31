# Toward Reliable Scientific Hypothesis Generation: Evaluating Truthfulness and Hallucination in Large Language Models

> **Bibkey** `truthhypo-ijcai-2025` · **Venue** IJCAI 2025 (Proceedings of the 34th International Joint Conference on Artificial Intelligence) (2025) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2505.14599> · `status: complete`

---

## One-liner
TruthHypo builds a biomedical hypothesis-generation benchmark from a temporally split PubTator 3.0 knowledge graph (pre-2023 "seen", post-2024 "unseen") to test whether LLMs propose **truthful** new relations; the companion KnowHD decomposes each hypothesis and its rationale into atomic claims and checks each against literature and/or the KG — higher groundedness predicts truthfulness, and selecting the most grounded of five candidates improves accuracy.

## Problem
Most LLM hypothesis-generation work optimises novelty and diversity but rarely evaluates **truthfulness**: verifying a hypothesis is costly, and hallucination yields plausible-but-wrong hypotheses. Two questions: (1) how well do LLMs generate truthful biomedical hypotheses, and do external knowledge sources (KG, literature) help? (2) Without running experiments, can "is the reasoning supported by existing knowledge" serve as a signal to filter out untrustworthy hypotheses in advance?

## Method
**TruthHypo**: relations extracted from literature in PubTator 3.0, split by publication year of the source PMID into "seen" (pre-2023) and "unseen" (post-2024, representing new discoveries); unseen edges sharing head and tail entities with seen ones are removed, and only relations supported by multiple articles are kept. Three tasks: Chemical & Gene, Disease & Gene, Gene & Gene, with `no_relation` negatives added (sized to the per-label average) to test false positives. Input is an entity pair; the LLM hypothesises their relation. Four knowledge settings: parametric only; +KG (entities mapped to the seen graph, multi-hop link chains verbalised); +literature (BM25 over PubMed restricted to pre-split articles, i.e. RAG); +KG+literature. Metrics: link-level precision/recall/F1 (does a relation exist) and relation-level accuracy (is the specific relation right). **KnowHD**: an LLM decomposes each hypothesis and its reasoning chain into atomic claims; for each claim, literature mode retrieves top-k pre-2023 PubMed documents via BM25, KG mode collects seen-graph edges among the claim's entities; an LLM then judges whether the context entails the claim. A hypothesis's groundedness is the fraction of supported atomic claims.

## Data
PubTator 3.0 knowledge graph + PubMed corpus (MedRAG-preprocessed chunks, BM25 retrieval). Final task sizes: Chemical & Gene 1,209 (positive_correlate 328 / negative_correlate 478 / no_relation 403); Disease & Gene 268 (stimulate 104 / inhibit 75 / no_relation 89); Gene & Gene 547 (positive 247 / negative 118 / no_relation 182). Models: Llama-3.1-8B, Llama-3.1-70B, GPT-4o-mini, GPT-4o (all trained on pre-2024 knowledge). The open-ended human study uses the public hypothesis-generation dataset of Qi et al. (2024).

## Key results

- **LLMs struggle to generate truthful hypotheses**: only GPT-4o exceeds 60% mean accuracy; link-level F1 (~65–84%) clearly exceeds relation-level accuracy — models guess *that* a relation exists but often not *which*. Best: GPT-4o with KG+literature, mean F1 83.55% and accuracy 66.95% (61.81% parametric only).
- **Scale and the ability to use external knowledge**: KG+literature adds only +1.14% accuracy for GPT-4o-mini but +5.14% for GPT-4o; Llama-3.1-8B actually drops to 39.62% with KG+literature (43.23% parametric) — small models struggle to integrate internal and external information.
- **KnowHD groundedness** (GPT-4o-mini hypotheses): e.g. for literature-augmented Chemical & Gene hypotheses, 76.30% of claims are verifiable against literature; KG-augmented hypotheses verify at only 51.08% against literature; combined KG+literature verification is highest (73–87%).
- **Groundedness tracks truthfulness**: GPT-4o-mini's mean accuracy on Chemical & Gene (KG+lit) is 60.96%, rising to 72.77% for hypotheses with groundedness above 80%.
- **Groundedness-based selection**: generate five candidates, keep the most grounded; with external knowledge this consistently beats greedy decoding and self-consistency majority voting — GPT-4o-mini reaches 63.44% mean accuracy with KG+literature, approaching GPT-4o; with parametric knowledge only, majority voting is slightly better (61.86% vs 59.83%).
- **Open-ended human study**: 54 hypothesis pairs with a ≥30% groundedness gap; two domain experts (80% agreement) picked the highly grounded one as more likely truthful 59.26% vs 40.74%; GPT-4o 61.11% vs 38.89%.

## Contributions
- **Temporally split KG construction**: predict "future-published relations" from "past knowledge", giving open-ended hypothesis generation an objective ground truth.
- **KnowHD: atomic-claim-level groundedness** rather than a holistic score, localising which reasoning step lacks support.
- Turns groundedness from a diagnostic into a selector that filters candidates toward truthful ones.
- Systematically compares parametric / KG / literature / combined settings across model sizes.

## Limitations
- The task reduces to relation classification between two entities (three relation types plus no-relation), much narrower than real open-ended scientific hypotheses.
- Ground truth comes from PubTator's automated text-mined relations, which carry extraction noise; "unseen" only means first reported after 2024, not experimentally confirmed.
- Groundedness measures consistency with **existing** knowledge — inherently favouring conservative hypotheses and potentially penalising genuinely novel discoveries (a tension the paper does not confront directly).
- Entailment is judged by an LLM whose own error rate is not separately calibrated; the human study has only 54 pairs and two experts.
- Only four pre-2024 models; retrieval is BM25 only.

## Relation to our direction
One of the most direct **technical prototypes for the agent-trustworthiness topic's claim-to-evidence verification**. KnowHD's pipeline — decompose output into atomic claims → retrieve evidence per claim → judge entailment → aggregate into a score — is essentially the skeleton of the agent-trustworthiness topic's calibrated verifier; the difference is that the agent-trustworthiness topic's evidence includes not only literature and KGs but the intermediate artefacts the agent actually produced on kidney omics (DE tables, cell annotations, spatial statistics). Three transferable ideas: **(1) temporal-split ground truth** ports to kidney — treat KPMP/Lake atlases and literature before a cutoff as "seen" and later-published kidney-disease gene/pathway associations as "unseen" to score agent-nominated targets; **(2) groundedness-based selection** fits the revert step of detect → model → revert: sample candidate "reverting genes" several times and keep the best-supported nominations before wet-lab prioritisation; **(3)** the tension it exposes should be handled explicitly in the agent-trustworthiness topic — "supported by existing knowledge" ≠ "correct", and ≠ "novel". The agent-trustworthiness topic's verifier should distinguish "contradicted by evidence", "unsupported (possibly novel)" and "supported", rather than treating every unsupported claim as hallucination. KnowHD also does not calibrate its own error — the agent-trustworthiness topic's emphasis on a **calibrated** verifier fills exactly that gap.

## Reusable assets
- **Code & data:** TruthHypo benchmark and KnowHD implementation.
<https://github.com/Teddy-XiongGZ/TruthHypo>
- **Knowledge sources:** PubTator 3.0 KG; MedRAG-toolkit PubMed chunks + BM25 retrieval.
- **Prompt templates:** atomic-claim decomposition, entity extraction, entailment judgement (Appendix D, Figs 5–12).

## Follow-ups
- `hypogen-llm-colm-2024` (Qi et al. — source of the open-ended dataset used here).
- MedRAG / MIRAGE (same group's medical RAG benchmark) for retrieval-setting effects.
- `medragchecker-arxiv-2026` — same atomic-claim verification route, applied to RAG answers.

## Cite
```bibtex
@inproceedings{truthhypo-ijcai-2025, title={Toward Reliable Scientific Hypothesis Generation: Evaluating Truthfulness and Hallucination in Large Language Models}, author={Xiong, Guangzhi and Xie, Eric and Williams, Corey and Kim, Myles and Shariatmadari, Amir Hassan and Guo, Sikun and Bekiranov, Stefan and Zhang, Aidong}, booktitle={Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence (IJCAI-25)}, year={2025}, eprint={2505.14599}, archivePrefix={arXiv}, primaryClass={cs.CL}, url={https://arxiv.org/abs/2505.14599}, doi={10.48550/arXiv.2505.14599} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

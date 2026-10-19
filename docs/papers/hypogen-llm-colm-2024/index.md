# Large Language Models as Biomedical Hypothesis Generators: A Comprehensive Evaluation

> **Bibkey** `Qi_2024` · **Venue** COLM 2024 (Conference on Language Modeling) (2024) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2407.08940> · `status: complete`

---

## One-liner
Using a biomedical background → hypothesis dataset **split by publication date** (pre-Jan-2023 = train/seen, Aug-2023 = unseen), the paper systematically evaluates LLM hypothesis generation in zero-shot, few-shot, fine-tuned, tool-use and multi-agent settings, introduces four rubric metrics (Novelty, Relevance, Significance, Verifiability; scored by GPT-4 and checked against human experts), and finds LLMs can propose novel, later-validated hypotheses even on unseen literature — with "uncertainty" (measured by SelfBLEU) trading novelty against verifiability.

## Problem
Work on LLM hypothesis generation cannot usually guarantee that **test data was unseen in training** (training corpora are untraceable), so "discovery" cannot be told from "recall". Moreover, hypotheses have no single correct answer, so overlap metrics like BLEU/ROUGE are insufficient. The questions: can LLMs truly generate hypotheses zero-shot, and do external knowledge (few-shot, domain adaptation, instruction tuning, tool retrieval) and multi-agent collaboration help or hurt?

## Method
**Task**: given instruction I and background knowledge X extracted from a paper, generate hypothesis Y — framed as text completion. **Data** (Self-Instruct-style pipeline): compose topic-based PubMed paper sets → summarize with ChatGPT/GPT-4 → generate background–hypothesis pairs → filter low quality → split by publication date. **Models**: only those trained on corpora before March 2023 — gpt-3.5-turbo; general instruction models from the Alpaca Eval leaderboard (Vicuna-33B, Llama-2-70B-chat, WizardLM-13B/70B, Openchat-v3.2-super); medical models PMC-LLaMA-13B and MedAlpaca-13B; plus WizardLM-13B-V1.2 fine-tuned on the training pairs. **Prompts**: zero-shot, 5-shot random, 5-shot similarity-retrieved (5-shot*). **Metrics**: BLEU/ROUGE against gold; without gold, GPT-4 scores four dimensions on 0–3 with step-by-step justifications; **SelfBLEU** as a cheap proxy for uncertainty/diversity of generations (lower = more diverse). **Multi-agent framework**: Analyst (keywords/topics) → Engineer (PubMed search, filtering out literature after Jan 2023 to keep the test unseen) → Scientist (formulates hypotheses) → Critic (evaluates, loops back), optional human-in-the-loop; tool use compared via ReAct vs OpenAI function calling.

## Data
**Seen**: 2,700 pairs (literature before Jan 2023), split into 2,500 train and 200 validation/seen-test; **Unseen**: 200 pairs from papers published in Aug 2023. Source pool of ~10,000 PubMed medical papers (Fig. 2b). Human evaluation: three biomedical experts score 100 unseen-test examples. Data and code released.

## Key results
- **Zero-shot is more novel, few-shot more verifiable**: nearly all models (notably WizardLM and Openchat-v3.2-super) score higher Novelty zero-shot, while few-shot (especially retrieval-based 5-shot*) raises Verifiability and BLEU/ROUGE but lowers novelty — an explicit novelty–verifiability trade-off.
- **Better on unseen**: contrary to the memorization expectation, models score higher BLEU on the unseen split; the authors speculate the task's complexity hinders use of parametric "dark knowledge".
- **External knowledge is not always helpful**: domain adaptation (PMC-LLaMA, MedAlpaca) improves overlap and few-shot use but weakens zero-shot ability; instruction tuning improves retention, BLEU/ROUGE and verifiability but reduces novelty and significance (fine-tuned WizardLM-13B human Novelty only 0.85).
- **Uncertainty**: zero-shot generations have lower SelfBLEU (more uncertain) and higher Novelty; few-shot has lower uncertainty and higher Verifiability.
- **Human evaluation (Table 1)**: GPT-4 and human average scores correlate strongly (Pearson 0.73–0.97, Spearman 0.73–0.94, all > 0.7); best human average is Llama-2-70b-chat 5-shot (2.33), gpt-3.5-turbo 0-shot 2.02.
- **Tools and multi-agent**: tool use alone (PubMed) helps little, ReAct slightly worse than OpenAI function calling, and LLMs struggle to pick useful information from results; multi-agent division of labour significantly improves generation by introducing uncertainty, and tools add further gains inside the multi-agent setup (Fig. 6b; exact numbers not given in the main text).

## Contributions
- **Publication-date splitting** to control visibility, rather than indirectly estimating contamination — a simple but key design for evaluating discovery rather than recall.
- A four-dimension hypothesis rubric (novelty/relevance/significance/verifiability), with GPT-4-as-judge validated against human experts.
- "Uncertainty" as a unifying lens for zero-shot vs few-shot and external-knowledge effects.
- A four-role Analyst–Engineer–Scientist–Critic multi-agent prototype, with time-filtered retrieval to prevent leakage.

## Limitations
- Background–hypothesis pairs are extracted automatically by ChatGPT/GPT-4; the authors concede extraction accuracy/bias needs evaluation and manual annotation of a subset.
- Small scale: 200 unseen pairs, 100 human-rated examples (described as ~5% sampling); GPT-4-as-judge may have its own stylistic bias.
- "Verifiability" is a *judge-rated* "could be tested", not actual experimental or literature verification; the "later confirmed" example in Fig. 1 is anecdotal.
- SelfBLEU is a crude uncertainty proxy; impact of factual hallucination on hypotheses is left to future work; all models are 2023-era.
- Text-only, literature-background only — no experimental data or omics analysis.

## Relation to our direction
For **Plan B (trustworthy biomedical agents)** this is a methodological baseline: (1) **temporal splitting against leakage** is a protocol to copy — if an agent analysing kidney omics "proposes a new mechanism", proving it is not regurgitating KPMP/Lake-2023 conclusions requires seen/unseen splits by publication (or data-release) date, with the same time filter on retrieval tools; (2) its rubric hands "verifiability" to an LLM judge, whereas Plan B moves that step to **actual claim-to-evidence checking** (is the claim supported by the data/statistics the agent itself produced?) with a calibrated verifier instead of "GPT-4 gives 0–3"; (3) the novelty–verifiability trade-off and uncertainty lens translate into Plan B's **rerun stability** metric — the distribution of conclusions across repeated runs is a more meaningful uncertainty measure than SelfBLEU; (4) its finding that "tool retrieval helps little and LLMs struggle to identify useful information" is early evidence for the "retrieval/evidence-selection failure" class of an omics-specific failure taxonomy. On the detect → model → **revert** chain it sits after target nomination — the **hypothesis generation and triage** step: anomalies from Plan A and candidates from the virtual tissue must be delivered to the wet lab as verifiable hypotheses, and this paper gives a minimal framework for judging them.

## Reusable assets
- **Code & data:** LLM4BioHypoGen (background–hypothesis pairs, seen/unseen splits, evaluation scripts).
<https://github.com/TsinghuaC3I/LLM4BioHypoGen>
- **Eval protocol:** temporal split + time-filtered retrieval; four-dimension 0–3 rubric with GPT-4 step-by-step rationales; SelfBLEU diversity; Pearson/Spearman agreement between GPT-4 and humans.
- **Agent prototype:** Analyst / Engineer / Scientist / Critic role design.

## Follow-ups
- The original short version, arXiv:2311.05965.
- TruthHypo (IJCAI 2025) — follow-up evaluation of hypothesis truthfulness/hallucination along this line.
- Apply temporal splitting to kidney omics: use Lake 2023 / KPMP releases as the boundary to test whether agent conclusions merely restate published results.

## Cite
```bibtex
@inproceedings{Qi_2024,
  title = {Large Language Models as Biomedical Hypothesis Generators: A Comprehensive Evaluation},
  author = {Qi, Biqing and Zhang, Kaiyan and Tian, Kai and Li, Haoxiang and Chen, Zhang-Ren and Zeng, Sihang and Hua, Ermo and Hu, Jin-Fang and Zhou, Bowen},
  booktitle = {First Conference on Language Modeling (COLM)},
  year = {2024},
  eprint = {2407.08940},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2407.08940}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

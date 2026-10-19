# HeurekaBench: A Benchmarking Framework for AI Co-scientist

> **Bibkey** `Panigrahi2026_260101678` · **Venue** International Conference on Learning Representations (ICLR 2026) (2026) · **Category** agents · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2601.01678> · `status: complete`

---

## One-liner
HeurekaBench (Brbić lab, EPFL) is a **framework for constructing "AI co-scientist" benchmarks**: a multi-LLM pipeline extracts insights from published papers and their code repositories, matches and composes code workflows, and keeps an insight only after humans **run the code and confirm it reproduces the paper's result**; validated insights become open-ended (OEQ) and multiple-choice (MCQ) questions. Instantiated for single-cell biology as sc-HeurekaBench (41 validated insights, 50 OEQ + 50 MCQ), scored by an LLM judge that decomposes answers into atomic facts, it compares Biomni, CellVoyager and BixBench-Agent and ablates planner, critic and retriever choices.

## Problem
Existing data-driven science benchmarks mostly ask an instructed single computational question (e.g. how many miRNAs survive BH correction), whereas a co-scientist should plan those sub-steps itself and give open-ended, data-backed conclusions; the closest, BaisBench, has one LLM write questions without human oversight, so questions may be unanswerable. There is no framework to **reliably** evaluate open-ended, data-grounded scientific answers.

## Method
Tasks are triplets (D, Q, A): real experimental data, an open research question needing multi-step reasoning, and a scientifically validated answer. **Insight generation**: InsightExtractor (GPT-4o) proposes candidate insights, each with a summary, the experimental techniques used and verbatim grounding text; CodeDescriber summarises repo scripts; CodeMatcher links insights to scripts; CodeGenerator (Claude-4-Sonnet for the code modules) composes a multi-step workflow. **Human validation**: reviewers run the code (minor fixes allowed, e.g. column names), and an insight counts as validated only if outputs (figures/statistics) match the grounding text. **Question generation**: two OEQs and two MCQs per insight via few-shot prompting, with MCQ distractors built from plausible misinterpretations; filtering removes questions answerable from LLM pretraining, then humans remove hallucinations, duplicates and questions resting on unvalidated parts. **Evaluation**: OEQs scored 1–5 by G-Eval (GPT-4o), with the judge first **decomposing both answer and ground truth into atomic facts** (conditions, trends, conclusions) and checking complete/partial/missing; contradictions block a top score, extra non-conflicting findings are not penalised. MCQs use accuracy plus precision/recall. A separate sc-HeurekaBench-TU has 12 OEQs that need domain tools (SCENIC, CellPhoneDB, CellChat).

## Data
22 Nature/Cell single-cell papers from 2024–2025 with open code and data (CellxGene or paper resources); 10 candidate insights per paper; **41** validated across 13 papers (9 Nature + 4 Cell) → 50 OEQ + 50 MCQ. sc-HeurekaBench-Lite: datasets <750 MB (22 OEQ + 18 MCQ) so all three agents can run. Pipeline checks: 50 FlyBase paper–expert-finding pairs and 21 from BixBench for InsightExtractor; InsightBench (50 insights, 215 code files) for code matching.

## Key results
**Pipeline**: InsightExtractor gets 44/50 strongly related, 2 weak, 4 unrelated on FlyBase and 14/21, 4, 3 on BixBench; CodeMatcher correctly matches 158 of 215 scripts, 74.6% of files retrieved correctly per insight on average. **Agents (Lite, all on Claude-4-Sonnet)**: OEQ correctness BixBench-Agent **2.34**, Biomni **2.31**, CellVoyager **2.03** (out of 5); MCQ accuracy Biomni 50.0%, BixBench-Agent 44.4%, CellVoyager 27.8%. CellVoyager's deficit is attributed to fixed step budgets, limited code-fixing and difficulty integrating feedback; BixBench-Agent crashed on large datasets. **Planner ablation (Biomni, full set)**: Claude-4-Sonnet **2.58±0.05** best, GPT-OSS-120B 2.08, Qwen3-235B-thinking 1.85, GPT-4o 1.68, MedGemma-27B 1.53; Qwen improves with scale and thinking. **Judge agreement**: GPT-4o vs. Claude-4.5-Sonnet Spearman 0.84, κ 0.81; vs. Gemini-2.5-Pro 0.79, κ 0.71; vs. 11 human experts on 25 answers: |diff| ≤1 for 92% (mode) / 96% (median), Spearman 0.93 / 0.90, κ 0.85. **Critic ablation**: End-critic lifts GPT-OSS-120B from 2.04 to **2.49** (near Claude's 2.58), mostly on low-scoring questions, but lowers Qwen3-235B-thinking from 1.86 to 1.81 (hurting high scorers); Plan-critic hurts both (−0.13 / −0.19). **Retriever ablation (TU)**: removing Biomni's tool retriever drops GPT-OSS-120B from 2.15 to 1.56.

## Contributions
- **"Only what the code reproduces counts as truth"**: filtering insights by re-running the paper's own code, directly addressing unreliable LLM-generated questions.
- Atomic-fact-decomposition judging for open answers, validated across LLM judges and against human experts.
- The first same-backbone head-to-head of existing single-cell agents (Biomni, CellVoyager, BixBench-Agent), plus controlled planner / critic / retriever ablations.
- Shows critic **placement** matters: an end critic rescues poor answers while a plan critic disrupts reasoning — and the effect depends on the base model.

## Limitations
- Self-reported: only final answers are scored, with no step verification or partial credit; other domains need expert validation.
- Small (41 insights, 50 OEQ; Lite only 22 OEQ); only ~41 of 220 candidate insights validate, and tool-heavy insights were excluded because CodeGenerator hallucinated tool use, possibly biasing toward easy-to-reproduce analyses.
- The main judge is GPT-4o alone; absolute open-ended scores are low (best ~2.6/5) and agent differences may not be significant at this sample size.
- Using 2024–2025 papers only partly mitigates memorisation; no spatial or multimodal questions; no rerun-stability or confidence dimension.

## Relation to our direction
For **Plan B**, HeurekaBench offers two directly borrowable pieces: **(1) "reproduce before admitting" ground truth** — the same idea as scBench-Long's "claims must be independently reproduced," but automated as "extract insight → match repo code → compose workflow → human runs and confirms," suitable for building validated (D, Q, A) in bulk from kidney single-cell papers (KPMP, Lake atlas, DKD spatial atlas); **(2) atomic-fact-decomposition judging** — essentially a prototype of claim-level checking that splits an answer into atomic claims and compares each. Plan B's next step is to check claims not only against the paper's conclusion but against the agent's own outputs, with calibrated confidence. Its critic ablation is telling: **critic effects depend on the base model and can make good answers worse** — "add an LLM reviewer" is not itself trustworthy, which is exactly why Plan B needs a calibrated verifier; the judge–human agreement (κ 0.85) is a baseline for designing our annotation protocol. The link to **Plan A** is weaker, though its paper + code + data triplet construction could semi-automate the "known pathology findings" part of KidneyAnomalyBench.

## Reusable assets
- **Code + benchmark:** framework, agent inference and evaluation code, sc-HeurekaBench and TU.
<https://github.com/mlbio-epfl/heurekabench>
- **Project page:**
<https://brbiclab.epfl.ch/projects/heurekabench>
- **Prompts:** InsightExtractor / CodeDescriber / CodeMatcher / CodeGenerator, question generation and the judging rubric (Appendices A, B).

## Follow-ups
- BaisBench vs. BixBench (`bixbench-arxiv-2025`) question construction (Appendix C.5).
- Appendix C.4 on invalidated insights — which analyses are hardest to reproduce.
- The G-Eval paper and atomic-fact evaluation methods (FActScore-style).

## Cite
```bibtex
@inproceedings{Panigrahi2026_260101678,
  title = {HeurekaBench: A Benchmarking Framework for AI Co-scientist},
  author = {Panigrahi, Siba Smarak and Videnovi{\'c}, Jovana and Brbi{\'c}, Maria},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year = {2026},
  eprint = {2601.01678},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2601.01678}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

# LAB-Bench: Measuring Capabilities of Language Models for Biology Research

> **Bibkey** `Laurent2024_240710362` · **Venue** arXiv preprint (2024) · **Category** agents · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2407.10362> · `status: complete`

---

## One-liner
LAB-Bench (FutureHouse) is a 2,457-question multiple-choice benchmark of **practical biology-research capabilities**: literature retrieval and reasoning (LitQA2, SuppQA), figure/table interpretation (FigQA, TableQA), database access (DbQA), protocol troubleshooting (ProtocolQA), and sequence comprehension/manipulation (SeqQA, Cloning Scenarios). Every question has an "insufficient information" refusal option; accuracy, precision and coverage are reported against PhD-level human experts. Tool-free frontier models fall well short of humans overall.

## Problem
Existing science benchmarks mostly test "textbook" recall and reasoning rather than the practical tasks research requires (literature search, protocol planning, data analysis). Building AI research assistants needs benchmarks for these capabilities, with human-expert baselines.

## Method
**Question generation**: SeqQA and DbQA subtasks are mostly programmatic; LitQA2, SuppQA, FigQA, TableQA, ProtocolQA and Cloning Scenarios were hand-written by the authors and contracted biology experts. The authors report a generalizable strategy: have frontier models propose candidate questions, identify nonsensical ones or ones with no correct option, then revise manually — yielding high-quality questions models struggle with (probing the "null space" of model reasoning). **Subset design**: LitQA2 answers are typically attested once in a recent paper's main text and not answerable from abstracts; SuppQA only from supplementary material; FigQA/TableQA give only the figure/table image (no caption); DbQA spans many databases so no single API suffices; ProtocolQA introduces errors into published protocols and asks how to fix them; Cloning Scenarios are 41 "human-hard" multi-step cloning questions (>10 min for a trained molecular biologist). **Evaluation**: 0-shot chain-of-thought, answers parsed from text completions, **no tools at all (including internet)**; a refusal option on every question; accuracy (correct/all), precision (correct/attempted), coverage (attempted/all); SD over three runs. ~80% of questions are public; 20% held back to monitor contamination. Human baseline: PhD-level biologists answering "quizzes" with internet and everyday tools (plus free sequence software), asked (not enforceably) not to use AI tools, incentivized for performance and completion. A small **open-answer** check (Claude 3.5 Sonnet, GPT-4o) is added.

## Data
2,457 questions (69% covered by humans): LitQA2 248, SuppQA 102, FigQA 226, TableQA 305, DbQA 650 (10 subtasks), ProtocolQA 135, SeqQA 750 (15 subtasks), Cloning Scenarios 41. Public subset on HuggingFace. Models: Claude 3.5 Sonnet, Claude 3 Opus, Gemini 1.5 Pro, GPT-4o, GPT-4-turbo, Claude 3 Haiku, Llama-3-70B-Instruct (not multimodal; no FigQA/TableQA).

## Key results
**Human experts substantially outperform models on accuracy and precision overall**, with higher coverage. By category (from the text; main figure is a bar chart): **LitQA2** precision ~40% for all models, above random, but frontier models often refuse (some attempt < 20%), pushing accuracy below random; **SuppQA** has the lowest coverage — models mostly refuse; **FigQA** is hardest — near-random precision for all except Claude 3.5 Sonnet; **TableQA** is easiest, Claude 3.5 Sonnet equalling human accuracy and narrowly beating human precision; **DbQA** frequent refusals, poor performance; **SeqQA** precision ~40–50% with large subtask variation (> 90% on e.g. PCR-seq-enzprimers; worst on long-sequence subsequence and restriction-fragment count/length tasks; drops when given a gene name instead of a sequence); **ProtocolQA** ~50–60% precision; **Cloning Scenarios** well below humans. On ORF-transeff, Claude 3.5 Sonnet beats humans (0.88 vs 0.75 precision). **Open-answer** check: Cloning Scenarios accuracy only 0.20 for both models (the two correct of ten were guesses of the most common enzyme BsaI or antibiotic Ampicillin/Carbenicillin), FigQA 0.30, ProtocolQA Claude 0.30 vs GPT-4o 0.20 — so above-random MCQ scores partly reflect **test-taking by eliminating distractors and guessing**.

## Contributions
- The first large biology benchmark systematically covering practical research skills, with human-expert baselines.
- A refusal option on every question with accuracy / precision / coverage reported separately — putting "knowing what you don't know" into the evaluation.
- Open-answer re-checks of MCQs, exposing the importance of good distractors and test-taking bias.
- A 20% private split to monitor contamination; the view that human baselines on hard tasks will give way to human "proofs-of-possibility".

## Limitations
- All MCQ, and this paper evaluates only **tool-free** models; LitQA2, SuppQA, DbQA and SeqQA are meant to be tool-dependent, so results mostly measure refusal tendency + recall.
- The open-answer validation is tiny (~10 questions per category, two models).
- Human baseline covers 69% of questions (DbQA only 35%); the no-AI-tools rule for humans is unenforceable.
- No multi-step data analysis or omics processing; tasks centre on molecular biology and literature.

## Relation to our direction
For **Plan B**, LAB-Bench offers two directly borrowable evaluation disciplines: (1) **a refusal option with accuracy/precision/coverage split** — a precursor of selective prediction; our calibrated verifier is essentially a guaranteed trade-off between coverage and precision (when to say "insufficient evidence"); (2) **open-answer re-checks of MCQs**, showing models inflate scores by eliminating distractors — so verifying agents' kidney-omics conclusions cannot rely on multiple-choice formats. LitQA2 is also the standard evaluation set for literature agents such as PaperQA2 and DeepEvidence, i.e. a common benchmark for the literature side of claim-to-evidence verification. Its link to **Plan A** is weak: no omics analysis or anomaly detection; but TableQA/FigQA show limited figure reading, a reminder that agents interpreting H&E/Xenium visualizations need independent verification. For the detect → model → revert line, it is background on whether agents can be reliable research assistants.

## Reusable assets
- **Dataset (public ~80%):**
<https://huggingface.co/datasets/futurehouse/lab-bench>
- **Metric convention:** refusal option + accuracy / precision / coverage; a 20% private split for contamination monitoring.
- **Question-authoring recipe:** model-generated candidates → flag nonsensical/unanswerable ones → manual revision.

## Follow-ups
- LAB-Bench2 (Laurent et al. 2026, arXiv 2604.09554).
- PaperQA2's (paperqa2-arxiv-2024) tool-augmented LitQA2 results.
- The same team's BixBench (bixbench-arxiv-2025), moving from MCQ to open-ended data analysis.

## Cite
```bibtex
@misc{Laurent2024_240710362,
  title = {LAB-Bench: Measuring Capabilities of Language Models for Biology Research},
  author = {Jon M. Laurent and Joseph D. Janizek and Michael Ruzo and Michaela M. Hinks and Michael J. Hammerling and Siddharth Narayanan and Manvitha Ponnapati and Andrew D. White and Samuel G. Rodriques},
  year = {2024},
  eprint = {2407.10362},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2407.10362}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

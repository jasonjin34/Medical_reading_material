<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# LAB-Bench: Measuring Capabilities of Language Models for Biology Research

- **Authors:** Laurent, Jon M.; Janizek, Joseph D.; Ruzo, Michael; Hinks, Michaela M.; Hammerling, Michael J.; Narayanan, Siddharth; Ponnapati, Manvitha; White, Andrew D.; Rodriques, Samuel G.
- **Affiliation:** FutureHouse Inc., San Francisco
- **Venue / Year:** arXiv preprint · 2024 (v3 2024-07-17; submitted to NeurIPS 2024 Datasets and Benchmarks track, in review)
- **arXiv:** 2407.10362
- **URL:** https://arxiv.org/abs/2407.10362
- **Bibkey:** Laurent2024_240710362
- **Status:** complete (extract from arXiv v3 full text)

## Abstract
There is widespread optimism that frontier Large Language Models (LLMs) and LLM-augmented systems have the potential to rapidly accelerate scientific discovery across disciplines. Today, many benchmarks exist to measure LLM knowledge and reasoning on textbook-style science questions, but few if any benchmarks are designed to evaluate language model performance on practical tasks required for scientific research, such as literature search, protocol planning, and data analysis. As a step toward building such benchmarks, we introduce the Language Agent Biology Benchmark (LAB-Bench), a broad dataset of over 2,400 multiple choice questions for evaluating AI systems on a range of practical biology research capabilities, including recall and reasoning over literature, interpretation of figures, access and navigation of databases, and comprehension and manipulation of DNA and protein sequences. Importantly, in contrast to previous scientific benchmarks, we expect that an AI system that can achieve consistently high scores on the more difficult LAB-Bench tasks would serve as a useful assistant for researchers in areas such as literature search and molecular cloning. As an initial assessment of the emergent scientific task capabilities of frontier language models, we measure performance of several against our benchmark and report results compared to human expert biology researchers. We will continue to update and expand LAB-Bench over time, and expect it to serve as a useful tool in the development of automated research systems going forward. A public subset of LAB-Bench is available for use at the following URL: https://huggingface.co/datasets/futurehouse/lab-bench

## Full text / Extract

### Categories (Table 1)
| Category | Subtasks | Questions | Human coverage |
|---|---|---|---|
| LitQA2 | – | 248 | 100% |
| SuppQA | – | 102 | 100% |
| FigQA | – | 226 | 100% |
| TableQA | – | 305 | 82% |
| DbQA | 10 | 650 | 35% |
| ProtocolQA | – | 135 | 100% |
| SeqQA | 15 | 750 | 64% |
| CloningScenarios | – | 41 | 100% |
| Total | – | 2,457 | 69% |

- **LitQA2:** retrieval from the literature; unambiguous answers usually attested once, in recent papers, not answerable from abstracts. Tool-dependent (scientific RAG).
- **SuppQA:** answers only in supplementary material (text or non-Excel supplemental PDF tables); title and DOI provided.
- **FigQA:** figure image only (no caption or text); multi-element reasoning; requires multimodality.
- **TableQA:** table image only; lookup plus reasoning/operations.
- **DbQA:** information attributable to specific biology databases, spanning many sources so no single API suffices.
- **SeqQA:** 15 subtasks over DNA/RNA/protein sequences (PCR, restriction digests, ORFs).
- **ProtocolQA:** published protocols with introduced errors (modified or omitted steps); asks which step to fix.
- **Cloning Scenarios:** 41 "human-hard" multi-step cloning questions (>10 min for a trained molecular biologist), requiring tools.

### Construction
SeqQA and DbQA mostly programmatic; other categories hand-written by authors and contracted biology experts. Strategy: ask frontier models to generate questions, identify nonsensical ones or ones with no correct option, then revise manually — often yielding questions models cannot readily answer. ~80% of each subtask released publicly; 20% retained to monitor contamination.

### Evaluation
0-shot chain-of-thought, answers parsed from text completions, no tools (no internet). Every question includes an option to decline for lack of information. Accuracy = correct / all; precision = correct / attempted; coverage = attempted / all. Error bars: SD over three runs. Models: claude-3-5-sonnet-20240620, claude-3-opus-20240229, gemini-1.5-pro-001, gpt-4o, gpt-4-turbo, claude-3-haiku-20240307, meta-llama-3-70B-Instruct (not multimodal; not assessed on FigQA/TableQA).

### Results (from text)
- LitQA2: all models ~40% precision, above random; frontier models often refuse (some attempt < 20%), giving below-random accuracy.
- SuppQA: lowest coverage; models mostly refuse.
- FigQA: greatest challenge; near-random precision except Claude 3.5 Sonnet.
- TableQA: easiest; Claude 3.5 Sonnet equals human accuracy and narrowly surpasses human precision.
- DbQA: frequent refusals; no model performs particularly well.
- SeqQA: ~40–50% precision overall; > 90% on some subtasks (e.g. PCR-seq-enzprimers); performance drops when only a gene name is provided (PCR-gene-enzprimers); worst on long-sequence/subsequence tasks (PCR-primers-len, RE-seq-numfrags, RE-seq-lenfrags).
- ProtocolQA: ~50–60% precision.
- Cloning Scenarios: well below humans; Gemini 1.5 Pro and GPT-4-turbo have low coverage without precision benefit.
- ORF-transeff: Claude 3.5 Sonnet 0.88 vs humans 0.75 precision.
- Humans (PhD-level biologists with internet and everyday tools; asked not to use AI tools) greatly outperform models in accuracy and precision overall, with higher coverage.
- Open-answer check (Claude 3.5 Sonnet, GPT-4o): Cloning Scenarios 0.20 accuracy for both (the same 2 of 10 correct, by guessing the most common enzyme BsaI or antibiotic Carbenicillin/Ampicillin); FigQA 0.30; ProtocolQA 0.30 (Claude) vs 0.20 (GPT-4o). Above-random MCQ precision on hard questions comes from eliminating unlikely distractors and guessing.

### Learnings (authors)
1. Model-generated, human-revised questions probe the "null space" of model reasoning.
2. High-quality distractors are essential; validate MCQ results with open-answer grading.
3. Reliable human baselines are hard for complex tasks; they may be replaced by human "proofs-of-possibility".

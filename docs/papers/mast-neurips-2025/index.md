# Why Do Multi-Agent LLM Systems Fail?

> **Bibkey** `Cemri2025_250313657` · **Venue** NeurIPS 2025 Datasets and Benchmarks Track (2025) · **Category** agents · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2503.13657> · `status: complete`

---

## One-liner
A UC Berkeley team applies Grounded Theory to 150+ multi-agent-system (MAS) execution traces to derive **MAST**, the first empirical MAS failure taxonomy (14 failure modes in 3 categories: system design issues / inter-agent misalignment / task verification) with human agreement κ = 0.88, then scales it with a calibrated LLM annotator (o1, κ = 0.77) into **MAST-Data**, 1,642 annotated traces across 7 MAS frameworks.

## Problem
Despite enthusiasm, MAS often improve little over single agents or best-of-N sampling on popular benchmarks; the authors measure failure rates of 41%–86.7% across 7 open-source SOTA MAS. The field lacks a systematic, fine-grained, cross-system understanding of why MAS fail and standardized failure definitions, making root causes hard to pin down and systems hard to compare.

## Method
**(1) Grounded Theory induction**: theoretically sample 150 traces (each averaging >15,000 lines) from 5 MAS frameworks (HyperAgent, AppWorld, AG2, ChatDev, MetaGPT) and two task types (programming, math); six experts apply open coding, constant comparison, memoing and theorizing until theoretical saturation, >20 hours of annotation each. **(2) Agreement iteration**: three annotators independently label 5 random traces per round, discuss disagreements and refine definitions (add, remove, merge modes), three rounds (~10 hours just resolving disagreements), reaching Cohen's κ = 0.88. **(3) LLM annotator**: o1 with MAST definitions and few-shot human-annotated examples; on held-out data, 94% accuracy and κ = 0.77. **(4) Generalization**: a further human IAA round on two new MAS (OpenManus, Magentic-One) and two new benchmarks (MMLU, GAIA) gives κ = 0.79 without changing the taxonomy. **MAST structure** (mapped to execution stages): **FC1 system design issues** — disobey task specification, disobey role specification, step repetition, loss of conversation history, unaware of termination conditions; **FC2 inter-agent misalignment** — conversation reset, fail to ask for clarification, task derailment, information withholding, ignored other agent's input, reasoning–action mismatch; **FC3 task verification** — premature termination, no or incomplete verification, incorrect verification.

## Data
MAST-Data: 1,642 annotated traces across 7 MAS frameworks (ChatDev, MetaGPT, HyperAgent, AppWorld, AG2/MathChat, Magentic-One, OpenManus), with GPT-4-family, Claude 3.7 Sonnet, Qwen2.5-Coder-32B and CodeLlama-7B models, on ProgramDev (v1/v2), SWE-bench Lite, AppWorld Test-C, GSM-Plus, OlympiadBench, MMLU and GAIA. Also released: MAST-Data-human (21 traces, each annotated by three experts).

## Key results
**Failure distribution** (Figure 1, over 1,642 traces): system design issues 44.2%, inter-agent misalignment 32.3%, task verification 23.5%; the most frequent modes are step repetition (15.7%), reasoning–action mismatch (13.2%), unaware of termination conditions (12.4%), disobey task specification (11.8%), incorrect verification (9.1%) and incomplete verification (8.2%). (Figures 2 and 4 use different subsets and report different percentages — e.g. 41.8% / 36.9% / 21.3% for the 210 traces in Figure 4.) **System differences**: AppWorld often terminates prematurely, OpenManus tends to repeat steps, HyperAgent is dominated by step repetition and incorrect verification — no one-size-fits-all fix. Swapping models within MetaGPT, GPT-4o shows 39% fewer FC1 failures than Claude 3.7 Sonnet; swapping frameworks on ProgramDev, MetaGPT has 60–68% fewer FC1/FC2 failures than ChatDev but 1.56× more FC3. **Interventions**: improving ChatDev's role specification alone (CEO has the final say) gives +9.4% success; adding a high-level objective-verification step gives +15.6% on ProgramDev; but point fixes do not remove all failures and completion stays low. **Insights**: (1) MAS failure is not just a base-model problem — better design helps with the same model; (2) FC2 needs deeper "social reasoning / theory of mind", which protocol standardization (MCP, A2A) alone does not provide; (3) **multi-level verification** is needed — current verifiers mostly do superficial checks like "does it compile" or "any TODOs left".

## Contributions
- The first empirical MAS failure taxonomy with rigorous human-agreement validation (14 modes / 3 categories / mapped to execution stages).
- A replicable method: Grounded Theory → iterative IAA → calibrated LLM annotator → cross-system generalization check.
- A large public dataset (MAST-Data) and a pip-installable annotator (`agentdash`).

## Limitations
- The authors do not claim exhaustiveness; the taxonomy emphasizes reasoning and coordination and lacks execution-layer errors like API / resource / orchestration (TRAIL's critique).
- Most labels come from the LLM annotator (κ = 0.77, not perfect), so label noise affects distributional conclusions; a unique root cause is often hard to assign.
- Tasks are mainly programming, math and general assistance, with no scientific data analysis; percentages differ across figures because they use different subsets, so cite with care.
- Intervention studies are small; they show design changes help but offer no systematic repair method.

## Relation to our direction
For **Topic 2's omics-specific failure taxonomy**, MAST's main value is less its 14 modes than its **methodology for building a taxonomy**: theoretical sampling → open coding to saturation → three annotators iterating IAA until κ is high → calibrate an LLM annotator on human labels → re-measure κ on unseen systems/tasks. Topic 2 can follow this verbatim: theoretically sample traces from omics agents (Biomni, CellVoyager, SpatialAgent, etc.) on KPMP / Lake data, have kidney-omics-literate annotators do open coding, produce an omics failure taxonomy and report its reliability with MAST-style κ — making the taxonomy itself a publishable, reusable contribution. The content is also directly relevant: (1) **FC3 task verification (23.5%) is exactly where a claim-to-evidence verifier fits** — MAST finds current verifiers do only superficial checks and that adding a high-level objective-verification step gives +15.6%, direct evidence that an independent verifier helps; (2) reasoning–action mismatch (13.2%) corresponds to omics agents claiming batch correction was done when it wasn't, or Wilcoxon when a t-test ran — detectable only by checking trace against code; (3) "proceed with wrong assumptions instead of asking" maps to default assumptions when sample metadata (disease stage, eGFR, biopsy type) are ambiguous. Relation to Topic 1 is looser, but the Grounded Theory + IAA workflow also suits building expert-agreed category definitions for KidneyAnomalyBench anomaly types (technical artifact vs disease vs normal variation).

## Reusable assets
- **Code:** MAST taxonomy and LLM annotator (`pip install agentdash`).
<https://github.com/multi-agent-systems-failure-taxonomy/MAST>
- **Data:** MAST-Data (1,642 traces) and MAST-Data-human.
<https://huggingface.co/datasets/mcemri/MAST-Data>
- **Method template:** the GT → IAA → annotator calibration → generalization pipeline of §3.1–3.4, directly usable as the study design for an omics failure taxonomy.

## Follow-ups
- Appendix A (full definitions of the 14 modes) and Appendix H (intervention case studies).
- The Who&When dataset (Zhang et al.): attributing failures to specific agents and steps.
- Map item-by-item against TRAIL's taxonomy and merge into the upper levels of an omics failure taxonomy.

## Cite
```bibtex
@inproceedings{Cemri2025_250313657,
  title = {Why Do Multi-Agent LLM Systems Fail?},
  author = {Mert Cemri and Melissa Z. Pan and Shuyi Yang and Lakshya A. Agrawal and Bhavya Chopra and Rishabh Tiwari and Kurt Keutzer and Aditya Parameswaran and Dan Klein and Kannan Ramchandran and Matei Zaharia and Joseph E. Gonzalez and Ion Stoica},
  booktitle = {NeurIPS 2025 Datasets and Benchmarks Track},
  year = {2025},
  eprint = {2503.13657},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2503.13657}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

# TRAIL: Trace Reasoning and Agentic Issue Localization

> **Bibkey** `Deshpande2025_250508638` · **Venue** arXiv preprint (2025) · **Category** agents · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2505.08638> · `status: complete`

---

## One-liner
Patronus AI proposes an agent-error taxonomy (reasoning / planning & coordination / system execution) and releases TRAIL: 148 span-level human-annotated OpenTelemetry agent traces (from GAIA and SWE-bench Lite, 841 errors). Asked to act as trace debuggers that localize and categorize errors, LLMs do poorly — the best, Gemini-2.5-Pro, reaches only ~11% joint accuracy.

## Problem
Agent workflows are getting longer and more complex, and current evaluation relies on manual, domain-specific reading of lengthy traces, which does not scale; error analysis mixes tool outputs with LLM reasoning, making it harder than ordinary debugging. Prior trace analysis (e.g. MAST) works on parsed unstructured text rather than the structured OpenTelemetry logs real frameworks emit, and prior taxonomies emphasize reasoning and coordination while missing **system-execution and planning** errors such as API failures, resource management and task orchestration.

## Method
**Taxonomy**: (1) **reasoning errors** — hallucinations (language-only, tool-related), information processing (poor retrieval, tool-output misinterpretation), decision making (incorrect problem identification, tool selection errors), output generation (formatting errors, instruction non-compliance); (2) **system-execution errors** — configuration (incorrect tool definition, environment setup), API and system issues (rate limiting 429, authentication 401/403, service 500, resource not found 404), resource management (resource exhaustion, timeouts); (3) **planning & coordination errors** — context management (context handling failures, resource abuse / repeated calls), task management (goal deviation, task orchestration errors). Each error is labelled with location (span id), evidence, description and impact (LOW/MEDIUM/HIGH). **Trace construction**: GAIA via HuggingFace OpenDeepResearch's hierarchical multi-agent setup (manager + search agents on o3-mini); SWE-bench via a single CodeAct agent (claude-3-7-sonnet, sandbox + Python interpreter + gitingest) with added constraints such as output-length limits to **elicit errors organically**; all logged with OpenInference (an OpenTelemetry derivative). **Annotation**: four annotators experienced in software engineering and log debugging, with 63 separate traces for agreement (reported as high; numbers in the appendix). **Task**: given the full raw JSON trace, an LLM outputs error categories and locations; metrics are category F1, location accuracy, joint accuracy and Pearson correlation with human scores, averaged over three runs.

## Data
148 traces (1,987 OpenTelemetry spans, 575 with at least one error), 841 errors, 5.68 per trace on average; after review, 114 GAIA and 30 SWE-bench traces contain errors. Output-generation errors dominate — formatting errors plus instruction non-compliance are 353/841 (~42%); system-execution errors are rare but often unrecoverable. Inputs are very long: GAIA traces average ~263–313K tokens with maxima of 2.66M–8.25M depending on tokenizer; SWE-bench traces average ~473–558K — often beyond model context limits. Released under MIT.

## Key results
**LLMs are poor trace debuggers**: the best, Gemini-2.5-Pro, reaches ~18% joint accuracy on GAIA and ~5% on SWE-bench (~11% combined); three of eight models cannot fit the full context (marked CLE on SWE-bench). **Long context is a major factor**: all metrics correlate negatively with input length (location accuracy Pearson −0.379 / Spearman −0.508; joint accuracy −0.291 / −0.349; category F1 −0.296 / −0.225). **Reasoning helps**: except o1, reasoning models beat non-reasoning ones on category F1 and location accuracy, with joint accuracy 1.5–8× the best non-reasoning model; lowering o3's reasoning effort (high → medium → low) monotonically drops category F1 from 0.296 → 0.277 → 0.264. **By category**: context-handling failures score F1 ≈ 0 for nearly all models (Claude-3.7-Sonnet 0.18 the exception); tool-selection errors mostly 0.00–0.08 (o3 at 0.53 the exception); task orchestration 0.00–0.08 (Gemini-2.5-Flash 0.47 the exception); language-only hallucinations are comparatively easy (0.14–0.59).

## Contributions
- A fine-grained taxonomy spanning reasoning, planning and system execution, adding API, resource and orchestration errors.
- The first human-annotated, span-localized trace benchmark on OpenTelemetry structured logs, with ecological validity.
- Shows that LLM-as-a-judge over traces fails badly at long context, setting a difficulty baseline for scalable trace evaluation.

## Limitations
- Text-only; drawn from just two benchmarks (GAIA, SWE-bench Lite) and two agent configurations; 148 traces is small.
- Long-tail categories have very few examples, though they are often high-impact; the authors suggest synthetic data.
- Some errors are elicited through prompt constraints and may be distributed differently from natural failures.
- The main text only calls inter-annotator agreement "high" (numbers in the appendix); authored by a company with related commercial products.

## Relation to our direction
Mainly serves **the agent-trustworthiness topic's omics failure taxonomy and verifier design**. (1) **Taxonomy template**: TRAIL's three layers (reasoning / planning & coordination / system execution) can serve directly as the skeleton for omics-specific leaves — reasoning: misused statistical tests, batch or ambient RNA read as biological signal, hallucinated cluster annotations; system execution: reference-genome/annotation version mismatch, memory exhaustion on large h5ad files; planning: skipping QC before DE, cross-modal (snRNA vs snATAC vs Xenium) disagreement left unchecked. (2) **Task form**: TRAIL defines evaluation as "which span is wrong + what type" — closer to claim-to-evidence than "is the final answer right"; our verifier must likewise point to **which analysis step fails to support which claim**. (3) **Difficulty warning**: the best model reaches ~11% joint accuracy and degrades with trace length — omics-agent traces (large tables, long code) will be longer still, so a verifier cannot simply feed the whole trace to one LLM; it needs segmentation, structured retrieval or specialized models. (4) The OpenTelemetry/OpenInference logging format is worth adopting in the agent-trustworthiness topic's rerun experiments for compatibility with TRAIL and HAL tooling. Relation to the artifact-injection topic is looser, but the "every error carries a location and evidence" annotation rule suits KidneyAnomalyBench expert labelling too (anomalies localized to spot / cell / region, with evidence).

## Reusable assets
- **Data:** the TRAIL dataset (MIT).
<https://huggingface.co/datasets/PatronusAI/TRAIL>
- **Taxonomy:** the category definitions in Figure 1 / §3, reusable as the upper levels of an omics-agent failure taxonomy.
- **Annotation format:** the five-field JSON (category / location / evidence / description / impact), directly usable for our trace annotation.

## Follow-ups
- Appendix A.7 for agreement numbers; A.4 for the full reasoning-effort ablation.
- Map against MAST (TRAIL positions itself as filling MAST's missing execution and planning categories).
- Whether follow-up trace benchmarks exist for scientific / bioinformatics agents.

## Cite
```bibtex
@misc{Deshpande2025_250508638,
  title = {TRAIL: Trace Reasoning and Agentic Issue Localization},
  author = {Darshan Deshpande and Varun Gangal and Hersh Mehta and Jitin Krishnan and Anand Kannappan and Rebecca Qian},
  year = {2025},
  eprint = {2505.08638},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2505.08638}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

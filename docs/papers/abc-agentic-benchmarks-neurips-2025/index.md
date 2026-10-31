# Establishing Best Practices for Building Rigorous Agentic Benchmarks

> **Bibkey** `Zhu2025_250702825` · **Venue** NeurIPS 2025 Datasets and Benchmarks Track (2025) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2507.02825> · `status: complete`

---

## One-liner
The authors split "can this agentic-benchmark score be trusted" into two conditions — **task validity** (task success ⇔ the target capability) and **outcome validity** (a positive evaluation ⇔ genuine task success) — and turn them into an actionable **Agentic Benchmark Checklist (ABC)**. Auditing ten popular agentic benchmarks with it, they find 7 violate outcome validity, 7 violate task validity, and all 10 have reporting gaps, with estimation errors of up to 100% in relative terms.

## Problem
Agentic benchmarks differ fundamentally from multiple-choice or text-generation benchmarks: success means completing an end-to-end task, and outcomes are **unstructured artefacts** — code, file edits, environment states, free text — graded by bespoke methods such as unit tests, string matching, state matching or LLM-as-a-Judge. Both the grading and the task setup can be wrong, causing over- or under-estimation. Examples: SWE-bench-Verified's insufficient unit tests make 24% of the top-50 leaderboard positions incorrect; in τ-bench a **trivial agent that returns nothing** passes intentionally impossible tasks, scoring 38% and beating a GPT-4o agent. The field lacked a systematic, actionable audit guideline.

## Method
**Corpus**: 17 agentic benchmarks used by leading AI providers (OpenAI, Anthropic, Amazon, Meta, Google, xAI, Mistral, DeepSeek) or award-winning at venues; combined with documented benchmark issues, agent-evaluation frameworks (e.g. UK AISI's Inspect), software-testing best practice and the authors' own benchmark-building experience (CVE-Bench, etc.) to curate ABC. **Three parts**: (1) **Task validity** (T.1–T.10): tool versions specified; APIs accessible, with evaluation terminating if they fail; residual state cleared between runs; agent fully isolated from ground truth; setup frozen over time (no live websites); ground truth verified; each task verified solvable; an **oracle solver** provided; no exploitable implementation vulnerabilities. (2) **Outcome validity** (O.a–O.i, grouped by outcome type and grading method): string matching must handle semantic equivalents, redundant words and negations and resist "list every answer" and guessing; **LLM-as-a-Judge needs documented accuracy, self-consistency and human-agreement evidence and must resist adversarial inputs**; unit tests manually verified and backed by objective metrics like coverage; fuzzing must cover edge cases, data types and memory layouts; E2E tests must avoid flakiness; state matching must include all achievable success states and check irrelevant states. (3) **Reporting** (R.1–R.13): open data and harness, contamination defences (held-out test set), stated construct validity, documented mitigation plus qualitative and quantitative impact analysis of unavoidable flaws, **confidence intervals**, interpretation guidance, and results for non-AI baselines (human experts) and **trivial agents (one that does nothing)**. **Scoring**: 1 point per satisfied item, averaged over applicable items.

## Data
Ten open-source benchmarks spanning all capability types and grading methods: SWE-bench (unit tests), SWE-Lancer (E2E tests), KernelBench (fuzzing), BIRD (unit tests / answer matching), Cybench (answer matching), MLE-bench (quality metric), GAIA (answer matching), τ-bench (substring + state matching), WebArena (whole/substring matching + LLM judge + state matching), OSWorld (state matching). Case study: CVE-Bench (a cybersecurity benchmark of real-world web-vulnerability exploitation).

## Key results
**Overall**: of 10 benchmarks, 7 violate task validity, 7 violate outcome validity, all 10 fall short on reporting; 80% fail to acknowledge their design/implementation weaknesses and none meets every reporting item. **New findings**: (1) τ-bench uses trivial states/substrings as ground truth (O.b.3, O.g.3), overestimating by 38%, and lets agents list every possible answer (O.b.2), overestimating by 40% — 38% of airline and 6% of retail tasks are intentionally impossible, so doing nothing passes; (2) WebArena's substring matching ignores extraneous content and its LLM judge accepts empty replies on "N/A" tasks without validated accuracy (O.c.1), overestimating by 1.4–5.2%; (3) **SWE-Lancer does not isolate agents from ground truth (T.5)**: tests sit in a password-protected ZIP whose directory can be listed and contents overwritten, so replacing them with `assert 1 == 1` yields **100% without solving any task**; (4) KernelBench's fuzzer varies only tensor values, not shapes or memory layouts (O.e.1/O.e.2), overestimating kernel correctness by ~31% absolute; (5) in OSWorld's chrome section 13/46 tasks are broken by website changes, underestimating UI-TARS by 28% absolute. **CVE-Bench revision**: time-based SQL injection was graded by a SLEEP string in the DB log (O.g.1), overestimating by 32.5%; an outbound server reachable from the same docker network was a shortcut, and fixing it cut success by 10%; overall ABC reduced CVE-Bench's overestimation by 33% absolute, confirmed by security experts.

## Contributions
- Formalizes agentic-evaluation rigour as two equivalence conditions — task validity and outcome validity — with an operational-vs-conceptual process diagram.
- The first item-by-item checklist for agentic benchmarks (task / outcome / reporting), with checks organized by outcome type and grading method.
- Quantifies previously unreported flaws in ten mainstream benchmarks with reproducible experiments.
- Shows with CVE-Bench how ABC is used during benchmark construction, not only post-hoc auditing.

## Limitations
- Binary per-item scoring with equal weights does not reflect differing severity of flaws.
- The audit centres on coding, web, cybersecurity and assistant benchmarks; **no scientific / biomedical-analysis benchmarks**, and no treatment of run-to-run stochasticity (rerun variance).
- The checklist is synthesized from experience and literature without a completeness claim; some items (e.g. adversarial robustness of LLM judges) give principles more than concrete protocols.
- Quantitative findings rest on author-designed validation experiments; numbers are not comparable across benchmarks.

## Relation to our direction
This is the **"evaluation constitution" for the agent-trustworthiness topic**, and it directly constrains **the artifact-injection topic's KidneyAnomalyBench**. For the agent-trustworthiness topic (trustworthy biomedical agents, claim-to-evidence verification, calibrated verifier, rerun stability, omics failure taxonomy, AIRIS WP3 / MLCommons): (1) **outcome validity is exactly what claim verification addresses** — an agent says "PT subcluster X is up in DKD", the grader says correct, but that does not make it true; ABC's O.c.1 (an LLM judge needs evidence of accuracy, self-consistency and human agreement) is precisely what our calibrated verifier must deliver; (2) **a trivial-agent baseline (R.13)** should be standard for omics-agent benchmarks: how much does an agent score that only returns a marker-gene table, or only restates Lake-atlas conclusions? A high score means the task does not measure analysis; (3) T.5 (isolation from ground truth) is acute for omics — a web-enabled agent can simply look up KPMP / Lake findings (HAL observed agents searching HuggingFace for answers); (4) T.6 (frozen environment) maps to pinning database/annotation versions (Ensembl, CellxGene). MLCommons' Rebecca Weiss and Fazl Barez are co-authors, so this checklist shares institutional lineage with AILuminate — the most natural methodological interface when AIRIS WP3 engages MLCommons. For the artifact-injection topic: KidneyAnomalyBench is a benchmark too — it needs T.7 (expert-verified ground truth), T.8/T.9 (each anomaly class verifiably detectable, with an oracle, e.g. injected doublets / ambient RNA), R.12/R.13 (report "everything normal" and "QC-metrics-only" trivial baselines plus a pathologist baseline) and R.10 (confidence intervals). Along detect → model → revert, any evaluation of "anomaly detected" or "reverting target nominated" should pass this checklist before its numbers are trusted.

## Reusable assets
- **Code:** audit experiments and checklist code.
<https://github.com/uiuc-kang-lab/agentic-benchmarks>
- **Website:** continuously updated ABC checklist and audit results.
<https://uiuc-kang-lab.github.io/agentic-benchmarks/>
- **The checklist itself:** T.1–T.10, O.a–O.i, R.1–R.13 can be adapted directly into a design-review form for KidneyAnomalyBench and omics-agent benchmarks.

## Follow-ups
- Appendices D/E (per-benchmark item scores and validation experiments) and F (BIRD as an example of high-quality reporting).
- Apply ABC to the biomedical agent benchmarks this repo is collecting (BixBench, scBench, LAB-Bench, BioML-bench, etc.).
- How the Holistic Agent Leaderboard (overlapping authors) operationalizes these principles in a harness and log analysis.

## Cite
```bibtex
@inproceedings{Zhu2025_250702825,
  title = {Establishing Best Practices for Building Rigorous Agentic Benchmarks},
  author = {Yuxuan Zhu and Tengjun Jin and Yada Pruksachatkun and Andy Zhang and Shu Liu and Sasha Cui and Sayash Kapoor and Shayne Longpre and Kevin Meng and Rebecca Weiss and Fazl Barez and Rahul Gupta and Jwala Dhamala and Jacob Merizian and Mario Giulianelli and Harry Coppock and Cozmin Ududec and Jasjeet Sekhon and Jacob Steinhardt and Antony Kellermann and Sarah Schwettmann and Matei Zaharia and Ion Stoica and Percy Liang and Daniel Kang},
  booktitle = {NeurIPS 2025 Datasets and Benchmarks Track},
  year = {2025},
  eprint = {2507.02825},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2507.02825}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

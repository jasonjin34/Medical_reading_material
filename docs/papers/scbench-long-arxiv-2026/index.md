# scBench-Long: Verifiable Benchmarking of Long-Horizon Single-Cell Biology

> **Bibkey** `Diks2026_260626563` · **Venue** arXiv preprint (2026) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2606.26563> · `status: complete`

---

## One-liner
scBench-Long (LatchBio) moves scBench from single steps to long horizons: 21 evaluations across 5 study systems in which agents start from raw or near-raw single-cell data, with no prescribed method, and must **recover a specific scientific conclusion**, graded deterministically over controlled vocabularies with companion trajectory rubrics for diagnosis. Across 1,068 trajectories the best model–harness pair (Claude Opus 4.8 + Claude Code) passes only 16/63 (25.4%), and failures are mostly **scientific-reasoning failures**, not tool-use failures.

## Problem
Single-cell claims emerge from multi-step workflows that integrate metadata, design and auxiliary evidence (TCR, chromatin, validation experiments); existing benchmarks test broad knowledge, executable workflows or local steps. The long-horizon difficulty is that **verifiable ground truth is hard to define**: the same data support multiple valid claims and published results do not always reproduce. How to constrain admissible answers without penalising valid, unanticipated analysis paths?

## Method
**Organised by study system, not dataset**: each system contributes several evaluations that interrogate the same experiment from different angles (identity, state, regulation, composition, mechanism). **Paper claims are candidate sources, not automatic ground truth**: a task is kept only if its conclusion can be independently reproduced from the staged data and survives review, distractor design and inspection of trajectories from multiple model families. Each task bundles a compact question, raw/near-raw data nodes, auxiliary resources, a controlled answer surface, reproduction notes and trajectory rubrics. **Answer surfaces** use the objects analysts reason with — cell-state identities, donor compositions, regulator and direction labels, clonotype/repertoire claims, ligand–receptor interpretations, and **explicit "mechanism-caution" labels**; distractors separate data-supported conclusions from shortcuts (canonical marker priors, abundance ranking, single-modality answers, unsupported causal readings). **Grading**: typed checks over structured JSON (list/dict matching, field predicates, synonyms, hard-fails for biologically incompatible answers), endpoint-only with any valid path allowed. **Diagnostics**: authors define "chokepoints" after reproduction; four LLM judges score trajectories against rubrics, used **only as diagnostics, never as the score**. **Runs**: 17 model–harness pairs (PI, Claude Code, OpenAI Codex harnesses; Claude, Gemini, GPT, Grok, Kimi, GLM models), three replicates per task, Wilson CIs and any/majority/all robustness counts.

## Data
Five systems, 21 tasks: melanoma tumour-reactive CD8 T cells (5; 10x 5′ scRNA + paired scTCR + sort-gate metadata); CD8 RNA+ATAC regulatory inference (3; 10x Multiome); human–monkey chimeric embryos (4; Smart-seq2, ortholog maps, developmental references, ligand–receptor resources); KRAS-driven lung-tumour aging (4; Parse Biosciences scRNA, external aging signatures); lethal COVID-19 lung pathology (5; snRNA-seq, BCR reconstruction, subset DE, immunohistochemistry). One task deliberately **swaps two metadata labels** (singlet and tumor_cluster) while leaving expression and TCR untouched, to test whether agents follow data rather than labels.

## Key results
**Overall**: Claude Opus 4.8 / Claude Code **16/63 (25.4%; Wilson 95% CI 16.3–37.3)**, Gemini 3.5 Flash / PI 14/63 (22.2%), Opus 4.8 / PI 13/63 (20.6%), Gemini 3.1 Pro / PI 17.5%, GPT-5.5 (Codex or PI) 15.9%, most others 2–11%, lowest Grok 4.3 / PI 1.6%. Only 125 of 1,068 trajectories (11.7%) pass. **Robustness**: the best pair has any-pass on 8/21 tasks, majority-pass on 6/21 and all-three-pass on only **2/21**. **Task spread**: 5 tasks have zero passes; the easiest (a pseudotime-delay task) is 26/51 (51.0%). **Harness effects**: same model, different harness, different results — Opus 4.8 16 (Claude Code) vs. 13 (PI); GPT-5.4 6 (PI) vs. 2 (Codex); GPT-5.5 10/63 under both but **solves different tasks**; 3–6 of 21 tasks change pass count per paired model. **Rubric diagnostics**: mean pairwise judge correlation 0.90 (min 0.87); judge SD 5.5 points per trajectory vs. replicate SD 6.3; passing trajectories average 75.9% rubric vs. 58.7% for failing; association with the endpoint is only Pearson r=0.29, Spearman ρ=0.30, AUC 0.77, and the top rubric decile holds just 47/106 passes — **high rubric scores do not mean correct conclusions**. **Failure modes**: (1) familiar priors masking task evidence (treating CD39/PD-1-high singlets as most tumour-reactive, ignoring physical engagement + clonal expansion; in the label-swap task, "relabelling back" to expected biology); (2) raw abundance mistaken for importance (chimera ligand–receptor task: 2/50 passes; GPT-5.5 and Opus 4.8 0/6); (3) association mistaken for mechanism (tumour–T-cell conjugate task: **no pair passes** — the immune-response programme is decontamination-sensitive and directionally undetermined, yet models assert a directional mechanism); (4) failure to integrate modalities (KLF2 tasks: nominating S1pr5 or Cd160 from RNA DE alone, or inferring KLF2 activity from Klf2 RNA rather than coordinated target behaviour).

## Contributions
- **A claim-conditioned, verifiable long-horizon benchmark**: paper claim → independent reproduction → controlled answer surface + shortcut distractors, addressing the "no gradable truth for long tasks" problem.
- Explicit **"mechanism-caution" answer labels** — making "do not draw a causal conclusion" itself a gradable correct answer.
- A data-perturbation probe (metadata label swap) testing whether agents follow data or labels.
- Quantitative evidence that **rubric/LLM-judge scores ≠ correctness** (AUC 0.77), and a quantified harness effect — agents should be evaluated as model + harness.
- A concrete taxonomy of single-cell reasoning failures (priors over evidence, abundance as importance, association as mechanism, single-modality inference).

## Limitations
- Small: 21 tasks, 5 systems, 3 replicates per pair per task; Wilson CIs are wide (16–37%) and most pairwise differences are not significant.
- Deterministic endpoint grading penalises valid claims outside the pre-specified surface (acknowledged); rubrics are prompt- and judge-dependent.
- No public link to code, tasks or trajectories is given, so external reproduction is hard; authors are at LatchBio (a bioinformatics-platform company).
- No spatial or histology modality; no calibration/confidence dimension — it asks "right or wrong," not "does the agent know it might be wrong."

## Relation to our direction
This is the paper in this batch **most central to Topic 2** — essentially its upstream evidence. **(1) Claim-level evaluation**: it scores not steps but "is this conclusion supported by the data," the same object as our claim-to-evidence verification; its "paper claims are candidates only and must be independently reproduced" pipeline can build a kidney claim set directly (take conclusions from KPMP/Lake/DKD-atlas papers, reproduce them on data we can access, then admit them). **(2) Failure taxonomy**: "priors over evidence / abundance as importance / association as mechanism / single-modality inference" is a starting point for our omics-specific taxonomy, to which kidney adds ambient RNA and batch read as biology, trusting one side when snRNA and Xenium disagree, and treating injury markers as causal drivers. **(3) Rubric score ≠ correctness (AUC 0.77)**: direct support for Topic 2's premise that a **calibrated** verifier is needed rather than another LLM judge; high inter-judge agreement (0.90) with weak correlation to truth shows that "judges agree" is not a proxy for reliability. **(4) Replicates and harnesses**: the best pair passes all three replicates on only 2/21 tasks and the same model solves different tasks under different harnesses — exactly the "rerun stability" Topic 2 wants to quantify, and a reminder that AIRIS WP3 / MLCommons-style reporting should use model + harness as the unit with any/majority/all counts. For **Topic 1**, the KLF2 lesson (RNA alone picks the wrong regulator; chromatin support is needed) shares the logic of using cross-modal agreement to separate artifact from disease: an snRNA anomaly unsupported in snATAC/Xenium should lose confidence.

## Reusable assets
- **Construction protocol:** claim → reproduction → controlled answer surface → shortcut distractors → hard-fails → chokepoint rubrics (Methods), directly usable for a kidney claim set.
- **Reporting convention:** Wilson CIs + any/majority/all robustness counts + paired-harness comparisons.
- **Probe designs:** metadata label swap, decontamination-sensitive programmes, "mechanism-caution" labels.
- **Code/data:** no public link in the paper (the results manifest is named `results/scbench-long-results-w-glm.csv`); watch LatchBio's scBench repo.
<https://github.com/latchbio/scbench>

## Follow-ups
- The sibling benchmarks the authors mention (spatial biology, epigenomics, therapeutics) and BioMysteryBench.
- Which task types from the five source studies (melanoma CD8, CD8 multiome, human–monkey chimera, KRAS lung aging, COVID lung) transfer to kidney.
- What the PI harness is and why it helps some models.

## Cite
```bibtex
@misc{Diks2026_260626563,
  title = {scBench-Long: Verifiable Benchmarking of Long-Horizon Single-Cell Biology},
  author = {Diks, Ian and Yang, Zhen and Banerjee, Arjun and Proctor, Tim and Workman, Kenny},
  year = {2026},
  eprint = {2606.26563},
  archivePrefix = {arXiv},
  primaryClass = {q-bio.GN},
  url = {https://arxiv.org/abs/2606.26563}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

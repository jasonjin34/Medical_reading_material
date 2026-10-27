# LLM-as-a-Judge in Healthcare: A Scoping Analysis of Applications, Methods, and Human Alignment

> **Bibkey** `Li2026_260525273` · **Venue** arXiv preprint (2026) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2605.25273> · `status: complete`

---

## One-liner
A PRISMA-guided scoping review: five databases searched for January 2023 – February 2026, 134 healthcare LLM-as-a-Judge studies included and coded by health scenario, judge configuration, technique and validation design. Judge–expert alignment is **mostly moderate to strong** (median agreement 0.83, median Cohen's κ 0.78, median correlation 0.69) but strongly task-, rubric- and model-dependent, and there are almost no controlled comparisons showing which configuration suits which clinical task.

## Problem
Healthcare LLM outputs are largely unstructured clinical text; expert annotation is the gold standard but slow and costly, BLEU/ROUGE/BERTScore measure lexical similarity rather than medical correctness, and fixed-answer benchmarks miss real-world ambiguity. LLM-as-a-Judge is a scalable alternative whose **validity** in healthcare is underexamined: judges may hallucinate, overrate reasoning, carry bias or share failure modes with the evaluated model. Prior reviews target general-purpose evaluation; the one close review (Li et al., 2026a) focuses on risk and governance. Four RQs: where it is applied, which models and techniques, how judge–human agreement is measured and how high it is, and what the opportunities and failure modes are.

## Method
**Search**: PubMed, Scopus, DBLP, OpenAlex, arXiv; title+abstract terms "LLM/GPT/Gemini/Claude/Llama/Qwen/DeepSeek/agent as (a) judge" AND health terms. **Screening**: 474 after year filter → 287 after exact de-duplication → 273 after similarity de-duplication → 169 after title/abstract screening → 157 full texts retrieved → **134** included after dual full-text screening. **Coding**: an 18-field pre-specified codebook in four groups (bibliographic, study/clinical context, judge configuration, evaluation/validation), including a binary "validated against humans" field. **Framework**: three steps — (1) task and rubric specification (single-output scoring, pairwise comparison, factual consistency against a reference, categorical safety labels); (2) judge configuration and enhancement (prompting, ensembles, RAG, calibration, fine-tuning, distillation, multi-agent); (3) validation and bias mitigation (κ/ICC, Pearson/Spearman, classification metrics, win rates; randomized order, source blinding, length control, repeated judgments).

## Data
134 included studies (7 in 2024, 81 in 2025, 46 in the first two months of 2026; 46 are arXiv preprints). Subsets for alignment synthesis: 13 studies reporting agreement rate, 10 reporting Cohen's κ, 13 reporting correlation (10 Pearson, 3 Spearman).

## Key results
**Applications**: Clinical Decision Support 54 (40.3%; diagnosis/screening 19, mental/behavioural health 18, treatment 8, clinical safety/quality only 5), Clinical NLP 28 (20.9%; documentation 21), Medical Knowledge & QA 24 (17.9%), Medical Communication 22 (16.4%). **Judge models**: OpenAI 90/134 (67.2%; GPT-4o most common at 34), Google 35 (26.1%), Anthropic 27 (20.1%), Meta 25 (18.7%), Qwen 24 (17.9%), DeepSeek 13 (9.7%; DeepSeek-R1 in 11, third most-used single model). **Techniques**: prompting 132/134 (98.5%), ensembles 18 (13.4%), multi-agent 10 (7.5%), fine-tuning 10 (7.5%), calibration 8 (6.0%), RAG 6 (4.5%), distillation 5 (3.7%). **Human alignment**: agreement 0.66–0.96 (median and mean 0.83; lowest GPT-5.2 on fine-grained biomedical entity linking, highest the four-model MedGUIDE ensemble); κ 0.59–0.88 (median 0.78, mean 0.76); correlation 0.40–0.94 (median 0.69, mean 0.68). **Telling details**: one judge reaches 0.83 agreement with at-least-one expert but 0.51 against majority-of-experts; Claude-Opus-4.6 has κ = 0.78 on unperturbed medical concepts but 0.24 on perturbed ones; one study reports 0.80 raw agreement but κ = 0.59 (class imbalance); heterogeneous ensembles cluster at the top (e.g. a three-judge ensemble at 0.90). **Failure modes**: correlated bias from shared model families; mistaking fluency/organization/assertive tone for quality; shallow clinical-semantic reasoning (e.g. chronic vs newly inferred ICD-10 diagnoses); **evaluation hallucination** (judges fabricate flaws or even alter the task); prompt sensitivity and cross-lingual fragility (English → Kinyarwanda degradation).

## Contributions
- The first review to systematically map healthcare LLM-as-a-Judge applications and **judge–human alignment**, with cross-study forest plots of agreement, κ and correlation.
- A three-step framework (task/rubric → configuration → validation/debiasing) and an implementation table for seven technique families.
- Five failure modes, notably "evaluation hallucination" and same-family correlated bias.
- Deployment guidance: risk-stratified evaluation, judge disagreement as an uncertainty signal for human routing, audit logs/versioning/drift monitoring, prospective silent-mode evaluation.

## Limitations
- Heterogeneous metrics, tasks and reference standards preclude pooled estimates; manual coding may suffer from incomplete reporting in source papers.
- Observed variation may reflect study design and reporting quality rather than judge capability; cost, latency, reproducibility and privacy are underreported.
- Fast-moving field with many preprints; may miss the newest frontier models; predominantly English settings.
- **No configuration recommendations** — the authors note no controlled comparison varies judge architecture, prompting or grounding on a fixed clinical task. (Also: the Discussion states "median Cohen's κ between 0.59 and 0.93", inconsistent with the Results' 0.59–0.88 range; the Results figure is used here.)

## Relation to our direction
For **Topic 2** this is the **evidence map for whether the verifier itself can be trusted**. Topic 2's calibrated verifier is essentially an LLM-as-a-Judge (does the evidence support the agent's omics conclusion?), and three lessons must be internalized: (1) **alignment depends heavily on the reference standard** — "0.83 vs any expert / 0.51 vs majority" means KidneyAnomalyBench and Topic 2 annotations need a clearly defined multi-expert consensus protocol, reporting both raw agreement and κ; (2) **collapse under perturbation** (κ 0.78 → 0.24) is exactly the robustness test Topic 2 wants: apply controlled perturbations to agent conclusions (flip direction, cell type, gene) and test whether the verifier catches them — stronger calibration evidence than static agreement; (3) **same-family bias** means the verifier should not share a base model with the evaluated agent, or should report cross-family ensembles. Its treatment of judge disagreement as an uncertainty signal, risk-stratified evaluation, audit logs and drift monitoring can go straight into an AIRIS WP3 / MLCommons-style evaluation protocol. Notably, only 5 of 134 studies address clinical safety/quality and essentially none involve omics or spatial data — "LLM judges for omics-analysis conclusions" is itself an open gap.

## Reusable assets
- **Search string and inclusion/exclusion criteria** (Table 1), reusable for updates or an omics/agent-focused review.
- **18-field codebook** (Appendix Table 4) — a template for Topic 2 literature coding and verifier reporting standards.
- **Technique–implementation table** (Table 2) and the rubric/metric taxonomy (Table 3).
- No code repository (review paper; not applicable).

## Follow-ups
- MedVAL (Aali et al., 2025): a distilled clinical-text judge (κ = 0.67; fine-tuned Qwen3-4B r = 0.833).
- Chung et al. (2025): atomic-claim factuality against EHR evidence (13,290 propositions, 0.89 agreement) — closest in form to Topic 2.
- Shawon et al. (2026): judge collapse on perturbed medical concepts.
- Li et al. (2026a): review of risk validation and governance frameworks for healthcare LLM judges.

## Cite
```bibtex
@misc{Li2026_260525273,
  title = {LLM-as-a-Judge in Healthcare: A Scoping Analysis of Applications, Methods, and Human Alignment},
  author = {Li, Lingyao and Li, Deyi and Chen, Chen and Ma, Renkai and Yu, Runlong and Lin, Mingquan and Yin, Rui and Fan, Lizhou and Shyr, Cathy and Ma, Siyuan and Liu, Mei and Bethard, Steven},
  year = {2026},
  eprint = {2605.25273},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2605.25273}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

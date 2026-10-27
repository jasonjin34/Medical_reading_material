# Generalization bias in large language model summarization of scientific research

> **Bibkey** `Peters_2025` · **Venue** Royal Society Open Science (2025) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1098/rsos.241776> · `status: complete`

---

## One-liner
Across 4,900 summaries from 10 prominent LLMs, most models rewrite restricted scientific conclusions into **broader generalizations** (dropping quantifiers into generics, past into present tense, descriptions into recommendations). LLM article summaries are **4.85× as likely** as expert NEJM Journal Watch summaries to contain generalized conclusions; counter-intuitively, **explicitly asking for accuracy doubles the effect**, and **newer models are worse than older ones** (Claude being the exception).

## Problem
Researchers and the public increasingly use LLM chatbots to summarize science. Beyond outright fabrication, a subtler risk is **omitting qualifiers and uncertainty** so that conclusions are broadened — e.g. turning "dulaglutide at a once-weekly dose of 0.75 or 1.5 mg was superior to placebo in improving glycaemic control through 26 weeks among youths with type 2 diabetes treated with or without metformin or basal insulin" into "dulaglutide is an effective and safe treatment option for improving glycaemic control in youths with type 2 diabetes". In clinical settings this can drive inappropriate prescribing. Three questions: (1) do algorithmic overgeneralizations occur? (2) can prompts emphasizing systematic or accurate processing mitigate them? (3) do LLMs overgeneralize more than human science communicators?

## Method
**Three generalization codes**: (1) **generics** — present-tense claims with no quantifier in the subject that extend results to whole categories ("parental warmth is protective"); (2) **present-tense generalizations** — past-tense sample findings rendered in present tense; (3) **action-guiding generalizations** — descriptive results turned into recommendations ("CBT should be recommended"). Any of these marks a text "generalized", otherwise "restricted". **Overgeneralization**: overall (more generalized LLM summaries than generalized originals) and specific (an original without generalization whose summary has one). Faithfulness to the original is the normative standard; whether the original's generalizations are warranted is not assessed. **Design**: preregistered on OSF; three prompts (simple / "take a deep breath and work step by step" systematic / "do not introduce any inaccuracies" accuracy); temperature 0 vs 0.7 vs UI default; some models retested 2–3 times; UI collection via fresh accounts or memory off. **Analysis**: binomial GLMMs with logit link controlling for temperature, prompt and test round. Two experts in corpus analysis and science communication coded with preregistered criteria; a third, source-blinded researcher recoded 100 texts (κ = 0.79–0.95).

## Data
**Source texts**: 200 abstracts — 100 from the top general medical journals (Lancet, NEJM, JAMA, BMJ) and 100 from multidisciplinary science journals (Nature, Science, Nature Human Behaviour, PSPI), the 25 most recent per journal; plus 100 full-length **prospective clinical study** articles from the four medical journals with their NEJM Journal Watch expert summaries. **Models** (10): GPT-3.5 Turbo, GPT-4 Turbo (API and UI), LLaMA 2 70B, Claude 2 (from January 2024); ChatGPT-4o, ChatGPT-4.5, LLaMA 3.3 70B, Claude 3.5 Sonnet, Claude 3.7 Sonnet, DeepSeek (March 2025). 4,900 summaries total (4,300 abstract-level + 600 article-level).

## Key results
**Pervasive**: all LLMs combined are about **twice** as likely as original abstracts to contain generalized conclusions (B = 0.693, p < 0.001); 6 of 10 models differ significantly from originals. Older GPT-4 Turbo and LLaMA 2 70B ~**2.6×**; newer ChatGPT-4o ~**9×** and LLaMA 3.3 70B ~**39×**; GPT-3.5 Turbo and Claude 2/3.5/3.7 do not differ significantly. Overall overgeneralization: ChatGPT-4o 45–60%, LLaMA 3.3 70B 69–73%, DeepSeek 26–67%, Claude −1% to 20%; specific overgeneralization peaks at 61% (ChatGPT-4o) and 73% (LLaMA 3.3 70B); the most frequent transition is **quantified → generic**. **Temperature**: temperature 0 makes generalized conclusions **76% less likely** than 0.7. **Prompts backfire**: the systematic prompt has no significant effect; the accuracy prompt doubles the odds (OR = 1.90, 95% CI [1.11, 3.26], p = 0.02), and every model except Claude overgeneralizes most under it (the authors liken it to psychological "ironic rebound"). **Stable on retest**: test round has no significant effect (p = 0.57) — a stable algorithmic bias rather than noise. **Human vs LLM**: NEJM JW summaries do not differ from originals; LLM article summaries are **6.72×** as likely as originals (95% CI [4.22, 10.71]) and **4.85×** as likely as NEJM JW (95% CI [3.06, 7.70], p < 0.001) to contain generalized conclusions.

## Contributions
- First systematic quantification of **scope inflation** in LLM science summaries — a subtler "hallucination" distinct from fabrication.
- An operational three-feature coding scheme (generic / present tense / action-guiding) with overall and specific overgeneralization scores, usable as a benchmark for any new model.
- Reveals two counter-intuitive effects — accuracy prompts backfire, newer models are worse — with an RLHF-prefers-confident-broad-answers hypothesis.
- Preregistered design, blinded recoding and GLMM statistics — methodologically rigorous.

## Limitations
- Only three prompts; LLMs were not assigned roles (expert, media office).
- Human–LLM comparison covers only four models and NEJM JW-style expert writers, not all human communicators.
- Mostly medical texts; tendencies may differ by field (foundational vs applied).
- Focuses on overgeneralization (undergeneralization exists but is rarer); does not judge whether originals' generalizations are warranted; model snapshots age quickly.

## Relation to our direction
For **Topic 2**, this defines **the failure most likely to slip past claim-to-evidence verification**: a conclusion that is "supported" in content but **inflated in scope**. The typical omics-agent version: "HAVCR1 up-regulation observed in PT cells of 3 DKD biopsies" becomes "HAVCR1 up-regulation is a hallmark of DKD" or even "HAVCR1 should be targeted" — which NLI-style verification usually marks as entailed. Topic 2's omics failure taxonomy should therefore list **scope inflation** as its own category, borrowing the three features as detection rules: (1) quantifiers/sample restrictions disappear (n, donors, cell type, region); (2) tense/universalization; (3) jumping from association to action — directly relevant to the last step of detect → model → **revert**, where writing "associated" as "a reversible target" is exactly the overgeneralization to stop. Three points apply directly to experimental design: **temperature 0 markedly reduces generalization** (fix and report temperature in agent evaluations); **"be accurate" prompts can backfire** (prompt-level exhortation is not mitigation); **the bias is stable across reruns** — high rerun stability does not mean correctness, so stable systematic bias needs its own measurement. For Topic 1, it is a reminder that anomaly-detection conclusions written into KidneyAnomalyBench labels or papers must keep their sample and modality qualifiers.

## Reusable assets
- **Preregistration, coding criteria and spreadsheets of all generalized conclusions (OSF):**
<https://osf.io/25ct6>
<https://osf.io/q936d/>
- **Three-step benchmark recipe:** have the LLM summarize → classify originals and summaries on the three features → compare to obtain an overgeneralization score (e.g. OAO).
- **Mitigations:** low temperature, avoid "do not be inaccurate" prompts, enforce past-tense reporting (shadow prompting), benchmark models on generalization accuracy.

## Follow-ups
- Peters et al.'s work on overgeneralization by scientists and science journalists (refs 16–18) as a human baseline.
- Zhou et al.'s Nature paper on larger, more instructible models refusing less and giving more authoritative but flawed answers (ref 41).
- Pilot: hand-code omics conclusions written by agents with these three features to estimate the base rate of scope inflation.

## Cite
```bibtex
@article{Peters_2025, title={Generalization bias in large language model summarization of scientific research}, volume={12}, ISSN={2054-5703}, url={http://dx.doi.org/10.1098/rsos.241776}, DOI={10.1098/rsos.241776}, number={4}, journal={Royal Society Open Science}, publisher={The Royal Society}, author={Peters, Uwe and Chin-Yee, Benjamin}, year={2025}, month=Apr }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

# AILuminate: Introducing v1.0 of the AI Risk and Reliability Benchmark from MLCommons

> **Bibkey** `Ghosh2025_250305731` · **Venue** arXiv preprint (2025) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2503.05731> · `status: complete`

---

## One-liner
AILuminate v1.0 is an **industry-standard AI-safety benchmark** built through an open process by the MLCommons AI Risk and Reliability working group (with the AI Verify Foundation): an assessment standard (12 hazard categories), 24,000 English prompts (practice + hidden official sets), an **ensemble evaluator** of fine-tuned guard models with entropy-based tunable thresholds, five-tier grading relative to a "reference system" (Poor → Excellent), and the technical and organizational infrastructure for long-term operation.

## Problem
Generative AI is a black box whose safety can only be tested empirically, yet academic benchmarks are fragmented and hard to sustain. What was missing is a standardized safety benchmark backed by a trusted institution, built on cross-industry consensus, repeatable, and usable for deployment decisions ("should I release / buy / permit this system?").

## Method
**Five components**: (1) **Assessment standard**: 12 hazards in three groups — physical (violent crimes, sex-related crimes, child sexual exploitation, suicide & self-harm, indiscriminate weapons/CBRNE), non-physical (IP, defamation, non-violent crimes, hate, privacy) and contextual (specialized advice — election/financial/health/legal — and sexual content, which can be switched off per application); each defines acceptable vs unacceptable responses as uniform rules for human annotators, following OECD's hazard/risk distinction. (2) **Prompt datasets**: practice and official sets of 12,000 prompts each, 1,000 per hazard, two personas (naive, knowledgeable); the official set is confidential to resist overfitting, with rotatable reserve prompts; 10% of the practice set is public under CC-BY 4.0; produced by three procured suppliers and checked for realism and distribution. (3) **Evaluator**: rather than one off-the-shelf model (which could favour its developer's systems), a "jury" ensemble of fine-tuned open guard models plus prompt-engineered general LLMs; candidate bases included LlamaGuard, WildGuard, AegisGuard, ShieldGemma, Llama and Mistral models; fine-tuning data came from two annotation vendors with three raters and majority vote; each evaluator gets an **entropy-based tunable threshold** to trade false positives against false negatives; the ensemble rule prioritizes the **lowest false-safe rate** and **highest run repeatability**; exact models, data and ensemble logic are **kept confidential** so the ensemble cannot be used as a guard to game a perfect score. Software: the open-source ModelBench. (4) **Grading**: SUT score = % violating responses; **Excellent requires an absolute rate < 0.1%**; other grades use the ratio S* to the reference (≤0.5 Very Good, 0.5–1.5 Good, 1.5–3 Fair, ≥3 Poor); the reference is the worse of the two best-scoring "accessible" systems (< 15B parameters, relatively open weights). (5) **Integrity**: no selective refusal tuned to hazard topics, mandatory version labelling, advertised systems must match tested system prompts/weights/safety settings, with permanent bans for violations.

## Data
24,000 single-turn English prompts (12 hazards × 1,000 × practice/official); French, Hindi and Simplified Chinese sets built by suppliers via machine translation plus human revision, planned for later release. Exploratory studies add Tattle Civic Tech's Hindi prompts (1,000 each for hate and sex-related crimes), Stanford Brainstorm's clinical annotation of suicide & self-harm, PRISM Eval's adaptive jailbreak tool BET, gender-bias prompt pairs, a 774-prompt text-to-image pilot and an image-to-text pilot.

## Key results
This is a method and infrastructure report; **official SUT results are not in the paper** (they are published at mlcommons.org/ailuminate and excluded because they may be updated live); initial SUTs include Anthropic, Google, Meta and OpenAI systems, with OLMo v1.0 as a control. Quantitative findings in the paper come mainly from exploratory studies: PRISM Eval's BET **raised prompt effectiveness from 8% to 78% in fewer than five optimization steps**, and jailbreak techniques effective on one system were often ineffective on others — static benchmarks struggle to measure jailbreak resistance. In the image-to-text pilot, commercial systems were generally < 1% unsafe while open systems reached 14%, some open systems being "**safe by accident**" (misunderstanding rather than recognizing and refusing), and no automatic evaluator accurately reproduced human safety judgements. The key methodological conclusion: **evaluator error is currently the largest source of uncertainty**; because the evaluator is tuned for a low false-safe rate it has a high false-unsafe rate, so the paper derives upper/lower score bounds (an error band) from these rates, and one result's band can span several grades; the reference system shares the same bias, partly cancelling the effect on grades.

## Contributions
- The first AI-safety benchmark produced by an open, cross-industry consensus process and maintained long-term by a nonprofit, with procurement, governance and integrity policies.
- A practice / hidden official / reserve three-tier data design against overfitting.
- A "jury" evaluator ensemble with entropy-based tunable thresholds, optimizing first for low false-safe rate.
- Reference-relative grading that turns violation rates into decision grades for non-experts, explicitly analysing how evaluator error propagates into grades.

## Limitations
- Single-turn, text-only, English (US) only; no expert adaptive attackers; the standard reflects US cultural norms and lacked a public-comment period.
- **Explicitly excludes "inaccurate medical advice"**: the specialized-advice hazard only requires a disclaimer and does not check correctness.
- Evaluator models, data and ensemble logic are confidential, preventing independent verification; evaluator uncertainty is large and error bands can span grades.
- Hazard scores assume an unsafe response belongs only to its prompt's category.
- Evaluates chat SUTs only — **not agents or tool use**.

## Relation to our direction
This is **the core reference for Plan B's AIRIS WP3 / MLCommons engagement**. AILuminate is MLCommons' most mature "benchmark-as-standard" product; if Plan B wants "claim-to-evidence trustworthiness of omics agents" to become an evaluation MLCommons can adopt, the cheapest route is to **reuse its skeleton**: (1) **assessment standard** ↔ an omics-claim standard (e.g. supported / unsupported / contradicted / unverifiable, plus omics-specific violations such as misused statistics, batch effect read as biology, artifact read as disease), written as explicit acceptable-vs-unacceptable rules for expert annotators; (2) **practice + hidden official + reserve sets** ↔ public KPMP / Lake / HuBMAP data as the practice set and the in-house 95-biopsy snRNA/snATAC/Xenium + H&E as the hidden set, leak-resistant by construction; (3) **jury evaluator + entropy thresholds + false-safe as the primary metric** ↔ our calibrated verifier: treat "a wrong claim judged supported" as the primary error to control (the analogue of false-safe), tune conservativeness with entropy/confidence thresholds, and, as in §6.3, derive an error band from the verifier's error rates — calibration made concrete at the benchmark level; (4) **reference-relative grading** ↔ grades expressed as "how much better than a strong open-agent baseline", not raw scores. More important is **the gap it leaves**: AILuminate explicitly does not test inaccurate medical advice (only disclaimers) and does not test agents or tool use — "is a biomedical analysis conclusion supported by evidence" falls squarely in that gap, which is Plan B's most persuasive positioning when proposing to MLCommons. Relation to Plan A is looser, but "expert annotation rules + hidden test set + error band" transfers directly to KidneyAnomalyBench design.

## Reusable assets
- **Code:** ModelBench (the full run / evaluate / report software).
<https://github.com/mlcommons/modelbench>
- **Data:** 10% of the practice prompts (CC-BY 4.0); the full practice set on request.
<https://github.com/mlcommons/ailuminate>
- **Standard and results:** hazard taxonomy, evaluation guidelines and SUT grades.
<https://mlcommons.org/ailuminate/>
- **Design patterns:** the grading table (Table 3), reference-system definition, error-band derivation, and Appendix A's failure-mode mitigation questionnaire (adaptable as an integrity registry for an omics benchmark).

## Follow-ups
- The full assessment standard (mlcommons.org/ailuminate/methodology), especially annotation rules for specialized advice (health).
- Whether MLCommons has an agentic-reliability version or a healthcare-domain follow-up.
- The AILuminate v0.5 report, to compare design changes from v0.5 to v1.0.
- Cross-reference with the ABC checklist (also with MLCommons co-authors).

## Cite
```bibtex
@misc{Ghosh2025_250305731,
  title = {AILuminate: Introducing v1.0 of the AI Risk and Reliability Benchmark from MLCommons},
  author = {Shaona Ghosh and Heather Frase and Adina Williams and others},
  year = {2025},
  eprint = {2503.05731},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2503.05731}
}
```
(Full list of 102 authors in `citation.bib`.)


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

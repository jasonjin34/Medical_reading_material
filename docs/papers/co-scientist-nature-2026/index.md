# Accelerating scientific discovery with Co-Scientist

> **Bibkey** `Gottweis_2026` · **Venue** Nature (2026) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1038/s41586-026-10644-y> · `status: complete`

---

## One-liner
Google's Co-Scientist is a Gemini 2.0–based multi-agent "structured scientific thinking engine": a Supervisor schedules six agent types — Generation, Reflection, Ranking, Proximity, Evolution, Meta-review — over an asynchronous task queue, self-improving hypotheses through "generate–debate–evolve" plus an Elo tournament as test-time compute scales. It is wet-lab validated in three settings: AML drug repurposing (KIRA6 IC50 10 nM in KG-1a, an 18-fold window over a non-AML control), liver-fibrosis epigenetic targets (2 of 3 active in human hepatic organoids) and the bacterial cf-PICI mechanism (an unpublished finding independently recapitulated in 2 days).

## Problem
Research faces a breadth–depth conundrum: topics demand ever deeper expertise while breakthroughs often come from broad cross-disciplinary links, and the literature explosion makes both hard for individuals. Existing LLM tools mostly stop at summarization and deep research; the question here is whether an AI system can **generate genuinely novel, testable hypotheses and protocols**, improve them steadily by scaling inference-time compute, and survive wet-lab tests.

## Method
**Four components**: a natural-language interface (scientists set goals, constraints, feedback, or submit their own hypotheses), an asynchronous task framework (the Supervisor manages the queue and allocates resources), specialized agents, and a persistent context memory (long-horizon reasoning and restart on failure). The research goal is parsed into a research-plan configuration (preferences, constraints, evaluation criteria); default criteria are alignment with the goal, plausibility, novelty, testability and safety. **Six agents**: Generation (web literature search, simulated expert debate, iterative identification of testable intermediate assumptions, research expansion guided by meta-review feedback); Reflection (a simulated peer reviewer — a tool-free initial review to discard quickly, a full review with search, a **deep verification review that decomposes a hypothesis into assumptions and sub-assumptions and evaluates each independently**, an observation review testing whether it explains long-tail observations, a simulation review stepping through the mechanism or experiment, and a tournament review absorbing recurring issues); Ranking (an Elo tournament, new hypotheses start at 1,200; top hypotheses are compared pairwise via multi-turn scientific debate to reduce ordering bias, lower-ranked ones via single-turn comparison; similar hypotheses are matched preferentially via Proximity); Proximity (a similarity graph for de-duplication and clustering); Evolution (grounding enhancement, feasibility improvement, combination, simplification, out-of-box thinking — **it creates new hypotheses rather than overwriting old ones**, which must re-enter the tournament); Meta-review (synthesizes recurring patterns across reviews and debates into feedback appended to other agents' prompts — "learning" without back-propagation — and writes the final research overview). The architecture is model-agnostic; Gemini 2.0 is used here.

## Data
**Automated evaluation**: 203 research goals entered by 3 Feb 2025 (mostly biomedicine, also mathematics and physics), split into 10 temporal buckets to track Elo; a subset of 15 hard goals curated by seven biomedical experts (postdocs/faculty), compared in Elo against the experts' "best guess" and Gemini 2.0 Pro / Flash Thinking, OpenAI o1, o3-mini-high and DeepSeek R1; blinded expert evaluation on 11 goals. **Wet lab**: AML — repurposing candidates from 2,300 approved drugs across 34 cancer types, tested in four AML lines (MOLM-13, KG-1a, HL-60, NOMO-1) plus the non-AML lymphoblastoid line TK6; liver fibrosis — human hepatic organoids with live-cell imaging; AMR — the host-range mechanism of cf-PICIs.

## Key results
- **Test-time compute scaling**: across 203 goals, best and top-10 mean Elo rise steadily with compute, with no saturation; on the 15 hard goals Co-Scientist eventually clearly surpasses other frontier LLMs/reasoning models and the experts' best guesses (o3-mini-high and DeepSeek R1 are competitive at far lower compute); seeded with expert best guesses it improves them beyond its self-generated solutions in Elo (preliminary).
- **Blinded expert evaluation** (11 goals): Co-Scientist has the best mean preference rank, 2.36 (1 best, 4 worst), and the highest novelty 3.64/5 and impact 3.09/5; all four LLM judges also prefer its outputs. The authors stress these are subjective and small-scale.
- **Ablations**: giving Reflection search tools effectively prevents hallucinated "novel but implausible" hypotheses; a scientific-debate prompt in Ranking substantially improves ranking and reduces positional bias; Evolution's iterative refinement substantially boosts quality.
- **AML repurposing (expert-in-the-loop)**: 30 top-ranked candidates went to oncologists, who picked five (binimetinib, pacritinib, cerivastatin, pravastatin, dimethyl fumarate); binimetinib, pacritinib and cerivastatin inhibited viability; binimetinib reached IC50 as low as 2 nM in AML lines except NOMO-1, and was much higher in TK6.
- **Autonomous AML single agents (no DepMap, no expert feedback, no prior preclinical evidence required)**: experts took three from the ranking (nanvuranlat, KIRA6, leflunomide); the IRE1α inhibitor KIRA6 had IC50 10 nM in KG-1a, 144 nM in NOMO-1, 870 nM in HL-60, 1,750 nM in MOLM-13 and 180 nM in TK6 — ~18-fold between KG-1a and TK6; the other two had limited effect. The system rated KIRA6's novelty "moderate" (IRE1α in AML is known, this drug is not).
- **Combinations**: seven proposed combinations were mostly synergistic in MOLM-13 (e.g. JNJ-64619178 + selinexor; JQ1 + olaparib + MSA2) but mixed synergy/antagonism in TP53-mutant KG-1a.
- **Liver fibrosis**: experts picked three epigenetic-modifier targets and drugs from the ranking; two showed significant anti-fibrotic activity in human hepatic organoids without toxicity, one being vorinostat, FDA-approved for a cancer indication. **AMR**: from minimal background, the top-ranked hypothesis — cf-PICIs interact with diverse phage tails to broaden host range — matched co-timed unpublished experimental findings, in 2 days.

## Contributions
- Brings the test-time-compute scaling paradigm to scientific hypothesis generation: asynchronous multi-agent + self-play debate + Elo tournament + evolution, with quality rising steadily with compute.
- Reflection's multiple review modes — especially **deep verification (decompose into assumptions and sub-assumptions and check each)** — a concrete engineering form of decomposition-based claim verification.
- Meta-review appends recurring critique patterns to prompts, achieving cross-round "learning" without fine-tuning.
- End-to-end wet-lab validation in three biomedical settings of increasing complexity, with scientists kept in the loop.

## Limitations
- **Evaluation leans on self-computed Elo**, which is not ground truth; the blinded expert evaluation covers only 11 goals with subjective ratings; the authors themselves call for more objective, automated metrics.
- Wet-lab validation is preliminary: cell-line viability checks with few candidates hand-picked by experts (selection bias), not in vivo efficacy; the authors note binimetinib showed limited monotherapy efficacy in a prior phase II trial.
- Access only to open-access literature and no negative results; mixed-quality sources risk propagating erroneous or irreproducible findings; the authors list **provenance that traces claims to specific figures or data in a source** as a key future direction.
- Inherits base-model hallucination and factuality issues; cannot yet reason directly over public databases and multimodal data or do data analysis (future work).

## Relation to our direction
Within detect → model → revert, Co-Scientist maps to the **nomination step of revert**: given a disease and constraints, propose targets/drugs that could pull the pathological phenotype back to normal, then test in the wet lab — its liver-fibrosis case (anti-fibrotic epigenetic targets in human hepatic organoids) is nearly isomorphic to "targets that reverse kidney interstitial fibrosis." But it consumes literature, not data, so it cannot use the anomalous regions and virtual-tissue perturbation results from our detect/model stages; a natural interface is to feed our spatial-omics anomalies and perturbation predictions in as research-goal context and as evidence for Reflection's observation review. For **the agent-trustworthiness topic** it is a key comparator: **(1) self-scored Elo ≠ correctness** — the system grades its own hypotheses in its own tournament, exactly the step the agent-trustworthiness topic wants to replace with an external, calibrated verifier; **(2) deep verification's "decompose into assumptions + check each"** is isomorphic to our claim-to-evidence verification, except it checks literature premises while we check whether an agent's conclusions about kidney-omics data are supported by the data and code; **(3) the provenance gap the authors name** (tracing claims to specific figures/data) is the agent-trustworthiness topic's starting point; **(4) its novelty self-rating** (KIRA6 "moderate") is a testable calibration question — do the system's novelty/confidence scores agree with experts? — suitable for evaluating a calibrated verifier. Also, every wet-lab candidate was expert-filtered, so reported "hit rates" mix in human selection; agent evaluation must separate human and machine contributions.

## Reusable assets
- **Paper and preprint:** open Nature full text and arXiv 2502.18864 (earlier version, useful for diffing). The extracted text gives no public code link — open-source status unconfirmed; check the article's Code availability statement.
<https://arxiv.org/abs/2502.18864>
- **Borrowable designs:** Reflection's six review modes (especially deep verification), Elo tournament with debate-style pairwise comparison, Evolution's "add, never overwrite," and the Meta-review prompt-feedback loop.
- **Eval protocol:** expert-curated goals + expert best guesses in the same Elo pool + blinded rating (5-point novelty/impact + preference rank) + cross-checking with LLM judges.

## Follow-ups
- The contemporaneous Robin (`robin-nature-2026`) and Kosmos (`kosmos-arxiv-2025`) — one adds a data-analysis loop, the other a world model for long-horizon data-driven discovery — contrasting "literature only" with "literature + data analysis."
- The companion liver-fibrosis paper (Guan et al., hepatic organoids) and the AMR companion (Penadés lab, cf-PICIs), for wet-lab details and the human–AI division of labour.
- The deep-verification examples in Supplementary Notes 10.6/10.7, as claim-decomposition templates.

## Cite
```bibtex
@article{Gottweis_2026, title={Accelerating scientific discovery with Co-Scientist}, volume={655}, ISSN={1476-4687}, url={http://dx.doi.org/10.1038/s41586-026-10644-y}, DOI={10.1038/s41586-026-10644-y}, number={8122}, journal={Nature}, publisher={Springer Science and Business Media LLC}, author={Gottweis, Juraj and Weng, Wei-Hung and Daryin, Alexander and Tu, Tao and Sirkovic, Petar and Myaskovsky, Artiom and Glowaty, Grzegorz and Weissenberger, Felix and Orlandi, Alessio and Popovici, Dan and Palepu, Anil and Rong, Keran and Tanno, Ryutaro and Saab, Khaled and Zhang, Fan and Blum, Jacob and Carroll, Andrew and Kulkarni, Kavita and Tomašev, Nenad and Zverinski, Dina and Rendulic, Ivor and Vedadi, Elahe and Hasler, Florian and Rimanic, Luka and Boia, Marina and Budiselic, Ivan and Feinstein, Ben and Bellaiche, Mathias and Sheffer, Tom and Freyberg, Jan and Ratcliff, Jeremy and Bertolli, Ottavia and Chou, Katherine and Hassidim, Avinatan and Gokturk, Burak and Vahdat, Amin and Guan, Yuan and Dhillon, Vikram and Vaishnav, Eeshit Dhaval and Lee, Byron and Costa, Tiago R. D. and Penadés, José R. and Peltz, Gary and Matias, Yossi and Manyika, James and Hassabis, Demis and Xu, Yunhan and Kohli, Pushmeet and Pawlosky, Annalisa and Karthikesalingam, Alan and Natarajan, Vivek}, year={2026}, month=May, pages={487–496} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

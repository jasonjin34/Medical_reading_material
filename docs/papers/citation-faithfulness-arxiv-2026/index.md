# Evaluating and Guarding Citation Faithfulness in Agentic Scientific Synthesis

> **Bibkey** `Goo2026_260720527` · **Venue** arXiv preprint (2026) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2607.20527> · `status: complete`

---

## One-liner
Literature-synthesis agents like OpenScholar and PaperQA2, and their benchmarks, all check whether citations hold — but nobody audits whether **the checker itself** is reliable. This paper shows that on identical agent outputs the unsupported-citation rate ranges from **~3% to ~18%** depending only on verifier strictness; verifiers agree on what is supported but barely agree on what to flag (negative-specific agreement 0.27–0.30). The authors give a **gold-anchored evaluation protocol** and a **split-conformal guard** that places a distribution-free, finite-sample guarantee on the catch rate of truly unsupported citations, and show that whether the guarantee transfers is governed by **calibration-negative difficulty**.

## Problem
Three gaps: (G1) the reported unsupported-citation rate is verifier-dependent, so one number does not compare across studies; (G2) verifiers disagree on what to flag, so no deployment flag set can be trusted; (G3) no method gives a distribution-free guarantee on how many truly unsupported citations slip past a chosen flagging rule. The contribution is not the known observation that model graders are imperfect, but its consequence for benchmarking and a remedy.

## Method
**Formalism**: answers decompose into claim–citation pairs (c, pᵢ); a verifier gives a binary v(c,p) and a continuous score s(c,p) ∈ [0,1] (probability of support); gold labels y(c,p) exist only on benchmarks. **Three gold anchors**: (1) validate the verifier against gold, not by reputation; (2) measure re-attribution against gold supporting passages; (3) calibrate the guarantee on gold. **The verifier as a swappable instrument**: compare verifiers at a **matched catch rate** rather than native thresholds; given comparable separation choose on cost — the local 3B AttrScore. **Guard** (per cited sentence): verify (AttrScore-3B, claim vs cited passage) → if unsupported, re-attribute (rank other provided passages, propose a replacement pointer, **re-verify** before moving it; the sentence is unchanged) → what cannot be repaired is **flagged [N UNVERIFIED], not deleted**. **Split-conformal threshold**: on gold calibration **unsupported-class** scores, τ = s₍ₖ₎ with k = ⌈(n_cal+1)(1−α)⌉; flag every s ≤ τ, giving Pr[s_new ≤ τ] ≥ 1−α under exchangeability (Proposition 4.1, with proof; ties broken conservatively). The guarantee is on **catch rate (the safety axis)**, not conclusion correctness. **Re-attribution ranker** is swappable: deterministic BM25 by default, compared with the verifier score and the generators' self-attribution.

## Data
**Systems audited**: four open 27–35B instruction models (two Gemma-4, two Qwen3.6; two dense, two MoE) run locally on one GPU; three pipelines: bare (no-retrieval floor), OpenScholar, PaperQA2; **retrieval context held fixed** with each system's published prompting, so only generation-time citation behaviour is measured; deployment outputs from ScholarQABench multi-paper tasks. **Five verifiers**: AttrScore-3B (high recall), OpenScholar post-hoc judge, GPT-4o, RAGAS, DeBERTa-NLI (high specificity). **Gold**: SciFact (208 test pairs + a disjoint 802 split for prompt selection / held-out validation); full QASA test set, 1,375 supported + 1,375 unsupported pairs (re-attribution and conformal calibration); PubMedQA 843 (scope control). Every headline number carries bootstrap or Wilson 95% CIs.

## Key results
**Verifier frontier (SciFact)**: supported-class recall / specificity — AttrScore-3B 0.90 / 0.54, OpenScholar post-hoc 0.50 / 0.92, GPT-4o 0.46 / 0.92, RAGAS 0.30 / 0.96, DeBERTa-NLI 0.25 / 0.97; AttrScore recall 0.94 on the held-out 802. ROC-AUCs overlap: AttrScore 0.88 [0.84, 0.93], DeBERTa 0.90 [0.85, 0.94], GPT-4o 0.87 [0.82, 0.92] — **a strict frontier judge (GPT-4o) buys no separation advantage**. Gold score means: supported 0.54 vs unsupported 0.20. **Rate is verifier-dependent**: identical outputs climb from ~3% (bare, high-recall verifier) to ~14–18% under strict NLI; agentic pipelines sit a few points above bare at each setting; most of the climb is strict verifiers **falsely rejecting genuinely supported citations**. **Disagreement**: on 300 deployed sentences, pairwise positive-specific agreement 0.90–0.96 but negative-specific only 0.27–0.30 — **60–80%** of citations one verifier flags another calls supported. **Conformal guarantee (QASA)**: targets 0.90/0.94/0.98 → held-out achieved 0.90/0.94/0.98; at calibration size 25 a naive empirical quantile under-covers (0.85 at a 0.90 target) while conformal holds (0.92), converging by ~200. **Transfer condition**: QASA calibration negatives are easy in-paper distractors (mean 0.20), whereas real mis-citations (SciFact human unsupported) average 0.50 — a τ calibrated on QASA for 90% catches only **37%** of the hard negatives (44% and 61% at 94% and 98% targets); recalibrating on target-domain negatives restores the guarantee at a higher review budget. **Review budget (90% guarantee)**: pooled flag rate bare 2.5%, OpenScholar 3.3%, PaperQA2 6.1% (cells up to e.g. PaperQA2 + Qwen3.6-35B 9.5% [6.5, 13.8]), rising with pipeline agency. **Re-attribution (QASA recall@1)**: Gemma-4-26B 0.76, Gemma-4-31B 0.74, **BM25 0.69 (CPU)**, verifier score 0.58, Qwen3.6 0.51–0.52, random 0.03; on the high-overlap half BM25 and Gemma tie (0.88), on the lowest-overlap quartile BM25 0.31 vs Gemma 0.53. BM25 cannot tell support from refutation (answer–refuting passage Jaccard 0.064 vs 0.055 on SciFact), hence verifier re-checking (0.83 vs 0.50). **Scope control**: PubMedQA (yes/no conclusions) κ = 0.02 — the guard checks "does the passage support the claim", **not whether the conclusion is correct**.

## Contributions
- Quantifies that citation-faithfulness metrics **depend on the verifier's operating point** and that verifiers barely agree on what to flag — cross-paper comparisons without a named verifier and protocol are invalid.
- A gold-anchored protocol (verifier validation, re-attribution and guarantee calibration all against human gold, not another model).
- Split-conformal calibration turns a moderate-agreement verifier into a **finite-sample, distribution-free catch-rate guarantee**, with "declare a tolerance → fix the review budget in advance" as the operating mode.
- Identifies and quantifies the condition governing transfer — **calibration-negative difficulty** — with a recalibration recipe (untested by prior conformal-factuality work, per the authors).
- An MIT-licensed single-GPU (80 GB) / CPU open audit kit.

## Limitations
- The demonstrated guarantee is **in-distribution** (QASA); it is optimistic for real mis-citations (37% vs a declared 90%), so deployments must recalibrate on target-domain negatives.
- Coverage is **marginal** over the calibration draw; an individual split can fall below target.
- Retrieval held fixed — only generation is audited, not errors from each agent's own retrieval.
- Checks only "does one passage support the claim" — not contradiction, selective citation or conclusion correctness (named as next steps).
- Does not handle agents optimized against the verifier; only 27–35B open models are audited.
- The authors warn that truncating passages to a prefix inflates the unsupported rate severalfold; sliding windows over full passages are required.

## Relation to our direction
This is almost a prototype of **Topic 2's "calibrated verifier"**, and methodologically very close to our plan: **(1) the stance that the verifier is an instrument to be validated** is exactly what we should adopt for kidney omics — never report "X% of the agent's claims are unsupported" without naming the verifier, the gold it was validated on, and its operating point. **(2) The split-conformal catch-rate guarantee** ports directly: replace claim–citation pairs with claim–evidence pairs (evidence can be a paper passage or the statistics/plots the agent actually computed), calibrate τ on expert gold, and promise "missed unsupported claims ≤ α" with a review budget declared in advance. **(3) Calibration-negative difficulty** is especially important for us: the hard errors in kidney omics (calling an ambient-RNA contamination signal a disease feature, reading a Xenium segmentation artifact as a cell state) are nothing like easy distractors — gold negatives must come from real agent errors (and can share the annotation pipeline with Topic 1's expert-validated KidneyAnomalyBench). **(4) The scope control** (the guard does not check conclusion correctness; PubMedQA κ = 0.02) reminds us that claim-to-evidence verification and "is the conclusion true" are two layers; the omics verifier needs the second layer — is the evidence (the data) itself reliable — which Topic 1's cross-modal agreement can provide. Complementary to citation-blame-emnlp-2026: that paper **localizes** which agent erred; this one gives the verifier's judgements a **statistical guarantee**.

## Reusable assets
- **Code (MIT, single-GPU/CPU audit kit):**
<https://github.com/GooTec/citation-guard>
- **Method:** compare verifiers at matched catch rate; split-conformal τ = s₍⌈(n+1)(1−α)⌉₎ on the unsupported class; verify → re-attribute → flag; mark [N UNVERIFIED] rather than delete.
- **Reporting norms:** per-class recall/specificity, negative-specific agreement (not κ alone, avoiding the kappa paradox), CIs everywhere.
- **Gold data:** SciFact, QASA, PubMedQA; deployment outputs from ScholarQABench.

## Follow-ups
- How OpenScholar (Asai et al., Nature 2026) and PaperQA2 (paperqa2-arxiv-2024) evaluate citations.
- Conformal factuality (Mohri & Hashimoto), conformal abstention (Abbasi-Yadkori et al. 2024), AttributionBench, AttrScore.
- Medical citation auditing, SourceCheckup (sourcecheckup-natcommun-2025), as the medical-domain comparator.
- The authors' next step: from "does a passage support" to "does the full body of cited evidence justify the claim", handling contradiction and selective citation.

## Cite
```bibtex
@misc{Goo2026_260720527,
  title = {Evaluating and Guarding Citation Faithfulness in Agentic Scientific Synthesis},
  author = {Taewan Goo and Junsik Kim and Kyulhee Han and GwonYul Jo and Jong-Soo Kim and Tae-Hyung Kim},
  year = {2026},
  eprint = {2607.20527},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2607.20527}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

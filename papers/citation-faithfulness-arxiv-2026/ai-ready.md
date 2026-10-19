<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# Evaluating and Guarding Citation Faithfulness in Agentic Scientific Synthesis

- **Authors:** Goo, Taewan; Kim, Junsik; Han, Kyulhee; Jo, GwonYul; Kim, Jong-Soo; Kim, Tae-Hyung
- **Affiliations:** BioNexus (Suwon, Republic of Korea); Seoul National University
- **Venue / Year:** arXiv preprint · 2026 (v1 2026-07-10; "Manuscript submitted to ACM")
- **arXiv:** 2607.20527
- **URL:** https://arxiv.org/abs/2607.20527
- **Code:** https://github.com/GooTec/citation-guard (MIT)
- **Bibkey:** Goo2026_260720527
- **Status:** complete (extract from arXiv v1 main text; supplementary S1–S6 not extracted)

## Abstract
Agentic LLM systems such as OpenScholar and PaperQA2 read the scientific literature and return cited answers, and both they and their benchmarks already check whether those citations hold, with a fixed attribution model or human graders. Neither audits the reliability of that check itself. We show it is not reliable, and that this matters. On identical agent outputs the measured unsupported-citation rate ranges from about 3% to about 18% depending only on the verifier's strictness, and although verifiers agree on which citations are supported, they disagree on which to flag (negative-specific agreement 0.27 to 0.30), so no single flag set is trustworthy and cross-paper comparison is invalid without a named verifier and protocol. We present a gold-anchored evaluation protocol and a deployable guard that make this behavior measurable and bounded. The protocol validates the verifier, measures re-attribution, and calibrates a guarantee against human gold rather than another model's verdict; the verifier is a swappable instrument chosen on cost (recall 0.94 on the supported class, held out), and re-attribution is a commodity step where a deterministic BM25 matches the best open generator. The guard adds a split-conformal layer placing a distribution-free, finite-sample bound on truly unsupported citations that slip past a chosen flagging rule, a guarantee on catch rate rather than conclusion correctness. The bound holds on held-out gold, and we identify and quantify the condition governing its transfer to deployment, calibration-negative difficulty, with a concrete recalibration recipe, left untested by prior conformal-factuality work. Validated across four open 27-35B models and three agentic pipelines on public benchmarks (SciFact, QASA, PubMedQA), with confidence intervals on every headline number, the protocol and guard ship as an open single-GPU kit.

## Full text / Extract

### Gaps
(G1) The reported unsupported-citation rate is verifier-dependent, so a single number does not compare across studies. (G2) Verifiers agree on what is supported but disagree on what to flag, so no single deployment flag set can be trusted. (G3) No method places a distribution-free guarantee on how many truly unsupported citations slip through a chosen flagging rule.

### Definitions
Claim–citation pair (c, pᵢ); verifier v(c, p) ∈ {0, 1}, optional continuous score s(c, p) ∈ [0, 1] (probability of support); gold label y(c, p) (benchmark only); tolerance α, target catch rate 1 − α; flag if s(c, p) ≤ τ. The unsupported-citation rate is meaningful only together with the verifier and protocol that produced it.

### Conformal guard
Per cited sentence: verify with AttrScore-3B; if unsupported, re-attribute to another provided passage (rank, propose, re-verify before moving the pointer; claim text unchanged); otherwise flag ([N UNVERIFIED]) rather than delete. Threshold τ = s₍ₖ₎ with k = ⌈(n_cal + 1)(1 − α)⌉ over sorted calibration unsupported-class scores. Proposition 4.1: if calibration unsupported scores and a fresh unsupported score are exchangeable, Pr[s_new ≤ τ] ≥ 1 − α (standard split-conformal argument; ties broken conservatively).

### Setup
Generators: four open 27–35B instruction-tuned models (Gemma-4 ×2, Qwen3.6 ×2; dense and MoE) run locally on one GPU. Pipelines: bare (no-retrieval floor), OpenScholar, PaperQA2; retrieved context held fixed and published prompting reproduced. Deployment citations: ScholarQABench multi-paper tasks. Verifiers: AttrScore-3B, OpenScholar post-hoc judge, GPT-4o, RAGAS, DeBERTa-NLI. Gold: SciFact (n = 208 test; disjoint n = 802 for prompt selection / held-out validation), QASA full test set (n = 1375 supported + 1375 unsupported), PubMedQA (n = 843, scope control). Metrics: per-class recall and specificity, Cohen's κ with bootstrap 95% CIs, unsupported rates, re-attribution recall@k with binomial/Wilson CIs, conformal catch rate vs target.

### Verifier frontier on SciFact gold (Table 2)
| Verifier | Recall (supported) | Specificity |
|---|---|---|
| AttrScore-3B (adopted) | 0.90 | 0.54 |
| OpenScholar post-hoc | 0.50 | 0.92 |
| GPT-4o | 0.46 | 0.92 |
| RAGAS | 0.30 | 0.96 |
| DeBERTa-NLI | 0.25 | 0.97 |

ROC-AUC: AttrScore-3B 0.88 [0.84, 0.93], DeBERTa-NLI 0.90 [0.85, 0.94], GPT-4o 0.87 [0.82, 0.92]. AttrScore held-out recall 0.94 (n = 802). Gold score means: supported 0.54, unsupported 0.20.

### Verifier-dependent rate and disagreement
Same outputs: ~3% unsupported at the bare floor under the high-recall verifier, rising to ~14–18% under a strict NLI judge; agentic pipelines a few points above the floor at each setting; much of the climb is strict verifiers falsely rejecting supported citations. On 300 deployed cited sentences, AttrScore-3B, DeBERTa-NLI and GPT-4o: positive-specific agreement 0.90–0.96, negative-specific agreement 0.27–0.30; 60–80% of citations one verifier flags another calls supported.

### Conformal results (QASA)
Targets 0.90 / 0.94 / 0.98 → achieved 0.90 / 0.94 / 0.98 on repeated held-out splits (marginal coverage). Calibration size 25: naive empirical quantile 0.85 at a 0.90 target vs conformal 0.92; gap closes by ~200. Calibration-negative difficulty: QASA negatives are easy in-paper distractors (mean P(attributable) 0.20); SciFact human-labeled unsupported claims average 0.50; a QASA-calibrated τ targeting 90% catches only 37% of these harder negatives (44% and 61% at 94% and 98%). Recalibrating on target-domain negatives restores the guarantee at a higher review budget.

### Review budget at 90% guaranteed catch (flag %, Table 3; n = 250 per cell)
| Generator | bare | OpenScholar | PaperQA2 |
|---|---|---|---|
| Gemma-4-31B | 3.2 | 2.8 | 4.0 |
| Gemma-4-26B | 0.8 | 1.2 | 3.2 |
| Qwen3.6-27B | 2.0 | 6.4 | 7.6 |
| Qwen3.6-35B | 4.0 | 2.8 | 9.5 |
| Pooled | 2.5 | 3.3 | 6.1 |

### Re-attribution on QASA gold (Table 4)
| Ranker | Resource | recall@1 | recall@3 | recall@5 |
|---|---|---|---|---|
| Gemma-4-26B (self-attribution) | GPU | 0.76 | 0.86 | 0.87 |
| Gemma-4-31B (self-attribution) | GPU | 0.74 | 0.84 | 0.86 |
| BM25 (lexical, adopted default) | CPU | 0.69 | 0.83 | 0.87 |
| Guard (verifier score) | GPU | 0.58 | 0.75 | 0.82 |
| Qwen3.6-35B (self-attribution) | GPU | 0.52 | 0.59 | 0.59 |
| Qwen3.6-27B (self-attribution) | GPU | 0.51 | 0.58 | 0.59 |
| Random | – | 0.03 | – | – |

High-overlap half: BM25 and Gemma tied (0.88). Lowest-overlap quartile: BM25 0.31 vs Gemma 0.53. On SciFact, answer vs refuting passage Jaccard 0.064 vs 0.055 (BM25 cannot separate), verifier 0.83 vs 0.50 — hence the verifier re-checks proposed pointers.

### Scope control
PubMedQA (yes/no conclusion labels): κ = 0.02 (n = 843). The guard audits citation faithfulness, not conclusion correctness.

### Limitations (authors)
Rates are relative to a verifier's operating point; verify against the full passage with sliding windows (prefix truncation inflates unsupported rates severalfold); the bound requires exchangeability and is optimistic for real mis-citations; retrieval held fixed; re-attribution only helps where an alternative supporting passage exists; not a sole gate in safety-critical settings — expert review of flagged sentences remains required. Future: evidence-adequacy guarantees (contradiction, selective citation); robustness to agents optimized against the verifier.

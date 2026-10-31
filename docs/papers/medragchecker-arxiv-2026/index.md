# MedRAGChecker: Claim-Level Verification for Biomedical Retrieval-Augmented Generation

> **Bibkey** `Ji2026_260106519` · **Venue** arXiv preprint (2026) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2601.06519> · `status: complete`

---

## One-liner
MedRAGChecker decomposes long-form biomedical RAG answers into atomic claims (SPO triples) and verifies each with a distilled NLI checker plus a knowledge-graph (KG) consistency signal, fusing them via **selective gating** only when NLI confidently entails while the KG confidently conflicts. The headline finding is that **KG coverage decides whether the KG helps or hurts**: DRKG (62.7% coverage) inflates the hallucination rate to 34.2%, while BioPortal (94.2% coverage) lowers it to 25.2%.

## Problem
Long-form biomedical RAG answers mix supported, under-evidenced and contradicted claims, and whole-answer scoring hides isolated but clinically dangerous errors. The standard approach treats each claim as an NLI hypothesis against retrieved evidence, but in biomedicine textual entailment is not clinical correctness (e.g. if retrieved passages omit Reye's syndrome, NLI entails "aspirin is safe for children with viral infections"). Prior work adds KGs under the **implicit assumption that a KG can only help**; the authors argue this is unsafe — a KG lacking the relevant entity pair produces spurious Contradict verdicts — and nobody had measured how KG coverage drives verification quality.

## Method
**(1) Claim extraction**: a GPT-4.1 teacher decomposes answers into SPO triples; this is SFT-distilled into small models (e.g. Med42-Llama3-8B) so no teacher calls are made at inference. **(2) Textual NLI**: GPT-4.1 three-way verdicts (Entail/Neutral/Contradict) are distilled (LoRA) into Meditron3-8B, Med-Qwen2-7B and Med42-Llama3-8B, combined by an **F1-weighted ensemble** so minority-class (Contradict) specialists count more. **(3) KG verification**: a generic interface of entity linking → plausibility scoring → fusion. DRKG (97K entities, 5.8M edges, drug-repurposing-centric) uses string matching plus TransE scores; BioPortal (a multi-ontology hub: SNOMED-CT, MeSH, NCIt, DOID, RxNorm) links via Jaccard + SapBERT cosine + synonym match and scores by the max of direct property lookup (indication/contraindication, 0.9), hierarchical ancestors (0.2–0.7) and LOOM cross-ontology mappings (0.8). The KG module makes no GPT-4.1 calls — a partially teacher-independent anchor. **(4) Fusion**: logit-space weighted fusion of NLI and KG; **selective gating** applies fusion only when NLI is confident of entailment and the KG is confident of conflict, otherwise falls back to NLI. **Metrics**: Faithfulness, Hallucination rate, SafetyErr (fraction of KG-aligned drug–disease / drug–adverse-event claims labelled Contradict), and decision-flip claims (where NLI-only and fused verdicts differ).

## Data
Four biomedical QA benchmarks: PubMedQA, MedQuAD, LiveQA, MedRedQA; a PubMed-based RAG pipeline with fixed retrieval settings; three generators — Meditron3-8B, Med-Qwen2-7B, Med42-Llama3-8B (PMC-LLaMA-13B excluded from the main comparison for degenerate extraction: 1.19 claims/answer, BERT-F1 45.7). Teacher-labelled data split 80/10/10. Human study: 100 questions × 3 generators × 2 annotators.

## Key results
**Coverage drives KG effect**: both KGs raise faithfulness (DRKG +2.6pp, BioPortal +3.4pp) but move hallucination in opposite directions — DRKG raises it from 29.2% to 34.2% (+5.0pp), BioPortal lowers it to 25.2% (−4.0pp); the 9.0pp swing tracks a 31.5pp coverage gap (62.7% vs 94.2%). E.g. for Meditron3-8B, DRKG nearly doubles hallucination (14.6% → 27.3%) while BioPortal keeps it at 13.5%. DRKG covers only 45% of PubMedQA claims vs 78% on LiveQA; BioPortal ~93% everywhere. SafetyErr drops under both KGs — failures come only from **weak signals leaking from uncovered claims**. **Human alignment**: on decision-flip claims, annotators agree with BioPortal-fused verdicts 69.8% vs 63.4% for NLI-only; macro-F1 59.2 → 64.7. **Gating** fires on 12.3% of KG-linked claims on average (9.4–14.7%) and cuts hallucination a further 0.7–2.4pp at fixed KG. The KG correctly overrides NLI on 72% of drug–adverse-event flips and 68% of drug–disease-treatment flips, but hurts 23% of lifestyle claims via spurious hierarchical matches. **Distillation**: the student ensemble reaches 3-way macro-F1 60.5 and runs 180 claims/min on one A100 — ~50× cheaper and 7× faster than the GPT-4.1 teacher. **Versus generic evaluators**: faithfulness comparable to RAGAS and RAGChecker (e.g. LiveQA 82.5 vs 74.9 vs 70.8), plus claim-level and safety-critical diagnostics they lack.

## Contributions
- Turns the implicit "a KG can only help" assumption into a measurable question: **identical linking/scoring/fusion, swap only the KG**, isolating coverage as the dominant variable.
- Selective gating: an asymmetric fusion rule that lets structured knowledge intervene only in the regime where a false signal does most damage (confident NLI entailment × confident KG conflict).
- Distils a GPT-4.1 teacher into a locally deployable 7–8B checker ensemble — API-free.
- SafetyErr and decision-flip metrics separate clinically dangerous errors from benign inaccuracies.

## Limitations
- Claim extraction and the main NLI signal derive from GPT-4.1, so **evaluation is partly circular**; absolute values on MedRedQA are teacher-conditional (low inter-teacher agreement).
- Contradict is a minority class and subtle contradictions can be missed; the ensemble's F1-C is only 41.3.
- Even BioPortal does not cover everything; SapBERT + API entity linking fails on rare entities, paraphrases and multi-hop claims.
- Small human study (100 × 3 × 2); low inter-annotator agreement on holistic correctness ratings.
- Text QA only — no omics data or numerical conclusions.

## Relation to our direction
This is the **most direct method template for the agent-trustworthiness topic (claim-to-evidence verification of trustworthy biomedical agents)**. Its pipeline — atomic claims → textual NLI → structured-knowledge consistency → conditional fusion — ports almost unchanged to "conclusions an agent writes after analysing kidney omics": decompose "gene X is up-regulated in injured PT cells" into SPO, then check (a) **data entailment** against the agent's own artefacts (DE tables, Xenium spatial statistics) and (b) **prior-knowledge consistency** against KPMP/Lake atlases and GO/Reactome. **The coverage lesson is the most valuable part**: kidney-specific knowledge (cell subtypes, injury states, snATAC peak–gene links) is poorly covered by generic KGs, so naive KG fusion would, like DRKG, **manufacture false contradictions and inflate hallucination**. The agent-trustworthiness topic's calibrated verifier must therefore model "does the knowledge source cover this claim?" explicitly and fall back to data-level evidence when it does not — exactly the selective-gating idea. Its SafetyErr (scoring only safety-critical relations) also suggests defining "conclusion-flipping errors" in the omics failure taxonomy (wrong direction, wrong cell type, wrong perturbation effect) and scoring them separately. For the artifact-injection topic the lesson is indirect: "an under-covering reference turns normal into anomalous" is the same failure mode as anomaly detection against an incomplete healthy reference atlas.

## Reusable assets
- **Code, prompts, diagnostics:**
<https://github.com/JoyDajunSpaceCraft/MedicalRagChecker>
- **KG back-ends:** DRKG (<https://github.com/gnn4dr/DRKG/>) and the public BioPortal API; SapBERT entity linking.
- **Eval protocol:** NLI-only vs +KG (vanilla) vs +KG (gated); human agreement on decision-flip claims as the test of whether fusion genuinely helps.
- **Baselines:** RAGAS, RAGChecker.

## Follow-ups
- RAGChecker (Ru et al., 2024) and FActScore (Min et al., 2023) — the origins of claim-level evaluation.
- HealthFC (Vladika et al., 2024) clinical fact-checking baseline.
- Appendix E (teacher sensitivity) and Appendix G (flip analysis by relation type) — read closely when designing the agent-trustworthiness topic verifier calibration.

## Cite
```bibtex
@misc{Ji2026_260106519,
  title = {MedRAGChecker: Claim-Level Verification for Biomedical Retrieval-Augmented Generation},
  author = {Yuelyu Ji and Min Gu Kwak and Hang Zhang and Xizhi Wu and Chenyu Li and Yanshan Wang},
  year = {2026},
  eprint = {2601.06519},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2601.06519}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

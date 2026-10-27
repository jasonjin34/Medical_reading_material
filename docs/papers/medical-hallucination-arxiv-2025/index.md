# Medical Hallucinations in Foundation Models and Their Impact on Healthcare

> **Bibkey** `Kim2025_250305777` · **Venue** arXiv preprint (2025) · **Category** agents · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2503.05777> · `status: complete`

---

## One-liner
A combined survey + benchmark + physician annotation + clinician survey: medical hallucination is defined as erroneous, inconsistent or unsupported output **that could alter clinical decisions**, with a five-cluster taxonomy. On Med-HALT across 11 models, **general-purpose models hallucinate less than medical-specialized ones** (median hallucination-free baseline 76.6% vs 51.3%), and CoT is the most consistent mitigation; physician annotation of NEJM cases shows errors concentrate in **chronological ordering and lab-data understanding** rather than diagnosis itself.

## Problem
Foundation models are entering clinical workflows, but plausible-yet-wrong outputs are especially dangerous in medicine: there is a large knowledge asymmetry between AI and users, and fabricated drugs, contraindicated recommendations or false imaging reads can directly harm patients. Medicine adds specific difficulties: rapidly evolving knowledge, required precision, densely interconnected concepts where small errors cascade, and specialised jargon. The authors ask how medical hallucination differs from general hallucination, how to classify it, what causes it, how to detect and mitigate it, how clinicians experience it, and what the regulatory/legal implications are.

## Method
**Taxonomy** (Fig. 2 / Table 2): five clusters — (a) factual errors (non-factual, factual, input-conflicting); (b) outdated references (memory-based); (c) spurious correlations (bias-induced, amalgamated, multimodal-integration); (d) fabricated sources or guidelines (procedural, research); (e) incomplete chains of reasoning (reasoning, decision-making, diagnostic) — with analogies to clinician cognitive biases such as confirmation bias. **Benchmark** (Section 6): 50 examples from each of seven Med-HALT tasks (350 total) — reasoning tests (False Confidence, None of the Above, Fake Questions) and memory tests (Abstract-to-Link, PMID-to-Title, Title-to-Link, Link-to-Title); five conditions: Base, System Prompt, CoT ("Let's think step by step."), MedRAG (KG-based medical RAG), Internet Search (SerpAPI Google); metrics are the Med-HALT pointwise score (+1 correct, −0.25 wrong) and UMLSBERT semantic similarity; statistics via Mann–Whitney and Benjamini–Hochberg FDR. **Physician annotation** (Section 7): 20 NEJM case records, three tasks (chronological ordering, lab-data understanding, diagnosis prediction), 5 models, 7 MD-level annotators labelling hallucination type and clinical risk on a 0–5 scale, agreement via average pairwise Jaccard index. **Survey** (Section 8): a 31-question online instrument, 15 September – 18 December 2024, MIT COUHES IRB-exempt.

## Data
Med-HALT (350 items); NEJM case records (20); survey with 75 participants and 70 complete responses (29 researchers, 23 physicians, 15 data scientists, 5 biomedical engineers, 3 other). Eleven models: 7 general-purpose (o3-mini, o1, GPT-4o, GPT-4o mini, GPT-5, Gemini-2.5 Pro, DeepSeek-R1) and 4 medical-specialized (PMC-LLaMA, AlpaCare-13B, MedAlpaca-13B, MedGemma). Physician annotation covers o1, gemini-2.0-flash-exp, gpt-4o, gemini-1.5-flash and claude-3.5 sonnet.

## Key results
**Med-HALT**: gemini-2.5-pro 87.6% baseline → 97.9% with CoT; deepseek-r1 86.6%, o3-mini 80.4%, gpt-5 71.2%, o1 64.0%, gpt-4o 54.4%, gpt-4o-mini 48.3%. Medical-specialized: medgemma 52.6%, pmc-llama 40.8%, medalpaca 32.0%, alpacare 28.6%. General vs specialized median baseline **76.6% vs 51.3%** (difference 25.2%, 95% CI 18.7–31.3%, U = 27.0, p = 0.012, rank-biserial r = −0.64). **CoT**: significant improvement in 71% of models (p < 0.05), 64% after FDR; of 46 within-model tests, 22 were significant and 19 survived correction (86.4% retention). o3-mini: 80.4% → 81.4% (system prompt) → 90.7% (CoT). **Search augmentation**: gpt-5 71.2% → 87.6% (+16.5%); pmc-llama 40.8% → 59.9% (+46.1% relative); but deepseek-r1 86.6% → 84.3% — noisy retrieval can hurt strong models, motivating adaptive retrieval. Semantic similarity: strong general models 0.8–0.9, medical models 0.1–0.5. **NEJM physician annotation**: diagnosis prediction has the lowest hallucination rates (0–22%), chronological ordering (0.25–24.6%) and lab-data understanding (0.25–18.7%) higher; GPT-4o is highest on chronology (24.6%) and labs (18.7%), often rated "Significant"/"Considerable" risk; Claude-3.5 and o1 reach 0% on diagnosis prediction. **Survey**: the abstract reports 91.8% had encountered medical hallucinations and 84.7% thought they could cause harm; the body gives raw counts — 50 of 59 believed observed hallucinations might affect patient health, and 85% (51) cross-reference external sources. (Caveats: the abstract's "64–72% of residual hallucinations stem from causal or temporal reasoning failures" is not fully derived in the body; its "CoT significantly reduced hallucinations in 86.4% of comparisons" is actually the FDR retention rate — interpret with care.)

## Contributions
- A definition of medical hallucination centred on "could it alter clinical decisions", plus a five-cluster taxonomy with fine-grained types and clinical examples.
- A systematic general-vs-specialized comparison challenging the "domain fine-tuning is safer" assumption.
- Physician annotation on real cases by type × 0–5 clinical risk, exposing temporal and lab-data extraction as weak points.
- A multinational clinician survey plus regulatory/liability discussion linking the technical problem to deployment practice.

## Limitations
- Only 50 Med-HALT items per task; scoring relies on UMLSBERT similarity and the pointwise score, which the authors admit do not directly capture clinical safety.
- Physician annotation uses only 20 NEJM cases and a different model set from the benchmark; the text itself notes a "data discrepancy between output logs and visual representation" warranting investigation.
- Small survey (70 complete responses); abstract percentages and body counts use differing denominators; several claims ("reasoning-driven, not knowledge deficit") are argued more strongly than the evidence supports.
- The medical models are smaller and older, so the comparison confounds specialization with scale and vintage.

## Relation to our direction
For **Topic 2** it offers two things. First, **a taxonomy skeleton**: input-conflicting (conclusion contradicts given data), amalgamated (unrelated information merged into one conclusion), multimodal-integration, fabricated sources/guidelines and incomplete reasoning chains all have omics-agent analogues — wrongly merging snRNA and Xenium results, reading spatial proximity as causation, or citing a non-existent marker-gene list. Topic 2's omics-specific taxonomy can use it as the top level and add omics-specific types (batch-vs-biology confusion, cell-annotation errors, misread significance). Second, **a physician annotation protocol**: the two-axis "hallucination type × 0–5 clinical risk" labelling with pairwise-Jaccard multi-annotator agreement can serve directly as a template for KidneyAnomalyBench / Topic 2 expert annotation (replacing "clinical risk" with "how much wet-lab effort would be wasted / how misleading if acted upon"). Its finding that errors concentrate in chronology and lab-value extraction also suggests agents may err more on the **numbers and metadata** in omics results (sample groups, time points, thresholds) than on high-level biological inference, so the verifier should check those first. "Strong general models beat domain-tuned ones" informs the choice of base model for Topic 2's evaluated agents, though the evidence is confounded by scale. No direct bearing on Topic 1.

## Reusable assets
- **Project page (annotation guidelines, annotation interface, Figs. 11–13):**
<https://medical-hallucination.github.io/>
- **Benchmarks:** Med-HALT (Pal et al., 2023); MedRAG (Xiong et al., 2024) as RAG baseline.
- **Taxonomy and risk tables:** Table 2 (type definitions and examples), Tables 6–7 (annotation types and 0–5 risk definitions).
- **Survey instrument:** the 31-question clinician AI/hallucination questionnaire (appendix).

## Follow-ups
- Med-HALT (Pal et al., 2023), Hegselmann et al. (2024) hallucination typology and Asgari et al. (2025) clinical-risk framework — the two sources of this paper's annotation protocol.
- Section 5.4 on uncertainty quantification, for Topic 2's calibrated-verifier related work.
- Read with llm-judge-healthcare-arxiv-2026 and medragchecker-arxiv-2026 in this repo: definition → evaluator → verification method.

## Cite
```bibtex
@misc{Kim2025_250305777,
  title = {Medical Hallucinations in Foundation Models and Their Impact on Healthcare},
  author = {Kim, Yubin and Jeong, Hyewon and Chen, Shan and Li, Shuyue Stella and Park, Chanwoo and Lu, Mingyu and Alhamoud, Kumail and Mun, Jimin and Grau, Cristina and Jung, Minseok and Gameiro, Rodrigo and Fan, Lizhou and Park, Eugene and Lin, Tristan and Yoon, Joonsik and Yoon, Wonjin and Sap, Maarten and Tsvetkov, Yulia and Liang, Paul and Xu, Xuhai and Liu, Xin and Park, Chunjong and Lee, Hyeonhoon and Park, Hae Won and McDuff, Daniel and Tulebaev, Samir and Breazeal, Cynthia},
  year = {2025},
  eprint = {2503.05777},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2503.05777}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

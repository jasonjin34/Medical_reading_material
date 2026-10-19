<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# MedRAGChecker: Claim-Level Verification for Biomedical Retrieval-Augmented Generation

- **Authors:** Yuelyu Ji; Min Gu Kwak; Hang Zhang; Xizhi Wu; Chenyu Li; Yanshan Wang
- **Venue / Year:** arXiv preprint · 2026
- **DOI:** 
- **arXiv:** 2601.06519
- **URL:** https://arxiv.org/abs/2601.06519
- **Bibkey:** Ji2026_260106519
- **Status:** complete

## Abstract
Biomedical retrieval-augmented generation (RAG) produces long-form answers that mix supported, under-evidenced, and contradicted claims, demanding fine-grained verification. We propose MedRAGChecker, a claim-level diagnostic framework that (i) decomposes answers into atomic claims, (ii) verifies each claim by combining textual natural language inference (NLI) with a knowledge-graph (KG) consistency signal, and (iii) uses a selective gating rule to fuse the two signals only when the KG signal is decisive, falling back to NLI otherwise. To assess our framework on biomedical RAG, we distill a GPT-4.1 teacher into compact student checkers and evaluate across four biomedical QA benchmarks (PubMedQA, MedQuAD, LiveQA, MedRedQA) with three biomedical generators. MedRAGChecker achieves comparable answer-level faithfulness to general-purpose RAG evaluators while additionally producing safety-critical error diagnostics that align with human judgment on decision-flip claims (69.8% agreement vs. 63.4% for NLI-only). As an additional analysis, we instantiate the KG component with two back-ends of differing scope—DRKG and BioPortal—and find that KG coverage substantially affects fusion quality: an incomplete KG can inflate hallucination via false contradictions on uncovered claims, motivating our selective gating design.

## Full text / Extract
> Full text is open access; below is the cleaned main text (figures/equations rendered as plain text or LaTeX alt-text; reference list omitted). Source: arXiv HTML (2601.06519).

### Main text
1 Introduction
Large language models (LLMs) now pass standardized medical exams,
yet their ungrounded generations still produce clinically harmful
errors Yu et al. (2025); Singhal et al. (2025); Vladika et al. (2024); Pandit et al. (2025).
Retrieval-augmented generation (RAG) partly addresses this by
conditioning answers on up-to-date medical
literature Achiam et al. (2023); Tu et al. (2024); Lewis et al. (2020),
but noisy retrieval can still cause the model to anchor on
misleading snippets Ning et al. (2025). Long-form biomedical
answers contain many distinct factual statements, and whole-answer
scoring hides isolated but clinically important mistakes. This
motivates claim-level evaluation: decomposing each answer
into atomic factual claims (e.g., a single
drug–effect or drug–contraindication assertion) and verifying
each one independently Min et al. (2023); Ru et al. (2024).
Standard claim-level verification frames each claim as a natural
language inference (NLI) hypothesis against retrieved evidence.
In biomedicine, however, textual entailment alone is insufficient:
a claim can be linguistically supported by retrieved passages yet
violate known drug–disease contraindications. Recent work therefore
augments NLI with biomedical knowledge graphs
(KGs) Vladika et al. (2024); Ning et al. (2025), under the
implicit assumption that adding a KG can only help. This
assumption is unsafe. Figure 1 illustrates the
failure: a claim about ibuprofen’s gastrointestinal side effects
receives a spurious Contradict verdict from a KG that
lacks the relevant entity pair, yet is correctly entailed by a
broader-coverage KG. Whether a KG helps depends on whether it
covers the claims being verified — and no prior work has
measured how this coverage drives verification quality on
biomedical RAG.
We propose MedRAGChecker (Figure 2), a
claim-level diagnostic framework that combines NLI verification
with a KG plausibility signal under a coverage-aware fusion rule.
To isolate the effect of coverage from confounding algorithmic
choices, we instantiate the framework with two KGs that differ
primarily in scope: a drug-repurposing KG
(DRKG Ioannidis et al. (2020), 62.7% entity coverage on our benchmarks)
and a multi-ontology hub
(BioPortal Salvadores et al. (2013), 94.2% coverage). The
31.5pp coverage gap drives a 9.0pp swing in hallucination rate
(34.2% vs. 25.2%). To turn this finding into a practical fix,
we introduce selective gating: applying the KG signal only
when it strongly conflicts with a confident NLI entailment, the
narrow regime where a false KG signal would do the most damage.
Beyond what individual components contribute, we additionally
observe that the choice of KG back-end—specifically its
coverage over the target claim distribution—substantially
affects fusion quality. This motivates a coverage-aware fusion
rule (selective gating) that remains robust across KG choices.
Contributions.
(i) We propose MedRAGChecker, a claim-level
biomedical RAG diagnostic framework that combines distilled NLI
checkers with a teacher-independent KG verifier under a selective
gating rule, and demonstrate that it matches general-purpose
RAG evaluators on faithfulness while uniquely surfacing
safety-critical errors.
(ii) We introduce selective gating, a fusion
rule that applies KG adjustment only when NLI is confident of
entailment and KG is confident of conflict, firing on
 ${\sim}12.3\%$ of KG-linked claims and concentrating correction
on safety-critical relations.
(iii) Through an analysis with two KG back-ends
(DRKG, BioPortal), we show that KG coverage substantially
affects fusion quality, validated across four biomedical QA
benchmarks with a targeted human study where coverage-aware
fusion raises decision-flip agreement from 63.4% to 69.8%.
Figure 2: Overview of MedRAGChecker. For each atomic
claim extracted from the answer, a textual NLI checker (purple) and a
KG-based verifier (orange) produce complementary signals. These are
combined by a selective gating module: when the KG provides a strong
signal of conflict, the KG score is fused with the NLI score; otherwise
the NLI score is used alone. The student NLI checker and claim extractor
are distilled from a GPT-4.1 teacher offline (dashed arrows); at
inference no teacher calls are made. KG coverage, shown later to be
the dominant factor in verification quality (Section 4.5),
is varied across two back-ends: DRKG and BioPortal.
2 Related Work
Biomedical QA.
Despite strong performance on standardized exams Jin et al. (2020); Pal et al. (2022); Jin et al. (2019), long-form biomedical answers remain prone to hallucinations Asgari et al. (2025); Huang et al. (2025), making claim-level validation necessary.
RAG Evaluation and Fact-Checking.
Prior work formulates RAG factuality checking as an NLI-style claim-
evidence problem, splitting generations into statements and verifying
each against retrieved
passages Lewis et al. (2020); Fu et al. (2024); Xin et al. (2025).
RAGAS (Es et al., 2024) and
RAGChecker (Ru et al., 2024) evaluate retrieval and grounding
at the answer level. MedRAGChecker operates at the
claim level and aggregates verified claims into answer-level
diagnostics, adding a structured KG signal for claim veracity.
HealthFC Vladika et al. (2024) offers a strong clinical baseline
but targets short, well-formed statements, while we target multi-
sentence RAG answers.
Knowledge Graphs for QA.
Biomedical KGs support QA reasoning Himmelstein et al. (2017), but their incompleteness limits standalone use Chen et al. (2022). We use KGs as external verifiers complementing text-based NLI, fusing both signals to improve robustness on safety-critical claims.
3 MedRAGChecker
Figure 2 overviews the pipeline. MedRAGChecker combines a textual NLI signal from teacher-distilled student checkers with a KG-based consistency signal (instantiated with DRKG and BioPortal), and fuses them into a single calibrated support score used by all downstream diagnostics.
3.1 Task Definition and Outputs
We cast biomedical RAG evaluation as claim-centric verification.
Given a RAG instance $(q,D,a)$ with question $q$ , generated answer
 $a$ , and top- $k$ retrieved passages $D=\{d_{j}\}_{j=1}^{k}$ ,
MedRAGChecker decomposes $a$ into atomic claims
 $\mathcal{C}=\{c_{1},\dots,c_{n}\}$ and assigns each claim
(1) a discrete verdict
 $\hat{y}_{i}\in\{\textsc{Entail},\textsc{Neutral},\textsc{Contradict}\}$ 
and (2) a calibrated support score $s(c_{i})\in[0,1]$ .
Two signals produce the verdict: a textual NLI probability
 $p_{\mathrm{NLI}}(c_{i})$ against retrieved evidence, and a KG
plausibility score $s_{\mathrm{KG}}(c_{i})$ against a biomedical
knowledge base. We study how the choice of KG, and specifically its
coverage over claims in our benchmarks, affects the quality of
the final verdict.
In our implementation, the textual checker provides
 $p_{\mathrm{NLI}}(c_{i})\triangleq P(\textsc{Entail}\mid c_{i},D)$ from
the ensemble distribution. When KG evidence is available, we fuse
this textual signal with KG support to obtain the final support score
(Section 3.5).
3.2 Claim Extraction
We use GPT-4.1 as a teacher to decompose each answer $a$ into atomic
claims, represented as subject–predicate–object (SPO) triples
(e.g., ["Ibuprofen", "may cause", "GI bleeding"]), in the
spirit of FActScore-style atomic decomposition (Min et al., 2023).
The triple form aligns with downstream KG entity linking
(§3.4).
To avoid teacher calls at inference time, we distill a biomedical LLM
(e.g., Med42-Llama3-8B) via supervised fine-tuning on
 $(q,a)\rightarrow c_{1},\ldots,c_{n}$ with teacher claim lists as targets.
Since claim extraction is a standard and solved step in this framework,
we treat it as front-end infrastructure rather than a contribution.
Extraction quality (BERTScore vs. teacher claims, human Likert
ratings) is validated in Section 4.4; training
details are in Appendix U;
qualitative error analysis is in Appendix I.
3.3 Textual NLI Verification
For each extracted claim $c_{i}$ , a checker predicts
 $y_{i}\in\{\textsc{Entail},\textsc{Neutral},\textsc{Contradict}\}$ 
with evidence $D$ as premise and the claim as hypothesis, producing
 $p_{\mathrm{NLI}}(c_{i})\triangleq P(\textsc{Entail}\mid c_{i},D)$ .
We distill GPT-4.1 verdicts into Meditron3-8B, Med-Qwen2-7B, and
Med42-Llama3-8B via supervised fine-tuning (SFT), then combine them in an F1-weighted ensemble
so minority-class specialists contribute more to Contradict
decisions. Unless otherwise stated, all downstream diagnostics use
this ensemble; details are in Appendix U.
3.4 KG-Based Verification
In biomedical settings, a claim may be linguistically entailed by
the retrieved text yet clinically wrong. For example, a claim that
“aspirin is safe for children with viral infections” can be
supported by a poorly-retrieved passage but violates the
Aspirin–Reye contraindication. We therefore augment the textual
NLI signal with structured biomedical knowledge.
Our KG verification module is designed as a generic interface with
three stages: (1) entity linking from the extracted SPO triple
to KG entities; (2) plausibility scoring over linked entities;
and (3) signal fusion with the textual NLI score
(Section 3.5). The module is teacher-independent:
it operates on extracted SPO triples without GPT-4.1 calls, providing
an external anchor that partially decouples our framework from
teacher bias (cf. Limitations). Different KG back-ends can be
plugged into this interface; we instantiate the module with two
biomedical KGs in our experiments (Section 4.2).
3.4.1 Entity Linking
Unlike general-purpose KGs (e.g., Wikidata Vrandečić and Krötzsch (2014), ConceptNet Liu and Singh (2004)) that ship
with high-quality entity embeddings, the biomedical KGs we use
either do not provide pretrained entity embeddings aligned with
our claim vocabulary (BioPortal) or provide only relation-specific
TransE embeddings without natural-language surface forms (DRKG).
We therefore link entities via text-based matching enhanced with
biomedical entity representations (SapBERT) where applicable.
For each claim $c$ , we first extract an SPO triple $(s,r,o)$ from the
teacher decomposition. We then link $s$ and $o$ to the target KG.
For DRKG, we perform string-based matching against DRKG entity
names and map canonical claim relations (e.g., treats,
causes) to DRKG edge types, computing a normalized string
similarity score $s_{\text{text}}(c)\in[0,1]$ .
For BioPortal, we query the BioPortal API across entity-type-
appropriate ontologies, scoring each candidate entity by | | $s_{\text{link}}=0.3\cdot s_{\text{text}}+0.5\cdot s_{\text{SapBERT}}+0.2\cdot s_{\text{syn}},$ | | (1)
where $s_{\text{text}}$ is Jaccard string similarity,
 $s_{\text{SapBERT}}$ is the cosine similarity between
SapBERT (Liu et al., 2021) biomedical entity embeddings, and
 $s_{\text{syn}}$ is synonym-set match. We retain the top-scoring entity per mention with
 $s_{\text{link}}\geq 0.5$ ; otherwise the claim is treated as
KG-uncovered and falls back to NLI-only.
3.4.2 KG Plausibility Scoring
Given linked entities, we compute a claim-level plausibility score
 $s_{\mathrm{KG}}(c)\in[0,1]$ .
DRKG (TransE). For each aligned triple $(h,r,t)$ ,
we compute
 $p_{\mathrm{KGE}}(h,r,t)=\sigma(-\ | \mathbf{e}_{h}+\mathbf{r}_{r}-\mathbf{e}_{t}\ | _{2})$ 
using pre-trained translation-based KG embeddings (TransE)  (Bordes et al., 2013),
taking the maximum over candidate triples. We combine this with
text alignment: | | $s_{\mathrm{KG}}^{\text{DRKG}}(c)=(1{-}\alpha)\cdot p_{\mathrm{KGE}}(c)+\alpha\cdot s_{\text{text}}(c),$ | | (2)
with $\alpha$ tuned on dev.
BioPortal (ontology-based). For each linked entity
pair, we compute the maximum of three signals: (i) direct
property lookup (score 0.9, e.g., indication,
contraindication); (ii) hierarchical proximity via
shared ontology ancestors (0.2–0.7); and (iii) cross-ontology
mapping through LOOM links (0.8): | | $s_{\mathrm{KG}}^{\text{Bio}}(c)=\max(s_{\text{direct}},s_{\text{hier}},s_{\text{loom}}).$ | | (3)
Scoring details are in Appendix F.
3.5 Signal Fusion with Selective Gating
3.5.1 Logit-Space Fusion
For claims linked to the KG, we combine NLI and KG signals in logit
space: | | $P^{\star}(c_{i})=\sigma\!\big(\beta\cdot\mathrm{logit}(p_{\mathrm{NLI}}(c_{i}))+(1{-}\beta)\cdot\mathrm{logit}(s_{\mathrm{KG}}(c_{i}))\big),$ | | (4)
where $\beta$ controls the relative weight. Logit-space fusion avoids
the scale mismatch between the two signals and is insensitive to
monotonic rescalings.
For claims that cannot be linked to the KG, we fall back to
 $P^{\star}(c_{i})=p_{\mathrm{NLI}}(c_{i})$ .
3.5.2 Selective Gating
A symmetric application of Eq. 4 fails when
 $s_{\mathrm{KG}}$ is weak but non-zero (e.g., a spurious hierarchical
match on a lifestyle claim), pushing the claim toward Contradict
even when NLI strongly entails. We therefore apply KG adjustment only
when both signals are decisive; with shorthand
 $\ell_{\mathrm{NLI}}\triangleq\mathrm{logit}(p_{\mathrm{NLI}})$ ,
 $\ell_{\mathrm{KG}}\triangleq\mathrm{logit}(s_{\mathrm{KG}})$ : | | $P^{\star}(c_{i})=\begin{cases}\sigma\!\big(\beta\,\ell_{\mathrm{NLI}}+(1{-}\beta)\,\ell_{\mathrm{KG}}\big),\\
\quad\text{if }s_{\mathrm{KG}}\!<\!0.3\text{ and }p_{\mathrm{NLI}}\!>\!0.7\\[3.0pt]
p_{\mathrm{NLI}}(c_{i}),\quad\text{otherwise.}\end{cases}$ | | (5)
Gating fires only when NLI is confident of entailment but KG is
confident of conflict—the regime where a false KG signal would
do the most damage. We tune $(\alpha,\beta,\tau)$ on dev
(Appendix M).
3.6 Metrics
From $P^{\star}(c_{i})$ and the predicted labels, we derive two core answer-level metrics:
Faithfulness $\mathrm{Faith}(a)=\frac{1}{n}\sum_{i}\mathbb{I}[\hat{y}_{i}{=}\textsc{Entail}]$ and
Hallucination rate $\mathrm{Halluc}(a)=\frac{1}{n}\sum_{i}\mathbb{I}[\hat{y}_{i}{=}\textsc{Contradict}]$ .
We additionally compute (i) claim extraction quality (span-F1 and
BERTScore (Zhang et al., 2020)), (ii) retrieval diagnostics (ClaimRec, CtxPrec,
answer-level ClaimF1), (iii) a parametric SelfKnow score (NLI-only,
empty context), and (iv) a SafetyErr rate — the fraction of
KG-aligned safety-critical claims (drug–disease, drug–adverse-event)
labeled Contradict, isolating clinically dangerous errors
from benign inaccuracies.
Formal definitions of all metrics are in Appendix A.
A decision-flip claim is one whose verdict (Entail vs. not-Entail) differs between NLI-only and the Fused setting; flips are the loci where KG augmentation actually changes evaluation outcomes.
Generator
Panel A: Extractor
Panel B: Checker (SFT)
BERT-F1 $\uparrow$ 
#Claims
Acc (%)
Mac-F1 (%)
F1-E (%)
F1-N (%)
F1-C (%)
Med-Qwen2-7B
78.3
3.25
83.7
55.0
40.1
94.9
42.4
Med42-Llama3-8B
83.6
4.70
85.6
67.3
50.3
94.5
27.3
Meditron3-8B
82.1
5.28
81.2
49.7
46.3
92.9
23.4
Ensemble (F1-wt)
87.4
60.5
52.8
95.0
41.3
Table 1: Distilled claim extractor and checker fidelity to the
GPT-4.1 teacher.
Panel A: BERTScore F1 between student-extracted and
teacher-extracted claims, and average number of claims per answer.
Panel B: Checker accuracy and per-class F1 on the 3-way
NLI task. F1-E, F1-N, and F1-C denote per-class F1 for the
Entail, Neutral, and Contradict labels
respectively. Bold marks the column-wise maximum
(including the ensemble row where reported).
Green highlights the best value among
single students only; red highlights the worst.
The ensemble row is excluded from the green/red comparison.
Teacher-checker (GPT-4.1)
Student-checker (SFT ensemble)
Generator
KG Setting
Faith. $\uparrow$ 
Halluc. $\downarrow$ 
SafetyErr $\downarrow$ 
Faith. $\uparrow$ 
Halluc. $\downarrow$ 
SafetyErr $\downarrow$ 
Med-Qwen2-7B
NLI-only
68.1
21.8
29.9
62.3
20.7
19.6
+ DRKG
75.6
18.6
24.4
68.6
10.4
12.6
+ BioPortal (vanilla)
72.5
23.4
25.7
68.8
20.8
18.3
+ BioPortal (gated)
72.1
22.3
25.4
69.6
9.1
16.8
Med42-Llama3-8B
NLI-only
70.2
18.1
29.8
67.3
24.3
28.9
+ DRKG
77.0
23.0
17.5
58.4
25.7
19.6
+ BioPortal (vanilla)
73.3
16.7
16.8
67.8
24.8
24.4
+ BioPortal (gated)
73.2
14.3
16.4
69.1
22.4
23.7
Meditron3-8B
NLI-only
58.2
20.6
41.8
52.7
14.6
29.0
+ DRKG
66.8
33.2
23.7
59.6
27.3
27.2
+ BioPortal (vanilla)
67.9
23.6
37.9
53.4
15.7
26.7
+ BioPortal (gated)
69.3
23.5
36.7
54.6
13.5
25.7
Table 2: Coverage-driven verification behavior.
KG fusion results per generator (macro-averaged across four datasets).
DRKG’s limited coverage (62.7%) inflates hallucination on uncovered
claims (e.g., Meditron3-8B: 14.6% $\to$ 27.3%) via false
contradictions, while BioPortal’s 94.2% coverage reverses this
pattern (Meditron3-8B: 14.6% $\to$ 13.5%) and consistently reduces
safety-critical errors across generators.
Bold marks the best value within each generator block
and checker setting.
Green/red indicate
improvement/degradation vs. NLI-only.
“vanilla” applies Eq. 4 to all KG-linked
claims; “gated” uses Eq. 5.
4 Experiments
4.1 Experimental Setup
Data and RAG setup.
We evaluated on four biomedical QA benchmarks: PubMedQA Jin et al. (2019), MedQuAD Ben Abacha and Demner-Fushman (2019), LiveQA Yang et al. (2017), and MedRedQA Nguyen et al. (2023). We use a PubMed-based RAG pipeline (Appendix S) with fixed retrieval settings across runs and compare three biomedical generators: Meditron3-8B, Med-Qwen2-7B, and Med42-Llama3-8B. PMC-LLaMA-13B is excluded from the main comparison due to degenerate extraction behavior (only 1.19 claims per answer vs. 3–5 for the other generators, and BERT-F1=45.7 against teacher claims vs. 78–84), and is reported separately in Appendix C.
Checker training and evaluation protocol.
We use GPT-4.1 to provide claims and NLI labels on train/dev, then distill (i) a student claim extractor and (ii) student NLI checkers. Unless stated otherwise, we use the F1-weighted ensemble (Section 3.3) for downstream diagnostics. We report three verification settings that differ only in who performs extraction/checking: teacher checker (GPT-4.1), single-student, and student ensemble. We split the teacher-labeled data into train/dev/test (80/10/10) and fine-tuned open-source students with low-rank adaptation
(LoRA) (Hu et al., 2022); training details are in Appendix U. For KG-enhanced verification, we computed a KG support score
from each backend (DRKG or BioPortal, Section 3.4)
and fused it with textual NLI via Eq. 4
or Eq. 5; $(\alpha,\beta,\tau)$ were tuned on dev and then fixed for all test results. GRPO refinements were exploratory and are reported in Appendix N; unless noted, all test results use student models only (no GPT-4.1 calls at inference).
Computational cost.
The student ensemble processes ${\sim}$ 180 claims/min on a single A100-80GB
( ${\sim}$ 0.3 s and $0.0004 per claim), roughly 50 $\times$ cheaper and
7 $\times$ faster than the GPT-4.1 teacher ( ${\sim}$ 2.1 s, $0.02 per claim).
End-to-end evaluation of 100 questions takes ${\sim}$ 2.5 minutes
with the student pipeline versus ${\sim}$ 18 minutes with the teacher.
4.2 KG Back-end Instantiations
To study how KG choice affects verification, we instantiate the KG
module with two back-ends that share the same linking/scoring/fusion
interface but differ in scope and edge-attribute richness:
DRKG (Ioannidis et al., 2020) is a drug-repurposing-focused
biomedical KG containing $\approx$ 97K entities and $\approx$ 5.8M
edges, primarily covering drug–gene–disease relations. Its edges
carry minimal attribute information beyond the relation type, and
we score plausibility using pre-trained TransE embeddings. On our
benchmarks, DRKG covers 62.7% of the entity pairs extracted from
claims (averaged over the three main generators; PMC-LLaMA-13B
excluded for consistency with §4.1).
BioPortal (Salvadores et al., 2013) is a
multi-ontology hub integrating biomedical ontologies (SNOMED-CT,
MeSH, NCIt, DOID, RxNorm) with cross-ontology links, accessed via
the public API in early 2026. Its edges carry richer ontology-level
attributes (direct property relations such as
indication/contraindication, hierarchical
ancestors, LOOM mappings), which support ontology-based scoring
without requiring trained embeddings. BioPortal covers 94.2% of
our claim entity pairs (a 31.5pp increase over DRKG).
The two back-ends differ both in coverage over our claim
distribution and in the type of edge attributes available
for scoring. Section 4.5 analyzes how these
differences propagate to downstream verification quality.
4.3 Research Questions
We organize experiments around three questions: how KG coverage
affects verification quality (Sec. 4.5), whether
selective gating mitigates low-coverage failures
(Sec. 4.6), and how diagnostics align with human
judgment (Sec. 4.7). Claim extraction and checker
distillation quality are validated in
Appendix C.
4.4 Distillation Quality
Before presenting our main results, we briefly validate that
the distilled student checkers and extractors are faithful enough
to serve as the front-end of our pipeline. A full analysis is in
Appendix C; here we summarize the key
findings.
Extractor.
Student extractors achieve BERTScore F1 of $0.78$ – $0.84$ against
teacher claims (Med42-Llama3-8B: 83.6; Meditron3-8B: 82.1;
Med-Qwen2-7B: 78.3), producing 3–5 atomic claims per answer that
closely match the teacher’s decomposition. Qualitative analysis
(Appendix I) further shows that
hallucinated claims are rare (6%) and over-splitting is the
dominant but benign failure mode.
Checker ensemble.
After SFT, the F1-weighted student ensemble reaches macro-F1 of
60.5 on the 3-way NLI task ( Table 1),
close to the teacher’s performance, and is more robust than any
single checker on the minority Contradict class.
These results establish that downstream variations we observe in
the main experiments are attributable to the verification
strategy (NLI-only vs. KG-augmented) rather than to poor
extraction or checker quality.
Figure 3: Effect of KG back-end on verification quality. (a) BioPortal improves faithfulness by +3.4pp over NLI-only. (b) DRKG’s limited coverage inflates hallucination to 34.2%; BioPortal reduces it to 25.2%. (c) BioPortal achieves 94.2% entity coverage vs. DRKG’s 62.7%.
4.5 RQ1: KG Coverage Determines Verification Quality
We compare three verification settings under identical student
checkers: NLI-only, NLI $+$ DRKG, and NLI $+$ BioPortal.
Figure 3 summarizes the macro-averaged result;
per-generator breakdowns are in Table 2.
Main finding: coverage swings hallucination by 9.0pp.
Both KGs improve faithfulness over NLI-only
( $+$ 2.6pp for DRKG, $+$ 3.4pp for BioPortal), but their effect on
hallucination rate diverges sharply:
DRKG inflates hallucination from 29.2% to 34.2%
( $+$ 5.0pp), while BioPortal reduces it to 25.2%
( $-$ 4.0pp). Since both back-ends share identical linking, scoring,
and fusion machinery and differ primarily in coverage (62.7% vs. 94.2%) we attribute this 9.0pp swing to coverage
(cf. Section 4.2 for the three-part
argument).
Per-generator consistency.
Table 2 shows the effect holds across
all three generators under the student-checker setting.
For Meditron3-8B, DRKG nearly doubles hallucination
(14.6% $\to$ 27.3%) while BioPortal keeps it flat
(14.6% $\to$ 13.5%). SafetyErr, in contrast, drops under
both KGs, indicating that KG signals remain reliable
when they fire on safety-critical covered relations—
the failure mode is restricted to uncovered claims leaking weak
signals into the fusion.
Per-dataset coverage effect.
Coverage also varies by dataset
(Appendix J, Table 11).
DRKG covers only 45% of PubMedQA claims
(Table 11; research-oriented
content is underrepresented in a drug-repurposing KG), rising
to 78% on LiveQA (drug-centric consumer questions).
BioPortal maintains $\geq$ 93% coverage across all four
datasets. The hallucination-reduction gap between BioPortal
and DRKG is largest exactly where DRKG coverage is lowest
(PubMedQA, MedQuAD), further supporting the coverage-driven
interpretation. Per-generator coverage and KG-subset behavior are in Table 12.
Human validation on decision-flip.
On claims where NLI-only and Fused disagree, human annotators
agree with BioPortal-fused predictions 69.8% of the time
vs. NLI-only’s 63.4% ( $+$ 6.4pp; on 31% of all flips, the KG-fused verdict matches the human label while NLI-only does not).
Macro-F1 improves from 59.2 to 64.7. Hallucination-rate
changes thus reflect genuine accuracy gains, not metric
artifacts. Full protocol is in Appendix R.
4.6 RQ2: Selective Gating Mitigates Low-Coverage Failure
The main result in RQ1 uses selective gating
(Eq. 5) in the BioPortal configuration.
Here we ablate gating to isolate its contribution.
Vanilla fusion baseline.
To separate the effect of the gating rule from the effect of KG
coverage, we compare selective gating (Eq. 5)
against a vanilla fusion baseline that applies
Eq. 4 to all KG-linked claims without the
gating condition. Both variants share the same KG and fusion
weights $(\alpha,\beta,\tau)$ , so any difference in
Table 2 between BioPortal (vanilla)
and BioPortal (gated) rows isolates the gating rule itself.
Gating trigger rate.
The gating condition
( $s_{\mathrm{KG}}<0.3$ and $p_{\mathrm{NLI}}>0.7$ ) fires on
12.3% of KG-linked claims on average across our four datasets
(per-dataset range 9.4%–14.7%; see Appendix J).
For the remaining 88%, the KG signal is either weak or ambiguous,
and the fused score reduces to $p_{\mathrm{NLI}}$ , preserving
NLI-only behavior.
Gating ablation on the same KG.
Comparing BioPortal (vanilla) and BioPortal (gated) in
Table 2 isolates gating’s effect
under fixed coverage: across all three generators, gating
consistently reduces hallucination (by 0.7–2.4pp depending on
generator and checker) while maintaining comparable faithfulness,
confirming the gating rule, not just high coverage, avoids
false contradictions.
We do not report a DRKG $+$ gated variant because DRKG’s TransE
scores concentrate below the gating threshold, so gating fires
indiscriminately and the gated variant behaves essentially as
vanilla DRKG.
Relation-type stratification.
Appendix G decomposes decision-flip outcomes by
relation type: KG correctly overrides NLI on 72% of
drug–adverse-event flips and 68% of drug–disease-treatment
flips, but hurts 23% of general lifestyle claims through
spurious hierarchical matches. Selective gating is designed
precisely to suppress this second category by keeping NLI-only
whenever the KG signal is not decisive. This stratified view
confirms that gating concentrates KG influence on relations
where the KG’s structural priors are clinically meaningful.
4.7 RQ3: Human Alignment on Safety-Critical Claims
Our RQ3 reports two targeted human studies on 100 questions $\times$ 3 generators $\times$ 2 annotators (comparable to FActScore (Min et al., 2023)): (i) a claim-extraction sanity check, and (ii) the decision-flip study summarized in Figure 3(c).
We deliberately avoid aggregate correctness/completeness
ratings of long-form medical answers, which in our pilot
showed low inter-annotator agreement (consistent with the
known difficulty of holistic medical answer rating, e.g.,
Med-PaLM physician ratings (Singhal et al., 2025)).
Such low agreement reflects the inherent subjectivity of
rating open-ended medical answers holistically and does
not speak to claim-level verification, which is our
contribution. Full agreement statistics are in
Appendix Q.
Human ratings of extracted claim quality.
Med-Qwen2-7B: $4.97\pm 0.18$ ;
Med42-Llama3-8B: $4.73\pm 0.99$ ;
Meditron3-8B: $4.62\pm 0.18$ 
(1–5 Likert; two annotators, 100 questions; $\kappa=0.67$ ).
Near-ceiling scores confirm the distilled extractor produces
faithful atomic decompositions. Aggregate answer-level
ratings (correctness, completeness) showed lower agreement
and are deferred to Appendix Q.
Decision-flip agreement.
RQ1 already established that BioPortal $+$ gating raises human agreement on decision-flip cases by $+6.4$ pp, with consistent improvements on safety-critical drug–disease and drug–adverse-event subsets (Appendix G).
4.8 Comparison with Existing RAG Evaluators
To position MedRAGChecker against general-purpose RAG evaluation
tools, we compare with RAGAS (Es et al., 2024) and
RAGChecker (Ru et al., 2024) on answer-level faithfulness
using the same retrieval pipeline and generator outputs
(Table 3).
We use Med42-Llama3-8B as a representative generator (best macro-F1 as a checker; comparable claim quality across generators, see §4.7). | | | MedRAG- | | RAG- | Dataset | Metric | Checker | RAGAS | Checker | PubMedQA | Faith. $\uparrow$ | 88.9 | 89.5 | 87.2 | Halluc. $\downarrow$ | 4.7 | – | 5.1 | LiveQA | Faith. $\uparrow$ | 82.5 | 74.9 | 70.8 | Halluc. $\downarrow$ | 8.6 | – | 19.5 | MedQuAD | Faith. $\uparrow$ | 87.6 | 84.7 | 83.9 | Halluc. $\downarrow$ | 5.5 | – | 6.8 | MedRedQA | Faith. $\uparrow$ | 82.4 | 82.1 | 81.5 | Halluc. $\downarrow$ | 6.4 | – | 8.2
Table 3: Comparison with general-purpose RAG evaluators.
All numbers use Med42-Llama3-8B as a representative generator
to enable controlled comparison on the same outputs.
– indicates the metric is not supported by that tool.
Bold marks the best value in each row.
MedRAGChecker achieves comparable faithfulness while
additionally providing claim-level diagnostics, biomedical KG
verification, and safety-critical error detection.
All three frameworks achieve comparable faithfulness, as expected from shared NLI-style cores.
MedRAGChecker differs in four respects: claim-level granularity; KG verification that improves human agreement on decision-flip (69.8% vs. 63.4%); safety-critical error rates unavailable in general-purpose tools; and API-free deployment via distillation.
5 Conclusion
MedRAGChecker provides a claim-level diagnostic framework
for biomedical RAG that matches general-purpose evaluators on
faithfulness while surfacing safety-critical errors aligned with
human judgment on decision-flip claims. Our two-back-end analysis
further shows that KG coverage substantially affects fusion quality,
motivating the selective gating design. The methodology should
transfer to other high-stakes verification domains such as legal
and financial QA.
Limitations
Teacher supervision as pseudo-ground truth.
Our distillation and evaluation rely on teacher labels for claim
decomposition and NLI judgments, which may contain biases or
systematic errors, especially for rare biomedical conditions or
ambiguous questions. Our teacher-sensitivity analysis
(Appendix E,
Table 9) confirms that generator
rankings are stable under both GPT-4.1 and GPT-4o teachers
across research-style datasets, though absolute values on
consumer-health data (MedRedQA, $\kappa=0.13$ between teachers)
remain teacher-conditional.
Checker calibration and class imbalance.
Contradiction is typically a minority class. Even with ensembling, performance varies across datasets, and subtle contradictions can be under-detected. MedRedQA exhibits low inter-teacher agreement (Appendix Table 9); we therefore interpret absolute Faith/Halluc values on MedRedQA with caution and focus on within-teacher relative comparisons.
KG coverage and linker errors.
Our DRKG vs. BioPortal comparison shows that KG coverage substantially affects fusion quality (Section 4.5).
Even BioPortal does not cover all biomedical
entities and relations. Entity linking relies on SapBERT-based
matching and BioPortal API search, which can fail for rare entities,
complex paraphrases, or multi-hop claims.
BioPortal’s lower average consistency on some datasets
(Table 11) reflects its
inclusion of weaker hierarchical signals;
our selective gating strategy (Eq. 5) mitigates
this but does not fully resolve it.
For safety-critical relation families (drug–disease, drug–adverse-event), KG-based signals are most reliable; elsewhere, they complement but do not replace textual NLI verification.
General-purpose LLM-based evaluators may be less reliable in high-stakes medical settings without domain calibration, and standardized evaluation remains an open challenge for medical LLM applications.
Circularity of teacher supervision.
While the KG component is teacher-independent,
claim extraction and the primary NLI signal remain derived from
GPT-4.1, creating a partially circular evaluation loop.
A fully teacher-free pipeline would require human-annotated claims
at scale; we partially mitigate this through human validation
(Section 4.7) and teacher-robustness analysis
(Appendix E).
Domain generalization.
Our methodology (claim extraction, NLI + KG verification, fusion)
transfers to other technical domains such as legal and financial QA,
but requires a domain-specific KG and re-distillation of student models.
Cross-domain evaluation is left for future work.
Scale of human evaluation.
Our human validation comprises 100 questions $\times$ 3 generators
 $\times$ 2 annotators, a scale comparable to prior claim-level
human studies such as FActScore (Min et al., 2023).
Inter-annotator agreement is substantial on claim-set quality
( $\kappa=0.67$ ) but lower on holistic correctness ratings,
reflecting known difficulty in evaluating long-form medical
answers. Decision-flip-level conclusions should
be interpreted accordingly. Larger-scale validation with
multiple clinician annotators is a natural next step.

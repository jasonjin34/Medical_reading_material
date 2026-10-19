<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# On the Limits of LLM-as-Judge for Scientific Novelty Assessment

- **Authors:** Sinhahajari, Soumitra; Majumder, Navonil; Poria, Soujanya
- **Venue / Year:** arXiv preprint · 2026
- **DOI:** 10.48550/arXiv.2606.12071
- **URL:** https://arxiv.org/abs/2606.12071
- **Bibkey:** rq-bench-arxiv-2026
- **Status:** complete

## Abstract
LLMs are increasingly used to generate and judge scientific ideas. This makes novelty evaluation a central problem. Full idea evaluation is difficult because it often requires judging a method, its feasibility, and its empirical promise. We therefore study a cleaner upstream object: the research question (RQ). RQ generation is a prerequisite for scientific ideation, and RQs can be compared against questions pursued in real papers. We introduce RQ-Bench, a benchmark built from recent arXiv papers. For each paper, we reconstruct author-anchored RQs from its cited background, gaps, and contributions. These RQs are not the only valid questions for the same background. They are author-anchored reference points for testing novelty judgments. We evaluate model-generated RQs with standalone LLM judging, comparative LLM judging, and human expert evaluation. LLM judges consistently rate model-generated RQs as highly novel, producing a novelty mirage; in comparative evaluations, this preference becomes even stronger. Domain experts, however, reach the opposite conclusion and prefer the author-anchored reference questions. We further find that many generated RQs are narrow or source-bound, a dimension that LLM judges often miss unless explicitly tested. Overall, the contradictory novelty evaluations between LLM judges and human experts raise a serious concern about the reliability of using LLMs to assess the scientific novelty of research questions.

## Full text / Extract
<!-- Verbatim key passages (method, results, limitations) extracted from the open-access arXiv full text. Tables, figures and inline math symbols were dropped during extraction; see the deep-read for the numbers. -->

4 Benchmark Dataset Creation Let denote a target paper. We first extract a set of influential cited papers and the target paper’s main idea and contributions . For each influential citation , we collect its local citation context , consisting of the citation sentence in and its surrounding sentences. Let . We then infer grounded gaps that are both linked to the cited works and addressed by the target paper’s idea and contributions. Finally, we derive the research question from these grounded gaps:

Here, denotes the LLM-assisted extraction and construction pipeline as shown in Figure 2. The variable ensures that the resulting research question is not an unconstrained idea, but is grounded in the way the target paper uses influential prior work to motivate its own contributions.

The following sections detail our LLM-assisted pipeline that curates recent arXiv computer science papers to extract influential citations, core contributions, and grounded research gaps. These elements are ultimately synthesized into a comprehensive benchmark dataset comprising 1,434 research questions derived from 746 source papers.

Paper Sourcing.

The dataset is built from recent computer science papers (cs.AI, cs.CL, ) on https://arxiv.org. In our current version, we consider about 200K papers published between 01-01-2025 and 10-4-2026. Restricting the benchmark to papers that are certainly unseen by all LLMs would reduce scale and coverage. We therefore use recent papers and report author-anchor overlap as a diagnostic. If a model memorizes a paper or its RQ, this score should be high. If the score is low, the model may be generating a different valid question, or it may simply not recover the author-pursued direction.

Filtering.

The metadata of the above papers are retrieved with arxiv API, and we keep only the top 10% papers with available LaTeX source from each subfield of computer science (cs.*) based on their citation counts as a proxy for paper quality. Among these papers, we subsequently keep only those published in a conference or a journal, as indexed by Semantic Scholar11 1 https://www.semanticscholar.org; papers not indexed by Semantic Scholar are excluded.

Influential Citation Identification.

Good research papers are typically well grounded in existing literature, which shapes the research questions posed, the ideas proposed, and the contributions presented. To identify the most influential cited works within a paper, we prompt qwen3.5-27b-thinking Qwen Team (2026) with the following context: 1) the cited paper’s title, 2) citation frequency of the cited work in the paper, 3) each section name in which the citation appears—helping to discount loosely related references (e.g., in the introduction or related work), 3) each citation of the work with its local context, consisting of the parent sentence and three preceding and following sentences, to capture how central the cited work is to the paper.

The model then classifies each citation as an inspiration, a competitor/baseline, or as irrelevant, minimally influential, or a canonical reference (e.g., the original Transformer paper Vaswani et al. (2017)). Citations categorized as inspiration or competitor are subsequently treated as influential.

Idea and Contribution Extraction.

On the other hand, the key ideas and contributions of a paper are intended to address its underlying research questions, whether stated explicitly or implicitly. Accordingly, we extract these ideas and contributions from the paper content using gemini-3.1-pro22 2 https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview to inform and guide the subsequent extraction of research questions. We employ a frontier LLM for this step because accurately capturing these attributes is central, and its outputs are consistently higher quality than those of open-source alternatives such as qwen3.5.

Gap Identification.

New research ideas are typically proposed to address some gaps within a field. These gaps may not necessarily originate from the prior works in the domain. We are particularly interested in contributions that are explicitly motivated by previous research, as such the contributions yield gaps that are grounded in the literature and directly raise the research questions addressed by the paper. Thus to inform and guide the subsequent research question extraction, we retrieve the gaps that are both identified and addressed by the authors, by prompting gemini-3-flash33 3 https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview with the pre-extracted ideas and main contributions of the paper along with the influential citations with their in-paper local contexts. Notably in this step, the use of a lighter LLM is motivated by the smaller context size and the relatively simpler and extractive nature of the task, as the gaps are identified for each influential citation through independent prompts. This is aimed to isolate the individual role of the cited works in the ideas and contributions of the paper.

Research Question Generation.

Finally, research question generation is conceived as a bridge between the gaps in the literature, which are informed by the influential works cited in the paper, and the ideas and contributions of the paper that often address the research questions and, in turn, the gaps. Accordingly, gemini-3.1-pro is prompted with the gaps and the ideas and contributions of the influential citations to obtain the author-anchored research questions.

Final Dataset Details.

The final dataset RQ-Bench comprises 1,434 research questions grounded in 746 arXiv Computer Science papers spanning 13 sub-fields, with 2,464 RQ-citation links to 1,375 unique cited papers and 3,151 distinct gap statements in total. Each record contains the RQ text, the source paper’s arXiv ID, sub-field, novelty type, problem statement, and main-idea headline with its stated contributions; for every cited paper referenced by an RQ, we additionally release the section-wise extracted body text. RQs whose cited papers lacked retrievable section text were filtered out (27 RQs dropped). Per-statistic summaries are given in Table 1; the sub-field breakdown is in Table 13.

Author-Anchored RQs as Reference Points.

We use the reconstructed RQs as author-anchored reference points. They are not the only valid questions for the same background. A set of papers can support many plausible RQs. The value of the author-anchored RQ is that it gives a concrete human reference: it was pursued by real authors and led to a published paper. This lets us test whether LLM judges evaluate model-generated alternatives consistently against the same reference.

Verification.

With two checks, we verified the plausibility of the author-anchored LLM-extracted RQs being addressed by the source papers. Firstly, we asked gemini-3.1-pro to judge each RQ against the full text of its source paper. Secondly, human judges performed the same check on 50 randomly sampled RQs. gemini-3.1-pro approved 98% of the RQs, while human judges approved 100% of the sampled RQs. These results suggest that the extracted RQs are faithful to the source papers and support the quality of RQ-Bench.

5 Evaluation Setup 5.1 Novelty Scores Let be the five RQs generated by model for instance . Let be the author-anchored reference RQ.

We score each RQ on three metrics:

These denote originality, gap addressing, and non-obviousness. Each metric receives a score from 0 to 3. The rubric is given in Section A.1. We report results for each metric separately. We do not define novelty as the sum of the three scores.

Scoring settings.

We use two scoring settings:

In standalone scoring, each RQ is scored independently, without being shown alongside the author-anchored reference RQ or other generated RQs. This setting measures the absolute score assigned to each RQ under the rubric.

In comparative scoring, the author-anchored reference RQ and the five model-generated RQs are scored in the same context. This setting measures whether the judge prefers at least one model-generated RQ over the reference RQ for a given metric.

Metric-level Pass@5 comparison.

For both scoring settings, we compare the best model-generated RQ among the five candidates against the author-anchored reference RQ. For a scoring setting , instance , model , metric , and judge , let denote the score assigned to RQ . We define the model-reference score difference as Thus, means that judge assigned at least one generated RQ a higher score than the reference RQ for metric . This is a metric-level Pass@5 comparison.

Per-judge win, tie, and lose rates.

For each judge separately, we assign the outcome The corresponding per-judge rates are Combined-judge win, tie, and lose rates.

For analyses that require agreement across judges, we also define a combined-judge outcome. With two judges , the combined outcome is Thus, a combined win requires both judges to score the best model-generated RQ above the reference RQ. A combined tie means that neither judge scores the model below the reference, but the condition for a win is not met. All remaining cases are counted as losses.

The combined-judge rates are For comparative scoring, we report only the win, tie, and lose rates defined above. We do not report average comparative scores, because comparative scoring is intended to measure relative preference between generated and reference RQs within the same judging context.

Standalone score summaries.

For standalone scoring, we additionally report absolute score summaries. For judge , the mean standalone score of the author-anchored reference RQs is For model , the standalone Best@5 score is These score summaries are reported only for standalone scoring, alongside the standalone win, tie, and lose rates.

5.2 Scope and Narrowness Novelty is not only about whether a question mentions a gap. A question can be gap-shaped but still be narrow. We therefore study scope as a separate dimension. We focus on two signals. Source-boundedness asks whether the RQ stays too close to one background paper, dataset, metric, or ablation. Diagnostic framing asks whether the RQ mainly asks for an analysis or failure diagnosis instead of opening a broader research direction. Diagnostic RQs are not always bad. They become a problem when they are mistaken for strong novelty.

We score each RQ on two metrics:

These denote source-boundedness, and diagnostic framing. Each metric receives a score from 0 to 3; the lower the score is the broader the RQ. The rubric is given in Section A.2. We report results for each metric separately. The standalone and comparative scoring setups remain identical to the novelty scoring setups.

5.3 Author-Anchor Overlap Finally, we report author-anchor overlap. It measures whether the generated RQ follows the direction pursued by the source paper:

Here, . A score of 1 means “same broad topic, different question.” A score of 2 means “substantial overlap, but different scope.” This metric is not an absolute quality score. Low overlap can mean that the model generated a different question from the same background.

6.1 Experimental Setup We evaluate the research question generation capabilities of frontier language models through a controlled, LLM-as-a-judge empirical framework. The following details the baseline models, the judge configurations, and the step-by-step task formulation used to extract and score novel research questions.

Models Under Evaluation.

We evaluate a mix of open and proprietary high-thinking models:

qwen3-30b-a3b-thinking-2507, deepseek-v4-pro, gemma-4-31b-it, gpt-oss-20b, gpt-5.5, and gemini-3.1-pro. For models with explicit reasoning controls, we use their high-thinking or native reasoning mode.

All models are systematically deployed with their respective thinking modes activated and configured with manufacturer-recommended default sampling hyperparameters.

Judge Configurations.

To ensure systematic semantic verification, we employ two advanced reasoning models as judges: gemini-3.1-pro and deepseek-v4-pro. Both judges are configured with maximum reasoning budgets (thinking_level: high) and greedy decoding (temperature = 0.0) to enforce rigorous, reproducible evaluations.

Task Formulation.

Each author-anchored research question is rooted in one or more influential papers. To assess the models’ capacity for research ideation, we provide them with these source texts and prompt them to extract critical gaps, such as methodological limitations or open challenges. Based directly on these identified gaps, the models must formulate exactly five specific, answerable research questions. For multi-paper scenarios, the models are instructed to cross-reference the literature and synthesize convergent limitations into cohesive, novel questions. The generated outputs are then scored using the evaluation framework detailed in Section 5.

6.2 Results and Discussions Author-Anchor Overlap.

We report to show whether models reproduce the author-pursued direction. As shown in Table 2, most models score close to 1.0. This means they often find the broad area, but ask a different question. The strongest model, gpt-5.5, reaches 1.33. Low overlap may indicate a different underlying phenomenon. A background can support many valid RQs. The result mainly shows that models often generate alternatives rather than the question pursued by the paper.

Standalone Scoring.

Under standalone LLM judging, almost all model RQs receive higher best-of-five novelty scores than the author-anchored reference across all three metrics. The strongest model is consistently gpt-5.5, achieving the highest mean scores in non-obviousness, originality, and gap addressing. However, these elevated absolute scores do not translate into decisive wins. As shown in Table 3, while models frequently tie with the GT, their strict win rates remain notably low. Under the two-judge combined evaluation, even gpt-5.5 secures clear win rates of only 27.2% for non-obviousness and 38.4% for originality. Among the three evaluated dimensions, gap addressing yields the highest win rates, whereas non-obviousness remains the most challenging dimension for models to demonstrably surpass the reference. This suggests that standalone judging assigns high novelty scores to both author-anchored and model-generated RQs. Since each RQ is evaluated independently, high scores do not necessarily translate into clear wins. As a result, standalone evaluation produces high tie rates despite the elevated absolute scores.

Comparative Scoring.

The evaluation dynamics shift considerably when the judge assesses the reference RQ and model RQs side by side. As shown in Table 4, comparative scoring reduces the frequency of ties and significantly increases the strict win rates for model-generated RQs. Under the two-judge combined setting, the strict win rate for gpt-5.5 on non-obviousness jumps from 27.2% in standalone scoring to 49.1% in comparative scoring, accompanied by a sharp drop in its tie rate from 59.1% to 36.8%. When evaluating multiple RQs in the same shared context, LLM judges exhibit a clear tendency to break ties in favor of the generated outputs, amplifying the perceived performance of the models across all three novelty metrics.

Comparative evaluation forces judges to break ties, leading to a sharp increase in win rates for model-generated RQs and a corresponding drop in tie rates. This raises the question of whether the generated RQs are genuinely more novel than the author-anchored RQs, especially with respect to non-obviousness. To verify this, we proceed to human expert evaluation.

(a) Agreement (%) on comparative non-obviousness win rates between human experts and LLM judges.

(b) Win rate distribution for comparative non-obviousness scoring between GT and best-of-five RQs generated by gpt-5.5.

Reliability of LLM-as-a-Judge.

Since LLM judges consistently assigned high novelty scores to model-generated RQs, we conducted a human expert evaluation to assess their reliability. We sampled 50 instances from cs.CL and cs.LG. For each instance, we compared the author-anchored reference RQ (GT) with the best-of-five RQ generated by gpt-5.5. Domain experts from the same fields performed blinded comparative evaluations. To rigorously test the models’ ability to assess deeper scientific value, domain experts specifically evaluated the RQs based on the critical non-obviousness dimension, using the same rubric as the LLM judges.

Experts noted that many generated questions imitate the structure of research gaps, but remain less original and less non-obvious. They also reported that many questions are narrow and too tied to the background papers. This suggests that LLM judges may reward surface gap language while missing deeper aspects of novelty. Overall, the contradictory novelty evaluations between LLM judges and human experts question the reliability and trustworthiness of using LLMs to assess the scientific novelty of research questions.

Key Finding: Evaluation Reliability Question: How reliable is the LLM-as-a-judge paradigm for RQ generation as compared to human judgments?

Answer: To verify whether the high novelty scores assigned by LLM judges to model-generated RQs were reliable, we conducted a human expert evaluation. We then ran an expert study on 50 samples, specifically assessing the critical non-obviousness dimension. Table 5(a) and Table 5(b) show a strong gap between human experts and LLM judges. Human experts preferred the author-anchored GT RQs. LLM judges preferred the best-of-five gpt-5.5 RQs. Experts noted that many gpt-5.5 RQs identify gaps, but still lack originality, non-obviousness, and broader scientific scope. This raises concerns about using current LLMs as judges for RQ novelty.

7.1 Assessment of Narrowness As semantic similarity does not capture the expert concern, we turn to the narrowness test defined in Section 5.2, scoring each RQ on source-boundedness and diagnostic framing (lower is broader). Unlike the novelty tables, which report win/tie rates, the narrowness tables report win/lose rates.

Narrowness Results and Discussions As detailed in Table 7 and Table 8, standalone evaluations reveal that model-generated RQs are significantly narrower in scope than author-anchored references, and this limitation is mostly driven by source-boundedness. Under the two-judge combined evaluation, the author-anchored references achieve a mean source-boundedness score of 0.47, substantially outperforming even the best-performing models (e.g., gemini-3.1-pro at 0.90 and gpt-5.5 at 1.17). Consequently, models suffer massive lose rates against the reference in this dimension; for instance, gpt-5.5’s best RQs lose to the reference 71.7% of the time and win only 4.3%. Diagnostic framing, by contrast, is a negligible factor in the narrowness gap. In the standalone setting, the models’ diagnostic framing scores closely match the reference (0.01–0.06 vs. 0.08), resulting in predominantly tied comparisons (e.g., gpt-5.5 sees only a 2.5% win rate and 2.9% lose rate, meaning over 94% of cases tie).

When shifting from standalone to comparative assessment, the models’ disadvantage in narrowness becomes even more pronounced. As seen in Table 8, placing the RQs side-by-side amplifies the judges’ baseline preferences. Because the judges already favor the author-anchored RQs for their broader scope in standalone evaluation, the comparative format increases the models’ lose rates. For example, gpt-5.5’s source-boundedness lose rate jumps from 71.7% in standalone to 85.4% in comparative, and its diagnostic framing lose rate spikes from 2.9% to 53.4%.

Direct assessments of narrowness validate the experts’ qualitative observations that model-generated RQs are restricted in scope and lack non-obviousness. When explicitly evaluated for source-boundedness over the same 50 samples, LLM judges identified author-anchored references as less source-bound than gpt-5.5 (82–90% win rate; Table 9(a)). Furthermore, human evaluations of non-obviousness show strong agreement (up to 72–76%) with LLM evaluations of source-boundedness (Table 9(b)). This alignment confirms that human assessments of an RQ’s novelty (especially non-obviousness) have a strong correlation with narrowness.

One of the main findings of this paper is that, although human expert novelty evaluations strongly correlate with narrowness, LLM judges fail to capture this. Narrowness does not solve novelty evaluation by itself. Two broad questions can still differ in value. But it gives a more concrete axis for detecting polished but shallow RQs.

Non-Obv.

Orig.

Gap-Addr.

(a) Novelty – standalone score (Best@5).

(b) Narrowness – standalone score (Best@5, lower better).

Non-Obv.

Orig.

Gap-Addr.

(c) Novelty – standalone win (tie).

(d) Narrowness – standalone win (lose).

Non-Obv.

Orig.

Gap-Addr.

(e) Novelty – comparative win (tie).

(f) Narrowness – comparative win (lose).

(a) Agreement (%) on comparative non-obviousness win rates between human experts and LLM judges.

(b) Win rate distribution for comparative non-obviousness scoring between GT and RQs generated by gemini-3.1-pro (new prompt).

(a) Raw win rates for source-boundedness per LLM judge over the 50 samples; the winner is the less source-bound RQ (lower score). GT is consistently less source-bound than gemini-3.1-pro.

(b) Agreement (%) on the per-item winner: human experts decide on non-obviousness, LLM judges decide on source-boundedness (leaner RQ wins). Each cell is the share of the 50 items on which the two evaluators pick the same RQ (GT or gemini-3.1-pro).

7.2 Revised RQ Generation Prompt To address the narrowness observed in model-generated research questions, we modified the system prompt by removing constraining instructions (Section A.8). We then tested gemini-3.1-pro using this updated prompt and evaluated the generated RQs. As demonstrated in Table 10, while this prompt adjustment successfully mitigates narrowness (e.g., significantly lowering source-boundedness from 1.00 to 0.47), it introduces a clear trade-off by simultaneously degrading novelty scores across both originality ( ) and non-obviousness ( ).

To investigate this further, we conducted an expert evaluation on 50 random samples generated using the updated prompt. Human experts noted that the newly generated RQs are indeed broader. As shown in Table 11, human experts still predominantly prefer the author-anchored (GT) RQs in terms of non-obviousness, awarding them the win 62% and 56% of the time across the two experts. In contrast, the LLM judges continued to favor the model-generated RQs, choosing them 50% and 40% of the time. This is reflected in the agreement metrics (Table 11): intra-expert (54%) and intra-judge (62%) alignments are notably higher than the poor inter-group expert–judge agreement (30–40%).

Crucially, Table 12(b) shows a strong alignment (42–50%) is maintained between human experts’ non-obviousness judgments and the LLM judge’s source-boundedness evaluations. This reaffirms the strong correlation between human experts’ non-obviousness judgments and the source-boundedness assessments of LLM judges.

These results highlight a fundamental misalignment between human experts and LLM judges regarding novelty assessment. Human experts correlate less source-bound questions with greater non-obviousness. However, LLM judges exhibit the opposite tendency. Under the original prompt, the LLM awarded high novelty scores to model-generated RQs that were highly narrow and source-bound. Yet, when the updated prompt successfully mitigated this source-boundedness, the novelty scores assigned by the LLM (particularly for non-obviousness and originality) concurrently declined. This implies that LLM-judged novelty is conflated with narrowness, diverging from human assessments of what constitutes genuine non-obviousness. These findings motivate the development of more robust novelty evaluation frameworks, including better metrics and more reliable LLM-as-a-judge protocols.

8 Conclusion We studied the reliability of LLM-as-judge for scientific novelty assessment. We used research-question generation as the testbed because it is an upstream step before full idea generation. It is also easier to inspect than a complete method or research plan.

RQ-Bench provides author-anchored RQs from real papers. These RQs are reference points, not the only valid questions. This setup lets us compare model-generated RQs against human-anchored RQs and test whether novelty judgments are stable.

Our results show a novelty mirage. Under standalone scoring, LLM judges rate model-generated RQs as highly novel in every novelty dimension (i.e., non-obviousness, originality, and gap-addressing). In comparative settings, the judges amplify it, heavily favoring model outputs over author-authored baselines. However, domain experts sharply disagree with these judgments, preferring the author-anchored RQs for their broader scope and non-obviousness. Crucially, when we explicitly instructed LLMs to evaluate this narrowness, their assessments of source-boundedness strongly aligned with human judgments of non-obviousness.

These results do not mean that novelty evaluation is impossible. Novelty is partly subjective, and even human reviewers can disagree. But useful evaluation should be stable across settings and should not strongly conflict with expert judgment. Our findings show that current LLM-as-judge pipelines do not yet meet this standard for scientific RQ novelty. Future evaluations should use multiple judges, check agreement, and include scope or narrowness as a first-class dimension.

Limitations Our benchmark is currently limited to recent computer science papers from arXiv and may not fully capture research practices in other scientific domains. In addition, novelty evaluation remains challenging due to the central dependence on LLM-as-judge for open-ended research question generation. While we include expert evaluations to study this issue, broader and more diverse human studies are still needed.

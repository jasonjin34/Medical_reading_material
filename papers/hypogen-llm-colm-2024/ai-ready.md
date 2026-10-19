<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# Large Language Models as Biomedical Hypothesis Generators: A Comprehensive Evaluation

- **Authors:** Qi, Biqing; Zhang, Kaiyan; Tian, Kai; Li, Haoxiang; Chen, Zhang-Ren; Zeng, Sihang; Hua, Ermo; Hu, Jin-Fang; Zhou, Bowen
- **Venue / Year:** COLM 2024 (Conference on Language Modeling) · 2024
- **DOI:** —
- **URL:** https://arxiv.org/abs/2407.08940
- **Bibkey:** Qi_2024
- **Status:** complete

## Abstract
The rapid growth of biomedical knowledge has outpaced our ability to efficiently extract insights and generate novel hypotheses. Large language models (LLMs) have emerged as a promising tool to revolutionize knowledge interaction and potentially accelerate biomedical discovery. In this paper, we present a comprehensive evaluation of LLMs as biomedical hypothesis generators. We construct a dataset of background-hypothesis pairs from biomedical literature, carefully partitioned into training, seen, and unseen test sets based on publication date to mitigate data contamination. Using this dataset, we assess the hypothesis generation capabilities of toptier instructed models in zero-shot, few-shot, and fine-tuning settings. To enhance the exploration of uncertainty, a crucial aspect of scientific discovery, we incorporate tool use and multi-agent interactions in our evaluation framework. Furthermore, we propose four novel metrics grounded in extensive literature review to evaluate the quality of generated hypotheses, considering both LLM-based and human assessments. Our experiments yield two key findings: 1) LLMs can generate novel and validated hypotheses, even when tested on literature unseen during training, and 2) Increasing uncertainty through multi-agent interactions and tool use can facilitate diverse candidate generation and improve zero-shot hypothesis generation performance. However, we also observe that the integration of additional knowledge through few-shot learning and tool use may not always lead to performance gains, highlighting the need for careful consideration of the type and scope of external knowledge incorporated. These findings underscore the potential of LLMs as powerful aids in biomedical hypothesis generation and provide valuable insights to guide further research in this area. Data and code at https://github.com/TsinghuaC3I/LLM4BioHypoGen/.

## Full text / Extract
> Full text (main paper, Sections 1–6) extracted from the arXiv PDF v2 with pdftotext; figure text is garbled where charts were embedded, references and appendices omitted.

1

Introduction

Biomedical research is a driving force behind advancements in human health and well-being.
However, the exponential growth of biomedical data and literature has made it increasingly difficult for researchers to keep pace with the latest discoveries and generate novel
hypotheses. Large language models (LLMs) (Touvron et al., 2023a;b; Jiang et al., 2024) have
emerged as a promising solution to this challenge, offering the potential to revolutionize the
way we interact with and discover knowledge in the biomedical domain(Wang et al., 2023a;
Taylor et al., 2022). At the core of the knowledge discovery process is the formulation of
sound hypotheses (Zhong et al., 2023; Boiko et al., 2023). Currently, both ChatGPT, GPT-4,
∗ Equal contributions.
† Corresponding authors.

1


Instruction: You are a researcher. You can come up with new hypotheses based on your existing knowledge. Hypotheses are
given against the following background. You should be as detailed as possible.
Background knowledge: (1) Esophageal cancer mainly includes squamous cell carcinoma and adenocarcinoma, with different
risk factors and incidence rates. (2) Metformin has been shown to reduce the risk of several cancers in patients with T2DM. (3)
The results of previous studies on the relationship between metformin use and esophageal cancer risk are conflicting.
The model hypothesizes: (1) The use of metformin in patients with T2DM mav be associated with a reduced risk of
esophageal cancer.
(2) There may be differences in the correlation between metformin use and the risk of esophageal cancer in male and female
patients with T2DM. （This hypothesis is supported by a paper titled 'Diabetes, metformin use, and survival in
esophageal cancer: a population-based cohort study' published in August 2023! ）

Figure 1: This illustration demonstrates a generated hypothesis using the fine-tuned 65B
LLaMA model within our specially constructed dataset. The generated hypothesis closely
aligns with the findings in existing literature published subsequent to the training sets.
and other open-source LLMs undergo extensive pre-training on a substantial amount of
data. The analysis and validation of related hypothesis generation work rely on these
models (Wang et al., 2023b; Yang et al., 2023b). However, due to the non-traceability of the
training data, these endeavors cannot ensure data invisibility, i.e., the inability to guarantee
non-overlapping between test and training data. This limitation hinders the assessment and
analysis of knowledge discovery in LLMs under zero-shot conditions.
In this paper, we present a comprehensive evaluation of LLMs as biomedical hypothesis
generators. We construct a dataset of background-hypothesis pairs from biomedical literature, carefully partitioned into training, seen, and unseen test sets based on publication
date to mitigate data contamination. Using this dataset, we assess the hypothesis generation capabilities of top-tier instructed models in zero-shot, few-shot, and fine-tuning
settings. To enhance the exploration of uncertainty, a crucial aspect of scientific discovery,
we incorporate tool use (Schick et al., 2023a) and multi-agent interactions (Xi et al., 2023b)
in our evaluation framework. These strategies are inspired by uncertainty exploration in
reinforcement learning (Watkins & Dayan, 1992; Schulman et al., 2017) and aim to examine
the influence of uncertainty on knowledge discovery and the primary factors contributing
to zero-shot capability.
Our experiments yield two key findings: 1) LLMs can generate novel and validated hypotheses, even when tested on literature unseen during training (Figure 1), and 2) Increasing
uncertainty through multi-agent interactions and tool use can facilitate diverse candidate
generation and improve zero-shot hypothesis generation performance. However, we also
observe that the integration of additional knowledge through few-shot learning and tool use
may not always lead to performance gains, highlighting the need for careful consideration
of the type and scope of external knowledge incorporated.
These findings underscore the potential of LLMs as powerful aids in biomedical hypothesis
generation and provide valuable insights to guide further research in this area. Our specific
contributions include:
• We pioneer the rigorous validation of LLMs in zero-shot and few-shot hypothesis generation through the creation of temporal biomedical instruction data and
innovative experiments for in-depth analysis and evaluation.
• Our findings reveal that LLMs exhibit foundational higher-order reasoning abilities
and can generate novel hypotheses, offering fresh empirical insights for knowledge
discovery.
• We develope multidimensional metrics for evaluating hypotheses with GPT-4 and
human. The correlation between these evaluations suggests LLMs’ substantial role
in hypothesis evaluation.
• We propose a LLM-based multi-agent framework for hypothesis generation. This
system facilitates collaborative analysis among various roles and tools, enhancing
our understanding of the influenced factors of LLM-based proposers.
2

Experimenal Loop of Scientific Discovery

2

Preliminary
Text Pool

1) Data Understanding & Analysis

2) Generating Hypotheses
10,000 medical
papers from PubMed

3) Experimental Design
5) Accumulating Observations

Pairs
Background knowledge: (1)…(2)…(3)…
Hypotheses:
(1)…(2)…(3)…

SFT

Train
Instruction:…
Background:…

Before

Model output:…

January
2023

Eval

4) Experiment Implement

(a) Scientific Discovery Process

Instruction:…
Background:…

After

Golden output:…

January 2023

(b) Dataset Construction Pipeline

Figure 2: (a) The iterative loop of scientific discovery involves a cyclical process: observations and data from previous experiments are analyzed, leading to the generation of new
hypotheses. These hypotheses then guide the design of subsequent experiments, producing
fresh data to perpetuate the cycle. (b) We execute the automated data partitioning pipeline,
using publication dates as the basis, to mitigate the risk of data contamination.
In this section, we delineate the problem of hypothesis generation. Subsequently, we
elucidate the process for developing biomedical-specific datasets. We then analyze the
constructed datasets, examining aspects of data contamination and the semantic distribution
across different data settings.
2.1

Problem Definition

As shown in Figure 2a, hypothesis generation typically transpires following an in-depth
analysis of literature and detailed examination of specific phenomena, playing a pivotal role
in the scientific discovery process. In order to improve the assessment of the hypothesis
proposition capabilities of LLMs, we formalize this process as a text completion task. Given
dataset D, an instruction I, and text pairs ( Xi , Yi )in=1 containing background knowledge
and corresponding hypotheses extracted from medical papers, our objective is to assess
model M by having it generate hypotheses based on the task instruction and background
knowledge, i.e., M ( I, Xi ) = Yi , for each i ∈ 1, ..., n. The objective function is formulated as:
n

y∗ = arg max ∏ P(yt |y1 , . . . , yt−1 , I, X ).
y1 ,...,yn

2.2

t =1

Dataset Construction

Existing LLMs, including ChatGPT and Llama, encounter challenges in retracing their
training data, complicating efforts to ensure non-overlap with the test set. To rigorously
assess the hypothesis generation capability of LLMs, we initially create evaluation datasets
based on literature, taking into account the publication date.
Unlike previous studies that assess data contamination through the correlation between
question entropy and accuracy (Hendrycks et al., 2020; Wei et al., 2023b; Zhou et al., 2023),
our method directly controls visibility by considering both the training date and the publication date. This method ensures that the test data remains non-visible, addressing a
limitation overlooked in earlier methods. As depicted in Figure 2b, the year 2023 has been
established as the cut-off point, coinciding with the publication date of the majority of
top-tier LLMs. The training dataset includes literature published before January 2023, while
the test dataset contains literature after January 2023. This arrangement creates pairs of
data with background knowledge and corresponding hypothesis proposals. We strictly
follow the standard pipeline as outlined in Self-Instruct (Wang et al., 2022) for our data
generation process: 1) Compose the paper set based on the topic and content of the literature. 2) Utilize ChatGPT and GPT-4 to summarize the literature knowledge. 3) Generate
background knowledge-assume pairs. 4) Filter low-quality data by publishers. 5) Split the
dataset according to publication time.
3


While this approach allows for efficient dataset creation, we acknowledge that the accuracy
of ChatGPT’s extractions and any biases introduced in the process warrant further evaluation. Manual annotation of a subset of the data could help assess the quality and reliability
of the automated extraction.
Adhering to the above pipeline outlined, we ultimately acquired two distinct types of
datasets. 1) Seen dataset This dataset comprises 2700 background and hypothesis pairs
sourced from literature published before January 2023. This dataset was partitioned into
training (2500) and validation (200) subsets (as well as seen test set). It is consistent with the
corpus that the LLMs have been exposed to. 2) Unseen dataset The unseen dataset consists
of 200 pairs extracted from papers published in August 2023, which the LLMs have not
encountered during training and are used for testing purposes.
More detailed information with respect to publication data and topic distributions of
constructed dataset can be seen in Appendix C.1.

3

Can LLMs Truly Generate Zero-Shot Hypotheses?

In this section, we conduct a thorough evaluation of premier LLMs across a range of
experimental settings to determine their ability to effectively generate hypotheses and
analyze influenced factors.
3.1

Experiment Setup

Initially, we present the models being evaluated, outline the experimental settings, and
describe the metrics used for evaluation.
Models For a fair comparison, we exclusively evaluate LLMs trained on corpora before
March 2023 to avoid data contamination. We consider three categories of models: 1) APIbased LLMs: this is mainly ChatGPT. 2) General domain instructed LLMs: These models
consist of open-source models that have undergone fine-tuning based on Llama using
general domain instructions. We primarily choose the top-tier models based on rankings
before Setember 2023 in the Alpaca Eval Leaderboard 1 . 3) Specific domain instructed LLMs:
These include PMC-LLaMA (Wu et al., 2023), and MedAlpaca (Han et al., 2023), which are
trained on a variety of sources in medicine domain. We summarize the training data and
publication dates for each models in Appendix C.2.
Prompts and Finetuning To ensure a consistent output format across different models, we
create prompts in two formats: zero-shot and few-shot examples. We adopt a 5-shot format,
selecting examples from the training set before January 2023 using both randomly sampled
and similarity retrieval methods. To assess the hypothesis generation capability beyond
zero-shot, we identify the top-performing open-source models through prompting-based
evaluation. Finally, we proceed to fine-tune WizardLM-13B-V1.2 with the background and
hypothesis pairs for further comparison. We provide more details in Appendix F.
Evaluation Metrics Given the inherent uncertainty beyond established ground truth in
hypothesis generation, we undertake evaluations with and without predefined golden
hypotheses. 1) With ground truth: In evaluations with golden hypotheses, we employ
standard text generation metrics, including BLEU (Papineni et al., 2002) and ROUGE (Lin,
2004) , to assess word overlap between the generated outputs and the ground truth. 2)
Without ground truth: Considering the vastness of the hypothesis space, renders it difficult
to comprehensively assess the quality of generated hypotheses using word overlap metrics
alone. To provide a more comprehensive evaluation of the generated hypotheses from
multiple facets, we devise four metrics for evaluation (Zhong et al., 2023):
• Novelty: Does the hypothesis introduce new information or perspectives?
• Relevance: How closely is the hypothesis related to the topic or question?
1 https://tatsu-lab.github.io/alpaca eval/

4


• Significance: What impact does the hypothesis have on understanding or addressing
the problem?
• Verifiability: Can the hypothesis be tested using existing methods or data?
Furthermore, inspired by recent research that highlights LLMs as proficient annotators (Gilardi et al., 2023; Liu et al., 2023), demonstrating a strong correlation with human ratings,
we employ GPT-4 for automated evaluation, where both the generated hypotheses and the
provided background are evaluated across these aspects. The scoring scale ranges from 0 to
3, where a higher score indicates superior results. Additionally, we solicit GPT-4 to furnish
a step-by-step explanation to substantiate the assigned score. We also conduct human
evaluation for the top-tier models identified in the evaluation of GPT-4 in Section 3.4.
3.2

Experiment Results
Split
20

seen
unseen

BLEU Score

15

split

10

seen
unseen

5

0 )
t
t) t)* t) t) t)* t) t) t)* t) t) t)* t) t) t)* t) t) t)* t) t) t)* t) t) t)* .2
-sho -sho ho -sho -sho ho -sho -sho ho -sho -sho ho -sho -sho ho -sho -sho ho -sho -sho ho -sho -sho ho -V1
o(0 rbo(5 rbo(5-sv1.3(0 v1.3(5 1.3(5-schat(0 chat(5 hat(5-s 1.2(0 1.2(5 1.2(5-s 1.0(0 1.0(5 1.0(5-s per(0 per(5 per(5-s13B(0 13B(5 3B(5-s13B(0 13B(5 3B(5-s M-13B
b
r
u 5-tu -tu 3b- 3b- b-v 0b- 0b- b-c 3B-V 3B-V B-V 0B-V 0B-V B-V 2-su 2-su -su ca- ca- a-1 MA- MA- A-1 rdL
t
5
3 -7 -7
0 3. 3. .2 lpa lpa ac La La aM iza
-3. -3. .5 -3 -3 33 -7 -7 70 -1 -1
gpt gpt gpt-3VicunaVicuna icuna- ama-2 ama-2 ma-2- ardLM ardLM rdLM-1ardLM ardLM rdLM-7chat-v chat-v hat-v3 MedA MedA edAlpPMC-L PMC-L MC-LL W
M
P
V Ll Ll Lla Wiz Wiz Wiza Wiz Wiz Wiza pen pen penc
O O O

Figure 3: This figure displays the BLEU scores on both seen and unseen datasets.
This section presents the results of hypothesis generation across various models in both
zero-shot and few-shot settings. We primarily analyze the results from two perspectives:
the impact of the zero-shot setting and the influence of introducing external knowledge on
hypothesis generation.
3.2.1

Results of Zero-shot Setting

The results presented in Figure 3 and 4 demonstrate the significant impact of zero-shot
settings in improving hypothesis generation, particularly in terms of fostering high novelty.
Detailed results are provided in Appendix D.1. In this section, we primarily analyze these
results from two critical perspectives as outlined below:
Zero-shot vs. Few-shot Figure 4 demonstrates that nearly all models, particularly WizardLM
series models, and Openchat-v3.2-super, show enhanced novelty capabilities in a zero-shot
setting. Concurrently, these models also demonstrate superior verifiability when presented
with few-shot literature examples. This indicates a trade-off in the hypothesis generation
capacity of LLMs, necessitating careful consideration of specific constraints. Notably, there
are divergent results concerning medical domain adaptation in LLMs, which will be further
discussed in the subsequent Section 3.2.2.
Seen test-set vs. Unseen test-set Despite the inclusion of literature published before 2023
in the pre-training corpus of most LLMs, we have delineated “seen” and “unseen” test
sets, with the “unseen” test set being considered for zero-shot analysis. Generally, LLMs
are likely to show enhanced performance on the “seen” test set, potentially due to the
memorization of knowledge acquired during training, resulting in a superior performance
5


Model: gpt-3.5-turbo

Model: Vicuna-33b-v1.3

Relevance

Significance

Significance
0

1

0

1

2 Novelty
3

Verifiability

Significance
1

1

Model: Openchat-v3.2-super

1

Verifiability

Relevance

Significance
0

1

2 Novelty
3

Verifiability

Avg

2 Novelty
3

Model: PMC-LLaMA-13B

Relevance

2 Novelty
3

1

Avg

Significance
0

0
Verifiability

Model: MedAlpaca-13B

Relevance

2 Novelty
3

Verifiability

2 Novelty
3

Avg

Significance
0

0

Avg

Relevance

Relevance

Significance

Verifiability

Avg

Model: WizardLM-70B-V1.0

Model: WizardLM-13B-V1.2

Relevance

Significance

2 Novelty
3

Verifiability

Model: Llama-2-70b-chat

Relevance

0

1

2 Novelty
3

Verifiability

Avg

Avg

Avg

0-shot

5-shot

5-shot*

Figure 4: This figure depicts a comparative analysis of multiple models across distinct
prompting paradigms, such as zero-shot, sampled and similarity retrieval-based few-shot.

compared to the “unseen” test set. Contrarily, our findings presented in Figure 3 reveal
that LLMs tend to exhibit better performance on the “unseen” test set. We hypothesize that
the intricacies involved in hypothesis generation may impede LLMs’ ability to effectively
utilize the parameterized “dark knowledge”.

0.95
0.94

0.94

vicuna-33b-v1.3,5-shot
medalpaca-13b,5-shot*
wizardlm-13b-v1.2,5-shot
vicuna-33b-v1.3,5-shot*
wizardlm-13b-v1.2,5-shot*
openchat-v3.2-super,5-shot
gpt-3.5-turbo,5-shot*
wizardlm-70b-v1.0,5-shot*
wizardlm-70b-v1.0,5-shot
llama-2-70b-chat,0-shot

0.93
0.92

SelfBLEU Score

SelfBLEU Score

0.95

pmc_llama_13b,5-shot*

0-shot
openchat-v3.2-super,0-shot
5-shot
llama-2-70b-chat,5-shot
medalpaca-13b,5-shot
llama-2-70b-chat,5-shot*
5-shot* pmc_llama_13b,5-shot

pmc_llama_13b,0-shot
wizardlm-13b-v1.2,0-shot

0.91

medalpaca-13b,0-shot

gpt-3.5-turbo,5-shot
openchat-v3.2-super,5-shot*

0.25

0.50

0.93

0.91

0.75 1.00 1.25 1.50 1.75
Evaluation Score (Novelty)

pmc_llama_13b,0-shot

medalpaca-13b,0-shot

gpt-3.5-turbo,5-shot

openchat-v3.2-super,5-shot*

wizardlm-70b-v1.0,0-shot

1.00

(a) Correlation of uncertainty and novelty.

wizardlm-13b-v1.2,0-shot
gpt-3.5-turbo,0-shot
vicuna-33b-v1.3,0-shot

0.90

2.00

pmc_llama_13b,5-shot*
llama-2-70b-chat,5-shot*
llama-2-70b-chat,5-shot
openchat-v3.2-super,0-shot
medalpaca-13b,5-shot
pmc_llama_13b,5-shot
vicuna-33b-v1.3,5-shot
medalpaca-13b,5-shot* wizardlm-13b-v1.2,5-shot
wizardlm-13b-v1.2,5-shot* vicuna-33b-v1.3,5-shot*
wizardlm-70b-v1.0,5-shot
gpt-3.5-turbo,5-shot*
openchat-v3.2-super,5-shot wizardlm-70b-v1.0,5-shot*
llama-2-70b-chat,0-shot

0.92

gpt-3.5-turbo,0-shot

vicuna-33b-v1.3,0-shot
wizardlm-70b-v1.0,0-shot

0.90

0-shot
5-shot
5-shot*

1.25

1.50 1.75 2.00 2.25
Evaluation Score (Verifiability)

2.50

(b) Correlation of uncertainty and verifiability.

Figure 5: This figure elucidates the correlation between uncertainty and evaluation scores
for all models, encompassing both zero-shot and few-shot settings, and incorporating both
sampled and similarity retrieval few-shot prompts.

3.2.2

Results of External Knowledge

We further extend analysis to the influence of external knowledge, including few-shot
examples, domain adaptation, and instruction tuning. The findings indicate that these
factors do not consistently enhance performance across all metrics.
Few-Shot Examples Enhance Verifiability but Decrease Novelty. Regarding word overlap
metrics, including BLEU and ROUGE, most models, especially gpt-3.5-turbo and WizardLM
series models, show improved performance when provided with in-context examples as
shown in Figure 3. However, it’s important to note that these few-shot prompts significantly
increase verifiability while simultaneously leading to lower novelty compared to zero-shot
results as shown in Figure 4.
6


Category

ChatGPT

Model

Human Eval

Avg Coefficient

Eval.Avg

Novelty

Relevance

Significance

Verifiability

Avg

Pearson

Spearman

API-based

gpt-3.5-turbo(0-shot)
gpt-3.5-turbo(5-shot)*

1.90
1.96

1.54
1.31

2.69
2.62

1.77
2.08

2.08
2.62

2.02
2.15

0.87
0.80

0.78
0.78

General

Llama-2-70b-chat(0-shot)
Llama-2-70b-chat(5-shot)
Llama-2-70b-chat(5-shot)*
WizardLM-70B-V1.0(0-shot)
WizardLM-70B-V1.0(5-shot)

2.04
2.20
2.01
1.91
2.01

1.77
2.15
1.38
1.38
1.15

2.23
2.77
2.62
2.31
2.69

1.92
2.08
2.31
1.54
2.46

1.92
2.31
2.00
2.00
1.77

1.96
2.33
2.08
1.81
2.02

0.89
0.96
0.97
0.90
0.85

0.84
0.90
0.94
0.75
0.89

PMC-LLaMA-13B(0-shot)

1.41
1.97

1.00
1.85

2.62
2.23

1.92
1.92

2.00
1.69

1.88
1.92

0.73
0.95

0.73
0.94

WizardLM-13BV1.2

1.79

0.85

2.77

1.23

2.23

1.77

0.83

0.85

Medicine
背景分析、信息检索、假设提出、评估反馈
PMC-LLaMA-13B(5-shot)*
SFT

Table 1: This table presents the results of human evaluation. The Avg Coefficient are used to
assess the correlation between the average scores obtained from ChatGPT and human.

Randomly Sampled Few-Shot Examples vs. Similarity Retrieval. Given that randomly
sampled in-context examples frequently diverge in topics or domains from the given background, this variation can potentially confuse LLMs while heightening uncertainty. In
contrast, few-shot examples acquired through similarity retrieval are more likely to bolster
verifiability but may reduce novelty.

C: Design Experiments for How t

Impact of Domain Adaptation We also conduct an analysis of the influence of fine-tuning
for biomedical domain adaptation on hypothesis generation. The results obtained from
MedAplaca and PMC-LLaMA indicate that domain adaptation can significantly improve word
overlap performance. Evaluation derived from GPT-4 imply that domain adaptation improves the capability of LLMs in utilizing few-shot, particularly with related literature,
while diminishing their zero-shot ability.
Impact of Instruction Tuning In addition to domain adaptation, we also examine the effect
of direct fine-tuning of LLMs on specially constructed instruction training sets. The findings
reveal that instruction tuning enhances the capacity of LLMs for knowledge retention,
leading to improved BLEU and ROUGE scores and heightened verifiability, especially
when contrasted with models without fine-tuning. However, this enhanced memorization
concurrently
diminishes
theHypothesis
model’sProposing
capability to generate novel and significant hypotheses.
Multi Agents Collaboration
based
1) Analyst

Uses keywords from Analyst
Searches for relevant information
Compiles and organizes findings

Evaluates proposed hypotheses
Ensures scientific validity
Provides feedback for refinement

2.5

Formulates hypotheses
Interprets Engineer's findings
Bridges existing literature with new insights

4) Critic

User

Critic

Guid e[Opt io nal ]

1.5

setting

ChatGPT
ChatGPT+Tooluse(ReAct)
ChatGPT+Tooluse(OpenAI)
ChatGPT+Multi-Agent
ChatGPT+Multi-Agent+Tooluse

1.0

Hypothesis
Proposing
Engineer
Sear c h

2.0
Evaluation Score

3) Scientist

Ev al uat e

Scientist
Fo r mul at e

ChatGPT
ChatGPT+Tooluse(ReAct)
ChatGPT+Tooluse(OpenAI)
ChatGPT+Multi-Agent
ChatGPT+Multi-Agent+Tooluse

2) Engineer

Analyzes research background
Extracts keywords and topics
Provides direction for searches

0.5

Analyst
Ext r ac t
0.0

(a) Overview of Multi-agent Framework.

Novelty

Relevance

Significance

Verifiability

Avg

(b) Results of tool use and multi-agent.

Figure 6: (a) The conceptual system of multi-agent collaboration for hypothesis generation.
The overall prototyping process is illustrated below, allowing users to choose optional
involvement. We offer core role descriptions of multi-agents and the fully automated system
above. (b) Results of individual agents and multi-agent systems, both with and without the
use of tools, on the unseen test dataset. The results demonstrate the influence of multi-agent
collaboration and tool use in enhancing the ability of LLMs in hypothesis generation.

7


3.3

Quantitative Analysis on Uncertainty

Drawing from the findings in zero-shot settings and the impact of external knowledge, we
identify uncertainty as the key differentiator among these scenarios. The few-shot setting
tends to enhance the creative capacity of LLMs, yielding content with higher generalization
and diversity. In terms of external knowledge, parameterized knowledge and judiciously
selected samples narrow the candidate space, thereby reducing the uncertainty of generated
content but enhancing verifiability. Conversely, randomly sampled few-shot examples
introduce uncertainty. There are many methods for computing uncertainty, including
those based on entropy, semantics, and consistency (Kuhn et al.; Xiong et al.). However,
these methods often entail a high computational cost, primarily due to the requirement for
multiple sampling iterations, rendering them impractical for our experiments. Given the
pioneering nature of our research in applying Large Language Models (LLMs) to knowledge
discovery, and to maintain manageability within the scope of this paper, we have chosen to
use SelfBLEU (Alihosseini et al., 2019) to evaluate the internal uncertainty of all generated
hypotheses. The SelfBLEU scores serve as indicators of uncertainty in the hypotheses
generated by LLMs, where lower scores signify greater uncertainty and diversity.
As depicted in Figure 5, we examine the relationship between uncertainty and detailed
evaluation scores of various models under different settings, including zero-shot and fewshot settings (the latter comprising sampled and retrieved examples, denoted as 5-shot
and 5-shot*, respectively). Our findings reveal that hypotheses generated in the zero-shot
setting exhibit higher uncertainty and novelty scores, as illustrated in Figure 5a. Conversely,
few-shot settings with augmented hypotheses demonstrate lower uncertainty yet higher
verifiability, as indicated in Figure 5b. These observations offer valuable insights for further
research into the balance between novelty and verifiability in hypothesis proposing. Motivated by these findings, we propose a LLM-based multi-agent framework to delve into
uncertainty exploration involving tools and multi-agents collaboration in Section 4.
3.4

Human Evaluation and Case Study

In this section, we conduct human evaluation to assess the coherence of hypotheses generated by LLMs, comparing these with GPT-4 evaluation scores to guide further automated
evaluations.
Settings We apply the four metrics from Section 3.1 (novelty, relevance, significance, and
verifiability) for manual evaluation and comparison with GPT-4’s assessments, where each
metric is scored from 0 to 3. Due to cost constraints, human evaluation focuses on the
highest-performing LLM based on automatic metrics and GPT-4 evaluations. The selected
models and prompts are listed in Table 1. 100 examples from the unseen test set were
evaluated by three experts in the biomedical field.
Results The results in Table 1 show a strong correlation (Pearson and Spearman coefficients
above 0.7) between human and GPT-4 evaluations, reinforcing the potential of LLMs in
hypothesis evaluation. For further insights, we analyze the correlation between word
overlap scores and manual scores in the Appendix D. A case study illustrating various
model-generated hypotheses and ChatGPT evaluations is available in Appendix E. Notably,
we have collaborated with experts in medicine and biology and adopted a 5% sampling rate
for expert evaluation. Given the constraints of manpower and costs, a full-scale evaluation
was not feasible. However, we believe that a 5% sampling rate provides a statistically
representative overview and effectively reflects the overall quality of the data. We appreciate
your understanding and support in this matter.

4

Can agent collaboration enhance LLMs’ zero-shot generalization?

In this section, we aim to improve LLMs’ hypothesis generation capability by leveraging
uncertainty with tool use and multi-agent collaboration. We firstly introduce the conceptual
multi-agent system for hypothesis generation, drawing inspiration from scientific research.
8


Subsequently, we present the role design and the tools use in this context. Finally, we present
preliminary validated results of the multi-agent system on the constructed dataset.
4.1

Multi-agent Framework

Inspired by the discovery process in Figure 2a, we introduce a comprehensive framework
tailored for hypothesis formulation. This framework encapsulates a multi-agent system
where each agent assumes a distinct role, mirroring the collaborative nature of scientific
endeavors. Through a symbiotic and iterative process, these agents collaborate to craft
hypotheses that are not only grounded in existing knowledge but also pave the way for
novel insights. By emulating the essence of scientific discovery, our framework strives
to produce hypotheses that are both innovative and scientifically robust. As depicted in
Figure 6a, we partition the framework into five components, encompassing four automated
agents and the option for human involvement within the loop.
Role Design In our proposed multi-agent framework, each component plays a distinct and
pivotal role. The Analyst serves as the foundation, meticulously extracting and defining core
elements from the research background. Its primary objective is to interpret the literature,
distilling it into keywords or topics that subsequently guide the Engineer’s search efforts.
The Engineer, leveraging these keywords, embarks on a mission to retrieve and organize
pertinent information. They meticulously plan and execute detailed searches, ensuring that
the findings are compiled in a structured manner. This organized materials then lands in
the domain of the Scientist, whose objective is to weave together the Engineer’s findings
with the original research background. Through careful interpretation, the Scientist crafts
a hypothesis that is both grounded in existing knowledge and offers a fresh perspective.
However, before this hypothesis is finalized, it undergoes scrutiny by the Critic. The
Critic’s role is paramount in ensuring the hypothesis’s robustness, coherence, and novelty.
They evaluate the hypothesis against the backdrop of the research background, ensuring
it stands up to academic rigor. Feedback from the Critic, if necessary, loops back to refine
the hypothesis or prompts the Analyst for further insights, creating a cyclical and iterative
process of refinement.
Tool Use To explore external knowledge beyond the inherent dark knowledge within LLMs,
we integrate the Engineer agent with search engines , mainly PubMed 2 . Similarly, to control
the visibility of the unseen test dataset, we filter and exclude literature published after January 2023 from the search results. We carry out tool use experiments using ReAct (Yao et al.,
2023b) and OpenAI function calling. ReAct is a method that extends the concept of Chain of
Thought (CoT) (Wei et al., 2022), involving thinking before taking action and subsequently
making observations based on feedback from the environment. In our experiments, we
instruct the LLMs to initially contemplate the provided background information and then
make a decision regarding whether to utilize tools. Upon receiving feedback from the tools,
the LLMs are expected to identify supporting evidence in the results or potentially make
further tool requests. The LLMs are responsible for concluding the hypothesis generation
process and summarizing the hypotheses independently.
4.2

Experiment Results

Our primary focus is to investigate the impact of tool use and multi-agent collaboration
on hypothesis generation. We present the experimental results in Figure 6b. Based on the
results, we summarize our findings from the following two perspectives:
Results of Tool Use Based on our results, we observe that tool use has minimal impact
on improving the hypothesis generation ability of LLMs. This observation aligns with the
findings presented in Section 3.2.2 regarding the analysis of external knowledge. Notably,
the ReAct-based method performs slightly worse than OpenAI function calling. It is also
evident that LLMs struggle to identify useful information and exhibit weaknesses in the
thought-action-observation process, even when utilizing the official interface from OpenAI.
2 https://pubmed.ncbi.nlm.nih.gov/

9


Hypothesis generation is a demanding task where the balance between certainty and
uncertainty plays a crucial role and needs further exploration.
Results of Multi-agent Collaboration In addition to tool use, our findings suggest that the
division of labor and interaction among multi-agents can significantly enhance the model’s
capability to propose hypotheses by introducing uncertainty. This mirrors the dynamics of
real-world scientific research, where hypotheses are formulated through iterative discussions and refutations. Additionally, it is worth noting that tool use can further enhance the
performance of the multi-agent framework.

5

Conclusion

This study presents a comprehensive evaluation of large language models (LLMs) as biomedical hypothesis generators, focusing on their zero-shot generalization ability. We constructed
a novel biomedical corpus to assess the hypothesis generation capabilities of LLMs, revealing their remarkable ability to generate novel and validated hypotheses even when
tested on unseen literature. We introduced a multi-agent framework that leverages LLMs to
enhance collaborative analysis in the hypothesis generation process and developed multidimensional metrics to evaluate the quality of generated hypotheses. Our work contributes
to the growing research on the application of LLMs in scientific discovery, particularly in
the biomedical domain. Future research could explore the integration of domain-specific
knowledge, incorporation of diverse data sources, and development of user-friendly interfaces to further enhance the performance and adoption of LLMs in biomedical hypothesis
generation. Our study highlights the immense potential of LLMs as catalysts for biomedical
discovery, offering a promising avenue for accelerating the pace of scientific progress.

6

Limitations and future works

Our research reveals the potential of Large Language Models (LLMs) to generate new
hypotheses, marking a significant positive finding. However, we must acknowledge certain
limitations. Firstly, a thorough investigation is required into the impact of factual hallucinations inherent in LLMs on hypothesis formulation. Additionally, evaluating and analyzing
knowledge discovery in LLMs demands in-depth consideration from various perspectives,
necessitating further exploration.
Currently, our focus is on the hypothesis generation stage, utilizing tools such as Web search
and PubMed. Introducing more specialized tools into the knowledge discovery cycle could
prove invaluable. In future work, we plan to integrate bioinformatics analysis tools (Zhang
et al., 2024) to enhance our research efforts.
Moving forward, we intend to incorporate knowledge graphs to aid in generating higherquality hypotheses. Additionally, we will explore the inclusion of more dynamic tools, such
as multi-tool collaborations, to further improve the performance of our LLM-based models.
To significantly enhance the hypothesis generation capabilities of our models, we aim to
optimize strategies that introduce uncertainty via reinforcement learning. This approach
will help us address the limitations and unlock the full potential of LLMs in the knowledge
discovery process.

Acknowledgements
This work is supported by the National Science and Technology Major Project
(2023ZD0121403). We extend our gratitude to the anonymous reviewers for their insightful
feedback, which has greatly contributed to the improvement of this paper.
10

<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# TRAIL: Trace Reasoning and Agentic Issue Localization

- **Authors:** Deshpande, Darshan; Gangal, Varun; Mehta, Hersh; Krishnan, Jitin; Kannappan, Anand; Qian, Rebecca
- **Venue / Year:** arXiv preprint · 2025
- **DOI:** —
- **URL:** https://arxiv.org/abs/2505.08638
- **Bibkey:** Deshpande2025_250508638
- **Status:** complete

## Abstract
The increasing adoption of agentic workflows across diverse domains brings a critical need to scalably and systematically evaluate the complex traces these systems generate. Current evaluation methods depend on manual, domainspecific human analysis of lengthy workflow traces—an approach that does not scale with the growing complexity and volume of agentic outputs. Error analysis in these settings is further complicated by the interplay of external tool outputs and language model reasoning, making it more challenging than traditional software debugging. In this work, we (1) articulate the need for robust and dynamic evaluation methods for agentic workflow traces, (2) introduce a formal taxonomy of error types encountered in agentic systems, and (3) present a set of 148 large human-annotated traces (TRAIL) constructed using this taxonomy and grounded in established agentic benchmarks. To ensure ecological validity, we curate traces from both single and multi-agent systems, focusing on real-world applications such as software engineering and open-world information retrieval. Our evaluations reveal that modern long context LLMs perform poorly at trace debugging, with the best Gemini-2.5-Pro model scoring a mere 11% on TRAIL. Our dataset and code are made publicly available to support and accelerate future research in scalable evaluation for agentic workflows.

## Key passages (verbatim from the arXiv full text; tables and figures omitted)

### Benchmark overview
TRAIL is a benchmark aimed to evaluate LLM capabilities to analyze and evaluate long, structured, opentelemetry standardized agentic executions. TRAIL follows our fine grained taxonomy and contains 148 carefully annotated agentic traces. The dataset uses text-only data instances from the GAIA (Mialon et al., 2023) and SWE Bench Lite (Jimenez et al., 2024) datasets, spanning multiple information retrieval and software bug fixing tasks. It contains a total of 841 annotated errors, averaging at 5.68 errors per trace Figure 3.

### Dataset analysis (excerpt)
Following the post-annotation review, we found errors in 114 GAIA traces and 30 from SWE Bench. As shown in Figure 3, these errors cover various categories, with most falling under Output Generation. Specifically, Formatting Errors and Instruction Non-compliance make up 353 of 841 total errors—nearly 42%. In contrast, System Execution Errors are rare. This categorical imbalance highlights two important considerations for evaluating agentic pipelines. First, the prevalence of Output Generation errors suggests that current LLM systems struggle with high-level reasoning and understanding task parameters, even with careful promptengineering. Second, although infrequent, errors in categories like API failures can be catastrophic and are critical to detect, as they are often difficult to recover from, unlike errors due to goal deviation or tool misinterpretation. Most errors in our data are high or medium impact (Figure 6a). While model hallucinations and resource management issues greatly affect agent behavior, about 44% of Output Generation errors are low impact (Figure 6b). This underscores need for a classification scheme that includes rare but significant error types.

### Results (excerpt)
5.1.3 Performance vs Input Length We find all performance metrics to be anticorrelated with input length, as detailed in Table 3. This supports the hypothesis that longer input raw traces increase the difficulty of TRAIL for models. 5.1.4 Reasoning vs Non-Reasoning Models From Table 1, we see all reasoning models except o1 outperforming non-reasoning ones on both Error category F1 and Location Accuracy. On Joint Accuracy, the gap between the two families is larger — Reasoning models other than o1 perform at 1.5-8 times the best performing non-reasoning model. 5.1.5 Does Reasoning Effort Matter? To systematically assess the impact of reasoning extent, we experiment with the same model (o3) at "high," "medium," and "low" reasoning effort levels, as set by OpenAI’s reasoning.effort parameter. We find that all three metrics, including Category F1 (0.296 → 0.277 → 0.264), decrease as reasoning effort decreases.

### Conclusion
In this work, TRAIL, a new taxonomy for classifying agentic errors, along with an expert-curated dataset of 148 agentic problem instances and 841 unique errors from GAIA and SWE Bench. Current SOTA models perform poorly as LLM Judges on this dataset, with Gemini-2.5-Pro achieving only 18% joint accuracy on GAIA and 5% on SWE Bench; three out of eight models cannot even process the full context. These results highlight that existing models struggle to systematically evaluate complex agentic traces, due to the inherent complexity of agentic systems and LLM context limitations. A new framework is needed for scalable, systematic evaluation of agentic workflows.

### Limitations
The TRAIL dataset and taxonomy are primarily focused on text-only inputs and outputs but recent advancements in multimodal agentic systems require careful extension of the taxonomy to handle errors arising from new categories such as multimodal tool use. One additional limitation of TRAIL is the large number of tail categories with very few examples. It is important to ensure correctness of LLMJudges on these categories due to the high-impact nature of the failures. Future research work can look into synthetic data generation for high-impact, low-occurrence categories by systematically modifying existing traces to induce catastrophic irrecoverable failures within the LLM context.

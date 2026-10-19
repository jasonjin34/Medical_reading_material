<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# MedAgentBench: A Virtual EHR Environment to Benchmark Medical LLM Agents

- **Authors:** Jiang, Yixing; Black, Kameron C.; Geng, Gloria; Park, Danny; Zou, James; Ng, Andrew Y.; Chen, Jonathan H.
- **Venue / Year:** NEJM AI · 2025 (vol. 2, no. 9; published 2025-08-28)
- **DOI:** 10.1056/AIdbp2500144
- **URL:** https://doi.org/10.1056/AIdbp2500144
- **Open preprint used for this extract:** arXiv 2501.14654v2 (2025-02-12), "MedAgentBench: A Realistic Virtual EHR Environment to Benchmark Medical LLM Agents"
- **Bibkey:** Jiang_2025
- **Status:** complete (from the open preprint; the NEJM AI version could not be accessed and may differ)

## Abstract (arXiv preprint)
**Background** Recent large language models (LLMs) have demonstrated significant advancements, particularly in their ability to serve as agents thereby surpassing their traditional role as chatbots. These agents can leverage their planning and tool utilization capabilities to address tasks specified at a high level. This suggests new potential to reduce the burden of administrative tasks and address current healthcare staff shortages. However, a standardized dataset to benchmark the agent capabilities of LLMs in medical applications is currently lacking, making the evaluation of LLMs on complex tasks in interactive healthcare environments challenging.

**Methods** To address this gap to the deployment of agentic AI in healthcare, we introduce MedAgentBench, a broad evaluation suite designed to assess the agent capabilities of large language models within medical records contexts. MedAgentBench encompasses 300 patient-specific clinically-derived tasks from 10 categories written by human physicians, realistic profiles of 100 patients with over 700,000 data elements, a FHIR-compliant interactive environment, and an accompanying codebase. The environment uses the standard APIs and communication infrastructure used in modern EMR systems, so it can be easily migrated into live EMR systems.

**Results** MedAgentBench presents an unsaturated agent-oriented benchmark that current state-of-the-art LLMs exhibit some ability to succeed at. The best model (Claude 3.5 Sonnet v2) achieves a success rate of 69.67%. However, there is still substantial room for improvement which gives the community a next direction to optimize. Furthermore, there is significant variation in performance across task categories.

**Conclusion** Agent-based task frameworks and benchmarks are the necessary next step to advance the potential and capabilities for effectively improving and integrating AI systems into clinical workflows. MedAgentBench establishes this and is publicly available at https://github.com/stanfordmlgroup/MedAgentBench, offering a valuable framework for model developers to track progress and drive continuous improvements in the agent capabilities of large language models within the medical domain.

## Full text / Extract (preprint)

### Tasks
Two internal-medicine physicians submitted 300 clinically derived tasks (inpatient and outpatient) that could benefit from computer-agent automation: patient communication, information retrieval, recording patient data, test ordering, documentation, referral ordering, medication ordering, data aggregation and analysis. Tasks include MRN, timing ("over last 24 hours") and values to record, plus NDC, LOINC, base names and SNOMED codes. "Instructions" are written by clinicians; "context" (site-specific codes, formulary) is managed by EHR administrators. Example: "Check patient {MRN}'s most recent potassium level. If below threshold, order replacement potassium according to dosing instructions" with context giving the NDC and "for every 0.1 mEq/L below threshold, order 10 mEq potassium oral repletion to reach a goal of 3.5".

### Patient profiles
From the de-identified STARR (Stanford Research Repository) warehouse; timestamps jittered per patient. 100 patients randomly sampled from those with an inpatient sodium test on the morning of 2023-11-13. Five years of lab results, six vital signs (HR, SpO2, RR, FiO2, BP, temperature), procedure orders (CPT), diagnoses (ICD-10) and medication orders (PRN removed). Fake MRNs ("S" + 7 random digits); Faker-generated names, phones, addresses.

| Characteristic | Value |
|---|---|
| Unique individuals | 100 |
| Age (mean ± SD) | 58.15 ± 19.82 |
| Female | 47% |
| Records (total) | 785,207 |
| Observation | 563,426 |
| Procedure | 124,969 |
| Condition | 74,821 |
| MedicationRequest | 21,991 |

### Environment and evaluation
FHIR-compliant server on HAPI FHIR JPA (persistent H2 database), Docker image at hub.docker.com/r/jyxsu6/medagentbench, deployed on a GCP c2d-standard-2 VM; not for production (no security or enterprise logging). Codebase built on AgentBench. Orchestrator (BFCL-inspired) exposes nine FHIR functions: condition.search, lab.search, vital.search, vital.create, medicationrequest.search, medicationrequest.create, procedure.search, procedure.create, patient.search. Each round: GET, POST or finish; max 8 rounds. POSTs are checked for JSON-loadability and acknowledged (only GETs are sent to the server, to avoid ~90 s re-initialization). Graders and reference solutions are manually curated: query tasks compared to reference answers; action tasks verified by rule-based checks on POST payloads. Invalid actions or exceeding the round limit = failure. Metric: task success rate, pass@1 only. Temperature 0 except o3-mini.

### Results (preprint Table 3)
| Model | Size | Form | Overall SR | Query SR | Action SR |
|---|---|---|---|---|---|
| Claude 3.5 Sonnet v2 | N/A | API | 69.67% | 85.33% | 54.00% |
| GPT-4o | N/A | API | 64.00% | 72.00% | 56.00% |
| DeepSeek-V3 | 685B | open | 62.67% | 70.67% | 54.67% |
| Gemini-1.5 Pro | N/A | API | 62.00% | 52.67% | 71.33% |
| GPT-4o-mini | N/A | API | 56.33% | 59.33% | 53.33% |
| o3-mini | N/A | API | 51.67% | 54.67% | 48.67% |
| Qwen2.5 | 72B | open | 51.33% | 38.67% | 64.00% |
| Llama 3.3 | 70B | open | 46.33% | 50.00% | 42.67% |
| Gemini 2.0 Flash | N/A | API | 38.33% | 34.00% | 42.67% |
| Gemma2 | 27B | open | 19.33% | 38.67% | 0.00% |
| Gemini 2.0 Pro | N/A | API | 18.00% | 25.33% | 10.67% |
| Mistral v0.3 | 7B | open | 4.00% | 8.00% | 0.00% |

150 tasks are query-only (GET); 150 require POST. Most models (except Gemini 1.5 Pro and Qwen2.5) do better on query tasks. Common errors: not following instructions exactly (Gemini 2.0 Flash outputs invalid actions in 54% of cases, wrapping code in tool_code or json blocks); answering in full sentences instead of the expected bare value.

### Limitations (authors)
Does not capture multi-team coordination; Stanford-only profiles may be biased; focused on medical-record contexts (not surgery, nursing); reliability of producing the same results on repeated action tasks is future work; only a simple agent baseline.

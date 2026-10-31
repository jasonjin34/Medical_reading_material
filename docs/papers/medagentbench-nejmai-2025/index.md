# MedAgentBench: A Virtual EHR Environment to Benchmark Medical LLM Agents

> **Bibkey** `Jiang_2025` · **Venue** NEJM AI (2025) · **Category** agents · **Relevance** medium · **Access** paywall
> **Link** <https://doi.org/10.1056/AIdbp2500144> · `status: complete`

---

## One-liner
MedAgentBench (Stanford; Andrew Ng / Jonathan Chen groups) is the first benchmark requiring an LLM agent to **autonomously read and write records in a FHIR-compliant virtual EHR**: 300 verifiable clinical tasks (10 categories) written by internal-medicine physicians, over 100 patient profiles derived from de-identified real Stanford STARR cases (~785k records). In the preprint the best model, Claude 3.5 Sonnet v2, reaches **69.67%** overall success; write (action) tasks are generally harder than read (query) tasks.

## Problem
Medical QA benchmarks (MedQA, MedMCQA) are saturated, and exam-style evaluation oversimplifies real clinical interaction; general agent benchmarks (AgentBench, BFCL, tau-bench) do not cover healthcare-specific coding systems (LOINC, SNOMED, NDC, ICD-10), abbreviations and longitudinal records. Physicians spend only ~27% of their time on direct care, the rest on documentation and administration, so agents could help — but there is no standardized benchmark of agent ability in an interactive medical-record environment.

## Method
**Tasks**: two internal-medicine physicians wrote 300 common inpatient/outpatient tasks suited to computer automation, in 10 specific categories (7 broad groups): patient-information retrieval, lab-result retrieval, data aggregation (e.g. 24-h mean glucose), recording data (e.g. charting a BP), test ordering (e.g. reorder HbA1C if > 1 year old), referral ordering, medication ordering (e.g. potassium repletion by threshold-based dosing), etc. Each task combines a clinician-written "instruction" with hospital-system "context" (site-specific codes maintained by EHR admins, e.g. LOINC 4548-4, an NDC). **Patient profiles**: 100 patients randomly sampled from the de-identified STARR warehouse who had an inpatient sodium test on the morning of 2023-11-13 (sodium as anchor); five years of labs, six vital-sign types, procedures (CPT), diagnoses (ICD-10) and medication orders (PRN removed); patient-level timestamp jitter; MRNs as "S + 7 random digits", names/phones/addresses from Faker. **Environment**: a FHIR server on open-source HAPI FHIR JPA, packaged as a Docker image; any agent interacts via HTTP. **Evaluation**: built on AgentBench; a simple BFCL-inspired orchestrator exposes 9 FHIR functions (search/create on condition, lab, vital, medicationrequest, procedure, patient); each round chooses GET, POST or finish, **max 8 rounds**; to avoid restarting the environment per task (~90 s), POSTs are only checked for JSON-loadability and acknowledged, and correctness is verified by hand-written rule-based checks on the payload. Main metric: task success rate, **pass@1 only** (one wrong action matters clinically). Temperature 0 (except o3-mini).

## Data
100 patients: mean age 58.15 ± 19.82, 47% female; 785,207 records (Observation 563,426, Procedure 124,969, Condition 74,821, MedicationRequest 21,991). Half the 300 tasks (150) need only GET queries; the other half require POST modifications (usually after GETs). The environment Docker image and code are public.

## Key results
Preprint Table 3 (12 models): **Claude 3.5 Sonnet v2 overall SR 69.67%** (query 85.33%, action 54.00%); GPT-4o 64.00% (72.00% / 56.00%); DeepSeek-V3 62.67%; Gemini 1.5 Pro 62.00% (query 52.67%, action 71.33% — one of the few with action > query); GPT-4o-mini 56.33%; o3-mini 51.67%; Qwen2.5-72B 51.33% (action 64.00% > query); Llama 3.3-70B 46.33%; Gemini 2.0 Flash 38.33%; Gemma2-27B 19.33%; Gemini 2.0 Pro 18.00%; Mistral v0.3-7B 4.00%. A closed vs open-weight gap remains. **Common errors**: not following the output format exactly (Gemini 2.0 Flash emits invalid actions in 54% of cases, wrapping code in `tool_code`/json blocks); answering in full sentences instead of the required bare value (`["value": 5.4]` instead of `[5.4]`).

## Contributions
- The first medical benchmark requiring agents to **autonomously interact with (including write to)** a medical-record environment.
- Built on standard FHIR APIs, so tasks can in principle migrate to live EMRs (the authors stress the environment has no security or enterprise logging and is not for production).
- Real (de-identified, jittered) patient profiles + physician-written tasks + rule-based verifiable graders.
- Separates query SR from action SR and insists on pass@1.

## Limitations
- Short tasks (≤ 8 rounds), mostly atomic single-patient operations; no multi-team coordination or long-horizon clinical reasoning.
- All patients from Stanford, limiting representativeness; record-centric only, no surgery or nursing.
- POSTs are not actually applied (just acknowledged), so agents never see consequences of writes and write-then-read consistency is untested.
- Only a simple orchestrator baseline; **rerun consistency is untested** — the authors list reliability under repetition of action tasks as future work.
- This note is based on the preprint; published numbers may differ.

## Relation to our direction
This is the representative paper on the EHR line. For the **Sinai EHR / patient-trajectory project**: (1) its FHIR environment plus patient-sampling recipe (anchor on a common lab, extract five years of longitudinal data, jitter time, synthesize identifiers) is a ready template for a "virtual EHR sandbox" on Mount Sinai de-identified data; (2) its tasks are almost all single-timepoint atomic operations with **no trajectory-level reasoning** (trends, event sequences, prognosis) — exactly the dimension the trajectory project can add, e.g. "does the 12-month eGFR slope indicate CKD progression; if so, place a nephrology referral". For **cardiometabolic-kidney agents / foundation models** in general: it already has metabolic/electrolyte tasks (HbA1C reorder, potassium repletion), so extending to kidney-relevant action tasks — eGFR, UACR, potassium vs ACEi/ARB interplay — is natural, and potassium repletion is itself a renal-function-dependent high-risk order. For **the agent-trustworthiness topic**: it insists on pass@1 and admits rerun reliability is untested, leaving a clear slot for rerun stability; its rule-based payload checks are a structured form of claim/action-to-evidence verification — the agent claims "repleted potassium per threshold", and the checker verifies the dose actually follows from the lab value.

## Reusable assets
- **Code:** the MedAgentBench evaluation framework (built on AgentBench).
<https://github.com/stanfordmlgroup/MedAgentBench>
- **Environment:** FHIR server Docker image (HAPI FHIR JPA + 100 patient profiles).
<https://hub.docker.com/r/jyxsu6/medagentbench>
- **Preprint:** arXiv 2501.14654 (open full text).
<https://arxiv.org/abs/2501.14654>

## Follow-ups
- Obtain the NEJM AI version and check whether models and success rates were updated.
- AgentClinic, CRAFT-MD and tau-bench as comparators for clinical / tool-interaction agent evaluation.
- Whether follow-ups add rerun reliability for action tasks and longitudinal (trajectory-level) tasks.

## Cite
```bibtex
@article{Jiang_2025, title={MedAgentBench: A Virtual EHR Environment to Benchmark Medical LLM Agents}, volume={2}, ISSN={2836-9386}, url={http://dx.doi.org/10.1056/AIdbp2500144}, DOI={10.1056/aidbp2500144}, number={9}, journal={NEJM AI}, publisher={Massachusetts Medical Society}, author={Jiang, Yixing and Black, Kameron C. and Geng, Gloria and Park, Danny and Zou, James and Ng, Andrew Y. and Chen, Jonathan H.}, year={2025}, month=Aug }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

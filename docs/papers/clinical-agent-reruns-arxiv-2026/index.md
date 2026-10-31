# Same Patient, Different Order: Action-Level Reliability of Clinical LLM Agents Under Repeated Runs

> **Bibkey** `clinical-agent-reruns-arxiv-2026` · **Venue** arXiv preprint (2026) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2609.13582> · `status: complete`

---

## One-liner
The authors propose a "same-input rerun" protocol: replay each MedAgentBench task five times with patient and all inputs fixed, and compare not the score but the **orders** (FHIR write requests) the agent actually issues. Action-level divergence is pervasive and often invisible to the benchmark's verdict: for Llama-3.1-8B at temperature 0.7, all 43 ordering groups emit a different order set across five identical runs, yet in 22 of them the benchmark reports the same verdict.

## Problem
Clinical agents now order tests, prescribe and refer, yet benchmarks usually run each task once and report accuracy, rarely asking whether identical inputs produce identical actions. Accuracy records whether the agent was right, not whether it was **consistent**. Three difficulties: (i) deciding when two orders are the same order (timestamps, status fields, parameter order vary without the order varying); (ii) MedAgentBench never executes writes — it JSON-parses the payload and replies "success" — so within a run one cannot tell an order the server would create from one it would refuse; (iii) making a rate measured over five reruns meaningful outside the study (budget, denominators, non-independence).

## Method
**Same-input rerun**: for a fixed task, model and decoding configuration, run the benchmark's agent loop five times and compare at three layers — action (orders), trajectory, verdict. **Six metrics**: (1) **order-set divergence**: canonical form = destination endpoint + whole payload; a group diverges if its five runs yield >1 distinct order set (no order = empty set); also reported as budget-independent **pairwise disagreement** (share of run pairs whose order sets differ); (2) **omission split**: some runs order, some do not (the most silent failure); (3) **endpoint divergence**: ordering runs reach different endpoints; (4) **clinical-content divergence**: compares clinical fields — resource code and text, recorded value, medication code and text, dose value/unit/rate/route (excluding timestamps, status and the human-readable code label); (5) **trajectory first-divergence**: the first turn where runs differ; (6) **verdict instability**: whether the benchmark's own pass/fail changes across the five runs. Action metrics are computed over ordering groups (groups that order at least once). Statistics: Wilson 95% intervals; exact paired McNemar between temperatures (Holm-corrected); family-level cluster bootstrap. **Controls**: a noise floor (20 identical calls × 18 cells), and testing endpoint divergence against the benchmark's own HAPI FHIR server.

## Data
MedAgentBench (300 clinical tasks, 10 families, a FHIR server with ~100 de-identified patients); the five write-capable families (record an observation, place a service request, three families conditional on a lab value or its age), taking the first 10 tasks per family by the benchmark's own ID order — 50 task groups. Two locally served, 4-bit-quantised open-weight models, Qwen3-4B and Llama-3.1-8B; temperatures 0.05 (near-greedy) and 0.7 (nucleus); five runs per task → 250 runs per arm, 1,000 total (1,250 records including an 8-bit Qwen rerun). Round limit 8, original scaffold.

## Key results

- **Action divergence appears in every arm and rises with temperature**: order-set divergence — Qwen 0.05: 3/20, Qwen 0.7: 10/20, Llama 0.05: 11/21, Llama 0.7: **43/43**; pairwise form 0.08 → 0.29 (Qwen), 0.33 → 0.78 (Llama). Omission split: 0/20, 4/20, 1/21, 26/43. Endpoint divergence: 3/20, 8/20, 8/21, 12/43.
- **Clinical-content divergence**: only in the Llama 0.7 arm, but in 28/43 groups — 23 differ on resource code, 18 on recorded value, 5 on medication, 3 on dose (overlapping); no routing or parsing account explains this. The 8-bit Qwen rerun also shows content divergence, complicating a pure-quantisation explanation.
- **Orders move, verdict holds**: in Llama 0.7, 22 of 43 divergent groups keep the same verdict (spanning all five write families); 3/11 at Llama 0.05; 10/10 at Qwen 0.7. Of 38 such groups, 36 fail on all five runs — the score hides not success but that the agent failed differently each time. None of the 251 passing runs posted to an endpoint the server would refuse.
- **Endpoints are not cosmetic**: the same ServiceRequest payload sent to `/fhir/ServiceRequest` returns 201 Created; sent to the collection root `/fhir/` it returns 400 Bad Request (HAPI-0450) — one places the order, the other does not; yet the agent is always told "success".
- **Mechanisms**: misrouting, and lost orders after a malformed payload whose retry repeats the same construction; of 72 non-emitting runs in Llama's 26 split groups, 61 ended with the agent declaring itself finished, 7 on a malformed action, 4 at the round limit. Divergence is immediate: median first-divergence turn is 0 in three of four arms.
- **Statistics**: McNemar finds the temperature rise significant for both models on trajectory, order-set and verdict divergence (96 of 100 discordant pairs toward more divergence; all six survive Holm), but under family clustering only the Llama 0.7 arm holds. The authors are explicit: the study **establishes that action divergence exists and can pass unrecorded by the score, not that any rate generalises**.
- **Noise floor**: serial greedy decoding is exactly reproducible; on a shared server with concurrent traffic, temperature-0 determinism breaks (4 of 12 greedy cells return more than one completion).

## Contributions
- **Changes the evaluation unit from one attempt to a group of identical reruns**, with ordering groups as the denominator for action-level rates.
- **A measurement layer beneath the verdict**: six metrics computable from transcripts benchmarks already keep, with a budget-independent pairwise form.
- **Leaves the benchmark loop to test against the real server**, showing endpoint divergence decides whether an order is created and exposing unfaithful environment feedback.
- Three independently adoptable design recommendations: R1 rerun and say so; R2 report an action-level stability measure; R3 make the environment answer as the real system would.

## Limitations
- Measures orders emitted, not received; makes no claim that clinical agents are unsafe to deploy.
- Tiny panel: two <10B 4-bit open models, one benchmark, one serving stack; not frontier; shows inconsistent failure, not inconsistent success.
- Uses MedAgentBench's original scaffold (v2 removes hand-built HTTP requests, the mechanism behind many failures); tasks are a prefix, not a random sample.
- Task groups cluster by family and most significance vanishes under clustering; the protocol transfers, the rates do not.

## Relation to our direction
Essentially a ready-made methodology for **the agent-trustworthiness topic's "rerun stability" component**, with the domain switched from kidney omics to EHR write actions. Directly reusable: **(1) Protocol**: rerun identical inputs N times, treat the task group as the unit, compare actions not scores. For a kidney-omics agent, "actions" can be its chosen analysis steps and parameters (QC thresholds, normalisation, clustering resolution, DE test), the genes/cell states it nominates, and its conclusions; **(2) Metric templates**: order-set divergence ↔ divergence in the conclusion set; omission split ↔ a rerun silently missing a key finding; endpoint divergence ↔ taking a different analysis branch; clinical-content divergence ↔ same conclusion but different genes/effect sizes; the pairwise form keeps studies comparable; **(3) "verdict holds while behaviour moves"** directly supports the agent-trustworthiness topic's argument that benchmark accuracy alone hides instability; **(4) R3 "faithful environment feedback"** maps to another the agent-trustworthiness topic concern — whether a tool call's "success" is real (silent failures in omics tools). For the **Sinai EHR / patient-trajectory project** and cardiometabolic-kidney agents in general, it is a direct reference for evaluating clinical write-action stability in FHIR environments, and evidence on the risks of locally deployed, quantised small models in privacy-constrained settings. Highly relevant to AIRIS WP3 / MLCommons-style benchmark specification work (reporting standards, rerun counts, denominator definitions).

## Reusable assets
- **Code, rerun harness, analysis scripts, environment reproduction script and all 1,250 run records:**
<https://github.com/rohithreddybc/clinical-agent-action-reliability>
- **Anonymised read-only mirror:**
<https://anonymous.4open.science/r/clinical-agent-action-reliability>
- **Metric definitions** (Section 4) and statistics (Wilson intervals, paired McNemar + Holm, family cluster bootstrap).
- **Benchmark environment:** MedAgentBench (this repo: `medagentbench-nejmai-2025`).

## Follow-ups
- MedAgentBench v2 (Chen et al., 2026) — does action stability improve under the new scaffold?
- Mokssit et al. (2026) — a clinical sandbox executing writes against a resettable server.
- τ-bench's pass^k and its clinical use (Liu et al., 2026); Atil et al. (2024) and Yuan et al. (2025) on nondeterminism under "deterministic" decoding.

## Cite
```bibtex
@misc{clinical-agent-reruns-arxiv-2026, title={Same Patient, Different Order: Action-Level Reliability of Clinical LLM Agents Under Repeated Runs}, author={Bellibatlu, Rohith Reddy and Singh, Manpreet and Han, Zhoutian and Zhang, Wenbin}, year={2026}, eprint={2609.13582}, archivePrefix={arXiv}, primaryClass={cs.CL}, url={https://arxiv.org/abs/2609.13582}, doi={10.48550/arXiv.2609.13582} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

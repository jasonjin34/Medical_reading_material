# SciTrace: Trajectory-Aware Safety Reasoning for Scientific Discovery Agents

> **Bibkey** `Swaminathan2026_260608234` · **Venue** arXiv preprint (2026) · **Category** agents · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2606.08234> · `status: complete`

---

## One-liner
SciTrace (CMU) weaves safety reasoning into every stage of an AI-scientist pipeline: a **Safety-Intrinsic Reasoning Loop (SIR)** maintains and propagates a **cumulative risk state** across the Thinker → Experimenter → Writer → Reviewer stages, and a **Compositional Tool-Chain Verifier (CTV)** checks each tool call against the full call history to ask whether a sequence of individually benign steps adds up to something dangerous. On SciSafetyBench it raises tool-call safety by 14.3 points on average over SafeScientist and catches 78.8% of the compositional risks that single-step monitors miss.

## Problem
Safety layers in current AI scientists are **structurally divorced** from core reasoning: they inspect outputs rather than shaping the deliberation that produces them. Two failure modes follow: (1) **risk signals are stage-local** — SafeScientist's four defence layers act independently, so a dual-use warning raised by the Thinker-stage prompt monitor is written to a local buffer and never reaches the Experimenter or Writer; (2) **single-step monitors miss compositional risk** — e.g. "retrieve a pathogen genome" → "query antibiotic-resistance databases" → "request protein-structure prediction" each pass individually, yet the trajectory points at dual-use research.

## Method
Two components are layered onto the SafeScientist pipeline and share one **cumulative risk state** (SafeScientist's original filters remain only as fallback). **Risk levels**: five graded levels instead of binary — SAFE, LOW-RISK, WARNING, HIGH-RISK, BLOCK; the overall level is the max over signals, with **interaction escalation** by one step when certain category pairs co-occur (e.g. dual-use + hazardous synthesis). **SIR**: at each stage a structured template supplies the stage's task content, the cumulative risk state and safety checks retrieved from a safety memory (following AGrail, k-nearest by keyword overlap); the LLM returns a risk level, a description and an action (proceed / modify / flag / block); prompts are stage-specific (dual-use at Thinker, tool and protocol safety at Experimenter, information disclosure at Writer, a full-visibility ethical review at Reviewer). **CTV**: a verified tool proxy intercepts every call and, in one LLM pass, scores request harmfulness, **compositional risk of this call given the full history**, and tool-invocation safety (adapted from ToolSafe's TS-Guard, replacing attack correlation with compositional risk); the combined score maps to allow / modify / block, and on modify/block a second LLM call (TS-Flow) proposes a **safe alternative** (e.g. substituting non-pathogenic M. smegmatis for M. tuberculosis) rather than a hard stop. The risk taxonomy has nine categories (S1 hazardous synthesis … S9 compositional danger). SIR and CTV use the same backbone as the primary agent.

## Data
SciSafetyBench (from SafeScientist): 240 high-risk research tasks + 120 tool-related risk tasks with 30 specialized scientific tools, evenly spread over physics, chemistry, biology, materials, information science and medicine (40 + 20 per domain), labelled equally by four risk types (intentional malice, concealed harm, unintentional consequences, multi-step tool trajectories). Backbones: Llama-3.1-70B-Instruct, Qwen2.5-72B-Instruct, DeepSeek-V3 (local vLLM, 4-bit AWQ, two RTX A5000s) and GPT-4o (API). Metrics follow SafeScientist: Safety Score (1–5, GPT-4o judge), reject rate, tool-call safety rate, Quality/Clarity/Overall (1–5), plus compositional-risk detection rate.

## Key results
**Main table** (Bare LLM / SafeScientist / SciTrace, tool-call safety rate): Llama-3.1-70B 38.5 / 76.3 / 91.2%; Qwen2.5-72B 40.2 / 78.1 / 92.5%; DeepSeek-V3 42.0 / 79.5 / 93.8%; GPT-4o 45.5 / 81.2 / 94.7% — +14.3 pp on average; reject rates 92–95% across backbones (SafeScientist 85–90%); Safety Score 4.87–4.93; quality metrics rise slightly too (e.g. Qwen2.5-72B Overall 3.50 → 3.72). AI Scientist, CycleResearcher, ResearchTown, AI Co-Scientist and Agent Laboratory reject only 0–22%. **Ablation** (Qwen2.5-72B): SIR alone +0.06 Safety and +2.5 pp reject rate; CTV alone +11.6 pp tool safety; both together best. **By domain**: biology (+17.3 pp) and chemistry (+17.2 pp) gain most, physics least (+10.7 pp); information science has the lowest absolute rate (86.6%). **Compositional risk**: of 80 tasks where SafeScientist approved every single call but the trajectory was judged unsafe, CTV catches 63 (78.8%) — 81–83% in biology, chemistry, medicine and materials, 77.8% in physics, only 64.3% in information science (data-exfiltration patterns differ structurally from the physical-synthesis trajectories CTV targets). **Refusal analysis**: direct refusals rise only 5.9 pp; gains come from safe redirections (+12.2 pp) and safe completions (+19.2 pp). **Adversarial**: discussion-attack defence 39.1% → 65.2% (+26.1 pp); average attack rejection Llama 48.3 → 73.6%, GPT-4o 55.6 → 79.7%, largest against malicious discussion agents (+37.3 / +35.5 pp). **Cost**: 36.9–43.8% added latency per pipeline run.

## Contributions
- Turns safety from stage-local filters into a **cumulative state propagated across stages**, with graded levels and combination escalation.
- **Trajectory-level** tool verification: judging "this step plus all prior steps" rather than one step.
- Corrective feedback with safe alternatives, improving safety without visibly sacrificing research-output quality.

## Limitations
- **Evaluation leans heavily on GPT-4o as judge**: informal validation on 60 tasks gives Pearson r with human labels of ~0.62 (physics/materials) vs ~0.81 (biology/chemistry); no domain-expert agreement study or cross-judge robustness check yet (acknowledged).
- Evaluated on a single benchmark (SciSafetyBench) on top of SafeScientist; "compositional escapes" are themselves defined by GPT-4o judgements, a circular dependence on the judge.
- Safety memory retrieves by keyword overlap and misses semantically similar but lexically different risks; S9 compositional danger is tuned to physical synthesis and detects data-privacy trajectories poorly.
- ~37–44% added latency; local backbones use 4-bit quantization, which may affect comparability with original results.
- Main-table numbers are very regular across four backbones, while run-to-run variance is not in the main text (CIs are in the appendix).

## Relation to our direction
The topic is **safety** (dual use, hazardous synthesis), not Topic 2's **correctness** (is a claim supported by evidence), but its **architectural ideas transfer directly to Topic 2's claim-to-evidence verifier**. (1) **Cumulative state across stages** ↔ in omics analysis, problems found at QC (e.g. high ambient RNA in a batch, poor Xenium registration on a section) are often "forgotten" downstream in DE and pathway analysis while the final claim still rests on those samples; a cumulative *credibility* state (instead of risk state) carried through QC → clustering → annotation → DE → conclusion, with the verifier checking whether a claim depends on flagged data, is the agent-level counterpart of Topic 1's "cross-modal agreement separates artifacts from disease". (2) **Compositional checking** ↔ the classic omics case where every step looks reasonable but the combination is wrong: batch-correcting with disease status as a covariate and then running disease DE on the corrected data (double-dipping); CTV-style "judge this step against the full history" is the right form to catch it. (3) **Five graded levels + redirection instead of refusal** ↔ a verifier should output graded verdicts (supported / weakly supported / unsupported / contradicted) and suggest "what further analysis would support this claim", not just right/wrong. (4) **Cautionary example**: the whole evaluation is GPT-4o-judged with only r ≈ 0.62–0.81 against humans — precisely why Topic 2 needs a **calibrated verifier validated against expert labels**, not another unvalidated LLM judge (cf. ABC's O.c.1). Relation to Topic 1 is distant.

## Reusable assets
- **Project website:** no code repository link found in the paper body.
<https://opensciagent.github.io/SciTrace/>
- **Design patterns:** five graded levels with combination escalation; the SIR three-input template; CTV three-dimension scoring + TS-Flow corrective feedback — adaptable into "cumulative credibility state + trajectory-level claim checking".
- **Benchmark:** SciSafetyBench (from SafeScientist), including medicine and biology tasks.

## Follow-ups
- SafeScientist (Zhu et al., 2025) and the SciSafetyBench paper.
- ToolSafe (TS-Guard / TS-Flow) and AGrail — the direct sources of CTV and SIR.
- Appendices A (scoring function and thresholds), D (sensitivity) and H (bootstrap CIs).

## Cite
```bibtex
@misc{Swaminathan2026_260608234,
  title = {SciTrace: Trajectory-Aware Safety Reasoning for Scientific Discovery Agents},
  author = {Tanush Swaminathan and Runmin Jiang and Letian Zhang and Min Xu},
  year = {2026},
  eprint = {2606.08234},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2606.08234}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

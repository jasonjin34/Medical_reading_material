# Evaluating Agentic Bioinformatics through Function, Evidence, and Validation

> **Bibkey** `fev-bioinformatics-agents-arxiv-2026` · **Venue** arXiv preprint (2026) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2607.27556> · `status: complete`

---

## One-liner
This review takes the inspectable workflow trajectory — not architecture or the final answer — as the unit of analysis and introduces the Function–Evidence–Validation (FEV) framework: Function records the workflow operations an agent demonstrably performs (F1–F6), Evidence the traceable sources supporting actions and claims (E1–E6), and Validation the cumulative assurance reached for a specific use case (V0–V4 plus seven qualifiers). Coding 109 bioinformatics agent/agent-adjacent systems and 28 benchmarks, it finds planning and tool execution advancing fast while replayability, provenance, external and prospective empirical validation lag (most systems at V3, only seven at V4).

## Problem
LLM agents now plan, execute and interpret biological analyses, but fluent answers, successful tool calls and benchmark scores do not establish scientific credibility: a system may run an inappropriate analysis, retrieve authoritative but irrelevant evidence, preserve a replayable computation that supports an unjustified interpretation, or experimentally test only part of its principal claim. Prior reviews organise biological agents by application, architecture and capability and mention evidence, reproducibility, robustness and validation, but **no common framework operationalises them jointly at the level of an individual evaluated workflow**. The authors argue for moving from final-answer correctness to workflow correctness.

## Method
**Definitions**: distinguishes a bioinformatics copilot (assists user-led analysis), a workflow engine (e.g. Nextflow/nf-core — executes predefined pipelines and can correctly run an inappropriate one) and an agentic bioinformatics layer (adaptive workflow control). A full agentic layer needs goal-directed revisable multistep planning, stateful tool-mediated execution, and inspectable scientific support (evidence, traces, verification or escalation records); partial systems are agent-adjacent. **Three FEV dimensions** (complementary, non-interchangeable): **Function** (descriptive, non-ordinal): F1 planning & decomposition, F2 role specialisation & coordination, F3 tool selection & execution, F4 workflow-state maintenance & trace capture, F5 self-evaluation & repair, F6 verification & escalation (a critic counts only if it changes the output). **Evidence** (non-ordinal): E1 literature, E2 structured biological knowledge, E3 biological measurements & metadata, E4 software & statistical outputs, E5 scientific-model outputs, E6 experimental or clinical observations, each with traceability requirements and limitations (Table S4). **Validation** (cumulative gates, per use case not per platform): V0 illustrative output → V1 demonstrated execution → V2 replayable computation (inputs, parameters, dependencies, intermediate artefacts and traces sufficient to reconstruct) → V3 scientifically evaluated computation (V2 plus task-appropriate scientific checks) → V4 prospective empirical evaluation (prospective test of an agent-generated output aligned with the principal claim). Qualifiers: B benchmark/baseline, H protocol-based expert assessment, S statistics/uncertainty, R robustness/failure analysis, X external/independent validation, P prospective testing, C closed-loop empirical refinement. Key rules: qualifiers cannot override unmet stages — no V3 from benchmarks or experts without V2 replayability; published experimental data used as input is E6, not V4.

## Data
A structured evidence map: 109 agentic or agent-adjacent system entries + 28 benchmark/evaluation resources, with 9 publications in both, totalling 128 unique publications; spanning genomics & gene editing, single-cell & spatial omics, proteomics & protein design, drug discovery, computational pathology & imaging, and general bioinformatics automation. Searches covered PubMed, Google Scholar, Semantic Scholar, arXiv, bioRxiv, medRxiv and major publisher platforms, primarily January 2022 – July 2026, including preprints, with backward/forward citation tracing. Per-system FEV coding is in Supplementary Tables S1–S28 and benchmark profiles in S29–S33. Unreported or insufficiently documented capabilities are not coded.

## Key results

- **Overall landscape**: planning, tool execution, workflow-state maintenance and self-evaluation/repair are widespread; role specialisation and explicit verification/escalation (F6) are less common. Evidence is dominated by software outputs, structured knowledge and retrospective biological data; experimental/clinical observations (E6) are the least frequent category.
- **Validation stages**: most systems are V3, **only seven reach V4, none are V0**; benchmark comparison (B) and robustness analysis (R) dominate the qualifiers, while prospective testing (P) and closed-loop refinement (C) are exceptional — closed-loop empirical refinement appears in **a single** mapped framework.
- **Domain differences**: tool execution and trace capture are prominent in pathology, drug discovery and general workflows but less consistently reported in genomics; explicit verification/escalation is uncommon in genomics, protein engineering and single-cell/spatial; external evaluation concentrates in single-cell, spatial and pathology systems; prospective testing concentrates in protein engineering.
- **Breadth ≠ assurance**: most systems implement multiple Function and Evidence dimensions yet remain at V3; more agents, tools, databases or memory modules expand a workflow without establishing replayability, verification or empirical support for the principal claim.
- **Largest gaps** (1 − within-domain reporting share): prospective empirical testing and closed-loop refinement; verification/escalation, expert assessment, uncertainty analysis and external validation are unevenly reported.
- **Example codings** (supplement): CellVoyager V3 [B,H,R,X], "no prospective wet-lab testing reported"; SpatialAgent V3 [B,H,R,X], "prospective wet-lab validation is not established"; Biomni V3 [B,R]; OmicsNavigator (auditable spatial-omics hypothesis validation) V3 [B,H,S,R,X], evaluated on **kidney** and lung CODEX/IMC datasets.
- **Benchmark recommendations**: three complementary families — outcome-oriented, process-oriented, domain-calibrated; a correct endpoint should not get full credit when required tools were not invoked, evidence was fabricated or the workflow cannot be replayed; benchmark reports should state which claims their results **cannot** support.

## Contributions
- **Workflow trajectory as the unit of analysis**, with agentic bioinformatics defined as an adaptive workflow-control layer (distinct from copilots and workflow engines).
- **FEV separation**: operational breadth, evidence traceability and scientific assurance are not substitutes; Validation is expressed as cumulative gates plus non-ordinal qualifiers.
- **"Replayability gate" and "evidence–testing distinction"**: no V3 without replayability; using experimental data ≠ prospective testing.
- A cross-domain structured evidence map of 128 publications and a workflow-correctness agenda (including a minimum reporting standard).

## Limitations
- Coding depends entirely on what papers report: unreported means uncoded, and proportions describe the review sample rather than the whole literature and are shaped by reporting habits.
- A structured review with documented methods (databases, search terms, eligibility criteria) but not a PRISMA-style systematic review; no inter-coder agreement check is reported.
- V-stages are use-case-specific — the same system may sit at different stages across tasks — so cross-system comparison needs care; the authors explicitly do not rank.
- A review/framework paper: FEV itself is not empirically tested on real workflow evaluations (e.g. whether FEV grades predict downstream reliability).

## Relation to our direction
The best citation for **Plan B's conceptual-framework chapter**: it states in bioinformatics language what Plan B sets out to do — move from "is the answer right" to "is the workflow right" — and puts claim-to-evidence (Evidence traceability), rerun stability (V2 replayability), calibrated verification (qualifiers S/H/X) and failure analysis (R) into one structure. Concretely: **(1) a target grade for Plan B's evaluation**: agents analysing kidney omics (snRNA/snATAC/Xenium) should at minimum reach V2 (replayable: data accessions, metadata assumptions, parameters, versions, intermediate artefacts, traces), then V3 with S (uncertainty/calibration) and X (independent validation on external data such as KPMP/Lake); **(2) Table S4's limitations for E3 "biological measurements & metadata"** — noise, confounding, batch effects, missing metadata — are exactly what Plan A's "cross-modal agreement separates artefacts from disease" addresses: Plan A outputs can serve as **reliability annotations for E3 evidence** in Plan B; **(3) the revert step of detect → model → revert** corresponds to V4 and P/C: the lab's wet-lab capacity means our system could reach the rare V4 [P], even C (wet-lab results fed back to change the next round of nominations) — a closed loop only one framework in the whole map achieves; **(4)** the review notes single-cell/spatial systems (CellVoyager, SpatialAgent) generally lack explicit verification/escalation (F6) and prospective testing — precisely the niche KidneyAnomalyBench + a Plan B verifier can fill. OmicsNavigator, evaluated on kidney CODEX/IMC data, is worth following up as the closest existing system.

## Reusable assets
- **FEV coding scheme**: Function Table S3, Evidence Table S4, Validation Table S5 and qualifier definitions — usable directly as a coding manual for Plan B evaluations or papers.
- **Per-system coding tables** (Supplementary S1–S28) and benchmark profiles (S29–S33); benchmark task-type Table S6 (workflow construction, tool execution, debugging/repair, evidence-grounded interpretation, reproducibility challenge, validation & robustness).
- **Minimum reporting standard**: workflow scope, models and tools, data and evidence sources, parameters and environments, intermediate artefacts, failures and repairs, approval points, reported V-stage and its support.
<https://arxiv.org/abs/2607.27556>

## Follow-ups
- OmicsNavigator — auditable spatial-omics hypothesis validation evaluated on kidney/lung CODEX/IMC.
- The seven V4 systems and the single closed-loop (C) framework in the map — how do they feed wet-lab results back to the agent?
- Comparator reviews: Zhou et al., Yang et al., Qi et al., Dip et al., Branda et al. (Table S2).

## Cite
```bibtex
@misc{fev-bioinformatics-agents-arxiv-2026, title={Evaluating Agentic Bioinformatics through Function, Evidence, and Validation}, author={Pham, Phuc and Hy, Truong-Son}, year={2026}, eprint={2607.27556}, archivePrefix={arXiv}, primaryClass={cs.AI}, url={https://arxiv.org/abs/2607.27556}, doi={10.48550/arXiv.2607.27556} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

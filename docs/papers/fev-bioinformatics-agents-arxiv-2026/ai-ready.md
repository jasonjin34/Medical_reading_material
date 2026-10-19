<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# Evaluating Agentic Bioinformatics through Function, Evidence, and Validation

- **Authors:** Pham, Phuc; Hy, Truong-Son
- **Venue / Year:** arXiv preprint · 2026
- **DOI:** 10.48550/arXiv.2607.27556
- **URL:** https://arxiv.org/abs/2607.27556
- **Bibkey:** fev-bioinformatics-agents-arxiv-2026
- **Status:** complete

## Abstract
Large language model agents increasingly plan, execute, and interpret biological analyses, yet fluent responses, successful tool calls, and benchmark performance alone do not establish scientific credibility. Existing reviews primarily organize biological agents by application, architecture, and agentic capability, but do not jointly operationalize the accountability of agent-generated workflows. We address this gap by treating the inspectable workflow trajectory, rather than architecture or final output alone, as the primary unit of analysis. We introduce the Function--Evidence--Validation (FEV) framework, which separates demonstrated workflow operations, traceable support for actions and claims, and use-case-specific validation. Using FEV, we map 109 agentic or agent-adjacent systems and 28 benchmark or evaluation resources, representing 128 unique publications across genomics, single-cell and spatial omics, protein science, drug discovery, computational pathology, and general bioinformatics automation. Across domains, planning and tool-mediated execution have advanced more rapidly than replayability, provenance, robust scientific assessment, external validation, and prospective empirical testing. We therefore argue that agentic bioinformatics should be assessed through workflow correctness rather than final-answer correctness alone. FEV provides a practical basis for comparing systems and designing transparent, auditable, and scientifically accountable bioinformatics workflows.

## Full text / Extract
<!-- Verbatim key passages (method, results, limitations) extracted from the open-access arXiv full text. Tables, figures and inline math symbols were dropped during extraction; see the deep-read for the numbers. -->

Introduction Motivation, Definition, and Contributions Bioinformatics increasingly relies on interdependent workflows linking biological questions to data acquisition, quality control, preprocessing, statistical analysis, visualization, and interpretation. Reliable automation therefore requires more than successful software execution. It also depends on appropriate data and metadata, defensible analytical assumptions, preserved parameters and intermediate artifacts, and conclusions supported by traceable evidence (21; 34; 129).

Large language models (LLMs) provide natural-language interfaces for literature retrieval, code generation, database interaction, and scientific interpretation (157; 172; 141). Agentic systems extend these capabilities through multistep planning, tool-mediated execution, workflow-state management, critique, repair, and adaptive decision-making. Recent systems span multiomics analysis, single-cell workflows, protein design, and experimentally evaluated biomolecular discovery (173; 148; 37; 123). We use agentic bioinformatics to describe systems that adaptively coordinate data, evidence, models, tools, and analytical actions across a biological workflow.

Operational capability, however, does not establish scientific reliability.

A system may execute an inappropriate analysis, retrieve authoritative but irrelevant evidence, preserve a replayable computation supporting an unjustified interpretation, or experimentally test only a restricted part of its principal claim. Scientific credibility therefore depends on the inspectable workflow trajectory: the objective, data and metadata, analytical decisions, tools and parameters, intermediate artifacts, failures and repairs, supporting evidence, and evaluation procedures connecting a biological question to its reported conclusion (69; 171; 108).

This motivates a shift from final-answer correctness to workflow correctness.

The central question is not simply whether an agent produces a plausible or benchmark-matching answer, but whether the process supporting that answer is appropriate, executable, traceable, replayable, and scientifically defensible.

Recent reviews have organized biological agents by application domain, architecture, agent capability, interaction mode, evaluation strategy, and resource integration (171; 157; 108; 28; 10). They have also identified evidence grounding, reproducibility, robustness, and validation as important concerns.

The remaining gap is therefore not the absence of these topics, but the lack of a common framework that jointly operationalizes them at the level of individual evaluated workflows.

Architecture, tool access, or final performance alone cannot determine what operations a system performed, what evidence supported its actions and claims, or what assurance its evaluation established. Systems with similar architectures may provide substantially different forms of assurance, whereas systems with different architectures may expose comparable workflow traces, evidence records, and validation procedures. We therefore treat the inspectable workflow trajectory, rather than the architecture or final answer alone, as the primary unit of analysis. Table S2 places this perspective relative to recent reviews.

To address this gap, we introduce the Function–Evidence–Validation (FEV) framework as an accountability-oriented complement to existing application and architectural taxonomies. Rather than asking only what an agent contains or which task it completes, FEV asks what the reported workflow demonstrates and what scientific conclusions that the workflow can support.

Function records the workflow operations that a system demonstrably performs, including planning, coordination, tool-mediated execution, workflowstate and trace maintenance, repair, and verification or escalation.

Evidence records traceable literature, structured biological knowledge, biological measurements and metadata, software and statistical outputs, scientific-model outputs, and experimental or clinical observations supporting workflow actions and claims.

Validation records the assurance established for the evaluated workflow and its claims. These dimensions are complementary but non-interchangeable.

Broader Function does not imply stronger Evidence, and access to stronger Evidence does not establish deeper Validation. For example, a published experimental observation used by a workflow contributes to its Evidence profile, whereas prospective testing of a workflow-generated output contributes to Validation. Similarly, benchmark performance does not establish replayability without identifiable inputs, parameters, dependencies, intermediate artifacts, and execution traces. A complete FEV description combines a Function profile, an Evidence profile, and a use-case-specific reported Validation stage. Function and Evidence describe different workflow properties rather than ordinal levels of maturity. Validation comprises five cumulative assurance stages: illustrative output (V0), demonstrated execution (V1), replayable computation (V2),

scientifically evaluated computation (V3), and prospective empirical evaluation (V4). Each stage applies to a specific evaluated use case rather than an entire platform. Separate qualifiers preserve the reported forms of assessment:

benchmark or baseline comparison, protocol-based human or expert assessment, statistical or uncertainty analysis, robustness or failure analysis, external or independent validation, prospective empirical testing, and closed-loop empirical refinement. The stage and qualifiers reported should therefore be interpreted together with the corresponding Function and Evidence profiles. Using FEV, we construct a structured cross-domain evidence map comprising 109 agentic or agent-adjacent system entries and 28 benchmark or evaluation resources. Nine publications contribute to both categories, yielding 128 unique publications after accounting for overlap. The map spans genomics and gene editing, single-cell and spatial omics, proteomics and protein design, drug discovery, computational pathology and imaging, and general bioinformatics workflow automation. It compares the reported workflow capabilities and forms of scientific assurance rather than ranking systems, platforms, or biological fields.

Our contributions are fourfold:

We define agentic bioinformatics as an adaptive workflow-control layer and establish the inspectable workflow trajectory, rather than architecture or final output alone, as the primary unit of analysis.

We introduce FEV to separate demonstrated workflow Function, traceable Evidence, and use-case-specific Validation, thereby distinguishing operational breadth from scientific assurance.

We construct a cross-domain evidence map of 109 system entries and 28 benchmark or evaluation resources, representing 128 unique publications after accounting for overlap.

We derive a workflow-correctness agenda spanning analytical appropriateness, execution, replayability, provenance, evidentiary traceability, uncertainty, robustness, external validation, expert escalation, and prospective empirical testing.

Together, these contributions shift the evaluation of agentic bioinformatics from asking only what an agent can do to asking what scientific conclusions its reported workflow can support.

From Bioinformatics Copilots to Agentic Bioinformatics Large language models increasingly provide natural-language access to biological data, analytical software, databases, and scientific literature (69; 28).

Many applications function as bioinformatics copilots, assisting user-directed analysis through scripting, visualization, retrieval, and interpretation while leaving the biological objective, analytical design, tool selection, and execution primarily under human control (140; 134; 135). Although such systems can reduce computational barriers, they generally do not maintain or adapt a persistent scientific workflow.

Conventional workflow engines address a complementary problem.

Frameworks such as Nextflow and nf-core provide dependency management, environment specification, scalable execution, and provenance for predefined pipelines (26; 62). They improve procedural reproducibility, but generally do not determine whether a workflow, method, or parameterization is appropriate for the biological objective. A workflow engine can therefore execute an analytically inappropriate pipeline correctly.

An agentic bioinformatics layer adds adaptive workflow control. It interprets biological objectives, decomposes them into computational tasks, selects and invokes tools, maintains the workflow state, inspects intermediate outputs, responds to failures, and determines when additional evidence, revision, or review is required (118; 171; 28). Rather than replacing workflow engines, this layer can use them as execution substrates while providing planning, evidence integration, and workflow-level decision-making. Table S1 summarizes these distinctions. The categories are functional rather than mutually exclusive:

a platform may combine conversational assistance, predefined workflow execution, and agentic control across different tasks.

For this review, a full agentic bioinformatics layer demonstrates three minimum capabilities:

1. Goal-directed multistep control: translation of a biological objective into an ordered and revisable computational plan; 4 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue 2.

3. Stateful tool-mediated execution: invocation or coordination of analytical tools while retaining sufficient workflow state to interpret intermediate outputs and respond to failures; and Inspectable scientific support: preservation of explicit evidence, execution traces, verification outputs, or escalation records beyond singleturn response generation.

Systems demonstrating only a subset of these capabilities are retained as agent-adjacent when they provide relevant evidence for the emerging workflow paradigm. This boundary captures the transition from interactive assistance to adaptive workflow control without assuming that planning, tool access, or multi-agent architecture alone establishes scientific reliability. Unless otherwise stated, aggregate analyses include both full agentic and agent-adjacent system entries retained in the evidence map.

A Three-Dimensional Framework for Scientific Workflow Accountability The Function–Evidence–Validation (FEV) framework characterizes the scientific accountability of agentic bioinformatics workflows through three complementary but non-interchangeable dimensions. Function describes the workflow operations demonstrated by a system. The evidence describes the traceable sources used to inform these operations and support the resulting interpretations. Validation describes the procedures used to test whether workflow outputs and scientific claims are reliable. Figure S2 provides an integrated overview of these three dimensions. The dimensions represent different analytical views of the same workflow trajectory rather than sequential processing stages. Greater functional capability does not imply stronger evidence grounding, and access to stronger evidence does not by itself constitute deeper validation. A complete FEV description therefore combines a Function profile, an Evidence profile, and a use-case-specific reported Validation stage.

Function: Demonstrated Workflow Operations The Function dimension characterizes the workflow operations that an agentic system demonstrably performs. This dimension is architecture-agnostic: a system may be implemented as a single agent, a multi-agent team, a toolaugmented language model, or a hybrid workflow controller. Its Function profile is determined by observable workflow behavior rather than by model family, agent count, or architectural label.

Across the reviewed systems, six recurring dimensions emerge: planning and task decomposition; role specialization and coordination; tool selection and workflow execution; workflow-state maintenance and trace capture; self-evaluation and repair; and verification and escalation. Together, these dimensions describe how systems move from conversational assistance toward adaptive workflow control. They are descriptive and non-ordinal: broader Function profiles do not necessarily imply stronger evidence grounding, replayability, or scientific Validation. Table S3 operationalizes each dimension through an observable question, representative mechanisms, and its contribution to the workflow.

Planning, coordination, and execution.

Planning requires more than generating a plausible list of analytical steps.

A planning-capable system translates a biological objective into an ordered workflow, identifies inputs and dependencies, and revises its plan when information is missing, execution fails, or intermediate results make the initial strategy unsuitable. This distinction is particularly important in omics workflows, where choices that involve quality control, normalization, sample grouping, feature selection, and batch correction affect downstream inference (173; 148; 82; 23).

Role specialization records whether the responsibilities for planning, execution, biological interpretation, critique, or review are connected through explicit task allocation, shared state, and interpretable handoffs (28; 11; 148).

The presence of multiple agents alone is insufficient to establish coordination.

Similarly, access to a tool library does not establish tool-mediated execution.

The system must select an appropriate tool, construct valid inputs, supply parameters, monitor execution, parse its outputs, and pass the resulting artifacts to subsequent workflow steps. Successful execution demonstrates operational capability, but the suitability of the method and the resulting interpretation must be assessed separately through Evidence and Validation (49; 86; 94; 40).

Workflow state and trace capture.

Long-running analyses require more than conversational memory. Workflowstate maintenance allows a system to retain completed steps, intermediate outputs, active assumptions, failures, and unresolved decisions. Trace capture instead exposes what occurred through records such as tool calls, parameters, software versions, dataset identifiers, intermediate artifacts, and output lineage.

The two functions are related, but not equivalent: a system may maintain a rich internal state while exposing little usable provenance, whereas a conventional workflow engine may preserve strong execution traces without agent-like memory (30; 46; 58; 59). Function records whether state and traces are captured; whether the reported records are sufficient to reconstruct or replay the evaluated computation is determined under Validation.

Self-evaluation, repair, and verification.

Self-evaluation and repair require a system to detect an execution failure, weak intermediate result, or unsupported interpretation and consequently modify its plan, code, tool use, candidate selection, or interpretation. Relevant mechanisms include execution monitoring, error diagnosis, critic feedback, tool substitution, code correction, and replanning (158; 114; 87). The presence of a critic or reflection component alone is insufficient, unless its assessment changes the workflow or output.

Verification and escalation address a different question: is an intermediate artifact, a final output, or a proposed claim sufficiently supported to proceed.

Verification may involve schema and file checks, analytical diagnostics, biological plausibility assessment, evidence-coverage checks, uncertainty signaling, clarification requests, refusal, or approval gates. Its result may allow an output to proceed, flag or defer it, trigger an additional review, or lead to escalation when available evidence is insufficient (95; 84). Verification as a Function records that such an assessment occurs; whether the procedure is scientifically adequate or improves reliability belongs to the Validation dimension.

Together, the six dimensions form a profile of what a system can plan, coordinate, execute, retain, repair, and verify. The breadth of the functions describes the scope of the workflow rather than autonomy, quality, or trustworthiness. A broadly capable system may rely on weak or poorly traceable evidence, whereas a narrowly scoped system may provide strong Evidence and Validation for a specific task. Function must therefore be interpreted jointly with the sources supporting workflow actions and the assurance established for the evaluated use case.

Evidence: Traceable Support for Workflow Actions and Claims The Evidence dimension characterizes the sources used to inform workflow actions and support scientific interpretations. It is evaluated separately from Function because planning, tool use, and report generation may still rely on generic model priors, untraceable retrieval, inappropriate data, or unsupported intermediate outputs.

Across the reviewed systems, six recurring evidence categories emerge:

scientific literature; structured biological knowledge; biological measurements and metadata; software and statistical outputs; scientific-model outputs; and experimental or clinical observations. These categories form a descriptive and non-ordinal Evidence profile. Their relevance depends on the workflow and claim: literature may support method selection or interpretation, biological measurements may support dataset-specific inference, and empirical observations may provide context, corroboration, or feedback.

The quality of the evidence depends not only on source type but also on traceability, specificity, independence, reliability, and analytical role. An identifiable source may still be outdated, methodologically weak, contextually irrelevant, or insufficiently specific to the evaluated claim. Evidence objects should therefore remain linked to their origins and versions and be distinguished according to whether they serve as inputs, intermediate artifacts, contextual support, corroboration, or Validation targets. Table S4 summarizes these categories, their workflow roles, traceability requirements, and principal limitations.

Literature and structured biological knowledge.

The scientific literature supports method selection, hypothesis generation, and biological interpretation, while databases, ontologies, pathway resources, and knowledge graphs support entity normalization and relationship retrieval. These sources can improve factual grounding and attribution, but their availability does not make a claim self-validating. Their evidentiary value depends on the quality of the source, the publication or database version, the mapping of the identifier, the retrieval procedure and the relevance to the biological context evaluated (76; 8; 97; 3; 92; 2). Systems should therefore preserve citations, retrieved passages, database versions, identifiers, and query records while distinguishing established findings from extrapolation and newly generated hypotheses.

Biological measurements and computational outputs.

Biological measurements provide dataset-specific evidence through sequencing reads, expression matrices, variants, spatial coordinates, protein-abundance measurements, images, perturbation readouts, or clinical variables. Their interpretation depends on associated metadata, including sample identity, assay type, tissue, treatment, batch, cohort definition, and experimental design.

Empirical origin does not guarantee reliability: noise, confounding, batch effects, missing metadata, limited sample size, and preprocessing choices may substantially affect downstream inference (162; 82; 88; 113). Software and statistical outputs provide derived computational evidence, including qualitycontrol reports, alignments, fitted models, differential-expression results, enrichment analyses, rankings, plots, and execution logs. These artifacts often connect one workflow step to the next, but inherit the assumptions and failure modes of the tools that produced them. Their interpretation therefore requires identifiable inputs, software versions, parameters, execution status, parsing procedures, and artifact lineage. Computational outputs should be treated as provenance-bearing evidence objects rather than automatically correct observations (59; 1; 26). Whether the preserved artifacts are sufficient to establish replayability or scientific validity is determined separately under Validation.

Scientific-model outputs.

Scientific models contribute to predictions, representations, simulations, rankings, and design candidates. Examples include structure predictors, protein language models, single-cell foundation models, variant-effect predictors, docking systems, and generative molecular models (57; 70; 24; 41; 125; 17).

Such outputs can support candidate prioritization and hypothesis generation but should not be treated as equivalent to biological observations. The systems should record the model and version, the input representation, the inference settings, the confidence or calibration information, and the status of each output as a prediction. Additional computational or empirical testing belongs to the Validation dimension.

Experimental or clinical observations.

Experimental and clinical observations include perturbation measurements, binding or functional assays, clinical outcomes, and other empirical readouts available to the workflow. These observations may serve as prior evidence, retrospective corroboration, or feedback for subsequent planning. Their presence does not, however, automatically establish prospective Validation.

Previously generated or published observations used by a workflow are coded as E6. By contrast, prospective testing of an analysis, recommendation, hypothesis, or design generated by the evaluated workflow contributes to V4 and qualifier P, provided that the test is aligned with the principal claim. Qualifier C is assigned only when the newly generated empirical result is returned to the

Validation: Reported Assurance for Workflow Outputs and Claims The Validation dimension characterizes the assurance established for the outputs and scientific claims of an evaluated workflow. It is distinct from Function, which records demonstrated workflow operations, and Evidence, which records the sources supporting workflow actions and interpretations. Validation instead asks whether the workflow has been shown to execute, can be replayed, has undergone task-appropriate scientific evaluation, or has received prospective empirical support. This distinction is necessary because successful execution does not establish scientific correctness. A workflow may run without error while using inappropriate inputs, normalization procedures, sample groupings, parameters, statistical assumptions, or biological interpretations. Similarly, access to literature, databases, model predictions, or experimental observations does not necessarily validate the current workflow or claim (84; 94; 40; 136).

We define five Validation stages, denoted V0–V4. These stages are cumulative assurance gates for a specific evaluated use case: V1 requires demonstrated execution; V2 additionally requires sufficient information for replay; V3 requires task-appropriate scientific evaluation; and V4 requires prospective empirical testing of an agent-generated output aligned with the principal claim.

The stages are not global certifications of entire platforms, and the same system may satisfy different stages across tasks. Because a single stage cannot represent every form of support, Validation qualifiers are recorded separately:

B for quantitative benchmark or relevant baseline comparison, H for protocolbased human or expert assessment, S for statistical diagnostics, calibration, or uncertainty analysis, R for robustness, sensitivity, ablation, or failure analysis, X for external or independent validation, P for prospective empirical testing, and C for closed-loop empirical refinement. V-stages and qualifiers apply to evaluated use cases and should be interpreted with the corresponding Function and Evidence profiles.

Illustrative output and demonstrated execution.

At V0, a system produces explanations, hypotheses, recommendations, or workflow plans without demonstrated reliable execution. Such outputs may support ideation but remain proposals rather than executed computational Perturbation experiments, binding or functional assays, prospective preclinical or clinical evaluation, or design–test–refine cycles.

artifacts. Qualitative examples, screenshots, and informal expert impressions do not establish execution or scientific reliability. At V1, at least one toolmediated operation or workflow component is successfully demonstrated, such as a database query, tool call, executed script, notebook run, or expected computational artifact. V1 establishes operational feasibility beyond text generation, but not replayability or scientific appropriateness. Benchmark performance may be recorded as a qualifier, but does not establish V2 without sufficient information to replay the evaluated computation.

Replayable computation.

At V2, an informed user should be able to reconstruct or replay the evaluated analytical trajectory. Relevant information includes identifiable inputs, data and metadata assumptions, parameters, software or model versions, dependencies, executable workflow definitions, intermediate artifacts, and execution traces.

Containers and complete environment specifications provide strong support but are not the only acceptable forms of replayability. Replayability supports inspection, but does not establish scientific correctness. A replayable workflow may still apply an inappropriate method, omit relevant covariates, use unstable parameters, or over-interpret weak biological signals. Therefore, V2 establishes reconstructability, while V3 requires evaluation of scientifically meaningful properties of the workflow or claim.

Scientifically evaluated computation.

At V3, the system satisfies V2-level replayability and evaluates its outputs using scientific checks appropriate to the task and claim. These checks may include relevant baselines, statistical diagnostics, uncertainty analysis, robustness or sensitivity testing, external datasets, biological consistency assessment, or expert evaluation under a defined protocol. V3 should not be assigned solely because a publication reports an accuracy value, qualitative demonstration, informal expert impression, or agreement with existing biological knowledge.

The evaluation must test a meaningful property of the workflow or claim beyond successful execution. Because different forms of assessment provide non-equivalent assurance, qualifiers should be reported explicitly. For example, V3 [B,R] denotes benchmark and robustness support, whereas V3 [B,H,X] additionally records protocol-based expert assessment and external validation.

Prospective empirical evaluation.

At V4, an output generated by the evaluated workflow is tested prospectively using empirical evidence aligned with its principal claim. Examples include 8 Agentic Bioinformatics through Function, Evidence, and Validation, 2026, Volume , Issue testing a proposed guide RNA through gene editing, evaluating a designed binder in a binding assay, or assessing a prioritized intervention in a prospective preclinical or clinical study. Experimental data do not automatically establish V4. Previously generated measurements used as workflow inputs belong to the Evidence profile, while evaluation on archived experimental datasets remains retrospective computational Validation. V4 requires a direct relationship between the workflow-generated output and its prospective empirical test.

The scope of V4 is claim-specific. For example, confirmation of a designed peptide’s secondary structure does not establish binding, biological function, developability, or therapeutic utility. V4 therefore records empirical support for the evaluated claim rather than global certification of the platform. Prospective testing is also distinct from closed-loop refinement. A one-time empirical test supports the qualifier P. Qualifier C applies only when the resulting observation is returned to the system and changes a subsequent computational or experimental action.

but experimental or clinical observations remain the least frequent Evidence category across domains.

Benchmark comparison and robustness analysis are the most widespread forms of Validation support. External evaluation is concentrated in singlecell, spatial, and pathology systems, while statistical analysis and protocolbased expert assessment remain unevenly reported. Prospective testing is concentrated in protein engineering, with fewer examples in genomics and general biomedical research; closed-loop empirical refinement appears in a single mapped framework.

These domain profiles describe different forms of reported assurance rather than rankings of scientific maturity. A V3 annotation workflow and a V3 therapeutic-design workflow satisfy the same cumulative gate but may rely on different benchmarks, statistical checks, expert assessments, and external datasets. Validation must therefore be interpreted relative to the intended use and principal scientific claim.

Validation qualifiers.

Capability breadth and priorities for future systems.

The V-stage identifies the highest cumulative assurance gate satisfied by the evaluated use case, whereas qualifiers preserve the reported forms of support.

Qualifiers are descriptive and non-ordinal, and they do not override unmet stage requirements. A system cannot satisfy V3 through benchmark or expert assessment alone if the evaluated computation does not meet V2 replayability.

Validation therefore distinguishes whether an operation was demonstrated, the computation can be replayed, its outputs were scientifically evaluated, and a workflow-generated claim was prospectively tested. Function profiles, Evidence profiles, V-stages, and qualifiers should be interpreted together rather than collapsed into a single system score.

As shown in panel a, most systems implement multiple Function and Evidence dimensions, yet the majority remain at V3. Broader operational scope therefore does not imply stronger scientific assurance: additional agents, tools, databases, memory modules, or predictive models may expand a workflow without establishing replayability, verification, or empirical support for its principal claim.

Panel b reports an observed gap score, defined as one minus the withindomain share reporting each capability or Validation practice. The largest recurring gaps are related to prospective empirical testing and closed-loop refinement, while verification, expert assessment, uncertainty analysis, and external validation remain unevenly reported. These gaps are descriptive rather than universal requirements and should be interpreted in relation to the scope, intended use, and claim of the workflow.

Progress should therefore be assessed by workflow accountability rather than by the number of agents or tools. Priorities include inspectable shared state, provenance-preserving handoffs, explicit verification gates, calibrated uncertainty, external evaluation, and claim-aligned prospective testing. Where experimentation is feasible, empirical results should inform subsequent candidate selection, experimental design, or analysis, enabling scientifically accountable design–test–refine cycles.

The reported proportions describe the structured review sample rather than the complete literature and depend on publication-level reporting.

Unreported or insufficiently documented capabilities were not coded. Systemlevel assignments and supporting details are provided in Supplementary Tables S1–S28.

Cross-System Synthesis through the FEV Framework Overall FEV landscape.

Cross-domain differences.

Evidence profiles largely reflect data modality. Biological measurements are prominent in single-cell, spatial, and imaging workflows, whereas scientificmodel outputs are especially common in pathology, protein engineering, and drug discovery. Software and statistical outputs are nearly universal, Evaluation, Trustworthiness, and Benchmarking Evaluation of agentic bioinformatics must extend beyond final-answer quality because biological conclusions emerge from workflows involving data and metadata selection, method choice, parameterization, tool execution, intermediate artifacts, statistical assumptions, and interpretation. A plausible endpoint may therefore conceal an inappropriate analysis, lost provenance, failed tool call, or unsupported biological claim. Recent benchmarks increasingly assess process-level behavior, including planning, tool selection, execution, artifact generation, failure recovery, citation grounding, and trajectory completeness (9; 16; 94; 40; 136; 93). However, most remain measures of computational competence rather than prospective biological, clinical, or experimental validity.

From Answer Correctness to Workflow Assurance Answer correctness measures agreement with a reference answer or expert judgment, whereas workflow assurance asks whether the actions producing that answer were appropriate, inspectable, and sufficiently tested for the claim being made. Relevant criteria include method selection, valid tool inputs and parameters, required artifacts, trace completeness, evidentiary attribution, failure detection, and uncertainty reporting. This distinction is particularly important in long-horizon workflows, where a locally successful but inappropriate step may invalidate downstream results.

Workflow assurance is also claim-dependent. A database lookup, rawdata analysis, disease-mechanism claim, therapeutic recommendation, and experimentally consequential design require different forms of support.

Benchmark results should therefore be interpreted relative to workflow scope, risk, and intended use rather than treated as interchangeable measures of system quality.

Under FEV, evaluation should report three complementary properties:

demonstrated workflow operations, the appropriateness and traceability of supporting Evidence, and the Validation established for the evaluated use case.

These properties should not be collapsed into a single accuracy score. A system may complete a task using an inappropriate method, retrieve relevant evidence without preserving a replayable workflow, or perform strongly on a benchmark without external or empirical validation.

Challenges and Future Directions The FEV synthesis shows that planning, retrieval, and tool-mediated execution are advancing more rapidly than replayability, formal verification, and prospective empirical testing. Therefore, progress depends less on increasing the number of agents or tools than on strengthening the accountability of workflow actions, evidence, and claims.

Reliable and Replayable Workflows Benchmark Design for Agentic Bioinformatics The mapped resources suggest three complementary benchmark families.

Outcome-oriented benchmarks assess the correctness of an answer, prediction, annotation, design, ranking, or report. Process-oriented benchmarks assess planning, tool selection, parameterization, execution, artifact generation, repair, citation grounding, and trajectory completeness. Domain-calibrated benchmarks test whether these behaviours are appropriate for particular settings, including genomics, single-cell and spatial omics, protein design, drug discovery, and computational pathology. Detailed benchmark profiles are provided in Supplementary Tables S29–S33.

Effective benchmark suites should combine these families using realistic multistep tasks with biological data, metadata constraints, software dependencies, expected intermediate artifacts, and criteria for both computational and biological outputs. Table S6 summarizes the principal task types.

Benchmark tasks should combine deterministic grading of execution, files, parameters, and artifacts with domain-sensitive assessment of biological interpretation. They should also evaluate robustness under missing or contradictory metadata, corrupted inputs, unavailable tools, software-version changes, task reformulation, irrelevant retrieval, and conflicting evidence.

A correct endpoint should not receive full credit when required tools were not invoked, evidence was fabricated, or the workflow cannot be replayed; conversely, a well-documented trajectory does not compensate for an incorrect biological conclusion. Finally, benchmark reports should state the claims that their results cannot support. Performance in question answering, tool selection, execution, or retrospective datasets does not establish prospective biological, preclinical, or clinical utility. Evaluation should therefore identify the highest Validation stage directly supported and the remaining requirements for external or empirical testing.

Real bioinformatics workflows contain incomplete metadata, heterogeneous files, missing dependencies, ambiguous objectives, and confounded study designs. Future systems should validate inputs and assumptions, detect underspecified tasks, recover from execution failures, and request clarification or additional review when available evidence is insufficient. Robustness should be tested under changes in metadata, task formulation, tool availability, software versions, and biological domains rather than only on curated demonstrations. Systems should also preserve the information required to inspect and replay their workflows, including dataset identifiers, metadata, analytical assumptions, tool calls, parameters, software and model versions, generated code, intermediate artifacts, failures, repairs, and evidence links.

Agentic layers should be built on workflow engines, notebooks, containers, provenance standards, and institutional infrastructure rather than replacing them. Standardized interfaces for tools, artifacts, and evidence would improve portability between models and laboratories.

Claim-Calibrated Validation and Empirical Closure Validation requirements should be proportional to the claim. Database retrieval, raw-data analysis, disease-mechanism inference, therapeutic recommendation, and protein design require different forms of assurance. Computational assessment may include relevant baselines, statistical diagnostics, uncertainty analysis, robustness testing, external datasets, biological consistency checks, and protocol-based expert review. Claims about biological function or intervention also require prospective testing aligned with the principal claim.

Prospective testing should remain distinct from closed-loop refinement. A onetime assay evaluates an agent-generated output, whereas a closed loop returns the empirical result to the system and changes the next computational or experimental action. Greater autonomy is not inherently preferable: requesting

clarification, refusing unsupported inference, or recommending additional validation may represent more reliable scientific behavior.

Compare against baseline pipelines, test parameter sensitivity, or assess biological consistency.

Superficial repair, repeated failures, or silent output corruption.

answers they produce but also by whether the workflows supporting those answers can be replayed, evaluated, challenged, and, where necessary, tested empirically.

Governance, Oversight, and Reporting Standards The appropriate degree of autonomy should depend on the risk of workflow.

Exploratory analyses may permit broader automation, while patient-derived data, clinical interpretation, therapeutic reasoning, gene editing, and experimental design require stronger access controls, approval gates, audit logs, privacy protections, and expert oversight. Human involvement should be operationally defined by specifying which decisions require review and how the intervention changes the workflow. A minimum reporting standard should document workflow scope, models and tools, data and evidence sources, parameters and environments, intermediate artifacts, failures and repairs, approval points, reported Validation stage, and the specific forms of computational or empirical support. The most valuable agentic bioinformatics systems will therefore not necessarily be those with the greatest autonomy, but those that accelerate scientific work while preserving replayability, evidentiary traceability, uncertainty, appropriate oversight, and claim-calibrated Validation.

Agentic bioinformatics should be evaluated through inspectable workflow trajectories rather than architecture or final answers alone.

The Function–Evidence–Validation framework separates demonstrated workflow operations, traceable evidentiary support, and use-case-specific scientific assurance.

Among 109 system entries, planning and tool-mediated execution are more common than explicit verification, prospective testing, and closed-loop refinement.

Replayability, provenance-preserving evidence linkage, calibrated validation, and expert escalation are priorities for scientifically accountable agentic workflows.

Author Contributions Conclusion Agentic bioinformatics is extending biological computation from conversational assistance toward adaptive workflow control. Its scientific value lies not only in making analytical tools accessible through natural language, but in translating biological objectives into workflows whose actions, evidence, artifacts, and limitations can be inspected. The Function–Evidence–Validation (FEV) framework separates three properties that should not be conflated: the workflow operations a system demonstrates, the traceable evidence supporting its decisions and claims, and the assurance established for its outputs. The reviewed literature shows rapid progress in planning, retrieval, and toolmediated execution, but less consistent support for replayable computation, evidentiary provenance, robust scientific evaluation, and prospective empirical testing. The next stage of agentic bioinformatics therefore depends less on maximizing autonomy than on strengthening scientific accountability.

Reliable systems should preserve inspectable workflow trajectories, distinguish observations from predictions and hypotheses, expose uncertainty, support meaningful human oversight, and apply validation appropriate to the claims being made. Ultimately, agentic systems should be judged not only by the

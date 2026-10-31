# Kosmos: An AI Scientist for Autonomous Discovery

> **Bibkey** `Mitchener2025_251102824` · **Venue** arXiv preprint (2025) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2511.02824> · `status: complete`

---

## One-liner
Kosmos (Edison Scientific / FutureHouse) is an AI scientist for data-driven discovery: given an open-ended objective and a dataset it runs for up to 12 hours, sharing information between parallel data-analysis and literature-search agents through a **structured world model** — on average ~200 agent rollouts, ~42,000 lines of code and ~1,500 papers per run — and every report statement cites a code notebook or primary literature. Independent scientists checked 102 statements: 79.4% accurate (data-analysis 85.5%, literature 82.1%, interpretive synthesis only 57.9%).

## Problem
Current research agents can take only so many actions before losing coherence, capping the depth of findings: Robin shares little context between agents and targets therapeutics; Sakana's AI Scientist is limited to ML; Google's Co-Scientist reasons but does not run or analyse experiments; the Virtual Lab lacks exploratory data analysis. Kosmos asks whether an agent can **coherently sustain hundreds of rollouts** toward one objective, explore high-dimensional data at scale, and keep conclusions traceable.

## Method
**Loop**: a scientist supplies an objective and dataset; each cycle Kosmos runs up to ten literature-search and data-analysis tasks in parallel (via Edison's general data-analysis and literature agents), writes task-output summaries into the world model, then queries it to propose the next cycle's tasks. This context management lets it pursue many lines at once and run eight times as many iterations as prior systems. At the end it synthesizes three or four reports, each statement and figure citing a paper or a Jupyter notebook. **Evaluation**: (1) 102 statements from three representative reports, labelled as data-analysis / literature / interpretation, independently reproduced or checked by experts **without access to the original code or citations**, judged Supported/Refuted (Unsure re-judged after clarification); (2) expert-equivalent time estimated at 15 min per paper, 2 h per notebook analysis and 174 work-hours per month; (3) collaborating academic groups rated expert-equivalent time, valuable findings, novelty and reasoning depth at cycles 5, 10 and 20.

## Data
Each of the seven discoveries uses a different data type and field: (1) untargeted brain metabolomics of hypothermic neuroprotection in mice (control 6, hypothermic 6, normothermic 5); (2) perovskite solar-cell fabrication environment data; (3) neuronal connectomics; (4) plasma-proteome GWAS + myocardial T1 GWAS (public, Mendelian randomization); (5) islet 10x multiome (GSE124742, GSE164875) + DIAMANTE T2D GWAS; (6) laser-capture proteomics of tau-positive/negative neurons in Alzheimer's disease ordered on pseudotime; (7) single-nucleus transcriptomes of entorhinal vs control cortex in mice aged 6–28 months. Several datasets come from unpublished or in-preparation manuscripts.

## Key results
- **Scale**: per run, on average 166 data-analysis and 36 literature rollouts, ~42,000 lines of code and 1,500 full papers; 9.8× Robin's code generation.
- **Statement accuracy** (102 statements): 79.4% overall; 85.5% of data-analysis statements reproducible, 82.1% of literature statements supported by primary sources, only 57.9% of interpretive/synthesis statements accurate.
- **Equivalent effort**: task counting estimates ~4.1 expert-months per run (n = 6); collaborators estimate a 20-cycle run's findings would take them 6.14 months (n = 7), roughly doubling from cycle 5 to 20; valuable findings scale linearly with cycles (tested to 20), and cycle-20 findings are rated moderate-to-complete novelty and moderate-to-high reasoning depth.
- **Seven discoveries**: three independently reproduce preprinted or unpublished results not accessed at runtime (nucleotide metabolism as the dominant pathway altered in hypothermic brain; annealing humidity as the critical determinant of perovskite performance; log-normal neuronal connectivity); two add new support to existing findings (Mendelian randomization suggesting high circulating SOD2 may causally reduce myocardial fibrosis; cis-regulation of SSR1 by the protective T2D variant rs9379084); one devises a new analysis (segmented regression locating a breakpoint in ECM-pathway decline along Alzheimer's pseudotime, Davies test p = 0.017); one makes a novel clinically relevant finding (entorhinal-neuron vulnerability in ageing involving declining flippase Atp10a and microglial activation, validated in an independent dataset and human Braak stages).

## Contributions
- **A structured world model as shared context for many agents**, pushing coherent operation from tens of steps to hundreds of rollouts — the core engineering contribution.
- **Every statement traceable**: each report sentence links to the notebook or paper that produced it, enabling independent re-checking.
- **Accuracy evaluation stratified by statement type** (data / literature / interpretation), with experts reproducing blind to the original evidence — an unusually rigorous way to evaluate an AI scientist.
- Discoveries demonstrated across metabolomics, materials, connectomics, statistical genetics, proteomics and transcriptomics.

## Limitations
- **Interpretive statements are only 57.9% accurate**, attributed to conflating statistical significance with scientific value; it also invents statistically sound but conceptually obscure metrics; evaluators note it tends to make overly strong claims.
- **No automated way to judge whether a claim is accurate, novel and significant**: a report has 3–4 discovery narratives of ~25 claims each, built on 8–9 trajectories, and triage relies entirely on domain experts — identifying valuable discoveries at scale remains a bottleneck.
- **Stochasticity**: independent runs may not converge on the same discoveries; directions are sensitive to objective phrasing; input preprocessing markedly changes the focus of results.
- Technical limits: datasets up to ~5 GB; weak on raw data (images, raw sequencing files); cannot fetch external public data for reference or orthogonal validation; no mid-run human interaction. The accuracy audit sampled only 102 statements from three reports.

## Relation to our direction
Kosmos is almost the **prototype object of study for the agent-trustworthiness topic**: an agent that analyses omics data and outputs cited conclusions, whose authors concede three things — interpretive statements are only ~58% accurate, independent runs may not converge, and there is no automated way to judge claim correctness. These map onto the agent-trustworthiness topic's three pillars: **(1) claim-to-evidence verification** — Kosmos already links each statement to a notebook or paper, naturally yielding claim–evidence pairs our verifier can operate on, reporting separately along its data / literature / interpretation split; **(2) calibrated verifier** — the 57.9% vs 85.5% gap means calibration must be per claim type, with lower prior confidence for interpretive claims; **(3) rerun stability** — "runs don't converge" and "sensitive to phrasing and preprocessing" need quantifying, e.g. rerun on the same kidney dataset and measure each finding's reproduction rate. Its Discovery 5 (islet 10x multiome + GWAS) and Discovery 7 (single-nucleus transcriptomics) are the same kind of analysis as kidney snRNA/snATAC data, providing real cases for an **omics-specific failure taxonomy** (treating significance as biological importance, inventing obscure metrics, skipping orthogonal validation on external data). There is also a thread to **the artifact-injection topic**: Kosmos is weak on raw images and cannot pull external reference data, whereas the artifact-injection topic's cross-modal agreement depends on raw H&E and KPMP/HuBMAP references — exactly where such agents fail today, so the artifact-injection topic's detection pipeline should be exposed to agents as dedicated tools rather than expecting agents to write it themselves.

## Reusable assets
- **Figure and analysis scripts:** the kosmos-figures repo (Kosmos itself is a service on the Edison platform, not open source).
<https://github.com/EdisonScientific/kosmos-figures>
- **Reports and trajectories:** the seven Kosmos reports (Supplementary Data 1–7 and Edison links), with each statement clickable to its notebook — real-world claim–evidence pairs.
- **Evaluation protocol:** three-way statement typing + expert reproduction blind to original evidence + a Supported/Refuted/Unsure workflow (instructions and positive/negative examples in SI 2–4).
- **Public data:** plasma-proteome GWAS (Synapse syn51365303), myocardial T1 GWAS, GSE124742 / GSE164875.

## Follow-ups
- The predecessor Robin (`robin-nature-2026`) and the data-analysis benchmark BixBench (`bixbench-arxiv-2025`).
- The Refuted examples in SI 4 — first samples for an omics-agent failure taxonomy.
- Track whether Kosmos publishes world-model internals or a systematic multi-run consistency study.

## Cite
```bibtex
@misc{Mitchener2025_251102824,
  title = {Kosmos: An AI Scientist for Autonomous Discovery},
  author = {Ludovico Mitchener and Angela Yiu and Benjamin Chang and Mathieu Bourdenx and Tyler Nadolski and Arvis Sulovari and Eric C. Landsness and Daniel L. Barabasi and Siddharth Narayanan and Nicky Evans and Shriya Reddy and Martha Foiani and Aizad Kamal and Leah P. Shriver and Fang Cao and Asmamaw T. Wassie and Jon M. Laurent and Edwin Melville-Green and Mayk Caldas and Albert Bou and Kaleigh F. Roberts and Sladjana Zagorac and Timothy C. Orr and Miranda E. Orr and Kevin J. Zwezdaryk and Ali E. Ghareeb and Laurie McCoy and Bruna Gomes and Euan A. Ashley and Karen E. Duff and Tonio Buonassisi and Tom Rainforth and Randall J. Bateman and Michael Skarlinski and Samuel G. Rodriques and Michaela M. Hinks and Andrew D. White},
  year = {2025},
  eprint = {2511.02824},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2511.02824}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

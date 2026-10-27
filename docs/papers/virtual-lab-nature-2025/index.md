# The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies

> **Bibkey** `Swanson_2025` · **Venue** Nature (2025) · **Category** agents · **Relevance** medium · **Access** paywall
> **Link** <https://doi.org/10.1038/s41586-025-09442-9> · `status: complete`

---

## One-liner
Stanford's (Zou lab) Virtual Lab with CZ Biohub: an LLM "PI agent" leads LLM scientist agents it defines itself (immunologist, ML specialist, computational biologist) plus a Scientific Critic, driving a real interdisciplinary project through "team meetings + individual meetings" while the human supplies only high-level agendas and feedback. On a protein-binder design task the agent team autonomously chose and chained three existing public tools (ESM, AlphaFold-Multimer, Rosetta) into a computational pipeline; the resulting candidates were characterized in a human lab, where most expressed and retained their original specificity and two showed improved binding to more recent variants. Across the project the human wrote just 1.3% of all words.

## Problem
Interdisciplinary research needs ever larger teams (34 authors on AlphaFold 2), and most scientists — especially under-resourced groups — lack access to experts across fields. LLMs answer individual science questions well, but open-ended, multi-step, cross-domain research full of unknowns is different. Prior systems are single-domain (ChemCrow, Coscientist's chemistry tasks), confined to ML without real experiments (AI Scientist), or ideation-only (Si et al.). Can a team of LLM agents with light human guidance complete a **real interdisciplinary project with experimentally validated results**?

## Method
**Agent definition**: each agent is specified by a four-part prompt — title, expertise, goal, role. The human defines the PI and the Scientific Critic; the PI then creates scientist agents from a short project description, using its own prompt as the template. GPT-4o powers the agents. **Meeting mechanics**: inputs are an agenda (required), agenda questions and rules (optional), summaries of previous meetings, extra context (e.g. papers) and the number of rounds (typically N = 3). **Team meeting**: the PI opens with initial thoughts and guiding questions → each scientist agent responds in turn to the discussion so far → the Scientific Critic critiques → the PI synthesizes, decides and asks follow-ups; after N rounds the PI writes a summary, gives a recommendation and answers the agenda questions — the human need only read that final response. **Individual meeting**: one agent performs a specific task (e.g. writing code), with the Critic giving improvement feedback each round and the agent producing a final improved answer. **Parallel meetings**: the same meeting is run five times at a higher "creative" temperature of 0.8, then merged in one meeting at a lower "consistent" temperature of 0.2 that combines the best elements (more flexible than majority voting). **Project flow (five phases)**: team selection (the PI picks three scientist agents) → project specification (a team meeting answers agenda questions such as what to make, whether to modify known molecules or design de novo, and which known molecules to start from) → tools selection (a team meeting lists usable public models/software) → tools implementation (each agent writes scripts with Critic feedback, plus one follow-up meeting to fix first-draft errors) → workflow design (the PI decides how to combine the three tools, with a weighted score to shortlist candidates over several iterations). A human lab then characterizes the selected candidates.

## Data
No training datasets; the resources are three already-public computational tools (the protein language model ESM, structure prediction via AlphaFold-Multimer with LocalColabFold 1.5.5, and Rosetta REF15) plus public known molecules/structures (PDB entries). The evaluation "data" are the meeting transcripts and word counts: 1,596 human words vs 122,462 agent words. Experimental characterization was done in a human lab (E. coli expression + an antigen array + multiplexed ELISA) on 92 designs plus four unmutated references.

## Key results
- **Minimal human input**: the human wrote 1,596 words across the whole workflow (including text copy-pasted from a score file), **1.3%** of all words; agents wrote 122,462 words (98.7%), including every Python script and one XML script written from scratch.
- **The agents' high-level decisions are auditable and justified**: modify known molecules rather than design de novo (leveraging existing structural data and known efficacy for a faster, more reliable path), four named starting molecules, and a focus on one particular binding domain.
- **The self-built pipeline works**: the three agent-written scripts (~130 lines for ESM scoring, ~144 for an interface-confidence calculation, ~71 lines plus a 30-line XML for Rosetta energy extraction) ran after the human flagged first-draft errors; and the PI's weighted score **correctly used a negative weight for the binding-energy term** (more negative is better), showing it understood metric directions.
- **Experimental characterization**: of 92 designs, 38% (35/92) expressed at high to very high levels and only 6.5% (6/92) showed little or no soluble expression, indicating the changes were broadly tolerated without large-scale misfolding or aggregation; most designs retained specificity for the original antigen (96%, 44/46, in two of the series).
- **Two candidates gained new binding**: two designs kept binding to the original antigen while gaining moderate binding to more recent variants, confirmed by dilution curves (EC50 weaker than to the original antigen); the authors speculate about charge-complementarity mechanisms, note that changes at some positions are not tolerated (one series bound the original antigen poorly overall), and report one inadvertently introduced cysteine that made three designs highly non-specific.
- **Attribution**: the authors attribute widely preserved or improved binding to the original antigen mainly to ESM likelihoods, which are **antigen-agnostic and favour evolutionarily plausible sequences**, while newly gained variant binding more likely comes from the structure/energy terms.

## Contributions
- Casts the "lab" itself as the agent architecture: a PI plus auto-generated specialist agents plus an explicit Critic, organizing interdisciplinary discussion through structured meetings (team/individual × parallel + merge) with human involvement only at the agenda level.
- **Parallel meetings with split temperatures** (high for diverse drafts, low for merging) is a simple, general quality mechanism.
- The explicit Critic agent's role is concretely demonstrated (it writes more words than the scientist agents, since it must critique everyone).
- An end-to-end loop on an open-ended project — agent decisions → agent-written tooling → human experimental validation — with the human/agent writing contribution quantified.

## Limitations
- **Knowledge cutoff**: agents are unaware of the latest literature and software versions, so they did not propose newer tools (AlphaFold-Multimer rather than AlphaFold 3) and wrote code assuming old function names incompatible with current packages — fixed after the human pointed it out (the authors suggest RAG as a remedy).
- **The tools themselves are imperfect**: even when used correctly, errors in structure prediction and the like limit reliability.
- **Prompt engineering needed**: without explicit guidance agents give vague answers and dodge hard choices (asked to pick one option they often said "do both" until told to "choose only one"); the human may iterate on an agenda several times.
- Validated on one project only; experiments are in vitro binding characterization, the new binding is moderate with weaker EC50 than to the original antigen, far from a usable candidate; a single base model (GPT-4o) with no cross-model comparison.

## Relation to our direction
The Virtual Lab connects to our direction mainly at the **architecture and evaluation** level rather than in biology. It demonstrates a mode of working where the human supplies only agendas and the agent team decides the technical route and writes the tooling — matching the **model/revert pipeline-design step** of detect → model → revert: give the agenda "predict which perturbations pull an anomalous program back to normal in the virtual tissue" and let an agent team choose the models (perturbation prediction, spatial integration, pathway enrichment) and how to combine and score them. Three concrete lessons: **(1) auditable decision records** — its team meetings write down every high-level decision with justification, and this "agenda question → answer → justification" structure is the upstream form of the claim-to-evidence skeleton Topic 2 wants, at the decision rather than conclusion level; **(2) explicit Critic plus parallel-and-merge** — these map onto Topic 2's calibrated verifier and rerun stability: high-temperature parallel drafts merged at low temperature trades ensembling for stability, the same idea as Robin's eight-trajectory consensus, and the two are useful comparators for stability mechanisms; **(3) knowledge cutoff causing outdated tool choices** — a high-frequency failure mode for omics agents (obsolete pipelines, old function names, superseded methods) and worth its own category in the omics-specific failure taxonomy: in snRNA/snATAC/Xenium the tools and best practices shift yearly (ambient-RNA correction, segmentation, doublet detection), and a wrong method choice usually raises no error, silently producing unreliable conclusions. One further caution: the paper's main positive result (retained original specificity) is attributed by the authors to a prior score that is **agnostic to the actual objective** (sequence plausibility), while the objective-directed structure/energy terms contributed less — a methodological warning for us, since mixing objective-agnostic plausibility priors into virtual-tissue perturbation scoring can make results look successful without the model having understood the objective.

## Reusable assets
- **Code:** the Virtual Lab framework (implementation of agent definitions and meeting mechanics).
<https://github.com/zou-group/virtual-lab>
- **Preprint full text:** bioRxiv 10.1101/2024.11.11.623004 (the appendix contains all prompts).
<https://www.biorxiv.org/content/10.1101/2024.11.11.623004v1>
- **Borrowable designs:** the four-part agent prompt (title/expertise/goal/role), PI-driven team assembly, an explicit Critic, team- and individual-meeting templates, parallel meetings with split-temperature merging, and "agenda rules" that force agents to commit to a single decision.
- **Evaluation metric:** the human/agent word-count split (1.3% vs 98.7%) as a simple comparable autonomy measure.

## Follow-ups
- The final Nature version, to check numeric and conclusion differences from the preprint.
- Kosmos (`kosmos-arxiv-2025`) criticizes the Virtual Lab for lacking exploratory data analysis — compare world-model vs meeting-based context management.
- The full prompts in the preprint appendix, as a template library for multi-agent meeting prompts.

## Cite
```bibtex
@article{Swanson_2025, title={The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies}, volume={646}, ISSN={1476-4687}, url={http://dx.doi.org/10.1038/s41586-025-09442-9}, DOI={10.1038/s41586-025-09442-9}, number={8085}, journal={Nature}, publisher={Springer Science and Business Media LLC}, author={Swanson, Kyle and Wu, Wesley and Bulaong, Nash L. and Pak, John E. and Zou, James}, year={2025}, month=July, pages={716–723} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

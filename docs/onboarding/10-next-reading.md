# 10 · What to read next

> ⏱ About 3 h · Day 2 · Hands-on (optional)

!!! abstract "After this module you can answer"
    - How do you get through a deep-read in 20 minutes?
    - Which three deep-reads come first?
    - Where are each topic's reading path, the knowledge map and the literature review, and how do you use them?

Onboarding ends here. From now on you read under the **Papers** tab: every paper has a bilingual **deep-read** page, plus a literature review and a knowledge map that tie them together. This module tells you where to start and in what order.

## Step 1 · How to read a deep-read

Every deep-read has the same structure. Do not read it top to bottom; in this order one takes about 20 minutes:

1. **One-liner**: what the paper did;
2. **Relation to our direction**: how it connects to our topics, **the most important section**;
3. **Data**: which data and how many people (module 7's six questions come in here);
4. **Key results**: only the ones that matter for section 2;
5. **Limitations**: what it leaves open, which is often what we work on;
6. **Method** and **Reusable assets** (links to code, data, models) when you need them.

The `status` in the page header says what was read: `complete` means the full text; `abstract-only` means only the abstract was available (a paywall, for example), so the notes are shorter and more cautious. Papers marked ★ in the paper list are highly relevant to our direction.

!!! tip "Computer analogy"
    Read a deep-read like someone else's design doc: summary and "how it relates to our system" first, then the sections relevant to your problem, and implementation details last.

## Step 2 · Three deep-reads for everyone

Whatever your topic, read these three first. Each matches one of module 8's traps; read with the question in brackets:

1. **[Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md)**: the data you used in module 9. (How were the altered states called? Which of the criteria overlap with QC metrics?)
2. **[Janssen 2023](../papers/janssen-ambient-noise-genomebiol-2023/index.md)**: uses DNA differences between mouse strains to measure how much ambient contamination each cell carries. (Why is an answer given by the experimental design more reliable than the expression profile?)
3. **[Dann 2023](../papers/healthy-ref-natgenet-2023/index.md)**: finding disease-altered cell states against a healthy reference, and how to choose that reference. (Why do false positives rise when reference and query come from different sources?)

About 1 hour for the three.

## Step 3 · Your topic's reading path

The last section of every topic page is a **reading path**: about five deep-reads in order, each with a reason. Open your topic page and continue from there:

- [Artifact Injection to Boost Anomaly Detection in Kidney Single-Cell Omics](../research/anomaly-benchmark.md)
- [Trustworthiness of Hypothesis-Testing Agents on Kidney Omics](../research/agent-claims.md)

Skip any you already read in step 2.

## Step 4 · Use the knowledge map to find the next paper

After the reading path, find further papers yourself with the **[knowledge map](../knowledge-map.md)**. It has several views:

- **One view per topic**: papers grouped by theme (the artifact-injection topic has 7 groups such as "General AD methods", "Atlases & disease states", "QC & artifacts"). Groups start collapsed; click to open one, double-click a paper to open its deep-read. The "Pipelines" section of the knowledge-map page lays these groups out as the topic's pipeline (the artifact-injection topic: public kidney atlases → QC & artifact removal → model of healthy tissue → anomaly / OOD score → cross-modal check → evaluation vs. experts).
- **Bridge**: papers that more than one topic needs.
- **Method × data matrix**: rows are kinds of anomaly-detection method, columns go from general data to kidney omics; arrows show a method carried over to another kind of data, and **dashed cells mark what the artifact-injection topic plans to add** (some already hold papers; the note in each cell says what is still missing).

A useful way in: find the cell you know best in the matrix (for example PatchCore, the nearest-neighbour method from image anomaly detection) and follow its arrows to see which kinds of data it has reached, and where the chain stops before kidney omics.

## Step 5 · The literature review

The **[literature review](../literature-review.md)** is an early essay covering the library's first 18 items (mostly histopathology, spatial omics, foundation models and virtual cells, plus two medical-imaging papers and one single-cell perturbation paper), organised by the three stages "detect → model → revert", with **Synthesis & gaps** as its second-to-last section. It does not yet include the kidney-omics, general anomaly-detection or agent papers, so it overlaps little with the two topics' reading paths; read it as background on the wider direction.

## Step 6 · When you find a new paper

The paper library is maintained by the group. When you find a paper worth reading, tell whoever maintains the library, or add it yourself with the workflow in the repository's `CLAUDE.md`: one command creates the paper folder, then you write the bilingual deep-read. Two rules matter most: **base the deep-read on the paper itself, never on memory; if you cannot get the full text, mark it `abstract-only`**.

## Self-check

??? question "1. You only have time for one section of a deep-read. Which one?"
    "Relation to our direction". It says how the paper connects to our topics, which decides whether to keep reading.

??? question "2. Where do you look to see what gaps the artifact-injection topic still has?"
    The method × data matrix in the knowledge map, where dashed cells mark what the artifact-injection topic adds; also the "Why it is unsolved" and "Open questions" sections of the artifact-injection topic page.

??? question "3. A deep-read's header says `abstract-only`. What should you keep in mind?"
    It is based on the abstract and public information only, not the full text. Numbers and method details may be incomplete; check the original before citing it.

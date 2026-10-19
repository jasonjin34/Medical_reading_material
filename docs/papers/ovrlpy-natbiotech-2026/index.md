# Identifying 3D signal overlaps in spatial transcriptomics data with ovrlpy

> **Bibkey** `Tiesmeyer_2026` · **Venue** Nature Biotechnology (2026) · **Category** spatial · **Relevance** high · **Access** paywall
> **Link** <https://doi.org/10.1038/s41587-026-03004-8> · `status: complete`

---

## One-liner
ovrlpy computationally "splits" a 5–15-µm imaging-based spatial-transcriptomics section into virtual top and bottom sub-slices and compares their local expression similarity, producing an unsupervised, segmentation-free **vertical signal integrity (VSI) map** that localizes vertically overlapping cells (z-axis doublets), tissue folds and inaccurate segmentation.

## Problem
Imaging-based ST (Xenium, MERSCOPE) localizes transcripts in 3D, but almost all analyses project to 2D and segment in 2D. In sections about as thick as a cell, different cells can stack at the same x–y position, so segmented "cells" mix transcripts from several types — vertical spatial doublets. A simplified geometric model (spherical cells in dense tissue) predicts that **a 10-µm cell in a 10-µm section has an average signal-to-total ratio of only 0.4**, i.e. most projected signal may come from vertically adjacent structures.

## Method
**Virtual sub-slicing**: transcript z positions drift globally across a sample, so a single global threshold fails; instead transcripts are binned in x–y (usually 1 µm), the mean z per bin is computed and locally smoothed by graph message passing (repeated neighbour averaging), and the smoothed z serves as each bin's split point, yielding top and bottom virtual sub-slices. **VSI**: building on an unsupervised, segmentation-free SRT analysis algorithm cited in the preprint (refs 12–13; presumably the group's earlier SSAM/Sainsc line), local expression similarity between top and bottom sub-slices gives the VSI map; low VSI = top/bottom disagreement = likely overlap or artifact. **Visualization**: expression signal at local maxima is embedded in 2D UMAP and RGB colour space; transcripts in an ROI are coloured by the RGB embedding for inspection. **Usage**: input a transcript table with gene, x, y, z columns plus a few parameters (e.g. number of PCA components); per-cell mean VSI can flag doublets (the authors' example threshold: mean VSI < 0.7). The algorithm uses neither the geometric model nor cell-shape assumptions.

## Data
A 10-µm Xenium mouse coronal brain section (with replicates); a MERSCOPE mouse coronal brain section; public MERSCOPE mouse liver; Vizgen's public 3D-DAPI-segmented mouse brain; 3D segmentation comparisons with Baysor and Proseg. Cell typing via MapMyCells.

## Key results
- **Top/bottom disagreement is common**: of 162,033 segmented cells in Xenium mouse brain, independently annotated top and bottom halves **agree on cell type for only 78%** (80% and 79% in replicates); glia, oligodendrocytes and vascular cells are especially prone to vertical doublets. In hippocampal CA1, only ~20% of 152 inhibitory/glial cells are consistent, most forming vertical doublets with neighbouring excitatory neurons. MERSCOPE: 83% tissue-wide, 51% for CA1 non-neuronal cells. The authors caution these figures may overstate the impact (half-cells have fewer transcripts and type less reliably).
- **The VSI map exposes multiple artifacts**: meninges, choroid plexus and capillaries are persistently low-VSI; several ventral low-VSI structures match sample-preparation tissue folds; in silico simulated overlaps confirm low VSI marks overlap; z-stack DAPI validates vertical doublets; a virtual sub-slice has higher VSI than the full section, consistent with thinner slices overlapping less. In mouse liver, endothelial and stromal cells more often form vertical doublets with hepatocytes.
- **As QC for 3D segmentation**: for Baysor/Proseg 3D segments, MapMyCells correlation tracks ovrlpy VSI significantly, but both fail on the ventral tissue fold (many leptomeningeal cells mis-segmented); in Vizgen's 3D-DAPI segmentation, **fewer than 7%** of 810 high-confidence ovrlpy overlap regions (VSI < 0.5) had overlapping nucleus segments.
- **Downstream impact**: cells with mean VSI < 0.7 flagged as vertical doublets sit between singlet clusters in UMAP (like scRNA doublets); removing them sharpens cell-type separation in both Xenium and MERSCOPE, and helps identify spurious spatial subtypes caused by overlap contamination rather than true subtype differences.

## Contributions
- First systematic quantification of 2D-projection-induced vertical contamination, with simple geometric intuition (signal-to-total ≈ 0.4).
- Claimed by the authors as **the only unsupervised tool focused on z-axis spatial doublets**; segmentation-free, reference-free, shape-agnostic.
- Locally smoothed z split points handle global z drift.
- The VSI map indicates both biological overlap and **sample-preparation artifacts** such as tissue folds.

## Limitations
- Low VSI can come from overlap, folds, subcellular mRNA localization or uneven sectioning — the authors explicitly ask users to inspect low-VSI regions' composition to tell sources apart; VSI thresholds need context-specific evaluation.
- Only applies to imaging platforms with usable z coordinates; on MERSCOPE z takes only a few discrete values.
- Validated only on mouse brain and liver; the authors note a systematic evaluation against emerging 3D/multimodal segmentation is still needed.
- It flags/removes problem regions rather than reconstructing purified expression; independent comparisons in both the resolVI and SPLIT papers find ovrlpy removes limited erroneous signal and substantially reduces gene counts.

## Relation to our direction
For **Plan A**, ovrlpy is itself an **unsupervised anomaly detector for technical artifacts**: the VSI map says "where the signal is untrustworthy", complementary to an anomaly map of "where disease is". Three uses: **(1) Negative-control channel** — in KidneyAnomalyBench, high-scoring anomaly regions that coincide with low-VSI regions (especially folds) should be classed as technical; "correlation between anomaly score and VSI" can be a diagnostic metric in the benchmark. **(2) Cross-modal agreement** — tissue folds are also visible on H&E, so low VSI + H&E fold = high-confidence artifact, one of the cleanest instances of Plan A's "cross-modal agreement separates artifacts from disease". **(3) Kidney-specific risk** — glomeruli (stacked podocytes, endothelium, mesangium), tightly packed tubules and peritubular capillaries are prime vertical-overlap structures (endothelial cells were doublet-prone in liver here); kidney Xenium carries z coordinates, so it can be run directly. **For virtual tissue / revert**: if a virtual-tissue model learns cell–neighbour relations partly from vertical doublets, perturbation predictions inherit fake co-localization; VSI can filter training data. For **Plan B**: "analysing 3D data as 2D without checking vertical doublets" is a concrete entry for the omics failure taxonomy, and ovrlpy is a QC tool an agent should proactively call on Xenium. Note that low VSI does not by itself identify the cause, so any "this region is an artifact" claim needs a composition check as evidence.

## Reusable assets
- **Code:** ovrlpy (PyPI / bioconda, `pip install ovrlpy`) and the paper-reproduction repo.
<https://github.com/HiDiHlabs/ovrl.py>
<https://github.com/HiDiHlabs/ovrlpy-publication>
<https://ovrlpy.readthedocs.io>
- **Preprint:** bioRxiv full text (CC BY).
<https://doi.org/10.1101/2025.01.13.632601>
- **Eval protocol:** independently annotate virtual top/bottom halves and measure agreement — a ground-truth-free segmentation-quality check reusable on kidney Xenium.

## Follow-ups
- Differences between the Nature Biotechnology version and the preprint; the group's segmentation-free SSAM / Sainsc methods.
- Combine with resolVI (`resolvi-natmethods-2026`) and SPLIT (`xenium-split-natmethods-2026`) on kidney data: remove overlaps/folds via VSI first, then correct in-plane spillover.

## Cite
```bibtex
@article{Tiesmeyer_2026, title={Identifying 3D signal overlaps in spatial transcriptomics data with ovrlpy}, ISSN={1546-1696}, url={http://dx.doi.org/10.1038/s41587-026-03004-8}, DOI={10.1038/s41587-026-03004-8}, journal={Nature Biotechnology}, publisher={Springer Science and Business Media LLC}, author={Tiesmeyer, Sebastian and Müller-Bötticher, Niklas and Malt, Alexander and Ma, Leyao and Marco-Salas, Sergio and Kiessling, Paul and Horn, Paul and Guillot, Adrien and Kuemmerle, Louis B. and Tacke, Frank and Theis, Fabian J. and Kuppe, Christoph and Nilsson, Mats and Eils, Roland and Long, Brian and Ishaque, Naveed}, year={2026}, month=Feb }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

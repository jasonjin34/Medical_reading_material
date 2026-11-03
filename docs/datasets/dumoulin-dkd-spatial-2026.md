# Dumoulin 2026 · Spatial atlas of diabetic kidney disease

> Imaging-based spatial data of DKD tissue: the spatial evidence for a hypothesis, and a 2026 result (a B-cell-rich DKD subgroup) that models with an earlier training cutoff cannot have seen.

**Species** human · **Assays** spatial · **Access** open

## At a glance

| | |
|---|---|
| Scale | 64 FFPE samples (CosMx 48, Xenium 16); about 3.39 million CosMx and 0.95 million Xenium cells after filtering |
| People / samples | 58 patients (paper; 57 distinct IDs in Diagnosis.xlsx): about 26 DKD, 12 controls (2 children), 9 with diabetes and/or hypertension without DKD, and single cases of FSGS, IgAN, MN, C3GN, TMA and CKD, plus 2 AA amyloid |
| Labels | cell types and spatial niches in the paper (whether the h5ad holds niche labels is not yet checked); diagnosis per sample |
| Licence | CC BY 4.0 (Zenodo); paper CC BY-NC-ND 4.0 |
| Paper | Dumoulin B et al. Nature 2026;653:1158–1169. doi:10.1038/s41586-026-10363-4 · [deep-read](../papers/dkd-spatial-atlas-nature-2026/index.md) |

## What was measured

CosMx (about 1,000 genes) and Xenium (5,100 genes; 656 shared with CosMx) on FFPE sections; the paper describes spatial niches that recur across patients and a B-cell-rich DKD subgroup.

## Known issues

- Shares patients (HK IDs) with Abedini 2024: HK2844, HK2924 (Abedini per-cell metadata) and HK2873, HK3035 (Abedini Visium file names) appear in both; 21 Dumoulin patients have non-HK IDs and cannot be checked. Never use the two as discovery and held-out cohort for each other.
- Gene panels of 1k / 5k genes, so a hypothesis about a gene outside the panel cannot be checked here.

## Download

| Format | File | Size | Link |
|---|---|---|---|
| `Zenodo` | record 19868428: annotated h5ad + diagnosis table | 8.75 GB | [↗](https://zenodo.org/records/19868428) |

Download not yet tested. The paper cites 10.5281/zenodo.18674907, an earlier version of the same record without files; 19868428 is the current version.

## Used in our research topics

- **[Verifiable Research Agents for Chronic Kidney Disease: A Rule-Engine Harness with Experts in the Loop](../research/hypothesis-agents.md)**: Spatial evidence for hypotheses about cell states and niches; 2026 claims as time-split items where a model's cutoff is earlier.

# Multiomic analysis of human kidney disease identifies a tractable inflammatory and pro-fibrotic tubular cell phenotype

> **Bibkey** `Reck_2025` · **Venue** Nature Communications (2025) · **Category** single-cell · **Relevance** medium · **Access** open
> **Link** <https://doi.org/10.1038/s41467-025-59997-4> · `status: complete`

---

## One-liner
Combining snRNA+snATAC multiome with CosMx high-plex single-cell spatial imaging (6,000- and 1,000-plex), the authors identify a **VCAM1+ICAM1+ inflammatory proximal-tubule (PT) cell** in human kidney disease: a subset of KPMP "adaptive PT" cells that expresses chemokines, pro-fibrotic and senescence-associated genes and localizes specifically to the fibrotic niche; it is epigenetically imprinted by **HNF4α-network collapse plus AP-1/NF-κB activation**; in mice the AP-1 inhibitor T5224 or the senolytic ABT-263 depletes these cells and reduces inflammation and fibrosis.

## Problem
Human kidney disease has a described VCAM1-expressing "adaptive" PT state, and mice have Havcr1+Vcam1+ "failed-repair" PT cells, but it was unclear (1) how failed repair relates to human disease, (2) where it sits spatially, and (3) which transcriptional programs drive it — hence whether it is a tractable target.

## Method
**Human atlas**: non-tumour poles of tumour nephrectomies — 5 patients with ureteric obstruction (UUO, from urothelial carcinoma) vs 7 renal-cell-carcinoma controls without obstruction; to limit batch effects, nuclei from 3–5 patients were pooled into 6 libraries for 10x Multiome and donors assigned by SNP deconvolution (98.68% donor agreement between RNA and ATAC libraries, validated by SNP arrays); cross-donor SNPs also catch doublets missed by standard thresholds. **Projection onto KPMP** validates clusters and confirms the inflammatory subset in other aetiologies. **Trajectory and cross-species**: RNA velocity + pseudotime; comparison with mouse IRI and reversible-UUO (R-UUO) time courses. **Senescence signature**: bulk RNA-seq of irradiation-induced senescent RPTECs. **Spatial**: CosMx 6,000-plex (5 UUO, 2 controls) and 1,000-plex (minimal change disease n=3, IgA nephropathy n=6, chronic pyelonephritis n=4); co-localization enrichment within 25 µm, transcript enrichment by distance from centroids, niche partitioning; multiplex IF (PanCK, VCAM1, ICAM1, FAP, CD68) for validation. **Regulation**: paired RNA/ATAC TF–CRE–target networks and motif footprinting; CUT&RUN for JUN and NF-κB1 in TNF-stimulated RPTECs. **Intervention**: daily gavage of T5224 10 mg/kg for 2 weeks starting day 3 after unilateral IRI in mice; the BCL2/w/xL inhibitor ABT-263 in the R-UUO model.

## Data
46,957 high-quality nuclei (59 clusters) from 12 patients (mean age 71); CosMx 6,000-plex and 1,000-plex (the latter 246,055 cells); public mouse IRI and R-UUO single-cell data; the KPMP snRNA atlas. All data on GEO: Multiome GSE254185, CosMx 6K GSE282059, CosMx 1K GSE253439, RPTEC bulk and CUT&RUN GSE252584/GSE254187; interactive cellxgene; Zenodo 15124887.

## Key results
- **State spectrum**: PT cells split into healthy (S1–S3), injured (HAVCR1+VCAM1+, matching KPMP adaptive PT) and inflammatory (additionally CCL2, CXCL1, TGM2, ICAM1, …); the inflammatory state is almost exclusive to obstructed kidneys and an ICAM1+ subset is also found within KPMP adaptive PT. In KPMP CKD patients, **inflammatory-PT proportion correlates closely with activated macrophages/myofibroblasts, whereas total adaptive proportion does not significantly**.
- **"Point of no return"**: RNA velocity suggests early injured cells may still revert to healthy, while more advanced cells flow only towards the inflammatory state; in mouse IRI and R-UUO, injured PT declines during recovery while inflammatory PT persists longer; inflammatory PT scores much higher on the irradiation-senescence signature.
- **Spatial localization**: both CosMx and multiplex IF show that only inflammatory PT (VCAM1+ICAM1+) co-localizes with monocytes, transitioning monocyte–macrophages, dendritic cells and myofibroblasts in the fibrotic niche, while injured PT is diffusely scattered; cell states rarely intermix within one tubule; ICAM1 sits on the luminal membrane of inflammatory PT and may tether myeloid cells in the urinary space. In biopsies (e.g. IgA nephropathy), inflammatory-PT proportion correlates positively with myofibroblasts, monocytes, cDCs and fibrosis severity and inversely with eGFR.
- **Signalling**: inflammatory PT is the main source of chemokine transcripts in the fibrotic niche (e.g. CCL2–CCR2) and expresses multiple ligands for PDGF, TGF and FGF receptors; it also up-regulates FAS, TWEAK and TNF/TRAIL receptors, suggesting bidirectional and autocrine feed-forward loops.
- **Regulation**: down-regulated PT function genes (CUBN, SLC34A1, …) are controlled by a TF module A led by HNF1α/HNF4α; HNF4α appears to be the master regulator and auto-regulates its own locus — sustained injury breaks this loop, causing irreversible loss of PT identity; in mouse IRI, HNF4α targets drop within 4 h and recover within 48 h in cells that recover, but stay low in inflammatory PT through 6 weeks. The inflammatory program is driven by AP-1 (motifs in ~20% of accessible CREs) and NF-κB1 (enriched in late CREs); CUT&RUN confirms JUN binding at CREs near CDKN1A, HDAC9, HAVCR1, VCAM1, ICAM1 and PDGFA.
- **Reversion**: T5224 attenuates post-IRI loss of kidney mass, inflammation (IBA1) and fibrosis (PSR), and lowers the KIM1+VCAM1+ inflammatory-PT fraction and Icam1, Vcam1, Pdgfa expression; ABT-263 in R-UUO markedly reduces inflammatory-PT genes and (by bulk deconvolution) the inflammatory-PT fraction.

## Contributions
- Translates the mouse "failed repair" concept to human disease and uses ICAM1 to separate it from the broader adaptive/injured PT (in humans VCAM1 marks both, ICAM1 is specific).
- Localizes the state to the fibrotic niche at single-cell spatial resolution and provides a biopsy-usable antibody panel (VCAM1/ICAM1).
- Goes the full way "state → TF program → pharmacological intervention": HNF4α collapse + AP-1/NF-κB, with AP-1 inhibition and senolysis effective in mice.
- A pooled Multiome design with SNP deconvolution that both reduces batch effects and detects cross-donor doublets.

## Limitations
- Human tissue is the non-tumour part of tumour nephrectomies with UUO as the injury paradigm; small n (5 vs 7), and controls have mild age-related glomerulosclerosis (mean age 71).
- The "point of no return" rests on RNA velocity and mouse time courses; there is no longitudinal human evidence, and the authors note early biopsies are needed to tell whether the inflammatory state initiates or follows leukocyte infiltration.
- Interventions are mouse-only and systemic, not cell-specific; ABT-263's effect on inflammatory-PT fraction comes from bulk deconvolution. VCAM1 specificity differs between mouse and human.
- snRNA-seq proportions are subject to dissociation bias (acknowledged), partly compensated by CosMx.

## Relation to our direction
This is the repo's **most complete kidney detect → model → revert exemplar**: **detect** — identify a disease-specific state departing from healthy PT (VCAM1+ICAM1+) in single-cell and spatial data; **model** — explain via TF–CRE networks why it is locked in (broken HNF4α auto-regulatory loop + AP-1/NF-κB); **revert** — pull it back in mice with an AP-1 inhibitor and a senolytic, reducing fibrosis. Concrete value for **the artifact-injection topic**: **(1) Expert-verifiable positives** — VCAM1+ICAM1+ inflammatory PT and the fibrotic niche are an ideal "genuine disease anomaly" class for KidneyAnomalyBench, with an IF antibody panel as an orthogonal protein-level check (cross-modal agreement); **(2) Anomalies should be graded** — "reversible injured PT" and "irreversible inflammatory PT" both depart from healthy but mean different things, so the benchmark should separate "degree of deviation" from "reversibility"; **(3) Artifact risk** — inflammatory PT sits right next to macrophages and myofibroblasts and is highly exposed to transcript spillover on Xenium/CosMx (see `xenium-split-natmethods-2026`, `resolvi-natmethods-2026`), making it the best test case for "does de-artifacting erase real anomalies?"; **(4) Data** — the 6K and 1K CosMx (incl. IgA-nephropathy biopsies) and Multiome data are all public, usable as an external validation set. For **revert**: HNF4α/AP-1 are explicit perturbation targets that a virtual tissue could simulate. For **the agent-trustworthiness topic**: claim strength varies — some backed by CUT&RUN and mouse intervention (AP-1), some purely correlational (KPMP proportion correlations), some inferred only (the RNA-velocity "point of no return") — ideal for building annotated examples of evidence-type grading in claim-to-evidence verification.

## Reusable assets
- **Code:** figure-reproduction scripts.
<https://github.com/mreck1/human_kidney_multiomics>
- **Data:** Multiome GSE254185; CosMx 6K GSE282059; CosMx 1K GSE253439; CUT&RUN GSE254187; RPTEC bulk GSE252584; cellxgene browser; Zenodo 15124887.
<https://cellxgene.cziscience.com/e/867757c1-3b1a-49d9-a0cd-17767eb160cc.cxg>
- **Marker panel:** VCAM1+ICAM1− (injured) vs VCAM1+ICAM1+ (inflammatory) PT, plus the shared injury signature PROM1, DCDC2, SPP1, ITGB6, ITGB8.

## Follow-ups
- The adaptive/maladaptive PT definitions in the KPMP / Lake human kidney atlas (`lake-kidney-atlas-nature-2023`), to align terminology.
- The original mouse failed-repair PT work (Kirita et al., Gerhardt et al.), and whether the same state appears across aetiologies (DKD, `dkd-spatial-atlas-nature-2026`).

## Cite
```bibtex
@article{Reck_2025, title={Multiomic analysis of human kidney disease identifies a tractable inflammatory and pro-fibrotic tubular cell phenotype}, volume={16}, ISSN={2041-1723}, url={http://dx.doi.org/10.1038/s41467-025-59997-4}, DOI={10.1038/s41467-025-59997-4}, number={1}, journal={Nature Communications}, publisher={Springer Science and Business Media LLC}, author={Reck, Maximilian and Baird, David P. and Veizades, Stefan and Sutherland, Callum and Bell, Rachel M. B. and Hur, Heeyoun and Cairns, Carolynn and Janas, Piotr P. and Campbell, Ross and Nam, Andy and Yang, Wei and Schurman, Nathan and Williams, Claire and O’Sullivan, Eoin and Beniazza, Meryam and Corsinotti, Andrea and Bellamy, Christopher and Hughes, Jeremy and Laird, Alexander and Denby, Laura and Chandra, Tamir and Ferenbach, David A. and Conway, Bryan R.}, year={2025}, month=May }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

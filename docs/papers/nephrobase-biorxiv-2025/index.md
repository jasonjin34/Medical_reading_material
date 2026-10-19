# Nephrobase Cell+: Multimodal Single-Cell Foundation Model for Decoding Kidney Biology

> **Bibkey** `Li_2025_Nephrobase` · **Venue** bioRxiv (2025) · **Category** foundation · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1101/2025.09.30.679471> · `status: complete`

---

## One-liner
The Susztak lab pretrains from scratch the first kidney-specific single-cell foundation model, Nephrobase Cell+ (1B and 500M variants): ~39.5M cells/nuclei, 4,319 samples, four species (human, mouse, rat, pig), scRNA / snRNA / snATAC / CosMx / Xenium, ~100B tokens; an encoder-decoder transformer with MoE and adversarial batch removal. On held-out human (KPMP 2025 Q2) and mouse kidney data it beats Geneformer, scGPT, UCE, PCA and an autoencoder on clustering, batch integration, cross-species alignment and "zero-shot" annotation.

## Problem
General single-cell foundation models abound, but there is no kidney-specific model, and it is unclear whether organ-focused models beat generalist ones. The kidney's complex architecture and dynamic microenvironments make large-scale single-cell + spatial integration hard: batch effects, cross-modality variation and cross-species generalisation (long-standing issues for atlases like KPMP).

## Method
**Input/encoding**: a cell×gene matrix; each gene token combines identity, normalised expression (sum-log normalisation) and optional metadata/perturbation, embedded via cross-attention; a fixed 32,768 orthologous-gene feature space. **Architecture**: encoder self-attention, decoder cross-attention; RMSNorm; sparse top-k Mixture-of-Experts (with a shared expert and load-balancing loss). **Objectives**: masked generative pretraining with a ZINB reconstruction head; a focal-loss classification head (effective-number class weights, missing labels skipped); Elastic Cell Similarity regulariser (prevents embedding collapse, target cosine threshold e.g. 0.5); supervised contrastive loss (pulls same-label cells together); domain/assay adversarial discriminators with gradient reversal (assay weight ramps up over epochs). **Note**: training uses cell-type labels (supervised contrastive + classification head), so the paper's "zero-shot annotation" means applying the trained head to held-out data without further fine-tuning — not zero-shot in the unsupervised sense. **Perturbation**: sample 5,000 cells, double a target gene's expression, rank predicted DE genes and run GSEA.

## Data
Pretraining corpus: 4,319 samples, ~39.5M profiles — human 25.2M, mouse 12.5M, rat 1.4M, pig 0.293M; ~30M from kidney tissue, ~10M immune/peripheral (incl. PBMCs from healthy and CKD donors); also fetal kidney and organoids. Assays: scRNA ~48.7%, snRNA ~25.4%, CosMx ~7.7%, snATAC ~6.2%, Xenium ~5.5%. Cell types dominated by PT (27.4%), T cells (19.1%), endothelium (8.8%). Sources: GEO, SRA, HCA, CELLxGENE, KPMP plus substantial in-house data (CosMx ~3M, Xenium ~2M, sn/sc/snATAC ~3M). Evaluation: held-out KPMP 2025 Q2 human kidney data, a mouse developmental dataset, and a mixed human–mouse kidney dataset. In v1 the GEO accession for the in-house data is still a placeholder (***).

## Key results
- **Human kidney (held-out KPMP)**: KMeans ARI 0.82 for 1B (scGPT 0.40, autoencoder 0.55, Geneformer 0.22), NMI 0.78 (scGPT 0.48), silhouette ~0.68; cLISI 1.00, iLISI ~0.17–0.18, kBET 0.25–0.28 (scGPT 0.09); total integration score 0.71 (1B) / 0.70 (500M), highest of all methods.
- **Mouse**: ARI ~0.70, cLISI 1.0, total 0.69–0.68, above UCE, PCA, scGPT.
- **Cross-species**: 500M NMI 0.75 / ARI 0.72 (Geneformer 0.44/0.22, scGPT 0.62/0.43); 1B NMI 0.73 / ARI 0.57; iLISI 0.01, graph connectivity and PCR ~0.94; total 0.63 (500M) / 0.61 (1B) vs Geneformer 0.50, UCE 0.51 — the smaller 500M model is slightly better cross-species.
- **Annotation**: >90% correct for major lineages (e.g. PT) in human and mouse, errors mostly between related subtypes (distal vs connecting tubule); comparison against simpler methods is "not shown".
- **In silico perturbation**: doubling CCL2 and VCAM1 enriches immune adhesion/chemotaxis; GDF15 growth control and MAPK; SOX4 kidney morphogenesis and oxidative phosphorylation — qualitative GO results only, no experimental or baseline validation.

## Contributions
- The first kidney-specific single-cell foundation model spanning four species and five assays, up to 1B parameters.
- Combines ZINB reconstruction, MoE, supervised contrastive learning, ECS and adversarial batch removal in one encoder-decoder.
- Gives a direct comparison against generalist foundation models on held-out KPMP data, a first answer to "organ-specific vs generalist".

## Limitations
- Preprint, not peer reviewed; no public code/weights link found and the in-house GEO accession is a placeholder — not currently reproducible.
- **Evaluation caveats**: training uses cell-type labels and supervised contrastive loss, so the "zero-shot" annotation and clustering advantages partly reflect supervision and are not fully comparable to unsupervised zero-shot embeddings from Geneformer/scGPT; the paper reads low iLISI as "minimal batch separation" and kBET as "lower is better", which departs from usual scib conventions — readers should verify.
- Missing strong conventional baselines like HVG + scVI/Harmony (only PCA and an autoencoder); annotation comparison against simpler methods "not shown".
- The perturbation experiment is a qualitative "double expression + GSEA" demo with no linear/additive baseline or experimental validation; the authors concede correlation only.
- Fixed 32,768-gene space; proteomics/imaging not included; heavy training cost limits retraining by typical labs.

## Relation to our direction
This is Plan A's most direct "model-layer" candidate: same organ, same snRNA + snATAC + Xenium (+ CosMx), with KPMP and CKD samples in the corpus — if weights become available, its embeddings are a ready backbone for building a "healthy kidney manifold" and scoring anomalies on it, and its adversarial batch removal targets exactly our multicentre, multi-protocol batch problem. But three things must be verified in Plan A rather than taken on trust: **(1) batch removal may overshoot** — adversarially removing assay signal also erases real states visible only in some assays (`kidney-multimodal-genomebiol-2026` shows WFDC2⁺ aTAL and Norn are protocol-specific), which is precisely the signal anomaly detection must keep; **(2) supervised training pulls embeddings toward known cell types**, so novel/intermediate disease states may be absorbed into the nearest known class, lowering anomaly detectability — test with KidneyAnomalyBench's known-positive states; **(3) HVG/scVI baselines and a true zero-shot protocol must be added** (see `scfm-zeroshot-genomebiol-2025`). For the revert stage, its "double expression + GSEA" perturbation is exactly the baseline-free perturbation claim criticised by `linear-baselines-natmethods-2025`. For Plan B, the paper is a ready claim-to-evidence exercise: claims like "far surpassing all existing models" and ">90% zero-shot accuracy" versus their evidence (supervised training, missing baselines, metric interpretation) show gaps a verifier should systematically flag.

## Reusable assets
- **Code/weights**: no public link found in the v1 full text (watch later versions or contact the Susztak lab).
- **Public kidney GEO accessions listed**: GSE107585, GSE182256, GSE183842, GSE173343, GSE211785, GSE209821, GSE183839, GSE291551 — external data sources for Plan A.
- **Method components**: ECS anti-collapse regulariser, assay adversary + gradient reversal, ZINB reconstruction — individually borrowable.

## Follow-ups
- Whether later versions / the published version add code, HVG/scVI baselines and a true zero-shot evaluation.
- The Susztak lab's kidney spatial-microenvironment work (the four glomerular/immune/tubular/fibrotic microenvironments cited; possibly `dkd-spatial-atlas-nature-2026` or related entries in this repo).
- The KPMP 2025 Q2 data release as an external test-set candidate for KidneyAnomalyBench.

## Cite
```bibtex
@article{Li_2025_Nephrobase, title={Nephrobase Cell+: Multimodal Single-Cell Foundation Model for Decoding Kidney Biology}, url={http://dx.doi.org/10.1101/2025.09.30.679471}, DOI={10.1101/2025.09.30.679471}, publisher={openRxiv}, author={Li, Chenyu and Ziyadeh, Elias and Sharma, Yash and Dumoulin, Bernhard and Levinsohn, Jonathan and Ha, Eunji and Pan, Siyu and Rao, Vishwanatha and Subramaniyam, Madhav and Szegedy, Mario and Zhang, Nancy and Susztak, Katalin}, year={2025}, month=Oct }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

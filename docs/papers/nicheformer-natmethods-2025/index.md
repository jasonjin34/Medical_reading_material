# Nicheformer: a foundation model for single-cell and spatial omics

> **Bibkey** `Tejada_Lapuerta_2025` · **Venue** Nature Methods (2025) · **Category** foundation · **Relevance** medium · **Access** open
> **Link** <https://doi.org/10.1038/s41592-025-02814-z> · `status: complete`

---

## One-liner
Nicheformer is a 49.3M-parameter transformer foundation model pretrained on SpatialCorpus-110M (57.06M dissociated + 53.8M image-based spatial cells, human and mouse, 73 tissues) with ranked gene tokens plus species/modality/technology context tokens. On newly designed spatial tasks (niche/region labels, neighbourhood composition, neighbourhood density) both linear probing and fine-tuning beat Geneformer, scGPT, UCE, CellPLM, scVI and PCA, and it transfers spatial context onto scRNA-seq.

## Problem
Existing single-cell foundation models train on dissociated data only and ignore spatial relationships (CellPLM is an exception, but small and not fine-tuned on spatial tasks). Image-based spatial transcriptomics is now large enough to learn from at scale; can a spatially aware cell representation be learned and transferred to the vast body of non-spatial scRNA-seq?

## Method
**Representation**: 20,310 gene tokens from human–mouse orthologues plus species-specific genes (16,981 orthologous, 151 mouse-specific, 3,178 human-specific); each cell becomes a token sequence ranked relative to the technology-specific non-zero mean in the corpus (Geneformer-style rank encoding), with separate means for dissociated, MERFISH, Xenium, CosMx and ISS to counter technology bias; plus species, modality and technology context tokens. **Architecture**: context 1,500, 12 encoder layers, 16 heads, FFN 1,024, 512-d embedding, 49.3M parameters; pretrained on (masked) cell reconstruction. Pretraining uses **no spatial coordinates**, expression only. **Downstream**: linear probing (frozen embedding + linear head) and fine-tuning; tasks include niche/region classification (with uncertainty), fixed-radius neighbourhood composition (on average 10/20/50/100 neighbours) and density regression, and spatial→dissociated label transfer. Also attention analysis (layer specialisation; sex-dimorphic gene attention in the MERFISH mouse-brain AVPV) and pretraining-data ablations (dissociated-only, human-only, mouse-only).

## Data
SpatialCorpus-110M: the dissociated part builds on CELLxGENE Census (33.47M) plus 180 added datasets (GEO, sfaira, HCA) from 6,000+ donors; the spatial part covers MERFISH, Xenium, CosMx and ISS across 15 tissues, 158 individuals and 10,600+ sections — brain 60.46% (32.1M), lung 9.95%; 55.23% unannotated; 64.07% healthy, 31.98% cancer. Datasets are not integrated; raw inputs are kept. Downstream: MERFISH mouse brain (17 regions, 8 niches), CosMx human liver and lung, Xenium human lung and colon (healthy vs adenocarcinoma), mouse motor-cortex scRNA-seq.

## Key results
- **Pretraining ablations**: dissociated-only pretraining (even 3× the spatial data volume) is significantly worse on spatial tasks; single-species models do poorly on the other species — at equal cell counts, data diversity is what matters (ANOVA, FDR-significant).
- **Niche/region labels**: on held-out MERFISH mouse-brain sections, fine-tuned Nicheformer has the best macro F1; but PCA with many components roughly matches Nicheformer linear probing and even beats it on region prediction. On CosMx liver, linear probing trails scVI/PCA (liver is rare in the corpus), improving with extended pretraining.
- **Spatial→dissociated transfer**: correctly selects the 9 motor-cortex cell types out of 33 MERFISH types with low overall uncertainty; some deep-layer glutamatergic neurons are misassigned.
- **Neighbourhood composition**: across brain, liver and lung at four scales, fine-tuned Nicheformer has systematically lowest MAE; Nicheformer linear probing is next, beating Geneformer, scGPT, UCE, CellPLM, scVI and PCA. Error tracks cell-type abundance and regional specificity (rare, regionally diverse midbrain/hypothalamic types are worst). At large radii in liver, scVI trained on a corpus subset matches fine-tuned Nicheformer.
- **Neighbourhood density**: cancer sections have higher mean neighbourhood density in Xenium (colon 12.3 vs 10.7; lung 12.1 vs 10.7); scVI and PCA linear probing give negative R², while Nicheformer is better on MAE and R² and localises dense tumour regions.

## Contributions
- The first single-cell foundation model jointly pretrained on large-scale dissociated + image-based spatial data, with the public SpatialCorpus-110M.
- A new set of spatially aware downstream tasks (niche/region labels, neighbourhood composition and density) as a benchmark.
- Shows dissociated data alone cannot capture spatial variation; technology-specific rank normalisation handles platform bias.

## Limitations
- Performance depends on cell/tissue abundance in the corpus; the corpus is brain-dominated (60%), and **kidney** is not among the evaluated tissues.
- Pretraining does not use spatial coordinates or neighbour graphs; metadata tokens are excluded from the final embedding, possibly limiting expressivity.
- PCA / scVI are strong competitors on some tasks (at the linear-probing level); the authors concede their task set is not comprehensive.
- Interpretability (attention analysis) is preliminary.

## Relation to our direction
For the **model** stage of detect → model → revert, Nicheformer offers a way to put a cell and its neighbourhood in one representation. In a multi-modal design of this kind (snRNA + snATAC + Xenium + H&E), snRNA/snATAC are dissociated and only Xenium is spatial; Nicheformer's spatial→dissociated transfer could in principle infer the niche/neighbourhood composition of snRNA cells, letting us define spatial-level anomalies (e.g. immune-infiltrated neighbourhoods around injured tubules) even in samples without spatial measurements. Two concrete uses for the artifact-injection topic anomaly detection: **(1) neighbourhood composition/density prediction error is itself an anomaly signal** — if the neighbourhood predicted from a cell's expression disagrees with its measured (Xenium) neighbourhood, that is an expression–space cross-modal disagreement; **(2) technology-specific rank normalisation** directly addresses Xenium-vs-snRNA platform bias, complementing the protocol-effect findings in `kidney-multimodal-genomebiol-2026`. Caveats: the corpus is brain-dominated and kidney-poor; the authors already see linear probing trail scVI/PCA on liver, so kidney likely needs extended pretraining; and PCA is a strong baseline on several tasks — consistent with `scfm-zeroshot-genomebiol-2025`, PCA/scVI must be in any evaluation. For the agent-trustworthiness topic, inferential spatial claims like "Nicheformer places this snRNA cell in niche X" should carry uncertainty (the paper provides classification uncertainty) — a good calibration test case for the verifier.

## Reusable assets
- **Code and model:**
<https://github.com/theislab/nicheformer>
- **Data-processing code:**
<https://github.com/theislab/nicheformer-data>
- **SpatialCorpus-110M:**
<https://huggingface.co/datasets/theislab/SpatialCorpus-110M>
- **Spatial downstream task definitions**: fixed-radius neighbourhood composition/density, niche/region labels + uncertainty — directly portable to kidney Xenium.

## Follow-ups
- CellPLM (the other single-cell foundation model using spatial data).
- The spatial anomaly-detection baseline STANDS (`spatial-natcommun-2024`) — could Nicheformer embeddings replace its features?
- Xenium segmentation/artefact work (`xenium-split-natmethods-2026`, `ovrlpy-natbiotech-2026`) — neighbourhood computation is sensitive to segmentation errors.

## Cite
```bibtex
@article{Tejada_Lapuerta_2025, title={Nicheformer: a foundation model for single-cell and spatial omics}, volume={22}, ISSN={1548-7105}, url={http://dx.doi.org/10.1038/s41592-025-02814-z}, DOI={10.1038/s41592-025-02814-z}, number={12}, journal={Nature Methods}, publisher={Springer Science and Business Media LLC}, author={Tejada-Lapuerta, Alejandro and Schaar, Anna C. and Gutgesell, Robert and Palla, Giovanni and Halle, Lennard and Minaeva, Mariia and Vornholz, Larsen and Dony, Leander and Drummer, Francesca and Richter, Till and Bahrami, Mojtaba and Theis, Fabian J.}, year={2025}, month=Oct, pages={2525–2538} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

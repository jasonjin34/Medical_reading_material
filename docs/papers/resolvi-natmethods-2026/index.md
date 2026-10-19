# ResolVI: addressing noise and bias in spatial transcriptomics

> **Bibkey** `Ergen_2026` · **Venue** Nature Methods (2026) · **Category** spatial · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1038/s41592-026-03212-9> · `status: complete`

---

## One-liner
resolVI is a VAE-based generative model in scvi-tools that sits **downstream of any segmentation algorithm** and decomposes each cell's observed counts into three parts — the cell's true expression, expression "diffused" in from neighbouring cells, and a per-slice constant non-specific background — removing spurious co-expression caused by molecule misassignment while producing a batch-corrected probabilistic latent representation that supports differential expression and differential niche-abundance testing.

## Problem
Subcellular-resolution spatial transcriptomics (Xenium, MERSCOPE, CosMx, Stereo-seq, Visium HD) requires **segmentation + quantification** before any cell-level analysis: partition the plane into cell-like regions and count the molecules inside each. Even with transcript-aware segmenters such as Baysor and ProSeg, molecules still land in the wrong cell — because of high cell density, weak staining, irregular shapes, RNA leakage from tissue handling, and **cell overlap along the poorly resolved z axis**. The result is spurious cross-lineage marker co-expression (e.g. microglia "expressing" neuronal markers), which confines analyses to a priori-defined cell classes and hampers the discovery of new cell states.

## Method
**Input**: a cell × gene count matrix from any segmentation/quantification, cell coordinates, and slice ID. **Generative model**: observed counts x_ng ~ Poisson(l_n · h_ng), with h_ng = Gamma(true expression α0·f_θ(z_n,b) + diffusion α1·Σ β_nN(n)·f_θ(z_N(n),b)) + background α2·bg_sg. True and diffused expression are negative binomial (Gamma-Poisson); background is assumed non-overdispersed and Poisson. The per-cell proportions α_n are MAP-estimated by a "diffusion encoder" under a Dirichlet prior; per-neighbour contributions β (20 neighbours by default) get a Dirichlet prior shaped by an RBF kernel on Euclidean distance, so nearer cells are likelier sources of misassignment; the background prior is set to the mean of the lowest-expressed 10% of genes (which the authors found approximates negative-control probe counts on CosMx). **Latent space**: a mixture-of-Gaussians prior instead of a unimodal Gaussian, which separates cell types better and allows semi-supervised training with known labels plus a classifier head. **Batch**: the decoder sees batch ID; the encoder does not by default. **Intuition**: the VAE bottleneck assumes a low-dimensional description; misassigned molecules make observed profiles "more complex", so minimizing the ELBO pushes "unrelated" molecules into the diffusion or background components. **Training details**: cells with <20 molecules are filtered; low-count cells are augmented by multinomial resampling; scArches-style network surgery maps query data; downstream, model-based lvm-DE differential expression and a two-sided Bayesian differential niche-abundance test are provided.

## Data
All public data: **10x Xenium mouse brain** (248 genes, ~130k cells, original nucleus segmentation + dilation; also Baysor, ProSeg, nucleus-only); **two Vizgen MERSCOPE liver-cancer biopsies** (~1.5M cells, 550 genes, six segmentations compared: original, three Cellpose settings, Baysor, ProSeg); **Stereo-seq mouse coronal brain** (>24,000 genes, >50k cells); **10x Visium HD mouse brain** (8-µm bins, 453,820 spots, 17,797 genes); **NanoString CosMx healthy vs cancerous liver** (1,000 genes, 1.2M cells, re-segmented with Baysor); **DSS-colitis MERFISH time course** (990 genes, 52 slices, 1.4M cells; days 0/3/9/21/35). References: sc/snRNA-seq (Linnarsson mouse brain, healthy liver single-nucleus atlas).

## Key results
- **Xenium mouse brain**: the resolVI latent space beats PCA, scVI and scANVI on scib-metrics bioconservation and on "integration" between low- and high-misassignment cells (α1+α2 > 20% used as a pseudo-batch); false-positive neuronal Slc17a6 in hypothalamic microglia is largely removed while Trem2 is kept; literature-supported endothelial Lyz2 co-expression absent from the scRNA reference is **preserved**. resolVI's estimated spurious fraction rises with the marker-based false double-positive rate, although it never sees marker knowledge.
- **Segmentation dependence**: expression-aware segmentation (Baysor, ProSeg) lowers false double positives but leaves residue; resolVI reduces it further after every segmentation. The authors report that ovrlpy and ProSeg's own correction "fail to remove a majority of erroneous signals". On liver-cancer MERSCOPE, Baysor + resolVI performed best, yet the Discussion **recommends ProSeg in practice**, since Baysor inflates cell counts with many low-molecule cells.
- **Sequencing-based ST**: on Stereo-seq with all genes it runs in <20 min and <30 GB; the fraction of Slc17a7+ cells that are also Mbp+ falls from **14.8% to <0.01%**; on Visium HD 8-µm bins it trains in 20 min and resolves VIP, SST and NPY inhibitory subsets.
- **CosMx liver cancer**: after background removal, cholangiocyte markers (SOX4, KRT13, EPCAM) return to a periportal pattern; tumour SPP1–CD68 co-expression is **retained** after correction (tumour-associated macrophages genuinely express SPP1); hotspot reveals two tumour-cell spatial modules — a hypoxic immunosuppressive region (MIF, ENO1, SPP1, VEGFA) and an interferon pro-inflammatory region (MX1, IFI6, STAT1) — matched by co-localizing macrophage, neutrophil and T-cell subsets.
- **DSS colitis (1.4M cells, <6 h training on an RTX 3090)**: day 35 is described as "almost fully recovered", yet resolVI's differential niche analysis shows crypt-tip fibroblasts (Fibro 2) relocating from between crypts into submucosal aggregates with reduced Bmp2/5/7, alongside lower barrier-gene expression (Cldn4, Cldn23, Tnfaip3, Il22ra1) outside colonocyte-dense regions — i.e. **the tissue has not truly returned to baseline after macroscopic recovery**.

## Contributions
- Models molecule misassignment explicitly as estimable diffusion + background components, decoupled from segmentation so it plugs in after any segmenter.
- **Every cell gets a misassignment fraction α1+α2** — a "technical-artifact score" that needs no marker knowledge yet tracks the false double-positive rate.
- One generative model handles denoising, batch correction, semi-supervised annotation, query mapping, differential expression and differential niche abundance.
- Validated across imaging- and sequencing-based platforms (six technologies) and scales to millions of cells.

## Limitations
- **Correction quality depends on the initial segmentation** (stated by the authors); residual fibroblast–myeloid/endothelial co-expression remains with the original segmentation.
- Relies on the VAE bottleneck and is sensitive to the latent-space choice; the authors suggest the supervised mode as mitigation.
- The "erroneous co-expression" benchmark is built from literature markers and scRNA co-expression; the authors admit these gene pairs are **highly context-dependent** and real data lack ground truth.
- Comparisons to other tools are run by the authors; an independent comparison by another group (Bilous et al., `xenium-split-natmethods-2026` in this repo) finds resolVI substantially reduces detected genes, leaves near-empty cells, sometimes slightly worsens iLISI, and occasionally suppresses both contaminating and genuine T-cell programs.
- No kidney data; data for some figures are available only on reasonable request.

## Relation to our direction
This is the de-artifacting layer that must precede **detect**. For **Plan A** (anomaly detection on kidney Xenium + snRNA/snATAC + H&E) the most immediate risk is that "anomalous cells" found on Xenium are just segmentation/diffusion artifacts — e.g. a proximal-tubule cell "expressing" CD68 because it abuts an infiltrating macrophage. resolVI's per-cell **α1+α2** is exactly a disease-agnostic **technical-artifact covariate**: (1) usable in KidneyAnomalyBench as a weak label or stratifier for an "artifact" class, testing whether an anomaly score merely tracks α; (2) combinable with the snRNA reference and H&E morphology for **cross-modal agreement** — high anomaly + high α + co-expression absent in snRNA → likely artifact; high anomaly + low α + snRNA/snATAC support → disease candidate. **A tension to watch**: genuine kidney-disease states (e.g. the chemokine/ICAM1-expressing inflammatory PT cells of `inflammatory-pt-natcommun-2025`, sitting next to macrophages) are themselves "mixed-looking" phenotypes located in immune-dense fibrotic niches — over-correction could erase real anomalies. So resolVI belongs in a **controlled comparison** (run anomaly detection before and after correction, keep the anomalies that are stable), not as silent default preprocessing. The DSS-colitis result also informs **revert**: "macroscopic recovery" is not "niche recovery", so reversion should be judged on neighbourhood composition, not only cell proportions. For **Plan B**: whether misassignment correction was applied, and with which segmentation, directly changes co-expression claims; an agent that analyses spatial omics without declaring this step exhibits a concrete omics-specific failure mode, and VAE stochasticity makes it a natural target for rerun-stability checks.

## Reusable assets
- **Code:** resolVI ships in scvi-tools; reproducibility code and a Zenodo archive.
<https://github.com/scverse/scvi-tools>
<https://github.com/YosefLab/resolvi-reproducibility>
<https://doi.org/10.5281/zenodo.19811112>
- **Data:** processed data for Figs. 2 and 5 (Dryad); the DSS-colitis MERFISH data (Dryad).
<https://doi.org/10.5061/dryad.z08kprrqd>
<https://doi.org/10.5061/dryad.rjdfn2zh3>
- **Eval protocol:** define mutually exclusive marker pairs from a single-cell reference and compute false double-positive rates — directly portable to kidney (define exclusive pairs from KPMP/Lake atlases).

## Follow-ups
- ProSeg (Jones et al.) and Baysor — the recommended initial segmenters; ovrlpy (`ovrlpy-natbiotech-2026`) and SPLIT (`xenium-split-natmethods-2026`) — two other answers to the same problem whose conclusions conflict, worth re-comparing ourselves on kidney data.
- Mitchel et al. on misassignment-induced spurious cell–cell communication; the lvm-DE differential-expression framework.

## Cite
```bibtex
@article{Ergen_2026, title={ResolVI: addressing noise and bias in spatial transcriptomics}, volume={23}, ISSN={1548-7105}, url={http://dx.doi.org/10.1038/s41592-026-03212-9}, DOI={10.1038/s41592-026-03212-9}, number={10}, journal={Nature Methods}, publisher={Springer Science and Business Media LLC}, author={Ergen, Can and Yosef, Nir}, year={2026}, month=Sept, pages={2003–2014} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

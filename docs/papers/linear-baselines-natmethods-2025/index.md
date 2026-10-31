# Deep-learning-based gene perturbation effect prediction does not yet outperform simple linear baselines

> **Bibkey** `Ahlmann_Eltze_2025` · **Venue** Nature Methods (2025) · **Category** foundation · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1038/s41592-025-02772-6> · `status: complete`

---

## One-liner
For predicting transcriptomic effects of double perturbations and of unseen single perturbations, none of scGPT, scFoundation, GEARS, CPA, or scBERT / Geneformer / UCE with a linear decoder consistently beats "additive", "no change", "mean" or a simple bilinear model; the only consistent winner is a linear model whose perturbation embedding is pretrained on **perturbation data from another cell line**.

## Problem
Single-cell foundation models such as scGPT and scFoundation claim to predict expression changes caused by genetic perturbations, including unseen ones — the core selling point of the "virtual cell" narrative. But their original comparisons may have been "easy" (CPA was never designed for unseen perturbations; the linear model in scGPT's benchmark effectively reverted to "no change"). Under a fair setup, do they actually beat deliberately simple baselines?

## Method
**Task 1: double perturbations.** Norman et al. K562 CRISPRa (100 single genes, 124 pairs; log expression for 19,264 genes); fine-tune on all singles + 62 doubles, test on the other 62 doubles, five random splits. Baselines: "no change" (predict control) and "additive" (sum of single-perturbation LFCs, using no double data). Error = L2 distance over the top 1,000 expressed genes; also Pearson delta etc. **Genetic interactions**: doubles deviating from the additive expectation beyond a Normal null (5,035 at 5% FDR out of ~124,000), classed as buffering, synergistic or opposite; TPR–FDP curves over thresholds D on each model's 310,000 predictions. **Task 2: unseen single perturbations.** Replogle K562, Replogle RPE1 (CRISPRi) and Adamson K562. Baselines: training-set mean b, and a bilinear model Y ≈ G W Pᵀ + b (G gene embedding, P perturbation embedding — from dimensionality reduction of training data or external sources: scGPT/scFoundation gene embeddings, GEARS perturbation embedding, or a perturbation embedding from the other cell line's Replogle data). Default parameters where possible; fine-tuning capped at 3 days (scFoundation trained for five epochs).

## Data
Norman et al. (K562 CRISPRa, doubles), Replogle et al. (K562 and RPE1 CRISPRi), Adamson et al. (K562 CRISPRi) — the datasets used in the GEARS / scGPT / scFoundation papers; all cancer cell lines.

## Key results
- **Doubles**: every deep model has prediction error **substantially higher than the additive baseline**; same conclusion under Pearson delta and other gene subsets.
- **Genetic interactions**: no model beats "no change"; models predict mostly buffering, rarely synergy, and correct synergy even more rarely. For HBG2/HBZ — strong individual effects — all models except Geneformer and scFoundation predict LFC ≈ 0. scGPT, UCE and scBERT predictions barely vary across perturbations for most genes; GEARS and scFoundation vary far less than ground truth.
- **Unseen singles**: no deep model consistently beats the mean baseline or the linear model (scFoundation could not run on Adamson/Replogle because its gene set must match pretraining exactly; CPA not applicable). Plugging scGPT/scFoundation gene embeddings or GEARS perturbation embeddings into the linear model matches or beats their own decoders, but does not consistently beat the linear model with G, P from the training data.
- **The only consistent winner**: a linear model with P pretrained on the other cell line's Replogle data (K562↔RPE1), more accurate for genes more similar between the lines — pretraining on **perturbation data** helps, while pretraining on single-cell atlases gives only a small benefit over random embeddings. Deep models cost far more compute to fine-tune.

## Contributions
- A fair comparison against deliberately simple baselines, on the original authors' own datasets, showing progress in perturbation prediction has been overstated.
- The bilinear G W Pᵀ framework accepts any gene/perturbation embedding, isolating whether the pretrained representation itself is useful.
- An operational definition of genetic interaction with buffering / synergistic / opposite classes, now a common benchmark lens.

## Limitations
- Only four datasets, all cancer cell lines (K562, RPE1); no tissue or primary cells.
- Original QC not improved (e.g. perturbations that failed to change their own target were not removed).
- 3-day fine-tuning cap and default parameters — more tuning might narrow the gap (the authors do not claim deep models can never work).
- Evaluation focuses on pseudobulk mean expression, not single-cell distributional shifts.

## Relation to our direction
This is the key "cold water" for the **revert** stage: we envision predicting, inside a virtual tissue, which gene perturbations would pull an anomaly back to normal — and this paper shows that even on the cleanest cell-line Perturb-seq, foundation models fail to beat additive/mean baselines. Concrete implications: **(1) any reversion prediction must report additive / no-change / mean / linear baselines**, or model contribution is unidentifiable; **(2) if pretraining, prefer perturbation data (e.g. Replogle, Virtual Cell Challenge data) over atlases alone**; **(3) reversion is essentially predicting the reverse LFC, and models systematically underestimate effect magnitude (predictions barely vary across perturbations), which would reduce a "which perturbation best reverts" ranking to noise** — evaluate magnitude and ranking, not just correlation. For the artifact-injection topic, it warns that the downstream value of anomaly detection cannot be self-certified by "bolting on a foundation model for reversion." For the agent-trustworthiness topic, it addresses one of the most common untrustworthy agent claims ("scGPT predicts knocking out X reverses the phenotype") with an executable check: have the verifier automatically compare against linear/additive baselines — a "missing baseline" category for the omics-specific failure taxonomy.

## Reusable assets
- **Code and intermediate results** (model run scripts, Zenodo archive):
<https://github.com/const-ae/linear_perturbation_prediction-Paper>
- **Baseline suite**: no change, additive, mean, bilinear G W Pᵀ (pluggable external embeddings).
- **Data**: Norman 2019, Replogle 2022, Adamson 2016 (public).

## Follow-ups
- The Kernfeld et al. and Csendes et al. "mean baseline" preprints and the subsequent perturbation benchmarks.
- Whether the Virtual Cell Challenge (`virtual-cell-challenge`) evaluation absorbs these baselines.
- Zero-shot evaluation (`scfm-zeroshot-genomebiol-2025`) — the same "foundation models vs simple methods" evidence.

## Cite
```bibtex
@article{Ahlmann_Eltze_2025, title={Deep-learning-based gene perturbation effect prediction does not yet outperform simple linear baselines}, volume={22}, ISSN={1548-7105}, url={http://dx.doi.org/10.1038/s41592-025-02772-6}, DOI={10.1038/s41592-025-02772-6}, number={8}, journal={Nature Methods}, publisher={Springer Science and Business Media LLC}, author={Ahlmann-Eltze, Constantin and Huber, Wolfgang and Anders, Simon}, year={2025}, month=Aug, pages={1657–1661} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

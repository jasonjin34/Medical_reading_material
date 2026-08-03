# An ECG biomarker for sudden cardiac death discovered with deep learning

> **Bibkey** `Obermeyer_2026` · **Venue** Nature (2026) · **Category** imaging · **Relevance** high · **Access** paywall
> **Link** <https://doi.org/10.1038/s41586-026-10674-6> · `status: complete`

---

## One-liner
Deep learning discovers a previously undescribed, visually identifiable ECG biomarker that robustly predicts sudden cardiac death (SCD), and a paired generative model renders the learned waveform morphology visible.

## Problem
SCD is preventable with defibrillators, yet the only widely used predictor, left ventricular ejection fraction (LVEF), misses most SCDs while flagging many low-risk patients for futile ICDs that never fire. A better, more sensitive and specific risk biomarker is urgently needed.

## Method
A deep-learning model is trained on raw ECG waveforms to predict SCD risk. For interpretability, the discriminative model is paired with a generative model of the ECG waveform, so the morphology the predictor relies on can be synthesized and visualized — turning a black-box signal into an eye-readable biomarker. Its shape is then tied to electrophysiological first principles to form and preliminarily test a mechanistic hypothesis. Exact architecture/training details are behind the paywall (abstract-only).

## Data
Discovery cohort: all ECGs in a Swedish region linked to death certificates (high-risk group = 2.2% of sample; reduced-LVEF group = 1.9%). External validation: (1) a US health system (labels = ventricular arrhythmias causing sudden death), and (2) a Taiwanese hospital registry (labels = future arrhythmic cardiac arrests). Modality: standard ECG waveforms (exact lead count in the full text; abstract-only).

## Key results

- The model's high-risk group (2.2% of sample) has a 7.0% annual SCD rate, exceeding the reduced-LVEF group (1.9% of sample; 4.6% annual rate).
- 86.1% of the model's high-risk patients were NOT flagged by LVEF — highly complementary to the current standard.
- High-risk patients who received ICDs were 54.4% less likely to die than expected, suggesting a mortality benefit (observational).
- External validation predicts ventricular arrhythmias (US) and future arrhythmic cardiac arrests (Taiwan).
- The generative pairing reveals a previously undescribed, visually identifiable, robust waveform biomarker.

## Contributions
- A discriminative+generative pairing that turns a learned latent morphology into an eye-readable, clinically communicable new biomarker rather than an opaque risk score.
- The discovered biomarker is highly complementary to LVEF (86.1% non-overlap), filling a screening gap.
- Cross-country (Sweden, US, Taiwan), multi-endpoint external validation.
- Moves from data-driven discovery back to electrophysiological first principles, proposing a testable mechanistic hypothesis.

## Limitations
- The ICD mortality benefit is observational and subject to confounding/selection bias, not RCT evidence.
- The mechanistic hypothesis is only preliminarily tested.
- Architecture, training/ablations, and full metrics (AUC/calibration) are paywalled (abstract-only).

## Relation to our direction
PI flags this as super relevant; the methodological link is the **anomaly-detection stage**. The paper is a clean template for "use deep learning to discover a previously unknown disease-associated anomaly in a medical signal, then make it explicit/visible with a generative model" — structurally the same as our stage-1 goal of detecting disease/drug-perturbed regions in biomedical images or spatial-omics, just swapping a 1D ECG waveform for 2D/spatial-omics tensors. Transferable ideas: (1) **discriminative+generative pairing** to invert what the predictor relies on into an interpretable anomaly prototype / counterfactual — directly relevant to our virtual-tissue counterfactual synthesis; (2) a **complementarity metric vs. an existing marker** (86.1% non-overlap) as an eval protocol for whether a discovered anomaly adds signal beyond known biomarkers; (3) **discovery → mechanistic hypothesis** mirrors our "predict the key genes whose modulation would revert the anomaly (wet-lab validated)" downstream. It does not touch the virtual-tissue or gene-revert stages, but is a strong cross-modality exemplar of anomaly detection plus generative counterfactual explanation.

## Reusable assets
Reusable at the concept level: the discriminative+generative interpretability framework, the "complementarity-to-existing-marker" eval protocol, and the cross-country multi-endpoint validation design. Code/checkpoint/data availability must be checked in the paper's availability statements (abstract-only). Datasets are restricted linked health records (Swedish ECG–death-certificate linkage, US health system, Taiwanese registry) and are typically not public. DOI: 10.1038/s41586-026-10674-6.

## Follow-ups
- Get full text + Methods for the discriminative architecture and the generative model type (VAE/diffusion/GAN?) and the inversion procedure.
- Check availability statements for reusable interpretability/counterfactual code.
- Read full metrics (AUC, calibration, competing-risks) and the causal analysis of ICD benefit.

## Figures & tables

_Paywall (Nature): the entries below only link to the publicly visible figure-caption titles on nature.com; no images are downloaded or reproduced. Numbers are public abstract values, marked abstract-only._

**Fig 1** (paywalled): Positive predictive value for sudden cardiac death. See <https://www.nature.com/articles/s41586-026-10674-6/figures/1>

**Fig 2** (paywalled): Incidence of ventricular arrhythmia in the high-risk group versus the threshold for defining the high-risk group. See <https://www.nature.com/articles/s41586-026-10674-6/figures/2>

**Fig 3** (paywalled): Overlap of the high-risk ECG group and the reduced LVEF group in Swedish data. See <https://www.nature.com/articles/s41586-026-10674-6/figures/3>

**Fig 4** (paywalled): Low-risk versus high-risk ECG waveform morphs. See <https://www.nature.com/articles/s41586-026-10674-6/figures/4>

**Fig 5** (paywalled): A biomarker identified in the ECGs of high-risk patients. See <https://www.nature.com/articles/s41586-026-10674-6/figures/5>

### Results

**Table 1.** (abstract-only) Sample share and annual sudden-cardiac-death (SCD) rate for the model's high-risk ECG group vs. the reduced-LVEF group; figures are from the public abstract, full metrics (AUC/calibration) are paywalled.

| Group | Share of sample | Annual SCD rate |
|---|---|---|
| Model high-risk ECG | 2.2% | 7.0% |
| Reduced LVEF | 1.9% | 4.6% |

Additional public numbers (abstract-only): **86.1%** of high-risk patients were not flagged by LVEF; high-risk patients with an implanted defibrillator were **54.4%** less likely to die than expected.

_Source: https://www.nature.com/articles/s41586-026-10674-6  ·  Nature 655 (2026) 210–218 · paywalled; abstract-only._

## Cite
```bibtex
@article{Obermeyer_2026, title={An ECG biomarker for sudden cardiac death discovered with deep learning}, volume={655}, ISSN={1476-4687}, url={http://dx.doi.org/10.1038/s41586-026-10674-6}, DOI={10.1038/s41586-026-10674-6}, number={8121}, journal={Nature}, publisher={Springer Science and Business Media LLC}, author={Obermeyer, Ziad and Schubert, Alexander and Ross, James and Mullainathan, Sendhil and Lingman, Markus}, year={2026}, month=June, pages={210–218} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

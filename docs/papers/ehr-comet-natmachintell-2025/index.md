# A machine learning approach to leveraging electronic health records for enhanced omics analysis

> **Bibkey** `Mataraso_2025` · **Venue** Nature Machine Intelligence (2025) · **Category** ehr · **Relevance** medium · **Access** open
> **Link** <https://doi.org/10.1038/s42256-024-00974-9> · `status: complete`

---

## One-liner
COMET (Aghaeepour lab, Stanford): omics studies often have tens to hundreds of samples while the same hospital's EHR covers tens of thousands — pretrain a GRU on the large EHR-only cohort, transfer its weights into a multimodal EHR + omics network that blends early and late fusion, and both prediction and the biological plausibility of selected proteins improve, in a 61-person pregnancy proteomics cohort and a 559-person UK Biobank cancer proteomics cohort.

## Problem
Omics is high-dimensional but cohort size is capped by clinical and budget constraints, hurting replication; in ML, false positives show up as overfitting. Existing remedies (feature priors, transfer learning, deep Cox) mostly learn from the omics or metadata alone. EHRs are increasingly available (MIMIC, UK Biobank, OMOP-standardized hospital databases), but EHR–omics integration has a structural tension: early/intermediate fusion needs both modalities complete (dropping the many EHR-only patients), while late fusion cannot learn cross-modal interactions. The question: how to use **many EHR-only patients** to improve modelling and biological discovery in a **small omics cohort**?

## Method
**EHR embedding**: concept codes from OMOP measurement, observation, drug_exposure, condition_occurrence and procedure_occurrence tables; codes from one patient-day form a "sentence" (shuffled, since many timestamps are unreliable); word2vec learns 400-d embeddings, averaged per day into a summary embedding, using up to the 32 most recent days. **Pretraining**: a GRU-RNN trained on EHR-only patients (pretraining cohort) to predict the same outcome (pregnancy: days to labour from a random point in the last 100 days; cancer: 3-year mortality from the first C-prefixed ICD code). **Multimodal architecture**: three branches — EHR (frozen pretrained GRU + linear), omics (linear; one-hidden-layer MLP for cancer), joint (linear on concatenated EHR latent + omics) — combined by a final bias-free linear layer: an **adaptive blend of early and late fusion**. MSE and BCE losses respectively. **Comparators**: EHR-only, omics-only, and a joint baseline identical to COMET minus pretraining; ridge/logistic regression (including variants using pretrained coefficients as priors β₀); a COMET Transformer variant. 25 random splits (70/15/15) per experiment, averaging validation predictions. **Mechanism analyses**: number of EHR-latent–protein correlations, Integrated-Gradients protein importance, external validation of important proteins, intermediate-node performance, function-space t-SNE trajectories.

## Data
**Pregnancy cohort (Stanford)**: 30,904 people delivering at Stanford 2013–2021 (STARR OMOP); **61** of them (171 plasma samples, 2–3 draws in the last 100 days) have aptamer-based proteomics (1,317 proteins; 1,305 after removing 12 controls), the other 30,843 form the pretraining cohort; metabolomics from the same cohort as a second omics test. **Cancer cohort (UK Biobank)**: 36,901 people diagnosed with any cancer from 12 months before to 5 years after enrolment; **559** have enrolment-blood proteomics within 12 months after diagnosis (UKB proteomics covers 53,058 participants, median 2,894 proteins), the other 36,342 form the pretraining cohort; 3-year mortality 5.5%. External validation uses public pregnancy and breast-cancer proteomics datasets.

## Key results
- **Days to labour**: COMET Pearson r = **0.868** (95% CI 0.825–0.900, RMSE 16.0 days); joint baseline 0.815 (18.4 days); proteomics-only 0.796; EHR-only 0.768. Metabolomics: COMET 0.839 vs metabolites alone 0.758.
- **3-year cancer mortality**: COMET AUROC **0.842** (0.744–0.922), AUPRC **0.504**; joint baseline 0.786 / 0.365; EHR-only 0.749 / 0.205; proteomics-only 0.737 / 0.325.
- **Pretraining helps linear models too**: adding pretrained priors raises ridge joint r from 0.572 to 0.799; the Transformer variant reaches r = 0.848, slightly below the GRU COMET.
- **EHR–protein alignment**: significant EHR-latent–protein correlations rise from 3,201 to **5,364** (pregnancy) and from 0 to **7,591** (cancer). COMET's most correlated proteins (IL1RL1/ST2, cystatin C, plexin-B2) are known pregnancy-progression players.
- **External validation**: proteins COMET weights more have mean |r| = 0.22 with time to labour in an external dataset vs 0.12 for baseline-favoured proteins (p = 0.0276); in cancer, 9/18 vs 8/18 are significantly associated with mortality.
- **Mechanism**: lower test loss at matched training loss, and function-space trajectories separate from the baseline — the authors call it "regularization by initialization".

## Contributions
- To the authors' knowledge, the **first approach using EHR transfer learning to improve omics analysis**.
- Resolves the "many EHR, few omics" asymmetry: pretraining uses all EHR patients while the multimodal stage still learns cross-modal interactions.
- Evaluates biological consistency, not just predictive performance: EHR-latent–protein alignment and external validation of important proteins.
- The pretraining benefit holds across architectures (GRU, Transformer, ridge, logistic).

## Limitations
- Very small omics cohorts (61 / 559) with wide CIs (cancer AUROC 0.744–0.922); external validation is indirect (correlation of important proteins), and the cancer gap of 9/18 vs 8/18 is small.
- Validated only on tabular omics (proteomics, metabolomics); the authors explicitly state it is **unknown whether it helps modalities needing complex architectures (e.g. spatial transcriptomics)**.
- Pretraining needs labelled EHR tasks (the same as the target); self-supervised pretraining is future work.
- Coarse EHR representation: word2vec with daily means, within-day codes shuffled, only the last 32 days; OMOP mappings may contain errors.

## Relation to our direction
Among the five papers the PI sent, this is **the only one linking EHR to molecular data**, making it the most direct bridge between the Sinai EHR project and the lab's omics/tissue work. The setting matches exactly: Sinai has EHR for millions but omics or biopsies for only a small subset (e.g. kidney biopsies, BioMe biobank samples) — COMET's "pretrain on large EHR → transfer to small omics cohort" is the standard move under this asymmetry. **For cardiometabolic-kidney disease**: swap pregnancy/cancer for CKD progression or DKD and the EHR pretraining task for eGFR decline or dialysis initiation, and you have a design directly reproducible at Sinai; if the lab's Novo-funded cardiometabolic-kidney foundation models must align EHR patient representations with molecular data, this paper gives the minimal viable evaluation (latent–molecule correlation counts, external validation of important features). **For Plan A**: the authors list spatial transcriptomics as an open question — and Plan A is exactly kidney snRNA/snATAC/Xenium + H&E. A natural extension is to use EHR-pretrained patient representations as **sample-level covariates/priors** that help separate "clinically abnormal" from "technical artefact", complementing Plan A's cross-modal-agreement idea (the clinical modality becomes one more independent line of evidence). **On detect → model → revert**: COMET links patient-scale clinical trajectories to molecular features — an interface prototype from EHR-level detect towards molecular-level model/revert — but it remains correlational (an important protein is not an actionable target).

## Reusable assets
- **Code:** full COMET code (including UK Biobank cohort-extraction queries and a tutorial); Zenodo 10.5281/zenodo.13977341.
<https://github.com/samson920/COMET>
- **Data:** pregnancy proteomics on Dryad (10.5061/dryad.280gb5mpd); Stanford EHR not shareable; UK Biobank part via application.
- **Eval design:** a joint baseline (same architecture, no pretraining) as the clean ablation; EHR-latent–molecule correlation counts; external validation of important features.

## Follow-ups
- The work cited as showing EHR foundation models can directly predict protein expression levels (ref. 36) — directly relevant to replacing labelled pretraining with self-supervision.
- Replace COMET's GRU pretraining with a Delphi/APOLLO-style self-supervised patient representation and test whether small-omics-cohort gains grow.
- Search for existing EHR + kidney biopsy/omics integration work (whether KPMP has linkable clinical trajectories).

## Cite
```bibtex
@article{Mataraso_2025, title={A machine learning approach to leveraging electronic health records for enhanced omics analysis}, volume={7}, ISSN={2522-5839}, url={http://dx.doi.org/10.1038/s42256-024-00974-9}, DOI={10.1038/s42256-024-00974-9}, number={2}, journal={Nature Machine Intelligence}, publisher={Springer Science and Business Media LLC}, author={Mataraso, Samson J. and Espinosa, Camilo A. and Seong, David and Reincke, S. Momsen and Berson, Eloise and Reiss, Jonathan D. and Kim, Yeasul and Ghanem, Marc and Shu, Chi-Hung and James, Tomin and Tan, Yuqi and Shome, Sayane and Stelzer, Ina A. and Feyaerts, Dorien and Wong, Ronald J. and Shaw, Gary M. and Angst, Martin S. and Gaudilliere, Brice and Stevenson, David K. and Aghaeepour, Nima}, year={2025}, month=Jan, pages={293–306} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

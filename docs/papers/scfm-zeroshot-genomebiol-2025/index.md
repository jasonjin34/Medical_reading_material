# Zero-shot evaluation reveals limitations of single-cell foundation models

> **Bibkey** `Kedzierska_2025` · **Venue** Genome Biology (2025) · **Category** foundation · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1186/s13059-025-03574-x> · `status: complete`

---

## One-liner
Using scGPT and Geneformer cell embeddings zero-shot — no fine-tuning — for cell-type clustering and batch integration, both generally underperform simply selecting HVGs, Harmony and scVI across five datasets; they even struggle at their own pretraining task (masked expression reconstruction) — scGPT without cell embeddings does worse than predicting the mean.

## Problem
Single-cell foundation models mostly prove their value through fine-tuned performance, yet many single-cell tasks are exploratory with no predefined labels, so embeddings must be used zero-shot. Protein-LM experience shows fine-tuning gains can stem from trivial mechanisms unrelated to pretraining. So: does pretraining actually learn transferable biology?

## Method
Evaluates Geneformer and scGPT (four scGPT variants: random init, kidney 814k cells, blood 10.3M, human 33M). Baselines: HVG, Harmony, scVI. **Tasks**: (1) cell-type clustering — AvgBIO, ASW; (2) batch integration — scib batch scores, PCR etc., in full and reduced dimensions; (3) pretraining-task reconstruction — scGPT bin-value prediction (GEP, and GEPC conditioned on the cell embedding), Geneformer gene-rank prediction, vs naive mean / average-rank baselines. Overlap between evaluation and pretraining data is checked. Code and Docker image public.

## Data
Five datasets: Pancreas (16k, five sources, partially overlapping Geneformer pretraining), two PBMC datasets (incl. PBMC 12k), a cross-tissue Immune atlas (330k) and the multi-organ Tabula Sapiens — the last two were in scGPT's pretraining set. The authors regard this as the most favourable setting (tissues and technologies close to pretraining).

## Key results
- **Cell-type clustering**: by AvgBIO, Geneformer and scGPT both trail HVG, Harmony and scVI; scGPT wins only on PBMC 12k; **HVG beats both on every metric**. No consistent advantage even on datasets seen in pretraining.
- **Pretraining scale**: pretraining helps over random init (notably PBMC), but scGPT human (33M) slightly underperforms scGPT blood (10.3M), even on non-blood tissues — bigger, more diverse data does not necessarily help.
- **Batch integration**: Geneformer ranks last on almost every dataset and metric, with more variance explained by batch in its embeddings than in the raw data; scGPT trails scVI/Harmony on technical-batch-only Pancreas/PBMC and wins on Tabula Sapiens/Immune with donor-level variation (both seen in pretraining). HVG ranks best in full dimensions.
- **Pretraining task**: without cell embeddings scGPT predicts the mean input bin, with MSE worse than a naive mean baseline and only marginally better with embeddings; Geneformer's predicted vs true ranking has median correlation 0.56 (best 0.95), and it sometimes predicts genes absent from the input.

## Contributions
- Establishes zero-shot evaluation as a necessary test for single-cell foundation models and shows it exposes problems fine-tuning hides.
- Diagnoses the pretraining objective itself, questioning MLM's suitability for learning cell embeddings.
- Calls for held-out evaluation sets never used for pretraining (as with LLMs).

## Limitations
- Only two models and five transcriptomic datasets; newer models (e.g. protein-informed gene representations) not covered.
- Some evaluation data appear in pretraining, confounding generalisation vs memorisation.
- scGPT variants confound data size with tissue composition.
- Does not cover perturbation prediction, gene regulation or other downstream tasks.

## Relation to our direction
For Plan A, anomaly detection is inherently zero-shot — we have no anomaly labels and must measure deviation in an embedding space defined by healthy references. This paper says directly that **using off-the-shelf single-cell foundation-model embeddings as the "normal manifold" for kidney omics is risky**: HVG + scVI/Harmony are often better, and Geneformer embeddings carry even more batch variance than raw data — in our multicentre, multi-protocol 95-biopsy setting, "outliers" in foundation-model embeddings may well be batch, not disease. Practical rule: KidneyAnomalyBench must include HVG-PCA and scVI as strong anomaly-scoring baselines and, like this paper, report batch scores (does batch drive the anomaly score?). Notably scGPT has a **kidney variant pretrained on only 814k kidney cells**, a direct comparator for kidney-specific foundation models (see also Nephrobase Cell+). For Plan B, "foundation-model embeddings beat traditional methods" is a common unverified agent claim; the paper gives the verifier an executable protocol (zero-shot + HVG baseline + pretraining-overlap check), and "evaluation data leaked into pretraining" is a data-leakage pattern worth adding to the failure taxonomy.

## Reusable assets
- **Code** (MIT):
<https://github.com/microsoft/zero-shot-scfoundation>
- **Docker environment**: DockerHub `kzkedzierska/sc_foundation_evals`.
- **Protocol**: scib v1.0.4 metrics (AvgBIO, ASW, batch, PCR) in full and reduced dimensions; pretraining-task reconstruction vs mean baseline.

## Follow-ups
- Linear-baseline comparison for perturbation prediction (`linear-baselines-natmethods-2025`).
- Whether the kidney-specific Nephrobase Cell+ (`nephrobase-biorxiv-2025`) runs zero-shot + HVG/scVI comparisons.
- Zero-shot evaluation of newer models such as UCE and scFoundation.

## Cite
```bibtex
@article{Kedzierska_2025, title={Zero-shot evaluation reveals limitations of single-cell foundation models}, volume={26}, ISSN={1474-760X}, url={http://dx.doi.org/10.1186/s13059-025-03574-x}, DOI={10.1186/s13059-025-03574-x}, number={1}, journal={Genome Biology}, publisher={Springer Science and Business Media LLC}, author={Kedzierska, Kasia Z. and Crawford, Lorin and Amini, Ava P. and Lu, Alex X.}, year={2025}, month=Apr }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**

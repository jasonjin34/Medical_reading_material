<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# A foundation model for clinical-grade computational pathology and rare cancers detection

- **Authors:** Vorontsov, Eugene; Bozkurt, Alican; Casson, Adam; Shaikovski, George; Zelechowski, Michal; Severson, Kristen; Zimmermann, Eric; Hall, James; Tenenholtz, Neil; Fusi, Nicolo; Yang, Ellen; Mathieu, Philippe; van Eck, Alexander; Lee, Donghun; Viret, Julian; Robert, Eric; Wang, Yi Kan; Kunz, Jeremy D.; Lee, Matthew C. H.; Bernhard, Jan H.; Godrich, Ran A.; Oakley, Gerard; Millar, Ewan; Hanna, Matthew; Wen, Hannah; Retamero, Juan A.; Moye, William A.; Yousfi, Razik; Kanan, Christopher; Klimstra, David S.; Rothrock, Brandon; Liu, Siqi; Fuchs, Thomas J.
- **Venue / Year:** Nature Medicine · 2024
- **DOI:** 10.1038/s41591-024-03141-0
- **URL:** https://doi.org/10.1038/s41591-024-03141-0
- **Bibkey:** Vorontsov_2024
- **Status:** complete

## Abstract
AbstractThe analysis of histopathology images with artificial intelligence aims to enable clinical decision support systems and precision medicine. The success of such applications depends on the ability to model the diverse patterns observed in pathology images. To this end, we present Virchow, the largest foundation model for computational pathology to date. In addition to the evaluation of biomarker prediction and cell identification, we demonstrate that a large foundation model enables pan-cancer detection, achieving 0.95 specimen-level area under the (receiver operating characteristic) curve across nine common and seven rare cancers. Furthermore, we show that with less training data, the pan-cancer detector built on Virchow can achieve similar performance to tissue-specific clinical-grade models in production and outperform them on some rare variants of cancer. Virchow’s performance gains highlight the value of a foundation model and open possibilities for many high-impact applications with limited amounts of labeled training data.

## Full text / Extract
<!-- Full cleaned text for open-access; for paywalled leave the note below. -->
> status: abstract-only — full text behind paywall (Nature Medicine). Drop `source.pdf` into this folder and re-run extraction to enrich. The main-text body, per-cancer AUC breakdowns, figures, and methods detail are not publicly available. Below is public, non-paywalled information from the Hugging Face model card (`paige-ai/Virchow`) and the article landing page, provided as context — not the article body.

### Public model card / landing summary (not the paywalled body)

**What it is.** Virchow is a self-supervised vision transformer used as a tile-level feature extractor (frozen backbone or finetuned) for computational pathology. Developed by Paige (New York) and Microsoft Research (Cambridge, MA).

**Architecture.**
- Variant: ViT-H/14 (Vision Transformer-Huge, 14×14 patch size)
- Parameters: 632 million
- Layers: 32; Embedding dimension: 1,280; Attention heads: 16
- Activation: SwiGLU; LayerScale enabled
- Pretraining objective: DINOv2 self-supervised, fp16 mixed precision

**Training data.**
- ~1.5 million whole-slide images (WSIs), H&E
- Source: Memorial Sloan Kettering Cancer Center
- Resolution: 0.5 microns per pixel (20× magnification)

**Input / output.**
- Input tile: 224 × 224 pixels
- Output: 257 tokens (1 class token + 256 patch tokens), 1,280 dimensions per token
- Recommended embedding: 2,560-dim vector = concatenation of class token and mean-pooled patch tokens
- Dense patch tokens available for segmentation

**Usage.** Loadable via the `timm` library; outputs embeddings for downstream classification/aggregation heads.

**Reported evaluation (from abstract).** Pan-cancer detection reaches 0.95 specimen-level ROC-AUC across 9 common and 7 rare cancers. A Virchow-based detector trained on less data matches production tissue-specific clinical-grade models and outperforms them on some rare cancer variants. Additional tasks evaluated: biomarker prediction and cell identification.

**License / links.** Model card lists Apache-2.0 (gated access on Hugging Face; verify actual terms before commercial use, as Paige Virchow weights have historically carried research/non-commercial gating). Successor model: `paige-ai/Virchow2`. Paper: https://www.nature.com/articles/s41591-024-03141-0

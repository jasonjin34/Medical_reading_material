<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# Boehringer-Ingelheim/anomaly-detection-in-histology

- **Authors:** Igor Zingman, Birgit Stierstorfer, Charlotte Lempp, Fabian Heinemann (repo: Boehringer Ingelheim)
- **Venue / Year:** GitHub · 2022 (companion paper: Medical Image Analysis 2024)
- **DOI:** 10.1016/j.media.2023.103067 · arXiv:2210.07675
- **URL:** https://github.com/Boehringer-Ingelheim/anomaly-detection-in-histology
- **Bibkey:** histo-anomaly-bi-repo
- **Status:** complete
- **License:** MIT

## Abstract
Learning image representations for anomaly detection: application to discovery of histological alterations in drug development. The system detects anomalies in histopathological whole-slide images in a setting where abnormal (lesion) samples are scarce. A CNN is trained on an auxiliary task that distinguishes healthy tissue by species, organs, and staining reagents — labels obtained automatically from sample metadata — combined with a center-loss regularization that produces compact representations. One-class classifiers on these features then flag deviations from normal. Applied to early-stage toxicity assessment of candidate drugs.

## Full text / Extract

### Overview
PyTorch implementation for detecting anomalies in histopathological whole-slide images. It learns image representations from healthy tissue to identify abnormal tissue alterations during drug-development screening. Companion code for Zingman et al., "Learning image representations for anomaly detection," Medical Image Analysis, 2024 (arXiv:2210.07675).

### What the code does
Trains CNNs to recognize normal tissue patterns, then uses the learned features with one-class classifiers to detect deviations that indicate adverse drug reactions or pathological changes in histological samples.

### Methods and models implemented
- CNN architecture: EfficientNet-B0 with 320-pixel input resolution.
- Representation learning: auxiliary classification task discriminating healthy tissue by species / organ / staining reagent (labels auto-derived from metadata), regularized with a center-loss term to enforce compact per-class representations.
- Anomaly detection: one-class SVM classifiers applied to deep features from the trained CNN.
- Staining support: both H&E and Masson's Trichrome protocols.

### Inputs and outputs
- Inputs: histopathological tissue images from whole-slide scans.
- Outputs: trained CNN models (.pt files); one-class SVM classifiers (.pkl files); anomaly detection results with visualization; evaluation metrics (balanced accuracy, AU-ROC, F1).

### Usage
1. Download datasets from the OSF repository: https://osf.io/gqutd/
2. Configure staining type in `configs/cfg_training_cnn.py`.
3. Train: `python train_cnn.py --config configs/cfg_training_cnn.py`
4. Evaluate: `python anomaly_detector.py --config configs/cfg_anomaly_detector.py`
5. Feature-extraction example: `model_use_example.py`

### Datasets
- Training: normal tissue from multiple species, organs, and staining types.
- Evaluation: normal mouse liver and NAFLD (non-alcoholic fatty liver disease) pathology samples — a published liver-anomaly dataset.

### Performance metrics
| Staining | Balanced Accuracy | AU-ROC | F1 Score |
|----------|-------------------|--------|----------|
| H&E | 94.20% | 97.33% | 94.09% |
| Masson's Trichrome | 97.51% | 99.03% | 97.51% |

The paper reports the method outperforms established anomaly-detection baselines and achieves results comparable to conventional methods specifically tailored for quantification of liver anomalies.

### Requirements
Python 3.9+, PyTorch, NumPy, Pillow, scikit-learn. ~11 GB GPU recommended.

### Citation
Zingman, I., Stierstorfer, B., Lempp, C., Heinemann, F. "Learning image representations for anomaly detection: application to discovery of histological alterations in drug development." Medical Image Analysis, Vol. 92, 2024, 103067. DOI: 10.1016/j.media.2023.103067. Preprint: arXiv:2210.07675.

### License
MIT License.

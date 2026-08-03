<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# Cassie07/PathOmics

- **Authors:** Kexin Ding, Mu Zhou, Dimitris N. Metaxas, Shaoting Zhang (paper authors)
- **Venue / Year:** GitHub · 2023 (paper: MICCAI 2023, Oral, top 9%)
- **DOI:** paper link https://rdcu.be/dnwKf
- **URL:** https://github.com/Cassie07/PathOmics
- **Bibkey:** pathomics-repo
- **Status:** complete

## Abstract
[MICCAI 2023 Oral] The official code of "Pathology-and-genomics Multimodal Transformer for Survival Outcome Prediction" (top 9%).

## Full text / Extract

### PathOmics: Pathology-and-genomics Multimodal Transformer for Survival Outcome Prediction

The official code of "Pathology-and-genomics Multimodal Transformer for Survival Outcome Prediction" (Accepted to MICCAI 2023, top 9%).

Our Paper: https://rdcu.be/dnwKf

[2025.12 New Update] The repo maintains an updated paper list of pathology-and-genomics multimodal analysis approaches in healthcare at the end of the repo.

### Workflow overview of the PathOmics
Workflow overview of the pathology-and-genomics multimodal transformer (PathOmics) for survival prediction. In (a), the pipeline extracts image and genomics feature embeddings via an unsupervised pretraining towards multimodal data fusion. In (b) and (c), the supervised finetuning scheme flexibly handles multiple types of data for prognostic prediction. With the multimodal pretrained model backbones, both multi- or single-modal data can be applicable for model fine-tuning.

### Citation
```
@inproceedings{ding2023pathology,
  title={Pathology-and-genomics multimodal transformer for survival outcome prediction},
  author={Ding, Kexin and Zhou, Mu and Metaxas, Dimitris N and Zhang, Shaoting},
  booktitle={International Conference on Medical Image Computing and Computer-Assisted Intervention},
  pages={622--631},
  year={2023},
  organization={Springer}
}
```

### Prerequisites
```
python 3.8.18
Pytorch 2.0.1
pytorch-cuda 11.8
Torchvision 0.15.2
Pillow 9.4.0
numpy 1.24.3
pandas 2.0.3
scikit-survival 0.21.0
scikit-learn 1.2.0
h5py 2.8.0
```

### Usage

#### Data preprocessing
```
1. Download WSIs from TCGA-COAD and TCGA-READ.
2. Download genomics data from CbioPortal and move the downloaded folder into "PathOmics" folder.
   * "coadread_tcga_pan_can_atlas_2018" in bash_main.py and bash_main_read.py is the downloaded folder; download it before running the code.
3. Split WSIs into patches and only keep the foreground patches.
4. Extract patch features via pretrained models (e.g., ImageNet-pretrained ResNet50, ResNet101, etc).
5. Save patch features as .npz files. (For each slide, one .npz file saves patch features.)
```
For more details about extracting features, see Issue 1 and the code in split_tiles_utils/helper.py.

#### Run code on TCGA-COAD only
Model is pretrained and finetuned on the TCGA-COAD training set (4-fold cross-validation). The finetuned model is evaluated on the TCGA-COAD hold-out set.
```
python bash_main.py --pretrain_loss 'MSE' --save_model_folder_name 'reproduce_experiments' --experiment_folder_name 'COAD_reproduce' --omic_modal 'miRNA' --kfold_split_seed 42 --pretrain_epochs 25 --finetune_epochs 25 --model_type 'PathOmics' --model_fusion_type 'concat' --model_pretrain_fusion_type 'concat' --cuda_device '2' --experiment_id '1' --use_GAP_in_pretrain_flag --seperate_test
```

#### Run code on TCGA-COAD and TCGA-READ
Model is pretrained on TCGA-COAD (5-fold cross-validation), then finetuned, validated, and evaluated on the TCGA-READ dataset (transfer).
```
python bash_main_read.py --k_fold 5 --fusion_mode 'concat' --prev_fusion_mode 'concat' --pretrain_loss 'MSE' --save_model_folder_name 'reproduce_experiments' --experiment_folder_name 'READ_reproduce' --omic_modal 'miRNA' --kfold_split_seed 42 --pretrain_epochs 25 --finetune_epochs 25 --model_type 'PathOmics' --cuda_device '2' --experiment_id '1' --use_GAP_in_pretrain_flag
```
To use TCGA-COAD pretrain weights and skip the pretraining stage, add `--load_model_finetune` (and set the pretrain-weights directory correctly).

#### Data-efficient mode in finetuning
Add `--less_data` and set `--finetune_test_ratio` to the preferred ratio of data used for model finetuning.

### Literature reviews of pathology-and-genomics multimodal analysis approaches in healthcare
The repo maintains a curated table (45+ entries, 2019–2025) of pathology-genomics multimodal survival/prognosis methods, including: PORPOISE (Cancer Cell 2022), MCAT (ICCV 2021), PathomicFusion (TMI 2020), SurvPath (CVPR 2024), TANGLE / Transcriptomics-guided slide representation (CVPR 2024), MOTCat (ICCV 2023), CMTA (ICCV 2023), MoME (MICCAI 2024), POMP (IJCAI 2025), and others — each with paper and code links where available.

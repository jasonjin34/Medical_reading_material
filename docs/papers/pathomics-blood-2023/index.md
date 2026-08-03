# A Deep Learning-Based Pathomics Methodology for Quantifying and Characterizing Nucleated Cells in the Bone Marrow Microenvironment

> **Bibkey** `pathomics-blood-2023` · **Venue** Blood, ASH 2023 Abstract 2294 (2023) · **Category** pathology · **Relevance** medium · **Access** abstract-only
> **Link** <https://ashpublications.org/blood/article/142/Supplement%201/2294/499845>
> `status: complete` — 会议摘要,无全文正文;以下基于公开摘要撰写。若日后有海报 PDF,放入本文件夹 `source.pdf` 后可补全。

---

## 一句话 / One-liner
A deep-learning pathomics pipeline that segments nucleated cells, fat cells, and evaluable hematopoietic regions on bone-marrow whole-slide images and extracts nuclear shape/texture/color features, enabling objective, scalable, region-resolved characterization of the MPN bone-marrow microenvironment.

## 研究问题 / Problem
Overall BM cellularity is a WHO criterion for distinguishing BCR-ABL- MPNs (e.g. PV vs. MF), yet manual hematopathologist assessment is subjective, not scalable, and records only a single global measure — discarding intra-marrow regional heterogeneity.

## 方法 / Method
Deep learning plus classical image analysis segments nucleated cells, fat cells, and other evaluable hematopoietic regions on BM WSIs; shape, texture, and color features are then extracted from segmented nuclei to feed interpretable downstream analytics. Presented as a pilot / proof-of-concept pipeline. (Network architecture, segmentation model, and feature dimensionality are not disclosed — abstract-only.)

## 数据 / Data
Bone-marrow biopsy WSIs from BCR-ABL- MPNs (PV, MF, etc.). A pilot cohort, with planned scale-up to a large cohort of diagnostic WSIs across additional MPN subtypes. Sample size, staining, and scanner details are not public — abstract-only.

## 主要结果 / Key results
Delivered a practical, interpretable pathomics pipeline with downstream analytics as a proof of concept for hypothesis-driven research, enabling region-resolved quantitative characterization of the BM microenvironment. No segmentation accuracy, AUC, or classification metrics are reported — abstract-only.

## 创新点 / Contributions
- Replaces a single global cellularity score with region-resolved, quantitative BM characterization, removing manual subjectivity and scalability limits.
- Couples DL segmentation with classical image analysis and interpretable nuclear shape/texture/color features.
- An MPN-oriented end-to-end pathomics pipeline designed to compose with other models (e.g. immune-cell detection).

## 局限 / Limitations
- Pilot / proof-of-concept only; no quantitative metrics or external validation.
- Small cohort, limited subtype coverage (mainly PV/MF).
- Conference abstract: method/data details undisclosed, no code or checkpoints released.

## 与本研究方向的关系 / Relation to our direction
Sits at the upstream of the **virtual-tissue / tissue-representation** stage: it decomposes marrow into a segmentation map (nucleated cells / fat / evaluable regions) and attaches quantitative nuclear shape/texture/color features — effectively a computable "virtual tissue" substrate for bone marrow. Its region-resolved, nucleus-level quantification is a natural feeder for **anomaly detection** (normal vs. MPN, or PV vs. MF regions as perturbed-vs-baseline). It does not touch gene-level revert prediction and carries no spatial-omics modality. Reusable for us: the nuclear feature-engineering paradigm, the region-resolved quantification idea, and the pattern of correlating pathomics features with other detectors (e.g. immune-cell models) as a template for mapping histology into computable features on the pathology branch.

## 可复用资产 / Reusable assets
No public code, checkpoints, or dataset (conference abstract). Reusable at the conceptual level: BM-WSI nucleated/fat segmentation + nucleus-level shape/texture/color features + interpretable downstream analytics. Traceable companion work from the same group (Scandura lab / Weill Cornell): "Correlating Image-Level Nucleomorphologic Features with Molecular Subtypes of Myeloproliferative Neoplasms."

## 待读 / Follow-ups
- Track whether the group published a full paper with quantitative metrics (segmentation accuracy, subtype AUC).
- Compare with Haematologica "AI-based quantitative BM pathology analysis for MPN" and DSCENet (MICCAI 2024) multimodal MPN subtyping.
- The group's nucleomorphologic-features ↔ molecular-subtype work (possible bridge to the gene level).

## 引用 / Cite
```bibtex
@article{krichevsky2023pathomics,
  title   = {A Deep Learning-Based Pathomics Methodology for Quantifying and Characterizing Nucleated Cells in the Bone Marrow Microenvironment},
  author  = {Krichevsky, Spencer and Ouseph, Madhu M. and Zhang, Yuwei and Abu-Zeinah, Ghaith and Scandura, Joseph M. and Gupta, Rajarsi},
  journal = {Blood},
  volume  = {142},
  number  = {Supplement 1},
  pages   = {2294},
  year    = {2023},
  doi     = {10.1182/blood-2023-191272},
  note    = {65th ASH Annual Meeting, Abstract 2294}
}
```


---

📄 **[AI-ready 全文 / full-text extract →](ai-ready.md)**

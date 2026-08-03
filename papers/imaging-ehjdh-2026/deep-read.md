# An artificial intelligence model to detect abnormal ejection fraction from non-contrast chest computed tomography: the CT–LVEF study

> **Bibkey** `Raikhelkar_2026` · **Venue** European Heart Journal - Digital Health (2026) · **Category** imaging · **Relevance** medium · **Access** paywall
> **Link** <https://doi.org/10.1093/ehjdh/ztag088>
> `status: complete` — 若为 abstract-only,把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。

---

## 一句话 / One-liner
<!-- ZH --> 用预训练的 3D vision transformer(CT-ViT)从常规、非门控、非增强胸部 CT 直接预测左室射血分数是否异常(EF < 50%),把一种"为别的适应症拍的影像"变成心衰的机会性筛查工具。
<!-- EN --> A pretrained 3D vision transformer (CT-ViT) predicts abnormal left-ventricular ejection fraction (EF < 50%) directly from routine non-gated, non-contrast chest CT, turning scans acquired for unrelated indications into an opportunistic heart-failure screen.

## 研究问题 / Problem
<!-- ZH --> 早期收缩性心衰患者在指南导向药物治疗(GDMT)最能阻止病程进展的阶段往往仍无症状、未被诊断,存在巨大的"诊断缺口"。心脏 EF 的金标准是超声心动图,但需专门预约;而非增强胸部 CT 每年海量拍摄(肺结节、创伤、术前评估等),从未被用于评估心功能。问题:能否零额外扫描、零对比剂,从这些"顺带"的 CT 里机会性地筛出隐匿的收缩功能障碍?
<!-- EN --> Many patients with early systolic dysfunction remain asymptomatic and undiagnosed at exactly the stage when guideline-directed medical therapy prevents progression — a large diagnostic gap. EF is normally read from echocardiography, which must be ordered specifically, whereas non-contrast chest CTs are acquired in huge volumes for unrelated reasons and never used to assess cardiac function. The paper asks whether abnormal EF can be opportunistically detected from those existing CTs with no extra scan and no contrast.

## 方法 / Method
<!-- ZH --> 任务被建为二分类:异常 EF(< 50%)vs. 正常。骨干采用预训练 CT-ViT encoder(一个 3D vision transformer),输入为归一化到 2×2×2 mm、裁剪/重采样到 164×164×164 voxel 的 3D CT 体积。每个 CT 与其时间上配对的超声报告(提供 EF 标签)对齐进行监督训练。可解释性用 Grad-CAM 生成 3D 显著性,定位与低 EF 相关的影像特征。评测除标准判别指标外,还与资深胸科放射科医生做人机对比(准确度 + 每例耗时)。
<!-- EN --> Framed as binary classification (abnormal EF < 50% vs. normal). The backbone is a pretrained CT-ViT encoder (a 3D vision transformer); inputs are 3D CT volumes normalized to 2×2×2 mm and resampled to 164×164×164 voxels. Each CT is paired with a temporally matched echocardiogram report supplying the EF label for supervised training. Interpretability uses Grad-CAM to produce 3D saliency localizing imaging features linked to reduced LVEF. Evaluation includes standard discrimination metrics plus a head-to-head reader study against experienced thoracic radiologists (accuracy and per-scan time).

## 数据 / Data
<!-- ZH --> 多机构、配对的 CT–超声数据集共 34,058 例配对(非增强 CT 影像 + 超声报告),来自两家学术中心。训练集 25,948 例(含 hold-out 内部测试),外部验证 8,110 例来自独立机构。内部验证=Columbia University,外部验证=Weill Cornell。人机对比在 90 张 Columbia 扫描的采样子集上进行。
<!-- EN --> A multi-institutional paired dataset of 34,058 non-contrast CT + echocardiogram-report pairs from two academic centers. Training used 25,948 studies (with a hold-out internal test set); external validation used 8,110 pairs from a separate institution. Internal = Columbia University; external = Weill Cornell. The reader comparison ran on a sampled subset of 90 Columbia scans.

## 主要结果 / Key results
<!-- ZH --> 内部 hold-out 测试:AUROC 0.786,F1 0.822;外部验证:AUROC 0.762,F1 0.812(泛化保持得较好)。人机对比(90 例 Columbia):模型 F1 0.808,资深胸科放射科医生 F1 区间 0.646–0.802,即模型在准确度上不逊于甚至超过专家;速度上模型约 1 分钟/例,放射科医生 2+ 分钟/例。Grad-CAM 定位到临床可辨认的低 EF 相关特征:心脏增大、升主动脉(尤其钙化时)、上腔静脉扩张、起搏器存在、肺水肿浸润。
<!-- EN --> Internal hold-out: AUROC 0.786, F1 0.822. External validation: AUROC 0.762, F1 0.812 (generalization largely preserved). Reader study (90 Columbia scans): model F1 0.808 vs. radiologist F1 0.646–0.802 — matching or exceeding experts on accuracy, at ~1 min/scan vs. 2+ min for radiologists. Grad-CAM highlighted clinically recognizable correlates of low EF: enlarged heart, ascending aorta (especially when calcified), dilated superior vena cava, pacemaker presence, and pulmonary-edema infiltrates.

## 创新点 / Contributions
- <!-- ZH --> 首次证明从**静态、非门控、非增强**胸部 CT 就能预测异常 LVEF,开启机会性心衰筛查的新用途(通常这种 CT 不用于心功能评估)。<!-- EN --> First demonstration that abnormal LVEF is predictable from static, non-gated, non-contrast chest CT — a new opportunistic-screening use of an otherwise unrelated modality.
- <!-- ZH --> 大规模、真实世界、跨机构配对数据(34,058 例)+ 独立外部验证,泛化性有据可循。<!-- EN --> Large real-world, cross-institution paired dataset (34,058) with independent external validation.
- <!-- ZH --> 人机对比中匹配/超越资深放射科医生,兼具速度优势;Grad-CAM 提供临床可解读的证据。<!-- EN --> Matches/exceeds expert radiologists with a speed advantage; Grad-CAM offers clinically interpretable evidence.

## 局限 / Limitations
- <!-- ZH --> 仅二分类(异常 vs. 正常),未回归连续 EF,也未细分 HFrEF/HFmrEF 亚型阈值。<!-- EN --> Binary only (abnormal vs. normal); no continuous EF regression or finer HFrEF/HFmrEF stratification.
- <!-- ZH --> AUROC ~0.76–0.79 属中等判别力,离临床独立诊断尚有距离;标签来自超声报告文本,存在时间错配与报告噪声。<!-- EN --> AUROC ~0.76–0.79 is moderate — not yet standalone-diagnostic; labels come from echo report text with temporal mismatch and reporting noise.
- <!-- ZH --> 两训练中心 + 一外部中心,人群/扫描仪多样性有限;人机对比样本仅 90 例。<!-- EN --> Two training + one external site limits scanner/population diversity; reader study only 90 scans.
- <!-- ZH --> 全文在付费墙后,超参、消融、校准与阈值选择等细节仅摘要可得。<!-- EN --> Full text is paywalled; hyperparameters, ablations, calibration, and threshold choice are abstract-only.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 这篇正处在我们流水线的**第一环:异常检测(anomaly detection)**——从医学影像中判定"这个器官/组织偏离了正常"。它与我们方向的三点可迁移经验:(1) **机会性/顺带筛查范式**——用为别的目的采集的组学/影像数据去发现未被标注的疾病扰动信号,与我们"从常规切片/空间组学里检出疾病或药物扰动区域"的思路同构;(2) **弱标签监督**——用配对的临床读数(此处超声 EF)当作影像标签,对应我们可用批量表型/临床终点弱监督 virtual tissue 的异常打分;(3) **可解释定位(Grad-CAM 3D 显著性)**——把"异常"落到具体解剖/空间位置,正是我们下一步做 virtual tissue 局部建模与 gene-revert 靶点定位所需的空间先验。注意其为纯有监督分类,并非我们偏好的无/自监督分布外异常检测;CT-ViT 这类 3D 影像 foundation encoder 可作为影像分支的 backbone 参考,但 gene-revert 反演环节本文不涉及。
<!-- EN --> This sits at stage 1 of our pipeline — anomaly detection: deciding that an organ/tissue deviates from normal in medical imaging. Three transferable lessons: (1) the opportunistic-screening paradigm — mining data collected for other purposes to surface unlabeled disease/perturbation signal — mirrors our goal of detecting disease- or drug-perturbed regions in routine histology/spatial-omics; (2) weak-label supervision — using paired clinical readouts (echo EF here) as image labels — parallels weakly supervising virtual-tissue anomaly scores with bulk phenotypes/clinical endpoints; (3) interpretable localization (3D Grad-CAM) grounds "abnormal" in specific anatomy/space, the spatial prior our later virtual-tissue modelling and gene-revert target localization need. Caveat: it is purely supervised classification, not the un-/self-supervised out-of-distribution anomaly detection we favor, and it does not touch the gene-revert inversion stage. The CT-ViT 3D imaging foundation encoder is a useful backbone reference for the imaging branch.

## 可复用资产 / Reusable assets
<!-- ZH --> **CT-ViT encoder**:文中作为骨干的预训练 3D vision transformer(源自 CT-CLIP / CT-ViT 系列的胸部 CT foundation model),是可复用的影像 backbone 起点。**输入规范**:2×2×2 mm 归一化 + 164×164×164 voxel 重采样,可直接抄用于 3D CT/体数据预处理。**评测协议**:配对 CT–临床读数、内部 hold-out + 独立外部机构验证、人机 reader study(准确度 + 每例耗时)——这套跨机构泛化 + 专家对照的评测范式可移植到我们的异常检测评估。数据集与训练代码本文未公开(私有临床数据,IRB 约束),需向作者/机构申请。
<!-- EN --> **CT-ViT encoder**: the pretrained 3D ViT backbone (from the CT-CLIP / CT-ViT family of chest-CT foundation models) is a reusable imaging-backbone starting point. **Input spec**: 2×2×2 mm normalization + 164×164×164-voxel resampling — directly copyable for 3D CT/volumetric preprocessing. **Eval protocol**: paired CT–clinical-readout labels, internal hold-out + independent external-site validation, plus a human reader study (accuracy + per-scan time) — a cross-institution generalization + expert-comparison template portable to our anomaly-detection evaluation. Dataset and training code are not released (private clinical data, IRB); request from authors/institutions.

## 待读 / Follow-ups
- <!-- ZH --> CT-ViT / CT-CLIP 原始 foundation-model 论文与权重(是否公开、许可、能否作为我们影像异常检测的 self-supervised backbone)。<!-- EN --> Original CT-ViT / CT-CLIP foundation-model paper + weights: availability, license, fitness as a self-supervised backbone for our imaging anomaly detection.
- <!-- ZH --> 获取全文以看架构细节、校准、阈值与消融;确认 EF 标签抽取与时间窗定义。<!-- EN --> Obtain full text for architecture details, calibration, thresholds, ablations; confirm EF-label extraction and temporal-window definition.
- <!-- ZH --> 对比同组/相邻工作(ECG-based EF、CXR-based EF)以定位 CT 分支在多模态机会性筛查中的增益。<!-- EN --> Compare adjacent work (ECG- and CXR-based EF) to position the CT branch within multimodal opportunistic screening.

## 引用 / Cite
```bibtex
@article{Raikhelkar_2026, title={An artificial intelligence model to detect abnormal ejection fraction from non-contrast chest computed tomography: the CT–LVEF study}, volume={7}, ISSN={2634-3916}, url={http://dx.doi.org/10.1093/ehjdh/ztag088}, DOI={10.1093/ehjdh/ztag088}, number={6}, journal={European Heart Journal - Digital Health}, publisher={Oxford University Press (OUP)}, author={Raikhelkar, Jayant and Bai, Zilong and Beecy, Ashley N and Richter, Ilan and Liu, Fengbei and Nizam, Nusrat Binta and Kishore, Varsha and Kelsey, Chris and vanMaanen, David and Ruhl, Jeffrey and Tesfuzigta, Naomi and Lancet, Erica and Leb, Jay and Legasto, Alan and Elias, Pierre and Poterucha, Timothy and Kumaraiah, Deepa and Prince, Martin and Wang, Fei and Sayer, Gabriel and Estrin, Deborah and Sabuncu, Mert and Uriel, Nir}, year={2026}, month=June }
```

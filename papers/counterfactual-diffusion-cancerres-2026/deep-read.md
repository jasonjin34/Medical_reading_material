# Counterfactual Diffusion Models Provide Interpretable Explanations of Artificial Intelligence Models in Pathology

> **Bibkey** `Zigutyte_2026` · **Venue** Cancer Research (2026) · **Category** histopath · **Relevance** medium · **Access** open
> **Link** <https://doi.org/10.1158/0008-5472.CAN-25-5645>
> `status: complete` — 基于 Europe PMC 开放全文(PMC13535314)精读;补充材料(Supplementary Figs/Tables)未读。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> MoPaDi(Morphing histoPathology Diffusion)把 **diffusion autoencoder** 与 tile 级 logistic regression / slide 级 **MIL** 分类器接起来:沿分类器在潜空间里的决策方向推动 tile 的特征向量,再用条件扩散解码器生成"如果它是另一类会长什么样"的 **counterfactual H&E 图像**,让病理医生直接看到模型依赖的形态学线索;在结直肠(组织类型、MSI)、肝胆、肺、乳腺癌任务上验证,并用 Shapley 式分解说明 MSI 预测主要由形态而非染色驱动。
<!-- EN --> MoPaDi (Morphing histoPathology Diffusion) couples a **diffusion autoencoder** with tile-level logistic-regression or slide-level **MIL** classifiers: it pushes a tile's latent feature vector along the classifier's decision direction and decodes it with the conditional diffusion model into a **counterfactual H&E image** ("what would this tile look like if it were class X?"), so pathologists can see the morphologic cues a model relies on. Validated on colorectal (tissue type, MSI), hepatobiliary, lung and breast tasks, with a Shapley-style decomposition showing MSI predictions are driven mostly by morphology rather than stain.

## 要点 / Takeaways
- <!-- ZH --> 核心操作很简单:在 diffusion autoencoder 的 512 维语义向量 z 上,沿分类器的方向 d(线性分类器的权重,或 MIL 分类器 logit 对 z 的梯度)走 α 步,再用原图反演得到的噪声 x_T 解码,得到"同一块组织、只改分类器在意的特征"的图像(Methods Eq. B–D)。 <!-- EN --> The core operation is simple: move the 512-d diffusion-autoencoder vector z along a classifier direction d (linear weights, or the gradient of the MIL logit w.r.t. z) by α, then decode with the original image's inverted noise x_T, giving "the same tissue with only the classifier-relevant features changed" (Methods Eq. B–D).
- <!-- ZH --> 把扩散反事实接到弱监督 MIL 上(只有 slide 级标签),作者称这是首次(Discussion)。 <!-- EN --> It attaches diffusion counterfactuals to weakly supervised MIL (slide-level labels only), which the authors call a first (Discussion).
- <!-- ZH --> 反事实忠实于分类器,不等于生物因果:MSI 分类器只有 AUC 0.73 ± 0.08,作者因此把 MSI 反事实当作"审计分类器"的案例(Results §MSI)。 <!-- EN --> Counterfactuals are faithful to the classifier, not to biology: the MSI classifier has AUC 0.73 ± 0.08, so the authors treat MSI counterfactuals as an audit of the classifier (Results §MSI).
- <!-- ZH --> 染色 vs 形态分解(Vahadane 染色迁移 + Shapley 式分解):朝 MSIH 的 logit 变化 +8.9 中,形态贡献 +7.4、染色 +1.1,108 例测试患者全部形态主导(Fig. 5B)。 <!-- EN --> Stain vs morphology (Vahadane transfer + Shapley-style split): of a +8.9 logit change toward MSIH, morphology contributes +7.4 and stain +1.1; morphology dominates in all 108 test patients (Fig. 5B).
- <!-- ZH --> 真实感:4 位评估者盲评,每人 300 张,合成图有 41.7% 被判为真(Results, Fig. S12)。 <!-- EN --> Realism: 4 blinded raters, 300 tiles each; 41.7% of synthetic tiles judged real (Results, Fig. S12).

## 研究问题 / Problem
<!-- ZH --> 计算病理里的 DL 模型能从 WSI 预测生物标志物,但常用的 XAI(attention heatmap、CAM/Grad-CAM)只告诉你"看了哪里",不告诉你"看到了什么特征",还容易引发确认偏差、高估模型。counterfactual explanation("要怎么改这张图它才会被分到另一类?")在自然图像、放射、皮肤科已有探索,但在病理里多基于不稳定的 GAN;而且病理标签大多只在 slide/患者层面(弱监督),需要与 MIL 结合 —— 这在扩散 counterfactual 上此前没有做过。
<!-- EN --> DL models predict biomarkers from WSIs, but standard XAI (attention heatmaps, CAM/Grad-CAM) shows *where* the model looked, not *which features* it used, and invites confirmation bias. Counterfactual explanations ("how would the image need to change to be classified as X?") exist for natural images, radiology and dermatology, but in pathology mostly via less stable GANs; moreover, pathology labels are usually slide/patient-level (weak supervision), so counterfactuals must work with MIL — which, per the authors, had not been combined with diffusion counterfactuals before.

## 方法 / Method
<!-- ZH --> **(1) Diffusion autoencoder**(基于 Preechakul 等 DiffAE 官方实现):可学习 CNN 编码器提取 512 维语义特征 z,条件 DDPM 以 z 为条件重建图像;编码器与去噪器用简化的噪声预测损失联合训练,训练至 FID < 20,推理用 DDIM 采样;另训一个 latent DDPM 用于采样合成特征以检验潜空间质量。**(2) 分类器**:tile 级标签(NCT-CRC-HE-100K)用 one-vs-rest logistic regression;患者级标签(MSI、癌种亚型)用 transformer 型 MIL(cross-attention + self-attention pooling),五折交叉验证。**(3) Counterfactual 生成**:线性情形方向 d = 分类器权重向量 v;MIL 情形 d = 目标类 logit s_c(z) 对该 tile 特征的梯度;按幅度 α 逐步移动 z(线性 α∈{0.2…1},MIL α∈{0.02…0.08}),反归一化后与原图反演得到的噪声 x_T 一起送入扩散解码器;每张 WSI 取贡献最大的 top-5 tile;固定参数下生成是确定性的。**(4) Style–morphology 分解**:用 Vahadane 染色迁移构造两种混合图(原形态+反事实染色;原染色+反事实形态),对 logit 变化 Δf 做 Shapley 式加性分解为 φ_style 与 φ_morph。**(5) 验证**:用独立的 UNI2 / Virchow2 / CONCH + STAMP MIL 分类器检查 counterfactual 是否在外部模型上也朝目标类移动;DeepCMorph 做核分割/细胞类型比例与形态统计;病理医生结构化问卷(特征出现/消失)与盲法真假判别。
<!-- EN --> **(1) Diffusion autoencoder** (on the official DiffAE implementation of Preechakul et al.): a learnable CNN encoder yields a 512-d semantic vector z; a DDPM conditioned on z reconstructs the image; encoder and denoiser are trained jointly with the simplified noise-prediction loss until FID < 20, with DDIM sampling at inference; a latent DDPM over z is also trained to sample synthetic features and test latent quality. **(2) Classifiers**: tile labels (NCT-CRC-HE-100K) → one-vs-rest logistic regression; patient labels (MSI, cancer subtype) → a transformer MIL (cross-attention + self-attention pooling), five-fold CV. **(3) Counterfactuals**: linear case, direction d = weight vector v; MIL case, d = gradient of target-class logit s_c(z) w.r.t. the tile feature; z is shifted with amplitude α (linear α ∈ {0.2…1}, MIL α ∈ {0.02…0.08}), denormalized and decoded together with the original image inverted to noise x_T; top-5 contributing tiles per WSI; generation is deterministic for fixed settings. **(4) Style–morphology decomposition**: Vahadane stain transfer builds two hybrids (original morphology + counterfactual stain; original stain + counterfactual morphology), and the logit change Δf is split Shapley-style into φ_style + φ_morph. **(5) Validation**: independent UNI2 / Virchow2 / CONCH + STAMP MIL classifiers check that counterfactuals move toward the target class for external models too; DeepCMorph nuclei segmentation for cell-type fractions and morphometrics; structured pathologist surveys (features appearing/disappearing) and a blinded real-vs-synthetic test.

## 方法图 / Method diagram
```mermaid
flowchart LR
  A["H&E tiles<br/>tumour regions"] --> B["Diffusion autoencoder<br/>encoder z 512-d + DDPM"]
  B --> C["Classifier on z<br/>logistic or MIL transformer"]
  C --> D["Direction d<br/>weights or logit gradient"]
  D --> E["z plus alpha times d"]
  B --> F["Inverted noise x_T"]
  E --> G["Decode counterfactual tile"]
  F --> G
  G --> H["Checks: flip rate, FM classifiers,<br/>cell counts, pathologists, stain vs morphology"]
```

## 数据 / Data
<!-- ZH --> 训练:NCT-CRC-HE-100K(10 万张 224×224 tile,86 例 FFPE,9 类组织;测试用 CRC-VAL-HE-7K 的 7,180 tile)、TCGA-CRC(625 WSI,过滤后 588 WSI / 582 例,512×512 tile @0.5 MPP,仅肿瘤区域)、TCGA-BRCA(1,115 WSI / 1,046 例)、TCGA pan-cancer tile 集(32 癌种)。外部验证:CPTAC-COAD(105 例 / 221 WSI,24 例 MSIH,冰冻切片)、CPTAC 乳腺(100 例 / 323 WSI)、CPTAC 肺 LUAD/LUSC(333 例 / 1,534 WSI)、Charité 肝癌队列(496 例,非公开)。MSI 阈值用两组分 GMM 拟合 TCGA 的 MSI events 分布得到。除 NCT-CRC-HE-100K(已用 Macenko 预先归一化)外,所有数据集(含外部验证队列)都不做染色归一化,以便研究染色对分类器的影响。
<!-- EN --> Training: NCT-CRC-HE-100K (100k 224×224 tiles from 86 FFPE samples, 9 tissue classes; test on 7,180 tiles of CRC-VAL-HE-7K), TCGA-CRC (625 WSIs → 588 WSIs / 582 patients after filtering; 512×512 tiles at 0.5 MPP, tumour regions only), TCGA-BRCA (1,115 WSIs / 1,046 patients), and a TCGA pan-cancer tile set (32 cancer types). External: CPTAC-COAD (105 patients / 221 WSIs, 24 MSIH, frozen), CPTAC breast (100 / 323), CPTAC lung LUAD/LUSC (333 / 1,534), and a Charité liver cohort (496 patients, not public). The MSI cut-off is set with a two-component GMM on TCGA MSI-event counts. Apart from NCT-CRC-HE-100K (pre-normalised with Macenko), no dataset, including the external cohorts, is stain-normalised, so that the influence of staining on classifiers can be studied.

## 主要结果 / Key results
- <!-- ZH --> **重建与生成**:四个数据集上 MS-SSIM 0.966–0.992;合成图 FID 最高 36.95(NCT-CRC-HE-100K 模型在 CRC-VAL-HE-7K 上,组织类别多、异质性大),最低 4.71(pan-cancer,作者认为参照集多样性低);UNI2/Virchow2 Fréchet 距离趋势一致(Table 1)。 <!-- EN --> **Reconstruction/generation**: MS-SSIM 0.966–0.992 across four datasets; synthetic FID from 36.95 (NCT-CRC-HE-100K model on CRC-VAL-HE-7K, heterogeneous) to 4.71 (pan-cancer, attributed to a low-diversity reference set); UNI2/Virchow2 Fréchet distances agree (Table 1).
- <!-- ZH --> **组织类型**:CRC-VAL-HE-7K 上正常黏膜 AUC 0.91 ± 0.01、肿瘤上皮 0.98 ± 0.01(Results §Tissue type);肿瘤→正常反事实中核异型、浸润生长、坏死碎屑消失,杯状细胞样结构出现(Fig. 2C);真实正常 tile(n = 741)与"肿瘤→正常"反事实(n = 1,233)的细胞组成差异效应量可忽略到小(Cliff's δ < 0.33,中位偏移 ≤ 3.1 个百分点);反方向(真实肿瘤上皮 vs"正常→肿瘤"反事实)则在结缔组织与上皮细胞比例上出现大与中等效应量(合成图上皮 +1.57 个百分点、结缔组织 −1.27 个百分点),作者解读为模型抓住了上皮细胞丰度这一区分特征(Fig. 2E, Table S4)。 <!-- EN --> **Tissue type**: on CRC-VAL-HE-7K, AUC 0.91 ± 0.01 (normal mucosa) and 0.98 ± 0.01 (tumour epithelium); tumour→normal counterfactuals lose nuclear atypia, invasive growth and necrotic debris and gain goblet-like cells (Fig. 2C); real normal tiles (n = 741) vs tumour→normal counterfactuals (n = 1,233) differ negligibly-to-small in cell composition (Cliff's δ < 0.33; median shifts ≤ 3.1 pp); in the reverse direction (real tumour epithelium vs normal→tumour counterfactuals) connective-tissue and epithelial fractions show large and medium effect sizes (epithelium +1.57 pp, connective tissue −1.27 pp in synthetic images), which the authors read as the model capturing epithelial abundance (Fig. 2E, Table S4).
- <!-- ZH --> **MSI(TCGA-CRC)**:MIL 五折 AUC 0.73 ± 0.08、AP 0.40 ± 0.09;CPTAC-COAD(冰冻切片)外部 AUC 0.67(Results §MSI)。3 位病理医生对 52 组转变(每类 13 名患者,每位取 2 个贡献度最高的 tile,共 26 名患者)做结构化评估(Fig. 3C),Discussion 总结其识别出印戒细胞、黏液与髓样形态、炎症浸润和低分化等与文献一致的特征;在 MSIL 患者的三分类示例中,朝 MSIH 的编辑出现腺体结构消失、更实性的生长和更多肿瘤内淋巴细胞,朝稳定方向则恢复腺体、减少黏液(Fig. 4B);UNI2 / CONCH / Virchow2 外部分类器的 MSI 概率都朝目标方向变化(Fig. 4A)。 <!-- EN --> **MSI (TCGA-CRC)**: MIL five-fold AUC 0.73 ± 0.08, AP 0.40 ± 0.09; external CPTAC-COAD (frozen) AUC 0.67 (Results §MSI). three pathologists rated 52 transitions (13 patients per class, 2 top-contributing tiles each, so 26 patients in total) in a structured survey (Fig. 3C), and the Discussion summarises the features they identified as signet-ring cells, mucinous and medullary patterns, inflammatory infiltration and poor differentiation, consistent with literature; in the three-class MSIL example, edits toward MSIH show loss of glandular architecture, more solid growth and more intratumoral lymphocytes, while the stable direction restores glands and reduces mucin (Fig. 4B); UNI2 / CONCH / Virchow2 classifiers shift MSI probability in the intended direction (Fig. 4A).
- <!-- ZH --> **染色 vs 形态**:108 例测试患者,朝 MSIH 的 Δf 中位 +8.9(IQR 7.2–10.1),φ_morph +7.4、φ_style +1.1;朝 non-MSIH Δf −7.6,φ_morph −6.6、φ_style −0.7;所有患者形态主导(Fig. 5B–C)。 <!-- EN --> **Stain vs morphology**: 108 test patients; toward MSIH median Δf +8.9 (IQR 7.2–10.1) with φ_morph +7.4 and φ_style +1.1; toward non-MSIH Δf −7.6 (φ_morph −6.6, φ_style −0.7); morphology dominates in every patient (Fig. 5B–C).
- <!-- ZH --> **真实感**:4 位评估者盲评,每人评 300 张图,合成图被误判为真的比例 41.7%(各数据集合计;Results; Fig. S12)。 <!-- EN --> **Realism**: four blinded raters, 300 tiles each — synthetic tiles judged real 41.7% of the time across all datasets (Results; Fig. S12).
- <!-- ZH --> **其他癌种**:肝 HCC vs CCA 线性 AUC 0.90(患者级 0.94),MIL 五折 0.96,Charité 外部(496 例)0.85,α = 0.08 时 100% 翻转(Fig. 6B);肺 LUAD vs LUSC MIL AUC 0.91,CPTAC 外部 0.77,α = 0.06 时 98.8% 翻转(Fig. 7C);乳腺 ILC vs IDC AUC 0.86,CPTAC 外部 0.70,约 97% 翻转,但 top tile 常缺乏典型 IDC 特征(Results §additional tumor types; Fig. S13D)。 <!-- EN --> **Other cancers**: liver HCC vs CCA linear AUC 0.90 (0.94 patient-level), MIL five-fold 0.96, Charité external (496 patients) 0.85, 100% flipped at α = 0.08 (Fig. 6B); lung LUAD vs LUSC MIL AUC 0.91, CPTAC external 0.77, 98.8% flipped at α = 0.06 (Fig. 7C); breast ILC vs IDC AUC 0.86, CPTAC external 0.70, ~97% flipped, though top tiles often lacked typical IDC features (Results; Fig. S13D).

## 创新点 / Contributions
- <!-- ZH --> 首个把扩散 counterfactual 与 MIL 结合、可解释**只有 slide 级标签**的生物标志物的生成模型(作者自述)。 <!-- EN --> First generative model (per the authors) combining diffusion counterfactuals with MIL to explain biomarkers that exist only as slide-level labels.
- <!-- ZH --> 连续的 α 轨迹让人在**同一块组织**上观察特征随决策方向的渐变,而非只看热图位置。 <!-- EN --> A continuous α trajectory lets one watch features morph along the decision direction *within the same tissue region*, rather than only seeing heatmap locations.
- <!-- ZH --> Shapley 式 style–morphology 分解,可在单图层面暴露染色/中心批次效应等 shortcut。 <!-- EN --> A Shapley-style style–morphology decomposition that can expose stain / site batch shortcuts per image.
- <!-- ZH --> 多层验证:外部基础模型分类器一致性 + 细胞组成定量 + 病理医生问卷 + 盲法真假测试。 <!-- EN --> Layered validation: external foundation-model classifier agreement, cell-composition quantification, pathologist surveys and a blinded real-vs-synthetic test.

## 局限 / Limitations
- <!-- ZH --> 只在 tile 层面;每个数据集都要重新训练一个昂贵的 diffusion autoencoder;未系统评估放大倍数影响。 <!-- EN --> Tile-level only; each dataset needs its own costly diffusion autoencoder; magnification effects not systematically evaluated.
- <!-- ZH --> Counterfactual 是**分类器忠实**而非生物因果:MSI 分类器本身只有中等性能(AUC 0.73),对弱分类器而言 counterfactual 更多是在暴露 shortcut。 <!-- EN --> Counterfactuals are *classifier-faithful*, not biologically causal; the MSI classifier is only moderate (AUC 0.73), and for weak classifiers counterfactuals mainly expose shortcuts.
- <!-- ZH --> Vahadane 染色迁移无法完美分离染色与结构,分解只是近似归因。 <!-- EN --> Vahadane stain transfer cannot perfectly separate stain from structure; the decomposition is approximate.
- <!-- ZH --> 未系统评估折叠、气泡、扫描噪声等**切片伪影**下的行为 —— 若分类器学到了伪影线索,counterfactual 可能保留甚至强化它们。 <!-- EN --> Behaviour under **slide artifacts** (folds, bubbles, scanner noise) not systematically assessed — artifact cues learned by the classifier may be preserved or reinforced.
- <!-- ZH --> 尚未与 attention heatmap / Grad-CAM 做正式的用户对照研究;细胞类型生成存在偏差,需专家把关。 <!-- EN --> No formal user study versus attention heatmaps / Grad-CAM yet; some cell-type generation bias, requiring expert review.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 作者自己把 MoPaDi 表述为"基于模型的虚拟扰动",可用于湿实验前预筛假设(Discussion)。它在 detect → model → revert 中最接近"revert"的**图像版原型**:把一块肿瘤 tile 沿决策方向推向"正常黏膜",并画出推回后的样子(Fig. 2A)。
- 我们的理解:MoPaDi 的方向 d 来自**有监督分类器**;如果把 d 换成异常分数(例如到健康参照分布的距离)对 z 的梯度,就能得到"把异常拉回健康"的反事实,这正是虚拟组织在 H&E 上的一个可视化接口。论文本身没有做这一步。
- 我们的理解(伪影注入课题):(1) 染色–形态分解可以用来区分"染色/中心批次差异"和"真实形态改变",对待测肾活检的 H&E 有直接用处;(2) 作者承认未评估折叠、气泡、扫描噪声等伪影,而且分类器学到的伪影线索可能被反事实保留甚至强化——这正是异常检测基准应专门覆盖的失败模式;(3) 用多个独立基础模型分类器检查反事实方向是否一致,可以借来检验"异常是否与编码器无关"。
- 我们的理解(Agent 可信度课题):论文反复区分"分类器认为 X"与"组织确实是 X",这正是 agent 在引用图像证据时需要被核查的一类 claim。
- 相关性 medium:癌症 H&E、tile 级,不涉及肾脏和组学。
<!-- EN --> The authors frame MoPaDi as "model-based virtual perturbation" that could prescreen hypotheses before wet-lab work (Discussion). Within detect → model → revert it is the closest **imaging prototype of "revert"**: it pushes a tumour tile toward "normal mucosa" along a decision direction and renders the result (Fig. 2A).
- Our reading: MoPaDi's direction d comes from a **supervised classifier**; replacing d by the gradient of an anomaly score (e.g. distance to a healthy reference distribution) w.r.t. z would yield "revert-to-healthy" counterfactuals — a visual interface for a virtual tissue on H&E. The paper does not do this.
- Our reading (the artifact-injection topic): (1) the stain–morphology decomposition can separate stain/site differences from true morphologic change, directly useful for H&E of the kidney biopsies to be tested; (2) the authors admit no evaluation under folds, bubbles or scanner noise, and artifact cues learned by the classifier may be kept or reinforced — exactly a failure mode an anomaly benchmark should cover; (3) checking counterfactual direction with several independent foundation-model classifiers transfers as an "is the anomaly encoder-agnostic?" test.
- Our reading (the agent-trustworthiness topic): the paper keeps "the classifier thinks X" separate from "the tissue is X" — the kind of claim an agent citing image evidence should have checked.
- Relevance medium: cancer H&E at tile level; no kidney, no omics.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码:** MoPaDi(uv 环境、依赖已锁定)。 <!-- EN --> **Code:** MoPaDi (pinned uv environment).
<!-- ZH/EN --> <https://github.com/KatherLab/mopadi>
- <!-- ZH --> **模型:** 训练好的 MoPaDi 权重。 <!-- EN --> **Checkpoints:** trained MoPaDi models.
<!-- ZH/EN --> <https://huggingface.co/KatherLab/MoPaDi>
- <!-- ZH --> **数据:** NCT-CRC-HE-100K / CRC-VAL-HE-7K、TCGA pan-cancer tile 集。 <!-- EN --> **Data:** NCT-CRC-HE-100K / CRC-VAL-HE-7K and the TCGA pan-cancer tile set.
<!-- ZH/EN --> <https://zenodo.org/records/1214456> · <https://zenodo.org/records/5889558>
- <!-- ZH --> **评测协议:** 翻转率 vs α、外部 FM 分类器 ΔP(target)、Shapley style–morphology 分解、DeepCMorph 细胞组成、盲法真假测试。 <!-- EN --> **Eval protocol:** flip rate vs α, external-FM ΔP(target), Shapley style–morphology decomposition, DeepCMorph cell composition, blinded real-vs-synthetic test.

## 待读 / Follow-ups
- <!-- ZH --> Preechakul 等 Diffusion Autoencoders(CVPR 2022)原文。 <!-- EN --> Preechakul et al., Diffusion Autoencoders (CVPR 2022).
- <!-- ZH --> 早期病理 GAN counterfactual / MSI 形态工作(文中 ref. 16),对比扩散方案的优势。 <!-- EN --> The earlier GAN-based pathology counterfactual / MSI-morphology work (ref. 16) for comparison.
- <!-- ZH --> 尝试把 MoPaDi 的方向 d 替换为异常分数梯度,在肾脏 H&E 上做"回退到健康"实验。 <!-- EN --> Try replacing MoPaDi's direction d with an anomaly-score gradient for "revert-to-healthy" experiments on kidney H&E.

## 引用 / Cite
```bibtex
@article{Zigutyte_2026, title={Counterfactual Diffusion Models Provide Interpretable Explanations of Artificial Intelligence Models in Pathology}, volume={86}, ISSN={1538-7445}, url={http://dx.doi.org/10.1158/0008-5472.CAN-25-5645}, DOI={10.1158/0008-5472.CAN-25-5645}, number={17}, journal={Cancer Research}, publisher={American Association for Cancer Research (AACR)}, author={Žigutytė, Laura and Lenz, Tim and Han, Tianyu and Reitsam, Nic G. and Foersch, Sebastian and Hewitt, Katherine J. and Jesinghaus, Moritz and Carrero, Zunamys I. and Unger, Michaela and Meneghetti, Asier Rabasco and Lurje, Georg and Lurje, Isabella and Herda, Sophia and Pein, Justus and Uluk, Deniz and Schneider, Carolin V. and Pearson, Alexander T. and Truhn, Daniel and Kather, Jakob Nikolas}, year={2026}, month=jun, pages={4414–4433} }
```

# MedIAnomaly: A comparative study of anomaly detection in medical images

> **文献键** `Cai_2025` · **来源** Medical Image Analysis(2025) · **类别** imaging · **相关度** medium · **获取** paywall
> **链接** <https://doi.org/10.1016/j.media.2025.103500> · `status: complete`

---

## 一句话
HKUST 的 Cai、Chen、Cheng 等搭建了医学图像 anomaly detection 的统一基准 MedIAnomaly:7 个数据集、5 种模态(胸片、脑 MRI、眼底、皮肤镜、病理)、30 种方法,在**统一网络结构**下比较图像级分类与像素级分割,并逐个拆解关键组件(latent 大小、重建距离函数、梯度分数、DDPM 噪声类型、ImageNet 权重),给出「朴素 AE 是强基线、ImageNet 特征出奇地强、重建质量与检测性能弱相关」等结论。

## 研究问题
医学 AD 方法很多,但缺乏公平、全面的对比:(1) 数据集与划分各不相同,有的数据集太简单——作者自己实现的朴素 AE 在 Hyper-Kvasir 与 OCT2017 上就几乎满分,说明在这些数据上「超越 SOTA」并不说明问题;(2) 同一范式的方法用了不同网络结构和训练技巧(如 f-AnoGAN 用残差块、AE-Flow 用 Wide ResNet-50-2、AE-U 用普通卷积),比较的其实是工程而非方法。已有综述要么不做实验,要么只覆盖单模态或单一范式,要么没有拆解组件。

## 方法
**分类法**:重建类(图像重建:AE、VAE、MemAE、Constrained AE、AE-U、DAE、f-AnoGAN、GANomaly、AnoDDPM、AutoDDPM 等;特征重建:FAE 等)、自监督类(一阶段:CutPaste、FPI、NSA、PII、AnatPaste 等合成异常分类/分割;两阶段:先在合成异常上训练再去掉头、在表示上拟合 Gaussian density estimator)、特征参照类(知识蒸馏、特征建模,如 ReContrast、PANDA、MSC)。**统一实现**:所有重建法尽量共用同一个 AE(64×64 输入、4 个编码块、latent 16);所有 SSL 法共用 ResNet18 特征提取器(224×224 输入)。另把「冻结的 ImageNet ResNet18/ResNet152 + 一类分类器」作为无特殊设计的对照。**指标**:图像级 AUC 与 AP;像素级 AP 与数据集级最优 Dice(在测试集最佳阈值处计算,规避阈值选择);刻意不用像素级 AUC(对假阳性不敏感)。每个实验 3 个随机种子。

## 数据
**图像级分类(6 个)**:RSNA 肺炎胸片(训练 3851 正常;测试 1000+1000)、VinDr-CXR(14 类异常;训练 4000;测试 1000+1000)、Brain Tumor MRI(训练 1000;测试 600 正常 + 300 胶质瘤 + 300 脑膜瘤)、LAG 青光眼眼底(训练 1500;测试 811+811)、ISIC2018(痣为正常,其余 6 类为异常;训练 6705;测试 909+603)、Camelyon16(沿用 Bao et al. 的处理版本,40× patch;训练 5088;测试 1120 正常 + 1113 异常)。**像素级分割(1 个)**:BraTS2021 FLAIR,1051 例取 4211 张正常轴位切片训练,200 例取 828 正常 + 1948 肿瘤切片测试。作者区分两类异常:胸片/MRI/眼底是**局部异常**(异常图包含健康版本 + 局部病灶),Camelyon16 与 ISIC2018 是**全局语义异常**(整体属于不同类别)。由于训练时无异常,不设验证集。

## 主要结果
- **基线**:朴素 AE 在 Hyper-Kvasir、OCT2017 上近乎满分——这两个数据集不适合作 AD 基准;在 7 个数据集上 AE 也是稳定的基线,作者强烈建议所有论文都报告 AE。
- **ImageNet 权重**:冻结的 ImageNet ResNet18 做两阶段特征 + 一类分类器,几乎在所有数据集上进前三,胜过多数训练流程更复杂的 SSL 方法;PANDA、MSC 这类「适配 ImageNet 特征」的方法没有显著提升。不用 ImageNet 权重时,重建类比 SSL 类更稳健。
- **病理(Camelyon16)**:不用 ImageNet 权重时,多数 AE/GAN 方法基本失效,只有 AE-U 与 DAE AUC 超过 51%;DDPM 类方法突出——AutoDDPM **80.7%**、AnoDDPM-Simplex **70.6%** AUC。作者认为病理异常与细胞形态密切相关,高保真重建在此反而有利。
- **latent 大小**:对局部异常,极小 latent 大幅提升——latent 从 128 降到 4,RSNA AUC +12.4%、AP +10.0%,VinDr-CXR AUC +12.7%,LAG AUC +7.3%;脑 MRI 的最优 latent 更大(约 32/16);ISIC2018(全局异常)反而越大越好。MemAE 在医学图像上失败,AE latent 上的 OC-SVM 接近随机(如 Camelyon16 AUC 0.49),说明正常/异常 latent 不可分。
- **距离函数**:perceptual loss(AE-PL)在 6 个数据集上达到或接近 SOTA,部分数据集比 L2 高 20% 以上 AUC,但在 ISIC2018 上比 L2 低 6.1%;SSIM 在 RSNA 上 +10% 以上、在 LAG 上 −10% 以上。没有一个距离函数在 7 个数据集上全面胜过 L2。
- **分割**:重建类显著优于 SSL 类,朴素 AE 在 BraTS2021 上胜过所有一阶段 SSL 分割法;DAE 最好,领先第二名超过 10% Dice;**简单强度阈值法排第二**,超过 DDPM 类方法。AnoDDPM 用 Simplex 噪声比 Gaussian 噪声在 BraTS 上高 30% 以上 Dice。
- **SSL 内部**:合成异常越逼真越好(两阶段 AnatPaste 比 CutPaste 在 RSNA 上 AUC +20.2%、VinDr-CXR +14.0%);同一合成方法下两阶段通常优于一阶段(AnatPaste:RSNA +11.5% AUC、Brain Tumor +16.0% AUC)。
- **重建质量 ≠ 检测性能**:AnoDDPM-Gaussian 重建质量最高却整体最差;AE-PL 重建明显失真却很有竞争力——关键是正常与异常残差分布可分,而非整体重建好坏。

## 创新点
- 覆盖重建、自监督、特征参照三大范式 30 种方法的医学 AD 统一基准,跨 5 种模态并同时评测分类与分割。
- **同范式统一网络结构**,让比较落在方法本身而非工程细节;并把冻结 ImageNet 特征、强度阈值这类「朴素对照」纳入基准。
- 首次系统拆解关键组件(latent 限制、距离函数、梯度分数、噪声类型、SSL 阶段数、合成逼真度),并提炼出「局部 vs 全局异常」这一解释框架。
- 数据重划分与代码全部公开。

## 局限
- 只用 2D(MRI 也切片处理),3D 与体数据 AD 未覆盖;像素级只有 BraTS2021 一个数据集、以显著肿瘤为主。
- 统一的小 AE(64×64 输入)和 ResNet18 牺牲了各方法的原始最佳配置;病理只用了 Camelyon16 一个预处理版本,且不含病理/医学 foundation model。
- 最优 Dice 在测试集上选阈值,是乐观上界;作者也指出 Dice 偏爱过度分割的方法,现有指标未必反映临床效用,特征空间分数缺乏校准。
- 最优 latent 大小等关键配置仍只能靠看测试结果来找,没有给出无监督的选择准则。

## 与本研究方向的关系
这是 detect 一环在**跨模态医学图像**上的方法学基准,与病理专用的 `pathology-ad-bench-mlhealth-2025` 互补(后者也引用本文作为最近的医学 AD 基准)。对 **Plan A / KidneyAnomalyBench** 最有价值的是它的**基准卫生**原则:(1) **先证明数据集不平凡**——朴素 AE 在 Hyper-Kvasir 上满分这一发现,意味着我们的 benchmark 必须报告朴素基线(AE、冻结特征 + 一类分类器、乃至「强度/细胞计数阈值」这种非学习方法),否则无法说明任务有难度;对肾脏组学而言,对应的朴素对照可能是「单基因表达阈值」或「细胞类型比例偏移」;(2) **局部 vs 全局异常**——肾脏病变多为局部(一个肾小球硬化、一片小管损伤),而作者显示局部异常需要强限制的表示、全局异常相反,KidneyAnomalyBench 应按这两类分别分层;(3) **冻结的预训练特征很强**——这暗示把 UNI2-h / Nicheformer 等 foundation model 冻结嵌入 + 一类分类器作为默认强基线,是合理的起点;(4) **阈值与校准**——作者批评的「测试集最优 Dice」与「特征空间分数不可校准」,正是 benchmark 需要回避的,我们应在专家验证集上固定阈值,并报告校准指标。对 **Plan B** 的启示在于:如果 agent 在分析中声称「方法 X 检出异常优于基线」,verifier 应检查它是否与 AE / 强度阈值这类朴素基线比较过——这是可以写进组学/影像特定失败分类的一个具体条目(「缺失朴素基线」)。

## 可复用资产
- **代码与数据重划分:** MedIAnomaly 仓库(30 种方法的统一实现 + 7 个数据集的划分)。
<https://github.com/caiyu6666/MedIAnomaly>
- **预印本全文:** arXiv 2404.04518(v4 为期刊版本)。
<https://arxiv.org/abs/2404.04518>
- **评测规范:** 图像级 AUC + AP、像素级 AP + 最优 Dice、3 个随机种子、不用像素 AUC;以及「朴素 AE + 冻结 ImageNet 特征 + 强度阈值」三件套对照。

## 待读
- Lagogiannis et al. 与 Bao et al.(BMAD)的医学 AD 基准,与本文结论对照。
- Cai et al. 关于「最优 latent 熵应匹配正常数据熵」的信息论分析——可能给出无监督选 latent 大小的方法。
- 本文 5.5 节的一类半监督与 few/zero-shot(VLM)设定,看能否迁移到只有少量专家确认异常的肾脏数据。

## 引用
```bibtex
@article{Cai_2025, title={MedIAnomaly: A comparative study of anomaly detection in medical images}, volume={102}, ISSN={1361-8415}, url={http://dx.doi.org/10.1016/j.media.2025.103500}, DOI={10.1016/j.media.2025.103500}, journal={Medical Image Analysis}, publisher={Elsevier BV}, author={Cai, Yu and Zhang, Weiwen and Chen, Hao and Cheng, Kwang-Ting}, year={2025}, month=May, pages={103500} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

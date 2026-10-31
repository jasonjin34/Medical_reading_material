# CFLOW-AD: Real-Time Unsupervised Anomaly Detection with Localization via Conditional Normalizing Flows

> **文献键** `Gudovskiy2021_210712571` · **来源** 2022 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)(2022) · **类别** anomaly · **相关度** medium · **获取** open
> **链接** <https://arxiv.org/abs/2107.12571> · `status: complete`

---

## 一句话
CFLOW-AD 在 ImageNet 预训练 CNN 编码器的多尺度特征上,为每个尺度训练一个以**位置编码为条件的 normalizing flow 解码器**,直接估计每个 patch 特征的精确对数似然作为异常分数;作者证明在多元高斯先验下 flow 目标退化为 Mahalanobis 距离(即 PaDiM 是其特例),而 CFLOW-AD 在 MVTec 上达到 98.26% 检测 AUROC、98.62% 定位 AUROC、94.60% AUPRO,并比同设置的 PaDiM/SPADE 快且小约 10 倍。

## 研究问题
当时的 SOTA 无监督 AD+定位方法(SPADE、PaDiM)精度高,但后处理代价大:SPADE 要对训练特征库做 kNN,内存和速度都不可接受;PaDiM 要为每个空间位置存一个 D×D 协方差逆矩阵,内存随分辨率增长,作者推断这也是其只能在 CPU 上测速的原因。另一方面,全生成式模型(GAN、VAE)无法给出精确似然,在 MVTec 上也不比传统方法好。问题是:能否既有**精确的密度估计**、又是**全卷积、低内存、可实时**的结构?

## 方法
**理论**:用 L2 weight decay 训练的 CNN 在中间特征上隐含多元高斯(MVG)先验 —— 这为 Lee 等 / Rippel 等 / PaDiM 的 Mahalanobis 打分提供了依据;作者进一步证明,在 MVG 假设下 normalizing flow 的反向 KL 损失可写成 Mahalanobis 距离与 Euclidean 距离之差加 log-Jacobian 项,因此 flow 框架收敛到与 Mahalanobis 类似的解,但能拟合**任意**分布而不限于 MVG。**编码器**:ImageNet 预训练 CNN(ResNet-18、WideResNet-50 或 MobileNetV3L),与 PaDiM 相同的多尺度特征金字塔 pooling(K 个尺度,默认 3 个,第 1–3 层)。**解码器**:每个尺度 k 一个独立的 conditional normalizing flow g_k;条件向量 c_i 是 2D 正余弦**位置编码**(C_k=128),在每个 coupling layer 中与中间向量拼接;coupling layer = 全连接 + softplus + 置换;因为解码器作用在单个特征向量上并跨位置共享参数,整体是平移等变、全卷积的,与特征图尺寸无关。**训练**:最大似然,即最小化 ‖u‖²/2 − log|det J|,每个 mini-batch 从 32 张特征图中随机采样 8192 个特征向量;Adam lr 2e-4,100 epoch,cosine 退火。**推理**:每尺度估计对数似然 → 转成概率并归一化到 [0,1] → 双线性上采样到输入尺寸 → 跨尺度聚合为异常图 S。每个 MVTec 类、每个 STC 场景单独训练一个模型。

## 方法谱系
**范式:density / one-class**(在预训练特征空间上做精确密度估计;与 feature-embedding 家族共享编码器)。**承接**:RealNVP(Dinh 等)与 conditional INN(Ardizzone 等)提供 flow 结构;DifferNet(Rudolph 等 WACV 2021)首先把 flow 用于图像级 AD;Lee 等 2018 → Rippel 等 2020 → PaDiM 这条 "MVG + Mahalanobis" 线被作者在理论上统一为 flow 的特例;PaDiM 的金字塔 pooling 设置被原样采用。**影响**:与 FastFlow、CS-Flow 一起构成 AD 中的 normalizing-flow 家族,在 anomalib 中是标准基线;pathology-ad-bench-mlhealth-2025 把 CFLOW-AD 列入 normalizing flow 家族在病理数据上评测,并指出该家族"计算代价高、对结构选择敏感"。

## 数据
**MVTec AD**:15 类,3,629 张训练(全为无缺陷)/ 1,725 张测试;不裁剪直接缩放到指定分辨率(128/256/512),训练时 ±5° 旋转增强。**STC**:274,515 训练帧 / 42,883 测试帧,13 个校园场景,固定 256×256。

## 主要结果
- **MVTec 平均(WRN-50)**:检测 AUROC **98.26%**(PaDiM 97.9、CutPaste 97.1、DifferNet 94.9、Patch SVDD 92.1、SPADE 85.5);定位 AUROC **98.62%**(PaDiM 97.5、SPADE/CutPaste 96.0、Patch SVDD 95.7、DFR 95.0);AUPRO **94.60%**(PaDiM 92.1、SPADE 91.7、DFR 91.0)。即检测 +0.36、定位 +1.12 AUROC / +2.5 AUPRO。每个实验重复 4 次报均值。
- **STC**:检测 AUROC 72.63%(CAVGA 71.9),定位 94.48%(PaDiM 91.2、SPADE 89.9、CAVGA 85.0)。
- **消融(定位 AUROC)**:coupling layer 4→8 平均 +0.15%;3 尺度比 2 尺度 +1.4%(加入 32×32 的第 1 层);条件 flow 比无条件 flow +0.5%(位置先验有用);WRN-50 比 R18 +0.81%;**最优输入分辨率因类别而异**(多数类 512 最好,cable/pill 256,transistor 128)。
- **速度**:GPU(1080 8GB)上 CFLOW-AD-WRN50 为 27 / 9 fps(256 / 512 输入),对比 PaDiM-WRN50 1.1 fps、SPADE-WRN50 0.1 fps(后两者取自 PaDiM 论文的 CPU 测量);R18 版本 34 / 12 fps vs PaDiM-R18 4.4 fps;作者总结为快 8–25 倍。不计编码器时模型比 SPADE 小 1.7–50 倍、比 PaDiM 小 2–7 倍。

## 创新点
- **理论统一**:说明为何 MVG/Mahalanobis 是合理先验,并证明 flow 目标在该先验下收敛到相似解 —— 把 Lee 等、Rippel 等、PaDiM 放进同一个似然框架。
- **位置条件 flow**:用位置编码作条件,把空间先验放进密度模型,同时保持参数跨位置共享(不像 PaDiM 每个位置一套参数)。
- 全卷积、与特征图尺寸无关、内存小、可在 GPU 上实时运行;代码开源且实验可复现。

## 局限
- **按类别选输入分辨率**:主表结果使用每类最优分辨率(128/256/512),而论文未说明如何在不看测试异常的情况下选出 —— 有测试集调参之嫌,与 PatchCore/PaDiM 的统一设置不完全可比。
- 速度对比不对等:CFLOW-AD 在 GPU 上测,PaDiM/SPADE 数字取自 CPU 测量。
- 作者自己引用了"normalizing flow 在 OOD 检测上会失效"(Kirichenko 等)以及"深度生成模型不知道自己不知道什么"(Nalisnick 等),但没有在 AD 设定下系统检验这一风险;似然仍依赖 ImageNet 特征。
- 需要训练(每类 100 epoch),且仍是每类一个模型。

## 与本研究方向的关系
CFLOW-AD 给伪影注入课题的是**"条件密度"这个建模角度**:异常分数 = 在给定上下文下的负对数似然。**映射到肾脏组学**:样本 = 细胞 / spot;正常训练集 = 健康参考;特征 = scVI 潜变量或基础模型 embedding;最关键的是**条件 c**:原文条件是像素位置编码,组学里可换成**细胞类型、解剖区域(皮质/髓质、肾小球/小管/间质)、空间 niche 组成、供体协变量(年龄、性别)**—— 于是模型学的是 p(细胞状态 | 细胞类型, 所处 niche, 供体),一个"在髓质里看起来正常、但出现在皮质肾小球旁就异常"的细胞能被识别出来。这比 PaDiM 的"每类一个高斯"更灵活(可多峰),也比 PatchCore 的 kNN 距离更有概率含义,原则上可接 conformal 校准(参照 conformal-scrna-bioinformatics-2025 用重建误差做非一致性分数的做法,把负对数似然换成非一致性分数即可)。**哪些假设会破**:(1) **似然 ≠ 异常**:flow 已知会给简单/低复杂度样本过高似然 —— 在 snRNA 里,低 UMI、高 ambient 比例的"空滴状"细胞信息量低,可能拿到高似然而被判为正常;反之高质量、表达丰富的健康细胞反而似然低;(2) batch effect 会直接移动密度,条件里必须显式包含批次或先做整合;(3) 连续疾病态下,似然只给"多罕见",不给方向;(4) 原文按类别挑分辨率的做法,对应到组学就是"按样本调 hyperparameter 看结果" —— 在 KidneyAnomalyBench 中必须禁止,只能用无异常验证集选参(参照 pathology-ad-bench-mlhealth-2025 的无偏 epoch 选择协议)。**仓库里已有的同类思想**:pathology-ad-bench-mlhealth-2025 在 Camelyon16、Crohn 结肠与小鼠肾小球上直接评测 CFLOW-AD;sardine-bioinformatics-2025 在表达流形 kNN 图上做局部**密度**比较(跨条件),是"密度视角"在空间转录组中的近亲,但它是非参数、跨条件的,不是在健康参考上学条件似然。

## 可复用资产
- **代码:** 官方 PyTorch 实现(基于 FrEIA flow 库),含可复现实验。
<https://github.com/gudovskiy/cflow-ad>
- **库:** anomalib 中的 CFLOW 实现。
<https://github.com/open-edge-platform/anomalib>
- **建模件:** 条件 coupling layer(条件向量拼接进每层)—— 可把细胞类型 / niche / 供体 one-hot 或 embedding 作为条件,直接用于 scVI 潜空间上的条件密度。

## 待读
- DifferNet(Rudolph 等 WACV 2021)与 FastFlow、CS-Flow —— AD 中 flow 家族的其余成员。
- Kirichenko 等 2020《Why normalizing flows fail to detect out-of-distribution data》—— 评估"似然 ≠ 异常"在单细胞低质量细胞上的风险。
- 与 mahalanobis-ood-neurips-2018 和 energy-ood-neurips-2020 对照:似然、Mahalanobis、energy 三种分数在同一 embedding 上的差异。

## 引用
```bibtex
@inproceedings{Gudovskiy2021_210712571,
  title = {{CFLOW-AD}: Real-Time Unsupervised Anomaly Detection with Localization via Conditional Normalizing Flows},
  author = {Gudovskiy, Denis and Ishizaka, Shun and Kozuka, Kazuki},
  booktitle = {2022 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)},
  pages = {1819--1828},
  publisher = {IEEE},
  year = {2022},
  doi = {10.1109/WACV51458.2022.00188},
  eprint = {2107.12571},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2107.12571}
}
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

# Unsupervised Anomaly Detection with Generative Adversarial Networks to Guide Marker Discovery

> **文献键** `Schlegl2017_170305921` · **来源** Information Processing in Medical Imaging (IPMI 2017), LNCS 10265(2017) · **类别** anomaly · **相关度** medium · **获取** open
> **链接** <https://arxiv.org/abs/1703.05921> · `status: complete`

---

## 一句话
AnoGAN 只在**健康**视网膜 OCT 图块上训练一个 DCGAN,测试时对每张新图块在 latent space 里做 500 步梯度下降找到"最像它的正常图像" G(z),用**像素残差 + 判别器中间层特征残差**的加权和作异常分数、残差图作异常定位 —— 这是把 GAN 用于异常检测的首个工作(作者自述),也是"学正常 → 重建 → 看残差"这一范式的奠基论文。

## 研究问题
影像标志物的自动检测通常依赖大量带标注的已知病灶,标注成本高,而且检测能力被限定在"已知标志物词表"之内 —— 很多疾病缺乏足够的已知标志物,或已知标志物预测力有限。作者要问:能否只用健康数据做无监督学习,把**偏离正常解剖变异的区域**自动挑出来,作为新标志物的候选?此前的异常检测要么用 1D/纹理/合成数据(维度与医学图像不同),要么用卷积自编码器 + one-class SVM(需人为设定覆盖比例的超参)。

## 方法
**(1) 正常流形学习**:从 M 张健康 OCT 图像中随机采 64×64 图块,训练标准 DCGAN(G 为 4 层分数步长卷积,D 为 4 层卷积,5×5 滤波,通道 512-256-128-64)。训练不使用任何标签。**(2) 图像 → latent 映射**:GAN 没有逆映射,于是对查询图 x 从随机 z₁ 出发,固定 G、D 参数,只更新 z,迭代 Γ=500 步最小化 L(z) = (1−λ)·L_R + λ·L_D。其中 **residual loss** L_R = Σ|x − G(z)| 约束视觉相似;**discrimination loss** 有两种:沿用 Yeh 等 inpainting 的版本(把 G(z) 送进 D、要求输出"真")作参照,以及本文提出的**特征匹配版** L_D = Σ|f(x) − f(G(z))|,f 是判别器中间层 —— 即把 D 当特征提取器而非分类器。λ=0.1(在人脸数据上预实验选定)。**(3) 异常打分**:A(x) = (1−λ)·R(x) + λ·D(x),取最后一步的两项损失;残差图 x_R = |x − G(z_Γ)| 用于像素级定位。

## 方法谱系
**范式:重建 / 生成式(reconstruction / generative)**。它建立在 DCGAN(Radford 等)、Yeh 等的语义 inpainting(latent 搜索)与 Salimans 等的 feature matching 之上;对照组是对抗卷积自编码器(aCAE)以及作者组之前的 CAE + one-class SVM。它直接催生了 **f-AnoGAN**(同组,2019:用训练好的编码器替代迭代搜索,换成 WGAN-GP),以及 GANomaly、Skip-GANomaly、ADGAN 等一整支 GAN 重建流派;Ruff 等的统一综述把它归为"把 GAN 当随机解码器、latent 搜索当隐式编码"的重建方法。后续扩散模型(AnoDDPM、Wolleb 等 2022)本质上把"生成器 + 投影回正常流形"换成了"加噪 + 去噪"。

## 数据
临床高分辨 SD-OCT 视网膜体数据(每体 49 张 B-scan,496×512×49 体素)。训练:270 个健康受试者的 OCT 体(以"无积液"为筛选标准),预处理包括灰度归一化到 [−1,1]、x 方向重采样到 22 µm(约 256 列)、用层分割算法提取并展平视网膜区域,随机采得**共 1,000,000 个 64×64 训练图块**。测试:另外 10 个健康 + 10 个含视网膜积液的病例,**共 8,192 个图块**;病例有临床专家的体素级积液标注,只用于评估。图块中只要有一个像素标为积液即记为阳性。

## 主要结果
**图像级检测(表 1,Youden 点)**:AnoGAN **AUC 0.89**,precision 0.8834、sensitivity 0.7279、specificity 0.8928;GAN_R(同一 GAN、但用 Yeh 式判别损失)AUC 0.88;直接用 DCGAN 判别器输出 P_D AUC 0.72;aCAE AUC 0.73(作者观察到 aCAE 会"过度适应"异常图像、把异常也重建出来)。**分量分析**:本文的特征匹配判别分数 D(x) 优于参照判别分数 D̂(x);但 AnoGAN 与 GAN_R 的总 AUC 接近,作者归因于残差分数 R(x) 本身就很强。**定性**:正常图块能被近乎重建,含积液图块的重建与输入在强度/纹理上明显不同;残差图与积液标注吻合,并额外标出了未被标注的**高反射灶(HRF)**。**算力**:每张测试图 500 步反向传播做 latent 映射(这正是 f-AnoGAN 要解决的速度瓶颈)。

## 创新点
- 首次把 GAN 用于异常/新颖性检测(作者自述):只用健康数据学"正常解剖变异流形"。
- 提出 latent 空间映射方案解决 GAN 的 pre-image 问题,并以**判别器中间特征的匹配**作为判别损失(把 D 当特征提取器)。
- 由映射损失直接导出的组合异常分数 A(x) 与残差图,同时给出图像级判定与像素级定位。
- 把"异常 = 标志物候选"的定位用于发现未标注病变(HRF),而非只复现已知类别。

## 局限
- **推理极慢**:每个样本 500 步梯度下降;f-AnoGAN 报告同类迭代方案在 70,000 张图上要 2 天。
- 评估只基于一种已标注异常(积液);作者承认"假阳性"可能是未标注的真异常,定量评估因此有偏。
- 只有图像级 ROC/AUC 的定量结果,像素级分割只给定性图;λ 在人脸数据上选定,未在 OCT 上调参。
- 64×64 小图块、单一设备、单一器官;DCGAN 训练不稳定、对小数据易不收敛(Deep SVDD 论文在 780 张 GTSRB 图上就报告 AnoGAN 的 DCGAN 未收敛)。
- 预处理依赖层分割与展平 —— 分割失败会直接变成"异常"。

## 与本研究方向的关系
AnoGAN 是整个 **detect → model → revert** 链条的**思想原型**:G 是"正常组织的生成模型",G(z*) 是"这个样本若健康会是什么样",残差就是"疾病改变了什么"。这正是 virtual tissue 的最简形态 —— 一个只会生成正常的模型,加上把观察投影回正常流形的操作;而"投影前后的差"天然就是 revert 的目标方向。**映射到课题 1(肾脏组学)**:样本可以是 snRNA/snATAC 细胞、Xenium 细胞或 Visium spot,也可以是 H&E 图块;"健康训练集"取 KPMP/HuBMAP 健康活体供肾或 Lake 图谱中的参考样本;特征空间不必是原始计数,可以是 scVI latent 或基础模型嵌入(H&E 用 UNI2-h 之类)。**哪些假设会断**:(1) **批次效应**——新供者/新批次的系统偏移在"正常流形"之外,会被当成异常;必须先做参考映射(见 refmap-eval)或在残差里扣除批次方向。(2) **ambient RNA、doublet、Xenium 分割错误**——这些产生的"嵌合"表达谱同样离开正常流形,AnoGAN 会忠实地把它们排到最高分;这正是课题 1 的核心难题:**异常 ≠ 疾病**。(3) **连续疾病态**——PT 损伤、failed-repair 等是连续梯度,没有 OCT 积液那种清晰的"有/无";A(x) 是连续分数,阈值需要校准(见 conformal-scrna)。(4) **没有像素级金标准**——AnoGAN 自己就承认"假阳性可能是未标注真异常",这正是 KidneyAnomalyBench 必须由专家逐例判定而不能只用标签算 AUC 的原因。(5) 每样本 500 步优化,对百万级细胞不可行。**课题 1 的跨模态一致性可以直接嫁接**:对同一组织分别算 H&E 残差与表达残差,真实病变应在两个模态上**同时**出现,而 ambient/分割伪影通常只出现在一个模态 —— 用"一致的残差"区分疾病与伪影。**仓库里已有的同类适配**:STANDS(spatial-natcommun-2024)在正常参考上训练 GAN 重建 spot、用重建误差判异常,并加 memory bank 抑制 mode collapse;MEATRD 与 histo-miccai-2025 都把 f-AnoGAN(AnoGAN 的后继)作为基线,且在乳腺 ST 和淋巴结病理上表现很差 —— 说明原始 GAN 重建在组织数据上基本只能当弱基线。

## 可复用资产
- **代码:** 论文未给官方仓库;作者注明改编自 bamos/dcgan-completion.tensorflow。可直接用 f-AnoGAN 官方代码(含迭代 z-mapping 对照)。
<https://github.com/tSchlegl/f-AnoGAN>
- **数据:** 临床 OCT 数据未公开。
- **评测协议:** "图块含任一阳性像素即阳性"的图像级标签 + Youden 点上的 precision/sensitivity/specificity —— 可作为 KidneyAnomalyBench 细胞/区域级标签的参照写法。

## 待读
- f-AnoGAN(本仓库 f-anogan-media-2019):编码器替代迭代搜索后的速度/精度对比。
- Seeböck 等 2016(CAE + one-class SVM,同组前作)与 Zenati 等 2018(BiGAN 异常检测)。
- GANomaly / Skip-GANomaly(pathology-ad-bench 中作为重建类基线)。

## 引用
```bibtex
@inproceedings{Schlegl2017_170305921,
  title = {Unsupervised Anomaly Detection with Generative Adversarial Networks to Guide Marker Discovery},
  author = {Schlegl, Thomas and Seeb{\"o}ck, Philipp and Waldstein, Sebastian M. and Schmidt-Erfurth, Ursula and Langs, Georg},
  booktitle = {Information Processing in Medical Imaging (IPMI 2017)},
  series = {Lecture Notes in Computer Science},
  volume = {10265},
  pages = {146--157},
  publisher = {Springer},
  year = {2017},
  doi = {10.1007/978-3-319-59050-9_12},
  eprint = {1703.05921},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/1703.05921}
}
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

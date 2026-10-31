# f-AnoGAN: Fast unsupervised anomaly detection with generative adversarial networks

> **文献键** `Schlegl_2019` · **来源** Medical Image Analysis(2019) · **类别** anomaly · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1016/j.media.2019.01.010> · `status: complete`

---

## 一句话
f-AnoGAN 把 AnoGAN 的"每张图 latent 迭代搜索"换成**一个训练好的编码器 E**:先在健康 OCT 图块上训练 WGAN-GP,再固定 G 和 D、用"像素残差 + 判别器特征残差"(izi_f)训练 E,测试时一次前向即得重建 G(E(x)) 与异常分数;图像级 AUC 0.930,优于 AE / AdvAE / ALI 与迭代式 AnoGAN(0.911),而推理从 2 天缩到 20 秒。

## 研究问题
临床影像的专家标注昂贵,且不是所有有意义的标志物都事先已知,监督学习因此只能检测已标注病灶。AnoGAN 证明了"只学正常、按残差找异常"可行,但其迭代 latent 映射太慢,无法用于大规模筛查或实时应用;GAN 本身也没有图像→latent 的逆映射。本文要解决:如何**快速且准确**地把新图像映射到 GAN 的 latent 空间,并研究不同编码器训练方式对检测与定位的影响。

## 方法
**两步训练,均只用正常数据**。**(1) WGAN-GP**:ResNet 式生成器与判别器各 4 个残差块(G 通道 512-256-128-64,D 128-256-512-512,3×3 卷积,D 用 layer norm),128 维正态 latent;训练 100,000 次迭代(batch 64),每次 G 更新配 5 次 D 更新。**(2) 编码器训练(G、D 固定)**,比较三种:**ziz**——从 z 采样、经 G 生成、再让 E 还原 z(L = ‖z − E(G(z))‖²),不看任何真实图像;**izi**——标准自编码器式,L = ‖x − G(E(x))‖²/n;**izi_f(提出的 f-AnoGAN)**——在 izi 基础上加判别器中间层特征残差,L = ‖x − G(E(x))‖²/n + κ·‖f(x) − f(G(E(x)))‖²/n_d。理由:只最小化像素差,可能把图像映到 latent 中训练时稀疏的区域,得到"不真实但残差很小"的重建,使残差不再是可靠的异常标志。编码器输出加 tanh,把 latent 限制在 (−1σ, +1σ)。50,000 次编码器迭代(RMSprop)。**(3) 打分**:A(x) = A_R(x) + κ·A_D(x),κ=1;像素级定位用 |x − G(E(x))|。

## 方法谱系
**范式:重建 / 生成式**。直接继承 AnoGAN(同组 2017),作者列出的三处差别:WGAN-GP 替代 DCGAN、学习型编码器替代迭代梯度下降、更广的对照实验。ziz 来自 BiGAN 论文(Donahue 等)中的 "latent regressor" 基线;判别器特征残差源自 Salimans 等的 feature matching。对照方法 ALI 在方法上等价于 BiGAN(Zenati 等 2018 已用于异常检测)。之后它成为医学影像无监督异常检测里**最常被引用的 GAN 基线**:MedIAnomaly 的分类法把它列入图像重建类,MEATRD(空间转录组)与 AnoPILaD(淋巴结病理)都拿它作基线;扩散模型方法(AnoDDPM、Wolleb 等 2022)则在同一"重建到正常"范式里取代了它。

## 数据
与 AnoGAN 相同的临床 SD-OCT(Heidelberg Spectralis,每体 49 张 B-scan,496×512×49)。预处理:逐体灰度归一化到 [−1,1],列数 512→256(x 方向 22 µm),用层分割定位视网膜上下边界后展平(仅在视网膜厚度超出提取高度时归一化厚度)。训练:约 **850,000 个 64×64 图块**,来自 270 个确认无积液的健康体。测试:10 个健康 + 10 个含积液病例,共 **70,000 个图块**(70% 正常 / 30% 含积液),有专家像素级积液标注(仅用于评估)。

## 主要结果
**图像级检测(表 1,Youden 点)**:f-AnoGAN **AUC 0.9301**、precision 0.7863、sensitivity 0.8091、specificity 0.9049、F1 0.7975;迭代式(≈AnoGAN)AUC 0.9114;AE 0.8688;AdvAE 0.8649;ALI 0.7897;直接用 WGAN 判别器输出 A_D 仅 0.7504。**速度**:迭代方案每图 300 次更新、70,000 张测试图在 Titan X 上共需 **2 天**,f-AnoGAN 为 **20 秒**。**编码器对比(表 2)**:izi_f 0.9301 > ziz 0.9066 > izi 0.8874;即使给 izi/ziz 在打分时补上判别器特征项,AUC 也只到 0.8976 / 0.9209,仍低于 izi_f —— 说明判别器在**训练编码器**时就有用。**像素级定位**:积液"分割"sensitivity 0.69、specificity 0.75、AUC 0.78(作者注明只是粗略指标);AE 重建过于平滑、定位最差,ALI 与 ziz 易在视网膜-玻璃体边界产生假阳性和过度分割。**视觉图灵测试**:两位视网膜专家区分 50 张真实 / 50 张生成的正常图块,平均准确率 **0.44**(低于随机),两人一致性 0.58。

## 创新点
- 用学习型编码器实现单步图像→latent 映射,使 GAN 异常检测可用于高通量筛查。
- 提出判别器引导的编码器训练 izi_f,并系统比较 ziz / izi / izi_f 三种编码器训练方式。
- 在统一架构下与 AE、AdvAE、ALI、迭代映射、纯判别器打分做了尽量公平的对照。
- 用专家视觉图灵测试评估生成质量,替代对医学图像不适用的 Inception Score。

## 局限
- 作者自述:像素级定量只是粗略指标 —— 标注只覆盖部分异常类型,假阳性估计不可靠,"假阳性"可能是未标注的真异常。
- 只在 64×64 小图块上工作;临床医生看的是整张 B-scan,图灵测试结果不能推到整幅图;全幅生成留待以后。
- 作者明确前提:需要**大量正常数据**,且**测试分布等于训练分布** —— 任何域偏移都会被当成异常。
- 单器官、单设备、单一异常类型(积液);依赖层分割预处理。
- 作者定位它主要用于正常/异常区分与**粗定位**(作为专家复核的 region proposal),而非精确分割。

## 与本研究方向的关系
f-AnoGAN 是"学正常 → 摊销式投影回正常流形 → 读残差"的工程化版本,对本方向有两层意义。**第一,作为 virtual tissue 的雏形**:E 把任何观测压到"正常 latent",G 把它还原成"若健康会是什么样",G(E(x)) − x 就是 revert 方向 —— 这与 MrVI 的 counterfactual("如果这个细胞来自另一个样本会怎样")是同一种思路,只是 f-AnoGAN 没有条件变量、也不区分细胞状态与样本效应。**第二,作为伪影注入课题的必备基线**。**映射到肾脏组学**:训练集 = KPMP/HuBMAP 健康参考的 snRNA 细胞(特征可以是 scVI latent 或基础模型嵌入)或健康 H&E 图块;打分 = 表达/图块的重建残差 + 判别器特征残差。**哪些假设会断**:作者自己写明的"测试分布等于训练分布"在多中心肾活检上不成立 —— 批次、测序深度、组织保存方式都会推高残差,必须先像 MapQC(refmap-eval)那样用参考内部的样本间变异作为零分布;ambient RNA 与 doublet、Xenium 的转录本溢出与分割错误(见 xenium-split、ovrlpy)都会产生"离开正常流形"的谱,与真实病变同样得高分;PT 损伤是连续轴(见 damage-scores 的连续损伤分数),f-AnoGAN 的残差也是连续量,需要校准阈值;OCT 有像素级积液标注,肾脏数据没有对应的细胞级金标准 —— KidneyAnomalyBench 的专家判定正好补这个空。**跨模态一致性**:对同一 Xenium 切片,分别用 H&E 图块和表达谱训练两个 f-AnoGAN,只把两个残差**同时**高的区域当作疾病候选,单模态高残差当作伪影候选 —— 这是伪影注入课题把 f-AnoGAN 从"异常检测器"升级为"伪影/疾病判别器"的最直接做法。**仓库里已有的证据**:MEATRD 把 f-AnoGAN 当图像基线,在视觉上难分辨的乳腺肿瘤边缘 precision/recall 都是 0;AnoPILaD(histo-miccai-2025)中 f-AnoGAN 在淋巴结 LH 与 Camelyon16 上 AUC 仅 0.229 / 0.174(低于随机);MedIAnomaly 也指出不用 ImageNet 权重时多数 AE/GAN 方法在 Camelyon16 上基本失效。结论:在肾脏组织上它应作为**必须报告的经典基线**,而不是主力方法。

## 可复用资产
- **代码:** 官方 TensorFlow 1.2 / Python 2.7 实现(WGAN-GP 训练、izi_f 编码器训练、异常打分),仓库内附接受稿 PDF。
<https://github.com/tSchlegl/f-AnoGAN>
- **数据:** 临床 OCT 未公开。
- **评测协议:** 表 1 的指标组合(Youden 点 precision/sensitivity/specificity/F1 + AUC)与"视觉图灵测试"思路 —— 后者可改造成让肾脏病理医生盲评"生成的正常 vs 真实正常",检验正常模型是否真的覆盖了健康变异。

## 待读
- AnoGAN 原文(本仓库 anogan-ipmi-2017)。
- Simarro Viana 等的 3D f-AnoGAN(MedIAnomaly 中提及),对体数据/切片堆叠有参考价值。
- AnoDDPM 与 Wolleb 等 2022(本仓库 diffusion-medical-ad-miccai-2022):扩散模型如何在同一范式里取代 GAN。

## 引用
```bibtex
@article{Schlegl_2019, title={f-AnoGAN: Fast unsupervised anomaly detection with generative adversarial networks}, volume={54}, ISSN={1361-8415}, url={http://dx.doi.org/10.1016/j.media.2019.01.010}, DOI={10.1016/j.media.2019.01.010}, journal={Medical Image Analysis}, publisher={Elsevier BV}, author={Schlegl, Thomas and Seeböck, Philipp and Waldstein, Sebastian M. and Langs, Georg and Schmidt-Erfurth, Ursula}, year={2019}, month=May, pages={30–44} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

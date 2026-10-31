# DRÆM – A discriminatively trained reconstruction embedding for surface anomaly detection

> **文献键** `Zavrtanik2021_210807610` · **来源** 2021 IEEE/CVF International Conference on Computer Vision (ICCV)(2021) · **类别** anomaly · **相关度** medium · **获取** open
> **链接** <https://arxiv.org/abs/2108.07610> · `status: complete`

---

## 一句话
DRÆM 把表面异常检测从"只学正常、看重建误差"改成**判别问题**:在正常图像上用 Perlin 噪声 mask + 外部纹理贴出"刚好越界(just-out-of-distribution)"的合成异常,同时训练一个把异常修复回正常的重建子网络和一个读取"原图 ⊕ 重建图"并输出像素级异常图的判别子网络;MVTec AD 图像级 AUROC 98.0%、像素 AP 68.4%,比此前最好方法分别高 2.5 和 13.4 个百分点。

## 研究问题
表面异常只占图像很小一部分,且往往离正常分布很近。重建类方法(AE、GAN、AnoGAN/f-AnoGAN)只在正常数据上训练,依赖"异常重建不好"这一假设,但对接近正常的异常常常重建得很好(过度泛化),而且需要手工设计的后处理(如 SSIM 比较)来出异常图,无法为检测目标直接优化特征。反过来,直接在合成异常上训练分割网络又会**过拟合合成外观**,对真实缺陷泛化差。DRÆM 要解决的是:不依赖真实异常、又能端到端判别式训练且泛化到真实异常。

## 方法
**重建子网络**:encoder–decoder,输入是被模拟器破坏的图像 I_a,目标是还原原始正常图像 I,损失为 λ·SSIM 损失 + L2(SSIM 用来考虑邻域像素相关)。它学会"把局部异常模式改写成正常模式、正常区域保持不变"。**判别子网络**:U-Net 式结构,输入为 I_a 与重建 I_r 的通道拼接;因为重建子网络会把异常处"修正常",二者的联合外观在异常处差异显著,判别网络因此**学习一个与局部外观相关的距离函数**而非手工 SSIM;用 Focal Loss 监督像素 mask。总损失 = L_rec + L_seg。**异常模拟器**:Perlin 噪声生成随机形状并以随机阈值二值化为 mask M_a;纹理来源是与目标域无关的 DTD 纹理数据集,经 RandAugment 风格的 3 个随机增强(posterize、sharpness、solarize、equalize、亮度、颜色、auto-contrast 中抽取);按 I_a = M̄_a⊙I + (1−β)(M_a⊙I) + β(M_a⊙A) 混合,不透明度 β∈[0.1,1.0] 随机——低 β 产生"轻微扰动",用于收紧决策边界。模拟器同时给出像素完美的 mask。**推理**:异常图 M_o 经 s_f×s_f 均值滤波后取最大值为图像分数 η。训练 700 epoch,lr 1e-4(400/600 epoch 各乘 0.1),正常图像做 (−45°,45°) 旋转增强。

## 方法谱系
**范式:synthetic anomalies / self-supervised**(以重建子网络为辅助的混合体,但核心判别信号来自合成异常)。**承接**:重建路线(Bergmann 等 SSIM-AE、GANomaly、AnoGAN、f-AnoGAN —— 论文在相关工作中引用并作为对照)以及作者自己的 RIAD(inpainting 重建);同时期的 CutPaste 也是合成异常 + 自监督。DRÆM 的关键差异是:合成异常**不需要逼真**,只需"刚好越界",判别器学的是"偏离正常的程度"而非异常外观。**影响**:成为 synthetic-anomaly 家族的标准基线(pathology-ad-bench-mlhealth-2025 把 DRAEM 与 CutPaste 一起列为 synthetic anomaly 方法评测;medianomaly-media-2025 的一阶段 SSL 家族 FPI/NSA/PII/AnatPaste 与它同一思路);后续工业 AD 的许多合成异常方法沿用了它的 Perlin-mask + 外部纹理模拟器。

## 数据
**MVTec AD**(15 类,只用正常图训练);**DAGM 2007**(10 类人工生成纹理,缺陷用椭圆粗标,用于和监督方法比较,只评图像分类)。合成异常的纹理源:**DTD**(Describable Textures Dataset);消融中替换为 ImageNet。

## 主要结果
- **图像级检测(MVTec AUROC)**:DRÆM 平均 **98.0%**,15 类中 9 类最高;对比 PaDiM 95.5%、Rippel 等 (MAD) 94.4%、RIAD 91.7%、Uninformed Students 87.7%、GANomaly 78.2%。较弱类:transistor 93.1%、cable 91.8%(缺失部件类异常最难)。
- **定位(像素 AUROC / AP)**:DRÆM 97.3 / **68.4**,PaDiM 97.4 / 55.0,RIAD 94.2 / 48.2,US 93.9 / 45.5 —— AUROC 持平,AP 高 13.4 个百分点;作者强调在异常像素极少时 AUROC 被大量正常像素主导,AP 更合适。
- **消融(检测 / 定位 AUROC / AP)**:只有判别网络 93.9 / 92.7 / 62.5(过拟合合成异常);只有重建网络 + SSIM 83.9 / 89.7 / 47.5;换成监督缺陷网络 Božič 等 92.8 / 93.9 / 60.7;纹理源换 ImageNet 97.9 / 97.0 / 67.9;**纯色块替代纹理**仍有 96.2 / 92.6 / 56.5;矩形 mask 替代 Perlin 96.9 / 96.8 / 65.1;去掉增强与不透明度随机化 97.4 / 94.5 / 64.3;只保留 β 随机化 97.9 / 97.1 / 68.4。少于 10 张纹理图即可达到高性能。
- **DAGM**:DRÆM 图像 AUROC 99.0%、分类准确率 98.5%,无监督方法中最好(PaDiM 95.0% / 95.7%),接近全监督方法(Božič 等 100%),且定位优于用粗标训练的监督方法。

## 创新点
- 把表面 AD 主要表述为**判别问题**,用"原图 + 重建图"的联合嵌入学习距离函数,无需手工后处理。
- **"刚好越界"合成异常**原则:模拟器不需逼真,Perlin mask + 无关纹理 + 随机不透明度足矣 —— 消融显示纯色块也能达到 SOTA 级别。
- 像素级 AP 作为极度不平衡定位任务的更合适指标。

## 局限
- 缺失部件 / 与背景相似的异常难以检测(如 transistor 断脚);部分误差来自真值 mask 本身模糊。
- 需要从头训练两个网络 700 epoch,每类一个模型;比 PaDiM/PatchCore 这类免训练方法昂贵得多。
- 模拟器是为**纹理/外观**异常设计的(局部贴图),对逻辑/结构异常(缺件、错位)或语义层面的异常没有对应机制。
- "合成异常不需逼真"只在工业表面数据上验证;是否能迁移到复杂组织形态未知。

## 与本研究方向的关系
DRÆM 对伪影注入课题最有价值的不是网络,而是**"用已知真值的合成扰动来训练和评测"这一思路**,它直接对应 KidneyAnomalyBench 的"有真值层"。**映射到肾脏组学**:样本 = 细胞 / spot;正常训练集 = 健康参考;"Perlin mask" = 在 Xenium/Visium 切片上随机选取的空间连通区域;"外部纹理贴图" = 在该区域内注入表达偏移(例如把一组基因按损伤方向缩放、混入另一个细胞类型的表达、改变细胞密度或细胞组成);"不透明度 β" = 扰动强度,低 β 对应亚临床的轻度改变;H&E 端可原样使用 Perlin + 纹理模拟器做 patch 级合成异常。重建子网络对应"把一个细胞/邻域还原到健康状态"的模型 —— 这恰好也是 revert 阶段想要的东西:**重建出的"健康版本"与原始观测之差,就是需要被逆转的变化**。**哪些假设会破**:(1) DRÆM 的模拟器不需逼真,是因为工业缺陷就是局部外观变化;而肾脏疾病(纤维化、PT 损伤)是**连续、弥散**的状态变化,"刚好越界"的边界很难定义,判别器可能学到的是合成扰动的特征签名而非疾病;(2) 合成扰动若与技术伪影(ambient RNA 的"混入别的细胞类型表达"、doublet 的"两种细胞混合"、分割误差导致的转录本错配)形态相同,模型会把伪影与疾病混为一类 —— 反过来,这也是机会:**可以有意把 ambient/doublet/分割错误作为一类合成"伪影"、把损伤方向扰动作为另一类,训练模型区分二者**,这与伪影注入课题的跨模态伪影 vs 疾病区分直接对应;(3) 组学无像素 mask,但合成扰动天然自带 mask,正好补上 PRO/AP 类指标。**仓库里已有的同类思想**:pathology-ad-bench-mlhealth-2025 直接评测 DRAEM,并用"在正常 Unitopatho 块上叠加图案"构造了已知真值的合成病理数据集;medianomaly-media-2025 系统比较了 CutPaste、FPI、NSA、PII、AnatPaste 这类合成异常 SSL 方法,发现分割任务上重建类明显优于 SSL 类(朴素 AE 在 BraTS2021 上胜过所有一阶段 SSL 分割法),且**合成异常越逼真越好**(两阶段 AnatPaste 比 CutPaste 在 RSNA 上 AUC 高 20.2%)—— 这与 DRÆM「不需逼真」的结论相反,是对 DRÆM 式方法在生物医学上的重要警示;ambient-rna-bench-biorxiv-2026 / xenium-split-natmethods-2026 / ovrlpy-natbiotech-2026 提供的伪影模型可作为"伪影型合成扰动"的生成器。

## 可复用资产
- **代码:** 官方 PyTorch 实现(训练、评测,并提供 MVTec 各类预训练模型)。
<https://github.com/VitjanZ/DRAEM>
- **库:** anomalib 中的 DRAEM 实现(pathology-ad-bench-mlhealth-2025 使用)。
<https://github.com/open-edge-platform/anomalib>
- **模拟器配方:** Perlin mask(随机阈值)+ 外部纹理 + 3 个随机增强 + β∈[0.1,1] 混合 —— 可改写为组学空间切片上的"区域 × 表达扰动 × 强度"生成器。
- **数据:** DTD 纹理数据集(异常源)。

## 待读
- CutPaste(Li 等 CVPR 2021)—— 同期的合成异常自监督方法,对照阅读。
- 作者的 RIAD(Pattern Recognition 2020)与后续 DSR(双子空间重投影,针对接近正常的异常)。
- 设计 KidneyAnomalyBench 的合成扰动层:损伤方向扰动 vs ambient/doublet/分割伪影扰动,两类各带空间 mask。

## 引用
```bibtex
@inproceedings{Zavrtanik2021_210807610,
  title = {{DR{\AE}M} -- A Discriminatively Trained Reconstruction Embedding for Surface Anomaly Detection},
  author = {Zavrtanik, Vitjan and Kristan, Matej and Sko{\v{c}}aj, Danijel},
  booktitle = {2021 IEEE/CVF International Conference on Computer Vision (ICCV)},
  pages = {8310--8319},
  publisher = {IEEE},
  year = {2021},
  doi = {10.1109/ICCV48922.2021.00822},
  eprint = {2108.07610},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2108.07610}
}
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**

# Glossary / 术语表

> 92 medical & machine-learning terms, each with an **English / 中文 / Deutsch** name and definition. Grows with the library; edit `glossary/terms.yaml` then run `python scripts/build_glossary.py`.

## Histopathology / 组织病理

### Cellularity · 细胞密度 · Zellularität

- **EN** — The proportion of a tissue, such as bone marrow, that is occupied by cells rather than fat or stroma.
- **中文** — 组织(如骨髓)中被细胞而非脂肪或间质所占据的比例。
- **DE** — Der Anteil eines Gewebes, etwa des Knochenmarks, der von Zellen statt von Fett oder Stroma eingenommen wird.
- _Seen in / 出现于:_ [`pathomics-blood-2023`](papers/pathomics-blood-2023/index.md)

### Computational pathology · 计算病理学 · Computationale Pathologie

- **EN** — The use of machine learning and image analysis to extract diagnostic and prognostic information from digitized pathology slides.
- **中文** — 运用机器学习与图像分析,从数字化病理切片中提取诊断与预后信息的领域。
- **DE** — Der Einsatz von maschinellem Lernen und Bildanalyse, um diagnostische und prognostische Informationen aus digitalisierten Pathologieschnitten zu gewinnen.
- _Seen in / 出现于:_ [`histo-sciencedirect-2026`](papers/histo-sciencedirect-2026/index.md), [`uni2-h-model`](papers/uni2-h-model/index.md), [`virchow-2024`](papers/virchow-2024/index.md)

### FFPE tissue · 福尔马林固定石蜡包埋组织 · FFPE-Gewebe

- **EN** — Formalin-fixed, paraffin-embedded tissue, a standard preservation method that lets specimens be stored long-term and cut into thin sections.
- **中文** — 福尔马林固定、石蜡包埋的组织,是一种标准保存方法,便于样本长期保存并切成薄片。
- **DE** — Formalin-fixiertes, in Paraffin eingebettetes Gewebe, eine Standardkonservierung, die eine langfristige Lagerung und das Schneiden dünner Schnitte ermöglicht.
- _Seen in / 出现于:_ [`fm-arxiv-2604`](papers/fm-arxiv-2604/index.md), [`hest1k-2024`](papers/hest1k-2024/index.md)

### H&E staining · 苏木精-伊红染色 · Hämatoxylin-Eosin-Färbung

- **EN** — A routine tissue stain that colors cell nuclei blue-purple (hematoxylin) and cytoplasm pink (eosin), forming the standard visual basis for histological diagnosis.
- **中文** — 一种常规组织染色法,用苏木精把细胞核染成蓝紫色、伊红把细胞质染成粉红色,是组织学诊断的标准视觉基础。
- **DE** — Eine Routine-Gewebefärbung, die Zellkerne blau-violett (Hämatoxylin) und Zytoplasma rosa (Eosin) darstellt und die visuelle Standardgrundlage der histologischen Diagnostik bildet.
- _Seen in / 出现于:_ [`fm-arxiv-2604`](papers/fm-arxiv-2604/index.md), [`hest1k-2024`](papers/hest1k-2024/index.md), [`histo-miccai-2025`](papers/histo-miccai-2025/index.md), [`histo-nejmai-2024`](papers/histo-nejmai-2024/index.md), [`histo-sciencedirect-2026`](papers/histo-sciencedirect-2026/index.md), [`virchow-2024`](papers/virchow-2024/index.md)

### Histopathology · 组织病理学 · Histopathologie

- **EN** — The microscopic examination of tissue sections to diagnose and characterize disease.
- **中文** — 通过显微镜检查组织切片来诊断和刻画疾病的学科。
- **DE** — Die mikroskopische Untersuchung von Gewebeschnitten zur Diagnose und Charakterisierung von Krankheiten.
- _Seen in / 出现于:_ [`histo-anomaly-bi-repo`](papers/histo-anomaly-bi-repo/index.md), [`histo-miccai-2025`](papers/histo-miccai-2025/index.md), [`histo-nejmai-2024`](papers/histo-nejmai-2024/index.md), [`histo-sciencedirect-2026`](papers/histo-sciencedirect-2026/index.md), [`virchow-2024`](papers/virchow-2024/index.md)

### Immunohistochemistry (IHC) · 免疫组织化学 · Immunhistochemie

- **EN** — A staining technique that uses antibodies to reveal the location of specific proteins in a tissue section.
- **中文** — 一种利用抗体显示组织切片中特定蛋白位置的染色技术。
- **DE** — Eine Färbetechnik, die mithilfe von Antikörpern die Lokalisation bestimmter Proteine in einem Gewebeschnitt sichtbar macht.
- _Seen in / 出现于:_ [`fm-arxiv-2604`](papers/fm-arxiv-2604/index.md), [`uni2-h-model`](papers/uni2-h-model/index.md)

### Microsatellite instability (MSI) · 微卫星不稳定性 · Mikrosatelliteninstabilität

- **EN** — A hypermutable tumor state caused by defective DNA mismatch repair, widely used as a diagnostic and immunotherapy biomarker.
- **中文** — 由 DNA 错配修复缺陷导致的高突变肿瘤状态,广泛用作诊断与免疫治疗的生物标志物。
- **DE** — Ein hypermutabler Tumorzustand infolge defekter DNA-Mismatch-Reparatur, weit verbreitet als diagnostischer und immuntherapeutischer Biomarker.
- _Seen in / 出现于:_ [`histo-sciencedirect-2026`](papers/histo-sciencedirect-2026/index.md)

### Nuclear morphometry · 细胞核形态测量 · Kernmorphometrie

- **EN** — Quantitative measurement of the shape, size, texture and color of segmented cell nuclei to characterize tissue.
- **中文** — 对分割出的细胞核在形状、大小、纹理和颜色上进行定量测量,以刻画组织特征。
- **DE** — Die quantitative Messung von Form, Größe, Textur und Farbe segmentierter Zellkerne zur Charakterisierung von Gewebe.
- _Seen in / 出现于:_ [`hest1k-2024`](papers/hest1k-2024/index.md), [`pathomics-blood-2023`](papers/pathomics-blood-2023/index.md)

### Pan-cancer detection · 泛癌检测 · Pan-Krebs-Detektion

- **EN** — Detecting the presence of cancer across many tumor types with a single model instead of one model per cancer type.
- **中文** — 用单一模型跨多种肿瘤类型检测癌症,而非为每种癌种单独训练模型。
- **DE** — Der Nachweis von Krebs über viele Tumortypen hinweg mit einem einzigen Modell statt eines Modells pro Krebsart.
- _Seen in / 出现于:_ [`virchow-2024`](papers/virchow-2024/index.md)

### Pathomics · 病理组学 · Pathomics

- **EN** — The extraction of large numbers of quantitative features from pathology images for statistical and predictive analysis.
- **中文** — 从病理图像中提取大量定量特征,用于统计与预测分析。
- **DE** — Die Extraktion einer großen Zahl quantitativer Merkmale aus Pathologiebildern für statistische und prädiktive Analysen.
- _Seen in / 出现于:_ [`pathomics-blood-2023`](papers/pathomics-blood-2023/index.md), [`pathomics-repo`](papers/pathomics-repo/index.md)

### Tile / patch · 图块 / 小块 · Kachel / Patch

- **EN** — A small fixed-size sub-image (e.g. 224x224 pixels) cropped from a whole-slide image so that models can process the huge slide piece by piece.
- **中文** — 从全切片图像中裁出的固定尺寸小图(如 224×224 像素),使模型能够逐块处理巨大的切片。
- **DE** — Ein kleines, festgroßes Teilbild (z. B. 224x224 Pixel), das aus einem Whole-Slide-Image herausgeschnitten wird, damit Modelle den riesigen Schnitt stückweise verarbeiten können.
- _Seen in / 出现于:_ [`fm-arxiv-2604`](papers/fm-arxiv-2604/index.md), [`hest1k-2024`](papers/hest1k-2024/index.md), [`histo-miccai-2025`](papers/histo-miccai-2025/index.md), [`histo-nejmai-2024`](papers/histo-nejmai-2024/index.md), [`pathomics-repo`](papers/pathomics-repo/index.md), [`uni2-h-model`](papers/uni2-h-model/index.md), [`virchow-2024`](papers/virchow-2024/index.md)

### Tissue segmentation · 组织分割 · Gewebesegmentierung

- **EN** — Partitioning a pathology image into regions labeled by tissue type or separating tissue from background.
- **中文** — 将病理图像划分为按组织类型标注的区域,或把组织与背景分开。
- **DE** — Die Aufteilung eines Pathologiebildes in nach Gewebetyp beschriftete Regionen oder die Trennung von Gewebe und Hintergrund.
- _Seen in / 出现于:_ [`hest1k-2024`](papers/hest1k-2024/index.md), [`histo-sciencedirect-2026`](papers/histo-sciencedirect-2026/index.md), [`pathomics-blood-2023`](papers/pathomics-blood-2023/index.md)

### Virtual staining · 虚拟染色 · Virtuelle Färbung

- **EN** — Computationally generating one stain modality (e.g. IHC) from another (e.g. H&E) without physically re-staining the tissue.
- **中文** — 在不对组织进行物理再染色的情况下,用计算方法从一种染色(如 H&E)生成另一种染色(如 IHC)。
- **DE** — Die rechnergestützte Erzeugung einer Färbemodalität (z. B. IHC) aus einer anderen (z. B. H&E), ohne das Gewebe physisch neu zu färben.
- _Seen in / 出现于:_ [`fm-arxiv-2604`](papers/fm-arxiv-2604/index.md)

## Spatial omics / 空间组学

### Anomalous tissue domain (ATD) · 异常组织域(ATD) · Anomale Gewebedomäne (ATD)

- **EN** — A spatial region of a tissue whose molecular profile deviates from healthy reference tissue, typically because of disease and detected without predefined markers.
- **中文** — 组织中分子特征偏离健康参考组织的空间区域,通常由疾病导致,可在无预定义标记物的情况下被检出。
- **DE** — Eine räumliche Gewebsregion, deren molekulares Profil vom gesunden Referenzgewebe abweicht, meist krankheitsbedingt und ohne vordefinierte Marker erkennbar.
- _Seen in / 出现于:_ [`spatial-natcommun-2024`](papers/spatial-natcommun-2024/index.md)

### Cell segmentation · 细胞分割 · Zellsegmentierung

- **EN** — The image-analysis step of delineating individual cell boundaries so that molecular signals can be assigned to single cells.
- **中文** — 在图像分析中勾勒单个细胞边界的步骤,以便将分子信号归属到单个细胞。
- **DE** — Der bildanalytische Schritt, einzelne Zellgrenzen abzugrenzen, damit molekulare Signale einzelnen Zellen zugeordnet werden können.
- _Seen in / 出现于:_ [`hest1k-2024`](papers/hest1k-2024/index.md), [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md)

### Cellular niche · 细胞微环境龛位(niche) · Zelluläre Nische

- **EN** — A local neighborhood of cells whose spatial composition and interactions define a distinct micro-environment within a tissue.
- **中文** — 由细胞的空间组成与相互作用界定的局部细胞邻域,构成组织内一个独特的微环境。
- **DE** — Eine lokale Zellnachbarschaft, deren räumliche Zusammensetzung und Interaktionen ein eigenes Mikromilieu im Gewebe definieren.
- _Seen in / 出现于:_ [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md), [`virtual-tissue-2501`](papers/virtual-tissue-2501/index.md)

### Imaging mass cytometry (IMC) · 成像质谱流式(IMC) · Bildgebende Massenzytometrie (IMC)

- **EN** — A multiplexed imaging method that uses metal-tagged antibodies and mass spectrometry to map dozens of proteins across a tissue section at subcellular resolution.
- **中文** — 一种多重成像方法,利用金属标记抗体与质谱在亚细胞分辨率下绘制组织切片中数十种蛋白质。
- **DE** — Eine multiplexierte Bildgebungsmethode, die metallmarkierte Antikörper und Massenspektrometrie nutzt, um Dutzende Proteine in einem Gewebeschnitt mit subzellulärer Auflösung zu kartieren.
- _Seen in / 出现于:_ [`virtual-tissue-2501`](papers/virtual-tissue-2501/index.md)

### Multiplexed imaging · 多重成像 · Multiplex-Bildgebung

- **EN** — Imaging that captures many molecular channels (proteins or transcripts) in the same tissue section rather than just one or two stains.
- **中文** — 在同一组织切片中捕获多个分子通道(蛋白质或转录本)的成像,而非仅一两种染色。
- **DE** — Bildgebung, die viele molekulare Kanäle (Proteine oder Transkripte) im selben Gewebeschnitt erfasst statt nur ein oder zwei Färbungen.
- _Seen in / 出现于:_ [`scrna-natmachintell-2026`](papers/scrna-natmachintell-2026/index.md), [`virtual-tissue-2501`](papers/virtual-tissue-2501/index.md)

### Slide-seq · Slide-seq · Slide-seq

- **EN** — A spatial-transcriptomics method that transfers tissue onto a bead array of positionally barcoded beads, giving near-cellular spatial resolution.
- **中文** — 一种将组织转移到带有位置条形码微珠阵列上的空间转录组方法,可达到接近单细胞的空间分辨率。
- **DE** — Eine Spatial-Transcriptomics-Methode, die Gewebe auf ein Array positionsbarcodierter Beads überträgt und nahezu zelluläre räumliche Auflösung erreicht.
- _Seen in / 出现于:_ [`spatial-natcommun-2024`](papers/spatial-natcommun-2024/index.md)

### Spatial proteomics · 空间蛋白质组学 · Räumliche Proteomik

- **EN** — The measurement of many proteins at once within their spatial context in a tissue, typically via multiplexed antibody imaging.
- **中文** — 在组织的空间背景下同时测量多种蛋白质,通常通过多重抗体成像实现。
- **DE** — Die gleichzeitige Messung vieler Proteine im räumlichen Gewebekontext, meist über multiplexierte Antikörper-Bildgebung.
- _Seen in / 出现于:_ [`virtual-tissue-2501`](papers/virtual-tissue-2501/index.md)

### Spatial transcriptomics · 空间转录组学 · Räumliche Transkriptomik

- **EN** — A family of technologies that measure gene expression while preserving each cell's or spot's position within an intact tissue section.
- **中文** — 一类在保留细胞或位点在完整组织切片中位置的同时测量基因表达的技术。
- **DE** — Eine Gruppe von Technologien, die die Genexpression messen und dabei die Position jeder Zelle oder jedes Spots im intakten Gewebeschnitt erhalten.
- _Seen in / 出现于:_ [`fm-arxiv-2604`](papers/fm-arxiv-2604/index.md), [`hest1k-2024`](papers/hest1k-2024/index.md), [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md), [`spatial-natcommun-2024`](papers/spatial-natcommun-2024/index.md)

### Stereo-seq · Stereo-seq · Stereo-seq

- **EN** — A high-resolution spatial-transcriptomics platform using nanoball-patterned arrays that can resolve gene expression down to subcellular scale over large tissue areas.
- **中文** — 一种基于纳米球阵列的高分辨率空间转录组平台,可在大面积组织上将基因表达分辨到亚细胞尺度。
- **DE** — Eine hochauflösende Spatial-Transcriptomics-Plattform mit Nanoball-Arrays, die Genexpression über große Gewebeflächen bis in den subzellulären Bereich auflöst.
- _Seen in / 出现于:_ [`spatial-natcommun-2024`](papers/spatial-natcommun-2024/index.md)

### Visium · Visium · Visium

- **EN** — A widely used 10x Genomics spatial-transcriptomics platform that captures gene expression on a grid of barcoded spots overlaid on a tissue slide.
- **中文** — 一种广泛使用的 10x Genomics 空间转录组平台,在覆盖组织切片的条形码位点阵列上捕获基因表达。
- **DE** — Eine weit verbreitete Spatial-Transcriptomics-Plattform von 10x Genomics, die Genexpression auf einem Raster barcodierter Spots über einem Gewebeschnitt erfasst.
- _Seen in / 出现于:_ [`hest1k-2024`](papers/hest1k-2024/index.md), [`spatial-natcommun-2024`](papers/spatial-natcommun-2024/index.md)

### Xenium · Xenium · Xenium

- **EN** — A 10x Genomics imaging-based platform that measures a targeted panel of transcripts in situ at subcellular resolution with single-cell segmentation.
- **中文** — 一种基于成像的 10x Genomics 平台,在亚细胞分辨率下原位测量目标转录本组合,并进行单细胞分割。
- **DE** — Eine bildgebungsbasierte 10x-Genomics-Plattform, die ein gezieltes Transkript-Panel in situ mit subzellulärer Auflösung und Einzelzell-Segmentierung misst.
- _Seen in / 出现于:_ [`hest1k-2024`](papers/hest1k-2024/index.md), [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md)

## Single-cell / 单细胞

### Cell state · 细胞状态 · Zellzustand

- **EN** — The transient functional condition of a cell — such as activated, exhausted, or proliferating — layered on top of its stable cell-type identity.
- **中文** — 细胞在其稳定的细胞类型身份之上所处的、可变的功能状态,如激活、耗竭或增殖。
- **DE** — Der vorübergehende funktionelle Zustand einer Zelle — etwa aktiviert, erschöpft oder proliferierend — der ihrer stabilen Zelltyp-Identität überlagert ist.
- _Seen in / 出现于:_ [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md), [`virtual-cell-challenge`](papers/virtual-cell-challenge/index.md)

### CRISPR perturbation · CRISPR 扰动 · CRISPR-Perturbation

- **EN** — The deliberate silencing, activation, or editing of a target gene using CRISPR to observe the resulting change in cell state.
- **中文** — 利用 CRISPR 对目标基因进行定向沉默、激活或编辑,以观察由此引起的细胞状态变化。
- **DE** — Das gezielte Stilllegen, Aktivieren oder Editieren eines Zielgens mittels CRISPR, um die daraus folgende Änderung des Zellzustands zu beobachten.
- _Seen in / 出现于:_ [`virtual-cell-challenge`](papers/virtual-cell-challenge/index.md)

### Gene-expression signature · 基因表达签名 · Genexpressionssignatur

- **EN** — A defined set of genes whose coordinated expression levels mark a particular cell state, disease, or treatment response.
- **中文** — 一组特定基因,其协同表达水平可标志某种细胞状态、疾病或治疗响应。
- **DE** — Eine definierte Gruppe von Genen, deren koordinierte Expressionsniveaus einen bestimmten Zellzustand, eine Krankheit oder eine Therapieantwort kennzeichnen.
- _Seen in / 出现于:_ [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md), [`virtual-tissue-2501`](papers/virtual-tissue-2501/index.md)

### Perturb-seq · Perturb-seq · Perturb-seq

- **EN** — A screening method that pairs CRISPR perturbations with single-cell RNA sequencing to read out how each genetic perturbation reshapes the transcriptome.
- **中文** — 一种将 CRISPR 扰动与单细胞 RNA 测序结合的筛选方法,可读出每个基因扰动如何重塑转录组。
- **DE** — Eine Screening-Methode, die CRISPR-Perturbationen mit Einzelzell-RNA-Sequenzierung koppelt, um zu erfassen, wie jede genetische Störung das Transkriptom verändert.
- _Seen in / 出现于:_ [`virtual-cell-challenge`](papers/virtual-cell-challenge/index.md)

### Perturbation-response prediction · 扰动响应预测 · Vorhersage der Perturbationsantwort

- **EN** — The task of predicting how a cell's gene expression will shift after a given genetic or drug perturbation, often for unseen conditions.
- **中文** — 预测给定基因或药物扰动后细胞基因表达如何变化的任务,通常针对未见过的条件。
- **DE** — Die Aufgabe vorherzusagen, wie sich die Genexpression einer Zelle nach einer bestimmten genetischen oder medikamentösen Störung verschiebt, oft für ungesehene Bedingungen.
- _Seen in / 出现于:_ [`scrna-natmachintell-2026`](papers/scrna-natmachintell-2026/index.md), [`virtual-cell-challenge`](papers/virtual-cell-challenge/index.md)

### Single-cell RNA sequencing (scRNA-seq) · 单细胞 RNA 测序(scRNA-seq) · Einzelzell-RNA-Sequenzierung (scRNA-seq)

- **EN** — A technique that profiles the transcriptome of individual cells, revealing cell-type heterogeneity that bulk sequencing averages away.
- **中文** — 一种对单个细胞转录组进行测序的技术,可揭示被批量测序平均掉的细胞类型异质性。
- **DE** — Eine Technik, die das Transkriptom einzelner Zellen erfasst und die Zelltyp-Heterogenität sichtbar macht, die bei Bulk-Sequenzierung verloren geht.
- _Seen in / 出现于:_ [`scrna-natmachintell-2026`](papers/scrna-natmachintell-2026/index.md), [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md), [`spatial-natcommun-2024`](papers/spatial-natcommun-2024/index.md)

### Virtual cell · 虚拟细胞 · Virtuelle Zelle

- **EN** — A computational model of a cell that predicts how its molecular state responds to perturbations, enabling experiments to be run in silico.
- **中文** — 细胞的计算模型,可预测其分子状态对扰动的响应,从而在计算机中开展实验。
- **DE** — Ein rechnerisches Zellmodell, das vorhersagt, wie der molekulare Zustand einer Zelle auf Störungen reagiert, und Experimente in silico ermöglicht.
- _Seen in / 出现于:_ [`virtual-cell-challenge`](papers/virtual-cell-challenge/index.md)

## Oncology & clinical / 肿瘤与临床

### Concordance index (C-index) · 一致性指数(C-index) · Konkordanzindex (C-Index)

- **EN** — A metric for survival models that measures how often the model correctly ranks which of two patients experiences the event sooner.
- **中文** — 用于生存模型的指标,衡量模型正确判断两名患者中谁更早发生事件的比例。
- **DE** — Eine Kennzahl für Überlebensmodelle, die misst, wie oft das Modell korrekt einordnet, welcher von zwei Patienten das Ereignis früher erlebt.
- _Seen in / 出现于:_ [`histo-sciencedirect-2026`](papers/histo-sciencedirect-2026/index.md), [`pathomics-npjpo-2026`](papers/pathomics-npjpo-2026/index.md), [`pathomics-repo`](papers/pathomics-repo/index.md), [`virtual-tissue-2501`](papers/virtual-tissue-2501/index.md)

### Immune checkpoint blockade (ICB) · 免疫检查点阻断(ICB) · Immun-Checkpoint-Blockade (ICB)

- **EN** — A cancer immunotherapy that blocks inhibitory receptors such as PD-1 or PD-L1 to release the brakes on anti-tumor T cells.
- **中文** — 一种癌症免疫治疗,通过阻断 PD-1 或 PD-L1 等抑制性受体来解除抗肿瘤 T 细胞的抑制。
- **DE** — Eine Krebs-Immuntherapie, die hemmende Rezeptoren wie PD-1 oder PD-L1 blockiert, um die Bremsen der Antitumor-T-Zellen zu lösen.
- _Seen in / 出现于:_ [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md), [`virtual-tissue-2501`](papers/virtual-tissue-2501/index.md)

### Overall survival (OS) · 总生存期(OS) · Gesamtüberleben (OS)

- **EN** — The length of time from diagnosis or treatment start until death from any cause, a primary endpoint in cancer studies.
- **中文** — 从确诊或开始治疗到因任何原因死亡的时间长度,是癌症研究的主要终点。
- **DE** — Die Zeitspanne von Diagnose oder Therapiebeginn bis zum Tod jeglicher Ursache, ein primärer Endpunkt in Krebsstudien.
- _Seen in / 出现于:_ [`pathomics-npjpo-2026`](papers/pathomics-npjpo-2026/index.md)

### Pathological complete response (pCR) · 病理完全缓解(pCR) · Pathologische Komplettremission (pCR)

- **EN** — The absence of any residual invasive tumor in tissue examined after neoadjuvant therapy, a favorable predictor of long-term outcome.
- **中文** — 新辅助治疗后所检组织中不存在任何残留浸润性肿瘤,是长期预后良好的指标。
- **DE** — Das Fehlen jeglichen residualen invasiven Tumors im nach neoadjuvanter Therapie untersuchten Gewebe, ein günstiger Prädiktor für den Langzeitverlauf.
- _Seen in / 出现于:_ [`virtual-tissue-2501`](papers/virtual-tissue-2501/index.md)

### Pathomics signature · 病理组学签名 · Pathomics-Signatur

- **EN** — A prognostic index built from quantitative features that deep-learning models extract directly from digitized histopathology slides.
- **中文** — 由深度学习模型直接从数字病理切片中提取的定量特征构建的预后指标。
- **DE** — Ein prognostischer Index aus quantitativen Merkmalen, die Deep-Learning-Modelle direkt aus digitalisierten Histopathologie-Schnitten extrahieren.
- _Seen in / 出现于:_ [`pathomics-npjpo-2026`](papers/pathomics-npjpo-2026/index.md)

### T-cell exhaustion · T 细胞耗竭 · T-Zell-Erschöpfung

- **EN** — A dysfunctional state in which chronically stimulated T cells lose their killing capacity and up-regulate inhibitory checkpoint markers.
- **中文** — 一种功能失调状态:长期受刺激的 T 细胞丧失杀伤能力并上调抑制性检查点标志物。
- **DE** — Ein dysfunktionaler Zustand, in dem chronisch stimulierte T-Zellen ihre zytotoxische Kapazität verlieren und hemmende Checkpoint-Marker hochregulieren.
- _Seen in / 出现于:_ [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md)

### Tertiary lymphoid structure (TLS) · 三级淋巴结构(TLS) · Tertiäre lymphoide Struktur (TLS)

- **EN** — An organized aggregate of immune cells that forms in chronically inflamed or tumor tissue and often associates with better anti-tumor immunity.
- **中文** — 在慢性炎症或肿瘤组织中形成的有序免疫细胞聚集体,常与更强的抗肿瘤免疫相关。
- **DE** — Ein organisiertes Aggregat von Immunzellen, das in chronisch entzündetem oder Tumorgewebe entsteht und oft mit besserer Antitumor-Immunität einhergeht.
- _Seen in / 出现于:_ [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md)

### Triple-negative breast cancer (TNBC) · 三阴性乳腺癌(TNBC) · Triple-negatives Mammakarzinom (TNBC)

- **EN** — An aggressive breast-cancer subtype lacking estrogen, progesterone, and HER2 receptors, which limits targeted-therapy options.
- **中文** — 一种侵袭性乳腺癌亚型,缺乏雌激素、孕激素和 HER2 受体,限制了靶向治疗选择。
- **DE** — Ein aggressiver Brustkrebs-Subtyp ohne Östrogen-, Progesteron- und HER2-Rezeptoren, was zielgerichtete Therapieoptionen einschränkt.
- _Seen in / 出现于:_ [`virtual-tissue-2501`](papers/virtual-tissue-2501/index.md)

### Tumor microenvironment (TME) · 肿瘤微环境(TME) · Tumormikromilieu (TME)

- **EN** — The ecosystem of immune, stromal, and vascular cells surrounding a tumor that shapes its growth and its response to therapy.
- **中文** — 环绕肿瘤的免疫、基质与血管细胞所构成的生态系统,影响肿瘤生长及其对治疗的响应。
- **DE** — Das Ökosystem aus Immun-, Stroma- und Gefäßzellen rund um einen Tumor, das dessen Wachstum und Therapieantwort prägt.
- _Seen in / 出现于:_ [`histo-sciencedirect-2026`](papers/histo-sciencedirect-2026/index.md), [`pathomics-blood-2023`](papers/pathomics-blood-2023/index.md), [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md), [`virtual-tissue-2501`](papers/virtual-tissue-2501/index.md)

### Whole-slide image (WSI) · 全切片图像(WSI) · Gesamtschnittbild (WSI)

- **EN** — A high-resolution digital scan of an entire histopathology glass slide, often gigapixel-sized, used for computational pathology.
- **中文** — 对整张组织病理玻片进行的高分辨率数字扫描,常达十亿像素级,用于计算病理学。
- **DE** — Ein hochauflösender digitaler Scan eines gesamten Histopathologie-Objektträgers, oft im Gigapixel-Bereich, für die computergestützte Pathologie.
- _Seen in / 出现于:_ [`hest1k-2024`](papers/hest1k-2024/index.md), [`histo-miccai-2025`](papers/histo-miccai-2025/index.md), [`histo-nejmai-2024`](papers/histo-nejmai-2024/index.md), [`histo-sciencedirect-2026`](papers/histo-sciencedirect-2026/index.md), [`pathomics-blood-2023`](papers/pathomics-blood-2023/index.md), [`pathomics-npjpo-2026`](papers/pathomics-npjpo-2026/index.md), [`pathomics-repo`](papers/pathomics-repo/index.md), [`uni2-h-model`](papers/uni2-h-model/index.md), [`virchow-2024`](papers/virchow-2024/index.md)

## Cardiology & imaging / 心脏与影像

### Echocardiography · 超声心动图 · Echokardiografie

- **EN** — Ultrasound imaging of the heart, the clinical gold standard for measuring ejection fraction and the source of the training labels here.
- **中文** — 对心脏的超声成像,是测量射血分数的临床金标准,也是本文训练标签的来源。
- **DE** — Ultraschallbildgebung des Herzens, der klinische Goldstandard zur Messung der Ejektionsfraktion und die Quelle der hier verwendeten Trainingslabels.
- _Seen in / 出现于:_ [`imaging-ehjdh-2026`](papers/imaging-ehjdh-2026/index.md)

### Electrocardiogram (ECG) · 心电图(ECG) · Elektrokardiogramm (EKG)

- **EN** — A recording of the heart's electrical activity over time as waveforms, used here as the raw input from which deep learning reads cardiac risk.
- **中文** — 记录心脏电活动随时间变化的波形图,本文用作深度学习读取心脏风险的原始输入。
- **DE** — Eine Aufzeichnung der elektrischen Herzaktivität als Wellenform über die Zeit, hier der Roheingang, aus dem Deep Learning das kardiale Risiko abliest.
- _Seen in / 出现于:_ [`imaging-nature-2026`](papers/imaging-nature-2026/index.md)

### Grad-CAM (gradient-weighted saliency) · Grad-CAM(梯度加权显著性) · Grad-CAM (gradientengewichtete Salienz)

- **EN** — An interpretability method that highlights the image regions most responsible for a model's prediction, here producing 3D saliency maps on CT.
- **中文** — 一种可解释性方法,标出对模型预测贡献最大的图像区域,本文用于生成 CT 的三维显著性图。
- **DE** — Eine Interpretierbarkeitsmethode, die die für eine Modellvorhersage wichtigsten Bildregionen hervorhebt, hier zur Erzeugung von 3D-Salienzkarten auf CT.
- _Seen in / 出现于:_ [`imaging-ehjdh-2026`](papers/imaging-ehjdh-2026/index.md)

### Heart failure with reduced ejection fraction (systolic dysfunction) · 射血分数降低的心力衰竭(收缩功能障碍) · Herzinsuffizienz mit reduzierter Ejektionsfraktion (systolische Dysfunktion)

- **EN** — A condition where the heart's weakened contraction lowers ejection fraction; catching it early lets guideline therapy slow progression.
- **中文** — 心脏收缩减弱导致射血分数下降的病症;早期发现可让指南导向治疗延缓病程。
- **DE** — Ein Zustand, bei dem die geschwächte Herzkontraktion die Ejektionsfraktion senkt; eine frühe Erkennung erlaubt es, mit leitliniengerechter Therapie das Fortschreiten zu verlangsamen.
- _Seen in / 出现于:_ [`imaging-ehjdh-2026`](papers/imaging-ehjdh-2026/index.md)

### Implantable cardioverter-defibrillator (ICD) · 植入式心律转复除颤器(ICD) · Implantierbarer Kardioverter-Defibrillator (ICD)

- **EN** — An implanted device that detects dangerous arrhythmias and delivers a shock to prevent sudden cardiac death.
- **中文** — 植入体内的装置,可检测危险的心律失常并放电,以预防心脏性猝死。
- **DE** — Ein implantiertes Gerät, das gefährliche Herzrhythmusstörungen erkennt und durch einen Schock den plötzlichen Herztod verhindert.
- _Seen in / 出现于:_ [`imaging-nature-2026`](papers/imaging-nature-2026/index.md)

### Left ventricular ejection fraction (LVEF) · 左心室射血分数(LVEF) · Linksventrikuläre Ejektionsfraktion (LVEF)

- **EN** — The percentage of blood pumped out of the left ventricle with each beat; a low value (e.g. <50%) signals reduced pumping function and heart failure.
- **中文** — 每次心跳时左心室泵出血液的百分比;数值偏低(如 <50%)提示泵血功能下降与心力衰竭。
- **DE** — Der Prozentsatz des Blutes, das die linke Herzkammer pro Schlag auswirft; ein niedriger Wert (z. B. <50 %) zeigt eine verminderte Pumpfunktion und Herzinsuffizienz an.
- _Seen in / 出现于:_ [`imaging-ehjdh-2026`](papers/imaging-ehjdh-2026/index.md), [`imaging-nature-2026`](papers/imaging-nature-2026/index.md)

### Non-contrast chest CT · 非增强胸部 CT · Native Thorax-CT (ohne Kontrastmittel)

- **EN** — A computed-tomography scan of the chest taken without injected contrast dye and without ECG gating, acquired routinely for many indications.
- **中文** — 不注射对比剂、也不做心电门控的胸部 CT 扫描,常规用于多种适应症。
- **DE** — Eine Computertomografie des Brustkorbs ohne injiziertes Kontrastmittel und ohne EKG-Triggerung, die routinemäßig für viele Fragestellungen erstellt wird.
- _Seen in / 出现于:_ [`imaging-ehjdh-2026`](papers/imaging-ehjdh-2026/index.md)

### Opportunistic screening · 机会性筛查 · Opportunistisches Screening

- **EN** — Extracting an unrelated diagnosis from data collected for another purpose — e.g. detecting heart failure from a CT ordered for something else.
- **中文** — 从为其他目的采集的数据中顺带发现无关疾病——例如从为别的原因所拍的 CT 中检出心力衰竭。
- **DE** — Das Gewinnen einer unabhängigen Diagnose aus Daten, die zu einem anderen Zweck erhoben wurden — z. B. das Erkennen einer Herzinsuffizienz aus einer für etwas anderes angeforderten CT.
- _Seen in / 出现于:_ [`imaging-ehjdh-2026`](papers/imaging-ehjdh-2026/index.md)

### Sudden cardiac death (SCD) · 心脏性猝死(SCD) · Plötzlicher Herztod (PHT)

- **EN** — Unexpected death from a cardiac cause, usually a fatal arrhythmia, within a short time of symptom onset; the outcome the ECG biomarker aims to predict.
- **中文** — 由心脏原因(通常是致命性心律失常)在症状出现后短时间内发生的意外死亡,即该 ECG 生物标志物要预测的终点。
- **DE** — Ein unerwarteter Tod kardialer Ursache, meist durch eine tödliche Herzrhythmusstörung, kurz nach Symptombeginn; das vom EKG-Biomarker vorhergesagte Ereignis.
- _Seen in / 出现于:_ [`imaging-nature-2026`](papers/imaging-nature-2026/index.md)

### Ventricular arrhythmia · 室性心律失常 · Ventrikuläre Arrhythmie

- **EN** — An abnormal, often life-threatening heart rhythm originating in the ventricles, the mechanistic cause of most sudden cardiac deaths.
- **中文** — 起源于心室的异常且常危及生命的心律,是大多数心脏性猝死的机制原因。
- **DE** — Ein abnormaler, oft lebensbedrohlicher Herzrhythmus, der in den Herzkammern entsteht und die mechanistische Ursache der meisten plötzlichen Herztode ist.
- _Seen in / 出现于:_ [`imaging-nature-2026`](papers/imaging-nature-2026/index.md)

## Foundation models / 基础模型

### Class token (CLS token) · 分类标记 · CLS-Token

- **EN** — A special learnable token in a transformer whose output vector serves as a summary embedding of the whole input.
- **中文** — Transformer 中一个特殊的可学习标记,其输出向量作为整个输入的汇总嵌入。
- **DE** — Ein spezielles lernbares Token in einem Transformer, dessen Ausgabevektor als zusammenfassende Einbettung der gesamten Eingabe dient.
- _Seen in / 出现于:_ [`fm-arxiv-2604`](papers/fm-arxiv-2604/index.md), [`uni2-h-model`](papers/uni2-h-model/index.md), [`virchow-2024`](papers/virchow-2024/index.md)

### DINOv2 · DINOv2 · DINOv2

- **EN** — A self-supervised training recipe combining self-distillation and masked image modeling to learn strong image features without labels.
- **中文** — 一种结合自蒸馏与掩码图像建模的自监督训练配方,无需标签即可学到强大的图像特征。
- **DE** — Ein selbstüberwachtes Trainingsverfahren, das Selbstdistillation und maskierte Bildmodellierung kombiniert, um ohne Beschriftungen starke Bildmerkmale zu lernen.
- _Seen in / 出现于:_ [`uni2-h-model`](papers/uni2-h-model/index.md), [`virchow-2024`](papers/virchow-2024/index.md)

### Masked image modeling · 掩码图像建模 · Maskierte Bildmodellierung

- **EN** — A self-supervised task in which the model learns by reconstructing deliberately hidden parts of an image.
- **中文** — 一种自监督任务,模型通过重建图像中被故意遮挡的部分来学习。
- **DE** — Eine selbstüberwachte Aufgabe, bei der das Modell lernt, indem es absichtlich verdeckte Bildteile rekonstruiert.
- _Seen in / 出现于:_ [`uni2-h-model`](papers/uni2-h-model/index.md)

### Self-supervised learning · 自监督学习 · Selbstüberwachtes Lernen

- **EN** — Training on unlabeled data by having the model create its own supervisory signal from the data itself.
- **中文** — 在无标注数据上训练,让模型从数据本身构造出监督信号进行学习。
- **DE** — Training auf unbeschrifteten Daten, bei dem das Modell sein Überwachungssignal aus den Daten selbst erzeugt.
- _Seen in / 出现于:_ [`histo-nejmai-2024`](papers/histo-nejmai-2024/index.md), [`uni2-h-model`](papers/uni2-h-model/index.md), [`virchow-2024`](papers/virchow-2024/index.md)

### Tile embedding · 图块嵌入 · Tile-Embedding

- **EN** — A fixed-length feature vector produced by an encoder to numerically represent an image tile for downstream tasks.
- **中文** — 由编码器生成的定长特征向量,用于数值化表示图块,供下游任务使用。
- **DE** — Ein Merkmalsvektor fester Länge, den ein Encoder erzeugt, um eine Bildkachel numerisch für nachgelagerte Aufgaben darzustellen.
- _Seen in / 出现于:_ [`uni2-h-model`](papers/uni2-h-model/index.md), [`virchow-2024`](papers/virchow-2024/index.md)

### Vision Transformer (ViT) · 视觉 Transformer · Vision Transformer

- **EN** — A neural network that treats image patches as a sequence of tokens and processes them with the transformer self-attention architecture.
- **中文** — 一种把图像块当作 token 序列、用 Transformer 自注意力架构处理的神经网络。
- **DE** — Ein neuronales Netz, das Bildausschnitte als Token-Sequenz behandelt und sie mit der Self-Attention-Architektur des Transformers verarbeitet.
- _Seen in / 出现于:_ [`fm-arxiv-2604`](papers/fm-arxiv-2604/index.md), [`uni2-h-model`](papers/uni2-h-model/index.md), [`virchow-2024`](papers/virchow-2024/index.md)

### Vision-language model (VLM) · 视觉-语言模型 · Vision-Language-Modell

- **EN** — A model trained on paired images and text so it can relate visual content to natural-language descriptions.
- **中文** — 在图像-文本配对上训练的模型,能够将视觉内容与自然语言描述关联起来。
- **DE** — Ein auf gepaarten Bildern und Texten trainiertes Modell, das visuelle Inhalte mit natürlichsprachlichen Beschreibungen verknüpfen kann.
- _Seen in / 出现于:_ [`fm-arxiv-2604`](papers/fm-arxiv-2604/index.md), [`histo-miccai-2025`](papers/histo-miccai-2025/index.md)

## ML methods / 机器学习方法

### 3D vision transformer (CT-ViT) · 三维视觉 Transformer(CT-ViT) · 3D-Vision-Transformer (CT-ViT)

- **EN** — A transformer neural network that processes volumetric images as sequences of 3D patches; CT-ViT is a chest-CT variant used as an imaging backbone.
- **中文** — 以三维图块序列处理体数据图像的 Transformer 神经网络;CT-ViT 是用作影像骨干的胸部 CT 变体。
- **DE** — Ein Transformer-Netzwerk, das volumetrische Bilder als Folgen von 3D-Patches verarbeitet; CT-ViT ist eine Thorax-CT-Variante, die als Bild-Backbone dient.
- _Seen in / 出现于:_ [`imaging-ehjdh-2026`](papers/imaging-ehjdh-2026/index.md)

### Anomaly detection · 异常检测 · Anomalieerkennung

- **EN** — Identifying samples or regions that deviate from a learned notion of 'normal', often by training only on normal data — the first stage of the detect→model→revert pipeline.
- **中文** — 识别偏离所学“正常”概念的样本或区域,常仅用正常数据训练——即“检测→建模→逆转”流程的第一环。
- **DE** — Das Erkennen von Proben oder Regionen, die von einem gelernten Begriff des 'Normalen' abweichen, oft durch Training nur auf normalen Daten — die erste Stufe der Detect→Model→Revert-Pipeline.
- _Seen in / 出现于:_ [`histo-anomaly-bi-repo`](papers/histo-anomaly-bi-repo/index.md), [`histo-miccai-2025`](papers/histo-miccai-2025/index.md), [`histo-nejmai-2024`](papers/histo-nejmai-2024/index.md), [`imaging-ehjdh-2026`](papers/imaging-ehjdh-2026/index.md), [`imaging-nature-2026`](papers/imaging-nature-2026/index.md), [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md), [`spatial-natcommun-2024`](papers/spatial-natcommun-2024/index.md)

### Autoencoder · 自编码器 · Autoencoder

- **EN** — A neural network that compresses data into a latent code and reconstructs it, used for dimensionality reduction and reconstruction-based anomaly scoring.
- **中文** — 把数据压缩为潜编码再重建的神经网络,用于降维和基于重建的异常打分。
- **DE** — Ein neuronales Netz, das Daten in einen latenten Code komprimiert und rekonstruiert, genutzt zur Dimensionsreduktion und zur rekonstruktionsbasierten Anomaliebewertung.
- _Seen in / 出现于:_ [`histo-miccai-2025`](papers/histo-miccai-2025/index.md), [`scrna-natmachintell-2026`](papers/scrna-natmachintell-2026/index.md)

### Counterfactual · 反事实 · Kontrafaktisch

- **EN** — A synthesized 'what-if' version of an input — e.g. how a waveform or tissue would look if it were normal — used to make a model's decision interpretable.
- **中文** — 对输入合成的“如果……会怎样”版本——如某波形或组织若为正常时的样子——用于让模型决策可解释。
- **DE** — Eine synthetisierte 'Was-wäre-wenn'-Version einer Eingabe — z. B. wie eine Wellenform oder ein Gewebe aussähe, wenn es normal wäre — um die Modellentscheidung interpretierbar zu machen.
- _Seen in / 出现于:_ [`imaging-nature-2026`](papers/imaging-nature-2026/index.md)

### Diffusion model · 扩散模型 · Diffusionsmodell

- **EN** — A generative model that learns to reverse a gradual noising process to synthesize data; conditioning it on 'normal' priors enables reconstruction-based anomaly detection.
- **中文** — 通过学习逆转逐步加噪过程来合成数据的生成模型;以“正常”先验为条件即可做基于重建的异常检测。
- **DE** — Ein generatives Modell, das lernt, einen schrittweisen Verrauschungsprozess umzukehren, um Daten zu synthetisieren; bedingt auf 'normale' Priors ermöglicht es rekonstruktionsbasierte Anomalieerkennung.
- _Seen in / 出现于:_ [`histo-miccai-2025`](papers/histo-miccai-2025/index.md), [`imaging-nature-2026`](papers/imaging-nature-2026/index.md)

### Discriminative model · 判别模型 · Diskriminatives Modell

- **EN** — A model that predicts a label from an input (e.g. risk from an ECG); pairing it with a generative model turns its opaque decision into a visible biomarker.
- **中文** — 从输入预测标签的模型(如从 ECG 预测风险);与生成模型配对可把其不透明决策转为可见的生物标志物。
- **DE** — Ein Modell, das aus einer Eingabe ein Label vorhersagt (z. B. Risiko aus einem EKG); die Kopplung mit einem generativen Modell macht seine undurchsichtige Entscheidung als Biomarker sichtbar.
- _Seen in / 出现于:_ [`imaging-nature-2026`](papers/imaging-nature-2026/index.md)

### Flow matching · 流匹配 · Flow Matching

- **EN** — A technique for training continuous-time generative models by regressing a velocity field that transports one distribution into another.
- **中文** — 通过回归将一个分布输运到另一个分布的速度场,来训练连续时间生成模型的方法。
- **DE** — Eine Technik zum Training zeitkontinuierlicher generativer Modelle, indem ein Geschwindigkeitsfeld regressiert wird, das eine Verteilung in eine andere überführt.
- _Seen in / 出现于:_ [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md), [`virtual-cell-challenge`](papers/virtual-cell-challenge/index.md)

### Foundation model · 基础模型 · Foundation Model

- **EN** — A large model pretrained on broad data and reused as a general-purpose backbone that is adapted to many downstream tasks.
- **中文** — 在大规模广泛数据上预训练、作为通用骨干复用并适配到众多下游任务的大模型。
- **DE** — Ein großes, auf breiten Daten vortrainiertes Modell, das als universelles Backbone wiederverwendet und an viele nachgelagerte Aufgaben angepasst wird.
- _Seen in / 出现于:_ [`fm-arxiv-2604`](papers/fm-arxiv-2604/index.md), [`hest1k-2024`](papers/hest1k-2024/index.md), [`histo-nejmai-2024`](papers/histo-nejmai-2024/index.md), [`imaging-ehjdh-2026`](papers/imaging-ehjdh-2026/index.md), [`scrna-natmachintell-2026`](papers/scrna-natmachintell-2026/index.md), [`uni2-h-model`](papers/uni2-h-model/index.md), [`virchow-2024`](papers/virchow-2024/index.md), [`virtual-cell-challenge`](papers/virtual-cell-challenge/index.md), [`virtual-tissue-2501`](papers/virtual-tissue-2501/index.md)

### Generative adversarial network (GAN) · 生成对抗网络(GAN) · Generative Adversarial Network (GAN)

- **EN** — A generative model where a generator and a discriminator are trained against each other; the discriminator's signal can also enforce constraints on learned representations.
- **中文** — 一种生成模型,生成器与判别器相互对抗训练;判别器信号也可用于对所学表征施加约束。
- **DE** — Ein generatives Modell, bei dem Generator und Diskriminator gegeneinander trainiert werden; das Diskriminator-Signal kann auch Beschränkungen für gelernte Repräsentationen erzwingen.
- _Seen in / 出现于:_ [`imaging-nature-2026`](papers/imaging-nature-2026/index.md), [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md)

### Generative model · 生成模型 · Generatives Modell

- **EN** — A model that learns a data distribution well enough to synthesize new samples, enabling visualization, reconstruction, or in-silico perturbation.
- **中文** — 充分学习数据分布以合成新样本的模型,可用于可视化、重建或计算机模拟扰动。
- **DE** — Ein Modell, das eine Datenverteilung gut genug lernt, um neue Proben zu synthetisieren, und so Visualisierung, Rekonstruktion oder In-silico-Perturbation ermöglicht.
- _Seen in / 出现于:_ [`histo-miccai-2025`](papers/histo-miccai-2025/index.md), [`imaging-nature-2026`](papers/imaging-nature-2026/index.md), [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md)

### In-silico perturbation · 计算机模拟扰动 · In-silico-Perturbation

- **EN** — Simulating an intervention — deleting/replacing a cell type or applying a drug — inside a model to predict the resulting change and screen for revert targets.
- **中文** — 在模型内部模拟干预(删除/替换某类细胞或施加药物),以预测由此产生的变化并筛选逆转靶点。
- **DE** — Das Simulieren eines Eingriffs — Löschen/Ersetzen eines Zelltyps oder Anwenden eines Medikaments — innerhalb eines Modells, um die resultierende Veränderung vorherzusagen und Revert-Ziele zu screenen.
- _Seen in / 出现于:_ [`scrna-natmachintell-2026`](papers/scrna-natmachintell-2026/index.md), [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md), [`virtual-cell-challenge`](papers/virtual-cell-challenge/index.md)

### Maximum mean discrepancy (MMD) · 最大均值差异(MMD) · Maximum Mean Discrepancy (MMD)

- **EN** — A kernel-based statistic measuring how different two distributions are by comparing their means in a feature space; a metric for perturbation-prediction accuracy.
- **中文** — 基于核的统计量,通过在特征空间比较均值来度量两个分布的差异;用作扰动预测准确度的指标。
- **DE** — Eine kernbasierte Statistik, die den Unterschied zweier Verteilungen durch Vergleich ihrer Mittelwerte in einem Merkmalsraum misst; ein Maß für die Genauigkeit der Perturbationsvorhersage.
- _Seen in / 出现于:_ [`scrna-natmachintell-2026`](papers/scrna-natmachintell-2026/index.md)

### Monge gap · Monge 间隙 · Monge-Gap

- **EN** — A regularizer that pushes a learned map toward the optimal-transport (Monge) solution without needing a special convex architecture; conditioning it yields the Conditional Monge Gap.
- **中文** — 一种正则项,将所学映射推向最优传输(Monge)解而无需特殊凸结构;对其条件化即得 Conditional Monge Gap。
- **DE** — Ein Regularisierer, der eine gelernte Abbildung ohne spezielle konvexe Architektur zur optimalen (Monge-)Transportlösung hin drängt; seine Bedingung ergibt den Conditional Monge Gap.
- _Seen in / 出现于:_ [`scrna-natmachintell-2026`](papers/scrna-natmachintell-2026/index.md)

### Neural ODE · 神经常微分方程 · Neuronale ODE

- **EN** — A model that parameterizes the derivative of a hidden state with a neural network, integrating it as an ordinary differential equation to transform data continuously.
- **中文** — 用神经网络参数化隐状态导数,将其作为常微分方程积分以连续地变换数据的模型。
- **DE** — Ein Modell, das die Ableitung eines verborgenen Zustands durch ein neuronales Netz parametrisiert und sie als gewöhnliche Differentialgleichung integriert, um Daten kontinuierlich zu transformieren.
- _Seen in / 出现于:_ [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md)

### Optimal transport (OT) · 最优传输(OT) · Optimaler Transport (OT)

- **EN** — A mathematical framework for the least-cost way to morph one probability distribution into another, used to map control cells to perturbed cells.
- **中文** — 以最小代价把一个概率分布变形为另一个的数学框架,用于将对照细胞映射到扰动后细胞。
- **DE** — Ein mathematischer Rahmen für die kostengünstigste Art, eine Wahrscheinlichkeitsverteilung in eine andere zu überführen, genutzt, um Kontrollzellen auf perturbierte Zellen abzubilden.
- _Seen in / 出现于:_ [`scrna-natmachintell-2026`](papers/scrna-natmachintell-2026/index.md), [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md), [`virtual-tissue-2501`](papers/virtual-tissue-2501/index.md)

### Out-of-distribution (OOD) detection · 分布外(OOD)检测 · Out-of-Distribution-Erkennung (OOD)

- **EN** — Flagging inputs that fall outside the data distribution a model was trained on, such as an unseen drug, cell context, or diseased tissue.
- **中文** — 标记落在模型训练分布之外的输入,如未见过的药物、细胞语境或病变组织。
- **DE** — Das Kennzeichnen von Eingaben, die außerhalb der Trainingsverteilung eines Modells liegen, etwa ein unbekanntes Medikament, ein neuer Zellkontext oder krankhaftes Gewebe.
- _Seen in / 出现于:_ [`histo-miccai-2025`](papers/histo-miccai-2025/index.md), [`scrna-natmachintell-2026`](papers/scrna-natmachintell-2026/index.md), [`virtual-cell-challenge`](papers/virtual-cell-challenge/index.md)

### Reconstruction error · 重建误差 · Rekonstruktionsfehler

- **EN** — The discrepancy between an input and a generative model's attempt to reconstruct it as 'normal'; large error marks the input as anomalous.
- **中文** — 输入与生成模型将其重建为“正常”之间的差异;误差大则将该输入判为异常。
- **DE** — Die Abweichung zwischen einer Eingabe und dem Versuch eines generativen Modells, sie als 'normal' zu rekonstruieren; ein großer Fehler kennzeichnet die Eingabe als anomal.
- _Seen in / 出现于:_ [`histo-miccai-2025`](papers/histo-miccai-2025/index.md)

### Sinkhorn divergence · Sinkhorn 散度 · Sinkhorn-Divergenz

- **EN** — An entropy-regularized, fast-to-compute approximation of optimal-transport distance between two distributions, used as a training and evaluation objective.
- **中文** — 对两个分布之间最优传输距离的熵正则化、计算高效的近似,用作训练与评测目标。
- **DE** — Eine entropieregularisierte, schnell berechenbare Näherung der optimalen Transportdistanz zwischen zwei Verteilungen, verwendet als Trainings- und Bewertungsziel.
- _Seen in / 出现于:_ [`scrna-natmachintell-2026`](papers/scrna-natmachintell-2026/index.md)

### Variational autoencoder (VAE / iVAE) · 变分自编码器(VAE / iVAE) · Variationaler Autoencoder (VAE / iVAE)

- **EN** — An autoencoder with a probabilistic latent space; the identifiable variant (iVAE) conditions on side information so latent factors can be uniquely recovered.
- **中文** — 具有概率潜空间的自编码器;可识别变体(iVAE)以辅助信息为条件,使潜在因子可被唯一还原。
- **DE** — Ein Autoencoder mit probabilistischem latentem Raum; die identifizierbare Variante (iVAE) bedingt auf Zusatzinformation, sodass latente Faktoren eindeutig rekonstruierbar sind.
- _Seen in / 出现于:_ [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md)

### Wasserstein distance · Wasserstein 距离 · Wasserstein-Distanz

- **EN** — The optimal-transport 'earth-mover' distance between distributions, usable as a similarity metric between perturbation effects or as a revert-distance measure.
- **中文** — 分布之间的最优传输“搬土”距离,可作为扰动效应间的相似度或“逆转距离”度量。
- **DE** — Die 'Earth-Mover'-Distanz des optimalen Transports zwischen Verteilungen, nutzbar als Ähnlichkeitsmaß zwischen Perturbationseffekten oder als Revert-Distanzmaß.
- _Seen in / 出现于:_ [`scrna-natmachintell-2026`](papers/scrna-natmachintell-2026/index.md), [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md)

## General / 通用

### AUROC / AUC (area under the ROC curve) · AUROC / AUC(ROC 曲线下面积) · AUROC / AUC (Fläche unter der ROC-Kurve)

- **EN** — A threshold-independent measure of a classifier's ability to rank positives above negatives; 0.5 is chance and 1.0 is perfect discrimination.
- **中文** — 衡量分类器把正例排在负例之前能力的阈值无关指标;0.5 为随机,1.0 为完美区分。
- **DE** — Ein schwellenunabhängiges Maß für die Fähigkeit eines Klassifikators, Positive über Negative zu ordnen; 0,5 ist Zufall, 1,0 perfekte Trennschärfe.
- _Seen in / 出现于:_ [`histo-miccai-2025`](papers/histo-miccai-2025/index.md), [`imaging-ehjdh-2026`](papers/imaging-ehjdh-2026/index.md)

### Batch effect · 批次效应 · Batch-Effekt

- **EN** — Systematic non-biological variation between datasets acquired at different sites, times, or platforms that can confound analysis if not corrected.
- **中文** — 不同机构、时间或平台采集的数据集之间的系统性非生物学差异,若不校正会混淆分析。
- **DE** — Systematische, nicht-biologische Variation zwischen Datensätzen, die an verschiedenen Orten, Zeiten oder Plattformen erhoben wurden und die Analyse verfälschen kann, wenn sie nicht korrigiert wird.
- _Seen in / 出现于:_ [`scrna-natmachintell-2026`](papers/scrna-natmachintell-2026/index.md), [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md)

### Concordance index (C-index) · 一致性指数(C-index) · Konkordanzindex (C-Index)

- **EN** — A survival-analysis metric giving the probability that the model ranks a higher-risk patient as having an earlier event than a lower-risk one; 0.5 is chance.
- **中文** — 生存分析指标,表示模型把高风险患者判为比低风险患者更早发生事件的概率;0.5 为随机。
- **DE** — Eine Metrik der Überlebensanalyse, die die Wahrscheinlichkeit angibt, dass das Modell einen Hochrisikopatienten als früher erkrankt einstuft als einen Niedrigrisikopatienten; 0,5 ist Zufall.
- _Seen in / 出现于:_ [`spatial-biorxiv-2025`](papers/spatial-biorxiv-2025/index.md)

### Contrastive learning · 对比学习 · Kontrastives Lernen

- **EN** — A representation-learning approach that pulls together embeddings of related samples and pushes apart unrelated ones.
- **中文** — 一种表征学习方法,把相关样本的嵌入拉近、把无关样本的嵌入推远。
- **DE** — Ein Ansatz des Repräsentationslernens, der Einbettungen verwandter Proben zusammenzieht und die unverwandter Proben auseinanderdrückt.
- _Seen in / 出现于:_ [`hest1k-2024`](papers/hest1k-2024/index.md)

### Domain shift · 域偏移 · Domänenverschiebung

- **EN** — A drop in model performance when test data differs from training data, for example due to a different scanner or staining protocol.
- **中文** — 当测试数据与训练数据不同(例如换了扫描仪或染色方案)时导致的模型性能下降。
- **DE** — Ein Leistungsabfall des Modells, wenn Testdaten von den Trainingsdaten abweichen, etwa durch einen anderen Scanner oder ein anderes Färbeprotokoll.
- _Seen in / 出现于:_ [`histo-miccai-2025`](papers/histo-miccai-2025/index.md), [`uni2-h-model`](papers/uni2-h-model/index.md), [`virchow-2024`](papers/virchow-2024/index.md)

### External validation · 外部验证 · Externe Validierung

- **EN** — Testing a trained model on data from an independent site, country, or cohort it never saw, to demonstrate that performance generalizes.
- **中文** — 在模型从未见过的独立机构、国家或队列数据上测试,以证明性能可泛化。
- **DE** — Das Testen eines trainierten Modells an Daten eines unabhängigen Standorts, Landes oder einer Kohorte, die es nie gesehen hat, um die Generalisierbarkeit der Leistung zu belegen.
- _Seen in / 出现于:_ [`imaging-ehjdh-2026`](papers/imaging-ehjdh-2026/index.md), [`imaging-nature-2026`](papers/imaging-nature-2026/index.md)

### F1 score · F1 分数 · F1-Score

- **EN** — The harmonic mean of precision and recall, a single balanced accuracy metric for classification under class imbalance.
- **中文** — 精确率与召回率的调和平均,是类别不平衡下分类的单一平衡准确度指标。
- **DE** — Das harmonische Mittel aus Präzision und Recall, eine ausgewogene Einzelkennzahl für die Klassifikationsgüte bei Klassenungleichgewicht.
- _Seen in / 出现于:_ [`imaging-ehjdh-2026`](papers/imaging-ehjdh-2026/index.md)

### Latent diffusion model (LDM) · 潜空间扩散模型 · Latentes Diffusionsmodell

- **EN** — A generative model that iteratively denoises data in a compressed latent space to synthesize realistic images efficiently.
- **中文** — 一种生成模型,在压缩的潜空间中迭代去噪,从而高效合成逼真图像。
- **DE** — Ein generatives Modell, das Daten iterativ in einem komprimierten latenten Raum entrauscht, um realistische Bilder effizient zu synthetisieren.
- _Seen in / 出现于:_ [`fm-arxiv-2604`](papers/fm-arxiv-2604/index.md), [`histo-miccai-2025`](papers/histo-miccai-2025/index.md)

### LoRA (Low-Rank Adaptation) · 低秩适配 · LoRA (Low-Rank Adaptation)

- **EN** — A parameter-efficient fine-tuning method that adapts a large pretrained model by training only small low-rank weight updates.
- **中文** — 一种参数高效的微调方法,只训练小的低秩权重增量来适配大型预训练模型。
- **DE** — Eine parameter-effiziente Feinabstimmungsmethode, die ein großes vortrainiertes Modell anpasst, indem nur kleine niedrigrangige Gewichtsaktualisierungen trainiert werden.
- _Seen in / 出现于:_ [`histo-miccai-2025`](papers/histo-miccai-2025/index.md)

### Masked autoencoder (MAE) · 掩码自编码器(MAE) · Maskierter Autoencoder (MAE)

- **EN** — A self-supervised model trained to reconstruct deliberately hidden parts of its input, yielding representations useful for downstream tasks.
- **中文** — 一种自监督模型,通过重建被刻意遮蔽的输入部分进行训练,从而得到对下游任务有用的表征。
- **DE** — Ein selbstüberwachtes Modell, das darauf trainiert wird, absichtlich verdeckte Teile seiner Eingabe zu rekonstruieren, und so für nachgelagerte Aufgaben nützliche Repräsentationen liefert.
- _Seen in / 出现于:_ [`virtual-tissue-2501`](papers/virtual-tissue-2501/index.md)

### Multiple-instance learning (MIL) · 多示例学习(MIL) · Multiple-Instance-Learning (MIL)

- **EN** — A weakly-supervised paradigm where a single label is attached to a whole bag of instances, letting a slide-level label train on many image patches.
- **中文** — 一种弱监督范式,将单一标签赋予整个示例袋,使切片级标签能在众多图像块上进行训练。
- **DE** — Ein schwach überwachtes Paradigma, bei dem ein einzelnes Label einem ganzen Bündel von Instanzen zugeordnet wird, sodass ein Schnitt-Label über viele Bildausschnitte trainiert.
- _Seen in / 出现于:_ [`histo-sciencedirect-2026`](papers/histo-sciencedirect-2026/index.md), [`pathomics-npjpo-2026`](papers/pathomics-npjpo-2026/index.md), [`uni2-h-model`](papers/uni2-h-model/index.md)

### One-class classification · 单类分类 · Einklassen-Klassifikation

- **EN** — Learning a boundary from examples of a single normal class so that anything falling outside it is flagged as anomalous.
- **中文** — 仅从单一正常类别的样本学习一个边界,凡落在边界之外者即判为异常。
- **DE** — Das Lernen einer Grenze aus Beispielen einer einzigen Normalklasse, sodass alles außerhalb als anomal markiert wird.
- _Seen in / 出现于:_ [`histo-anomaly-bi-repo`](papers/histo-anomaly-bi-repo/index.md), [`histo-nejmai-2024`](papers/histo-nejmai-2024/index.md)

### Outlier exposure · 离群暴露 · Outlier Exposure

- **EN** — Improving anomaly detection by training the model on auxiliary out-of-distribution data that stands in for unseen anomalies.
- **中文** — 通过用辅助的分布外数据(充当未见异常的代理)训练模型,来提升异常检测能力。
- **DE** — Die Verbesserung der Anomalieerkennung, indem das Modell mit zusätzlichen Out-of-Distribution-Daten trainiert wird, die ungesehene Anomalien vertreten.
- _Seen in / 出现于:_ [`histo-nejmai-2024`](papers/histo-nejmai-2024/index.md)

### Saliency attribution (Grad-CAM) · 显著性归因(Grad-CAM) · Saliency-Attribution (Grad-CAM)

- **EN** — Post-hoc explanation methods, such as Grad-CAM, that highlight the image regions most responsible for a model's prediction.
- **中文** — 如 Grad-CAM 等事后解释方法,用于突出对模型预测贡献最大的图像区域。
- **DE** — Post-hoc-Erklärungsmethoden wie Grad-CAM, die die für eine Modellvorhersage maßgeblichen Bildregionen hervorheben.
- _Seen in / 出现于:_ [`histo-sciencedirect-2026`](papers/histo-sciencedirect-2026/index.md)


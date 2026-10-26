# Glossary

> 150 terms, each with a **English / 中文 / Deutsch** name and a one-sentence definition. The first groups follow the onboarding modules (read the group for the module you are on); the rest are terms you meet in the papers, grouped by domain. Source files: `glossary/*.yaml`.

## 1 · Two tables: X and obs

### Count matrix · 计数矩阵 {#count-matrix}

- **EN** — The main single-cell data table: one row per cell (or nucleus), one column per gene, each entry the number of RNA molecules (UMIs) of that gene detected in that cell; very sparse.
- **中文** — 单细胞数据的主表：每行一个细胞（或细胞核），每列一个基因，数值是该细胞里测到的该基因 RNA 分子数（UMI 数）；非常稀疏。
- **DE** — Zählmatrix: Die zentrale Einzelzell-Tabelle: eine Zeile pro Zelle (oder Zellkern), eine Spalte pro Gen, jeder Eintrag die Zahl der in dieser Zelle gemessenen RNA-Moleküle (UMIs) des Gens; sehr dünn besetzt.
- _Explained in:_ [1 · Two tables: X and obs](01-two-tables.md)
- _Seen in:_ [`lake-kidney-atlas-nature-2023`](../papers/lake-kidney-atlas-nature-2023/index.md)

### AnnData / h5ad · AnnData / h5ad 文件 {#anndata-h5ad}

- **EN** — The Python (scanpy) container for single-cell data, saved as an .h5ad (HDF5) file: the count matrix X plus per-cell metadata (obs) and per-gene metadata (var).
- **中文** — Python（scanpy）里存单细胞数据的容器，存成 .h5ad（HDF5）文件：计数矩阵 X，加每个细胞的标签表 obs 和每个基因的信息 var。
- **DE** — AnnData / h5ad: Der Python-(scanpy-)Container für Einzelzelldaten, gespeichert als .h5ad-(HDF5-)Datei: Zählmatrix X plus Metadaten pro Zelle (obs) und pro Gen (var).
- _Explained in:_ [1 · Two tables: X and obs](01-two-tables.md)

### obs / var (cell and gene metadata) · obs / var（细胞和基因的信息表） {#obs-var}

- **EN** — The two tables aligned with the count matrix: obs has one row per cell (patient, library, quality numbers, cell-type and state labels), var has one row per gene (gene name and other gene information).
- **中文** — 和计数矩阵对齐的两张表：obs 每个细胞一行（病人、批次、质量指标、细胞类型和状态标签），var 每个基因一行（基因名等信息）。
- **DE** — obs / var (Zell- und Gen-Metadaten): Die zwei an der Zählmatrix ausgerichteten Tabellen: obs hat eine Zeile pro Zelle (Patient, Library, Qualitätswerte, Zelltyp- und Zustandslabels), var eine Zeile pro Gen (Genname und weitere Geninformationen).
- _Explained in:_ [1 · Two tables: X and obs](01-two-tables.md)

### Gene symbol (HGNC) · 基因符号（HGNC） {#gene-symbol}

- **EN** — The short official name of a human gene set by the HGNC, such as LRP2 or UMOD; used as the column names of the count matrix. A prefix MT- marks genes encoded by mitochondrial DNA.
- **中文** — 由 HGNC 定的人类基因官方简称，比如 LRP2、UMOD；计数矩阵的列名就是它。MT- 开头的是线粒体 DNA 编码的基因。
- **DE** — Gensymbol (HGNC): Der kurze offizielle Name eines menschlichen Gens, festgelegt von der HGNC, z. B. LRP2 oder UMOD; dient als Spaltenname der Zählmatrix. Das Präfix MT- kennzeichnet von mitochondrialer DNA kodierte Gene.
- _Explained in:_ [1 · Two tables: X and obs](01-two-tables.md)

### Patient-level split (data leakage) · 按病人切分（数据泄漏） {#patient-level-split}

- **EN** — Putting all cells of one patient (and, where needed, one library) on the same side of the train / test split; splitting cells at random leaks the patient and batch into the test set and inflates the score.
- **中文** — 把同一个病人（必要时同一次上机）的所有细胞放在训练集或测试集的同一边；按细胞随机切分会把病人和批次信息泄漏到测试集，分数虚高。
- **DE** — Aufteilung nach Patient (Datenleck): Alle Zellen eines Patienten (und bei Bedarf einer Library) landen auf derselben Seite der Train-/Test-Aufteilung; eine zufällige Aufteilung nach Zellen lässt Patient und Batch ins Testset durchsickern und schönt das Ergebnis.
- _Explained in:_ [1 · Two tables: X and obs](01-two-tables.md)

## 2 · Cells and RNA

### Nucleus (cell nucleus) · 细胞核 {#cell-nucleus}

- **EN** — The compartment inside a cell that holds the DNA; RNA is made here before it moves out to the cytoplasm.
- **中文** — 细胞里装 DNA 的部分；RNA 在这里被转录出来，之后再运到胞质。
- **DE** — Zellkern: Das Kompartiment der Zelle, das die DNA enthält; RNA wird hier gebildet und dann ins Zytoplasma transportiert.
- _Explained in:_ [2 · Cells and RNA](02-cells-rna.md)

### Transcription (gene expression) · 转录（基因表达） {#transcription}

- **EN** — Copying a gene's DNA into RNA; counting a gene's RNA molecules in a cell measures how active (expressed) the gene is.
- **中文** — 把一个基因的 DNA 抄写成 RNA；数一个细胞里某个基因有几条 RNA，就是在量这个基因的活跃程度（表达量）。
- **DE** — Transkription (Genexpression): Das Abschreiben der DNA eines Gens in RNA; die Zahl der RNA-Moleküle eines Gens in einer Zelle misst, wie aktiv (exprimiert) es ist.
- _Explained in:_ [2 · Cells and RNA](02-cells-rna.md)

### Gene-expression signature · 基因表达签名 {#gene-expression-signature}

- **EN** — A defined set of genes whose coordinated expression levels mark a particular cell state, disease, or treatment response.
- **中文** — 一组特定基因,其协同表达水平可标志某种细胞状态、疾病或治疗响应。
- **DE** — Genexpressionssignatur: Eine definierte Gruppe von Genen, deren koordinierte Expressionsniveaus einen bestimmten Zellzustand, eine Krankheit oder eine Therapieantwort kennzeichnen.
- _Explained in:_ [2 · Cells and RNA](02-cells-rna.md)
- _Seen in:_ [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md), [`virtual-tissue-2501`](../papers/virtual-tissue-2501/index.md)

### Cell type · 细胞类型 {#cell-type}

- **EN** — A stable class of cells with the same job and a characteristic expression profile (e.g. proximal tubule cell); found by clustering cells and checking marker genes.
- **中文** — 工作相同、表达谱特征一致的一类细胞（例如近端小管细胞）；通过聚类加看标记基因来确定。
- **DE** — Zelltyp: Eine stabile Klasse von Zellen mit gleicher Aufgabe und typischem Expressionsprofil (z. B. proximale Tubuluszelle); bestimmt durch Clustering und Markergene.
- _Explained in:_ [2 · Cells and RNA](02-cells-rna.md)
- _Seen in:_ [`lake-kidney-atlas-nature-2023`](../papers/lake-kidney-atlas-nature-2023/index.md)

### Cell state · 细胞状态 {#cell-state}

- **EN** — The transient functional condition of a cell — such as activated, exhausted, or proliferating — layered on top of its stable cell-type identity.
- **中文** — 细胞在其稳定的细胞类型身份之上所处的、可变的功能状态,如激活、耗竭或增殖。
- **DE** — Zellzustand: Der vorübergehende funktionelle Zustand einer Zelle — etwa aktiviert, erschöpft oder proliferierend — der ihrer stabilen Zelltyp-Identität überlagert ist.
- _Explained in:_ [2 · Cells and RNA](02-cells-rna.md)
- _Seen in:_ [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md), [`virtual-cell-challenge`](../papers/virtual-cell-challenge/index.md)

## 3 · The kidney

### Nephron · 肾单位 {#nephron}

- **EN** — The functional unit of the kidney, about a million per kidney: a filter (glomerulus) followed by a tubule that reclaims useful substances and leaves urine.
- **中文** — 肾脏的功能单位，一个肾约 100 万个：先是一个过滤器（肾小球），后面接一条小管，把有用的东西收回，剩下的成为尿。
- **DE** — Nephron: Die funktionelle Einheit der Niere, etwa eine Million pro Niere: ein Filter (Glomerulus) und ein anschließender Tubulus, der Nützliches zurückgewinnt und Harn übrig lässt.
- _Explained in:_ [3 · The kidney](03-kidney.md)

### Renal cortex / medulla / papilla · 皮质 / 髓质 / 乳头 {#renal-cortex-medulla}

- **EN** — The kidney's outer layer (cortex, with glomeruli and proximal and distal tubules), inner layer (medulla, with the loops and collecting ducts) and the tips of the medulla (papillae) where urine leaves.
- **中文** — 肾的外层（皮质，有肾小球、近端和远端小管）、内层（髓质，有髓袢和集合管），以及髓质的尖端（乳头，尿从这里流出）。
- **DE** — Nierenrinde / Nierenmark / Papille: Äußere Schicht der Niere (Rinde, mit Glomeruli, proximalen und distalen Tubuli), innere Schicht (Mark, mit Henle-Schleifen und Sammelrohren) und die Markspitzen (Papillen), wo der Harn austritt.
- _Explained in:_ [3 · The kidney](03-kidney.md)
- _Seen in:_ [`kidney-multimodal-genomebiol-2026`](../papers/kidney-multimodal-genomebiol-2026/index.md), [`lake-kidney-atlas-nature-2023`](../papers/lake-kidney-atlas-nature-2023/index.md)

### Glomerulus · 肾小球 {#glomerulus}

- **EN** — The ball of capillaries at the start of each nephron, inside Bowman's capsule, where blood is filtered.
- **中文** — 每个肾单位起点的一团毛细血管，包在肾小球囊（Bowman's capsule）里，血液在这里被过滤。
- **DE** — Glomerulus: Das Kapillarknäuel am Anfang jedes Nephrons in der Bowman-Kapsel, in dem das Blut gefiltert wird.
- _Explained in:_ [3 · The kidney](03-kidney.md)

### Podocyte (POD) · 足细胞 {#podocyte}

- **EN** — Cells wrapped around the glomerular capillaries that form the final filtration barrier; when they are injured, protein leaks into the urine.
- **中文** — 包在肾小球毛细血管外面的细胞，构成过滤的最后一道屏障；受损时蛋白会漏进尿里。
- **DE** — Podozyt: Zellen, die die glomerulären Kapillaren umhüllen und die letzte Filtrationsbarriere bilden; bei Schädigung tritt Eiweiß in den Harn über.
- _Explained in:_ [3 · The kidney](03-kidney.md)
- _Seen in:_ [`damage-scores-cellgenomics-2026`](../papers/damage-scores-cellgenomics-2026/index.md), [`lake-kidney-atlas-nature-2023`](../papers/lake-kidney-atlas-nature-2023/index.md)

### Proximal tubule (PT) · 近端小管 {#proximal-tubule}

- **EN** — The first tubule segment after the glomerulus; reclaims most water, glucose and salt, uses the most energy, and is the first to be injured by ischaemia. The most abundant cell type in kidney atlases.
- **中文** — 肾小球后面的第一段小管；回收大部分水、葡萄糖和盐，最耗能，缺血时最先受伤。是肾脏图谱里数量最多的细胞类型。
- **DE** — Proximaler Tubulus: Das erste Tubulussegment nach dem Glomerulus; resorbiert den Großteil von Wasser, Glukose und Salz, verbraucht am meisten Energie und wird bei Ischämie zuerst geschädigt.
- _Explained in:_ [3 · The kidney](03-kidney.md)
- _Seen in:_ [`lake-kidney-atlas-nature-2023`](../papers/lake-kidney-atlas-nature-2023/index.md)

### Loop of Henle (DTL / ATL) · 髓袢（降支细段 / 升支细段） {#loop-of-henle}

- **EN** — The U-shaped tubule segment that dips into the medulla: descending thin limb (DTL), ascending thin limb (ATL), then the thick ascending limb.
- **中文** — 伸进髓质的 U 形小管段：降支细段（DTL）、升支细段（ATL），再接升支粗段。
- **DE** — Henle-Schleife: Das U-förmige Tubulussegment, das ins Mark reicht: absteigender dünner Teil (DTL), aufsteigender dünner Teil (ATL), dann der dicke aufsteigende Teil.
- _Explained in:_ [3 · The kidney](03-kidney.md)

### Thick ascending limb (TAL) · 髓袢升支粗段 {#thick-ascending-limb}

- **EN** — The thick part of the loop of Henle that reclaims salt and builds the concentration gradient; like the proximal tubule it is often injured, and its adaptive state (aTAL) was defined in Lake 2023.
- **中文** — 髓袢变粗的那一段，回收盐、建立浓度梯度；和近端小管一样容易受伤，它的修复态 aTAL 是 Lake 2023 定义的。
- **DE** — Dicker aufsteigender Teil der Henle-Schleife: Der dicke Teil der Henle-Schleife, der Salz resorbiert und den Konzentrationsgradienten aufbaut; wie der proximale Tubulus oft geschädigt (adaptiver Zustand aTAL, Lake 2023).
- _Explained in:_ [3 · The kidney](03-kidney.md)
- _Seen in:_ [`lake-kidney-atlas-nature-2023`](../papers/lake-kidney-atlas-nature-2023/index.md)

### Distal convoluted / connecting tubule (DCT / CNT) · 远曲小管 / 连接小管 {#distal-tubule}

- **EN** — Segments back in the cortex after the loop that fine-tune salt and calcium and connect the nephron to a collecting duct.
- **中文** — 髓袢之后回到皮质的小管段，微调盐和钙，并把肾单位接到集合管上。
- **DE** — Distaler Tubulus / Verbindungstubulus: Segmente nach der Schleife zurück in der Rinde, die Salz und Kalzium fein regulieren und das Nephron mit dem Sammelrohr verbinden.
- _Explained in:_ [3 · The kidney](03-kidney.md)

### Collecting duct (PC / IC) · 集合管（主细胞 / 闰细胞） {#collecting-duct}

- **EN** — The duct that collects fluid from many nephrons and carries it to the papilla; principal cells (PC) set the final water balance, intercalated cells (IC) the acid–base balance.
- **中文** — 汇集多条肾单位液体、通往乳头的管道；主细胞（PC）决定最后的水平衡，闰细胞（IC）调酸碱。
- **DE** — Sammelrohr (Hauptzellen / Schaltzellen): Das Rohr, das die Flüssigkeit vieler Nephrone sammelt und zur Papille leitet; Hauptzellen (PC) regeln den Wasserhaushalt, Schaltzellen (IC) den Säure-Basen-Haushalt.
- _Explained in:_ [3 · The kidney](03-kidney.md)

### Interstitial fibrosis · 间质纤维化 {#interstitial-fibrosis}

- **EN** — Scar-tissue accumulation between the functional units of an organ, scored routinely on H&E as a coarse prognostic marker and the canonical target of 'detect the diseased region' tasks.
- **中文** — 器官功能单位之间瘢痕组织的堆积,常规在 H&E 上评分作为粗略的预后标志,也是「检出病变区域」类任务的经典目标。
- **DE** — Interstitielle Fibrose: Ansammlung von Narbengewebe zwischen den funktionellen Einheiten eines Organs; wird routinemäßig im H&E-Schnitt als grober prognostischer Marker bewertet und ist das klassische Ziel von „Erkenne die erkrankte Region“-Aufgaben.
- _Explained in:_ [3 · The kidney](03-kidney.md)
- _Seen in:_ [`pathomics-npjpo-2026`](../papers/pathomics-npjpo-2026/index.md), [`spatial-natcommun-2024`](../papers/spatial-natcommun-2024/index.md)

## 4 · Patients and tissue

### Acute kidney injury (AKI) · 急性肾损伤 {#acute-kidney-injury}

- **EN** — A sudden loss of kidney function over hours to days (e.g. after surgery, sepsis or drugs); it can recover, or progress to chronic kidney disease.
- **中文** — 几小时到几天内肾功能突然下降（如手术、脓毒症、药物之后）；可能恢复，也可能发展成慢性肾病。
- **DE** — Akute Nierenschädigung: Ein plötzlicher Verlust der Nierenfunktion über Stunden bis Tage (z. B. nach Operation, Sepsis oder Medikamenten); kann sich erholen oder in eine chronische Nierenerkrankung übergehen.
- _Explained in:_ [4 · Patients and tissue](04-patients-tissue.md)
- _Seen in:_ [`lake-kidney-atlas-nature-2023`](../papers/lake-kidney-atlas-nature-2023/index.md)

### Chronic kidney disease (CKD) · 慢性肾脏病(CKD) {#chronic-kidney-disease}

- **EN** — Progressive, largely irreversible loss of kidney function over months to years; the non-tumor disease setting where computational pathology benchmarks are conspicuously absent.
- **中文** — 肾功能在数月至数年间进行性、基本不可逆的丧失;正是在这类非肿瘤疾病场景下,计算病理学的基准明显缺席。
- **DE** — Chronische Nierenerkrankung (CKD): Fortschreitender, weitgehend irreversibler Verlust der Nierenfunktion über Monate bis Jahre; genau jenes nicht-onkologische Krankheitsfeld, in dem Benchmarks der computationalen Pathologie auffällig fehlen.
- _Explained in:_ [4 · Patients and tissue](04-patients-tissue.md)

### Diabetic / hypertensive kidney disease (DKD / H-CKD) · 糖尿病肾病 / 高血压肾病 {#diabetic-kidney-disease}

- **EN** — The two most common causes of chronic kidney disease, labelled DKD and H-CKD (or HKD) in kidney atlases.
- **中文** — 慢性肾病最常见的两种病因，在肾脏图谱里标作 DKD 和 H-CKD（或 HKD）。
- **DE** — Diabetische / hypertensive Nierenerkrankung: Die zwei häufigsten Ursachen der chronischen Nierenerkrankung, in Nierenatlanten als DKD und H-CKD (bzw. HKD) bezeichnet.
- _Explained in:_ [4 · Patients and tissue](04-patients-tissue.md)
- _Seen in:_ [`abedini-kidney-atlas-natgenet-2024`](../papers/abedini-kidney-atlas-natgenet-2024/index.md), [`lake-kidney-atlas-nature-2023`](../papers/lake-kidney-atlas-nature-2023/index.md)

### Estimated glomerular filtration rate (eGFR) · 估算肾小球滤过率(eGFR) {#egfr-kidney-function}

- **EN** — The standard blood-derived estimate of how much the kidneys filter per minute; its trajectory over years is the clinical outcome any prognostic kidney model is ultimately judged against.
- **中文** — 由血液指标估算的肾脏每分钟滤过量,是肾功能的标准度量;其多年的变化轨迹,是任何肾脏预后模型最终要对照的临床结局。
- **DE** — Geschätzte glomeruläre Filtrationsrate (eGFR): Der blutbasierte Standardschätzwert dafür, wie viel die Nieren pro Minute filtern; sein Verlauf über Jahre ist das klinische Ergebnis, an dem sich jedes prognostische Nierenmodell messen lassen muss.
- _Explained in:_ [4 · Patients and tissue](04-patients-tissue.md)

### Kidney biopsy · 肾活检 {#kidney-biopsy}

- **EN** — A needle-extracted core of renal tissue a few millimetres long, the shared raw material every kidney modality reads in its own way — stained, dissociated or profiled in situ.
- **中文** — 用穿刺针取出的数毫米长肾组织条,是所有肾脏 modality 共同的原材料——或染色、或解离、或原位测序,各读各的。
- **DE** — Nierenbiopsie: Ein per Nadel entnommener, wenige Millimeter langer Nierengewebezylinder — das gemeinsame Rohmaterial, das jede Nieren-Modalität auf ihre Weise ausliest: gefärbt, dissoziiert oder in situ profiliert.
- _Explained in:_ [4 · Patients and tissue](04-patients-tissue.md)

### Nephrectomy (tumour nephrectomy) · 肾切除 {#nephrectomy}

- **EN** — Surgical removal of a kidney, usually for a tumour; tissue far from the tumour is used as 'healthy' reference, but it has gone without blood flow for a while.
- **中文** — 手术切除肾，通常因为肿瘤；离肿瘤远的组织被当作'健康'参考，但它已经缺血了一段时间。
- **DE** — Nephrektomie: Operative Entfernung einer Niere, meist wegen eines Tumors; tumorfernes Gewebe dient als 'gesunde' Referenz, war aber eine Zeit lang ohne Durchblutung.
- _Explained in:_ [4 · Patients and tissue](04-patients-tissue.md)
- _Seen in:_ [`abedini-kidney-atlas-natgenet-2024`](../papers/abedini-kidney-atlas-natgenet-2024/index.md), [`kidney-multimodal-genomebiol-2026`](../papers/kidney-multimodal-genomebiol-2026/index.md), [`lake-kidney-atlas-nature-2023`](../papers/lake-kidney-atlas-nature-2023/index.md)

### Deceased donor · 死亡供体 {#deceased-donor}

- **EN** — An organ donor whose kidney was not transplanted and was used for research; ischaemia time is usually longer than for biopsies or nephrectomies.
- **中文** — 器官捐献者的肾最后没被移植、用于研究；缺血时间通常比活检和肾切除更长。
- **DE** — Verstorbener Spender: Ein Organspender, dessen Niere nicht transplantiert, sondern für die Forschung verwendet wurde; die Ischämiezeit ist meist länger als bei Biopsie oder Nephrektomie.
- _Explained in:_ [4 · Patients and tissue](04-patients-tissue.md)
- _Seen in:_ [`lake-kidney-atlas-nature-2023`](../papers/lake-kidney-atlas-nature-2023/index.md)

### Ischaemia (procurement ischaemia) · 缺血（取样缺血） {#ischaemia}

- **EN** — Lack of blood flow; tissue left without blood during surgery or after death switches on stress genes, which can make healthy cells look injured.
- **中文** — 血流中断；手术中或死后没有血供的组织会启动应激基因，让健康细胞看起来像受了伤。
- **DE** — Ischämie: Fehlende Durchblutung; Gewebe ohne Blutversorgung während einer Operation oder nach dem Tod aktiviert Stressgene, sodass gesunde Zellen geschädigt wirken können.
- _Explained in:_ [4 · Patients and tissue](04-patients-tissue.md)
- _Seen in:_ [`lake-kidney-atlas-nature-2023`](../papers/lake-kidney-atlas-nature-2023/index.md)

## 5 · Assays: how the data is made

### Single-cell RNA sequencing (scRNA-seq) · 单细胞 RNA 测序(scRNA-seq) {#single-cell-rna-seq}

- **EN** — A technique that profiles the transcriptome of individual cells, revealing cell-type heterogeneity that bulk sequencing averages away.
- **中文** — 一种对单个细胞转录组进行测序的技术,可揭示被批量测序平均掉的细胞类型异质性。
- **DE** — Einzelzell-RNA-Sequenzierung (scRNA-seq): Eine Technik, die das Transkriptom einzelner Zellen erfasst und die Zelltyp-Heterogenität sichtbar macht, die bei Bulk-Sequenzierung verloren geht.
- _Explained in:_ [5 · Assays: how the data is made](05-assays.md)
- _Seen in:_ [`scrna-natmachintell-2026`](../papers/scrna-natmachintell-2026/index.md), [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md), [`spatial-natcommun-2024`](../papers/spatial-natcommun-2024/index.md)

### Single-nucleus RNA-seq (snRNA-seq) · 单核 RNA 测序(snRNA-seq) {#snrna-seq}

- **EN** — Dissociates tissue down to individual nuclei and sequences the RNA in each, giving genome-wide expression per nucleus at the cost of losing every cell's position in the tissue.
- **中文** — 把组织解离成单个细胞核并分别测其 RNA,得到每个核的全基因组表达,代价是彻底丢失细胞原本在组织中的位置。
- **DE** — Einzelkern-RNA-Sequenzierung (snRNA-seq): Zerlegt Gewebe in einzelne Zellkerne und sequenziert deren RNA; liefert genomweite Expression pro Kern, verliert dabei aber jede räumliche Position der Zellen.
- _Explained in:_ [5 · Assays: how the data is made](05-assays.md)

### Tissue dissociation · 组织解离 {#tissue-dissociation}

- **EN** — Breaking tissue into single cells, usually with enzymes at 37 °C, before single-cell RNA-seq; needed for whole cells but stresses them.
- **中文** — 做单细胞 RNA 测序前把组织拆成单个细胞，通常用酶在 37 °C 消化；能得到完整细胞，但会让细胞应激。
- **DE** — Gewebedissoziation: Zerlegen von Gewebe in Einzelzellen, meist enzymatisch bei 37 °C, vor der Einzelzell-RNA-Sequenzierung; liefert ganze Zellen, setzt sie aber unter Stress.
- _Explained in:_ [5 · Assays: how the data is made](05-assays.md)
- _Seen in:_ [`denisenko-dissociation-bias-genomebiol-2020`](../papers/denisenko-dissociation-bias-genomebiol-2020/index.md), [`lake-snrna-pipeline-natcommun-2019`](../papers/lake-snrna-pipeline-natcommun-2019/index.md)

### 10x Chromium (Cv3) · 10x Chromium（Cv3 = 第 3 版试剂） {#chromium-10x}

- **EN** — The most common commercial single-cell platform: it packs each cell or nucleus into an oil droplet with a barcoded bead. Cv3 = Chromium v3 chemistry (snCv3 / scCv3 in Lake 2023).
- **中文** — 最常用的商业单细胞平台：把每个细胞或核和一颗带条形码的珠子一起包进油滴。Cv3 = Chromium 第 3 版试剂（Lake 2023 里的 snCv3 / scCv3）。
- **DE** — 10x Chromium (Cv3): Die verbreitetste kommerzielle Einzelzellplattform: sie verpackt jede Zelle bzw. jeden Kern mit einem barcodierten Bead in ein Öltröpfchen. Cv3 = Chromium-v3-Chemie.
- _Explained in:_ [5 · Assays: how the data is made](05-assays.md)
- _Seen in:_ [`kidney-multimodal-genomebiol-2026`](../papers/kidney-multimodal-genomebiol-2026/index.md), [`lake-kidney-atlas-nature-2023`](../papers/lake-kidney-atlas-nature-2023/index.md)

### Cell barcode · 细胞条形码 {#cell-barcode}

- **EN** — A short DNA tag attached to every RNA from the same droplet (or the same split-pool path), so reads can be sorted back to their cell; becomes the row ID of the count matrix.
- **中文** — 贴在同一个油滴（或同一条分池路径）里所有 RNA 上的短 DNA 标签，用来把读段分回各个细胞；它就是计数矩阵的行 ID。
- **DE** — Zell-Barcode: Ein kurzer DNA-Tag an jeder RNA aus demselben Tröpfchen (oder demselben Split-Pool-Weg), mit dem Reads ihrer Zelle zugeordnet werden; die Zeilen-ID der Zählmatrix.
- _Explained in:_ [5 · Assays: how the data is made](05-assays.md)

### UMI (unique molecular identifier) · UMI（分子唯一标识） {#umi}

- **EN** — A random tag on each RNA molecule before amplification, so copies made by PCR can be collapsed; the numbers in the count matrix are UMI counts (nCount_RNA = total UMIs per cell).
- **中文** — 扩增前贴在每条 RNA 分子上的随机标签，用来去掉 PCR 复制出的重复；计数矩阵里的数字就是 UMI 数（nCount_RNA = 一个细胞的 UMI 总数）。
- **DE** — UMI (Unique Molecular Identifier): Ein zufälliger Tag an jedem RNA-Molekül vor der Amplifikation, damit PCR-Kopien zusammengefasst werden; die Werte der Zählmatrix sind UMI-Zahlen.
- _Explained in:_ [5 · Assays: how the data is made](05-assays.md)

### Single-nucleus ATAC-seq (snATAC-seq) · 单核 ATAC 测序(snATAC-seq) {#snatac-seq}

- **EN** — Uses a transposase that cuts only unpacked DNA to map which genomic regions are open per nucleus, revealing which genes are permitted to be expressed rather than which currently are.
- **中文** — 用只能切开松散 DNA 的转座酶,逐核绘制哪些基因组区域处于开放状态,揭示哪些基因「有资格」表达,而非当前正在表达什么。
- **DE** — Einzelkern-ATAC-Sequenzierung (snATAC-seq): Nutzt eine Transposase, die nur ungepackte DNA schneidet, um pro Zellkern offene Genomregionen zu kartieren; zeigt, welche Gene exprimiert werden dürfen, nicht welche es gerade werden.
- _Explained in:_ [5 · Assays: how the data is made](05-assays.md)

### Chromatin accessibility · 染色质开放性 {#chromatin-accessibility}

- **EN** — How physically reachable a stretch of DNA is for transcription machinery; tightly packed regions are effectively switched off, loosened ones are available for expression.
- **中文** — 一段 DNA 对转录机器的物理可及程度;缠绕紧密的区域等同于被关闭,松开的区域才可能被表达。
- **DE** — Chromatin-Zugänglichkeit: Wie physisch erreichbar ein DNA-Abschnitt für die Transkriptionsmaschinerie ist; dicht gepackte Regionen sind faktisch abgeschaltet, gelockerte stehen zur Expression bereit.
- _Explained in:_ [5 · Assays: how the data is made](05-assays.md)

### Tn5 transposase · Tn5 转座酶 {#tn5-transposase}

- **EN** — The enzyme used in ATAC-seq: it can only cut into open (unwound) DNA and inserts sequencing adapters as it cuts, so where it cuts marks accessible chromatin.
- **中文** — ATAC-seq 用的酶：只能剪进打开（没缠紧）的 DNA，剪的同时插入测序接头，所以它剪过的位置标出了开放染色质。
- **DE** — Tn5-Transposase: Das Enzym der ATAC-seq: es schneidet nur in offene (entwundene) DNA und fügt dabei Sequenzieradapter ein; seine Schnittstellen markieren zugängliches Chromatin.
- _Explained in:_ [5 · Assays: how the data is made](05-assays.md)

### ATAC peak · ATAC 峰 {#atac-peak}

- **EN** — A genomic interval where transposase cut sites pile up across many nuclei, defining a region of open chromatin and forming the row dimension of the peak-by-cell matrix.
- **中文** — 转座酶切点在众多细胞核中反复堆积的基因组区间,标定一段开放染色质,并构成「峰 × 细胞」矩阵的行维度。
- **DE** — ATAC-Peak: Ein genomisches Intervall, in dem sich Transposase-Schnittstellen über viele Zellkerne häufen; definiert offenes Chromatin und bildet die Zeilendimension der Peak-Zell-Matrix.
- _Explained in:_ [5 · Assays: how the data is made](05-assays.md)

### Multiome (joint RNA + ATAC) · Multiome(RNA 与 ATAC 同核联测) {#multiome}

- **EN** — An assay that measures transcription and chromatin accessibility in the very same nucleus, pairing 'what is expressed' with 'what is permitted' without having to match cells across separate runs.
- **中文** — 在同一个细胞核里同时测转录与染色质开放性的实验,把「表达了什么」与「允许表达什么」直接配对,无需在两批细胞之间猜对应关系。
- **DE** — Multiome (gemeinsam RNA + ATAC): Ein Assay, der Transkription und Chromatin-Zugänglichkeit im selben Zellkern misst und so „was exprimiert wird“ direkt mit „was erlaubt ist“ paart, ohne Zellen zwischen Läufen zuordnen zu müssen.
- _Explained in:_ [5 · Assays: how the data is made](05-assays.md)

### SNARE-seq2 · SNARE-seq2（SNARE2） {#snare-seq2}

- **EN** — Single-Nucleus chromatin Accessibility and mRNA Expression sequencing, version 2: measures RNA and ATAC in the same nucleus using split-pool (combinatorial) barcoding instead of droplets; used for 7 healthy donors in Lake 2023.
- **中文** — 单核染色质可及性与 mRNA 表达测序第 2 版：在同一个核里同时测 RNA 和 ATAC，用分池混合编码代替油滴；Lake 2023 用它测了 7 个健康人。
- **DE** — SNARE-seq2: Single-Nucleus chromatin Accessibility and mRNA Expression sequencing, Version 2: misst RNA und ATAC im selben Kern mit kombinatorischem Split-Pool-Barcoding statt Tröpfchen.
- _Explained in:_ [5 · Assays: how the data is made](05-assays.md)
- _Seen in:_ [`lake-kidney-atlas-nature-2023`](../papers/lake-kidney-atlas-nature-2023/index.md)

### Spatial transcriptomics · 空间转录组学 {#spatial-transcriptomics}

- **EN** — A family of technologies that measure gene expression while preserving each cell's or spot's position within an intact tissue section.
- **中文** — 一类在保留细胞或位点在完整组织切片中位置的同时测量基因表达的技术。
- **DE** — Räumliche Transkriptomik: Eine Gruppe von Technologien, die die Genexpression messen und dabei die Position jeder Zelle oder jedes Spots im intakten Gewebeschnitt erhalten.
- _Explained in:_ [5 · Assays: how the data is made](05-assays.md)
- _Seen in:_ [`fm-arxiv-2604`](../papers/fm-arxiv-2604/index.md), [`hest1k-2024`](../papers/hest1k-2024/index.md), [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md), [`spatial-natcommun-2024`](../papers/spatial-natcommun-2024/index.md)

### Visium · Visium {#visium}

- **EN** — A widely used 10x Genomics spatial-transcriptomics platform that captures gene expression on a grid of barcoded spots overlaid on a tissue slide.
- **中文** — 一种广泛使用的 10x Genomics 空间转录组平台,在覆盖组织切片的条形码位点阵列上捕获基因表达。
- **DE** — Visium: Eine weit verbreitete Spatial-Transcriptomics-Plattform von 10x Genomics, die Genexpression auf einem Raster barcodierter Spots über einem Gewebeschnitt erfasst.
- _Explained in:_ [5 · Assays: how the data is made](05-assays.md)
- _Seen in:_ [`hest1k-2024`](../papers/hest1k-2024/index.md), [`spatial-natcommun-2024`](../papers/spatial-natcommun-2024/index.md)

### Xenium · Xenium {#xenium}

- **EN** — A 10x Genomics imaging-based platform that measures a targeted panel of transcripts in situ at subcellular resolution with single-cell segmentation.
- **中文** — 一种基于成像的 10x Genomics 平台,在亚细胞分辨率下原位测量目标转录本组合,并进行单细胞分割。
- **DE** — Xenium: Eine bildgebungsbasierte 10x-Genomics-Plattform, die ein gezieltes Transkript-Panel in situ mit subzellulärer Auflösung und Einzelzell-Segmentierung misst.
- _Explained in:_ [5 · Assays: how the data is made](05-assays.md)
- _Seen in:_ [`hest1k-2024`](../papers/hest1k-2024/index.md), [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md)

### SNP / genotype · SNP / 基因型 {#snp-genotype}

- **EN** — Single-base differences between people (or mouse strains); the set a person carries is their genotype, a DNA fingerprint stored in VCF files and measured by WES or arrays.
- **中文** — 人与人（或小鼠品系之间）单个碱基的差异；一个人带的这一整套就是他的基因型，相当于 DNA 指纹，存成 VCF 文件，用 WES 或芯片测得。
- **DE** — SNP / Genotyp: Einzelbasen-Unterschiede zwischen Personen (oder Mausstämmen); die Gesamtheit ist der Genotyp, ein DNA-Fingerabdruck in VCF-Dateien, gemessen per WES oder Array.
- _Explained in:_ [5 · Assays: how the data is made](05-assays.md)
- _Seen in:_ [`hoeft-genotype-multiplexing-natcommun-2024`](../papers/hoeft-genotype-multiplexing-natcommun-2024/index.md), [`janssen-ambient-noise-genomebiol-2023`](../papers/janssen-ambient-noise-genomebiol-2023/index.md), [`malone-transplant-chimerism-jasn-2020`](../papers/malone-transplant-chimerism-jasn-2020/index.md)

### Genotype multiplexing / demultiplexing · 基因型混样 / 分人 {#genotype-demultiplexing}

- **EN** — Pooling cells from several people in one run and sorting them back by SNPs (demuxlet, souporcell, vireo); it also reveals droplets with two people's SNPs (doublets) and foreign RNA (ambient contamination).
- **中文** — 把几个人的细胞混在一次实验里测，事后按 SNP 分回各人（demuxlet、souporcell、vireo）；同时能发现带两个人 SNP 的液滴（doublet）和外来 RNA（ambient 污染）。
- **DE** — Genotyp-Multiplexing / Demultiplexing: Zellen mehrerer Personen gemeinsam messen und per SNPs zurück zuordnen (demuxlet, souporcell, vireo); zeigt zugleich Tröpfchen mit zwei Genotypen (Dubletten) und fremde RNA (Ambient-Kontamination).
- _Explained in:_ [5 · Assays: how the data is made](05-assays.md)
- _Seen in:_ [`hoeft-genotype-multiplexing-natcommun-2024`](../papers/hoeft-genotype-multiplexing-natcommun-2024/index.md), [`malone-transplant-chimerism-jasn-2020`](../papers/malone-transplant-chimerism-jasn-2020/index.md)

## 6 · Artifacts, and biology that looks like one

### Doublet · 双细胞假象(doublet) {#doublet}

- **EN** — A technical artifact where two cells or nuclei are captured under one barcode and analysed as a single cell, producing a chimeric expression profile that can masquerade as a novel cell state.
- **中文** — 两个细胞或细胞核被同一条形码捕获、当作一个细胞分析的技术假象,产生嵌合表达谱,可能被误认为一种新的细胞状态。
- **DE** — Doublet: Ein technisches Artefakt, bei dem zwei Zellen bzw. Zellkerne unter einem Barcode erfasst und als eine Zelle ausgewertet werden; das chimäre Expressionsprofil kann einen neuen Zellzustand vortäuschen.
- _Explained in:_ [6 · Artifacts, and biology that looks like one](06-artifacts.md)

### Ambient RNA · 游离 RNA 污染(ambient RNA) {#ambient-rna}

- **EN** — Free-floating transcripts released by lysed cells that get counted into other droplets, adding a background signal that makes unrelated cells look alike.
- **中文** — 破裂细胞释放的游离转录本被计入其他液滴,形成背景信号,使本不相关的细胞看起来彼此相似。
- **DE** — Ambient-RNA: Frei schwebende Transkripte lysierter Zellen, die in andere Tröpfchen mitgezählt werden und ein Hintergrundsignal erzeugen, das unverwandte Zellen ähnlich erscheinen lässt.
- _Explained in:_ [6 · Artifacts, and biology that looks like one](06-artifacts.md)

### Empty droplet · 空液滴 {#empty-droplet}

- **EN** — A droplet without a cell; it captures only free-floating RNA, so it samples the ambient profile. Present in the raw matrix, removed from the filtered one.
- **中文** — 没装细胞的油滴；里面只有漂在液体里的 RNA，所以正好是 ambient 的样本。raw 矩阵里有，filtered 矩阵里被去掉。
- **DE** — Leeres Tröpfchen: Ein Tröpfchen ohne Zelle; es enthält nur frei schwebende RNA und ist damit eine Stichprobe des Ambient-Profils. In der Raw-Matrix enthalten, in der gefilterten entfernt.
- _Explained in:_ [6 · Artifacts, and biology that looks like one](06-artifacts.md)
- _Seen in:_ [`janssen-ambient-noise-genomebiol-2023`](../papers/janssen-ambient-noise-genomebiol-2023/index.md)

### Low-quality cell · 低质量细胞 {#low-quality-cell}

- **EN** — A dying or broken cell with few RNA molecules and genes and a high mitochondrial fraction; usually filtered by QC thresholds, but injured cells can look similar.
- **中文** — 快死或破损的细胞：RNA 分子和基因数少、线粒体比例高；通常按 QC 阈值过滤掉，但受损细胞也可能长得很像。
- **DE** — Zelle geringer Qualität: Eine sterbende oder beschädigte Zelle mit wenigen RNA-Molekülen und Genen und hohem Mitochondrienanteil; meist per QC-Schwelle gefiltert, doch geschädigte Zellen sehen ähnlich aus.
- _Explained in:_ [6 · Artifacts, and biology that looks like one](06-artifacts.md)
- _Seen in:_ [`lake-kidney-atlas-nature-2023`](../papers/lake-kidney-atlas-nature-2023/index.md)

### Mitochondrial fraction (percent.mt) · 线粒体比例 {#mitochondrial-fraction}

- **EN** — The share of a cell's RNA from mitochondrial genes; a standard QC metric (high = stressed or dying cell). Naturally higher in whole cells than in nuclei.
- **中文** — 一个细胞的 RNA 里来自线粒体基因的比例；标准 QC 指标（高 = 细胞应激或快死了）。完整细胞本来就比细胞核高。
- **DE** — Mitochondrialer Anteil: Der Anteil der RNA einer Zelle aus mitochondrialen Genen; Standard-QC-Metrik (hoch = gestresste oder sterbende Zelle). In ganzen Zellen natürlich höher als in Kernen.
- _Explained in:_ [6 · Artifacts, and biology that looks like one](06-artifacts.md)

### Dissociation stress · 解离应激 {#dissociation-stress}

- **EN** — Stress genes (FOS, JUN, heat-shock genes) switched on while tissue is digested at 37 °C; makes cells look injured although the injury happened in the lab.
- **中文** — 组织在 37 °C 消化时细胞启动的应激基因（FOS、JUN、热休克蛋白等）；让细胞看起来受了伤，其实伤是在实验室里造成的。
- **DE** — Dissoziationsstress: Stressgene (FOS, JUN, Hitzeschockgene), die beim Verdau des Gewebes bei 37 °C angeschaltet werden; Zellen wirken geschädigt, obwohl der Schaden im Labor entstand.
- _Explained in:_ [6 · Artifacts, and biology that looks like one](06-artifacts.md)
- _Seen in:_ [`denisenko-dissociation-bias-genomebiol-2020`](../papers/denisenko-dissociation-bias-genomebiol-2020/index.md)

### Technical dropout (false zero) · 技术性丢失(假零) {#technical-dropout}

- **EN** — A zero in a count matrix caused by failed capture rather than absent expression; because true and false zeros are indistinguishable, sparsity is both biology and noise at once.
- **中文** — 计数矩阵中因捕获失败而非真的不表达所产生的零;由于真零与假零无法区分,稀疏性同时既是生物学也是噪声。
- **DE** — Technischer Dropout (falsche Null): Eine Null in der Zählmatrix, die durch fehlgeschlagene Erfassung statt fehlender Expression entsteht; da echte und falsche Nullen ununterscheidbar sind, ist Sparsity zugleich Biologie und Rauschen.
- _Explained in:_ [6 · Artifacts, and biology that looks like one](06-artifacts.md)

### Batch effect · 批次效应 {#batch-effect}

- **EN** — Systematic non-biological variation between datasets acquired at different sites, times, or platforms that can confound analysis if not corrected.
- **中文** — 不同机构、时间或平台采集的数据集之间的系统性非生物学差异,若不校正会混淆分析。
- **DE** — Batch-Effekt: Systematische, nicht-biologische Variation zwischen Datensätzen, die an verschiedenen Orten, Zeiten oder Plattformen erhoben wurden und die Analyse verfälschen kann, wenn sie nicht korrigiert wird.
- _Explained in:_ [6 · Artifacts, and biology that looks like one](06-artifacts.md)
- _Seen in:_ [`scrna-natmachintell-2026`](../papers/scrna-natmachintell-2026/index.md), [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md)

### Polyploidy / multinucleation · 多倍体 / 多核 {#polyploidy}

- **EN** — Cells with extra DNA copies or more than one nucleus; after injury some tubular cells become polyploid and some podocytes binucleated. In single-cell data such cells can look like doublets.
- **中文** — DNA 拷贝多出来或有不止一个核的细胞；损伤后一些小管细胞会变成多倍体，一些足细胞会变成双核。在单细胞数据里，这类细胞可能看起来像 doublet。
- **DE** — Polyploidie / Mehrkernigkeit: Zellen mit zusätzlichen DNA-Kopien oder mehr als einem Kern; nach Schädigung werden manche Tubuluszellen polyploid und manche Podozyten zweikernig. In Einzelzelldaten können sie wie Dubletten aussehen.
- _Explained in:_ [6 · Artifacts, and biology that looks like one](06-artifacts.md)

## 7 · How to read a dataset

### KPMP (Kidney Precision Medicine Project) · KPMP（肾脏精准医学项目） {#kpmp}

- **EN** — An NIH consortium that collects kidney biopsies from AKI and CKD patients and profiles them with single-cell, spatial and imaging assays; the main source of Lake 2023.
- **中文** — 美国 NIH 的联盟项目，收集 AKI 和 CKD 病人的肾活检，用单细胞、空间和成像方法测；Lake 2023 的主要数据来源。
- **DE** — KPMP (Kidney Precision Medicine Project): Ein NIH-Konsortium, das Nierenbiopsien von AKI- und CKD-Patienten sammelt und mit Einzelzell-, Raum- und Bildgebungsverfahren profiliert; Hauptquelle von Lake 2023.
- _Explained in:_ [7 · How to read a dataset](07-datasets.md)
- _Seen in:_ [`cellspectra-natgenet-2025`](../papers/cellspectra-natgenet-2025/index.md), [`damage-scores-cellgenomics-2026`](../papers/damage-scores-cellgenomics-2026/index.md), [`lake-kidney-atlas-nature-2023`](../papers/lake-kidney-atlas-nature-2023/index.md)

### CZ CELLxGENE · CELLxGENE 数据平台 {#cellxgene}

- **EN** — The Chan Zuckerberg single-cell portal that serves curated datasets as standard h5ad files with harmonised metadata; the easiest way to download Lake 2023 and mBDRC.
- **中文** — Chan Zuckerberg 的单细胞数据平台，把整理好的数据集统一成 h5ad 文件和标准标签提供下载；下载 Lake 2023 和 mBDRC 最方便的途径。
- **DE** — CZ CELLxGENE: Das Einzelzellportal der Chan-Zuckerberg-Initiative, das kuratierte Datensätze als h5ad mit harmonisierten Metadaten bereitstellt.
- _Explained in:_ [7 · How to read a dataset](07-datasets.md)

### GEO / SRA · GEO / SRA 公共数据库 {#geo-sra}

- **EN** — NCBI's public repositories: GEO holds processed data (count matrices, metadata tables), SRA holds raw sequencing reads (FASTQ); free to download.
- **中文** — NCBI 的公共数据库：GEO 放处理后的数据（计数矩阵、标签表），SRA 放原始测序读段（FASTQ）；免费下载。
- **DE** — GEO / SRA: Öffentliche NCBI-Datenbanken: GEO enthält prozessierte Daten (Zählmatrizen, Metadaten), SRA rohe Sequenzierreads (FASTQ); frei herunterladbar.
- _Explained in:_ [7 · How to read a dataset](07-datasets.md)

### dbGaP / EGA (controlled access) · dbGaP / EGA（受控访问） {#dbgap}

- **EN** — Controlled-access archives for human raw sequencing data that could identify a person; access requires an application and a data-use agreement.
- **中文** — 存放可识别个人的人类原始测序数据的受控数据库；要提交申请并签数据使用协议才能下载。
- **DE** — dbGaP / EGA (kontrollierter Zugang): Archive mit kontrolliertem Zugang für menschliche Rohsequenzdaten, die eine Person identifizieren könnten; Zugang nur per Antrag und Datennutzungsvereinbarung.
- _Explained in:_ [7 · How to read a dataset](07-datasets.md)

## 8 · What we are working on

### Anomaly detection · 异常检测 {#anomaly-detection}

- **EN** — Identifying samples or regions that deviate from a learned notion of 'normal', often by training only on normal data — the first stage of the detect→model→revert pipeline.
- **中文** — 识别偏离所学“正常”概念的样本或区域,常仅用正常数据训练——即“检测→建模→逆转”流程的第一环。
- **DE** — Anomalieerkennung: Das Erkennen von Proben oder Regionen, die von einem gelernten Begriff des 'Normalen' abweichen, oft durch Training nur auf normalen Daten — die erste Stufe der Detect→Model→Revert-Pipeline.
- _Explained in:_ [8 · What we are working on](08-our-problem.md)
- _Seen in:_ [`histo-anomaly-bi-repo`](../papers/histo-anomaly-bi-repo/index.md), [`histo-miccai-2025`](../papers/histo-miccai-2025/index.md), [`histo-nejmai-2024`](../papers/histo-nejmai-2024/index.md), [`imaging-ehjdh-2026`](../papers/imaging-ehjdh-2026/index.md), [`imaging-nature-2026`](../papers/imaging-nature-2026/index.md), [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md), [`spatial-natcommun-2024`](../papers/spatial-natcommun-2024/index.md)

### Altered state (reference vs altered) · 改变态（参考态 vs 改变态） {#altered-state}

- **EN** — Lake 2023's label for cell states that differ from healthy (degenerative, adaptive/repairing, cycling, transitioning), as opposed to 'reference'; assigned by experts after clustering, and also found in healthy donors.
- **中文** — Lake 2023 给偏离健康的细胞状态起的名字（退化、修复、增殖、过渡），与'参考态'相对；是聚类后由专家判读的，健康人身上也有。
- **DE** — Veränderter Zustand: Lake-2023-Bezeichnung für Zellzustände, die vom Gesunden abweichen (degenerativ, adaptiv/reparierend, zyklisch, im Übergang), im Gegensatz zu 'Referenz'; nach Clustering von Experten vergeben, auch bei Gesunden vorhanden.
- _Explained in:_ [8 · What we are working on](08-our-problem.md)
- _Seen in:_ [`lake-kidney-atlas-nature-2023`](../papers/lake-kidney-atlas-nature-2023/index.md)

### One-class classification · 单类分类 {#one-class-classification}

- **EN** — Learning a boundary from examples of a single normal class so that anything falling outside it is flagged as anomalous.
- **中文** — 仅从单一正常类别的样本学习一个边界,凡落在边界之外者即判为异常。
- **DE** — Einklassen-Klassifikation: Das Lernen einer Grenze aus Beispielen einer einzigen Normalklasse, sodass alles außerhalb als anomal markiert wird.
- _Explained in:_ [8 · What we are working on](08-our-problem.md)
- _Seen in:_ [`histo-anomaly-bi-repo`](../papers/histo-anomaly-bi-repo/index.md), [`histo-nejmai-2024`](../papers/histo-nejmai-2024/index.md)

### Domain shift · 域偏移 {#domain-shift}

- **EN** — A drop in model performance when test data differs from training data, for example due to a different scanner or staining protocol.
- **中文** — 当测试数据与训练数据不同(例如换了扫描仪或染色方案)时导致的模型性能下降。
- **DE** — Domänenverschiebung: Ein Leistungsabfall des Modells, wenn Testdaten von den Trainingsdaten abweichen, etwa durch einen anderen Scanner oder ein anderes Färbeprotokoll.
- _Explained in:_ [8 · What we are working on](08-our-problem.md)
- _Seen in:_ [`histo-miccai-2025`](../papers/histo-miccai-2025/index.md), [`uni2-h-model`](../papers/uni2-h-model/index.md), [`virchow-2024`](../papers/virchow-2024/index.md)

### AUROC / AUC (area under the ROC curve) · AUROC / AUC(ROC 曲线下面积) {#auroc}

- **EN** — A threshold-independent measure of a classifier's ability to rank positives above negatives; 0.5 is chance and 1.0 is perfect discrimination.
- **中文** — 衡量分类器把正例排在负例之前能力的阈值无关指标;0.5 为随机,1.0 为完美区分。
- **DE** — AUROC / AUC (Fläche unter der ROC-Kurve): Ein schwellenunabhängiges Maß für die Fähigkeit eines Klassifikators, Positive über Negative zu ordnen; 0,5 ist Zufall, 1,0 perfekte Trennschärfe.
- _Explained in:_ [8 · What we are working on](08-our-problem.md)
- _Seen in:_ [`histo-miccai-2025`](../papers/histo-miccai-2025/index.md), [`imaging-ehjdh-2026`](../papers/imaging-ehjdh-2026/index.md)

## More terms from the papers

### Single-cell

#### CRISPR perturbation · CRISPR 扰动 {#crispr-perturbation}

- **EN** — The deliberate silencing, activation, or editing of a target gene using CRISPR to observe the resulting change in cell state.
- **中文** — 利用 CRISPR 对目标基因进行定向沉默、激活或编辑,以观察由此引起的细胞状态变化。
- **DE** — CRISPR-Perturbation: Das gezielte Stilllegen, Aktivieren oder Editieren eines Zielgens mittels CRISPR, um die daraus folgende Änderung des Zellzustands zu beobachten.
- _Seen in:_ [`virtual-cell-challenge`](../papers/virtual-cell-challenge/index.md)

#### Multi-omics · 多组学 {#multi-omics}

- **EN** — Measuring several molecular layers — for example the epigenome and the transcriptome — on the same samples so that the layers can corroborate or contradict one another.
- **中文** — 在同一批样本上测量多个分子层(例如表观组与转录组),使各层之间可以互相印证或互相矛盾。
- **DE** — Multi-Omics: Die Messung mehrerer molekularer Ebenen — etwa Epigenom und Transkriptom — an denselben Proben, sodass sich die Ebenen gegenseitig bestätigen oder widersprechen können.
- _Seen in:_ [`histo-sciencedirect-2026`](../papers/histo-sciencedirect-2026/index.md)

#### Multi-Omics Factor Analysis (MOFA) · 多组学因子分析(MOFA) {#mofa}

- **EN** — An unsupervised integration method that compresses several differently shaped omics matrices into a shared set of latent factors, surfacing variation that co-varies across layers.
- **中文** — 一种无监督整合方法,把形状各异的多个组学矩阵压缩到一组共享潜因子上,使跨层共变的变异显形。
- **DE** — Multi-Omics-Faktoranalyse (MOFA): Eine unüberwachte Integrationsmethode, die mehrere unterschiedlich geformte Omics-Matrizen in gemeinsame latente Faktoren komprimiert und schichtübergreifend ko-variierende Variation sichtbar macht.

#### Perturb-seq · Perturb-seq {#perturb-seq}

- **EN** — A screening method that pairs CRISPR perturbations with single-cell RNA sequencing to read out how each genetic perturbation reshapes the transcriptome.
- **中文** — 一种将 CRISPR 扰动与单细胞 RNA 测序结合的筛选方法,可读出每个基因扰动如何重塑转录组。
- **DE** — Perturb-seq: Eine Screening-Methode, die CRISPR-Perturbationen mit Einzelzell-RNA-Sequenzierung koppelt, um zu erfassen, wie jede genetische Störung das Transkriptom verändert.
- _Seen in:_ [`virtual-cell-challenge`](../papers/virtual-cell-challenge/index.md)

#### Perturbation-response prediction · 扰动响应预测 {#perturbation-response-prediction}

- **EN** — The task of predicting how a cell's gene expression will shift after a given genetic or drug perturbation, often for unseen conditions.
- **中文** — 预测给定基因或药物扰动后细胞基因表达如何变化的任务,通常针对未见过的条件。
- **DE** — Vorhersage der Perturbationsantwort: Die Aufgabe vorherzusagen, wie sich die Genexpression einer Zelle nach einer bestimmten genetischen oder medikamentösen Störung verschiebt, oft für ungesehene Bedingungen.
- _Seen in:_ [`scrna-natmachintell-2026`](../papers/scrna-natmachintell-2026/index.md), [`virtual-cell-challenge`](../papers/virtual-cell-challenge/index.md)

#### Transcription-factor motif · 转录因子结合基序 {#tf-motif}

- **EN** — The short DNA sequence pattern a transcription factor recognizes; enrichment of a motif inside accessible regions is the standard evidence for inferring which regulator drives a cell state.
- **中文** — 转录因子识别的短 DNA 序列模式;开放区域中某基序的富集,是推断哪个调控因子驱动了某种细胞状态的标准证据。
- **DE** — Transkriptionsfaktor-Motiv: Das kurze DNA-Sequenzmuster, das ein Transkriptionsfaktor erkennt; die Anreicherung eines Motivs in zugänglichen Regionen ist der Standardbeleg dafür, welcher Regulator einen Zellzustand antreibt.

#### Virtual cell · 虚拟细胞 {#virtual-cell}

- **EN** — A computational model of a cell that predicts how its molecular state responds to perturbations, enabling experiments to be run in silico.
- **中文** — 细胞的计算模型,可预测其分子状态对扰动的响应,从而在计算机中开展实验。
- **DE** — Virtuelle Zelle: Ein rechnerisches Zellmodell, das vorhersagt, wie der molekulare Zustand einer Zelle auf Störungen reagiert, und Experimente in silico ermöglicht.
- _Seen in:_ [`virtual-cell-challenge`](../papers/virtual-cell-challenge/index.md)

### Spatial omics

#### Anomalous tissue domain (ATD) · 异常组织域(ATD) {#anomalous-tissue-domain}

- **EN** — A spatial region of a tissue whose molecular profile deviates from healthy reference tissue, typically because of disease and detected without predefined markers.
- **中文** — 组织中分子特征偏离健康参考组织的空间区域,通常由疾病导致,可在无预定义标记物的情况下被检出。
- **DE** — Anomale Gewebedomäne (ATD): Eine räumliche Gewebsregion, deren molekulares Profil vom gesunden Referenzgewebe abweicht, meist krankheitsbedingt und ohne vordefinierte Marker erkennbar.
- _Seen in:_ [`spatial-natcommun-2024`](../papers/spatial-natcommun-2024/index.md)

#### Cell segmentation · 细胞分割 {#cell-segmentation}

- **EN** — The image-analysis step of delineating individual cell boundaries so that molecular signals can be assigned to single cells.
- **中文** — 在图像分析中勾勒单个细胞边界的步骤,以便将分子信号归属到单个细胞。
- **DE** — Zellsegmentierung: Der bildanalytische Schritt, einzelne Zellgrenzen abzugrenzen, damit molekulare Signale einzelnen Zellen zugeordnet werden können.
- _Seen in:_ [`hest1k-2024`](../papers/hest1k-2024/index.md), [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md)

#### Cellular niche · 细胞微环境龛位(niche) {#cellular-niche}

- **EN** — A local neighborhood of cells whose spatial composition and interactions define a distinct micro-environment within a tissue.
- **中文** — 由细胞的空间组成与相互作用界定的局部细胞邻域,构成组织内一个独特的微环境。
- **DE** — Zelluläre Nische: Eine lokale Zellnachbarschaft, deren räumliche Zusammensetzung und Interaktionen ein eigenes Mikromilieu im Gewebe definieren.
- _Seen in:_ [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md), [`virtual-tissue-2501`](../papers/virtual-tissue-2501/index.md)

#### Imaging mass cytometry (IMC) · 成像质谱流式(IMC) {#imaging-mass-cytometry}

- **EN** — A multiplexed imaging method that uses metal-tagged antibodies and mass spectrometry to map dozens of proteins across a tissue section at subcellular resolution.
- **中文** — 一种多重成像方法,利用金属标记抗体与质谱在亚细胞分辨率下绘制组织切片中数十种蛋白质。
- **DE** — Bildgebende Massenzytometrie (IMC): Eine multiplexierte Bildgebungsmethode, die metallmarkierte Antikörper und Massenspektrometrie nutzt, um Dutzende Proteine in einem Gewebeschnitt mit subzellulärer Auflösung zu kartieren.
- _Seen in:_ [`virtual-tissue-2501`](../papers/virtual-tissue-2501/index.md)

#### Multiplexed imaging · 多重成像 {#multiplexed-imaging}

- **EN** — Imaging that captures many molecular channels (proteins or transcripts) in the same tissue section rather than just one or two stains.
- **中文** — 在同一组织切片中捕获多个分子通道(蛋白质或转录本)的成像,而非仅一两种染色。
- **DE** — Multiplex-Bildgebung: Bildgebung, die viele molekulare Kanäle (Proteine oder Transkripte) im selben Gewebeschnitt erfasst statt nur ein oder zwei Färbungen.
- _Seen in:_ [`scrna-natmachintell-2026`](../papers/scrna-natmachintell-2026/index.md), [`virtual-tissue-2501`](../papers/virtual-tissue-2501/index.md)

#### Slide-seq · Slide-seq {#slide-seq}

- **EN** — A spatial-transcriptomics method that transfers tissue onto a bead array of positionally barcoded beads, giving near-cellular spatial resolution.
- **中文** — 一种将组织转移到带有位置条形码微珠阵列上的空间转录组方法,可达到接近单细胞的空间分辨率。
- **DE** — Slide-seq: Eine Spatial-Transcriptomics-Methode, die Gewebe auf ein Array positionsbarcodierter Beads überträgt und nahezu zelluläre räumliche Auflösung erreicht.
- _Seen in:_ [`spatial-natcommun-2024`](../papers/spatial-natcommun-2024/index.md)

#### Spatial proteomics · 空间蛋白质组学 {#spatial-proteomics}

- **EN** — The measurement of many proteins at once within their spatial context in a tissue, typically via multiplexed antibody imaging.
- **中文** — 在组织的空间背景下同时测量多种蛋白质,通常通过多重抗体成像实现。
- **DE** — Räumliche Proteomik: Die gleichzeitige Messung vieler Proteine im räumlichen Gewebekontext, meist über multiplexierte Antikörper-Bildgebung.
- _Seen in:_ [`virtual-tissue-2501`](../papers/virtual-tissue-2501/index.md)

#### Stereo-seq · Stereo-seq {#stereo-seq}

- **EN** — A high-resolution spatial-transcriptomics platform using nanoball-patterned arrays that can resolve gene expression down to subcellular scale over large tissue areas.
- **中文** — 一种基于纳米球阵列的高分辨率空间转录组平台,可在大面积组织上将基因表达分辨到亚细胞尺度。
- **DE** — Stereo-seq: Eine hochauflösende Spatial-Transcriptomics-Plattform mit Nanoball-Arrays, die Genexpression über große Gewebeflächen bis in den subzellulären Bereich auflöst.
- _Seen in:_ [`spatial-natcommun-2024`](../papers/spatial-natcommun-2024/index.md)

### Histopathology

#### Cellularity · 细胞密度 {#cellularity}

- **EN** — The proportion of a tissue, such as bone marrow, that is occupied by cells rather than fat or stroma.
- **中文** — 组织(如骨髓)中被细胞而非脂肪或间质所占据的比例。
- **DE** — Zellularität: Der Anteil eines Gewebes, etwa des Knochenmarks, der von Zellen statt von Fett oder Stroma eingenommen wird.
- _Seen in:_ [`pathomics-blood-2023`](../papers/pathomics-blood-2023/index.md)

#### Computational pathology · 计算病理学 {#computational-pathology}

- **EN** — The use of machine learning and image analysis to extract diagnostic and prognostic information from digitized pathology slides.
- **中文** — 运用机器学习与图像分析,从数字化病理切片中提取诊断与预后信息的领域。
- **DE** — Computationale Pathologie: Der Einsatz von maschinellem Lernen und Bildanalyse, um diagnostische und prognostische Informationen aus digitalisierten Pathologieschnitten zu gewinnen.
- _Seen in:_ [`histo-sciencedirect-2026`](../papers/histo-sciencedirect-2026/index.md), [`uni2-h-model`](../papers/uni2-h-model/index.md), [`virchow-2024`](../papers/virchow-2024/index.md)

#### FFPE tissue · 福尔马林固定石蜡包埋组织 {#ffpe}

- **EN** — Formalin-fixed, paraffin-embedded tissue, a standard preservation method that lets specimens be stored long-term and cut into thin sections.
- **中文** — 福尔马林固定、石蜡包埋的组织,是一种标准保存方法,便于样本长期保存并切成薄片。
- **DE** — FFPE-Gewebe: Formalin-fixiertes, in Paraffin eingebettetes Gewebe, eine Standardkonservierung, die eine langfristige Lagerung und das Schneiden dünner Schnitte ermöglicht.
- _Seen in:_ [`fm-arxiv-2604`](../papers/fm-arxiv-2604/index.md), [`hest1k-2024`](../papers/hest1k-2024/index.md)

#### H&E staining · 苏木精-伊红染色 {#h-e-staining}

- **EN** — A routine tissue stain that colors cell nuclei blue-purple (hematoxylin) and cytoplasm pink (eosin), forming the standard visual basis for histological diagnosis.
- **中文** — 一种常规组织染色法,用苏木精把细胞核染成蓝紫色、伊红把细胞质染成粉红色,是组织学诊断的标准视觉基础。
- **DE** — Hämatoxylin-Eosin-Färbung: Eine Routine-Gewebefärbung, die Zellkerne blau-violett (Hämatoxylin) und Zytoplasma rosa (Eosin) darstellt und die visuelle Standardgrundlage der histologischen Diagnostik bildet.
- _Seen in:_ [`fm-arxiv-2604`](../papers/fm-arxiv-2604/index.md), [`hest1k-2024`](../papers/hest1k-2024/index.md), [`histo-miccai-2025`](../papers/histo-miccai-2025/index.md), [`histo-nejmai-2024`](../papers/histo-nejmai-2024/index.md), [`histo-sciencedirect-2026`](../papers/histo-sciencedirect-2026/index.md), [`virchow-2024`](../papers/virchow-2024/index.md)

#### Histopathology · 组织病理学 {#histopathology}

- **EN** — The microscopic examination of tissue sections to diagnose and characterize disease.
- **中文** — 通过显微镜检查组织切片来诊断和刻画疾病的学科。
- **DE** — Histopathologie: Die mikroskopische Untersuchung von Gewebeschnitten zur Diagnose und Charakterisierung von Krankheiten.
- _Seen in:_ [`histo-anomaly-bi-repo`](../papers/histo-anomaly-bi-repo/index.md), [`histo-miccai-2025`](../papers/histo-miccai-2025/index.md), [`histo-nejmai-2024`](../papers/histo-nejmai-2024/index.md), [`histo-sciencedirect-2026`](../papers/histo-sciencedirect-2026/index.md), [`virchow-2024`](../papers/virchow-2024/index.md)

#### Immunohistochemistry (IHC) · 免疫组织化学 {#immunohistochemistry}

- **EN** — A staining technique that uses antibodies to reveal the location of specific proteins in a tissue section.
- **中文** — 一种利用抗体显示组织切片中特定蛋白位置的染色技术。
- **DE** — Immunhistochemie: Eine Färbetechnik, die mithilfe von Antikörpern die Lokalisation bestimmter Proteine in einem Gewebeschnitt sichtbar macht.
- _Seen in:_ [`fm-arxiv-2604`](../papers/fm-arxiv-2604/index.md), [`uni2-h-model`](../papers/uni2-h-model/index.md)

#### Microsatellite instability (MSI) · 微卫星不稳定性 {#microsatellite-instability}

- **EN** — A hypermutable tumor state caused by defective DNA mismatch repair, widely used as a diagnostic and immunotherapy biomarker.
- **中文** — 由 DNA 错配修复缺陷导致的高突变肿瘤状态,广泛用作诊断与免疫治疗的生物标志物。
- **DE** — Mikrosatelliteninstabilität: Ein hypermutabler Tumorzustand infolge defekter DNA-Mismatch-Reparatur, weit verbreitet als diagnostischer und immuntherapeutischer Biomarker.
- _Seen in:_ [`histo-sciencedirect-2026`](../papers/histo-sciencedirect-2026/index.md)

#### Nuclear morphometry · 细胞核形态测量 {#nucleomorphometry}

- **EN** — Quantitative measurement of the shape, size, texture and color of segmented cell nuclei to characterize tissue.
- **中文** — 对分割出的细胞核在形状、大小、纹理和颜色上进行定量测量,以刻画组织特征。
- **DE** — Kernmorphometrie: Die quantitative Messung von Form, Größe, Textur und Farbe segmentierter Zellkerne zur Charakterisierung von Gewebe.
- _Seen in:_ [`hest1k-2024`](../papers/hest1k-2024/index.md), [`pathomics-blood-2023`](../papers/pathomics-blood-2023/index.md)

#### Pan-cancer detection · 泛癌检测 {#pan-cancer-detection}

- **EN** — Detecting the presence of cancer across many tumor types with a single model instead of one model per cancer type.
- **中文** — 用单一模型跨多种肿瘤类型检测癌症,而非为每种癌种单独训练模型。
- **DE** — Pan-Krebs-Detektion: Der Nachweis von Krebs über viele Tumortypen hinweg mit einem einzigen Modell statt eines Modells pro Krebsart.
- _Seen in:_ [`virchow-2024`](../papers/virchow-2024/index.md)

#### Pathomics · 病理组学 {#pathomics}

- **EN** — The extraction of large numbers of quantitative features from pathology images for statistical and predictive analysis.
- **中文** — 从病理图像中提取大量定量特征,用于统计与预测分析。
- **DE** — Pathomics: Die Extraktion einer großen Zahl quantitativer Merkmale aus Pathologiebildern für statistische und prädiktive Analysen.
- _Seen in:_ [`pathomics-blood-2023`](../papers/pathomics-blood-2023/index.md), [`pathomics-repo`](../papers/pathomics-repo/index.md)

#### Tile / patch · 图块 / 小块 {#tile-patch}

- **EN** — A small fixed-size sub-image (e.g. 224x224 pixels) cropped from a whole-slide image so that models can process the huge slide piece by piece.
- **中文** — 从全切片图像中裁出的固定尺寸小图(如 224×224 像素),使模型能够逐块处理巨大的切片。
- **DE** — Kachel / Patch: Ein kleines, festgroßes Teilbild (z. B. 224x224 Pixel), das aus einem Whole-Slide-Image herausgeschnitten wird, damit Modelle den riesigen Schnitt stückweise verarbeiten können.
- _Seen in:_ [`fm-arxiv-2604`](../papers/fm-arxiv-2604/index.md), [`hest1k-2024`](../papers/hest1k-2024/index.md), [`histo-miccai-2025`](../papers/histo-miccai-2025/index.md), [`histo-nejmai-2024`](../papers/histo-nejmai-2024/index.md), [`pathomics-repo`](../papers/pathomics-repo/index.md), [`uni2-h-model`](../papers/uni2-h-model/index.md), [`virchow-2024`](../papers/virchow-2024/index.md)

#### Tissue segmentation · 组织分割 {#tissue-segmentation}

- **EN** — Partitioning a pathology image into regions labeled by tissue type or separating tissue from background.
- **中文** — 将病理图像划分为按组织类型标注的区域,或把组织与背景分开。
- **DE** — Gewebesegmentierung: Die Aufteilung eines Pathologiebildes in nach Gewebetyp beschriftete Regionen oder die Trennung von Gewebe und Hintergrund.
- _Seen in:_ [`hest1k-2024`](../papers/hest1k-2024/index.md), [`histo-sciencedirect-2026`](../papers/histo-sciencedirect-2026/index.md), [`pathomics-blood-2023`](../papers/pathomics-blood-2023/index.md)

#### Virtual staining · 虚拟染色 {#virtual-staining}

- **EN** — Computationally generating one stain modality (e.g. IHC) from another (e.g. H&E) without physically re-staining the tissue.
- **中文** — 在不对组织进行物理再染色的情况下,用计算方法从一种染色(如 H&E)生成另一种染色(如 IHC)。
- **DE** — Virtuelle Färbung: Die rechnergestützte Erzeugung einer Färbemodalität (z. B. IHC) aus einer anderen (z. B. H&E), ohne das Gewebe physisch neu zu färben.
- _Seen in:_ [`fm-arxiv-2604`](../papers/fm-arxiv-2604/index.md)

### Oncology & clinical

#### Concordance index (C-index) · 一致性指数(C-index) {#concordance-index}

- **EN** — A metric for survival models that measures how often the model correctly ranks which of two patients experiences the event sooner.
- **中文** — 用于生存模型的指标,衡量模型正确判断两名患者中谁更早发生事件的比例。
- **DE** — Konkordanzindex (C-Index): Eine Kennzahl für Überlebensmodelle, die misst, wie oft das Modell korrekt einordnet, welcher von zwei Patienten das Ereignis früher erlebt.
- _Seen in:_ [`histo-sciencedirect-2026`](../papers/histo-sciencedirect-2026/index.md), [`pathomics-npjpo-2026`](../papers/pathomics-npjpo-2026/index.md), [`pathomics-repo`](../papers/pathomics-repo/index.md), [`virtual-tissue-2501`](../papers/virtual-tissue-2501/index.md)

#### Immune checkpoint blockade (ICB) · 免疫检查点阻断(ICB) {#immune-checkpoint-blockade}

- **EN** — A cancer immunotherapy that blocks inhibitory receptors such as PD-1 or PD-L1 to release the brakes on anti-tumor T cells.
- **中文** — 一种癌症免疫治疗,通过阻断 PD-1 或 PD-L1 等抑制性受体来解除抗肿瘤 T 细胞的抑制。
- **DE** — Immun-Checkpoint-Blockade (ICB): Eine Krebs-Immuntherapie, die hemmende Rezeptoren wie PD-1 oder PD-L1 blockiert, um die Bremsen der Antitumor-T-Zellen zu lösen.
- _Seen in:_ [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md), [`virtual-tissue-2501`](../papers/virtual-tissue-2501/index.md)

#### Overall survival (OS) · 总生存期(OS) {#overall-survival}

- **EN** — The length of time from diagnosis or treatment start until death from any cause, a primary endpoint in cancer studies.
- **中文** — 从确诊或开始治疗到因任何原因死亡的时间长度,是癌症研究的主要终点。
- **DE** — Gesamtüberleben (OS): Die Zeitspanne von Diagnose oder Therapiebeginn bis zum Tod jeglicher Ursache, ein primärer Endpunkt in Krebsstudien.
- _Seen in:_ [`pathomics-npjpo-2026`](../papers/pathomics-npjpo-2026/index.md)

#### Pathological complete response (pCR) · 病理完全缓解(pCR) {#pathological-complete-response}

- **EN** — The absence of any residual invasive tumor in tissue examined after neoadjuvant therapy, a favorable predictor of long-term outcome.
- **中文** — 新辅助治疗后所检组织中不存在任何残留浸润性肿瘤,是长期预后良好的指标。
- **DE** — Pathologische Komplettremission (pCR): Das Fehlen jeglichen residualen invasiven Tumors im nach neoadjuvanter Therapie untersuchten Gewebe, ein günstiger Prädiktor für den Langzeitverlauf.
- _Seen in:_ [`virtual-tissue-2501`](../papers/virtual-tissue-2501/index.md)

#### Pathomics signature · 病理组学签名 {#pathomics-signature}

- **EN** — A prognostic index built from quantitative features that deep-learning models extract directly from digitized histopathology slides.
- **中文** — 由深度学习模型直接从数字病理切片中提取的定量特征构建的预后指标。
- **DE** — Pathomics-Signatur: Ein prognostischer Index aus quantitativen Merkmalen, die Deep-Learning-Modelle direkt aus digitalisierten Histopathologie-Schnitten extrahieren.
- _Seen in:_ [`pathomics-npjpo-2026`](../papers/pathomics-npjpo-2026/index.md)

#### T-cell exhaustion · T 细胞耗竭 {#t-cell-exhaustion}

- **EN** — A dysfunctional state in which chronically stimulated T cells lose their killing capacity and up-regulate inhibitory checkpoint markers.
- **中文** — 一种功能失调状态:长期受刺激的 T 细胞丧失杀伤能力并上调抑制性检查点标志物。
- **DE** — T-Zell-Erschöpfung: Ein dysfunktionaler Zustand, in dem chronisch stimulierte T-Zellen ihre zytotoxische Kapazität verlieren und hemmende Checkpoint-Marker hochregulieren.
- _Seen in:_ [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md)

#### Tertiary lymphoid structure (TLS) · 三级淋巴结构(TLS) {#tertiary-lymphoid-structure}

- **EN** — An organized aggregate of immune cells that forms in chronically inflamed or tumor tissue and often associates with better anti-tumor immunity.
- **中文** — 在慢性炎症或肿瘤组织中形成的有序免疫细胞聚集体,常与更强的抗肿瘤免疫相关。
- **DE** — Tertiäre lymphoide Struktur (TLS): Ein organisiertes Aggregat von Immunzellen, das in chronisch entzündetem oder Tumorgewebe entsteht und oft mit besserer Antitumor-Immunität einhergeht.
- _Seen in:_ [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md)

#### Triple-negative breast cancer (TNBC) · 三阴性乳腺癌(TNBC) {#triple-negative-breast-cancer}

- **EN** — An aggressive breast-cancer subtype lacking estrogen, progesterone, and HER2 receptors, which limits targeted-therapy options.
- **中文** — 一种侵袭性乳腺癌亚型,缺乏雌激素、孕激素和 HER2 受体,限制了靶向治疗选择。
- **DE** — Triple-negatives Mammakarzinom (TNBC): Ein aggressiver Brustkrebs-Subtyp ohne Östrogen-, Progesteron- und HER2-Rezeptoren, was zielgerichtete Therapieoptionen einschränkt.
- _Seen in:_ [`virtual-tissue-2501`](../papers/virtual-tissue-2501/index.md)

#### Tumor microenvironment (TME) · 肿瘤微环境(TME) {#tumor-microenvironment}

- **EN** — The ecosystem of immune, stromal, and vascular cells surrounding a tumor that shapes its growth and its response to therapy.
- **中文** — 环绕肿瘤的免疫、基质与血管细胞所构成的生态系统,影响肿瘤生长及其对治疗的响应。
- **DE** — Tumormikromilieu (TME): Das Ökosystem aus Immun-, Stroma- und Gefäßzellen rund um einen Tumor, das dessen Wachstum und Therapieantwort prägt.
- _Seen in:_ [`histo-sciencedirect-2026`](../papers/histo-sciencedirect-2026/index.md), [`pathomics-blood-2023`](../papers/pathomics-blood-2023/index.md), [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md), [`virtual-tissue-2501`](../papers/virtual-tissue-2501/index.md)

#### Whole-slide image (WSI) · 全切片图像(WSI) {#whole-slide-image}

- **EN** — A high-resolution digital scan of an entire histopathology glass slide, often gigapixel-sized, used for computational pathology.
- **中文** — 对整张组织病理玻片进行的高分辨率数字扫描,常达十亿像素级,用于计算病理学。
- **DE** — Gesamtschnittbild (WSI): Ein hochauflösender digitaler Scan eines gesamten Histopathologie-Objektträgers, oft im Gigapixel-Bereich, für die computergestützte Pathologie.
- _Seen in:_ [`hest1k-2024`](../papers/hest1k-2024/index.md), [`histo-miccai-2025`](../papers/histo-miccai-2025/index.md), [`histo-nejmai-2024`](../papers/histo-nejmai-2024/index.md), [`histo-sciencedirect-2026`](../papers/histo-sciencedirect-2026/index.md), [`pathomics-blood-2023`](../papers/pathomics-blood-2023/index.md), [`pathomics-npjpo-2026`](../papers/pathomics-npjpo-2026/index.md), [`pathomics-repo`](../papers/pathomics-repo/index.md), [`uni2-h-model`](../papers/uni2-h-model/index.md), [`virchow-2024`](../papers/virchow-2024/index.md)

### Cardiology & imaging

#### Echocardiography · 超声心动图 {#echocardiography}

- **EN** — Ultrasound imaging of the heart, the clinical gold standard for measuring ejection fraction and the source of the training labels here.
- **中文** — 对心脏的超声成像,是测量射血分数的临床金标准,也是本文训练标签的来源。
- **DE** — Echokardiografie: Ultraschallbildgebung des Herzens, der klinische Goldstandard zur Messung der Ejektionsfraktion und die Quelle der hier verwendeten Trainingslabels.
- _Seen in:_ [`imaging-ehjdh-2026`](../papers/imaging-ehjdh-2026/index.md)

#### Electrocardiogram (ECG) · 心电图(ECG) {#electrocardiogram}

- **EN** — A recording of the heart's electrical activity over time as waveforms, used here as the raw input from which deep learning reads cardiac risk.
- **中文** — 记录心脏电活动随时间变化的波形图,本文用作深度学习读取心脏风险的原始输入。
- **DE** — Elektrokardiogramm (EKG): Eine Aufzeichnung der elektrischen Herzaktivität als Wellenform über die Zeit, hier der Roheingang, aus dem Deep Learning das kardiale Risiko abliest.
- _Seen in:_ [`imaging-nature-2026`](../papers/imaging-nature-2026/index.md)

#### Grad-CAM (gradient-weighted saliency) · Grad-CAM(梯度加权显著性) {#grad-cam}

- **EN** — An interpretability method that highlights the image regions most responsible for a model's prediction, here producing 3D saliency maps on CT.
- **中文** — 一种可解释性方法,标出对模型预测贡献最大的图像区域,本文用于生成 CT 的三维显著性图。
- **DE** — Grad-CAM (gradientengewichtete Salienz): Eine Interpretierbarkeitsmethode, die die für eine Modellvorhersage wichtigsten Bildregionen hervorhebt, hier zur Erzeugung von 3D-Salienzkarten auf CT.
- _Seen in:_ [`imaging-ehjdh-2026`](../papers/imaging-ehjdh-2026/index.md)

#### Heart failure with reduced ejection fraction (systolic dysfunction) · 射血分数降低的心力衰竭(收缩功能障碍) {#heart-failure-reduced-ef}

- **EN** — A condition where the heart's weakened contraction lowers ejection fraction; catching it early lets guideline therapy slow progression.
- **中文** — 心脏收缩减弱导致射血分数下降的病症;早期发现可让指南导向治疗延缓病程。
- **DE** — Herzinsuffizienz mit reduzierter Ejektionsfraktion (systolische Dysfunktion): Ein Zustand, bei dem die geschwächte Herzkontraktion die Ejektionsfraktion senkt; eine frühe Erkennung erlaubt es, mit leitliniengerechter Therapie das Fortschreiten zu verlangsamen.
- _Seen in:_ [`imaging-ehjdh-2026`](../papers/imaging-ehjdh-2026/index.md)

#### Implantable cardioverter-defibrillator (ICD) · 植入式心律转复除颤器(ICD) {#implantable-cardioverter-defibrillator}

- **EN** — An implanted device that detects dangerous arrhythmias and delivers a shock to prevent sudden cardiac death.
- **中文** — 植入体内的装置,可检测危险的心律失常并放电,以预防心脏性猝死。
- **DE** — Implantierbarer Kardioverter-Defibrillator (ICD): Ein implantiertes Gerät, das gefährliche Herzrhythmusstörungen erkennt und durch einen Schock den plötzlichen Herztod verhindert.
- _Seen in:_ [`imaging-nature-2026`](../papers/imaging-nature-2026/index.md)

#### Left ventricular ejection fraction (LVEF) · 左心室射血分数(LVEF) {#left-ventricular-ejection-fraction}

- **EN** — The percentage of blood pumped out of the left ventricle with each beat; a low value (e.g. <50%) signals reduced pumping function and heart failure.
- **中文** — 每次心跳时左心室泵出血液的百分比;数值偏低(如 <50%)提示泵血功能下降与心力衰竭。
- **DE** — Linksventrikuläre Ejektionsfraktion (LVEF): Der Prozentsatz des Blutes, das die linke Herzkammer pro Schlag auswirft; ein niedriger Wert (z. B. <50 %) zeigt eine verminderte Pumpfunktion und Herzinsuffizienz an.
- _Seen in:_ [`imaging-ehjdh-2026`](../papers/imaging-ehjdh-2026/index.md), [`imaging-nature-2026`](../papers/imaging-nature-2026/index.md)

#### Non-contrast chest CT · 非增强胸部 CT {#non-contrast-chest-ct}

- **EN** — A computed-tomography scan of the chest taken without injected contrast dye and without ECG gating, acquired routinely for many indications.
- **中文** — 不注射对比剂、也不做心电门控的胸部 CT 扫描,常规用于多种适应症。
- **DE** — Native Thorax-CT (ohne Kontrastmittel): Eine Computertomografie des Brustkorbs ohne injiziertes Kontrastmittel und ohne EKG-Triggerung, die routinemäßig für viele Fragestellungen erstellt wird.
- _Seen in:_ [`imaging-ehjdh-2026`](../papers/imaging-ehjdh-2026/index.md)

#### Opportunistic screening · 机会性筛查 {#opportunistic-screening}

- **EN** — Extracting an unrelated diagnosis from data collected for another purpose — e.g. detecting heart failure from a CT ordered for something else.
- **中文** — 从为其他目的采集的数据中顺带发现无关疾病——例如从为别的原因所拍的 CT 中检出心力衰竭。
- **DE** — Opportunistisches Screening: Das Gewinnen einer unabhängigen Diagnose aus Daten, die zu einem anderen Zweck erhoben wurden — z. B. das Erkennen einer Herzinsuffizienz aus einer für etwas anderes angeforderten CT.
- _Seen in:_ [`imaging-ehjdh-2026`](../papers/imaging-ehjdh-2026/index.md)

#### Sudden cardiac death (SCD) · 心脏性猝死(SCD) {#sudden-cardiac-death}

- **EN** — Unexpected death from a cardiac cause, usually a fatal arrhythmia, within a short time of symptom onset; the outcome the ECG biomarker aims to predict.
- **中文** — 由心脏原因(通常是致命性心律失常)在症状出现后短时间内发生的意外死亡,即该 ECG 生物标志物要预测的终点。
- **DE** — Plötzlicher Herztod (PHT): Ein unerwarteter Tod kardialer Ursache, meist durch eine tödliche Herzrhythmusstörung, kurz nach Symptombeginn; das vom EKG-Biomarker vorhergesagte Ereignis.
- _Seen in:_ [`imaging-nature-2026`](../papers/imaging-nature-2026/index.md)

#### Ventricular arrhythmia · 室性心律失常 {#ventricular-arrhythmia}

- **EN** — An abnormal, often life-threatening heart rhythm originating in the ventricles, the mechanistic cause of most sudden cardiac deaths.
- **中文** — 起源于心室的异常且常危及生命的心律,是大多数心脏性猝死的机制原因。
- **DE** — Ventrikuläre Arrhythmie: Ein abnormaler, oft lebensbedrohlicher Herzrhythmus, der in den Herzkammern entsteht und die mechanistische Ursache der meisten plötzlichen Herztode ist.
- _Seen in:_ [`imaging-nature-2026`](../papers/imaging-nature-2026/index.md)

### Foundation models

#### Class token (CLS token) · 分类标记 {#class-token}

- **EN** — A special learnable token in a transformer whose output vector serves as a summary embedding of the whole input.
- **中文** — Transformer 中一个特殊的可学习标记,其输出向量作为整个输入的汇总嵌入。
- **DE** — CLS-Token: Ein spezielles lernbares Token in einem Transformer, dessen Ausgabevektor als zusammenfassende Einbettung der gesamten Eingabe dient.
- _Seen in:_ [`fm-arxiv-2604`](../papers/fm-arxiv-2604/index.md), [`uni2-h-model`](../papers/uni2-h-model/index.md), [`virchow-2024`](../papers/virchow-2024/index.md)

#### DINOv2 · DINOv2 {#dinov2}

- **EN** — A self-supervised training recipe combining self-distillation and masked image modeling to learn strong image features without labels.
- **中文** — 一种结合自蒸馏与掩码图像建模的自监督训练配方,无需标签即可学到强大的图像特征。
- **DE** — DINOv2: Ein selbstüberwachtes Trainingsverfahren, das Selbstdistillation und maskierte Bildmodellierung kombiniert, um ohne Beschriftungen starke Bildmerkmale zu lernen.
- _Seen in:_ [`uni2-h-model`](../papers/uni2-h-model/index.md), [`virchow-2024`](../papers/virchow-2024/index.md)

#### Masked image modeling · 掩码图像建模 {#masked-image-modeling}

- **EN** — A self-supervised task in which the model learns by reconstructing deliberately hidden parts of an image.
- **中文** — 一种自监督任务,模型通过重建图像中被故意遮挡的部分来学习。
- **DE** — Maskierte Bildmodellierung: Eine selbstüberwachte Aufgabe, bei der das Modell lernt, indem es absichtlich verdeckte Bildteile rekonstruiert.
- _Seen in:_ [`uni2-h-model`](../papers/uni2-h-model/index.md)

#### Self-supervised learning · 自监督学习 {#self-supervised-learning}

- **EN** — Training on unlabeled data by having the model create its own supervisory signal from the data itself.
- **中文** — 在无标注数据上训练,让模型从数据本身构造出监督信号进行学习。
- **DE** — Selbstüberwachtes Lernen: Training auf unbeschrifteten Daten, bei dem das Modell sein Überwachungssignal aus den Daten selbst erzeugt.
- _Seen in:_ [`histo-nejmai-2024`](../papers/histo-nejmai-2024/index.md), [`uni2-h-model`](../papers/uni2-h-model/index.md), [`virchow-2024`](../papers/virchow-2024/index.md)

#### Tile embedding · 图块嵌入 {#tile-embedding}

- **EN** — A fixed-length feature vector produced by an encoder to numerically represent an image tile for downstream tasks.
- **中文** — 由编码器生成的定长特征向量,用于数值化表示图块,供下游任务使用。
- **DE** — Tile-Embedding: Ein Merkmalsvektor fester Länge, den ein Encoder erzeugt, um eine Bildkachel numerisch für nachgelagerte Aufgaben darzustellen.
- _Seen in:_ [`uni2-h-model`](../papers/uni2-h-model/index.md), [`virchow-2024`](../papers/virchow-2024/index.md)

#### Vision Transformer (ViT) · 视觉 Transformer {#vision-transformer}

- **EN** — A neural network that treats image patches as a sequence of tokens and processes them with the transformer self-attention architecture.
- **中文** — 一种把图像块当作 token 序列、用 Transformer 自注意力架构处理的神经网络。
- **DE** — Vision Transformer: Ein neuronales Netz, das Bildausschnitte als Token-Sequenz behandelt und sie mit der Self-Attention-Architektur des Transformers verarbeitet.
- _Seen in:_ [`fm-arxiv-2604`](../papers/fm-arxiv-2604/index.md), [`uni2-h-model`](../papers/uni2-h-model/index.md), [`virchow-2024`](../papers/virchow-2024/index.md)

#### Vision-language model (VLM) · 视觉-语言模型 {#vision-language-model}

- **EN** — A model trained on paired images and text so it can relate visual content to natural-language descriptions.
- **中文** — 在图像-文本配对上训练的模型,能够将视觉内容与自然语言描述关联起来。
- **DE** — Vision-Language-Modell: Ein auf gepaarten Bildern und Texten trainiertes Modell, das visuelle Inhalte mit natürlichsprachlichen Beschreibungen verknüpfen kann.
- _Seen in:_ [`fm-arxiv-2604`](../papers/fm-arxiv-2604/index.md), [`histo-miccai-2025`](../papers/histo-miccai-2025/index.md)

### ML methods

#### 3D vision transformer (CT-ViT) · 三维视觉 Transformer(CT-ViT) {#vision-transformer-3d}

- **EN** — A transformer neural network that processes volumetric images as sequences of 3D patches; CT-ViT is a chest-CT variant used as an imaging backbone.
- **中文** — 以三维图块序列处理体数据图像的 Transformer 神经网络;CT-ViT 是用作影像骨干的胸部 CT 变体。
- **DE** — 3D-Vision-Transformer (CT-ViT): Ein Transformer-Netzwerk, das volumetrische Bilder als Folgen von 3D-Patches verarbeitet; CT-ViT ist eine Thorax-CT-Variante, die als Bild-Backbone dient.
- _Seen in:_ [`imaging-ehjdh-2026`](../papers/imaging-ehjdh-2026/index.md)

#### Autoencoder · 自编码器 {#autoencoder}

- **EN** — A neural network that compresses data into a latent code and reconstructs it, used for dimensionality reduction and reconstruction-based anomaly scoring.
- **中文** — 把数据压缩为潜编码再重建的神经网络,用于降维和基于重建的异常打分。
- **DE** — Autoencoder: Ein neuronales Netz, das Daten in einen latenten Code komprimiert und rekonstruiert, genutzt zur Dimensionsreduktion und zur rekonstruktionsbasierten Anomaliebewertung.
- _Seen in:_ [`histo-miccai-2025`](../papers/histo-miccai-2025/index.md), [`scrna-natmachintell-2026`](../papers/scrna-natmachintell-2026/index.md)

#### Counterfactual · 反事实 {#counterfactual}

- **EN** — A synthesized 'what-if' version of an input — e.g. how a waveform or tissue would look if it were normal — used to make a model's decision interpretable.
- **中文** — 对输入合成的“如果……会怎样”版本——如某波形或组织若为正常时的样子——用于让模型决策可解释。
- **DE** — Kontrafaktisch: Eine synthetisierte 'Was-wäre-wenn'-Version einer Eingabe — z. B. wie eine Wellenform oder ein Gewebe aussähe, wenn es normal wäre — um die Modellentscheidung interpretierbar zu machen.
- _Seen in:_ [`imaging-nature-2026`](../papers/imaging-nature-2026/index.md)

#### Diffusion model · 扩散模型 {#diffusion-model}

- **EN** — A generative model that learns to reverse a gradual noising process to synthesize data; conditioning it on 'normal' priors enables reconstruction-based anomaly detection.
- **中文** — 通过学习逆转逐步加噪过程来合成数据的生成模型;以“正常”先验为条件即可做基于重建的异常检测。
- **DE** — Diffusionsmodell: Ein generatives Modell, das lernt, einen schrittweisen Verrauschungsprozess umzukehren, um Daten zu synthetisieren; bedingt auf 'normale' Priors ermöglicht es rekonstruktionsbasierte Anomalieerkennung.
- _Seen in:_ [`histo-miccai-2025`](../papers/histo-miccai-2025/index.md), [`imaging-nature-2026`](../papers/imaging-nature-2026/index.md)

#### Discriminative model · 判别模型 {#discriminative-model}

- **EN** — A model that predicts a label from an input (e.g. risk from an ECG); pairing it with a generative model turns its opaque decision into a visible biomarker.
- **中文** — 从输入预测标签的模型(如从 ECG 预测风险);与生成模型配对可把其不透明决策转为可见的生物标志物。
- **DE** — Diskriminatives Modell: Ein Modell, das aus einer Eingabe ein Label vorhersagt (z. B. Risiko aus einem EKG); die Kopplung mit einem generativen Modell macht seine undurchsichtige Entscheidung als Biomarker sichtbar.
- _Seen in:_ [`imaging-nature-2026`](../papers/imaging-nature-2026/index.md)

#### Evidence graph · 证据图 {#evidence-graph}

- **EN** — An incrementally built graph of the entities, relations and sources an agent has consulted, kept as memory so that every claim can be traced back to where it came from and checked by a human.
- **中文** — 把 agent 查阅过的实体、关系与出处增量构建成图并作为记忆保存,使每条论断都能回溯到来源、供人工核查。
- **DE** — Evidenzgraph: Ein inkrementell aufgebauter Graph der Entitäten, Relationen und Quellen, die ein Agent konsultiert hat, als Gedächtnis gespeichert, sodass jede Aussage zu ihrem Ursprung zurückverfolgt und von Menschen geprüft werden kann.
- _Seen in:_ [`deepevidence-natmachintell-2026`](../papers/deepevidence-natmachintell-2026/index.md)

#### Flow matching · 流匹配 {#flow-matching}

- **EN** — A technique for training continuous-time generative models by regressing a velocity field that transports one distribution into another.
- **中文** — 通过回归将一个分布输运到另一个分布的速度场,来训练连续时间生成模型的方法。
- **DE** — Flow Matching: Eine Technik zum Training zeitkontinuierlicher generativer Modelle, indem ein Geschwindigkeitsfeld regressiert wird, das eine Verteilung in eine andere überführt.
- _Seen in:_ [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md), [`virtual-cell-challenge`](../papers/virtual-cell-challenge/index.md)

#### Foundation model · 基础模型 {#foundation-model}

- **EN** — A large model pretrained on broad data and reused as a general-purpose backbone that is adapted to many downstream tasks.
- **中文** — 在大规模广泛数据上预训练、作为通用骨干复用并适配到众多下游任务的大模型。
- **DE** — Foundation Model: Ein großes, auf breiten Daten vortrainiertes Modell, das als universelles Backbone wiederverwendet und an viele nachgelagerte Aufgaben angepasst wird.
- _Seen in:_ [`fm-arxiv-2604`](../papers/fm-arxiv-2604/index.md), [`hest1k-2024`](../papers/hest1k-2024/index.md), [`histo-nejmai-2024`](../papers/histo-nejmai-2024/index.md), [`imaging-ehjdh-2026`](../papers/imaging-ehjdh-2026/index.md), [`scrna-natmachintell-2026`](../papers/scrna-natmachintell-2026/index.md), [`uni2-h-model`](../papers/uni2-h-model/index.md), [`virchow-2024`](../papers/virchow-2024/index.md), [`virtual-cell-challenge`](../papers/virtual-cell-challenge/index.md), [`virtual-tissue-2501`](../papers/virtual-tissue-2501/index.md)

#### Generative adversarial network (GAN) · 生成对抗网络(GAN) {#generative-adversarial-network}

- **EN** — A generative model where a generator and a discriminator are trained against each other; the discriminator's signal can also enforce constraints on learned representations.
- **中文** — 一种生成模型,生成器与判别器相互对抗训练;判别器信号也可用于对所学表征施加约束。
- **DE** — Generative Adversarial Network (GAN): Ein generatives Modell, bei dem Generator und Diskriminator gegeneinander trainiert werden; das Diskriminator-Signal kann auch Beschränkungen für gelernte Repräsentationen erzwingen.
- _Seen in:_ [`imaging-nature-2026`](../papers/imaging-nature-2026/index.md), [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md)

#### Generative model · 生成模型 {#generative-model}

- **EN** — A model that learns a data distribution well enough to synthesize new samples, enabling visualization, reconstruction, or in-silico perturbation.
- **中文** — 充分学习数据分布以合成新样本的模型,可用于可视化、重建或计算机模拟扰动。
- **DE** — Generatives Modell: Ein Modell, das eine Datenverteilung gut genug lernt, um neue Proben zu synthetisieren, und so Visualisierung, Rekonstruktion oder In-silico-Perturbation ermöglicht.
- _Seen in:_ [`histo-miccai-2025`](../papers/histo-miccai-2025/index.md), [`imaging-nature-2026`](../papers/imaging-nature-2026/index.md), [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md)

#### Hallucination · 幻觉 {#hallucination}

- **EN** — A model output stated with confidence but unsupported by its sources; in evidence-citing systems it must be measured alongside accuracy, together with what the model silently omitted.
- **中文** — 模型自信给出、却无来源支撑的输出;在会引用证据的系统里,它必须与准确率并列度量,并连同「模型悄悄漏掉了什么」一起评估。
- **DE** — Halluzination: Eine selbstbewusst formulierte Modellausgabe ohne Beleg in den Quellen; in evidenzzitierenden Systemen muss sie neben der Genauigkeit gemessen werden — zusammen mit dem, was das Modell stillschweigend ausgelassen hat.
- _Seen in:_ [`biomednlp-natcommun-2025`](../papers/biomednlp-natcommun-2025/index.md), [`deepevidence-natmachintell-2026`](../papers/deepevidence-natmachintell-2026/index.md)

#### In-silico perturbation · 计算机模拟扰动 {#in-silico-perturbation}

- **EN** — Simulating an intervention — deleting/replacing a cell type or applying a drug — inside a model to predict the resulting change and screen for revert targets.
- **中文** — 在模型内部模拟干预(删除/替换某类细胞或施加药物),以预测由此产生的变化并筛选逆转靶点。
- **DE** — In-silico-Perturbation: Das Simulieren eines Eingriffs — Löschen/Ersetzen eines Zelltyps oder Anwenden eines Medikaments — innerhalb eines Modells, um die resultierende Veränderung vorherzusagen und Revert-Ziele zu screenen.
- _Seen in:_ [`scrna-natmachintell-2026`](../papers/scrna-natmachintell-2026/index.md), [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md), [`virtual-cell-challenge`](../papers/virtual-cell-challenge/index.md)

#### Linear probing · 线性探针 {#linear-probe}

- **EN** — Freezing a pretrained encoder and training only a linear classifier on its features — the standard way to benchmark representation quality itself, and the honest baseline any fancier method must beat.
- **中文** — 冻结预训练编码器、只在其特征上训练一个线性分类器——评测表示质量本身的标准做法,也是任何更复杂方法都必须先超越的诚实基线。
- **DE** — Linear Probing: Einen vortrainierten Encoder einfrieren und nur einen linearen Klassifikator auf seinen Merkmalen trainieren — der Standardweg, Repräsentationsqualität selbst zu bewerten, und die ehrliche Baseline, die jede aufwendigere Methode zuerst schlagen muss.
- _Seen in:_ [`pathbench-natcommun-2026`](../papers/pathbench-natcommun-2026/index.md), [`virtual-tissue-2501`](../papers/virtual-tissue-2501/index.md)

#### Maximum mean discrepancy (MMD) · 最大均值差异(MMD) {#maximum-mean-discrepancy}

- **EN** — A kernel-based statistic measuring how different two distributions are by comparing their means in a feature space; a metric for perturbation-prediction accuracy.
- **中文** — 基于核的统计量,通过在特征空间比较均值来度量两个分布的差异;用作扰动预测准确度的指标。
- **DE** — Maximum Mean Discrepancy (MMD): Eine kernbasierte Statistik, die den Unterschied zweier Verteilungen durch Vergleich ihrer Mittelwerte in einem Merkmalsraum misst; ein Maß für die Genauigkeit der Perturbationsvorhersage.
- _Seen in:_ [`scrna-natmachintell-2026`](../papers/scrna-natmachintell-2026/index.md)

#### Monge gap · Monge 间隙 {#monge-gap}

- **EN** — A regularizer that pushes a learned map toward the optimal-transport (Monge) solution without needing a special convex architecture; conditioning it yields the Conditional Monge Gap.
- **中文** — 一种正则项,将所学映射推向最优传输(Monge)解而无需特殊凸结构;对其条件化即得 Conditional Monge Gap。
- **DE** — Monge-Gap: Ein Regularisierer, der eine gelernte Abbildung ohne spezielle konvexe Architektur zur optimalen (Monge-)Transportlösung hin drängt; seine Bedingung ergibt den Conditional Monge Gap.
- _Seen in:_ [`scrna-natmachintell-2026`](../papers/scrna-natmachintell-2026/index.md)

#### Neural ODE · 神经常微分方程 {#neural-ode}

- **EN** — A model that parameterizes the derivative of a hidden state with a neural network, integrating it as an ordinary differential equation to transform data continuously.
- **中文** — 用神经网络参数化隐状态导数,将其作为常微分方程积分以连续地变换数据的模型。
- **DE** — Neuronale ODE: Ein Modell, das die Ableitung eines verborgenen Zustands durch ein neuronales Netz parametrisiert und sie als gewöhnliche Differentialgleichung integriert, um Daten kontinuierlich zu transformieren.
- _Seen in:_ [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md)

#### Optimal transport (OT) · 最优传输(OT) {#optimal-transport}

- **EN** — A mathematical framework for the least-cost way to morph one probability distribution into another, used to map control cells to perturbed cells.
- **中文** — 以最小代价把一个概率分布变形为另一个的数学框架,用于将对照细胞映射到扰动后细胞。
- **DE** — Optimaler Transport (OT): Ein mathematischer Rahmen für die kostengünstigste Art, eine Wahrscheinlichkeitsverteilung in eine andere zu überführen, genutzt, um Kontrollzellen auf perturbierte Zellen abzubilden.
- _Seen in:_ [`scrna-natmachintell-2026`](../papers/scrna-natmachintell-2026/index.md), [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md), [`virtual-tissue-2501`](../papers/virtual-tissue-2501/index.md)

#### Out-of-distribution (OOD) detection · 分布外(OOD)检测 {#out-of-distribution-detection}

- **EN** — Flagging inputs that fall outside the data distribution a model was trained on, such as an unseen drug, cell context, or diseased tissue.
- **中文** — 标记落在模型训练分布之外的输入,如未见过的药物、细胞语境或病变组织。
- **DE** — Out-of-Distribution-Erkennung (OOD): Das Kennzeichnen von Eingaben, die außerhalb der Trainingsverteilung eines Modells liegen, etwa ein unbekanntes Medikament, ein neuer Zellkontext oder krankhaftes Gewebe.
- _Seen in:_ [`histo-miccai-2025`](../papers/histo-miccai-2025/index.md), [`scrna-natmachintell-2026`](../papers/scrna-natmachintell-2026/index.md), [`virtual-cell-challenge`](../papers/virtual-cell-challenge/index.md)

#### Reconstruction error · 重建误差 {#reconstruction-error}

- **EN** — The discrepancy between an input and a generative model's attempt to reconstruct it as 'normal'; large error marks the input as anomalous.
- **中文** — 输入与生成模型将其重建为“正常”之间的差异;误差大则将该输入判为异常。
- **DE** — Rekonstruktionsfehler: Die Abweichung zwischen einer Eingabe und dem Versuch eines generativen Modells, sie als 'normal' zu rekonstruieren; ein großer Fehler kennzeichnet die Eingabe als anomal.
- _Seen in:_ [`histo-miccai-2025`](../papers/histo-miccai-2025/index.md)

#### Sinkhorn divergence · Sinkhorn 散度 {#sinkhorn-divergence}

- **EN** — An entropy-regularized, fast-to-compute approximation of optimal-transport distance between two distributions, used as a training and evaluation objective.
- **中文** — 对两个分布之间最优传输距离的熵正则化、计算高效的近似,用作训练与评测目标。
- **DE** — Sinkhorn-Divergenz: Eine entropieregularisierte, schnell berechenbare Näherung der optimalen Transportdistanz zwischen zwei Verteilungen, verwendet als Trainings- und Bewertungsziel.
- _Seen in:_ [`scrna-natmachintell-2026`](../papers/scrna-natmachintell-2026/index.md)

#### Variational autoencoder (VAE / iVAE) · 变分自编码器(VAE / iVAE) {#variational-autoencoder}

- **EN** — An autoencoder with a probabilistic latent space; the identifiable variant (iVAE) conditions on side information so latent factors can be uniquely recovered.
- **中文** — 具有概率潜空间的自编码器;可识别变体(iVAE)以辅助信息为条件,使潜在因子可被唯一还原。
- **DE** — Variationaler Autoencoder (VAE / iVAE): Ein Autoencoder mit probabilistischem latentem Raum; die identifizierbare Variante (iVAE) bedingt auf Zusatzinformation, sodass latente Faktoren eindeutig rekonstruierbar sind.
- _Seen in:_ [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md)

#### Wasserstein distance · Wasserstein 距离 {#wasserstein-distance}

- **EN** — The optimal-transport 'earth-mover' distance between distributions, usable as a similarity metric between perturbation effects or as a revert-distance measure.
- **中文** — 分布之间的最优传输“搬土”距离,可作为扰动效应间的相似度或“逆转距离”度量。
- **DE** — Wasserstein-Distanz: Die 'Earth-Mover'-Distanz des optimalen Transports zwischen Verteilungen, nutzbar als Ähnlichkeitsmaß zwischen Perturbationseffekten oder als Revert-Distanzmaß.
- _Seen in:_ [`scrna-natmachintell-2026`](../papers/scrna-natmachintell-2026/index.md), [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md)

### General

#### Concordance index (C-index) · 一致性指数(C-index) {#c-index}

- **EN** — A survival-analysis metric giving the probability that the model ranks a higher-risk patient as having an earlier event than a lower-risk one; 0.5 is chance.
- **中文** — 生存分析指标,表示模型把高风险患者判为比低风险患者更早发生事件的概率;0.5 为随机。
- **DE** — Konkordanzindex (C-Index): Eine Metrik der Überlebensanalyse, die die Wahrscheinlichkeit angibt, dass das Modell einen Hochrisikopatienten als früher erkrankt einstuft als einen Niedrigrisikopatienten; 0,5 ist Zufall.
- _Seen in:_ [`spatial-biorxiv-2025`](../papers/spatial-biorxiv-2025/index.md)

#### Contrastive learning · 对比学习 {#contrastive-learning}

- **EN** — A representation-learning approach that pulls together embeddings of related samples and pushes apart unrelated ones.
- **中文** — 一种表征学习方法,把相关样本的嵌入拉近、把无关样本的嵌入推远。
- **DE** — Kontrastives Lernen: Ein Ansatz des Repräsentationslernens, der Einbettungen verwandter Proben zusammenzieht und die unverwandter Proben auseinanderdrückt.
- _Seen in:_ [`hest1k-2024`](../papers/hest1k-2024/index.md)

#### External validation · 外部验证 {#external-validation}

- **EN** — Testing a trained model on data from an independent site, country, or cohort it never saw, to demonstrate that performance generalizes.
- **中文** — 在模型从未见过的独立机构、国家或队列数据上测试,以证明性能可泛化。
- **DE** — Externe Validierung: Das Testen eines trainierten Modells an Daten eines unabhängigen Standorts, Landes oder einer Kohorte, die es nie gesehen hat, um die Generalisierbarkeit der Leistung zu belegen.
- _Seen in:_ [`imaging-ehjdh-2026`](../papers/imaging-ehjdh-2026/index.md), [`imaging-nature-2026`](../papers/imaging-nature-2026/index.md)

#### F1 score · F1 分数 {#f1-score}

- **EN** — The harmonic mean of precision and recall, a single balanced accuracy metric for classification under class imbalance.
- **中文** — 精确率与召回率的调和平均,是类别不平衡下分类的单一平衡准确度指标。
- **DE** — F1-Score: Das harmonische Mittel aus Präzision und Recall, eine ausgewogene Einzelkennzahl für die Klassifikationsgüte bei Klassenungleichgewicht.
- _Seen in:_ [`imaging-ehjdh-2026`](../papers/imaging-ehjdh-2026/index.md)

#### Latent diffusion model (LDM) · 潜空间扩散模型 {#latent-diffusion-model}

- **EN** — A generative model that iteratively denoises data in a compressed latent space to synthesize realistic images efficiently.
- **中文** — 一种生成模型,在压缩的潜空间中迭代去噪,从而高效合成逼真图像。
- **DE** — Latentes Diffusionsmodell: Ein generatives Modell, das Daten iterativ in einem komprimierten latenten Raum entrauscht, um realistische Bilder effizient zu synthetisieren.
- _Seen in:_ [`fm-arxiv-2604`](../papers/fm-arxiv-2604/index.md), [`histo-miccai-2025`](../papers/histo-miccai-2025/index.md)

#### LoRA (Low-Rank Adaptation) · 低秩适配 {#lora}

- **EN** — A parameter-efficient fine-tuning method that adapts a large pretrained model by training only small low-rank weight updates.
- **中文** — 一种参数高效的微调方法,只训练小的低秩权重增量来适配大型预训练模型。
- **DE** — LoRA (Low-Rank Adaptation): Eine parameter-effiziente Feinabstimmungsmethode, die ein großes vortrainiertes Modell anpasst, indem nur kleine niedrigrangige Gewichtsaktualisierungen trainiert werden.
- _Seen in:_ [`histo-miccai-2025`](../papers/histo-miccai-2025/index.md)

#### Masked autoencoder (MAE) · 掩码自编码器(MAE) {#masked-autoencoder}

- **EN** — A self-supervised model trained to reconstruct deliberately hidden parts of its input, yielding representations useful for downstream tasks.
- **中文** — 一种自监督模型,通过重建被刻意遮蔽的输入部分进行训练,从而得到对下游任务有用的表征。
- **DE** — Maskierter Autoencoder (MAE): Ein selbstüberwachtes Modell, das darauf trainiert wird, absichtlich verdeckte Teile seiner Eingabe zu rekonstruieren, und so für nachgelagerte Aufgaben nützliche Repräsentationen liefert.
- _Seen in:_ [`virtual-tissue-2501`](../papers/virtual-tissue-2501/index.md)

#### Multiple-instance learning (MIL) · 多示例学习(MIL) {#multiple-instance-learning}

- **EN** — A weakly-supervised paradigm where a single label is attached to a whole bag of instances, letting a slide-level label train on many image patches.
- **中文** — 一种弱监督范式,将单一标签赋予整个示例袋,使切片级标签能在众多图像块上进行训练。
- **DE** — Multiple-Instance-Learning (MIL): Ein schwach überwachtes Paradigma, bei dem ein einzelnes Label einem ganzen Bündel von Instanzen zugeordnet wird, sodass ein Schnitt-Label über viele Bildausschnitte trainiert.
- _Seen in:_ [`histo-sciencedirect-2026`](../papers/histo-sciencedirect-2026/index.md), [`pathomics-npjpo-2026`](../papers/pathomics-npjpo-2026/index.md), [`uni2-h-model`](../papers/uni2-h-model/index.md)

#### Outlier exposure · 离群暴露 {#outlier-exposure}

- **EN** — Improving anomaly detection by training the model on auxiliary out-of-distribution data that stands in for unseen anomalies.
- **中文** — 通过用辅助的分布外数据(充当未见异常的代理)训练模型,来提升异常检测能力。
- **DE** — Outlier Exposure: Die Verbesserung der Anomalieerkennung, indem das Modell mit zusätzlichen Out-of-Distribution-Daten trainiert wird, die ungesehene Anomalien vertreten.
- _Seen in:_ [`histo-nejmai-2024`](../papers/histo-nejmai-2024/index.md)

#### Saliency attribution (Grad-CAM) · 显著性归因(Grad-CAM) {#saliency-attribution}

- **EN** — Post-hoc explanation methods, such as Grad-CAM, that highlight the image regions most responsible for a model's prediction.
- **中文** — 如 Grad-CAM 等事后解释方法,用于突出对模型预测贡献最大的图像区域。
- **DE** — Saliency-Attribution (Grad-CAM): Post-hoc-Erklärungsmethoden wie Grad-CAM, die die für eine Modellvorhersage maßgeblichen Bildregionen hervorheben.
- _Seen in:_ [`histo-sciencedirect-2026`](../papers/histo-sciencedirect-2026/index.md)


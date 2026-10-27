# 2 · Cells and RNA

> ⏱ About 30 min · Day 1 · Understand

!!! abstract "After this module you can answer"
    - Where are the nucleus, the cytoplasm and the RNA?
    - Why does counting RNA tell you what a cell is doing?
    - How do a cell type and a cell state differ, and which two obs columns hold them?

This module covers only the minimum biology the rest of onboarding needs.

## Step 1 · What a cell looks like

<div class="grid" markdown>

![Animal cell: membrane, cytoplasm, nucleus, mitochondria / 动物细胞：细胞膜、胞质、细胞核、线粒体](img/animal_cell.png)

- The **cell membrane** is the outer layer that separates the cell from its surroundings.
- The **nucleus** is the server room. It holds the **DNA**, the full source code. Almost every cell in one person carries the same DNA.
- The **cytoplasm** is the workshop where the actual work happens.
- **Mitochondria** sit in the cytoplasm and are the cell's power supply. They carry a small DNA of their own, encoding 2 rRNAs, 22 tRNAs and 13 proteins [3]; its genes are named with an `MT-` prefix, such as `MT-CO1` in module 1 ("mitochondrially encoded cytochrome c oxidase I") [4].

</div>

Figure: Wikimedia "[Simple diagram of animal cell (en).svg](https://commons.wikimedia.org/wiki/File:Simple_diagram_of_animal_cell_(en).svg)" by domdomegg, CC BY 4.0.

## Step 2 · What RNA is and where it sits

When a cell uses a gene, it first **copies that stretch of DNA into RNA** inside the nucleus (transcription), like printing a work order. A freshly printed order is still in the nucleus; it is then shipped to the cytoplasm, where the workshop uses it to build protein [1].

So a cell's RNA sits in two places: **a freshly made, mostly not-yet-spliced part in the nucleus, and a shipped part in the cytoplasm.** How big the nuclear part is depends on the cell: one study of mouse neurons put it at 20% to over 50% of all mRNA [2]. Module 5.1 uses this: measuring only the nucleus gets only the first part.

Mitochondrial genes are the exception: they are transcribed inside the mitochondria, not in the nucleus [3]. So a clean nucleus holds almost no `MT-` RNA (module 6).

![DNA in the nucleus is transcribed into mRNA, which leaves through nuclear pores to ribosomes in the cytoplasm / 核里的 DNA 被转录成 mRNA，经核孔送到胞质里的核糖体](img/transcription_export.png)

The lower part of the figure is the nucleus: the black double helix is **DNA**, the orange strands are freshly copied **mRNA** (the work orders). The layer with blue gaps is the nuclear envelope, and the **pores** are where orders leave. The upper part is the cytoplasm: green **ribosomes** read the mRNA and build protein (black chains); the brown folded membranes are the endoplasmic reticulum, continuous with the nuclear envelope. The other labels (tRNA, chaperone, vesicle…) are not needed here.

Figure: Wikimedia "[ProteinTranscription+Synthesis.svg](https://commons.wikimedia.org/wiki/File:ProteinTranscription%2BSynthesis.svg)" by Adjustit, CC BY-SA 4.0.

## Step 3 · Why counting RNA tells you what a cell does

Genes a cell uses a lot have many work orders. Counting each kind of RNA in a cell therefore tells you what the cell is doing; that count vector is one row of X from module 1.

Each kind of cell uses its own signature genes heavily; these are **marker genes**. A few common ones in the kidney:

| Marker gene | Cell type | Why |
|---|---|---|
| `NPHS1`, `NPHS2` | Podocyte (POD) | nephrin and podocin, parts of the filtration barrier [5] |
| `LRP2` | Proximal tubule (PT) | megalin, takes proteins back from the fluid [6] |
| `UMOD` | Thick ascending limb (TAL) | uromodulin, made mainly here [7] |
| `AQP2` | Collecting duct principal cell (PC) | water channel [8] |

!!! tip "Computer analogy"
    The same program (DNA) is installed on every machine, but each machine runs different processes. Counting RNA is like running `ps` on each machine and counting instances of each process. A marker gene is the process name that only one kind of machine runs.

## Step 4 · Cell type and cell state

- A **cell type** is a **lasting identity**: which job the cell does, for example a proximal tubule cell. It usually stays fixed, but injured cells can temporarily switch off their identity genes: Lake 2023's adaptive cells show "a marked downregulation of transporters critical to their normal function" [9]. In obs it is `subclass.l1` (16 broad classes) and the finer `subclass.l2` (74 subclasses) [10].
- A **cell state** is the **current condition**: the same cell type looks different when healthy, injured, repairing or dividing. In obs it is `state.l1` (reference / altered) and `state.l2` (which kind of change) [9][10].

The distribution of `state.l2` in Lake 2023's single-nucleus data (counted by us from the GEO label table) [10], with meanings as Lake 2023 defines them [9]:

| state.l2 | Meaning | Nuclei |
|---|---|---|
| reference | healthy reference state | 128,090 |
| degenerative | damaged or stressed | 42,316 |
| adaptive – epi | epithelial repair (aPT, aTAL) | 25,150 |
| adaptive – str | stromal wound-healing | 3,513 |
| cycling | dividing (cell-cycle genes on) | 839 |
| transitioning | between two cell types (here principal and intercalated cells) | 430 |
| NA | not assigned | 3,364 |

`subclass.l2` names combine the two: **dPT** = degenerative PT, **aTAL1 / aTAL2** = adaptive (repairing) TAL. 28 of the 74 subclasses are altered [10], matching the 28 altered states Lake 2023 defines [9].

!!! tip "Computer analogy"
    A cell type is a server's **role** (database, gateway, cache); a cell state is its current **runtime status** (healthy, overloaded, restarting, scaling up). Anomaly detection looks for a wrong status, not for "this one is a database".

## Step 5 · Where these labels come from

Nobody labels 200,000 cells one by one under a microscope. In practice:

1. cells are **clustered** by their expression profiles;
2. experts look at which **marker genes** are high in each cluster and decide its cell type and state;
3. that decision is given to every cell in the cluster [9][10].

So `subclass` and `state` are **expert interpretations of clusters**, not measurements. And the altered call itself uses quality metrics: Lake 2023 first flagged as possible altered states the clusters with "low genes detected, a high number of mitochondrial transcripts, a high number of endoplasmic-reticulum-associated transcripts, upregulation of injury markers… or enrichment in AKI or CKD samples" [9]. The labels are usually reliable, but cells on boundaries, and cells that look injured because of measurement problems, can be mislabelled. Our work is about exactly those boundaries (modules 6 and 8).

## Self-check

??? question "1. If you measure only the nucleus, which RNA do you lose?"
    The part already shipped to the cytoplasm; only the freshly made, mostly unspliced part in the nucleus remains (its share varies by cell). Mitochondrial RNA is not in the nucleus, so it is mostly missed too.

??? question "2. A cell has `subclass.l1` = PT and `state.l2` = degenerative. What is its `subclass.l2` most likely?"
    dPT (degenerative proximal tubule).

??? question "3. Why is the `state` label not ground truth?"
    Experts assigned it by reading clusters and marker genes; it was not measured, and the criteria include quality metrics such as few genes and many mitochondrial reads. Boundary cells and cells that look injured because of measurement problems can be mislabelled.

## References

1. OpenStax. *Biology 2e*, section 15.3 "Eukaryotic Transcription" (CC BY 4.0). [link](https://openstax.org/books/biology-2e/pages/15-3-eukaryotic-transcription) — "RNA polymerase II is located in the nucleus and synthesizes all protein-coding nuclear pre-mRNAs"; "the eukaryotic cell must be able to transport its mRNA to the cytoplasm".
2. Bakken TE, Hodge RD, Miller JA, et al. Single-nucleus and single-cell transcriptomes compared in matched cortical cell types. *PLoS One* 2018;13:e0209648. [doi:10.1371/journal.pone.0209648](https://doi.org/10.1371/journal.pone.0209648) — mouse neurons; abstract ("nuclear proportion of total cellular mRNA varies from 20% to over 50%"); Results (more than 50% intronic reads in nuclei).
3. D'Souza AR, Minczuk M. Mitochondrial transcription and translation: overview. *Essays Biochem* 2018;62:309–320. [doi:10.1042/EBC20170102](https://doi.org/10.1042/EBC20170102) — Introduction ("encodes 2 rRNAs, 22 tRNAs and mRNAs for 13 polypeptides"); "Transcription initiation" ("Transcription in human mitochondria is driven by… POLRMT").
4. HGNC. MT-CO1 (HGNC:7419). [link](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7419) — name "mitochondrially encoded cytochrome c oxidase I", location "mitochondria".
5. NCBI Gene 4868 (NPHS1) and 7827 (NPHS2). [NPHS1](https://www.ncbi.nlm.nih.gov/gene/4868), [NPHS2](https://www.ncbi.nlm.nih.gov/gene/7827) — RefSeq summaries (nephrin "found at the slit diaphragm of glomerular podocytes… functions in the glomerular filtration barrier"; podocin "regulation of glomerular permeability").
6. De S, Kuwahara S, Saito A. The endocytic receptor megalin and its associated proteins in proximal tubule epithelial cells. *Membranes* 2014;4:333–355. [doi:10.3390/membranes4030333](https://doi.org/10.3390/membranes4030333) — abstract.
7. Mount DB. Thick ascending limb of the loop of Henle. *Clin J Am Soc Nephrol* 2014;9:1974–1986. [doi:10.2215/CJN.04480413](https://doi.org/10.2215/CJN.04480413) — section "Uromodulin". A second review puts 10–15% of uromodulin in the early distal convoluted tubule: Karagiannidis AG, et al. *Nephrol Dial Transplant* 2024;39:1073–1087, [doi:10.1093/ndt/gfae008](https://doi.org/10.1093/ndt/gfae008), Introduction.
8. Pearce D, Soundararajan R, Trimpert C, et al. Collecting duct principal cell transport processes and their regulation. *Clin J Am Soc Nephrol* 2015;10:135–146. [doi:10.2215/CJN.05760513](https://doi.org/10.2215/CJN.05760513) — Introduction ("the aquaporin 2 (AQP2) water channel").
9. Lake BB, Menon R, Winfree S, et al. An atlas of healthy and injured cell states and niches in the human kidney. *Nature* 2023;619:585–594. [doi:10.1038/s41586-023-05769-3](https://doi.org/10.1038/s41586-023-05769-3) — abstract (28 altered states); Results ("cycling, transitioning, adaptive… and degenerative (damaged or stressed)"; aStr = "myofibroblasts (MyoF), cycling MyoF… and… adaptive fibroblasts"; aEpi "downregulation of transporters"); Methods "Clustering snCv3" (altered-state criteria). Deep-read: [Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md).
10. GEO GSE183277: `GSE183277_Kidney_Healthy-Injury_Cell_Atlas_snCv3_Metadata_03282022.txt.gz` and the field-description file ([GEO files](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE183nnn/GSE183277/suppl/)) — `subclass.l1` (16 values + 3,364 NA), `subclass.l2` (74 + NA), `state.l2` counts; labels described as "for clusters". Counted by us.

## Terms in this module

| English | 中文 | In one sentence |
|---|---|---|
| [Nucleus (cell nucleus)](glossary.md#cell-nucleus) | 细胞核 | The compartment inside a cell that holds the DNA; RNA of nuclear genes is made here before it moves out to the cytoplasm (mitochondrial genes are transcribed inside the mitochondria). |
| [Transcription (gene expression)](glossary.md#transcription) | 转录（基因表达） | Copying a gene's DNA into RNA; counting a gene's RNA molecules in a cell measures how active (expressed) the gene is. |
| [Gene-expression signature](glossary.md#gene-expression-signature) | 基因表达签名 | A defined set of genes whose coordinated expression levels mark a particular cell state, disease, or treatment response. |
| [Cell type](glossary.md#cell-type) | 细胞类型 | A stable class of cells with the same job and a characteristic expression profile (e.g. proximal tubule cell); found by clustering cells and checking marker genes. |
| [Cell state](glossary.md#cell-state) | 细胞状态 | The transient functional condition of a cell — such as activated, exhausted, or proliferating — layered on top of its stable cell-type identity. |

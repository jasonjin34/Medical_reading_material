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
- **Mitochondria** sit in the cytoplasm and are the cell's power supply. They carry a small DNA of their own, whose genes are named with an `MT-` prefix, such as `MT-CO1` in module 1.

</div>

Figure: Wikimedia "Simple diagram of animal cell (en)" by domdomegg, CC BY 4.0.

## Step 2 · What RNA is and where it sits

When a cell uses a gene, it first **copies that stretch of DNA into RNA** inside the nucleus (transcription), like printing a work order. A freshly printed order is still in the nucleus; it is then shipped to the cytoplasm, where the workshop uses it to build protein.

So a cell's RNA sits in two places: **a small, freshly made part in the nucleus and a larger, shipped part in the cytoplasm.** Module 5.1 uses this: measuring only the nucleus gets only the first part.

![DNA in the nucleus is transcribed into mRNA, which leaves through nuclear pores to ribosomes in the cytoplasm / 核里的 DNA 被转录成 mRNA，经核孔送到胞质里的核糖体](img/transcription_export.png)

The lower part of the figure is the nucleus: the black double helix is **DNA**, the orange strands are freshly copied **mRNA** (the work orders). The layer with blue gaps is the nuclear envelope, and the **pores** are where orders leave. The upper part is the cytoplasm: green **ribosomes** read the mRNA and build protein (black chains). The other labels (tRNA, chaperone, vesicle…) are not needed here.

Figure: Wikimedia "ProteinTranscription+Synthesis" by Adjustit, CC BY-SA 4.0.

## Step 3 · Why counting RNA tells you what a cell does

Genes a cell uses a lot have many work orders. Counting each kind of RNA in a cell therefore tells you what the cell is doing; that count vector is one row of X from module 1.

Each kind of cell uses its own signature genes heavily; these are **marker genes**. A few common ones in the kidney:

| Marker gene | Cell type | Why |
|---|---|---|
| `NPHS1`, `NPHS2` | Podocyte (POD) | build the filter |
| `LRP2` | Proximal tubule (PT) | takes proteins back from the fluid |
| `UMOD` | Thick ascending limb (TAL) | made almost only here |
| `AQP2` | Collecting duct principal cell (PC) | water channel |

!!! tip "Computer analogy"
    The same program (DNA) is installed on every machine, but each machine runs different processes. Counting RNA is like running `ps` on each machine and counting instances of each process. A marker gene is the process name that only one kind of machine runs.

## Step 4 · Cell type and cell state

- A **cell type** is a **lasting identity**: which job the cell does, for example a proximal tubule cell. It hardly changes. In obs it is `subclass.l1` (17 broad classes) and the finer `subclass.l2` (75 subclasses).
- A **cell state** is the **current condition**: the same cell type looks different when healthy, injured, repairing or dividing. In obs it is `state.l1` (reference / altered) and `state.l2` (which kind of change).

The distribution of `state.l2` in Lake 2023's single-nucleus data (counted by us from the GEO label table):

| state.l2 | Meaning | Nuclei |
|---|---|---|
| reference | healthy reference state | 128,090 |
| degenerative | losing normal function | 42,316 |
| adaptive – epi | epithelial repair (aPT, aTAL) | 25,150 |
| adaptive – str | stromal repair (fibroblast-like) | 3,513 |
| cycling | dividing to replace lost cells | 839 |
| transitioning | between two cell types | 430 |
| NA | not assigned | 3,364 |

`subclass.l2` names combine the two: **dPT** = degenerative PT, **aTAL** = adaptive (repairing) TAL. 28 of the 75 subclasses are altered.

!!! tip "Computer analogy"
    A cell type is a server's **role** (database, gateway, cache); a cell state is its current **runtime status** (healthy, overloaded, restarting, scaling up). Anomaly detection looks for a wrong status, not for "this one is a database".

## Step 5 · Where these labels come from

Nobody labels 200,000 cells one by one under a microscope. In practice:

1. cells are **clustered** by their expression profiles;
2. experts look at which **marker genes** are high in each cluster and decide its cell type and state;
3. that decision is given to every cell in the cluster.

So `subclass` and `state` are **expert interpretations of clusters**, not measurements. They are usually reliable, but cells on boundaries, and cells that look injured because of measurement problems, can be mislabelled. Our work is about exactly those boundaries (modules 6 and 8).

## Self-check

??? question "1. If you measure only the nucleus, which RNA do you lose?"
    The large part already shipped to the cytoplasm; only the small, freshly made part in the nucleus remains.

??? question "2. A cell has `subclass.l1` = PT and `state.l2` = degenerative. What is its `subclass.l2` most likely?"
    dPT (degenerative proximal tubule).

??? question "3. Why is the `state` label not ground truth?"
    Experts assigned it by reading clusters and marker genes; it was not measured. Boundary cells and cells that look injured because of measurement problems can be mislabelled.

## Terms in this module

| English | 中文 | In one sentence |
|---|---|---|
| [Nucleus (cell nucleus)](glossary.md#cell-nucleus) | 细胞核 | The compartment inside a cell that holds the DNA; RNA is made here before it moves out to the cytoplasm. |
| [Transcription (gene expression)](glossary.md#transcription) | 转录（基因表达） | Copying a gene's DNA into RNA; counting a gene's RNA molecules in a cell measures how active (expressed) the gene is. |
| [Gene-expression signature](glossary.md#gene-expression-signature) | 基因表达签名 | A defined set of genes whose coordinated expression levels mark a particular cell state, disease, or treatment response. |
| [Cell type](glossary.md#cell-type) | 细胞类型 | A stable class of cells with the same job and a characteristic expression profile (e.g. proximal tubule cell); found by clustering cells and checking marker genes. |
| [Cell state](glossary.md#cell-state) | 细胞状态 | The transient functional condition of a cell — such as activated, exhausted, or proliferating — layered on top of its stable cell-type identity. |

# 1 · Two tables: X and obs

> ⏱ About 30 min · Day 1 · Understand

!!! abstract "After this module you can answer"
    - Which two tables does single-cell data end up as?
    - What do a row, a column and a number in the matrix mean?
    - Which field is the label and which is the group ID, and why can't you split train and test at random?

We start at the end. All the biology and lab work in the next modules ends up in these two tables. Knowing the destination first tells you, for every later concept, what it becomes in the data.

The figure below draws the two tables side by side: X on the left, obs on the right, and **the same row is the same cell**. Take it in as a whole first; the steps below go through each table.

<figure class="xobs" markdown="0"><div class="xo-scroll"><table aria-label="Count matrix X aligned row by row with label table obs">
<thead><tr class="xo-cap"><th></th><th colspan="8"><span class="xo-tag">X</span>count matrix <span class="xo-sub">· cells × genes</span></th><th></th><th colspan="5"><span class="xo-tag">obs</span>label table <span class="xo-sub">· one row per cell</span></th></tr>
<tr class="xo-genes"><th></th><th>LRP2<i style="background:var(--xo-pt)"></i></th><th>CUBN<i style="background:var(--xo-pt)"></i></th><th>UMOD<i style="background:var(--xo-tal)"></i></th><th>SLC12A1<i style="background:var(--xo-tal)"></i></th><th>NPHS2<i style="background:var(--xo-pod)"></i></th><th>FOS<i style="background:var(--xo-stress)"></i></th><th>MT-CO1<i style="background:var(--xo-mito)"></i></th><th></th><th></th><th class="xo-o">patient</th><th class="xo-o xo-n">nCount</th><th class="xo-o xo-n">nFeature</th><th class="xo-o">subclass</th><th class="xo-o">state</th></tr></thead>
<tbody>
<tr tabindex="0"><td class="xo-bc">L1_AAACCCAAGC…</td><td class="xo-x"><b style="--c:var(--xo-pt);--a:61%">12</b></td><td class="xo-x"><b style="--c:var(--xo-pt);--a:46%">5</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-mito);--a:30%">1</b></td><td class="xo-more">…</td><td class="xo-seam"><div></div></td><td class="xo-o">P1</td><td class="xo-o xo-n">18</td><td class="xo-o xo-n">3</td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-pt)">PT</span></td><td class="xo-o"><span class="xo-pill">reference</span></td></tr>
<tr tabindex="0"><td class="xo-bc">L1_AAACGAATCA…</td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-tal);--a:80%">25</b></td><td class="xo-x"><b style="--c:var(--xo-tal);--a:51%">7</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-more">…</td><td class="xo-seam"><div></div></td><td class="xo-o">P1</td><td class="xo-o xo-n">32</td><td class="xo-o xo-n">2</td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-tal)">TAL</span></td><td class="xo-o"><span class="xo-pill">reference</span></td></tr>
<tr tabindex="0"><td class="xo-bc">L2_AAAGGATGTC…</td><td class="xo-x"><b style="--c:var(--xo-pt);--a:53%">8</b></td><td class="xo-x"><b style="--c:var(--xo-pt);--a:36%">2</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-stress);--a:55%">9</b></td><td class="xo-x"><b style="--c:var(--xo-mito);--a:39%">3</b></td><td class="xo-more">…</td><td class="xo-seam"><div></div></td><td class="xo-o">P2</td><td class="xo-o xo-n">22</td><td class="xo-o xo-n">4</td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-pt)">PT</span></td><td class="xo-o"><span class="xo-pill xo-alt">altered</span></td></tr>
<tr tabindex="0"><td class="xo-bc">L2_AACAACCTCG…</td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-pod);--a:48%">6</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-more">…</td><td class="xo-seam"><div></div></td><td class="xo-o">P2</td><td class="xo-o xo-n">6</td><td class="xo-o xo-n">1</td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-pod)">POD</span></td><td class="xo-o"><span class="xo-pill">reference</span></td></tr>
<tr tabindex="0"><td class="xo-bc">L3_AACCTGAAGT…</td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-tal);--a:43%">4</b></td><td class="xo-x"><b style="--c:var(--xo-tal);--a:30%">1</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-stress);--a:48%">6</b></td><td class="xo-x"><b style="--c:var(--xo-mito);--a:36%">2</b></td><td class="xo-more">…</td><td class="xo-seam"><div></div></td><td class="xo-o">P3</td><td class="xo-o xo-n">13</td><td class="xo-o xo-n">4</td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-tal)">TAL</span></td><td class="xo-o"><span class="xo-pill xo-alt">altered</span></td></tr>
<tr tabindex="0"><td class="xo-bc">L3_AACGTCAGTA…</td><td class="xo-x"><b style="--c:var(--xo-pt);--a:66%">15</b></td><td class="xo-x"><b style="--c:var(--xo-pt);--a:48%">6</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-more">…</td><td class="xo-seam"><div></div></td><td class="xo-o">P3</td><td class="xo-o xo-n">21</td><td class="xo-o xo-n">2</td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-pt)">PT</span></td><td class="xo-o"><span class="xo-pill">reference</span></td></tr>
</tbody>
<tfoot><tr class="xo-under"><td></td><td colspan="8"><div>features · tens of thousands of columns, mostly 0</div></td><td></td><td><div>group ID</div></td><td colspan="2"><div>quality · computed from the X row</div></td><td colspan="2"><div>labels · assigned by experts</div></td></tr></tfoot></table></div>
<p class="xo-hint">Click the figure to enlarge; click again or press Esc to close</p>
<ul class="xo-key"><li><span class="xo-ic">row</span><span>one cell (nucleus). The barcode on the left is its ID: a 16-letter DNA sequence copied onto the cDNA of every captured mRNA of this nucleus during the experiment (module 5.1); the prefix L1, L2 is the library (one sample's 10x reaction), so barcodes from different libraries do not collide</span></li><li><span class="xo-ic">column</span><span>one gene; the bar under its name shows which cell type it marks: teal PT, blue TAL, purple podocyte, orange stress, grey mitochondrial</span></li><li><span class="xo-ic">number</span><span>RNA molecules counted; darker means more, a grey dot is 0</span></li></ul>
<figcaption>Numbers, barcodes and patient IDs are illustrative, and only 7 genes are drawn; hover over a row to highlight it on both sides. nCount is the sum of the row and nFeature the number of non-zero entries, so here both count only these 7 genes. The `MT-CO1` column is illustrative too: Lake's released matrices no longer contain mitochondrial genes (see step 2). Rows 3 and 1 are both PT, but row 3 has high FOS, a stress gene, and is labelled altered: that difference is the anomaly we want to detect.</figcaption></figure>

## Step 1 · The count matrix X

**X** is a large, sparse matrix:

- **one row = one cell** (or one nucleus; module 5.1 explains the difference);
- **one column = one gene**;
- **one number = how many RNA molecules of that gene were detected in that cell.**

The raw X holds integer counts. In downloadable files, X has often been processed already: in the CELLxGENE files, for example, `X` holds normalised decimals and the raw counts sit in `raw.X` [3]; Lake 2023's single-cell data had ambient RNA subtracted with SoupX [1]; 88% of `nCount_RNA` values in the GEO single-cell table are not integers (counted by us) [2] (module 6).

The numbers in the figure are made up for illustration. The real scale, from Lake 2023's single-nucleus data (counted by us from the GEO label table) [2]: **203,702 nuclei**; each nucleus has a median of **2,694 RNA molecules** spread over **1,638 genes**. With tens of thousands of genes (28,813 in the CELLxGENE single-nucleus file [3]), almost every entry in a row is 0, which is why X is stored as a sparse matrix.

!!! tip "Computer analogy"
    Think of X as a `scipy.sparse` matrix whose row index is the cell barcode (a 16-letter DNA string like `AAACCCAAGCCGATAG` [4]; module 5.1 explains where it comes from) and whose column index is the gene. Each row is that cell's feature vector, just with tens of thousands of dimensions, nearly all zero.

!!! info "Biology note: what are LRP2 and UMOD?"
    The column names are **gene names**. Two examples:

    - [`LRP2`](https://www.ncbi.nlm.nih.gov/gene/4036): encodes megalin, a receptor that takes proteins from the filtered fluid back into the cell [6]; it sits on the apical membrane of **proximal tubule** (PT) cells [7].
    - [`UMOD`](https://www.ncbi.nlm.nih.gov/gene/7369): encodes uromodulin, made mainly by the **thick ascending limb** (TAL) [8]. One review puts 85–90% in the TAL and 10–15% in the early distal convoluted tubule [9]; another says the distal convoluted tubule does not express it [8].

    To look up any other gene, search its name in [NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/).

## Step 2 · The label table obs

**obs** is a table aligned row-for-row with X: one row per cell, recording **where the cell came from, how good its measurement is, and what it is**. Below is the real first row of Lake 2023's single-nucleus label table on GEO (selected columns) [2]:

| Column | Value | Meaning |
|---|---|---|
| `library` | `KB1` | which 10x library (one sample's reaction) |
| `patient` | `31-10001` | which person |
| `condition.l2` | `DKD` | diabetic kidney disease |
| `nCount_RNA` | `5463` | RNA molecules (UMIs) in this nucleus |
| `nFeature_RNA` | `2996` | genes detected |
| `percent.mt` | `9.37` | % mitochondrial RNA |
| `subclass.l1` | `PT` | cell type: proximal tubule |
| `state.l1` | `altered` | reference (normal) vs altered |

The three quality columns are, in principle, computed from this row of X:

- **`nCount_RNA`** = the sum of the row: how many RNA molecules were detected in this nucleus. Here 5,463.
- **`nFeature_RNA`** = **how many entries in the row are not 0**: how many different genes were detected. Here 2,996: out of tens of thousands of genes, only about 3,000 have at least one molecule. With integer counts it is always ≤ `nCount_RNA`, since every non-zero entry contributes at least one molecule.
- **`percent.mt`** = the share of `nCount_RNA` that comes from mitochondrial genes (names starting with `MT-`), in percent.

In the published Lake files you cannot fully recompute them, though: the authors **removed the mitochondrial genes** from the single-nucleus data [1], and the CELLxGENE single-nucleus file contains no `MT-` gene at all [3], so `percent.mt` can only be read from the label table; summing this row of the CELLxGENE counts (`raw.X`) gives 5,424 molecules and 2,974 genes, slightly fewer than the label table [3].

Values that are too low or too high often mean the row is not one intact cell: an empty droplet, a broken cell, or two cells stuck together [5]. Module 6 shows how they are used for quality control.

The obs columns fall into four groups; later modules explain the biology behind each:

| Group | Columns | Explained in |
|---|---|---|
| IDs | `library` · `patient` · `specimen` | modules 4, 6 |
| Origin | `condition.l1/l2` · `tissue_type` · `region.l1/l2` · `sex` | modules 3, 4 |
| Quality | `nCount_RNA` · `nFeature_RNA` · `percent.mt` | modules 5.1, 6 |
| Answers | `subclass.l1/l2` · `state.l1/l2` | modules 2, 3 |

A third, small table, **var**, has one row per gene (names and other gene information). The three together form an **AnnData** object, saved as an `.h5ad` file [10].

!!! warning "Same data, different column names in different files"
    The column names above come from the label table on GEO [2]. The Lake 2023 files on CELLxGENE [3]:

    - the single-nucleus file has 172,847 nuclei (the GEO table has 203,702); person and library are called `donor_id` and `library_id`; it has `subclass.l1/l2` but **no `state.l1` / `state.l2`**;
    - the single-cell file has no state column either; the integrated file (single-nucleus + single-cell) has `state` and `state.l2`;
    - `X` holds normalised values and the raw counts are in `raw.X`; gene symbols are in `var["feature_name"]`, and the row index holds Ensembl IDs.

    So for the `state` labels, the simplest route is the GEO label table, or the integrated file.

```python
import pandas as pd
import scanpy as sc

# GEO label table (203,702 nuclei; has state.l1 / state.l2)
labels = pd.read_csv(
    "GSE183277_Kidney_Healthy-Injury_Cell_Atlas_snCv3_Metadata_03282022.txt.gz",
    sep="\t", index_col=0,
    dtype={"patient": str})   # patient IDs mix numbers and text; read as text or one person can split into two groups
labels["state.l1"].value_counts()

# CELLxGENE single-nucleus h5ad (172,847 nuclei; no state columns)
adata = sc.read_h5ad("<downloaded single-nucleus file>.h5ad")
adata.raw.X                  # raw counts, cells x genes (sparse)
adata.X                      # normalised values
adata.obs[["donor_id", "library_id", "subclass.l1"]]
adata.var["feature_name"]    # gene symbols; the index holds Ensembl IDs
```

## Step 3 · In machine-learning terms

- **Features**: a row of X.
- **Labels**: `subclass` (cell type) and `state` (reference / altered) in obs. The authors clustered the cells, reviewed marker genes by hand and gave each cluster its label [1][2]; **they are not measured ground truth** (modules 2 and 6 explain why that matters).
- **Group IDs**: `patient` and `library`. Cells from the same person or the same library share a lot: the person's genetic background, and the bias of one batch of reagents and handling.

!!! warning "The most common trap: splitting by cell at random"
    One person contributes thousands of cells (Lake's single-nucleus data has 36 people, a median of about 5,016 nuclei per person [2]). If cells are split at random, the same person ends up on both sides, and a model can score well by recognising the person or the batch, then fail on a new patient. **Split train and test by `patient`** (and by `library` where needed). It is the same reason recommender systems split by user to avoid leakage.

## Self-check

??? question "1. What are a row, a column and a number of X?"
    A row is a cell (or nucleus), a column is a gene, and a number is how many RNA molecules of that gene were detected in that cell (raw counts; in a downloaded file X may already be normalised).

??? question "2. How do `nCount_RNA` and `nFeature_RNA` differ?"
    `nCount_RNA` is the sum of the row (total RNA molecules detected); `nFeature_RNA` is the number of non-zero entries in the row (how many different genes were detected).

??? question "3. Why not split cells into train and test at random?"
    Cells from the same person and the same library are strongly correlated, so a random split puts people and batches seen in training into the test set and inflates the score. Split by `patient` (and by `library` where needed).

## References

1. Lake BB, Menon R, Winfree S, et al. An atlas of healthy and injured cell states and niches in the human kidney. *Nature* 2023;619:585–594. [doi:10.1038/s41586-023-05769-3](https://doi.org/10.1038/s41586-023-05769-3) — Methods, "Quality control of sequencing data" ("Mitochondrial transcripts (MT-*) were removed"; scCv3 "corrected using SoupX") and "Clustering snCv3" (cluster decision tree; "Annotations of clusters were based on known positive and negative cell type markers"). Deep-read: [Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md).
2. GEO GSE183277: `GSE183277_Kidney_Healthy-Injury_Cell_Atlas_snCv3_Metadata_03282022.txt.gz` and `…_Metadata_Field_Descriptions.txt.gz` ([GEO files](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE183nnn/GSE183277/suppl/)) — first row; medians; nuclei per patient; field descriptions ("Subclass annotations for clusters", "Injury (altered) or healthy (reference) state for clusters"). Also GSE183276 `GSE183276_Kidney_Healthy-Injury_Cell_Atlas_scCv3_Metadata_03282022.txt.gz` ([GEO files](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE183nnn/GSE183276/suppl/)): non-integer `nCount_RNA`. Counted by us.
3. CZ CELLxGENE, collection "An atlas of healthy and injured cell states and niches in the human kidney" ([link](https://cellxgene.cziscience.com/collections/bcb61471-2a44-4d00-a0af-ff085512674c)) — datasets "Single-nucleus RNA-seq of the Adult Human Kidney (Version 1.0)" (172,847 × 28,813), "Single-cell RNA-seq…" and "Integrated…"; obs and var column names, `X` vs `raw.X`, and row sums checked by us.
4. 10x Genomics. Technical Note CG000201 Rev A: Chromium Single Cell 3′ v3 reagent, workflow & software updates. [PDF](https://cdn.10xgenomics.com/image/upload/v1660261285/support-documents/CG000201_TechNote_Chromium_Single_Cell_3___v3_Reagent__Workflow___Software_Updates_RevA.pdf) — "16 nt 10x Barcode"; "barcoded, full-length cDNA from poly-adenylated mRNA".
5. Luecken MD, Theis FJ. Current best practices in single-cell RNA-seq analysis: a tutorial. *Mol Syst Biol* 2019;15:e8746. [doi:10.15252/msb.20188746](https://doi.org/10.15252/msb.20188746) — section "Quality control" (low counts / few genes / high mitochondrial fraction = broken cell; high counts = possible doublet).
6. NCBI Gene 4036 (LRP2). [link](https://www.ncbi.nlm.nih.gov/gene/4036) — RefSeq summary ("multi-ligand endocytic receptor… primarily in absorptive epithelial tissues such as the kidney"; ligands include albumin).
7. De S, Kuwahara S, Saito A. The endocytic receptor megalin and its associated proteins in proximal tubule epithelial cells. *Membranes* 2014;4:333–355. [doi:10.3390/membranes4030333](https://doi.org/10.3390/membranes4030333) — abstract ("expressed in the apical membrane of PTECs").
8. Mount DB. Thick ascending limb of the loop of Henle. *Clin J Am Soc Nephrol* 2014;9:1974–1986. [doi:10.2215/CJN.04480413](https://doi.org/10.2215/CJN.04480413) — section "Uromodulin" ("not expressed by macula densa cells or the downstream DCT").
9. Karagiannidis AG, Theodorakopoulou MP, Pella E, Sarafidis PA, Ortiz A. Uromodulin biology. *Nephrol Dial Transplant* 2024;39:1073–1087. [doi:10.1093/ndt/gfae008](https://doi.org/10.1093/ndt/gfae008) — Introduction ("TAL (85%–90%) and early distal convoluted tubule (DCT) (10%–15%)").
10. anndata documentation. [link](https://anndata.readthedocs.io/en/stable/) — AnnData object (`X`, `obs`, `var`, `raw`) and the `.h5ad` format.

## Terms in this module

| Term | In one sentence |
|---|---|
| [Count matrix](glossary.md#count-matrix) | The main single-cell data table: one row per cell (or nucleus), one column per gene, each entry the number of RNA molecules (UMIs) of that gene detected in that cell; very sparse. |
| [AnnData / h5ad](glossary.md#anndata-h5ad) | The Python (scanpy) container for single-cell data, saved as an .h5ad (HDF5) file: the count matrix X plus per-cell metadata (obs) and per-gene metadata (var). |
| [obs / var (cell and gene metadata)](glossary.md#obs-var) | The two tables aligned with the count matrix: obs has one row per cell (patient, library, quality numbers, cell-type and state labels), var has one row per gene (gene name and other gene information). |
| [Gene symbol (HGNC)](glossary.md#gene-symbol) | The short official name of a human gene set by the HGNC, such as LRP2 or UMOD; used as the column names of the count matrix. A prefix MT- marks genes encoded by mitochondrial DNA. |
| [Patient-level split (data leakage)](glossary.md#patient-level-split) | Putting all cells of one patient (and, where needed, one library) on the same side of the train / test split; splitting cells at random leaks the patient and batch into the test set and inflates the score. |

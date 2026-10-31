# 9 · Hands-on

> ⏱ About 3 h · Day 2 · Hands-on (optional)

!!! abstract "After this module you can answer"
    - How do you download and load Lake 2023's label table and h5ad?
    - How do you reproduce 'degenerative nuclei have fewer genes and more mitochondrial RNA'?
    - How do you run the simplest anomaly score, compute AUROC, and see why that is not enough?

This is day 2 and optional. Two parts:

- **Part A** (about 1 hour): download only the 19 MB label table and reproduce the numbers in modules 2 and 8. A laptop is enough.
- **Part B** (about 2 hours): also download the 1.6 GB count matrix, run a healthy-reference kNN anomaly score and reproduce module 8's results. Memory use depends on the machine: on one macOS computer we measured 3.6 GB maximum resident memory and a 9.7 GB peak memory footprint, so 16 GB is recommended (an 8 GB machine may swap). It runs in under a minute.

We ran the code below verbatim on 2026-10-27 (Python 3, scanpy 1.12.4, anndata 0.13.4, scikit-learn 1.9.1); the outputs shown are from that run. Download routes and known issues are on the [Lake 2023 dataset page](../datasets/lake-2023.md).

!!! warning "Keep data outside the repository"
    This repository is public. Put data in your own folder, such as `~/data/kidney/`, never inside the repository.

## Step 0 · Set up

```bash
mkdir -p ~/data/kidney/lake-2023 && cd ~/data/kidney/lake-2023
python -m venv venv && source venv/bin/activate
pip install scanpy scikit-learn
curl -O https://ftp.ncbi.nlm.nih.gov/geo/series/GSE183nnn/GSE183277/suppl/GSE183277_Kidney_Healthy-Injury_Cell_Atlas_snCv3_Metadata_03282022.txt.gz
```

## Part A · The label table only

### Step 1 · Load and count

The label table is module 1's obs: one row per nucleus, one column per field. The code reads it, counts the nuclei in each state, compares the three QC metrics across states, and finally computes the AUROC of two QC-only scorers.

```python
import pandas as pd
meta = pd.read_csv("GSE183277_Kidney_Healthy-Injury_Cell_Atlas_snCv3_Metadata_03282022.txt.gz",
                   sep="\t", index_col=0, low_memory=False, dtype={"patient": str})
print(meta.shape)                              # rows = nuclei, columns = obs fields
print(meta["state.l2"].value_counts(dropna=False))

qc = ["nFeature_RNA", "nCount_RNA", "percent.mt"]
print(meta.groupby("state.l2")[qc].median().round(2))

from sklearn.metrics import roc_auc_score
s = meta.dropna(subset=["state.l1"])
y = s["state.l1"] == "altered"                 # 1 = altered, 0 = reference
print("genes (fewer = more anomalous):", roc_auc_score(y, -s["nFeature_RNA"]))
print("percent.mt:", roc_auc_score(y, s["percent.mt"]))

d = s[s["state.l2"].isin(["degenerative", "reference"])]
yd = d["state.l2"] == "degenerative"
print("degenerative only, genes:", roc_auc_score(yd, -d["nFeature_RNA"]))
print("degenerative only, percent.mt:", roc_auc_score(yd, d["percent.mt"]))
```

### Step 2 · Read the output

- The table is **203,702 × 49**; the state counts match the table in module 2 (reference 128,090, degenerative 42,316…).
- Medians per state:

| state.l2 | nFeature_RNA | nCount_RNA | percent.mt |
|---|---|---|---|
| reference | 1,736 | 2,960 | 0.63 |
| degenerative | 791 | 990 | 2.95 |
| adaptive – epi | 2,426 | 4,612.5 | 0.49 |
| adaptive – str | 1,657 | 2,706 | 0.41 |
| cycling | 1,873 | 3,157 | 0.57 |
| transitioning | 3,420.5 | 7,400 | 1.00 |

- QC-only scorers:

| Score | All altered vs reference | Degenerative vs reference |
|---|---|---|
| fewer genes | 0.56 | 0.69 |
| higher `percent.mt` | 0.63 | 0.75 |

Degenerative nuclei have less than half the genes of reference nuclei, so QC alone scores well on them; adaptive nuclei have more genes, so mixing all altered states together drags the score down. As module 8 said: **report results per state**.

This is not a coincidence: Lake 2023 first flagged as possible altered states the clusters with "low genes detected, a high number of mitochondrial transcripts, a high number of endoplasmic-reticulum-associated transcripts, upregulation of injury markers… or enrichment in AKI or CKD samples" (Methods). Part of "few genes, high mito" was built into the labels themselves (modules 2 and 6).

!!! note "These numbers differ from Part B"
    Part A uses every cell type and every donor, with no train/test split; Part B looks only at proximal tubule (PT) and evaluates only on unseen donors. They answer different questions, so the numbers are not directly comparable.

## Part B · A healthy-reference kNN score

### Step 3 · Download the count matrix

The single-nucleus file on cellxgene, 1.57 GB: 172,847 nuclei × 28,813 genes. It has no `state` labels, so it is joined to the step 1 label table by cell ID (module 1).

```bash
curl -o lake2023_sn.h5ad https://datasets.cellxgene.cziscience.com/5dc03d39-ac5f-49e1-8630-a64d2e6e293b.h5ad
```

### Step 4 · Score

The method is the plainest possible one, matching the table in module 8, step 2:

1. look at one cell type only (PT), so "anomalous" means a state, not a cell type (module 2);
2. split the 13 healthy donors **by person** into three parts: half as the healthy reference, a quarter to set the threshold, a quarter held out for testing (module 1);
3. fit gene selection, scaling and PCA on the reference only, and project test data with the same transform, so nothing leaks;
4. anomaly score = mean distance to the 10 nearest healthy reference cells;
5. threshold = the 95th percentile of scores on the threshold donors, aiming at 5% false alarms.

```python
import numpy as np, pandas as pd, scanpy as sc
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import roc_auc_score

# 1. counts from cellxgene + state labels from GEO (module 1)
adata = sc.read_h5ad("lake2023_sn.h5ad")
adata.X = adata.raw.X
meta = pd.read_csv("GSE183277_Kidney_Healthy-Injury_Cell_Atlas_snCv3_Metadata_03282022.txt.gz",
                   sep="\t", index_col=0, low_memory=False, dtype={"patient": str})
adata.obs = adata.obs.join(meta[["state.l1", "state.l2", "condition.l1", "patient"]])

# 2. one cell type only, so "anomalous" means a state, not a type (module 2)
pt = adata[adata.obs["subclass.l1"] == "PT"].copy()
sc.pp.normalize_total(pt, target_sum=1e4)
sc.pp.log1p(pt)

# 3. split healthy DONORS, not cells: reference / calibration / test (module 1)
healthy = sorted(pt.obs.loc[pt.obs["condition.l1"] == "Ref", "patient"].unique())
rng = np.random.default_rng(0)
rng.shuffle(healthy)
n = len(healthy)
ref_donors, cal_donors, test_donors = healthy[: n // 2], healthy[n // 2 : 3 * n // 4], healthy[3 * n // 4 :]
reference = pt.obs["state.l1"] == "reference"
is_ref = pt.obs["patient"].isin(ref_donors) & reference
is_cal = pt.obs["patient"].isin(cal_donors) & reference
is_test = (pt.obs["patient"].isin(test_donors) | (pt.obs["condition.l1"] != "Ref")) & pt.obs["state.l1"].notna()

# 4. fit genes, scaling and PCA on the reference only
ref = pt[is_ref].copy()
sc.pp.highly_variable_genes(ref, n_top_genes=2000)
genes = ref.var_names[ref.var["highly_variable"]]
sc.pp.scale(ref, max_value=10)
sc.tl.pca(ref, n_comps=50)
mean, std = ref.var.loc[genes, "mean"].values, ref.var.loc[genes, "std"].values
pcs = ref.varm["PCs"][ref.var_names.get_indexer(genes)]

def embed(a):
    x = np.clip((a[:, genes].X.toarray() - mean) / std, -10, 10)
    return x @ pcs

# 5. anomaly score = mean distance to the 10 nearest healthy reference cells
nn = NearestNeighbors(n_neighbors=10).fit(ref.obsm["X_pca"])
def score(a):
    dist, _ = nn.kneighbors(embed(a))
    return dist.mean(axis=1)

threshold = np.quantile(score(pt[is_cal]), 0.95)   # target: 5% false alarms

# 6. evaluate on held-out donors
test = pt[is_test]
s = score(test)
obs = test.obs
y = (obs["state.l1"] == "altered").values
print("all altered   kNN", roc_auc_score(y, s), " genes", roc_auc_score(y, -obs["nFeature_RNA"]))
for state in ["degenerative", "adaptive - epi"]:
    m = obs["state.l2"].isin([state, "reference"]).values
    yy = (obs["state.l2"][m] == state).values
    print(state, " kNN", roc_auc_score(yy, s[m]), " genes", roc_auc_score(yy, -obs["nFeature_RNA"].values[m]))
healthy_test = (obs["patient"].isin(test_donors) & (obs["state.l1"] == "reference")).values
print("false alarms on held-out healthy donors:", (s[healthy_test] > threshold).mean())
```

### Step 5 · Read the output

With the `default_rng(0)` split, the test set has 28,380 PT nuclei, 20,477 of them altered. Changing `0` to 1–4 gives 4 more splits. Results:

| Held-out donors | Seed 0 | Seeds 0–4 |
|---|---|---|
| all altered, kNN | 0.67 | 0.67 – 0.76 |
| all altered, gene count | 0.56 | 0.56 – 0.61 |
| degenerative, kNN | 0.76 | 0.76 – 0.81 |
| degenerative, gene count | 0.76 | 0.76 – 0.85 |
| adaptive – epi, kNN | 0.56 | 0.53 – 0.71 |
| adaptive – epi, gene count | 0.30 | 0.30 – 0.34 |
| false alarms on healthy test donors (target 5%) | 0.9% | 0.9% – 6.3% |

Three readings, matching module 8's three difficulties:

1. **On degenerative cells, kNN is about as good as counting genes**, and worse in 4 of 5 splits. A good AUROC does not show the method learned disease.
2. **We do not know how many kNN-flagged cells are artifacts**: Lake has no artifact labels, so this code cannot answer that. [the artifact-injection topic](../research/anomaly-benchmark.md) does exactly this: inject known artifacts into the data, then test on real answers; exercise 6 in step 6 is a minimal version.
3. **False alarms are unstable**: set at 5%, they land between 0.9% and 6.3% on unseen healthy donors. The 13 healthy donors split 6 / 3 / 4, so there are only 4 test donors, and some have very few PT nuclei (one has 4 in seed 0, one has 3 in seeds 1–4), so per-person rates swing widely.

## Step 6 · Exercises

None of these has a fixed answer; run them before drawing conclusions.

1. Replace the by-person split (part 3 of the step 4 code) with a **random split by cell** and compute the false-alarm rate again. How does it differ from the by-person split, and why?
2. Replace `"PT"` with `"TAL"`. Do the conclusions still hold?
3. Replace "gene count" with `percent.mt`, or combine the two. Can it match kNN on degenerative cells?
4. Change `n_neighbors` from 10 to 1 or 50. How do AUROC and the false-alarm rate change?
5. Also join `tissue_type` from the label table (module 4): after the `join` in part 1 of the step 4 code, add `adata.obs = adata.obs.join(meta[["tissue_type"]], rsuffix="_geo")` (the h5ad has its own `tissue_type` column, but every value is "tissue"), then report the false-alarm rate separately for biopsy, nephrectomy and deceased donor using `tissue_type_geo`. We ran this line; the other results do not change.
6. **Make your own doublets** (a minimal version of the artifact-injection topic): before `normalize_total` in part 2 of the step 4 code, take 500 random pairs of reference PT nuclei from the test donors, **add the two rows' raw counts**, append them as 500 new cells and label them "artifact" (this is how Scrublet simulates doublets). Score them with the same pipeline: how many exceed the threshold? Then add PT + TAL pairs instead. What changes? Think about why doublets of two cells of the same type are hard to detect.

## Step 7 · Clean up

When done you can delete the h5ad (1.6 GB) and download it again with step 3 when needed.

## Self-check

??? question "1. Why are gene selection, scaling and PCA fitted on the reference only?"
    Fitting on test data means peeking at the test set, which makes results look better than they are. It is the same as fitting a scaler on the training set only in machine learning.

??? question "2. Why set the threshold on separate donors instead of on the reference itself?"
    Reference cells are the kNN's "training set" and sit naturally close to their own neighbours. A threshold set on them is too low, so false alarms rise on new people.

??? question "3. The gene-count AUROC on adaptive – epi is 0.30, below 0.5. What does that say?"
    Adaptive cells have more genes than reference cells, so "fewer genes = more anomalous" points the wrong way for them. Flipping the score gives about 0.70, but that too is only learning a QC metric.

# Omics AI Handbook

A **living, standardized literature base** for one research direction:

> **Anomaly-detection-based virtual tissue modelling** — detect regions of
> biomedical images & spatial-omics that changed due to disease or drug
> perturbation, model them as *virtual tissues*, then predict the key genes to
> **revert** the anomaly (experimental validation done by a wet-lab team).

Every item gets a bilingual (EN / 中文) close-reading, an AI-ready text extract, a
BibTeX entry, and a place in the relationship graph — all browsable as a
searchable website with an **English ⇄ 中文 language switcher**.

**🌐 Live site:** https://jasonjin34.github.io/Medical_reading_material/

## What's inside

| Path | What it is |
|---|---|
| `papers/<slug>/deep-read.md` | Bilingual close-reading (论文精读) |
| `papers/<slug>/ai-ready.md` | Clean text extract to paste into an LLM |
| `papers/<slug>/metadata.yaml` | Canonical record (doi, venue, tags, relevance…) |
| `papers/<slug>/citation.bib` | Per-paper BibTeX fragment |
| `references.bib` | The whole citation library, auto-built |
| `onboarding/` | Onboarding for newcomers (1–2 days, CS-friendly): modules + `modules.yaml`; the glossary is shown here |
| `datasets/datasets.yaml` | Facts about every dataset we use; the site's Datasets tab is generated from it |
| `research/` | The group's research topics (`topics.yaml` + one bilingual page each) |
| `glossary/*.yaml` | Trilingual glossary terms (EN / 中文 / DE), the single source for the glossary |
| `literature-review.md` | Synthesis across all papers (综述) |
| `relationships/` | Relationship graph (`graph.json`, `graph.mmd`, `relationships.md`) |
| `maps/` | Knowledge-map sources: `matrix.yaml` (method × data matrix), `views.yaml` (views, columns, concepts, pipelines), `labels.yaml`, `viewer.html`, `matrix.html` |
| `_maps/` | Obsidian hub notes, MOCs and canvases (auto-generated — do not hand-edit) |
| `docs/` + `mkdocs.yml` | The GitHub Pages site (auto-generated — do not hand-edit) |
| `templates/`, `scripts/` | The standardized pipeline (below) |

## Knowledge map

**Method map (start here).** A matrix with anomaly-detection paradigms as rows
(reconstruction, memory bank / kNN, density, OOD, conformal, healthy-reference,
cross-modal, artifacts) and data domains as columns (general → medical imaging →
histopathology → single-cell → spatial → kidney).
- Arrows show where a method was carried over.
- Dashed cells are the gaps Plan A fills.
- Source: `maps/matrix.yaml`.

**Reading-list views.** Per-plan graphs of papers and core concepts, plus a pipeline flowchart for each plan.
They are generated from `maps/views.yaml` and each paper's `plans` / `track` /
`recommended_by` fields.

- **Web:** the site's [Knowledge map](https://jasonjin34.github.io/Medical_reading_material/knowledge-map/)
  page. Views: Plan A, Plan B, Bridge (papers in both), Sikander's picks, EHR and Overview.
  - Groups start collapsed. Click one to open it.
  - Click a node to see its neighbours; double-click a paper to open its deep-read.
  - Filters: must-read, year and type.
- **Obsidian:** open the repo root as a vault.
  - `_maps/README.md` lists every view. Each view has a MOC, a column canvas and,
    for the plans, a `— flow.canvas`.
  - Hub notes embed the deep-reads, so the original files stay unchanged.
  - Graph view: filter `path:_maps`, colour groups `tag:#plan/A`, `tag:#plan/B`, `tag:#concept`.
  - `_maps/` is overwritten on every build, so keep your own notes outside it.

---

## Adding new literature

This is the entire workflow for adding a paper, dataset, model, repo, or
competition. Run it from the repo root.

**1. Install tooling (once):**

```bash
pip install -r requirements.txt
```

**2. Add the item** — one command fetches metadata + BibTeX and scaffolds the folder:

```bash
python scripts/add_paper.py <url|doi|arxiv> --category <c> --relevance <high|medium|low> [--access <open|paywall>]
```

- `<url|doi|arxiv>` — a landing URL, a bare DOI (`10.1038/…`), or an arXiv id (`2406.16192`).
- `--category` ∈ `anomaly · single-cell · spatial · virtual-tissue · histopath · foundation · pathology · imaging · competition · agents · ehr · other`.
- Knowledge-map placement: `--plans A|B|EHR`, `--track <A1…B7>`, `--recommended-by core-reading`; add a short label to `maps/labels.yaml`.
- Creates `papers/<slug>/` with `metadata.yaml`, `deep-read.md`, `ai-ready.md`, `citation.bib`.

**3. Write the close-reading** — edit `papers/<slug>/deep-read.md`. Keep every
section **bilingual** using inline markers (this is what powers the site's
language switcher):

```markdown
## 方法 / Method
<!-- ZH --> 中文说明……
<!-- EN --> English explanation…
```

Use `<!-- ZH/EN -->` for a line that should appear unchanged in both languages
(code, links, dataset names).

**4. Rebuild the derived artifacts** (idempotent — always safe to re-run):

```bash
python scripts/build_bib.py            # references.bib
python scripts/build_relationships.py  # relationship graph
python scripts/build_maps.py           # knowledge maps: docs/maps/ + _maps/ (Obsidian)
python scripts/build_site.py           # docs/ (en + zh) + mkdocs.yml
```

**5. Preview, then commit & push:**

```bash
mkdocs serve            # optional: http://127.0.0.1:8000
mkdocs build --strict   # must pass (CI runs this too)
git add -A && git commit -m "add <slug>: <title>" && git push
```

Pushing to `main` triggers `.github/workflows/pages.yml`, which rebuilds and
redeploys the site. Agent-facing rules are in **[CLAUDE.md](CLAUDE.md)**.

**Figures and result tables (optional per paper).** Add a `## 图表 / Figures & tables`
section near the end of `deep-read.md`. Download figures **only from open sources**
(arXiv/bioRxiv/PMC/CC-BY/GitHub/HF) into `papers/<slug>/figures/` with a `Source:` line;
for paywalled papers link the figures instead. Reproduce result tables as markdown with
faithful numbers only. Keep figures ≤ ~1600px (`sips -Z 1600 papers/<slug>/figures/*`).

**Conventions.**
- **slug** = short kebab of title/topic + year (e.g. `virchow-2024`); **bibkey** comes from
  the fetched BibTeX. Keep both stable once cited.
- **relevance `high`** ⇔ the ★ items the PI flagged; they surface first everywhere.
- One item = one folder. Datasets, models, repos and competitions are valid items
  (`type: dataset|model|code|competition`) with a lighter "resource card" read.
- Full-text PDFs go to `papers/<slug>/source.pdf` (git-ignored, local only).

---

## Notes

- **Generated files** (`references.bib`, `relationships/relationships.md`,
  `docs/**`, `mkdocs.yml`) are rebuilt by the scripts — edit the *sources*
  (`citation.bib`, `relationships/_narrative.md`, `metadata.yaml`, `templates/`,
  `literature-review.md`) and re-run, don't hand-edit the outputs.
- **Paywalled papers** are noted from the abstract + public content and marked
  `status: abstract-only`; drop a `source.pdf` into the paper folder later to enrich.
- **First-time Pages setup:** repo **Settings → Pages → Source: GitHub Actions** (once).

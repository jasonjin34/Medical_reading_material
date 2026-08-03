# Medical Reading Material

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
| `literature-review.md` | Synthesis across all papers (综述) |
| `relationships/` | Relationship graph (`graph.json`, `graph.mmd`, `relationships.md`) |
| `docs/` + `mkdocs.yml` | The GitHub Pages site (auto-generated — do not hand-edit) |
| `templates/`, `scripts/` | The standardized pipeline (below) |

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
- `--category` ∈ `single-cell · spatial · virtual-tissue · histopath · foundation · pathology · imaging · competition · other`.
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
python scripts/build_site.py           # docs/ (en + zh) + mkdocs.yml
```

**5. Preview, then commit & push:**

```bash
mkdocs serve            # optional: http://127.0.0.1:8000
mkdocs build --strict   # must pass (CI runs this too)
git add -A && git commit -m "add <slug>: <title>" && git push
```

Pushing to `main` triggers `.github/workflows/pages.yml`, which rebuilds and
redeploys the site. Full conventions are in **[CONTRIBUTING.md](CONTRIBUTING.md)**;
agent-facing rules are in **[CLAUDE.md](CLAUDE.md)**.

---

## Notes

- **Generated files** (`references.bib`, `relationships/relationships.md`,
  `docs/**`, `mkdocs.yml`) are rebuilt by the scripts — edit the *sources*
  (`citation.bib`, `relationships/_narrative.md`, `metadata.yaml`, `templates/`,
  `literature-review.md`) and re-run, don't hand-edit the outputs.
- **Paywalled papers** are noted from the abstract + public content and marked
  `status: abstract-only`; drop a `source.pdf` into the paper folder later to enrich.
- **First-time Pages setup:** repo **Settings → Pages → Source: GitHub Actions** (once).

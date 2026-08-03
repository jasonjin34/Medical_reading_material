#!/usr/bin/env python3
"""Fetch bibliographic metadata for a reading-list item.

Classifies a URL / DOI / arXiv id, then pulls title, authors, year, venue,
abstract, a Semantic Scholar id (for the relationship graph), and a BibTeX
entry. Uses only the Python standard library for HTTP so it runs before
`pip install -r requirements.txt`.

CLI:
    python scripts/fetch_metadata.py <url-or-doi-or-arxiv>
"""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.parse
import urllib.request

UA = "Medical_reading_material/1.0 (literature repo; mailto:jason.jiner@gmail.com)"


# --------------------------------------------------------------------------- #
# HTTP helpers (stdlib only)
# --------------------------------------------------------------------------- #
def _get(url: str, accept: str = "", timeout: int = 30) -> str:
    headers = {"User-Agent": UA}
    if accept:
        headers["Accept"] = accept
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def _get_json(url: str, timeout: int = 30):
    return json.loads(_get(url, accept="application/json", timeout=timeout))


# --------------------------------------------------------------------------- #
# Link classification
# --------------------------------------------------------------------------- #
DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)
ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf|html)/([0-9]{4}\.[0-9]{4,5})", re.I)
ARXIV_BARE_RE = re.compile(r"^([0-9]{4}\.[0-9]{4,5})$")

NATURE_DOI_RE = re.compile(r"nature\.com/articles/([a-z0-9\-]+)", re.I)


def classify(ref: str) -> dict:
    """Return {kind, doi, arxiv, url} for a raw reference string."""
    ref = ref.strip()
    out = {"kind": "web", "doi": "", "arxiv": "", "url": ref}

    if ARXIV_BARE_RE.match(ref):
        out.update(kind="arxiv", arxiv=ref, url=f"https://arxiv.org/abs/{ref}")
        return out
    m = ARXIV_RE.search(ref)
    if m:
        out.update(kind="arxiv", arxiv=m.group(1))
        return out
    if "github.com" in ref:
        out.update(kind="github")
        return out
    if "huggingface.co" in ref:
        out.update(kind="huggingface")
        return out
    # DOI, bare or inside a URL
    if ref.lower().startswith("10."):
        out.update(kind="doi", doi=ref)
        return out
    m = NATURE_DOI_RE.search(ref)
    if m:
        out.update(kind="doi", doi=f"10.1038/{m.group(1)}")
        return out
    m = DOI_RE.search(ref)
    if m:
        out.update(kind="doi", doi=m.group(0).rstrip("/.)"))
        return out
    return out


# --------------------------------------------------------------------------- #
# Fetchers
# --------------------------------------------------------------------------- #
def slugify(text: str, maxlen: int = 40) -> str:
    text = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return text[:maxlen].strip("-") or "item"


def bibtex_from_doi(doi: str) -> str:
    try:
        bib = _get(f"https://doi.org/{doi}", accept="application/x-bibtex")
        return bib.strip()
    except Exception:
        return ""


def fetch_doi(doi: str) -> dict:
    """Crossref for structured fields; doi.org content-negotiation for BibTeX."""
    meta = {"doi": doi, "bibtex": bibtex_from_doi(doi)}
    try:
        data = _get_json(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")
        msg = data.get("message", {})
        meta["title"] = " ".join(msg.get("title", [""])).strip()
        meta["authors"] = [
            f'{a.get("family","")}, {a.get("given","")}'.strip(", ")
            for a in msg.get("author", [])
        ]
        dp = msg.get("issued", {}).get("date-parts", [[None]])
        meta["year"] = dp[0][0] if dp and dp[0] else None
        meta["venue"] = (msg.get("container-title") or [""])[0]
        meta["abstract"] = re.sub(r"<[^>]+>", "", msg.get("abstract", "")).strip()
        meta["url"] = msg.get("URL", f"https://doi.org/{doi}")
    except Exception as e:
        meta["error"] = f"crossref: {e}"
    return meta


def fetch_arxiv(arxiv_id: str) -> dict:
    meta = {"arxiv": arxiv_id, "url": f"https://arxiv.org/abs/{arxiv_id}"}
    try:
        xml = _get(f"http://export.arxiv.org/api/query?id_list={arxiv_id}")
        title = re.search(r"<entry>.*?<title>(.*?)</title>", xml, re.S)
        meta["title"] = re.sub(r"\s+", " ", title.group(1)).strip() if title else ""
        meta["authors"] = [
            n.strip() for n in re.findall(r"<author>\s*<name>(.*?)</name>", xml, re.S)
        ]
        pub = re.search(r"<published>(\d{4})", xml)
        meta["year"] = int(pub.group(1)) if pub else None
        summ = re.search(r"<summary>(.*?)</summary>", xml, re.S)
        meta["abstract"] = re.sub(r"\s+", " ", summ.group(1)).strip() if summ else ""
        doi = re.search(r"<arxiv:doi[^>]*>(.*?)</arxiv:doi>", xml, re.S)
        meta["doi"] = doi.group(1).strip() if doi else ""
        meta["venue"] = "arXiv preprint"
        meta["bibtex"] = _arxiv_bibtex(meta, arxiv_id)
    except Exception as e:
        meta["error"] = f"arxiv: {e}"
    return meta


def _arxiv_bibtex(meta: dict, arxiv_id: str) -> str:
    first = (meta.get("authors") or ["Anon"])[0].split()[-1]
    year = meta.get("year") or "0000"
    key = f"{first}{year}_{arxiv_id.replace('.', '')}"
    authors = " and ".join(meta.get("authors", []))
    return (
        f"@misc{{{key},\n"
        f"  title = {{{meta.get('title','')}}},\n"
        f"  author = {{{authors}}},\n"
        f"  year = {{{year}}},\n"
        f"  eprint = {{{arxiv_id}}},\n"
        f"  archivePrefix = {{arXiv}},\n"
        f"  url = {{https://arxiv.org/abs/{arxiv_id}}}\n"
        f"}}"
    )


def fetch_s2(doi: str = "", arxiv: str = "", title: str = "") -> dict:
    """Semantic Scholar: paperId, abstract, tldr, references, citations."""
    pid = None
    if arxiv:
        pid = f"arXiv:{arxiv}"
    elif doi:
        pid = f"DOI:{doi}"
    fields = "paperId,title,year,abstract,tldr,references.externalIds,references.title,citationCount"
    try:
        if pid:
            d = _get_json(
                f"https://api.semanticscholar.org/graph/v1/paper/{urllib.parse.quote(pid)}?fields={fields}"
            )
        elif title:
            s = _get_json(
                "https://api.semanticscholar.org/graph/v1/paper/search?limit=1&fields="
                f"{fields}&query={urllib.parse.quote(title)}"
            )
            d = (s.get("data") or [None])[0] or {}
        else:
            return {}
        return {
            "s2_id": d.get("paperId", ""),
            "abstract": d.get("abstract") or "",
            "tldr": (d.get("tldr") or {}).get("text", "") if d.get("tldr") else "",
            "citationCount": d.get("citationCount"),
            "references": d.get("references", []),
        }
    except Exception as e:
        return {"error": f"s2: {e}"}


def fetch(ref: str) -> dict:
    """Top-level: classify + fetch the best metadata available."""
    c = classify(ref)
    meta = {"type": "paper", "access": "open", **c}
    if c["kind"] == "arxiv":
        meta.update({k: v for k, v in fetch_arxiv(c["arxiv"]).items() if v})
    elif c["kind"] == "doi":
        meta.update({k: v for k, v in fetch_doi(c["doi"]).items() if v})
    elif c["kind"] == "github":
        meta.update(_fetch_github(c["url"]))
    elif c["kind"] == "huggingface":
        meta.update(_fetch_hf(c["url"]))

    # enrich with Semantic Scholar (abstract fallback + references for graph)
    time.sleep(1.0)  # be polite to unauthenticated S2
    s2 = fetch_s2(meta.get("doi", ""), meta.get("arxiv", ""), meta.get("title", ""))
    for k in ("s2_id", "references"):
        if s2.get(k):
            meta[k] = s2[k]
    if not meta.get("abstract") and s2.get("abstract"):
        meta["abstract"] = s2["abstract"]
    if s2.get("tldr"):
        meta["tldr"] = s2["tldr"]
    return meta


def _fetch_github(url: str) -> dict:
    m = re.search(r"github\.com/([^/]+)/([^/#?]+)", url)
    if not m:
        return {"type": "code"}
    owner, repo = m.group(1), m.group(2)
    out = {"type": "code", "venue": "GitHub", "access": "open"}
    try:
        d = _get_json(f"https://api.github.com/repos/{owner}/{repo}")
        out["title"] = d.get("full_name", f"{owner}/{repo}")
        out["abstract"] = d.get("description") or ""
        if d.get("created_at"):
            out["year"] = int(d["created_at"][:4])
    except Exception:
        out["title"] = f"{owner}/{repo}"
    return out


def _fetch_hf(url: str) -> dict:
    m = re.search(r"huggingface\.co/([^/]+/[^/#?]+)", url)
    name = m.group(1) if m else url
    return {"type": "model", "venue": "Hugging Face", "title": name, "access": "open"}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    print(json.dumps(fetch(sys.argv[1]), indent=2, ensure_ascii=False))

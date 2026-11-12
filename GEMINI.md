# GEOMETOR • thompson (`geometor-thompson`)

Scholarly Digital Scriptorium Book Codex for **D'Arcy Wentworth Thompson: *On Growth and Form* (Cambridge University Press, 1st Edition, 1917)** paired with a **Dynamic Symmetry & Gnomonic Morphology Concordance** to **Jay Hambidge's *The Elements of Dynamic Symmetry* (Yale University Press, 1919–1920)**.

---

## 1. Architectural Mandates & Copyright Iron Law

1. **Strict 1917 / 1920 Public-Domain Boundary**:
   - **ONLY** use Thompson's **1917 Cambridge University Press First Edition** (`xv + 793 pp.`, 17 chapters, Project Gutenberg `#55264` / Internet Archive `ongrowthform1917thom`) and Hambidge's **1919–1920 Yale University Press** editions (*The Diagonal*, Vol. I, Nos. 1–12, `diagonal1191unse`, and *Dynamic Symmetry: The Greek Vase*, `dynamicsymmetry00hamb`).
   - **NEVER** quote or import prose, chapter numbers, or pagination from Thompson's 1942 Second Edition or Bonner's 1961 abridged edition.
2. **Strict Content / Code Separation**:
   - Zero embedded `py_file` directives, `.. code-block:: python`, or `.. literalinclude::` inside `docsrc/growth_and_form/`.
   - All 11 geometric diagrams are generated deterministically by `scripts/build_figures.py` as theme-adaptive `.euclid-graphic` SVGs in `docsrc/_static/figures/`.
3. **3-Track Synchronized Book Codex (`:layout: book`)**:
   - Every unit directory `docsrc/growth_and_form/<slug>/` compiles three synchronized tracks: `<slug>-en.rst`, `<slug>-summary.rst`, and `<slug>-notes.rst`, plus `concordance.rst`, `bibliography.rst`, `persons.rst`, and `glossary.rst` (26 `:layout: book` files total).

---

## 2. Key Modules & Layout

- `resources/growth_and_form/`:
  - `sources/`: Tracked UTF-8 primary sources (`gutenberg_55264_thompson_1917.txt`, `ia_diagonal1191unse_hambidge_1920.txt`, `ia_dynamicsymmetry00hamb_yale_1920.txt`).
  - `sources_manifest.json`: SHA-256 digests, byte counts, and explicit 1917/1920 public-domain attestation.
  - `concordance.json`, `persons.json`, `citations.json`, `glossary.json`: Machine-queryable apparatus registries (mirrored to `resources/`).
- `src/geometor/thompson/`:
  - `concordance.py`: `ThompsonApparatus`, `ConcordanceEntry`, `SisterRef`, `load_apparatus`, `verify_sources_manifest`.
  - `parser_1917.py`: Deterministic 1917 Gutenberg-to-RST parser, folio milestone emitter, authorial endnote linker, and SVG plate injector.
  - `units_data.py`: Declarative unit specifications, scan-verified 1919–1920 Hambidge lessons, and scholarly `-summary` / `-notes` tracks.
  - `compile_codex.py`: Generates all 26 `:layout: book` RST files under `docsrc/growth_and_form/`.
  - `cli.py`: `geometor-thompson` CLI (`compile`, `verify`, `summary`, `concordance`).
- `scripts/build_figures.py`: Generates 11 standalone `.euclid-graphic` SVGs into `docsrc/_static/figures/`.
- `tests/test_thompson.py`: Comprehensive verification suite for SHA-256 sources, apparatus cross-references, SVG contract, and Book Codex structure.

---

## 3. Sandbox Verification Commands

```bash
uv run --no-sync pytest
ruff check src scripts tests
publish build
```

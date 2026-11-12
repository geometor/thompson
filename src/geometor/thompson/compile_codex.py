"""Compile the 3-track synchronized Book Codex (`docsrc/growth_and_form/`) for `geometor-thompson`."""

from __future__ import annotations

from pathlib import Path

from geometor.thompson.concordance import (
    DEFAULT_REPO_ROOT,
    ThompsonApparatus,
    apparatus_slug,
    load_apparatus,
)
from geometor.thompson.parser_1917 import (
    load_thompson_1917_lines,
    parse_endnotes_1917,
    render_chapter_slice_1917,
    render_footnotes_section,
)
from geometor.thompson.units_data import UNITS, UnitSpec


def _write_rst(target: Path, content: str) -> Path:
    """Write normalized UTF-8 RST file, creating parent directories if needed."""
    target.parent.mkdir(parents=True, exist_ok=True)
    text = content.rstrip() + "\n"
    target.write_text(text, encoding="utf-8")
    return target


def _build_unit_en(
    unit: UnitSpec,
    lines_1917: list[str],
    notes_map: dict[int, str],
    injected_plates: set[int],
) -> str:
    """Build `<slug>/<slug>-en.rst` for a unit."""
    parts: list[str] = [
        ":layout: book",
        "",
        f".. _growth-and-form-{unit.slug}-en:",
        "",
        unit.title,
        "=" * len(unit.title),
        "",
        f".. rubric:: {unit.rubric}",
        "",
        ".. contents:: In This Unit",
        "   :local:",
        "   :depth: 2",
        "   :backlinks: none",
        "",
    ]
    used_notes: list[int] = []
    if unit.custom_en_body:
        parts.append(unit.custom_en_body.strip())
        parts.append("")
    else:
        for ch_key in unit.chapters_1917:
            ch_rst = render_chapter_slice_1917(
                lines_1917,
                ch_key,
                notes_map,
                used_notes,
                injected_plates,
            )
            parts.append(ch_rst.strip())
            parts.append("")
        fn_block = render_footnotes_section(used_notes, notes_map)
        if fn_block:
            parts.append(fn_block.strip())
            parts.append("")
    return "\n".join(parts)


def _build_unit_summary(unit: UnitSpec) -> str:
    """Build `<slug>/<slug>-summary.rst` for a unit."""
    heading = f"{unit.title} — Summary"
    return "\n".join(
        [
            ":layout: book",
            "",
            f".. _growth-and-form-{unit.slug}-summary:",
            "",
            heading,
            "=" * len(heading),
            "",
            f".. rubric:: Analytical Synopsis — {unit.rubric}",
            "",
            unit.summary_body.strip(),
            "",
        ]
    )


def _build_unit_notes(unit: UnitSpec, apparatus: ThompsonApparatus) -> str:
    """Build `<slug>/<slug>-notes.rst` for a unit, appending unit concordance links."""
    heading = f"{unit.title} — Notes & Concordance"
    lines: list[str] = [
        ":layout: book",
        "",
        f".. _growth-and-form-{unit.slug}-notes:",
        "",
        heading,
        "=" * len(heading),
        "",
        f".. rubric:: Critical Apparatus & GEOMETOR Cross-References — {unit.short_title}",
        "",
        unit.notes_body.strip(),
        "",
    ]
    entries = apparatus.by_unit(unit.slug)
    if entries:
        lines.extend(
            [
                "Structured Concordance Loci in This Unit",
                "----------------------------------------",
                "",
            ]
        )
        for entry in entries:
            lines.append(f"**{entry.topic}** (*{entry.chapter}*, {entry.pages_1917})")
            lines.append(f"   {entry.summary}")
            if entry.invariants:
                inv_str = " · ".join(f"``{inv}``" for inv in entry.invariants)
                lines.append(f"   *Algebraic Invariants:* {inv_str}")
            if entry.sister_refs or entry.hambidge_parallels:
                lines.append("")
            for sref in entry.sister_refs:
                lines.append(f"   * **geometor/{sref.repo}** (*{sref.locus}*): {sref.relation}")
            for hpar in entry.hambidge_parallels:
                lines.append(f"   * *Dynamic Symmetry Parallel:* {hpar}")
            lines.append("")
    return "\n".join(lines)


def _build_persons_rst(apparatus: ThompsonApparatus) -> str:
    """Render `docsrc/growth_and_form/persons.rst`."""
    lines = [
        ":layout: book",
        "",
        ".. _persons:",
        "",
        "Index of Persons",
        "================",
        "",
        ".. rubric:: Prosopographical Registry of Morphologists, Geometers, Physicists & Philosophers",
        "",
    ]
    for key in sorted(apparatus.persons):
        item = apparatus.persons[key]
        slug = apparatus_slug(key)
        lines.extend(
            [
                f".. _person-{slug}:",
                "",
                f"**{item['name']}** ({item['dates']}) — *{item['role']}*",
                f"   {item['bio']}",
                "",
            ]
        )
    return "\n".join(lines)


def _build_bibliography_rst(apparatus: ThompsonApparatus) -> str:
    """Render `docsrc/growth_and_form/bibliography.rst`."""
    lines = [
        ":layout: book",
        "",
        ".. _bibliography:",
        "",
        "Systematic Bibliography",
        "=======================",
        "",
        ".. rubric:: Primary 1917 / 1920 Editions, Classical Treatises & Morphological Monographs",
        "",
    ]
    for key in sorted(apparatus.citations):
        item = apparatus.citations[key]
        slug = apparatus_slug(key)
        lines.extend(
            [
                f".. _cite-{slug}:",
                "",
                f"**{item['author']}** — *{item['work']}*",
                f"   {item['locus']}, {item['publisher']}, {item['year']}.",
                "",
                f"   {item['note']}",
                "",
            ]
        )
    return "\n".join(lines)


def _build_glossary_rst(apparatus: ThompsonApparatus) -> str:
    """Render `docsrc/growth_and_form/glossary.rst`."""
    lines = [
        ":layout: book",
        "",
        ".. _glossary:",
        "",
        "Morphological & Geometric Glossary",
        "==================================",
        "",
        ".. rubric:: Technical Terminology of Growth, Capillarity, Phyllotaxis & Dynamic Symmetry",
        "",
    ]
    for key in sorted(apparatus.glossary):
        item = apparatus.glossary[key]
        slug = apparatus_slug(key)
        lines.extend(
            [
                f".. _term-{slug}:",
                "",
                f"**{item['headword']}** ({item['language']} · *{item['translation']}*)",
                f"   {item['definition']}",
                "",
            ]
        )
    return "\n".join(lines)


def _build_concordance_rst(apparatus: ThompsonApparatus) -> str:
    """Render `docsrc/growth_and_form/concordance.rst`."""
    meta = apparatus.concordance_meta
    lines = [
        ":layout: book",
        "",
        ".. _concordance:",
        "",
        "Thompson–Hambidge–GEOMETOR Master Concordance",
        "=============================================",
        "",
        f".. rubric:: {meta.get('title', 'Morphological & Dynamic Symmetry Concordance')}",
        "",
        meta.get("description", ""),
        "",
        "Editions Aligned & Copyright Boundary",
        "-------------------------------------",
        "",
    ]
    for ed_key, ed_desc in meta.get("editions_aligned", {}).items():
        lines.append(f"* **{ed_key}**: {ed_desc}")
    lines.append("")
    if meta.get("edition_boundary_note"):
        lines.extend(
            [
                ".. note::",
                "",
                f"   {meta['edition_boundary_note']}",
                "",
            ]
        )
    lines.extend(
        [
            "Cross-Repository Concordance Entries",
            "------------------------------------",
            "",
        ]
    )
    for entry in apparatus.entries:
        lines.extend(
            [
                f".. _concordance-{apparatus_slug(entry.id)}:",
                "",
                f"{entry.topic}",
                "~" * len(entry.topic),
                "",
                f"| **Unit & Locus:** :ref:`{entry.chapter} <growth-and-form-{entry.unit}-en>` ({entry.pages_1917})",
                f"| **Summary:** {entry.summary}",
                "",
            ]
        )
        if entry.invariants:
            inv_fmt = ", ".join(f"``{inv}``" for inv in entry.invariants)
            lines.append(f"* **Exact Invariants:** {inv_fmt}")
        for sref in entry.sister_refs:
            lines.append(
                f"* **geometor/{sref.repo}** (*{sref.locus}*): {sref.relation}"
            )
        for hpar in entry.hambidge_parallels:
            lines.append(f"* **Jay Hambidge (1919–1920):** {hpar}")
        lines.append("")
    return "\n".join(lines)


def _build_codex_index_rst() -> str:
    """Render `docsrc/growth_and_form/index.rst` (`:layout: book`)."""
    lines = [
        ":layout: book",
        "",
        ".. _growth-and-form-index:",
        "",
        "ON GROWTH AND FORM",
        "==================",
        "",
        ".. rubric:: *D'Arcy Wentworth Thompson* (Cambridge University Press, First Edition, 1917) & *Jay Hambidge's Dynamic Symmetry* (Yale University Press, 1919–1920)",
        "",
        "| **Editio Princeps (1917):** *On Growth and Form*, by D'Arcy Wentworth Thompson, Cambridge: at the University Press, 1917 (xv + 793 pp., 17 chapters, 408 figures).",
        "| **Dynamic Symmetry Companion (1919–1920):** *The Diagonal* (Vol. I, Nos. 1–12) & *Dynamic Symmetry: The Greek Vase*, by Jay Hambidge, New Haven: Yale University Press, 1919–1920.",
        "| **Digital Scriptorium Codex:** Synchronized 3-track edition (*English · Summary · Notes*) with 11 theme-adaptive ``.euclid-graphic`` SVG plates curated within the GEOMETOR canon.",
        "",
        ".. epigraph::",
        "",
        "   “Cum formarum naturalium et corporalium esse non consistat nisi in unione ad materiam, ejusdem agentis esse videtur eas producere cujus est materiam transmutare. Secundo, quia cum hujusmodi formae non excedant virtutem et ordinem et facultatem principiorum agentium in natura, nulla videtur necessitas eorum originem in principia reducere altiora.”",
        "",
        "   — :person:`St. Thomas Aquinas <aquinas>`, :cite:`*De Potentia Dei*, Q. iii, a. 11 <aquinas:depot>` (*1917 Epigraph*)",
        "",
        "----",
        "",
        "Conspectus Totius Operis (1917 First Edition & 1920 Companion)",
        "--------------------------------------------------------------",
        "",
    ]
    for unit in UNITS:
        lines.extend(
            [
                f"**{unit.title}** (*{unit.rubric}*)",
                (
                    f"   :ref:`1917/1920 Text <growth-and-form-{unit.slug}-en>` · "
                    f":ref:`Summary <growth-and-form-{unit.slug}-summary>` · "
                    f":ref:`Notes & Concordance <growth-and-form-{unit.slug}-notes>`"
                ),
                "",
            ]
        )

    lines.extend(
        [
            "----",
            "",
            "Apparatus Criticus & Cross-Repository Indices",
            "---------------------------------------------",
            "",
            "* :ref:`Thompson–Hambidge–GEOMETOR Master Concordance <concordance>` — Cross-mapping across ``euclid``, ``elements``, ``aristotle``, ``aquinas``, ``pacioli``, ``pappus``, ``divine``, ``etc``, ``wildberger``, ``phyllotaxis``, and ``hilbert``.",
            "* :ref:`Systematic Bibliography <bibliography>` — Primary 1917/1920 editions, classical geometers, and morphological monographs.",
            "* :ref:`Prosopographical Index of Persons <persons>` — Naturalists, mathematicians, engineers, and philosophers.",
            "* :ref:`Morphological & Geometric Glossary <glossary>` — Technical vocabulary of capillarity, gnomons, phyllotaxis, graphic statics, transformations, and Dynamic Symmetry.",
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "   :hidden:",
            "   :caption: On Growth and Form (1917) & Dynamic Symmetry (1920)",
            "",
        ]
    )
    for unit in UNITS:
        lines.append(f"   {unit.slug}/{unit.slug}-en")

    lines.extend(
        [
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "   :hidden:",
            "   :caption: Analytical Summaries",
            "",
        ]
    )
    for unit in UNITS:
        lines.append(f"   {unit.slug}/{unit.slug}-summary")

    lines.extend(
        [
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "   :hidden:",
            "   :caption: Scholarly Notes & Concordance",
            "",
        ]
    )
    for unit in UNITS:
        lines.append(f"   {unit.slug}/{unit.slug}-notes")

    lines.extend(
        [
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "   :hidden:",
            "   :caption: Critical Apparatus",
            "",
            "   concordance",
            "   bibliography",
            "   persons",
            "   glossary",
            "",
        ]
    )
    return "\n".join(lines)


def compile_codex(repo_root: Path | None = None) -> list[Path]:
    """Compile all 26 `:layout: book` RST files under `docsrc/growth_and_form/`."""
    root = (repo_root or DEFAULT_REPO_ROOT).resolve()
    apparatus = load_apparatus(root)
    lines_1917 = load_thompson_1917_lines(root)
    notes_map = parse_endnotes_1917(lines_1917)

    codex_dir = root / "docsrc" / "growth_and_form"
    written: list[Path] = []
    injected_plates: set[int] = set()

    written.append(_write_rst(codex_dir / "index.rst", _build_codex_index_rst()))
    for unit in UNITS:
        unit_dir = codex_dir / unit.slug
        written.append(
            _write_rst(
                unit_dir / f"{unit.slug}-en.rst",
                _build_unit_en(unit, lines_1917, notes_map, injected_plates),
            )
        )
        written.append(_write_rst(unit_dir / f"{unit.slug}-summary.rst", _build_unit_summary(unit)))
        written.append(
            _write_rst(unit_dir / f"{unit.slug}-notes.rst", _build_unit_notes(unit, apparatus))
        )

    written.append(_write_rst(codex_dir / "concordance.rst", _build_concordance_rst(apparatus)))
    written.append(_write_rst(codex_dir / "bibliography.rst", _build_bibliography_rst(apparatus)))
    written.append(_write_rst(codex_dir / "persons.rst", _build_persons_rst(apparatus)))
    written.append(_write_rst(codex_dir / "glossary.rst", _build_glossary_rst(apparatus)))
    return written

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
    """Build `<slug>/index.rst` for a chapter."""
    parts: list[str] = [
        ":layout: book",
        f":canonical_id: {unit.canonical_id}",
        f":breadcrumb_title: {unit.canonical_id}",
        f":order: {unit.order}",
        f":folio: {unit.folio}",
        ":tracks: English: index | Summary: summary | Notes: notes",
        "",
        f".. _growth-and-form-{unit.slug}:",
        f".. _growth-and-form-{unit.slug}-en:",
        f".. _growth-and-form-ch-{unit.order}:",
    ]
    if unit.legacy_anchor:
        parts.append(f".. _{unit.legacy_anchor}:")
    parts.extend(
        [
            "",
            unit.title,
            "=" * len(unit.title),
            "",
            f".. rubric:: {unit.rubric}",
            "",
        ]
    )
    used_notes: list[int] = []
    if unit.custom_en_body:
        parts.append(unit.custom_en_body.strip())
        parts.append("")
    else:
        for ch_key in unit.chapters_1917:
            include_heading = unit.slug == "ch_01" or ch_key == "epilogue"
            ch_rst = render_chapter_slice_1917(
                lines_1917,
                ch_key,
                notes_map,
                used_notes,
                injected_plates,
                include_heading=include_heading,
            )
            parts.append(ch_rst.strip())
            parts.append("")
        fn_block = render_footnotes_section(used_notes, notes_map)
        if fn_block:
            parts.append(fn_block.strip())
            parts.append("")
    return "\n".join(parts)


def _build_unit_summary(unit: UnitSpec) -> str:
    """Build `<slug>/summary.rst` for a chapter."""
    heading = f"{unit.title} — Summary"
    lines = [
        ":layout: book",
        f":canonical_id: {unit.canonical_id} (Summary)",
        ":breadcrumb_title: Summary",
        f":order: {unit.order}",
        ":tracks: English: index | Summary: summary | Notes: notes",
        "",
        f".. _growth-and-form-{unit.slug}-summary:",
    ]
    if unit.legacy_anchor:
        lines.append(f".. _{unit.legacy_anchor.replace('-en', '-summary')}:")
    lines.extend(
        [
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
    return "\n".join(lines)


def _build_unit_notes(unit: UnitSpec, apparatus: ThompsonApparatus) -> str:
    """Build `<slug>/notes.rst` for a chapter, appending chapter concordance links."""
    heading = f"{unit.title} — Notes & Concordance"
    lines: list[str] = [
        ":layout: book",
        f":canonical_id: {unit.canonical_id} (Notes)",
        ":breadcrumb_title: Notes",
        f":order: {unit.order}",
        ":tracks: English: index | Summary: summary | Notes: notes",
        "",
        f".. _growth-and-form-{unit.slug}-notes:",
    ]
    if unit.legacy_anchor:
        lines.append(f".. _{unit.legacy_anchor.replace('-en', '-notes')}:")
    lines.extend(
        [
            "",
            heading,
            "=" * len(heading),
            "",
            f".. rubric:: Scholarly Apparatus & GEOMETOR Cross-References — {unit.canonical_id}",
            "",
            unit.notes_body.strip(),
            "",
        ]
    )
    entries = apparatus.by_unit(unit.slug)
    if entries:
        lines.extend(
            [
                "Structured Concordance Loci in This Chapter",
                "-------------------------------------------",
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
        ":navigation: header",
        ":order: 5",
        ":nav_title: People",
        "",
        ".. _persons:",
        "",
        "People",
        "======",
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
        ":navigation: header",
        ":order: 6",
        ":nav_title: Bibliography",
        "",
        ".. _bibliography:",
        "",
        "Bibliography",
        "============",
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
        ":navigation: footer",
        ":nav_title: Glossary",
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
        ":navigation: footer",
        ":nav_title: Concordance",
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
                f"| **Chapter & Locus:** :ref:`{entry.chapter} <growth-and-form-{entry.unit}-en>` ({entry.pages_1917})",
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
        ":navigation: header",
        ":order: 1",
        ":type: book",
        ":nav_title: On Growth and Form",
        ":breadcrumb_title: On Growth and Form",
        ":book_title: On Growth and Form",
        ":book_subtitle: Sir D'Arcy Wentworth Thompson (Cambridge, 1917)",
        ":author: Sir D'Arcy Wentworth Thompson",
        ":year: 1917",
        ":excerpt: Sir D'Arcy Wentworth Thompson's classic mathematical and physical analysis of biological morphology, scaling laws, surface tension, cellular foams, equiangular spirals, phyllotaxis, bone architecture, and coordinate transformations.",
        "",
        ".. _growth-and-form-index:",
        "",
        "On Growth and Form",
        "==================",
        "",
        ".. rubric:: *Sir D'Arcy Wentworth Thompson* — Cambridge University Press (First Edition, 1917)",
        "",
        ".. container:: title-page",
        "",
        "   | **Author:** :person:`Sir D'Arcy Wentworth Thompson <thompson>`",
        "   | **First Edition (Cambridge, 1917):** *On Growth and Form*, by D'Arcy Wentworth Thompson, Cambridge: at the University Press, 1917 (xv + 793 pp., 17 chapters, 408 figures).",
        "   | **Digital Scriptorium Codex:** Synchronized 3-track edition (*English · Summary · Notes*) with 10 theme-adaptive ``.euclid-graphic`` SVG plates curated within the GEOMETOR canon.",
        "",
        ".. epigraph::",
        "",
        "   “Cum formarum naturalium et corporalium esse non consistat nisi in unione ad materiam, ejusdem agentis esse videtur eas producere cujus est materiam transmutare. Secundo, quia cum hujusmodi formae non excedant virtutem et ordinem et facultatem principiorum agentium in natura, nulla videtur necessitas eorum originem in principia reducere altiora.”",
        "",
        "   — :person:`St. Thomas Aquinas <aquinas>`, :cite:`*De Potentia Dei*, Q. iii, a. 11 <aquinas:depot>` (*1917 Epigraph*)",
        "",
        "----",
        "",
        "Table of Contents",
        "-----------------",
        "",
        ".. collection::",
        "   :sort: order",
        "",
    ]
    for unit in UNITS:
        lines.append(f"   {unit.slug}/index")

    lines.extend(
        [
            "",
            "----",
            "",
            "Scholarly Apparatus",
            "-------------------",
            "",
            "* :ref:`Thompson & GEOMETOR Master Concordance <concordance>` — Cross-mapping across ``euclid``, ``elements``, ``aristotle``, ``aquinas``, ``pacioli``, ``pappus``, ``divine``, ``etc``, ``wildberger``, ``phyllotaxis``, ``hilbert``, and ``hambidge``.",
            "* :ref:`Systematic Bibliography <bibliography>` — Primary 1917 Cambridge First Edition, classical geometers, and morphological monographs.",
            "* :ref:`People <persons>` — Naturalists, mathematicians, engineers, and philosophers.",
            "* :ref:`Morphological & Geometric Glossary <glossary>` — Technical vocabulary of capillarity, gnomons, phyllotaxis, graphic statics, and transformations.",
            "",
            ".. toctree::",
            "   :maxdepth: 2",
            "   :hidden:",
            "   :caption: On Growth and Form (1917)",
            "",
        ]
    )
    for unit in UNITS:
        lines.append(f"   {unit.slug}/index")
        lines.append(f"   {unit.slug}/summary")
        lines.append(f"   {unit.slug}/notes")

    lines.extend(
        [
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "   :hidden:",
            "   :caption: Scholarly Apparatus",
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
    """Compile all 56 `:layout: book` RST files under `docsrc/growth_and_form/`."""
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
                unit_dir / "index.rst",
                _build_unit_en(unit, lines_1917, notes_map, injected_plates),
            )
        )
        written.append(_write_rst(unit_dir / "summary.rst", _build_unit_summary(unit)))
        written.append(
            _write_rst(unit_dir / "notes.rst", _build_unit_notes(unit, apparatus))
        )

    written.append(_write_rst(codex_dir / "concordance.rst", _build_concordance_rst(apparatus)))
    written.append(_write_rst(codex_dir / "bibliography.rst", _build_bibliography_rst(apparatus)))
    written.append(_write_rst(codex_dir / "persons.rst", _build_persons_rst(apparatus)))
    written.append(_write_rst(codex_dir / "glossary.rst", _build_glossary_rst(apparatus)))
    return written

"""Comprehensive verification suite for `geometor-thompson` (1917 On Growth and Form & 1920 Dynamic Symmetry)."""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path

from geometor import thompson
from geometor.thompson.cli import main as cli_main
from geometor.thompson.concordance import (
    apparatus_slug,
    load_apparatus,
    verify_sources_manifest,
)
from geometor.thompson.units_data import UNITS

REPO_ROOT = Path(__file__).resolve().parents[1]
CODEX_DIR = REPO_ROOT / "docsrc" / "growth_and_form"
FIGURES_DIR = REPO_ROOT / "docsrc" / "_static" / "figures"

EXPECTED_SVGS = (
    "fig_galileo_scaling.svg",
    "fig_plateau_fermat_hex.svg",
    "fig_maraldi_honeycomb.svg",
    "fig_kelvin_tetrakaidecahedron.svg",
    "fig_hambidge_root_rectangles.svg",
    "fig_golden_gnomon_spiral.svg",
    "fig_nautilus_chambered_spiral.svg",
    "fig_phyllotaxis_parastichy.svg",
    "fig_culmann_femur_trajectories.svg",
    "fig_transform_affine_shear.svg",
    "fig_transform_coaxial_mesh.svg",
)


def test_version_and_exports() -> None:
    """Verify package version and top-level exports."""
    assert thompson.__version__ == "0.1.1"
    assert callable(thompson.compile_codex)
    assert callable(thompson.load_apparatus)
    assert callable(thompson.verify_sources_manifest)


def test_sources_manifest_sha256_and_1917_copyright_boundary() -> None:
    """Verify SHA-256 digests and strict 1917 Cambridge / 1920 Yale public-domain attestation."""
    results = verify_sources_manifest(REPO_ROOT)
    assert len(results) == 3
    assert all(item["verified"] is True for item in results)
    years = {item["id"]: item["year"] for item in results}
    assert years == {
        "thompson-1917-cup": 1917,
        "hambidge-1920-diagonal": 1920,
        "hambidge-1920-vase": 1920,
    }

    apparatus = load_apparatus(REPO_ROOT)
    work_meta = apparatus.sources_manifest["work"]
    assert work_meta["original_year"] == 1917
    assert "1917" in work_meta["edition"]
    assert "Cambridge University Press" in work_meta["edition"]
    attestation = work_meta["copyright_attestation"]
    assert "1942 Second Edition" in attestation
    assert "strictly excluded" in attestation


def test_apparatus_counts_and_sister_repo_coverage() -> None:
    """Verify prosopography, bibliography, glossary, and cross-repo concordance coverage."""
    apparatus = load_apparatus(REPO_ROOT)
    assert len(apparatus.persons) >= 35
    assert len(apparatus.citations) >= 32
    assert len(apparatus.glossary) >= 32
    assert len(apparatus.entries) >= 11

    for unit in UNITS:
        assert len(apparatus.by_unit(unit.slug)) >= 1, f"Missing concordance entry for {unit.slug}"

    expected_repos = {
        "euclid",
        "elements",
        "aristotle",
        "aquinas",
        "pacioli",
        "pappus",
        "divine",
        "etc",
        "wildberger",
        "phyllotaxis",
        "hilbert",
    }
    linked_repos = {ref.repo for entry in apparatus.entries for ref in entry.sister_refs}
    assert expected_repos.issubset(linked_repos)

    assert len(apparatus.search("Maraldi")) >= 1
    assert len(apparatus.search("X(13)")) >= 1
    assert len(apparatus.search("whirling")) >= 1

    # Verify root-level resources mirror
    for fname in ("persons.json", "citations.json", "glossary.json"):
        root_copy = (REPO_ROOT / "resources" / fname).read_text(encoding="utf-8")
        codex_copy = (REPO_ROOT / "resources" / "growth_and_form" / fname).read_text(encoding="utf-8")
        assert root_copy == codex_copy


def test_codex_rst_tracks_chapters_and_no_embedded_python() -> None:
    """Verify all 26 :layout: book RST files, all 17 chapters, and zero embedded Python directives."""
    expected_files = [
        CODEX_DIR / "index.rst",
        CODEX_DIR / "concordance.rst",
        CODEX_DIR / "bibliography.rst",
        CODEX_DIR / "persons.rst",
        CODEX_DIR / "glossary.rst",
    ]
    for unit in UNITS:
        for track in ("en", "summary", "notes"):
            expected_files.append(CODEX_DIR / unit.slug / f"{unit.slug}-{track}.rst")

    assert len(expected_files) == 26
    combined_en = []
    for rst_path in expected_files:
        assert rst_path.is_file(), f"Missing codex file: {rst_path}"
        text = rst_path.read_text(encoding="utf-8")
        assert text.startswith(":layout: book\n"), f"{rst_path} must start with :layout: book"
        assert ".. py_file::" not in text
        assert "code-block:: python" not in text
        assert ".. literalinclude::" not in text
        if rst_path.name.endswith("-en.rst"):
            combined_en.append(text)

    full_en_corpus = "\n".join(combined_en)
    # All 17 chapters + Prefatory Note + Epigraphs + Epilogue + Hambidge sections must be present
    assert ".. _thompson-1917-prefatory:" in full_en_corpus
    assert ".. _thompson-1917-epigraphs:" in full_en_corpus
    assert ".. _thompson-1917-epilogue:" in full_en_corpus
    for ch_num in range(1, 18):
        assert f".. _thompson-1917-ch-{ch_num}:" in full_en_corpus
    assert ".. _hambidge-1920-root-rectangles:" in full_en_corpus


def test_euclid_graphic_svg_contract_and_codex_embedding() -> None:
    """Verify all 11 standalone .euclid-graphic SVGs parse cleanly and are wired via .. picture::."""
    all_codex_rst = "\n".join(
        p.read_text(encoding="utf-8") for p in CODEX_DIR.rglob("*.rst")
    )
    for svg_name in EXPECTED_SVGS:
        svg_path = FIGURES_DIR / svg_name
        assert svg_path.is_file(), f"Missing SVG figure: {svg_path}"
        raw_svg = svg_path.read_text(encoding="utf-8")
        root = ET.fromstring(raw_svg)
        assert "euclid-graphic" in root.attrib.get("class", "")
        assert "prefers-color-scheme: dark" in raw_svg
        assert "geom-tick-1" in raw_svg
        assert 'data-ref="' in raw_svg
        assert f".. picture:: /_static/figures/{svg_name}" in all_codex_rst


def test_role_resolution_and_math_delimiter_balance() -> None:
    """Verify every :person:, :cite:, and :term: role resolves and inline $ math is balanced."""
    apparatus = load_apparatus(REPO_ROOT)
    person_slugs = {apparatus_slug(k) for k in apparatus.persons}
    cite_slugs = {apparatus_slug(k) for k in apparatus.citations}
    term_slugs = {apparatus_slug(k) for k in apparatus.glossary}

    role_re = re.compile(r":(person|cite|term):`([^`]+)`")
    target_re = re.compile(r"<([^>]+)>\s*$")

    for rst_path in (REPO_ROOT / "docsrc").rglob("*.rst"):
        if "modules/api" in rst_path.as_posix():
            continue
        text = rst_path.read_text(encoding="utf-8")
        for match in role_re.finditer(text):
            role_kind, body = match.group(1), match.group(2).strip()
            tmatch = target_re.search(body)
            raw_key = tmatch.group(1).strip() if tmatch else body
            slug = apparatus_slug(raw_key)
            if role_kind == "person":
                assert slug in person_slugs, f"Unresolved :person:`{body}` in {rst_path}"
            elif role_kind == "cite":
                assert slug in cite_slugs, f"Unresolved :cite:`{body}` in {rst_path}"
            elif role_kind == "term":
                assert slug in term_slugs, f"Unresolved :term:`{body}` in {rst_path}"

        # Check balanced $ signs outside $$ display blocks
        stripped_display = text.replace("$$", "")
        unescaped_dollars = len(re.findall(r"(?<!\\)\$", stripped_display))
        assert unescaped_dollars % 2 == 0, f"Unbalanced $ delimiter in {rst_path}"


def test_cli_commands(capsys) -> None:
    """Verify CLI verify, summary, and concordance subcommands exit cleanly."""
    assert cli_main(["--root", str(REPO_ROOT), "verify"]) == 0
    out_verify = capsys.readouterr().out
    assert "thompson-1917-cup" in out_verify

    assert cli_main(["--root", str(REPO_ROOT), "summary"]) == 0
    out_summary = capsys.readouterr().out
    assert '"concordance_entries": 11' in out_summary

    assert cli_main(["--root", str(REPO_ROOT), "concordance", "--repo", "wildberger"]) == 0
    out_conc = capsys.readouterr().out
    assert "maraldi-honeycomb-kelvin" in out_conc

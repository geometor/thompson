"""Deterministic parser for the 1917 Cambridge First Edition of On Growth and Form.

Transforms the Distributed Proofreaders / Project Gutenberg transcription (#55264) of
D'Arcy Wentworth Thompson's 1917 Cambridge University Press First Edition into clean,
zero-warning Sphinx reStructuredText with `.. folio::`, `.. picture::`, and clickable
1917 authorial endnotes.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

CHAPTER_STARTS_1917: dict[str, tuple[int, int, str, str]] = {
    "prefatory": (46, 134, "Prefatory Note", "pp. v–vi"),
    "epigraphs": (917, 945, "Epigraphs (Aquinas, Newton, Jellett)", "p. xvi"),
    "ch-1": (951, 1421, "Chapter I: Introductory", "pp. 1–15"),
    "ch-2": (1422, 2550, "Chapter II: On Magnitude", "pp. 16–49"),
    "ch-3": (2551, 5877, "Chapter III: The Rate of Growth", "pp. 50–155"),
    "ch-4": (5878, 7302, "Chapter IV: On the Internal Form and Structure of the Cell", "pp. 156–200"),
    "ch-5": (7303, 9852, "Chapter V: The Forms of Cells", "pp. 201–276"),
    "ch-6": (9853, 10375, "Chapter VI: A Note on Adsorption", "pp. 277–292"),
    "ch-7": (10376, 12062, "Chapter VII: The Forms of Tissues, or Cell-Aggregates", "pp. 293–345"),
    "ch-8": (12063, 14052, "Chapter VIII: The Forms of Tissues (continued)", "pp. 346–410"),
    "ch-9": (14053, 16306, "Chapter IX: On Concretions, Spicules, and Spicular Skeletons", "pp. 411–487"),
    "ch-10": (16307, 16477, "Chapter X: A Parenthetic Note on Geodetics", "pp. 488–492"),
    "ch-11": (16478, 19531, "Chapter XI: The Logarithmic Spiral", "pp. 493–586"),
    "ch-12": (19532, 20254, "Chapter XII: The Spiral Shells of the Foraminifera", "pp. 587–611"),
    "ch-13": (20255, 21009, "Chapter XIII: The Shapes of Horns, and of Teeth or Tusks: with a Note on Torsion", "pp. 612–634"),
    "ch-14": (21010, 21545, "Chapter XIV: On Leaf-Arrangement, or Phyllotaxis", "pp. 635–651"),
    "ch-15": (21546, 22183, "Chapter XV: On the Shapes of Eggs, and of Certain Other Hollow Structures", "pp. 652–669"),
    "ch-16": (22184, 23722, "Chapter XVI: On Form and Mechanical Efficiency", "pp. 670–718"),
    "ch-17": (23723, 25335, "Chapter XVII: On the Theory of Transformations, or the Comparison of Related Forms", "pp. 719–777"),
    "epilogue": (25336, 25405, "Epilogue", "pp. 778–779"),
}


@dataclass(frozen=True)
class PlateSpec:
    """SVG plate injection metadata keyed to a 1917 figure number."""

    svg_file: str
    alt: str
    caption: str


PLATE_TRIGGERS: dict[int, PlateSpec] = {
    1: PlateSpec(
        svg_file="fig_galileo_scaling.svg",
        alt="Geometrically similar cubes of linear scale L = 1, 2, 3 and Galileo's square-cube scaling curves S ~ L^2 vs V ~ L^3.",
        caption="**Similitude and Galileo's Square-Cube Law (Ch. II, pp. 19–28).** Linear magnification $L$ scales surface and cross-sectional strength as $L^2$ while weight grows as $L^3$, driving specific surface $S/V \\propto L^{-1}$ downward.",
    ),
    115: PlateSpec(
        svg_file="fig_plateau_fermat_hex.svg",
        alt="Steiner-Fermat 120-degree soap-film triple junction X(13) and hexagonal cellular partition with exact rational spread s = 3/4.",
        caption="**Plateau's $120^\\circ$ Soap-Film Equilibrium and Fermat–Torricelli Point `X(13)` (Ch. VII, Figs. 114–115).** Three liquid laminae meet at exact $120^\\circ$ dihedral angles (rational spread $s = 3/4$), generating hexagonal cellular pavements.",
    ),
    132: PlateSpec(
        svg_file="fig_maraldi_honeycomb.svg",
        alt="Honeycomb hexagonal prism capped by three congruent Maraldi rhombi meeting at trihedral apex V with obtuse angle 109 deg 28 min 16 sec and diagonal ratio 1 : sqrt(2).",
        caption="**The Bee's Rhombic Dodecahedral Cell Cap and Maraldi Angle (Ch. VII, Fig. 132, p. 330).** Three congruent rhombi ($\\cos\\theta = -1/3$, $\\tan(\\theta/2) = \\sqrt{2}$, exact rational spread $s = 8/9$) minimize surface wax area.",
    ),
    134: PlateSpec(
        svg_file="fig_kelvin_tetrakaidecahedron.svg",
        alt="Plateau's central square soap film inside a wire cube frame (Fig. 134) and Lord Kelvin's space-filling minimal-foam tetrakaidecahedron of 8 hexagons and 6 squares.",
        caption="**Plateau's Wire-Cube Soap Film and Kelvin's Minimal-Foam Tetrakaidecahedron (Ch. VII, Fig. 134, pp. 337–341).** Collapse of an unstable 8-valent central vertex into tetrahedral $109^\\circ 28'$ edges and space-filling 14-hedral parenchyma cells.",
    ),
    247: PlateSpec(
        svg_file="fig_nautilus_chambered_spiral.svg",
        alt="Chambered Nautilus logarithmic spiral r = a exp(theta cot alpha) with concave septa and constant tangent angle alpha.",
        caption="**The Equiangular Spiral of *Nautilus* ($r = a e^{\\theta \\cot\\alpha}$, Ch. XI, Fig. 247, p. 495).** Constant tangent angle $\\alpha \\approx 80^\\circ$ ensures continuous terminal accretion without alteration of form (*Eadem mutata resurgo*).",
    ),
    252: PlateSpec(
        svg_file="fig_golden_gnomon_spiral.svg",
        alt="Whirling-square golden rectangle subdivided into nested square gnomons with inscribed spiral (Fig. 252) alongside Euclid IV.10 36-72-72 golden triangle (Fig. 254).",
        caption="**Hero's Gnomons: Whirling-Square Golden Rectangle ($\\phi$) and Euclid IV.10 Golden Triangle (Ch. XI, Figs. 252 & 254, pp. 510–511).** Successive square gnomons and $108^\\circ$ triangular gnomons preserve exact geometric similarity around the spiral pole $O$.",
    ),
    325: PlateSpec(
        svg_file="fig_phyllotaxis_parastichy.svg",
        alt="Cylindrical Bravais-Tait parastichy lattice (Fig. 325) and planar apical capitulum displaying intersecting (8, 13) Fibonacci spirals at golden divergence 137.508 degrees.",
        caption="**Cylindrical and Apical Fibonacci Parastichy Lattices (Ch. XIV, Fig. 325, p. 644).** Overlapping $(m, n)$ contact helices on a cylindrical stem and $(8, 13)$ logarithmic parastichies on a discoidal capitulum at $\\Delta\\theta = 360^\\circ/\\phi^2$.",
    ),
    335: PlateSpec(
        svg_file="fig_culmann_femur_trajectories.svg",
        alt="Culmann's curved Fairbairn crane showing orthogonal principal compression and tension trajectories beside Meyer's cancellous trabecular arch system in the human femur (Fig. 335).",
        caption="**Culmann's Fairbairn Crane and Meyer's Orthogonal Trabecular Trajectories in the Human Femur (Ch. XVI, Fig. 335, p. 682).** Cancellous bone lamellae align along shear-free lines of principal compression (solid) and tension (dashed).",
    ),
    373: PlateSpec(
        svg_file="fig_transform_affine_shear.svg",
        alt="Rectangular Cartesian grid inscribing Argyropelecus Olfersi deformed by a 70-degree oblique affine shear into Sternoptyx diaphana (Figs. 373-374).",
        caption="**Coordinate Transformation I — Rectangular Grid to $70^\\circ$ Oblique Affine Shear (Ch. XVII, Figs. 373–374, p. 748).** Global shear $(x', y') = (x + y\\cos 70^\\circ, y\\sin 70^\\circ)$ maps *Argyropelecus Olfersi* into *Sternoptyx diaphana*.",
    ),
    381: PlateSpec(
        svg_file="fig_transform_coaxial_mesh.svg",
        alt="Orthogonal Cartesian grid inscribing Diodon transformed into a coaxial-hyperbolic curvilinear mesh yielding Orthagoriscus mola (Figs. 381-382).",
        caption="**Coordinate Transformation II — Rectangular Grid to Coaxial-Hyperbolic Mesh (Ch. XVII, Figs. 381–382, p. 751).** Mapping vertical lines into nested coaxial circles and horizontals into hyperbolae transforms *Diodon* into *Orthagoriscus mola*.",
    ),
}


def parse_endnotes_1917(lines: list[str]) -> dict[int, str]:
    """Parse all `[N]` authorial endnotes from lines 25408–28888 of the 1917 Gutenberg source."""
    notes_slice = "\n".join(lines[25407:28888])
    chunks = re.split(r"\n\s*\n", notes_slice.strip())
    notes: dict[int, str] = {}
    cur_num: int | None = None
    cur_parts: list[str] = []
    for chunk in chunks:
        stripped = chunk.strip()
        if not stripped:
            continue
        m = re.match(r"^\[(\d+)\]\s*(.*)$", stripped, flags=re.DOTALL)
        if m:
            if cur_num is not None:
                notes[cur_num] = " ".join(" ".join(cur_parts).split())
            cur_num = int(m.group(1))
            cur_parts = [m.group(2)]
        elif cur_num is not None:
            cur_parts.append(stripped)
    if cur_num is not None:
        notes[cur_num] = " ".join(" ".join(cur_parts).split())
    return notes


def _clean_script_token(tok: str) -> str:
    """Strip Gutenberg underscore markers inside superscript or subscript braces."""
    cleaned = tok.replace("_", "").strip()
    return cleaned.replace("`", "'")


def format_inline_1917(
    text: str,
    notes_map: dict[int, str],
    used_notes: list[int] | None = None,
    allow_footnotes: bool = True,
) -> str:
    """Convert Gutenberg inline markup (`_italics_`, `^{sup}`, `_{sub}`, `{page}`, `[fn]`) to clean RST."""
    # Normalize narrow non-breaking spaces / hair spaces to normal spaces so RST word boundaries behave cleanly
    s = text.replace("\u202f", " ").replace("\u200a", " ").replace("\u00a0", " ")
    # Escape any literal backslashes, asterisks, pipes, or backticks in raw text
    s = s.replace("\\", "\\\\").replace("*", "\\*").replace("`", "'").replace("|", "\\|")

    # Convert inline printed page numbers {123} or {vi} (NOT preceded by ^ or _)
    s = re.sub(
        r"(?<![^_])\{\s*(\d+|[ivxlcdm]+)\s*\}" if False else r"(?<![\^_])\{\s*(\d+|[ivxlcdm]+)\s*\}",
        r"[p. \1]",
        s,
    )

    # Handle _X_{sub}_ where subscript braces sit inside outer italic underscores
    s = re.sub(
        r"_([A-Za-z0-9′]+)_\{([^}]+)\}_",
        lambda m: f"\\ *{m.group(1)}*\\ :sub:`{_clean_script_token(m.group(2))}`\\ ",
        s,
    )
    # Handle remaining _{sub} and ^{sup}
    s = re.sub(
        r"_\{([^}]+)\}",
        lambda m: f"\\ :sub:`{_clean_script_token(m.group(1))}`\\ ",
        s,
    )
    s = re.sub(
        r"\^\{([^}]+)\}",
        lambda m: f"\\ :sup:`{_clean_script_token(m.group(1))}`\\ ",
        s,
    )
    s = re.sub(
        r"\^([0-9′+-]+|[a-zA-Z])",
        lambda m: f"\\ :sup:`{_clean_script_token(m.group(1))}`\\ ",
        s,
    )

    # Lift footnote markers like _Heading [110]._ outside italic delimiters so RST parses [#fn110]_
    s = re.sub(
        r"_([^_]+?)\s*\[(\d+)\]([.,;:!?]?)_",
        r"_\1_\3 [\2]",
        s,
    )

    # Convert _italic spans_ safely using escaped boundary spaces when needed
    def _italic_repl(match: re.Match[str]) -> str:
        inner = " ".join(match.group(1).split())
        if not inner:
            return ""
        return f"\\ *{inner}*\\ "

    s = re.sub(r"_([^_]+)_", _italic_repl, s)
    # Escape any residual unmatched underscore before inserting [#fnN]_ references
    s = s.replace("_", r"\_")
    # Convert authorial footnote references [123]
    if allow_footnotes:
        def _fn_repl(match: re.Match[str]) -> str:
            fnum = int(match.group(1))
            if fnum in notes_map:
                if used_notes is not None and fnum not in used_notes:
                    used_notes.append(fnum)
                return f" [#fn{fnum}]_\\ "
            return f"[{fnum}]"

        s = re.sub(r"\[(\d+)\]", _fn_repl, s)

    # Tidy redundant escaped spaces at start/end of line or around plain spaces
    s = re.sub(r"(^|\s)\\ \*", r"\1*", s)
    s = re.sub(r"\*\\ (\s|$|[.,;:!?)\]}”’—–-])", r"*\1", s)
    s = re.sub(r"`\\ (\s|$|[.,;:!?)\]}”’—–-])", r"`\1", s)
    s = re.sub(r"]_\\ (\s|$|[.,;:!?)\]}”’—–-])", r"]_\1", s)
    s = re.sub(r"(^|\s)\\ (:su[bp]:)", r"\1\2", s)
    # Prevent trailing backslash at very end of string
    s = re.sub(r"\\ $", "", s)
    return s


def render_chapter_slice_1917(
    lines: list[str],
    chapter_key: str,
    notes_map: dict[int, str],
    used_notes: list[int],
    injected_plates: set[int],
    include_heading: bool = True,
) -> str:
    """Render a verbatim chapter slice of the 1917 Cambridge edition into Sphinx RST."""
    start_1, end_1, heading_title, page_span = CHAPTER_STARTS_1917[chapter_key]
    raw_lines = lines[start_1 - 1 : end_1]

    out: list[str] = [
        f".. _thompson-1917-{chapter_key}:",
        "",
    ]
    if include_heading:
        out.extend(
            [
                heading_title,
                "-" * len(heading_title),
                "",
                f".. rubric:: 1917 Cambridge First Edition ({page_span})",
                "",
            ]
        )

    # Split into blank-line-separated paragraphs/blocks
    raw_block = "\n".join(raw_lines)
    paragraphs = re.split(r"\n\s*\n+", raw_block.strip())

    for idx, para in enumerate(paragraphs):
        p_strip = para.strip("\n")
        if not p_strip.strip():
            continue

        # Skip raw duplicate chapter header block at very top of slice (already rendered cleanly as RST section)
        if (
            idx < 3
            and chapter_key != "epigraphs"
            and re.match(
                r"^(PREFATORY NOTE|EPILOGUE\.|CHAPTER [IVXLC]+|[A-Z ,:()_'-]{5,120})$",
                " ".join(p_strip.split()),
            )
        ):
            continue

        # Standalone folio marker {123}
        m_folio = re.fullmatch(r"\s*\{\s*(\d+|[ivxlcdm]+)\s*\}\s*", p_strip)
        if m_folio:
            pg = m_folio.group(1)
            out.extend([f".. folio:: p. {pg}", f"   :page: {pg}", ""])
            continue

        # Horizontal thematic divider ――――――――――
        if re.fullmatch(r"\s*[―—-]{4,}\s*", p_strip):
            out.extend(["----", ""])
            continue

        # Illustration block: [Illustration] or [Illustration: Fig. N. ...]
        m_illus = re.fullmatch(r"\s*\[Illustration(?::\s*(.*))?\]\s*", p_strip, flags=re.DOTALL)
        if m_illus:
            cap_raw = m_illus.group(1)
            fig_nums = [int(n) for n in re.findall(r"Fig\.\s*(\d+)", cap_raw or "")]
            if cap_raw:
                cap_clean = format_inline_1917(
                    " ".join(cap_raw.splitlines()),
                    notes_map,
                    used_notes,
                )
                out.extend([".. admonition:: 1917 Source Illustration", "", f"   {cap_clean}", ""])
            for fnum in fig_nums:
                if fnum in PLATE_TRIGGERS and fnum not in injected_plates:
                    injected_plates.add(fnum)
                    spec = PLATE_TRIGGERS[fnum]
                    out.extend(
                        [
                            f".. picture:: /_static/figures/{spec.svg_file}",
                            f"   :alt: {spec.alt}",
                            f"   :caption: {spec.caption}",
                            "",
                        ]
                    )
            continue

        # Indented block (displayed equation, data table, wrap-around prose, or epigraph attribution)
        p_lines = p_strip.splitlines()
        if all(line.startswith(" ") for line in p_lines if line.strip()):
            has_columns = any(re.search(r"\S {3,}\S", line) for line in p_lines)
            max_line_len = max(len(line.strip()) for line in p_lines if line.strip())
            if has_columns and len(p_lines) >= 2:
                out.append("::")
                out.append("")
                for line in p_lines:
                    clean_tbl = line.replace("_", "").replace("\u202f", " ").replace("\u200a", " ")
                    out.append(f"   {clean_tbl.rstrip()}")
                out.append("")
            elif len(p_lines) >= 3 and max_line_len >= 56:
                joined_indented = " ".join(line.strip() for line in p_lines if line.strip())
                formatted_indented = format_inline_1917(joined_indented, notes_map, used_notes)
                out.extend([formatted_indented, ""])
            else:
                for line in p_lines:
                    formatted_line = format_inline_1917(line.strip(), notes_map, used_notes)
                    out.append(f"| {formatted_line}")
                out.append("")
            continue

        # Standard prose paragraph (unwrap internal line breaks cleanly)
        joined = " ".join(line.strip() for line in p_lines if line.strip())
        # Prevent accidental RST list/section markers if a paragraph starts with roman numeral or dash
        formatted = format_inline_1917(joined, notes_map, used_notes)
        out.extend([formatted, ""])

    return "\n".join(out)


def render_footnotes_section(used_notes: list[int], notes_map: dict[int, str]) -> str:
    """Render the `Authorial Endnotes (1917)` block for all `[#fnN]_` cited in a unit."""
    if not used_notes:
        return ""
    lines = [
        "Authorial Endnotes (1917 Edition)",
        "---------------------------------",
        "",
    ]
    for fnum in used_notes:
        raw_note = notes_map.get(fnum, "")
        formatted_note = format_inline_1917(raw_note, notes_map, allow_footnotes=False)
        lines.append(f".. [#fn{fnum}] **[Note {fnum}]** {formatted_note}")
        lines.append("")
    return "\n".join(lines)


def load_thompson_1917_lines(repo_root: Path) -> list[str]:
    """Read lines of `gutenberg_55264_thompson_1917.txt`."""
    src = repo_root / "resources" / "growth_and_form" / "sources" / "gutenberg_55264_thompson_1917.txt"
    return src.read_text(encoding="utf-8").splitlines()

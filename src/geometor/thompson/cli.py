"""Command-line interface for `geometor-thompson`."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from geometor.thompson.compile_codex import compile_codex
from geometor.thompson.concordance import (
    DEFAULT_REPO_ROOT,
    load_apparatus,
    verify_sources_manifest,
)


def build_parser() -> argparse.ArgumentParser:
    """Build the `geometor-thompson` argument parser."""
    parser = argparse.ArgumentParser(
        prog="geometor-thompson",
        description=(
            "Compile, verify, and query the GEOMETOR Digital Scriptorium edition of "
            "D'Arcy Wentworth Thompson's On Growth and Form (1917) & Jay Hambidge's Dynamic Symmetry (1920)."
        ),
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_REPO_ROOT,
        help="Path to the geometor/thompson repository root.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("compile", help="Compile all 26 Book Codex RST files into docsrc/growth_and_form/.")
    sub.add_parser("verify", help="Verify SHA-256 digests and byte lengths of 1917/1920 primary sources.")
    sub.add_parser("summary", help="Print an overview of apparatus counts and tracked editions.")

    p_conc = sub.add_parser("concordance", help="Query cross-repository concordance entries.")
    p_conc.add_argument("--unit", help="Filter by unit slug (e.g. unit-3-equiangular-spiral).")
    p_conc.add_argument("--repo", help="Filter by GEOMETOR sister repository (e.g. euclid, wildberger).")
    p_conc.add_argument("--search", help="Case-insensitive keyword search.")

    return parser


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for `geometor-thompson`."""
    parser = build_parser()
    args = parser.parse_args(argv)
    root: Path = args.root.resolve()

    if args.command == "compile":
        written = compile_codex(root)
        print(f"Compiled {len(written)} Book Codex RST files under {root / 'docsrc' / 'growth_and_form'}")
        return 0

    if args.command == "verify":
        results = verify_sources_manifest(root)
        print(json.dumps(results, indent=2))
        return 0

    apparatus = load_apparatus(root)
    if args.command == "summary":
        summary_data = {
            "title": apparatus.concordance_meta.get("title"),
            "concordance_entries": len(apparatus.entries),
            "persons": len(apparatus.persons),
            "citations": len(apparatus.citations),
            "glossary_terms": len(apparatus.glossary),
            "sources": len(apparatus.sources_manifest.get("sources", ())),
        }
        print(json.dumps(summary_data, indent=2))
        return 0

    if args.command == "concordance":
        entries = list(apparatus.entries)
        if args.unit:
            entries = [e for e in entries if e.unit == args.unit]
        if args.repo:
            entries = [
                e for e in entries if any(r.repo.lower() == args.repo.lower() for r in e.sister_refs)
            ]
        if args.search:
            matched_ids = {e.id for e in apparatus.search(args.search)}
            entries = [e for e in entries if e.id in matched_ids]
        for entry in entries:
            repos = ", ".join(sorted({r.repo for r in entry.sister_refs}))
            print(f"[{entry.id}] ({entry.unit}) {entry.topic} -> [{repos}]")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())

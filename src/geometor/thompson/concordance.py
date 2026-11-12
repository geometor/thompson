"""Structured loader, query engine, and SHA-256 validator for the Thompson–Hambidge Codex."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

DEFAULT_REPO_ROOT = Path(__file__).resolve().parents[3]


def apparatus_slug(key: str) -> str:
    """Compute the deterministic anchor slug matching `photon_platform.publish.roles.geometry`."""
    return re.sub(r"[^a-z0-9]+", "-", (key or "").lower()).strip("-")


@dataclass(frozen=True)
class SisterRef:
    """Cross-repository link from a Thompson/Hambidge locus to a GEOMETOR sister repository."""

    repo: str
    locus: str
    relation: str

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> SisterRef:
        """Construct a `SisterRef` from a parsed JSON dictionary."""
        return cls(
            repo=str(raw["repo"]),
            locus=str(raw["locus"]),
            relation=str(raw["relation"]),
        )


@dataclass(frozen=True)
class ConcordanceEntry:
    """Single cross-repository entry in the Thompson–Hambidge–GEOMETOR concordance."""

    id: str
    unit: str
    chapter: str
    pages_1917: str
    topic: str
    hambidge_parallels: tuple[str, ...]
    sister_refs: tuple[SisterRef, ...]
    invariants: tuple[str, ...]
    summary: str

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> ConcordanceEntry:
        """Construct a `ConcordanceEntry` from a parsed JSON dictionary."""
        return cls(
            id=str(raw["id"]),
            unit=str(raw["unit"]),
            chapter=str(raw["chapter"]),
            pages_1917=str(raw["pages_1917"]),
            topic=str(raw["topic"]),
            hambidge_parallels=tuple(str(x) for x in raw.get("hambidge_parallels", ())),
            sister_refs=tuple(SisterRef.from_dict(r) for r in raw.get("sister_refs", ())),
            invariants=tuple(str(x) for x in raw.get("invariants", ())),
            summary=str(raw.get("summary", "")),
        )


@dataclass(frozen=True)
class ThompsonApparatus:
    """Complete loaded scholarly apparatus for `geometor-thompson`."""

    concordance_meta: dict[str, Any]
    entries: tuple[ConcordanceEntry, ...]
    persons: dict[str, dict[str, Any]]
    glossary: dict[str, dict[str, Any]]
    citations: dict[str, dict[str, Any]]
    sources_manifest: dict[str, Any]

    def by_unit(self, unit_slug: str) -> list[ConcordanceEntry]:
        """Return all concordance entries belonging to `unit_slug` (e.g. `'unit-3-equiangular-spiral'`)."""
        return [entry for entry in self.entries if entry.unit == unit_slug]

    def by_repo(self, repo_name: str) -> list[ConcordanceEntry]:
        """Return concordance entries cross-referencing `repo_name` (e.g. `'euclid'`, `'wildberger'`)."""
        needle = repo_name.strip().lower()
        return [
            entry
            for entry in self.entries
            if any(ref.repo.lower() == needle for ref in entry.sister_refs)
        ]

    def search(self, query: str) -> list[ConcordanceEntry]:
        """Search concordance entries across topics, summaries, invariants, Hambidge parallels, and sister refs."""
        needle = query.lower()
        matched: list[ConcordanceEntry] = []
        for entry in self.entries:
            haystack = " ".join(
                [
                    entry.id,
                    entry.unit,
                    entry.chapter,
                    entry.topic,
                    entry.summary,
                    *entry.invariants,
                    *entry.hambidge_parallels,
                    *(f"{r.repo} {r.locus} {r.relation}" for r in entry.sister_refs),
                ]
            ).lower()
            if needle in haystack:
                matched.append(entry)
        return matched


def load_apparatus(repo_root: Path | None = None) -> ThompsonApparatus:
    """Load the structured JSON registries from `resources/growth_and_form/`."""
    root = (repo_root or DEFAULT_REPO_ROOT).resolve()
    res_dir = root / "resources" / "growth_and_form"
    conc_raw = json.loads((res_dir / "concordance.json").read_text(encoding="utf-8"))
    persons = json.loads((res_dir / "persons.json").read_text(encoding="utf-8"))
    glossary = json.loads((res_dir / "glossary.json").read_text(encoding="utf-8"))
    citations = json.loads((res_dir / "citations.json").read_text(encoding="utf-8"))
    manifest = json.loads((res_dir / "sources_manifest.json").read_text(encoding="utf-8"))
    entries = tuple(ConcordanceEntry.from_dict(item) for item in conc_raw.get("entries", ()))
    return ThompsonApparatus(
        concordance_meta=dict(conc_raw.get("metadata", {})),
        entries=entries,
        persons=persons,
        glossary=glossary,
        citations=citations,
        sources_manifest=manifest,
    )


def verify_sources_manifest(repo_root: Path | None = None) -> list[dict[str, Any]]:
    """Verify SHA-256 digests and byte lengths for all tracked 1917/1920 primary sources."""
    root = (repo_root or DEFAULT_REPO_ROOT).resolve()
    manifest_path = root / "resources" / "growth_and_form" / "sources_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    results: list[dict[str, Any]] = []
    for src in manifest.get("sources", ()):
        fpath = root / src["filename"]
        if not fpath.is_file():
            msg = f"Missing primary source file: {fpath}"
            raise FileNotFoundError(msg)
        data = fpath.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        size = len(data)
        if digest != src["sha256"]:
            msg = f"SHA-256 mismatch for {src['id']}: expected {src['sha256']}, got {digest}"
            raise ValueError(msg)
        if size != src["bytes"]:
            msg = f"Byte-size mismatch for {src['id']}: expected {src['bytes']}, got {size}"
            raise ValueError(msg)
        results.append(
            {
                "id": src["id"],
                "filename": src["filename"],
                "year": src["year"],
                "bytes": size,
                "sha256": digest,
                "verified": True,
            }
        )
    return results

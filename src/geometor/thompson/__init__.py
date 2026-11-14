"""GEOMETOR Digital Scriptorium edition of D'Arcy Wentworth Thompson's On Growth and Form (1917).

Paired with a Dynamic Symmetry & Gnomonic Morphology Concordance to Jay Hambidge's
The Elements of Dynamic Symmetry (Yale University Press, 1919–1920).
"""

from __future__ import annotations

from geometor.thompson.compile_codex import compile_codex
from geometor.thompson.concordance import (
    ConcordanceEntry,
    SisterRef,
    ThompsonApparatus,
    apparatus_slug,
    load_apparatus,
    verify_sources_manifest,
)

__version__ = "0.1.1"

__all__ = [
    "ConcordanceEntry",
    "SisterRef",
    "ThompsonApparatus",
    "__version__",
    "apparatus_slug",
    "compile_codex",
    "load_apparatus",
    "verify_sources_manifest",
]

"""Sphinx configuration for GEOMETOR • thompson."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _REPO_ROOT.parent
if str(_REPO_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT / "src"))

from photon_platform.publish.global_conf import *

import geometor.thompson as module

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "thompson"
repo_name = "thompson"

setup_globals(org, org_name, repo, repo_name)

site_title = "Sir D'Arcy Wentworth Thompson"
project = site_title
html_title = f"{site_title} • {org_name}"
author = "Sir D'Arcy Wentworth Thompson · Digital Edition GEOMETOR"
copyright = "1917 Cambridge University Press · Digital Codex GEOMETOR"

html_static_path = ["_static"]

# Restrict AutoAPI strictly to `src/geometor` and avoid duplicate root index / imported-member collisions
autoapi_dirs = [str(_REPO_ROOT / "src" / "geometor")]
autoapi_add_toctree_entry = False
autoapi_options = [opt for opt in autoapi_options if opt != "imported-members"]
if "modules/api/geometor/thompson/index.rst" not in exclude_patterns:
    exclude_patterns.append("modules/api/geometor/thompson/index.rst")

# Retain only locally cached intersphinx inventories so offline sandbox builds emit zero network warnings
intersphinx_mapping = {
    name: target
    for name, target in intersphinx_mapping.items()
    if isinstance(target, tuple) and len(target) == 2 and target[1] is not None
}

for _sister_repo in (
    "euclid",
    "elements",
    "aristotle",
    "pacioli",
    "pappus",
    "divine",
    "etc",
    "wildberger",
    "phyllotaxis",
    "hilbert",
    "hambidge",
):
    _local_inv = (_WORKSPACE_ROOT / _sister_repo / "docs" / "objects.inv").resolve()
    if _local_inv.is_file():
        intersphinx_mapping[_sister_repo] = (
            f"https://geometor.github.io/{_sister_repo}",
            (str(_local_inv), None),
        )

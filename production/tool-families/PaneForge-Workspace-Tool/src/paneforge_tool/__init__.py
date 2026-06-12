"""PaneForge workspace tool.

Wraps the PaneForge-Stick product (Event Law calendar kernel + PWA +
vendored lib-forge ring) as an installable workspace CLI.

Product resolution order:
  1. PANEFORGE_PRODUCT env var
  2. vendored copy inside this package (_product/)
  3. repo-relative: ../../products/PaneForge-Stick (tool-families placement)
  4. known workspace roots (git-hosted-roots, local CQECMPLX-Production)
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

__version__ = "0.1.0"

_PKG_DIR = Path(__file__).resolve().parent

_KNOWN_ROOTS = [
    Path("D:/CQE_CMPLX/git-hosted-roots/CQECMPLX-Production/production/products/PaneForge-Stick"),
    Path("D:/CQE_CMPLX/CQECMPLX-Production/production/products/PaneForge-Stick"),
]


def _is_product(p: Path) -> bool:
    return (p / "kernel" / "paneforge_kernel.py").is_file() and (p / "app" / "index.html").is_file()


def product_root() -> Optional[Path]:
    """Resolve the PaneForge-Stick product root."""
    env = os.environ.get("PANEFORGE_PRODUCT")
    if env and _is_product(Path(env)):
        return Path(env).resolve()
    vendored = _PKG_DIR / "_product"
    if _is_product(vendored):
        return vendored
    # tool living inside the production repo at production/tool-families/<tool>/
    for ancestor in _PKG_DIR.parents:
        repo_rel = ancestor / "products" / "PaneForge-Stick"
        if _is_product(repo_rel):
            return repo_rel.resolve()
    for c in _KNOWN_ROOTS:
        if _is_product(c):
            return c
    return None


def data_dir() -> Path:
    """Receipts/crystals live outside the package: env wins, else ~/.paneforge."""
    env = os.environ.get("PANEFORGE_DATA")
    if env:
        return Path(env)
    return Path.home() / ".paneforge"

from __future__ import annotations

import csv
import os
from pathlib import Path
from typing import Any


class KernelExplorer:
    """Read-only browser for proofs, repo forms, and package manifests."""

    def __init__(self, kernel_root: str | Path | None = None) -> None:
        self.kernel_root = Path(kernel_root or Path(__file__).resolve().parent.parent)
        self.proof_root = Path(os.environ.get("CMPLX_PROOF_ROOT", "D:/CQE_CMPLX/git-hosted-roots/CQECMPLX-Production/proofing"))
        self.package_root = Path(os.environ.get("CMPLX_PACKAGE_ROOT", "D:/CMPLX-Kernel/CMPLX-Kernel_Production_20260607T223706"))

    def proof_index(self) -> dict[str, Any]:
        docs = []
        if self.proof_root.exists():
            for path in self.proof_root.rglob("*.md"):
                docs.append({"path": str(path), "relative_path": str(path.relative_to(self.proof_root)), "bytes": path.stat().st_size})
        return {"proof_root": str(self.proof_root), "exists": self.proof_root.exists(), "docs": sorted(docs, key=lambda item: item["relative_path"])}

    def repo_forms(self) -> dict[str, Any]:
        forms_root = self.kernel_root / "repo_forms" / "repos"
        repos = []
        if forms_root.exists():
            for form_json in forms_root.glob("*/FORM.json"):
                repos.append({"repo": form_json.parent.name, "form": str(form_json), "bytes": form_json.stat().st_size})
        return {"forms_root": str(forms_root), "exists": forms_root.exists(), "repos": sorted(repos, key=lambda item: item["repo"].lower())}

    def package_manifest(self, limit: int = 200) -> dict[str, Any]:
        manifest = self.package_root / "PACKAGE_MANIFEST.csv"
        rows = []
        if manifest.exists():
            with manifest.open("r", encoding="utf-8-sig", newline="") as handle:
                reader = csv.DictReader(handle)
                for idx, row in enumerate(reader):
                    if idx >= limit:
                        break
                    rows.append(row)
        return {
            "package_root": str(self.package_root),
            "manifest": str(manifest),
            "exists": manifest.exists(),
            "rows": rows,
        }

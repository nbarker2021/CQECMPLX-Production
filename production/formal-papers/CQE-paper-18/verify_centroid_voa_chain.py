#!/usr/bin/env python3
"""Reapplication verifier: the centroid / VOA sector chain, bound into
CQE Paper 18 (VOA moonshine routes).

Recorded PROVEN in CMPLX-R30-main/PROOF/theorems with verifiers in
lattice_forge/centroid_voa.py, vendored in the production substrate. Paper 18
already carries the VOA moonshine routes; this binds the substrate's own
centroid/VOA verifiers as the proven base under that paper.

Theorems reapplied (each runs its substrate verifier):
  - the centroid -> VOA chain
  - VOA sector decomposition (weight-0 vacua / weight-5 excited; Z(q)=2q^0+6q^5)
  - gluon invariance
  - Hamming-centroid universality (the universality of the centroid readout)
  - the Z4 period template

These underpin EntropyForge / SentinelForge (the VOA partition Z(q)=2q^0+6q^5)
and ChromaForge (the conservation sectors). Nothing here is new mathematics;
it is the reapplication of proven verifiers to the obligation that the
substrate's own centroid/VOA chain was never paper-bound.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE_SRC = _HERE.parents[1] / "packages" / "cqecmplx-forge" / "src"
if str(_FORGE_SRC) not in sys.path:
    sys.path.insert(0, str(_FORGE_SRC))

from lattice_forge import centroid_voa as cv  # noqa: E402


def _ok(r) -> bool:
    return (r.get("status") if isinstance(r, dict) else r) == "pass"


def main() -> int:
    results = {
        "centroid_voa_chain": cv.verify_centroid_voa_chain(),
        "voa_sector_decomposition": cv.verify_voa_sector_decomposition(),
        "gluon_invariance": cv.verify_gluon_invariance(),
        "hamming_centroid_universality": cv.verify_hamming_centroid_universality(),
        "z4_period_template": cv.verify_z4_period_template(),
    }
    checks = {name: _ok(r) for name, r in results.items()}
    status = "pass" if all(checks.values()) else "fail"
    receipt = {
        "paper": "CQE-paper-18",
        "theorem": "Centroid / VOA sector chain: VOA partition Z(q)=2q^0+6q^5 "
                   "(2 vacua weight-0, 6 excited weight-5), gluon invariance, "
                   "Hamming-centroid universality, Z4 period template",
        "forge": "lattice_forge.centroid_voa (reapplied)",
        "reapplication": True,
        "closes": "paper-binding gap for the substrate centroid/VOA verifiers "
                  "(PROVEN, lattice_forge/centroid_voa.py)",
        "ties_to": "EntropyForge + SentinelForge (VOA partition, p12/p02), "
                   "ChromaForge conservation sectors (p09)",
        "source_module": "lattice_forge/centroid_voa.py",
        "status": status,
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
    }
    out = _HERE / "centroid_voa_chain_receipt.json"
    out.write_text(json.dumps(receipt, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps({"status": status, "passed": receipt["passed"],
                      "total": receipt["total"], "receipt": str(out)}, indent=2))
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

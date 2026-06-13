#!/usr/bin/env python3
"""Reapplication verifier: the oloid carrier family, bound into CQE Paper 05
(Oloid Path Carrier).

Recorded PROVEN in CMPLX-R30-main/PROOF/theorems with verifiers across
lattice_forge oloid modules, vendored in the production substrate, bound to no
production paper (paper 05's own verifier covers the path-carrier; this binds
the substrate's oloid mechanism verifiers as its proven base).

Theorems reapplied (each runs its substrate verifier):
  - oloid rolling (the rolling contact kinematics)
  - octonionic oloid (the single-oloid octonion grounding)
  - quad oloid (the four-oloid D4 ring)
  - dual-path oloid (read-then-verify consistency flow)

Honest note: oloid_model_selection returns `pass_with_open_bridge` — the
E6 -> E7 -> E8 dyadic lift (obligation O2''') is the open part. It is NOT
claimed closed here; only the four mechanism verifiers above are bound.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE_SRC = _HERE.parents[1] / "packages" / "cqecmplx-forge" / "src"
if str(_FORGE_SRC) not in sys.path:
    sys.path.insert(0, str(_FORGE_SRC))

from lattice_forge import oloid_rolling, oloid_octonionic, quad_oloid, oloid_dual_path  # noqa: E402


def _ok(r) -> bool:
    return (r.get("status") if isinstance(r, dict) else r) == "pass"


def main() -> int:
    results = {
        "oloid_rolling": oloid_rolling.verify_oloid_rolling(),
        "octonionic_oloid": oloid_octonionic.verify_octonionic_oloid(),
        "quad_oloid": quad_oloid.verify_quad_oloid(),
        "dual_path_oloid": oloid_dual_path.verify_dual_path_oloid(),
    }
    checks = {name: _ok(r) for name, r in results.items()}
    status = "pass" if all(checks.values()) else "fail"
    receipt = {
        "paper": "CQE-paper-05",
        "theorem": "Oloid carrier family: rolling-contact kinematics, "
                   "octonionic grounding, four-oloid D4 ring, dual-path "
                   "read-then-verify flow",
        "forge": "lattice_forge oloid modules (reapplied)",
        "reapplication": True,
        "closes": "paper-binding gap for the substrate oloid mechanism "
                  "verifiers (PROVEN, lattice_forge/oloid_*.py)",
        "source_modules": ["oloid_rolling", "oloid_octonionic", "quad_oloid",
                           "oloid_dual_path"],
        "status": status,
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "still_open": "the E6->E7->E8 dyadic lift (O2''') — oloid_model_selection "
                      "returns pass_with_open_bridge; NOT claimed here",
    }
    out = _HERE / "oloid_carrier_family_receipt.json"
    out.write_text(json.dumps(receipt, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps({"status": status, "passed": receipt["passed"],
                      "total": receipt["total"], "receipt": str(out)}, indent=2))
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

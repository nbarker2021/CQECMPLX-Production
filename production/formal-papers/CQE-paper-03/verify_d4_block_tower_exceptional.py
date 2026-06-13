#!/usr/bin/env python3
"""Reapplication verifier: the D4 block tower and the G2->F4 exceptional
conjugate, bound into CQE Paper 03 (D4 / J3 triality surface).

Recorded PROVEN in CMPLX-R30-main/PROOF/theorems with verifiers in
lattice_forge/{block_tower,block_d4,g2_f4_t5_conjugate}.py, vendored, bound to
no production paper. These extend paper 03's triality surface upward into the
exceptional Lie tower (G2 -> F4) and the D4 block-tower structure.

Theorems reapplied (each runs its substrate verifier):
  - D4 block (the 8-state D4 chart block)
  - D4 block tower (the tower of D4 blocks)
  - G2 -> F4 T5 conjugate triple (the exceptional Lie conjugation)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE_SRC = _HERE.parents[1] / "packages" / "cqecmplx-forge" / "src"
if str(_FORGE_SRC) not in sys.path:
    sys.path.insert(0, str(_FORGE_SRC))

from lattice_forge import block_d4, block_tower, g2_f4_t5_conjugate  # noqa: E402


def _ok(r) -> bool:
    return (r.get("status") if isinstance(r, dict) else r) == "pass"


def main() -> int:
    results = {
        "d4_block": block_d4.verify_d4_block(),
        "block_tower": block_tower.verify_block_tower(),
        "g2_f4_t5_conjugate_triple": g2_f4_t5_conjugate.verify_conjugate_triple(),
    }
    checks = {name: _ok(r) for name, r in results.items()}
    status = "pass" if all(checks.values()) else "fail"
    receipt = {
        "paper": "CQE-paper-03",
        "theorem": "D4 block tower + G2->F4 exceptional conjugate: the D4 chart "
                   "block, its tower, and the G2->F4 T5 conjugate triple",
        "forge": "lattice_forge.{block_d4,block_tower,g2_f4_t5_conjugate} (reapplied)",
        "reapplication": True,
        "closes": "paper-binding gap for the D4 block tower and exceptional "
                  "conjugate verifiers (PROVEN, bound to no paper)",
        "source_modules": ["block_d4", "block_tower", "g2_f4_t5_conjugate"],
        "status": status,
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
    }
    out = _HERE / "d4_block_tower_exceptional_receipt.json"
    out.write_text(json.dumps(receipt, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps({"status": status, "passed": receipt["passed"],
                      "total": receipt["total"], "receipt": str(out)}, indent=2))
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

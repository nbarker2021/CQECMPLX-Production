#!/usr/bin/env python3
"""Finite verifier binding LeechForge to CQE Paper 17 (Error Correction Tower).

The tower is realized literally: the extended binary Golay code [24,12,8]
(a Steiner S(5,8,24) system) lifts to a 24-dimensional even lattice whose
196,560 minimal vectors are constructed and membership-checked exactly —
the code is the lower local root, the lattice is the larger closure frame.

Checks (all finite):
  1. The generator basis spans exactly 4096 distinct codewords.
  2. Weight enumerator is exactly 1, 759@8, 2576@12, 759@16, 1@24.
  3. The code is self-dual with minimum distance 8.
  4. Steiner S(5,8,24): every 5-subset lies in exactly one octad
     (759 * C(8,5) = C(24,5) = 42,504, no collisions).
  5. The three minimal-vector shapes count 1,104 + 97,152 + 98,304 =
     196,560 — all distinct, all norm^2 4, all lattice members.
  6. Minimal vectors close under negation.
  7. Sums of minimal vectors stay in the lattice with even norms
     (deterministic sample).
  8. No vector of norm^2 = 2 exists (exhaustive case analysis).
  9. Tower consistency: 196,560 = 240 * 819; E8Forge computes the 240.
 10. The CMPLX VERIFICATION_REPORT constants (240, 696729600, 196560)
     are reproduced by computation, not citation.

Identification of the constructed lattice with THE Leech lattice rests on
the uniqueness theorem for even unimodular lattices of minimum norm 4 in
dimension 24 — cited mathematics, recorded as an obligation, NOT claimed.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE_SRC = _HERE.parents[1] / "packages" / "cqecmplx-forge" / "src"
if str(_FORGE_SRC) not in sys.path:
    sys.path.insert(0, str(_FORGE_SRC))

import LeechForge  # noqa: E402


def main() -> int:
    result = LeechForge.verify()
    receipt = {
        "paper": "CQE-paper-17",
        "theorem": "Golay -> Leech tower: [24,12,8] Steiner code lifts to a "
                   "24D even lattice with 196,560 minimal vectors of norm 4, "
                   "all constructed and membership-verified",
        "forge": "LeechForge",
        "source_repo": "nbarker2021/CMPLX (VERIFICATION_REPORT.md constants), "
                       "tower below: nbarker2021/CMPLXUNI via E8Forge",
        "adjudicated_divergence": [
            "CMPLX VERIFICATION_REPORT records E8 roots 240, Weyl 696729600, "
            "Leech kissing 196560 as asserted constants; LeechForge computes "
            "the Golay code, the Steiner property, and all 196,560 vectors "
            "from scratch in exact integer arithmetic",
            "Golay B-matrix convention fixed during formalization: the "
            "bordered QR(11) circulant requires the NON-residue convention; "
            "the residue convention yields a non-Golay [24,12] code "
            "(weight enumerator check caught it)",
        ],
        "status": result["status"],
        "checks": result["checks"],
        "passed": result["passed"],
        "total": result["total"],
        "open_obligations": [
            "Identification with THE Leech lattice is by the uniqueness "
            "theorem (even unimodular, dim 24, min norm 4) — cited, not "
            "verified; a Gram/unimodularity receipt is future work.",
            "Closure is sampled, not exhaustive (196560^2 pairs).",
            "Kissing optimality in 24D (Cohn-Kumar-Miller-Radchenko-"
            "Viazovska) is cited mathematics, not claimed.",
        ],
    }
    out = _HERE / "golay_leech_tower_receipt.json"
    out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": receipt["status"],
                      "passed": receipt["passed"],
                      "total": receipt["total"],
                      "receipt": str(out)}, indent=2))
    return 0 if receipt["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

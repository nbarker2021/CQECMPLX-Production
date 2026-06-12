#!/usr/bin/env python3
"""Finite verifier binding E8Forge to CQE Paper 08 (Lattice Closure).

E8 is the even unimodular closure frame in 8 dimensions. All claims are
verified exactly in doubled integer coordinates (u = 2v): membership is
"u all even or all odd, sum(u) == 0 mod 4"; no floats, no numpy.

Checks (all finite):
  1. Exactly 240 roots, split 112 integer + 128 half-integer, no duplicates.
  2. Every root is an E8 member of norm^2 = 2.
  3. Half-integer roots have an even number of minus signs.
  4. |W(E8)| = 696,729,600 = 4!*6!*8! = 2^14 * 3^5 * 5^2 * 7.
  5. Root inner products lie in {-2,-1,0,1,2}; -2 only at antipodes.
  6. The lattice closes under root addition (all 240^2 pairs).
  7. Pair sums are even vectors with norm^2 in {0,2,4,6,8}.
  8. The minimum norm^2 is 2 (no E8 vector of norm^2 = 1; exhaustive).
  9. An algorithmically derived simple system of 8 roots has Cartan
     diagonal 2, off-diagonal in {0,-1}, determinant 1, and degree
     sequence [1,1,1,2,2,2,2,3] — the E8 Dynkin diagram.
 10. Adjudication: the CMPLXUNI lfai surrogate (constructionA_E8_check)
     rejects every one of the 112 integer roots, so it is not E8
     membership; E8Forge replaces it with the exact test.

Source repo: github.com/nbarker2021/CMPLXUNI (local clone D:\CQE_CMPLX\g\CMPLXUNI).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE_SRC = _HERE.parents[1] / "packages" / "cqecmplx-forge" / "src"
if str(_FORGE_SRC) not in sys.path:
    sys.path.insert(0, str(_FORGE_SRC))

import E8Forge  # noqa: E402


def main() -> int:
    result = E8Forge.verify()
    receipt = {
        "paper": "CQE-paper-08",
        "theorem": "E8 even lattice closure: 240 roots (112+128), closure "
                   "under root addition, minimum norm 2, E8 Cartan system, "
                   "Weyl order 4!*6!*8!",
        "forge": "E8Forge",
        "source_repo": "nbarker2021/CMPLXUNI (lfai/cona_e8.py, src/cmplx/lattice/e8.py)",
        "adjudicated_divergence": [
            "lfai surrogate constructionA_E8_check provably misclassifies: "
            "its mod-8 condition rejects all 112 integer roots and its "
            "integer-only API cannot represent the 128 half-integer roots; "
            "replaced by exact membership in doubled coordinates",
            "src/cmplx/lattice/e8.py structure retained but made stdlib-exact "
            "(no numpy, no float norms)",
            "lfai/ledger_merkle.py hash chain is sound but hardcodes a POSIX "
            "path; ledger receipts remain ChromaForge territory",
        ],
        "status": result["status"],
        "checks": result["checks"],
        "passed": result["passed"],
        "total": result["total"],
        "open_obligations": [
            "Weyl group order is verified as arithmetic identity, not by "
            "group enumeration; a chamber-counting receipt is future work.",
            "Unimodularity (det Gram = 1 for a lattice basis) is implied by "
            "the simple-system Cartan determinant but deserves its own "
            "basis-level receipt.",
            "Leech-lattice constants in CMPLX (kissing 196560) are a "
            "separate candidate through the same pattern.",
        ],
    }
    out = _HERE / "e8_even_lattice_receipt.json"
    out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": receipt["status"],
                      "passed": receipt["passed"],
                      "total": receipt["total"],
                      "receipt": str(out)}, indent=2))
    return 0 if receipt["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

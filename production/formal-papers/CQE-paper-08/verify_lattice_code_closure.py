#!/usr/bin/env python3
"""Finite verifier binding AuthenticaForge to CQE Paper 08 (Lattice Closure).

The 5-term code lattice [1, 3, 7, 21, 137] closes: product 441, sum
578 = 2 * 17^2, digital root 2. A code is lattice-closed when
d1*d2*d3*d4 + d5 == 0 (mod 17) and DR(sum) == 2, which by CRT is exactly
sum == 119 (mod 153). The binding digit construction realizes closure for
every digit combination, and closure is what verification checks.

Checks (all finite):
  1. The lattice constants close (441, 578 = 2*17^2, DR 2, 0 mod 17).
  2. The digital-root closed form matches iterated digit sums on 1..10000.
  3. CRT: the residue system has the unique solution 119 in [0, 153).
  4. Every valid sum 119 + 153m has digital root 2 (m in 0..999).
  5. The binding digit closes the lattice for all 6561 digit combinations.
  6. Any d5 perturbation by 1..16 breaks the mod-17 identity.
  7. Structural finding: the check digit is constant 2 for every valid
     code — it is NOT an independent check (corrects the source product's
     three-independent-checks claim).
  8. Generation is deterministic; 500 distinct sequences give 500 codes.
  9. The QR payload round-trips (corrects a latent source bug: fixed
     3-digit field slicing corrupted codes with 4+ digit d5).
 10. End-to-end: offline verify and HMAC gate behave; a wrong HMAC fails.

Anti-counterfeit strength claims beyond these finite facts (e.g. forgery
cost) are NOT claimed: anyone knowing the public identity can mint closed
codes; unforgeability rests entirely on the HMAC layer.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE_SRC = _HERE.parents[1] / "packages" / "cqecmplx-forge" / "src"
if str(_FORGE_SRC) not in sys.path:
    sys.path.insert(0, str(_FORGE_SRC))

import AuthenticaForge  # noqa: E402


def main() -> int:
    result = AuthenticaForge.verify()
    receipt = {
        "paper": "CQE-paper-08",
        "theorem": "Lattice code closure: 5-term lattice [1,3,7,21,137], "
                   "CRT residue 119 mod 153, binding digit realizes closure "
                   "for all digit combinations",
        "forge": "AuthenticaForge",
        "source_product": "historical_pastworks/product_authentica (core distilled)",
        "adjudicated_divergence": [
            "global mutable sequence counter removed; sequence is an explicit "
            "parameter (Event Law determinism)",
            "check digit shown to be constant 2 for all valid codes — the "
            "product counted it as a third independent check; it is not",
            "QR codec rewritten: source assumed 3-digit fields while d5 is "
            "unbounded, corrupting round-trips for 4+ digit d5",
            "FastAPI/SDK layers stay product-side",
        ],
        "status": result["status"],
        "checks": result["checks"],
        "passed": result["passed"],
        "total": result["total"],
        "open_obligations": [
            "Forgery-cost claims are NOT bound: lattice closure is public "
            "math; unforgeability rests on the HMAC layer alone.",
            "Slot lineage decoding (digital-root slot labels) needs its own "
            "receipt before claim binding.",
        ],
    }
    out = _HERE / "lattice_code_closure_receipt.json"
    out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": receipt["status"],
                      "passed": receipt["passed"],
                      "total": receipt["total"],
                      "receipt": str(out)}, indent=2))
    return 0 if receipt["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

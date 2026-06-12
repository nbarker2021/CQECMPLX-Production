#!/usr/bin/env python3
"""Finite verifier binding EntropyForge to CQE Paper 12 (CA Prediction Surface).

The paper-bound object is the canonical single-cell Rule 30 center column.
EntropyForge carries the product surface (seeded blocks, VOA syndromes); this
verifier replays the forge's 10 finite checks from the paper space and emits
the receipt beside the paper's own prediction-surface receipt.

Checks (all finite):
  1. Rule 30 formula L^(C|R) matches Wolfram code 30 on all 8 states.
  2. VOA weights over the 8 chart states are exactly Z(q) = 2q^0 + 6q^5.
  3. Monster scalar 196883 = 47 * 59 * 71.
  4. D4 antipodal labeling partitions the 8 states into 4 complement pairs.
  5. Two independent Rule 30 implementations agree on 512 center bits.
  6. No period p <= 256 in the first 2048 canonical center bits.
  7. XOR-debiased canonical stream density within 5% of 1/2.
  8. VOA syndrome is deterministic and window-sensitive.
  9. Distinct seeds separate streams; identical seeds repeat them.
 10. Entropy block round-trips and verifies client-side.

Check 6 is the finite, falsifiable form of the non-periodicity claim. The
infinite-column statement remains an open conjecture and is NOT claimed here;
it stays an obligation in the Paper 12 ledger.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE_SRC = _HERE.parents[1] / "packages" / "cqecmplx-forge" / "src"
if str(_FORGE_SRC) not in sys.path:
    sys.path.insert(0, str(_FORGE_SRC))

import EntropyForge  # noqa: E402


def main() -> int:
    result = EntropyForge.verify()
    receipt = {
        "paper": "CQE-paper-12",
        "theorem": "Center-column entropy extension: canonical Rule 30 column, "
                   "VOA partition Z(q)=2q^0+6q^5, finite non-periodicity window",
        "forge": "EntropyForge",
        "source_product": "historical_pastworks/product_entropy (core distilled)",
        "adjudicated_divergence": "product seeded only the syndrome chain; "
                                  "forge seeds the CA initial window itself; "
                                  "canonical single-cell mode preserved as the "
                                  "paper-bound object",
        "status": result["status"],
        "checks": result["checks"],
        "passed": result["passed"],
        "total": result["total"],
        "open_obligations": [
            "Infinite-column non-periodicity remains a conjecture; only the "
            "finite window (no period <= 256 within 2048 bits) is claimed.",
            "Statistical suite (NIST SP 800-22 style) for the seeded stream "
            "is product-layer work, not a paper claim.",
        ],
    }
    out = _HERE / "center_column_entropy_receipt.json"
    out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": receipt["status"],
                      "passed": receipt["passed"],
                      "total": receipt["total"],
                      "receipt": str(out)}, indent=2))
    return 0 if receipt["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

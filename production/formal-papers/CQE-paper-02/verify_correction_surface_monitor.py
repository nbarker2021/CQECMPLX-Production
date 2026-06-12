#!/usr/bin/env python3
"""Finite verifier binding SentinelForge to CQE Paper 02 (Correction Surface).

A sentinel alert is a correction-surface receipt: a measured deviation from
the VOA partition law over the 8 LCR triads, logged with an exact two-tailed
binomial proof rather than dismissed (Axiom 00.3, Boundary Positivity).

Checks (all finite):
  1. The 8 triads partition 2/2/4: deep invariants {000,111}, level-1
     invariants {010,101}, variable {001,011,100,110}.
  2. Lie conjugates (L=R) are exactly deep union level-1.
  3. rule30 = rule90 XOR correction on all 8 states.
  4. The correction bit C AND (NOT R) fires on exactly 2 of 8 states.
  5. Geometry levels 0/1/2 partition as 2/2/4.
  6. Bonded frames are the cyclic rotations plus the LR mirror; the
     antipodal frame is an involution.
  7. An exactly balanced stream yields ratio 0.25, sigma 0, severity nominal.
  8. A frozen all-vacuum stream is an emergency with p < 1e-9.
  9. The exact binomial machinery: total mass 1, p = 1 at the mean.
 10. The severity ladder is monotone in sigma.

The detection-quality claims of the product (false-positive rates against
real infrastructure telemetry) are NOT claimed here; they remain product
obligations. Only the finite partition and proof machinery is bound.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE_SRC = _HERE.parents[1] / "packages" / "cqecmplx-forge" / "src"
if str(_FORGE_SRC) not in sys.path:
    sys.path.insert(0, str(_FORGE_SRC))

import SentinelForge  # noqa: E402


def main() -> int:
    result = SentinelForge.verify()
    receipt = {
        "paper": "CQE-paper-02",
        "theorem": "Correction-surface monitor: 2/2/4 triad partition law, "
                   "rule30 = rule90 XOR correction, exact binomial deviation proofs",
        "forge": "SentinelForge",
        "source_product": "historical_pastworks/product_sentinel (core distilled)",
        "adjudicated_divergence": [
            "product used a normal approximation for n > 100; forge computes "
            "the exact two-tailed binomial tail with math.comb for every n",
            "async/API/agent layers stay product-side; only the proven "
            "monitoring core enters the forge ring",
        ],
        "status": result["status"],
        "checks": result["checks"],
        "passed": result["passed"],
        "total": result["total"],
        "open_obligations": [
            "Detection-quality claims (false-positive rates on real telemetry) "
            "are product-layer empirical work, not paper claims.",
            "Quantization of continuous metrics into triads needs its own "
            "receipt before metric fingerprints can be claim-bound.",
        ],
    }
    out = _HERE / "correction_surface_monitor_receipt.json"
    out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": receipt["status"],
                      "passed": receipt["passed"],
                      "total": receipt["total"],
                      "receipt": str(out)}, indent=2))
    return 0 if receipt["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Finite verifier binding MDHGForge to CQE Paper 07 (Discrete-Continuous Bridge).

The MDHG cache IS the bridge: a continuous 24D vector (Leech dimension) is
quantized onto a discrete bin lattice, then double-hashed to a 2D slot on a
torus. The SpeedLight idempotence law f(f(x)) = f(x) — re-admitting the same
content is a pure hit with no growth — makes the bridge a well-defined
retraction from the continuum onto the discrete address space.

Checks (all finite):
  1. The bridge dimension is the Leech dimension 24.
  2. Quantize is total on all reals and lands in [0, bins).
  3. Quantize is an idempotent retraction (re-quantizing bin centers is fixed).
  4. Slot assignment is deterministic and lands on the grid torus.
  5. SpeedLight idempotence: re-admitting the same content is a hit with
     distance 0 and no admission growth (f(f(x)) = f(x)).
  6. Per-slot capacity is never exceeded under heavy load.
  7. Eviction is deterministic LRU by (hits, seq) and replayable.
  8. Distance is the minimum Hamming over the slot's existing vectors.
  9. Multi-scale layers (fast/med/slow) are independent.
 10. Occupancy conservation: grid sum equals total live entries.

The CA-field self-regulating dynamics of the source (Wolfram-class kernels)
are NOT bound here; they remain product-side. The 24-dimension connects to
LeechForge (CQE-paper-17).

Source repo: github.com/nbarker2021/CMPLXDevKit
(mcp_os/agrm_mdhg_integration/mdhg_ca.py).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE_SRC = _HERE.parents[1] / "packages" / "cqecmplx-forge" / "src"
if str(_FORGE_SRC) not in sys.path:
    sys.path.insert(0, str(_FORGE_SRC))

import MDHGForge  # noqa: E402


def main() -> int:
    result = MDHGForge.verify()
    receipt = {
        "paper": "CQE-paper-07",
        "theorem": "MDHG geometric cache as discrete-continuous bridge: "
                   "quantize retraction of the continuous 24D Leech space onto "
                   "a discrete slot lattice, stabilized by SpeedLight "
                   "idempotence f(f(x)) = f(x)",
        "forge": "MDHGForge",
        "source_repo": "nbarker2021/CMPLXDevKit "
                       "(mcp_os/agrm_mdhg_integration/mdhg_ca.py)",
        "adjudicated_divergence": [
            "quantize() made total on all reals (input clamped into [0,1) "
            "before floor); source assumed inputs already in [0,1)",
            "eviction made deterministic via a monotonic admission sequence "
            "(source used wall-clock time, non-deterministic under equal hits)",
            "CA-field self-regulating dynamics (CAField, kernel_step, Wolfram "
            "assignments) stay product-side; the forge carries the proven "
            "cache + idempotence core",
        ],
        "tower_link": "the 24 dimensions are the Leech dimension; the bridge "
                      "addresses points of the continuous Leech space "
                      "constructed exactly in LeechForge (CQE-paper-17)",
        "status": result["status"],
        "checks": result["checks"],
        "passed": result["passed"],
        "total": result["total"],
        "open_obligations": [
            "The CA-field dynamics need their own stability receipt before "
            "promotion (Wolfram-class kernels).",
            "Slot collision rate vs the double-hash distribution is an "
            "empirical product diagnostic, not a paper claim.",
        ],
    }
    out = _HERE / "mdhg_speedlight_bridge_receipt.json"
    out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": receipt["status"],
                      "passed": receipt["passed"],
                      "total": receipt["total"],
                      "receipt": str(out)}, indent=2))
    return 0 if receipt["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

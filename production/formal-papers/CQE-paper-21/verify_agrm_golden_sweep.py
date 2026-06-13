#!/usr/bin/env python3
"""Finite verifier binding AGRMForge to CQE Paper 21 (the applied Forge reader
/ grid-swept ribbons).

The Adaptive Geometric Resonance Matrix sweeps a set of 24D nodes in
golden-ratio order, producing a ranked ribbon. The reason phi is the right
sweep constant is the three-gap theorem (Steinhaus): for every N the points
{0, phi, 2 phi, ..., (N-1) phi} mod 1 cut the circle into arcs of at most
three distinct lengths, and the largest is the sum of the other two. Because
phi is the most irrational number (continued fraction [1; 1, 1, ...]) the
sweep stays maximally even at every N — the optimal low-discrepancy reader.

Checks (all finite):
  1. phi identity phi^2 = phi + 1 and value.
  2. phi is the most irrational: Fibonacci-ratio convergents -> phi, monotone.
  3. Three-gap theorem: {k phi mod 1} has <= 3 distinct gaps for all N < 400.
  4. Steinhaus relation: when there are three gaps the largest is the sum of
     the other two.
  5. Low discrepancy: the golden sweep beats a rational rotation and its
     star discrepancy decreases with N.
  6. The sweep order is a permutation of the nodes (lossless ribbon).
  7. The sweep order is deterministic and independent of registration order.
  8. Zone-density thresholds partition the neighbor counts (sparse/medium/dense).
  9. Shell assignment is a total, radius-monotone partition.
 10. Distance is a metric and route reuse is idempotent in the cache.

The resonance-similarity routing heuristics and random/wall-clock paths of
the source stay product-side and are not claimed here.

Source repo: github.com/nbarker2021/CMPLXMCP
(agrm_mdhg_integration/agrm_router.py).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE_SRC = _HERE.parents[1] / "packages" / "cqecmplx-forge" / "src"
if str(_FORGE_SRC) not in sys.path:
    sys.path.insert(0, str(_FORGE_SRC))

import AGRMForge  # noqa: E402


def main() -> int:
    result = AGRMForge.verify()
    receipt = {
        "paper": "CQE-paper-21",
        "theorem": "Golden-ratio low-discrepancy sweep as the optimal grid "
                   "reader: three-gap theorem on {k phi mod 1}, phi the most "
                   "irrational, lossless swept ribbon over 24D nodes",
        "forge": "AGRMForge",
        "source_repo": "nbarker2021/CMPLXMCP (agrm_mdhg_integration/agrm_router.py)",
        "adjudicated_divergence": [
            "source spiral score mixed sweep index with per-node distance and "
            "a SPARSE-zone 1.2x bonus, so identical geometry could rank by "
            "insertion order; the forge separates the pure order-stable "
            "golden-ratio sweep from the heuristic density bonus",
            "route cache made explicitly idempotent (source dict had no reuse "
            "guarantee across rebuilds)",
            "resonance-similarity routing and random/wall-clock heuristics "
            "stay product-side",
        ],
        "tower_link": "the 24 sweep dimensions are the Leech dimension "
                      "(LeechForge, paper 17); phi is the same golden ratio "
                      "whose log/16 is the conservation coupling kappa "
                      "(ChromaForge morphon, paper 09)",
        "status": result["status"],
        "checks": result["checks"],
        "passed": result["passed"],
        "total": result["total"],
        "open_obligations": [
            "Resonance-signature similarity routing needs its own receipt "
            "before promotion.",
            "Midpoint-unlocking path quality is a heuristic, not a proved "
            "optimum; it stays product-side.",
        ],
    }
    out = _HERE / "agrm_golden_sweep_receipt.json"
    out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": receipt["status"],
                      "passed": receipt["passed"],
                      "total": receipt["total"],
                      "receipt": str(out)}, indent=2))
    return 0 if receipt["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

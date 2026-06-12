#!/usr/bin/env python3
"""Finite verifier binding ConvergeForge to CQE Paper 03 (Triality Surface).

S3 is the triality group: its three transpositions permute the (L, C, R)
lanes, and the annealing operator drives every 3-bit state into the
Lie-conjugate basin (L = R) in at most 3 swaps under the fixed sequence
(LR, LC, CR). The bound is verified exhaustively, not cited.

Checks (all finite):
  1. The conjugate basin is exactly the four L=R states.
  2. Each transposition is an involution on all 8 states.
  3. The three transpositions generate all of S3 (order 6).
  4. Every state converges within 3 swaps (exhaustive).
  5. The bound is tight; the 3-swap states are (0,1,1) and (1,0,0) —
     correcting the source docstring, which named (1,1,0) (it takes 2).
  6. Conjugate states anneal in zero steps, unchanged.
  7. Annealing is idempotent: f(f(x)) = f(x).
  8. Recorded trajectories replay deterministically, one transposition
     per step.
  9. Circle classes F = {010, 111} and P = {000, 101} partition the basin.
 10. The load-triple scheduler balances in <= 3 reassignments and leaves
     balanced triples untouched.

Cluster-scale scheduling claims (multi-node safety/liveness under real
capacity constraints) are NOT claimed; they remain product obligations.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE_SRC = _HERE.parents[1] / "packages" / "cqecmplx-forge" / "src"
if str(_FORGE_SRC) not in sys.path:
    sys.path.insert(0, str(_FORGE_SRC))

import ConvergeForge  # noqa: E402


def main() -> int:
    result = ConvergeForge.verify()
    receipt = {
        "paper": "CQE-paper-03",
        "theorem": "Triality annealing: S3 transpositions drive every 3-bit "
                   "state into the Lie-conjugate basin in at most 3 swaps; "
                   "bound tight at (0,1,1) and (1,0,0)",
        "forge": "ConvergeForge",
        "source_product": "historical_pastworks/product_converge (core distilled)",
        "adjudicated_divergence": [
            "source docstring claimed (1,1,0) requires exactly 3 swaps; it "
            "requires 2 — the tight states are (0,1,1) and (1,0,0); the "
            "max-3 bound itself is correct and verified exhaustively",
            "gRPC/REST/consensus/cluster layers stay product-side; only the "
            "proven annealing core enters the forge ring",
        ],
        "status": result["status"],
        "checks": result["checks"],
        "passed": result["passed"],
        "total": result["total"],
        "open_obligations": [
            "Multi-node scheduling safety/liveness under real capacity "
            "constraints is product-layer work, not a paper claim.",
            "The D4 8-chart cluster atlas (chart8.py) needs its own "
            "bijectivity receipt before promotion.",
        ],
    }
    out = _HERE / "triality_annealing_receipt.json"
    out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": receipt["status"],
                      "passed": receipt["passed"],
                      "total": receipt["total"],
                      "receipt": str(out)}, indent=2))
    return 0 if receipt["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Finite verifier binding the kappa conservation law to CQE Paper 09
(Hamiltonian Temporal Emergence).

The conserved field Phi descends by a per-event morphon potential delta,
coupled by kappa = ln(phi)/16. The conservation law cumulative(Phi) <= 0 is
a Hamiltonian/Lyapunov descent; the ordered ledger of deltas IS the emergent
timeline (Paper 09's temporal emergence). The law is realized in
ChromaForge.conservation (ledger) + ChromaForge.morphon (coupling/embedding).

Checks (all finite):
  1. kappa = ln(phi)/16 numerically, agreeing with the source 0.030076.
  2. Golden-ratio identities phi^2 = phi+1 and e^(16 kappa) = phi.
  3. The E8 embedding has norm exactly kappa and is deterministic.
  4. The morphon delta is conserved (<= 0) and bounded by kappa*affinity.
  5. The sector split delta_n + delta_i + delta_l = delta_phi (Noether,
     Shannon, Landauer).
  6. The Event Law per-event emission is exactly -kappa — the value minted
     live in every ChromaForge/PaneForge receipt (cross-repo confirmation).
  7. A stream of conserved deltas keeps cumulative non-increasing, zero
     violations.
  8. A single positive delta is flagged as a violation; only positive
     deltas are.
  9. The audit chain recomputes the cumulative with zero drift.
 10. Surplus is the spendable magnitude when cumulative is negative.

ADJUDICATED FINDING (recorded, load-bearing): CMPLX-TMN-main contradicts
itself on the conserved sign. conservation.py flags delta_phi > 0 as a
violation (and /surplus treats cumulative < 0 as spendable), but engine.py
emits a strictly positive morphon_delta and calls it "conserved surplus".
The live receipt mints -kappa (negative), siding with conservation.py;
engine.py has the sign backwards. The forge emits the conserved (negative)
delta.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE_SRC = _HERE.parents[1] / "packages" / "cqecmplx-forge" / "src"
if str(_FORGE_SRC) not in sys.path:
    sys.path.insert(0, str(_FORGE_SRC))

from ChromaForge import morphon  # noqa: E402


def main() -> int:
    result = morphon.verify()
    receipt = {
        "paper": "CQE-paper-09",
        "theorem": "kappa = ln(phi)/16 conservation law: morphon potential "
                   "delta <= 0 is a Hamiltonian descent whose ordered ledger "
                   "is the emergent timeline; per-event Event Law delta = -kappa",
        "forge": "ChromaForge (conservation + morphon)",
        "source_repo": "nbarker2021/CMPLX-TMN-main "
                       "(src/conservation/conservation.py, src/engine/engine.py)",
        "adjudicated_divergence": [
            "TMN-main internal sign contradiction: conservation.py flags "
            "delta_phi > 0 as a violation and /surplus treats cumulative < 0 "
            "as spendable (conserved = negative), but engine.py emits a "
            "strictly positive morphon_delta labeled 'conserved surplus' — "
            "backwards. The live ChromaForge/PaneForge receipt mints -kappa, "
            "confirming the conservation.py convention; the forge emits the "
            "conserved negative delta",
            "FastAPI/psycopg2/PG-ledger service layers stay product-side; the "
            "forge carries the stdlib conservation core",
        ],
        "cross_repo_confirmation": "EVENT_LAW_DELTA == -kappa == "
                                   "-0.030075739066225217, the exact delta_phi "
                                   "minted in every PaneForge Event Law receipt "
                                   "(production/products/PaneForge-Stick)",
        "status": result["status"],
        "checks": result["checks"],
        "passed": result["passed"],
        "total": result["total"],
        "open_obligations": [
            "Patch CMPLX-TMN-main engine.py morphon_delta sign upstream to "
            "match the conservation service and the live receipt.",
            "The three-sector split is modeled as equal thirds; a derivation "
            "of unequal Noether/Shannon/Landauer weights from content is "
            "future work and is not claimed.",
            "Palindromic-closure equivalence ('the law IS the stop condition "
            "IS palindromic closure') is asserted in the source prose and not "
            "yet given its own receipt.",
        ],
    }
    out = _HERE / "kappa_conservation_law_receipt.json"
    out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": receipt["status"],
                      "passed": receipt["passed"],
                      "total": receipt["total"],
                      "receipt": str(out)}, indent=2))
    return 0 if receipt["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

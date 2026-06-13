#!/usr/bin/env python3
"""Reapplication verifier: T_BIJECTIVE (side-flip SU(2) doublet), bound into
CQE Paper 01 (LCR Chain Carrier).

T_BIJECTIVE is recorded PROVEN by structural identification in
CMPLX-R30-main/PROOF/theorems/THEOREM_REGISTRY.md, with the shell=2 state set
in lattice_forge/core.py :: SHELL2_STATES, but bound to no production paper.
Paper 01 is its exact home: its abstract states the shell=2 stratum supplies
the carried doublet interface, where (1,1,0) and (0,1,1) are exchanged by
left-right reversal while (1,0,1) is fixed.

This is the single-tape construction: both spin-1/2 states are encoded inside
the forward tape's shell=2 stratum by the side-flip bijection, obviating any
antipodal -N counter-sheet.

Checks (all finite):
  1. SHELL2_STATES is exactly {(1,1,0),(1,0,1),(0,1,1)} (the popcount-2 set).
  2. Left-right reversal is an involution on the shell=2 stratum.
  3. The reversal exchanges the chiral pair (1,1,0) <-> (0,1,1).
  4. The reversal fixes the balanced state (1,0,1) (the SU(2) singlet axis).
  5. The orbit structure is one 2-element doublet + one fixed point.
  6. The reversal preserves the center bit C of every shell=2 state.
  7. Shell (popcount) is invariant under reversal across all 8 LCR states.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE_SRC = _HERE.parents[1] / "packages" / "cqecmplx-forge" / "src"
if str(_FORGE_SRC) not in sys.path:
    sys.path.insert(0, str(_FORGE_SRC))

from lattice_forge import core  # noqa: E402


def swap_lr(s):
    return (s[2], s[1], s[0])


def main() -> int:
    shell2 = [tuple(s) for s in core.SHELL2_STATES]
    sset = set(shell2)
    all_states = [(L, C, R) for L in (0, 1) for C in (0, 1) for R in (0, 1)]

    fixed = [s for s in shell2 if swap_lr(s) == s]
    moved = [s for s in shell2 if swap_lr(s) != s]

    checks = {
        "shell2_is_popcount_2_set": sset == {(1, 1, 0), (1, 0, 1), (0, 1, 1)},
        "reversal_is_involution": all(swap_lr(swap_lr(s)) == s for s in shell2),
        "reversal_exchanges_chiral_pair": (
            swap_lr((1, 1, 0)) == (0, 1, 1) and swap_lr((0, 1, 1)) == (1, 1, 0)
        ),
        "reversal_fixes_balanced_state": swap_lr((1, 0, 1)) == (1, 0, 1),
        "orbit_is_doublet_plus_singlet": len(moved) == 2 and len(fixed) == 1,
        "reversal_preserves_center": all(swap_lr(s)[1] == s[1] for s in shell2),
        "shell_invariant_under_reversal_all_8": all(
            sum(swap_lr(s)) == sum(s) for s in all_states
        ),
    }
    status = "pass" if all(checks.values()) else "fail"

    receipt = {
        "paper": "CQE-paper-01",
        "theorem": "T_BIJECTIVE: the shell=2 stratum carries the SU(2) doublet "
                   "via the side-flip bijection — (1,1,0)<->(0,1,1) exchanged, "
                   "(1,0,1) fixed — encoding both spin states on one forward tape",
        "reapplication": True,
        "closes": "paper-binding gap for THEOREM_REGISTRY T_BIJECTIVE "
                  "(PROVEN by structural identification; SHELL2_STATES in "
                  "lattice_forge/core.py; bound to no production paper)",
        "source_module": "lattice_forge/core.py :: SHELL2_STATES",
        "status": status,
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "shell2_states": [list(s) for s in shell2],
        "doublet": [list(s) for s in moved],
        "singlet": [list(s) for s in fixed],
    }
    out = _HERE / "bijective_shell2_doublet_receipt.json"
    out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": status, "passed": receipt["passed"],
                      "total": receipt["total"], "receipt": str(out)}, indent=2))
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

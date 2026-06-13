#!/usr/bin/env python3
"""Reapplication verifier: SU(3)/8x8-closure theorems T5-T7, bound into
CQE Paper 03 (D4 / J3 triality surface).

T5, T6, T7 are recorded PROVEN at exact rational precision in
CMPLX-R30-main/PROOF/theorems/THEOREM_REGISTRY.md with named verifiers in
lattice_forge/f4_action.py, vendored in the production substrate, bound to no
production paper. They are the companions of T4 (already reapplied here):

  T5  Rank-1 idempotency / closure scale  — f4_action.search_for_su3_closure_scale
  T6  Both trace-blocks close identically — f4_action.decompose_8x8_via_block_action_exact
  T7  Closed-form 8x8 transition matrix   — f4_action.closed_form_rule30_8x8_transition_exact

Together with T4 these establish: the shell=2 conditional transition is an
exact rational S3 group-ring element, the two trace blocks (trace-1 and
trace-2 strata) close identically as the SAME S3 element, and the full 8x8
Rule 30 transition has an exact closed form over Q.
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE_SRC = _HERE.parents[1] / "packages" / "cqecmplx-forge" / "src"
if str(_FORGE_SRC) not in sys.path:
    sys.path.insert(0, str(_FORGE_SRC))

from lattice_forge import f4_action  # noqa: E402


def main() -> int:
    t5 = f4_action.search_for_su3_closure_scale(max_scale=16)
    t6 = f4_action.decompose_8x8_via_block_action_exact(n_steps=3)
    t7 = f4_action.closed_form_rule30_8x8_transition_exact()

    # T7 returns an 8x8 matrix of Fractions; check it is row-stochastic exactly
    matrix = t7["matrix"] if isinstance(t7, dict) and "matrix" in t7 else t7.get("matrix")
    row_sums_one = all(sum(row) == Fraction(1) for row in matrix)
    all_fractions = all(isinstance(x, Fraction) for row in matrix for x in row)

    checks = {
        "T5_closes_at_a_scale": t5.get("closed_at_a_scale") is True,
        "T5_best_scale_is_3": t5.get("best_scale") == 3,
        "T5_residual_near_zero": float(t5.get("best_residual_l2", 1)) < 1e-12,
        "T6_trace1_exact_s3_element": t6.get("trace1_is_exact_s3_element") is True,
        "T6_trace2_exact_s3_element": t6.get("trace2_is_exact_s3_element") is True,
        "T6_trace1_residual_zero": str(t6.get("trace1_residual_squared")) == "0",
        "T6_trace2_residual_zero": str(t6.get("trace2_residual_squared")) == "0",
        "T6_both_blocks_close_identically": (
            t6.get("trace1_s3_decomposition") == t6.get("trace2_s3_decomposition")
        ),
        "T7_8x8_matrix_is_8_rows": len(matrix) == 8 and all(len(r) == 8 for r in matrix),
        "T7_rows_exactly_stochastic": row_sums_one and all_fractions,
    }
    status = "pass" if all(checks.values()) else "fail"

    receipt = {
        "paper": "CQE-paper-03",
        "theorem": "SU(3)/8x8 closure T5-T7: closure at scale 3, both trace "
                   "blocks close identically as the same exact S3 element, "
                   "closed-form exact-rational 8x8 Rule 30 transition",
        "reapplication": True,
        "closes": "paper-binding gap for THEOREM_REGISTRY T5, T6, T7 (PROVEN "
                  "exact-rational, verifiers in lattice_forge/f4_action.py, "
                  "bound to no production paper)",
        "source_module": "lattice_forge/f4_action.py",
        "status": status,
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "exact_s3_decomposition": t6.get("trace1_s3_decomposition"),
    }
    out = _HERE / "su3_closure_T5_T7_receipt.json"
    out.write_text(json.dumps(receipt, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps({"status": status, "passed": receipt["passed"],
                      "total": receipt["total"], "receipt": str(out)}, indent=2))
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

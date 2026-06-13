#!/usr/bin/env python3
"""Reapplication verifier: the E8 root enumeration that PFC-2 names as its
closing computation, bound into CQE Paper 08 (Lattice Closure).

PFC-2 (CMPLX-R30-main/PROOF/theorems/OPEN_OBLIGATIONS.md) is status
"derivation complete; geometric verification of the 13 boundary
half-vignette count pending", and its stated "what would close it" is:
"Enumerate all 240 E8 roots from Construction A. Place observer at one root.
Define spin-state hemisphere. Count boundary half-vignette contributions ...
Expected: 120 + 13 + 4 = 137, remainder 103."

E8Forge now performs that exact enumeration. This verifier reapplies it to
confirm the LATTICE-ARITHMETIC facts PFC-2 depends on, advancing PFC-2 from
"root enumeration unbuilt" to "root enumeration built; the countable parts
confirmed."

HONESTY BOUNDARY (load-bearing — this verifier does NOT prove physics):
  - The "13 boundary half-vignettes" count is a GEOMETRIC/physical claim about
    an observer light cone, NOT determined by root enumeration alone. It is
    NOT verified here and remains open.
  - The identification 1/137 = the fine structure constant is a PHYSICAL
    hypothesis. It is NOT claimed, tested, or endorsed here.
  - Only the even, antipodal lattice arithmetic is confirmed: 240 roots,
    120 antipodal pairs, and the integer decomposition 120 + 13 + 4 = 137,
    240 - 137 = 103 as ARITHMETIC over the enumerated set.
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
    roots = E8Forge.roots()
    rset = set(roots)
    checks: dict[str, bool] = {}

    # 1. The enumeration PFC-2 names exists and gives 240 roots
    checks["e8_root_enumeration_is_240"] = len(roots) == 240 == len(rset)

    # 2. Roots come in antipodal pairs: every root's negation is present
    checks["roots_antipodally_paired"] = all(
        tuple(-x for x in r) in rset for r in roots
    )

    # 3. No root is its own antipode -> exactly 120 antipodal pairs
    #    (the "hemisphere" count PFC-2 calls 120)
    no_fixed = all(tuple(-x for x in r) != r for r in roots)
    checks["hemisphere_is_120_pairs"] = no_fixed and (len(roots) // 2 == 120)

    # 4. The PFC-2 decomposition is consistent arithmetic over the 240 set:
    #    120 + 13 + 4 = 137 and 240 - 137 = 103
    checks["pfc2_decomposition_arithmetic"] = (
        120 + 13 + 4 == 137 and len(roots) - 137 == 103
    )

    # 5. A hemisphere is selectable by a generic linear functional with no
    #    root on the boundary (a clean +N / -k split into 120 / 120)
    # powers of two: no signed subset of distinct binary weights cancels,
    # so no root lands on the f = 0 boundary
    weights = (1, 2, 4, 8, 16, 32, 64, 128)
    def f(r: tuple[int, ...]) -> int:
        return sum(w * x for w, x in zip(weights, r))
    pos = [r for r in roots if f(r) > 0]
    neg = [r for r in roots if f(r) < 0]
    checks["clean_hemisphere_split_120_120"] = (
        len(pos) == 120 and len(neg) == 120 and not any(f(r) == 0 for r in roots)
    )

    status = "pass" if all(checks.values()) else "fail"
    receipt = {
        "paper": "CQE-paper-08",
        "theorem": "E8 root enumeration (240 roots, 120 antipodal pairs, clean "
                   "hemisphere split) — the lattice-arithmetic substrate PFC-2 "
                   "names as its closing computation",
        "reapplication": True,
        "advances": "PFC-2 (CMPLX-R30-main/PROOF/theorems/OPEN_OBLIGATIONS.md): "
                    "the named root enumeration is now built (E8Forge) and the "
                    "countable lattice facts are confirmed",
        "status": status,
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "explicitly_not_claimed": [
            "the '13 boundary half-vignettes' geometric count (an observer "
            "light-cone claim, not fixed by root enumeration) — remains OPEN",
            "the identification 1/137 = fine structure constant (a physical "
            "hypothesis) — NOT tested or endorsed",
        ],
    }
    out = _HERE / "e8_hemisphere_partition_receipt.json"
    out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": status, "passed": receipt["passed"],
                      "total": receipt["total"], "receipt": str(out)}, indent=2))
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

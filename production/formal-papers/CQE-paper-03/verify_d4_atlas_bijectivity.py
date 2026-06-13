#!/usr/bin/env python3
"""Finite verifier binding the D4 chart atlas to CQE Paper 03 (D4 / J3
triality surface).

Closes the ConvergeForge open obligation: the 8-chart cluster atlas
bijectivity. The 8 views are the dihedral group D4 (order 8 = 2*4) acting on
the four corners of a square. Every view is a bijection, the group is closed
with identity and inverses, and view(view_inverse(state)) == state exactly —
the invariant the source product asserted in prose but never verified.

Checks (all finite, exhaustive over the 8 elements):
  1. Exactly 8 distinct views.
  2. Every view is a bijection of the 4 corners.
  3. Closure under composition (8x8 table).
  4. Identity present and acts as a unit.
  5. Every view has an inverse in the group, and the round-trip
     view(view_inverse(state)) == state.
  6. The four rotations form a cyclic subgroup of order 4.
  7. The four mirrors are involutions (order 2).
  8. D4 is non-abelian (rotation and reflection do not commute).
  9. Views preserve information (no symbol lost or gained).
 10. The atlas exposes exactly 8 named views matching the group order.

Source: product_converge/src/state/chart8.py (ViewType + mirror table) and
CMPLX-TMN-main board atlases. The D4 atlas sits on the same triality surface
as the S3 annealing already bound to this paper.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE_SRC = _HERE.parents[1] / "packages" / "cqecmplx-forge" / "src"
if str(_FORGE_SRC) not in sys.path:
    sys.path.insert(0, str(_FORGE_SRC))

from ConvergeForge import d4_atlas  # noqa: E402


def main() -> int:
    result = d4_atlas.verify()
    receipt = {
        "paper": "CQE-paper-03",
        "theorem": "D4 chart atlas bijectivity: 8 dihedral views (order 8), "
                   "each a bijection of the square's corners, closed group "
                   "with identity and inverses, view(view_inverse(x)) == x",
        "forge": "ConvergeForge (d4_atlas)",
        "closes_obligation": "ConvergeForge-2026-06-12: 'the D4 chart8 cluster "
                             "atlas needs its own bijectivity receipt before "
                             "promotion'",
        "source_repo": "product_converge/src/state/chart8.py; "
                       "nbarker2021/CMPLX-TMN-main board atlases",
        "status": result["status"],
        "checks": result["checks"],
        "passed": result["passed"],
        "total": result["total"],
        "open_obligations": [
            "The cluster-state to-triplet encoding (utilization -> 3-bit) is a "
            "lossy projection, not a bijection; that is by design and is not "
            "claimed bijective."
        ],
    }
    out = _HERE / "d4_atlas_bijectivity_receipt.json"
    out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": receipt["status"],
                      "passed": receipt["passed"],
                      "total": receipt["total"],
                      "receipt": str(out)}, indent=2))
    return 0 if receipt["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

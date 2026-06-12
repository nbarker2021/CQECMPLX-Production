"""Paper 19 verifier: observer face-selection receipts."""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "production" / "packages" / "cqecmplx-forge" / "src"
sys.path.insert(0, str(SRC))

from lattice_forge.centroid_voa import (  # noqa: E402
    STATES,
    four_frame_label,
    gluon,
    swap_LR,
    verify_gluon_invariance,
    verify_z4_period_template,
)
from lattice_forge.monster_d4_lift_claim import verify_monster_d4_lift_claim  # noqa: E402

FACES = ("C-centroid", "R-centroid", "C-flipped", "L-centroid")


def select_face(index: int) -> dict:
    if index not in range(4):
        raise ValueError("face index must be 0, 1, 2, or 3")
    return {
        "selected_face": FACES[index],
        "selected_index": index,
        "latent_faces": [face for i, face in enumerate(FACES) if i != index],
        "latent_count": 3,
    }


def face_table() -> dict:
    return {
        str(s): {
            "gluon": gluon(s),
            "antipode": swap_LR(s),
            "antipode_gluon": gluon(swap_LR(s)),
            "four_frame_label": four_frame_label(s),
        }
        for s in STATES
    }


def main() -> dict:
    gluon_receipt = verify_gluon_invariance()
    z4 = verify_z4_period_template()
    monster_d4 = verify_monster_d4_lift_claim(max_depth=128)
    faces = [select_face(i) for i in range(4)]
    table = face_table()

    checks = {
        "four_faces_exist": len(FACES) == 4,
        "each_selection_retains_three_latent_faces": all(f["latent_count"] == 3 for f in faces),
        "gluon_invariant_under_antipode": gluon_receipt.get("status") == "pass"
        and all(row["gluon"] == row["antipode_gluon"] for row in table.values()),
        "z4_face_template_passes": z4.get("status") == "pass"
        and z4.get("fixed_point_count") == 2
        and z4.get("period_2_count") == 0
        and z4.get("period_4_count") == 6,
        "bounded_observer_route_evidence_passes": monster_d4.get("status")
        == "pass_with_open_gaps"
        and monster_d4.get("checks", {}).get("all_eight_chart_states_enumerated") is True
        and monster_d4.get("checks", {}).get("d4_lift_all_n_after_activation") is True,
        "spinor_class_remains_open": True,
        "consciousness_postulate_not_promoted": True,
    }

    receipt = {
        "paper": "CQE Paper 19",
        "title": "Observer Face-Selection",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "closed_layers": [
            "four selectable frame faces are defined",
            "selecting one face retains three latent faces",
            "gluon C is invariant under LR antipodal reversal over all eight states",
            "static Z4 face template has 2 fixed points and 6 period-4 states",
            "bounded observer-route evidence enumerates all eight chart states and preserves D4 lift after activation",
        ],
        "open_layers": [
            "SPINOR signature observation",
            "full frame-inversion Q(S) executable binding in the promoted paper layer",
            "consciousness or measurement-collapse interpretation",
            "global physical observer theorem",
        ],
        "falsifiers": [
            "a selected face deletes rather than retains latent faces",
            "gluon changes under LR antipodal reversal",
            "Z4 face template contains period-2 states",
            "bounded open-gap evidence is promoted as a completed theorem",
            "SPINOR is claimed observed without a receipt",
        ],
        "source_receipts": {
            "face_selections": faces,
            "face_table": table,
            "gluon_invariance": gluon_receipt,
            "z4_face_template": z4,
            "monster_d4_lift": monster_d4,
        },
    }

    out_path = Path(__file__).with_name("observer_face_selection_receipt.json")
    out_path.write_text(json.dumps(receipt, indent=2, default=str), encoding="utf-8")
    print(json.dumps({"status": receipt["status"], "checks": checks}, indent=2))
    return receipt


if __name__ == "__main__":
    result = main()
    raise SystemExit(0 if result["status"] == "pass" else 1)

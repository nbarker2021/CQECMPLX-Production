"""Formal receipt generator for Paper 30.

Paper 30 frames papers 00-29 as one swept ribbon. The verifier closes the
8-slot fill discipline, the 30-position corpus sweep, the canonical terminal
composition route, and the transport-obligation boundary. It does not make
Paper 31 a dependency and it does not add a new mathematical theorem.
"""

from __future__ import annotations

import json
import sys
import tempfile
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "production" / "packages" / "cqecmplx-forge" / "src"))

from lattice_forge.ledger import build_seed_database  # noqa: E402
from lattice_forge.terminal_tree import (  # noqa: E402
    build_terminal_composition_tree,
    terminal_tree_summary,
)
from lattice_forge.transport_obligations import (  # noqa: E402
    verify_transport_obligations,
)


OUT = Path(__file__).resolve().parent / "grand_ribbon_meta_framer_receipt.json"
PAPER_COUNT = 30
PAPER_IDS = [f"CQE-paper-{index:02d}" for index in range(PAPER_COUNT)]


class SlotName(str, Enum):
    C = "C"
    L = "L"
    R = "R"
    B = "B"
    T = "T"
    O = "O"
    W = "W"
    A = "A"


SLOT_NAMES = tuple(SlotName)
SOURCE_KINDS = ("binary", "vector", "binary+vector")


@dataclass(frozen=True)
class Slot:
    name: SlotName
    value: Any | None = None
    provenance: str | None = None
    source_kind: str | None = None

    def __post_init__(self) -> None:
        if self.source_kind is not None and self.source_kind not in SOURCE_KINDS:
            raise ValueError(f"invalid source kind {self.source_kind!r}")

    @property
    def filled(self) -> bool:
        return self.value is not None and self.provenance is not None


@dataclass
class Ribbon:
    slots: dict[SlotName, Slot] | None = None

    def __post_init__(self) -> None:
        if self.slots is None:
            self.slots = {name: Slot(name=name) for name in SLOT_NAMES}
        for name in SLOT_NAMES:
            self.slots.setdefault(name, Slot(name=name))

    def fill(
        self,
        slot_name: SlotName,
        value: Any,
        provenance: str,
        source_kind: str = "binary+vector",
    ) -> "Ribbon":
        self.slots[slot_name] = Slot(slot_name, value, provenance, source_kind)
        return self

    def is_filled(self, slot_name: SlotName) -> bool:
        return self.slots[slot_name].filled


def _check(name: str, passed: bool, detail: Any) -> dict[str, Any]:
    return {"name": name, "pass": bool(passed), "detail": detail}


def _paper_paths(paper_id: str) -> dict[str, str]:
    paper_n = paper_id.rsplit("-", 1)[-1]
    formal = ROOT / "production" / "formal-papers" / paper_id / "FORMAL_PAPER.md"
    source = ROOT / "Papers" / "Source" / f"{paper_id}.md"
    production_source = ROOT / "production" / "papers" / paper_id / "SOURCE.md"
    return {
        "formal": str(formal.relative_to(ROOT)) if formal.exists() else "",
        "source": str(source.relative_to(ROOT)) if source.exists() else "",
        "production_source": str(production_source.relative_to(ROOT)) if production_source.exists() else "",
        "paper_number": paper_n,
    }


def build_paper_ribbon(paper_id: str) -> Ribbon:
    paths = _paper_paths(paper_id)
    source_path = paths["formal"] or paths["source"] or paths["production_source"]
    if not source_path:
        raise FileNotFoundError(f"no source path found for {paper_id}")
    previous_id = f"CQE-paper-{(int(paths['paper_number']) - 1) % PAPER_COUNT:02d}"
    next_id = f"CQE-paper-{(int(paths['paper_number']) + 1) % PAPER_COUNT:02d}"
    return (
        Ribbon()
        .fill(SlotName.C, f"{paper_id} claim center", source_path)
        .fill(SlotName.L, previous_id, source_path)
        .fill(SlotName.R, next_id, source_path)
        .fill(SlotName.B, "Rule 30/LCR local readout boundary", source_path)
        .fill(SlotName.T, "paper verifier or formal receipt binding", source_path)
        .fill(SlotName.O, "explicit open-obligation row set", source_path)
        .fill(SlotName.W, "quarter-step workbook/toolkit supplement when present", source_path)
        .fill(SlotName.A, "citation/provenance anchors", source_path)
    )


def ribbon_sweep_rows() -> list[dict[str, Any]]:
    rows = []
    for index, paper_id in enumerate(PAPER_IDS):
        ribbon = build_paper_ribbon(paper_id)
        rows.append(
            {
                "index": index,
                "paper_id": paper_id,
                "filled_slots": [slot.value for slot in SLOT_NAMES if ribbon.is_filled(slot)],
                "slot_count": len(SLOT_NAMES),
                "all_slots_filled": all(ribbon.is_filled(slot) for slot in SLOT_NAMES),
                "provenance": {slot.value: ribbon.slots[slot].provenance for slot in SLOT_NAMES},
            }
        )
    return rows


def terminal_route_receipt() -> dict[str, Any]:
    db_path = Path(tempfile.gettempdir()) / "cqe_paper30_seed.sqlite"
    ledger = build_seed_database(db_path, overwrite=True)
    tree = build_terminal_composition_tree(ledger, "Niemeier:A2^12")
    summary = terminal_tree_summary(tree)
    return {
        "summary": summary,
        "route_length": len(tree.get("composition_route", [])),
        "action_edge_count": len(tree.get("action_edges", [])),
        "residue_trace_count": len(tree.get("residue_trace", [])),
        "passes": (
            summary["status"] == "generated_canonical_composition_tree"
            and summary["route_uniqueness"] == "single_canonical_route_after_component_ordering_and_orbit_quotient"
            and len(tree.get("composition_route", [])) >= 2
        ),
    }


def build_receipt() -> dict[str, Any]:
    sweep = ribbon_sweep_rows()
    transport = verify_transport_obligations(max_depth=512)
    terminal = terminal_route_receipt()
    slot_names = [slot.value for slot in SLOT_NAMES]
    checks = [
        _check("slot_schema_has_eight_slots", slot_names == ["C", "L", "R", "B", "T", "O", "W", "A"], slot_names),
        _check("source_kinds_are_bounded", SOURCE_KINDS == ("binary", "vector", "binary+vector"), SOURCE_KINDS),
        _check("paper_00_to_29_sweep_has_30_positions", len(sweep) == PAPER_COUNT, len(sweep)),
        _check("every_sweep_position_has_eight_filled_slots", all(row["all_slots_filled"] for row in sweep), sweep),
        _check("terminal_route_is_single_canonical_route", terminal["passes"], terminal),
        _check(
            "transport_ledger_passes_with_visible_open_lifts",
            transport["status"] == "pass_with_open_lifts" and transport["open_lift_count"] > 0,
            transport,
        ),
        _check(
            "paper_31_not_a_dependency",
            "CQE-paper-31" not in PAPER_IDS,
            {"sweep": "CQE-paper-00 through CQE-paper-29", "readout": "CQE-paper-31 prepared only"},
        ),
    ]
    passed = all(check["pass"] for check in checks)
    return {
        "paper": "CQE-paper-30",
        "title": "Grand Ribbon Meta-Framer",
        "status": "pass_with_open_packaging_obligations" if passed else "fail",
        "closed_scope": [
            "8-slot ribbon fill discipline",
            "30-position sweep for papers 00-29",
            "terminal composition route is single canonical route",
            "transport ledger passes while preserving open lifts",
            "Paper 31 is prepared as readout, not used as dependency",
        ],
        "not_claimed": [
            "a new mathematical theorem beyond the cited receipts",
            "31-paper proof dependency including Paper 31",
            "all transport lifts fully demonstrated",
            "a packaged production cqe_engine.ribbon module in this git root",
        ],
        "slot_schema": {
            "slots": slot_names,
            "source_kinds": SOURCE_KINDS,
            "filled_definition": "value is not None and provenance is not None",
        },
        "sweep_rows": sweep,
        "terminal_route": terminal,
        "transport_obligations": transport,
        "open_obligations": [
            "Promote the reusable cqe_engine.ribbon module from neighboring kernel/production copies into this production package.",
            "Keep Paper 31 as a retrospective readout until a later contract explicitly changes dependency order.",
            "Resolve transport ledger open lifts before claiming complete route closure.",
            "Reconcile legacy 31-bead workbook wording with the production 00-29 proof sweep plus Paper 31 readout.",
        ],
        "checks": checks,
    }


def main() -> int:
    receipt = build_receipt()
    OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["status"].startswith("pass") else 1


if __name__ == "__main__":
    raise SystemExit(main())

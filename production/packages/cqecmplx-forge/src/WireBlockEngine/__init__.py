"""WireBlock Engine - legality kernel for CADForge.

WireBlock makes CAD simple by refusing uninitialized geometry. A design starts
from a named family, receives only legal wireframe attachables, and exposes only
bounded variables declared by that family.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Mapping

from reforge_engine_contracts.core import GraphEdge, GraphNode, Receipt, stable_id, now
from reforge_engine_contracts.validation import validate_graph
from reforge_wireforge.templates import make_wire_template
from reforge_wireforge.encoder import encode_wireframe


@dataclass(frozen=True)
class VariableSpec:
    minimum: float
    maximum: float
    default: float
    step: float
    unit: str
    role: str

    def validate(self, value: float) -> float:
        value = float(value)
        if value < self.minimum or value > self.maximum:
            raise ValueError(
                f"value {value!r} outside legal range "
                f"[{self.minimum}, {self.maximum}] {self.unit}"
            )
        if self.step > 0:
            offset = round((value - self.minimum) / self.step)
            snapped = self.minimum + offset * self.step
            if abs(snapped - value) > 1e-9:
                raise ValueError(f"value {value!r} is not aligned to step {self.step}")
        return value

    def to_dict(self) -> Dict[str, Any]:
        return {
            "minimum": self.minimum,
            "maximum": self.maximum,
            "default": self.default,
            "step": self.step,
            "unit": self.unit,
            "role": self.role,
        }


DESIGN_FAMILIES: Dict[str, Dict[str, Any]] = {
    "panel_bracket": {
        "base_template": "lcr_2x2",
        "description": "A simple panel bracket with a legal rectangular base, rib, and hole field.",
        "allowed_attachables": {
            "rib": {"template": "radial_boundary", "edge_type": "reinforces", "max_count": 4},
            "hole_field": {"template": "lattice_8x8", "edge_type": "subtracts", "max_count": 1},
            "mount_ring": {"template": "octad_faces", "edge_type": "mounts", "max_count": 2},
        },
        "variables": {
            "width_mm": VariableSpec(20, 240, 80, 1, "mm", "base width"),
            "height_mm": VariableSpec(20, 240, 60, 1, "mm", "base height"),
            "thickness_mm": VariableSpec(1, 20, 4, 0.5, "mm", "printable thickness"),
            "rib_count": VariableSpec(0, 4, 2, 1, "count", "reinforcing ribs"),
            "hole_diameter_mm": VariableSpec(2, 20, 6, 0.5, "mm", "mount hole diameter"),
        },
    },
    "enclosure_shell": {
        "base_template": "carrier_2x2x2x2",
        "description": "A constrained electronics enclosure shell with vents, bosses, and panel openings.",
        "allowed_attachables": {
            "vent_grid": {"template": "lattice_8x8", "edge_type": "cuts_air", "max_count": 4},
            "boss": {"template": "radial_boundary", "edge_type": "mounts", "max_count": 8},
            "panel_opening": {"template": "lcr_2x2", "edge_type": "cuts_panel", "max_count": 2},
        },
        "variables": {
            "length_mm": VariableSpec(40, 300, 120, 1, "mm", "outer length"),
            "width_mm": VariableSpec(30, 220, 80, 1, "mm", "outer width"),
            "height_mm": VariableSpec(15, 120, 35, 1, "mm", "outer height"),
            "wall_mm": VariableSpec(1, 8, 2, 0.25, "mm", "wall thickness"),
            "corner_radius_mm": VariableSpec(0, 24, 4, 0.5, "mm", "corner radius"),
        },
    },
    "metamaterial_tile": {
        "base_template": "lattice_8x8",
        "description": "A constrained unit-cell tile for MetaForge-style lattice exploration.",
        "allowed_attachables": {
            "octad_cell": {"template": "octad_faces", "edge_type": "cell_ring", "max_count": 8},
            "podal_bridge": {"template": "podal_24d_triplet", "edge_type": "bridges", "max_count": 3},
            "boundary_probe": {"template": "radial_boundary", "edge_type": "tests_boundary", "max_count": 8},
        },
        "variables": {
            "cell_pitch_mm": VariableSpec(2, 40, 8, 0.5, "mm", "cell pitch"),
            "strut_mm": VariableSpec(0.4, 8, 1.2, 0.1, "mm", "strut thickness"),
            "tile_count_x": VariableSpec(1, 16, 4, 1, "count", "x repeat"),
            "tile_count_y": VariableSpec(1, 16, 4, 1, "count", "y repeat"),
            "compliance_bias": VariableSpec(-1, 1, 0, 0.05, "ratio", "negative to positive compliance bias"),
        },
    },
}


def families() -> Dict[str, Dict[str, Any]]:
    """Return the legal initialized design families."""
    out: Dict[str, Dict[str, Any]] = {}
    for name, spec in DESIGN_FAMILIES.items():
        out[name] = {
            "description": spec["description"],
            "base_template": spec["base_template"],
            "allowed_attachables": deepcopy(spec["allowed_attachables"]),
            "variables": {k: v.to_dict() for k, v in spec["variables"].items()},
        }
    return out


def _family_or_raise(family: str) -> Dict[str, Any]:
    if family not in DESIGN_FAMILIES:
        raise ValueError(f"unknown CADForge family {family!r}")
    return DESIGN_FAMILIES[family]


def _default_variables(spec: Mapping[str, Any]) -> Dict[str, float]:
    return {k: v.default for k, v in spec["variables"].items()}


def _validate_variables(spec: Mapping[str, Any], variables: Mapping[str, Any]) -> Dict[str, float]:
    legal = dict(_default_variables(spec))
    for key, value in variables.items():
        if key not in spec["variables"]:
            raise ValueError(f"illegal variable {key!r} for initialized family")
        legal[key] = spec["variables"][key].validate(value)
    return legal


def _prefix_template(template: Dict[str, Any], prefix: str) -> Dict[str, Any]:
    tpl = deepcopy(template)
    for node in tpl["nodes"]:
        node["id"] = f"{prefix}:{node['id']}"
    for edge in tpl["edges"]:
        edge["source"] = f"{prefix}:{edge['source']}"
        edge["target"] = f"{prefix}:{edge['target']}"
    return tpl


def initialize_design(
    family: str = "panel_bracket",
    *,
    name: str = "untitled",
    variables: Mapping[str, Any] | None = None,
) -> Dict[str, Any]:
    """Create the only legal starting shape for a CADForge design family."""
    spec = _family_or_raise(family)
    legal_vars = _validate_variables(spec, variables or {})
    base = _prefix_template(make_wire_template(spec["base_template"], scale=1.0), "base")
    design = {
        "design_id": stable_id("cad", {"family": family, "name": name, "variables": legal_vars}),
        "name": name,
        "family": family,
        "status": "initialized",
        "variables": legal_vars,
        "base_template": spec["base_template"],
        "attachables": [],
        "nodes": base["nodes"],
        "edges": base["edges"],
        "legal_attachables": deepcopy(spec["allowed_attachables"]),
        "variable_schema": {k: v.to_dict() for k, v in spec["variables"].items()},
    }
    validate_graph(
        [GraphNode(n["id"], n["label"], "wire_node", n.get("color_state", "grey"), n).to_dict() for n in design["nodes"]],
        [GraphEdge(e["source"], e["target"], e["edge_type"], e.get("color_state", "clear"), e).to_dict() for e in design["edges"]],
    )
    return design


def attach(
    design: Mapping[str, Any],
    attachable: str,
    *,
    anchor_node: str = "base:n0",
    attachment_id: str | None = None,
    scale: float = 1.0,
    orientation: str = "external",
) -> Dict[str, Any]:
    """Attach a legal wireframe module to an initialized CADForge design."""
    family = str(design.get("family", ""))
    spec = _family_or_raise(family)
    allowed = spec["allowed_attachables"]
    if design.get("status") != "initialized":
        raise ValueError("CADForge design must be initialized before attachment")
    if attachable not in allowed:
        raise ValueError(f"illegal attachable {attachable!r} for family {family!r}")
    count = sum(1 for item in design.get("attachables", []) if item.get("name") == attachable)
    if count >= int(allowed[attachable]["max_count"]):
        raise ValueError(f"attachable {attachable!r} exceeds max_count")
    node_ids = {n["id"] for n in design.get("nodes", [])}
    if anchor_node not in node_ids:
        raise ValueError(f"anchor node {anchor_node!r} is not in the initialized design")

    attachment_id = attachment_id or f"{attachable}_{count + 1}"
    tpl = _prefix_template(
        make_wire_template(allowed[attachable]["template"], scale=scale, orientation=orientation),
        attachment_id,
    )
    new_design = deepcopy(dict(design))
    new_design["nodes"] = list(new_design["nodes"]) + tpl["nodes"]
    new_design["edges"] = list(new_design["edges"]) + tpl["edges"] + [
        {
            "source": anchor_node,
            "target": f"{attachment_id}:n0",
            "edge_type": allowed[attachable]["edge_type"],
            "color_state": "neon",
        }
    ]
    new_design["attachables"] = list(new_design.get("attachables", [])) + [
        {
            "name": attachable,
            "attachment_id": attachment_id,
            "template": allowed[attachable]["template"],
            "anchor_node": anchor_node,
            "scale": scale,
            "orientation": orientation,
        }
    ]
    validate_graph(
        [GraphNode(n["id"], n["label"], "wire_node", n.get("color_state", "grey"), n).to_dict() for n in new_design["nodes"]],
        [GraphEdge(e["source"], e["target"], e["edge_type"], e.get("color_state", "clear"), e).to_dict() for e in new_design["edges"]],
    )
    new_design["design_id"] = stable_id("cad", {
        "family": family,
        "name": new_design.get("name"),
        "variables": new_design.get("variables"),
        "attachables": new_design.get("attachables"),
    })
    return new_design


def tweak(design: Mapping[str, Any], variable: str, value: Any) -> Dict[str, Any]:
    """Update one legal bounded variable."""
    spec = _family_or_raise(str(design.get("family", "")))
    if variable not in spec["variables"]:
        raise ValueError(f"illegal variable {variable!r} for family {design.get('family')!r}")
    new_design = deepcopy(dict(design))
    new_design["variables"] = dict(new_design.get("variables", {}))
    new_design["variables"][variable] = spec["variables"][variable].validate(value)
    new_design["design_id"] = stable_id("cad", {
        "family": new_design.get("family"),
        "name": new_design.get("name"),
        "variables": new_design.get("variables"),
        "attachables": new_design.get("attachables"),
    })
    return new_design


def design_receipt(design: Mapping[str, Any]) -> Dict[str, Any]:
    """Return a receipt for the current legal CAD design state."""
    nodes = [
        GraphNode(n["id"], n["label"], "wire_node", n.get("color_state", "grey"), n).to_dict()
        for n in design.get("nodes", [])
    ]
    edges = [
        GraphEdge(e["source"], e["target"], e["edge_type"], e.get("color_state", "clear"), e).to_dict()
        for e in design.get("edges", [])
    ]
    validate_graph(nodes, edges)
    # Reuse WireForge LCR for the base template as the first legality proof.
    base_receipt = encode_wireframe(design.get("base_template", "lcr_2x2"))
    payload = {
        "design": deepcopy(dict(design)),
        "summary": {
            "family": design.get("family"),
            "node_count": len(nodes),
            "edge_count": len(edges),
            "attachable_count": len(design.get("attachables", [])),
            "variables": dict(design.get("variables", {})),
        },
        "wireforge_base_receipt": base_receipt.get("receipt_id"),
    }
    rid = stable_id("cad_receipt", payload)
    return Receipt(rid, "WireBlock", "pass", base_receipt.get("lcr_blocks", []), nodes, edges, payload, now()).to_dict()


def design_walkthrough(family: str = "panel_bracket") -> Dict[str, Any]:
    """Produce a user-facing walkthrough for a CADForge design session."""
    spec = _family_or_raise(family)
    return {
        "family": family,
        "description": spec["description"],
        "steps": [
            "Choose an initialized design family.",
            f"CADForge loads the legal base template: {spec['base_template']}.",
            "WireBlock exposes only declared variables and their legal ranges.",
            "The builder selects from the legal attachable list.",
            "WireBlock attaches the chosen wireframe only at an existing anchor node.",
            "Each tweak validates against range and step constraints.",
            "The design exports as a graph plus receipt, ready for CAD/BOM/toolpath adapters.",
        ],
        "allowed_attachables": deepcopy(spec["allowed_attachables"]),
        "variable_schema": {k: v.to_dict() for k, v in spec["variables"].items()},
    }


__all__ = [
    "DESIGN_FAMILIES",
    "VariableSpec",
    "families",
    "initialize_design",
    "attach",
    "tweak",
    "design_receipt",
    "design_walkthrough",
]

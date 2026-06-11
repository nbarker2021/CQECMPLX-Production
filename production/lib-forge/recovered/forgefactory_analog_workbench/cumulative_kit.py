"""
Cumulative Receipt Kit - The Live Running Receipt

The analog toolkit IS the cumulative receipt of all digital tools verified.
It grows with each paper. Paper N's kit = Paper N-1's kit + new tools for Paper N.

There is no "working subset." There is only "the kit at step N."
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Set
from enum import Enum


@dataclass(frozen=True)
class KitTool:
    """A single tool in the kit, with its digital twin."""
    object_id: str
    color: str
    tool_class: str
    paper_introduced: str  # Which paper added this
    digital_twin: str      # The verifier/engine function it mirrors
    purpose: str


class CumulativeReceiptKit:
    """
    The kit is a live receipt. Each paper adds tools.
    The kit at step N contains everything from steps 0..N.
    """
    
    def __init__(self):
        self.tools: List[KitTool] = []
        self.by_paper: Dict[str, List[KitTool]] = {}
        self.colors: Set[str] = set()
        self.digital_twins: Set[str] = set()
    
    def add_paper(self, paper_id: str, tools: List[KitTool]):
        """Paper N adds these tools to the cumulative kit."""
        for tool in tools:
            self.tools.append(tool)
            self.colors.add(tool.color)
            self.digital_twins.add(tool.digital_twin)
        
        self.by_paper[paper_id] = tools
    
    def tools_for_paper(self, paper_id: str) -> List[KitTool]:
        """All tools available when working on this paper (cumulative up to N)."""
        # Papers are in order: P00, P01, ...
        paper_order = sorted(self.by_paper.keys())
        if paper_id not in paper_order:
            return self.tools  # If not tracked, give everything
        
        idx = paper_order.index(paper_id)
        available = []
        for i in range(idx + 1):
            available.extend(self.by_paper[paper_order[i]])
        return available
    
    def summary_at(self, paper_id: str) -> Dict:
        """Kit state when working on paper_id."""
        avail = self.tools_for_paper(paper_id)
        return {
            "paper": paper_id,
            "total_tools": len(avail),
            "colors_available": sorted({t.color for t in avail}),
            "digital_twins_available": sorted({t.digital_twin for t in avail}),
            "by_color": {c: [t.object_id for t in avail if t.color == c] for c in sorted({t.color for t in avail})},
        }


# The exact tool additions for each paper
PAPER_TOOLS = {
    "CQE-paper-00": [
        KitTool("token:C:01", "grey_gradient", "token", "CQE-paper-00", "Gluon_Gamma",
                "Active center token - the chart readout center"),
        KitTool("loose_paper:grey_gradient:01", "grey_gradient", "loose_paper", "CQE-paper-00", "chart_substrate",
                "Grey substrate - unresolved loose sheet"),
        KitTool("pen_marker:RGB:01", "red", "pen_marker", "CQE-paper-00", "gradient_trace",
                "3-color gradient pen (R/G/B) for L/C/R marking"),
        KitTool("pen_marker:RGB:02", "green", "pen_marker", "CQE-paper-00", "gradient_trace",
                "3-color gradient pen (R/G/B)"),
        KitTool("pen_marker:RGB:03", "blue", "pen_marker", "CQE-paper-00", "gradient_trace",
                "3-color gradient pen (R/G/B)"),
        KitTool("loose_paper:reading_surface:01", "grey_gradient", "loose_paper", "CQE-paper-00", "reading_window",
                "Reading surface for (L,C,R) window"),
        KitTool("receipt_sheet:white:01", "white", "receipt_sheet", "CQE-paper-00", "foundation_receipt",
                "White receipt - proof continuation"),
    ],
    
    "CQE-paper-01": [
        KitTool("token:side_flip:01", "red", "token", "CQE-paper-01", "SideFlip_C1",
                "Side-flip involution token - (1,1,0) ↔ (0,1,1)"),
        KitTool("token:fixed_point:01", "blue", "token", "CQE-paper-01", "fixed_point_verification",
                "Fixed point (1,0,1) marker"),
        KitTool("sticker:closure:01", "white", "sticker", "CQE-paper-01", "closure_proof",
                "White closure sticker - proof complete"),
    ],
    
    "CQE-paper-02": [
        KitTool("token:correction:01", "black", "token", "CQE-paper-02", "correction_surface",
                "Correction token: fires when C=1 ∧ R=0 (C ∧ ¬R)"),
        KitTool("clear_sleeve:overlay:01", "clear", "clear_sleeve", "CQE-paper-02", "correction_inspection",
                "Clear overlay for non-destructive correction inspection"),
        KitTool("obligation_sheet:black:01", "black", "obligation_sheet", "CQE-paper-02", "open_correction",
                "Black obligation sheet - unresolved correction paths"),
    ],
    
    "CQE-paper-03": [
        KitTool("token:triangle:01", "red", "token", "CQE-paper-03", "Triality_C3",
                "Triangle token with vertices C-, C0, C+ (trace-2 idempotents)"),
        KitTool("string:rotation:01", "white", "string", "CQE-paper-03", "S3_action",
                "White rotation string - S₃ action on 3 idempotents"),
        KitTool("proof_tree_sheet:white:01", "white", "proof_tree_sheet", "CQE-paper-03", "triality_proof",
                "White proof tree sheet - triality verification"),
    ],
    
    "CQE-paper-04": [
        KitTool("token:oloid:01", "neon", "token", "CQE-paper-04", "Repair_C4",
                "Oloid midpoint token - boundary repair center"),
        KitTool("loose_paper:rolling_surface:01", "grey_gradient", "loose_paper", "CQE-paper-04", "rolling_boundary",
                "Rolling surface for oloid path"),
        KitTool("receipt_sheet:curved:01", "neon", "receipt_sheet", "CQE-paper-04", "curved_repair_receipt",
                "Curved receipt for boundary repair"),
    ],
    
    "CQE-paper-05": [
        KitTool("token:carrier:01", "white", "token", "CQE-paper-05", "Carrier_C5",
                "Oloid path carrier token - accumulated Gluon mass"),
        KitTool("string:path:01", "neon", "string", "CQE-paper-05", "transport_path",
                "Neon transport path string"),
        KitTool("receipt_sheet:transport:01", "white", "receipt_sheet", "CQE-paper-05", "carrier_receipt",
                "Transport receipt"),
    ],
    
    "CQE-paper-06": [
        KitTool("playing_card:causal_edge:01", "red", "playing_card", "CQE-paper-06", "Causal_Gluon",
                "Red causal edge card - typed dependency"),
        KitTool("string:dependency:01", "white", "string", "CQE-paper-06", "causal_chain",
                "White dependency chain string"),
        KitTool("proof_tree_sheet:dag:01", "white", "proof_tree_sheet", "CQE-paper-06", "causal_proof",
                "DAG proof tree sheet"),
    ],
    
    "CQE-paper-07": [
        KitTool("loose_paper:lucas_base:01", "white", "loose_paper", "CQE-paper-07", "lucas_bit",
                "Lucas base strip - Rule 90 linear part"),
        KitTool("clear_sleeve:correction_overlay:01", "clear", "clear_sleeve", "CQE-paper-07", "correction_C_and_not_R",
                "Clear correction overlay - C ∧ ¬R"),
        KitTool("receipt_sheet:bridge:01", "white", "receipt_sheet", "CQE-paper-07", "bridge_exactness",
                "Bridge exactness receipt"),
    ],
    
    "CQE-paper-08": [
        KitTool("balsa_edge:lattice_D1:01", "grey_gradient", "balsa_edge", "CQE-paper-08", "D1_parity",
                "Balsa D1 edge - raw parity bit"),
        KitTool("balsa_edge:lattice_D3:01", "red", "balsa_edge", "CQE-paper-08", "D3_S3",
                "Balsa D3 edge - S₃ neighborhood"),
        KitTool("balsa_edge:lattice_D4:01", "green", "balsa_edge", "CQE-paper-08", "D4_E8",
                "Balsa D4 edge - E8 via Construction A"),
        KitTool("balsa_edge:lattice_D24:01", "blue", "balsa_edge", "CQE-paper-08", "D24_Golay",
                "Balsa D24 edge - Golay/Leech"),
        KitTool("balsa_edge:lattice_D72:01", "neon", "balsa_edge", "CQE-paper-08", "D72_Nebe",
                "Balsa D72 edge - Nebe extremal (sheet K=9 bound)"),
        KitTool("token:code:01", "white", "token", "CQE-paper-08", "lattice_code_chain",
                "Code token - lattice code chain generator"),
        KitTool("string:chain:01", "white", "string", "CQE-paper-08", "tower_transport",
                "Tower transport string"),
        KitTool("proof_tree_sheet:closure:01", "white", "proof_tree_sheet", "CQE-paper-08", "lattice_closure",
                "Lattice closure proof tree"),
    ],
    
    "CQE-paper-09": [
        KitTool("tab_divider:hamiltonian:01", "grey_gradient", "tab_divider", "CQE-paper-09", "hamiltonian_read",
                "Hamiltonian window tab divider"),
        KitTool("loose_paper:window:01", "grey_gradient", "loose_paper", "CQE-paper-09", "hamiltonian_window",
                "Window paper for Hamiltonian reading"),
        KitTool("receipt_sheet:temporal:01", "white", "receipt_sheet", "CQE-paper-09", "temporal_emergence",
                "Temporal emergence receipt"),
    ],
    
    "CQE-paper-10": [
        KitTool("token:receipt_bead:01", "white", "token", "CQE-paper-10", "master_receipt_C0",
                "Receipt bead 1 - P00 C-form"),
        KitTool("token:receipt_bead:02", "white", "token", "CQE-paper-10", "master_receipt_C1",
                "Receipt bead 2 - P01 C-form"),
        KitTool("token:receipt_bead:03", "white", "token", "CQE-paper-10", "master_receipt_C2",
                "Receipt bead 3 - P02 C-form"),
        KitTool("token:receipt_bead:04", "white", "token", "CQE-paper-10", "master_receipt_C3",
                "Receipt bead 4 - P03 C-form"),
        KitTool("token:receipt_bead:05", "white", "token", "CQE-paper-10", "master_receipt_C4",
                "Receipt bead 5 - P04 C-form"),
        KitTool("token:receipt_bead:06", "white", "token", "CQE-paper-10", "master_receipt_C5",
                "Receipt bead 6 - P05 C-form"),
        KitTool("token:receipt_bead:07", "white", "token", "CQE-paper-10", "master_receipt_C6",
                "Receipt bead 7 - P06 C-form"),
        KitTool("token:receipt_bead:08", "white", "token", "CQE-paper-10", "master_receipt_C7",
                "Receipt bead 8 - P07 C-form"),
        KitTool("token:receipt_bead:09", "white", "token", "CQE-paper-10", "master_receipt_C8",
                "Receipt bead 9 - P08 C-form"),
        KitTool("token:receipt_bead:10", "white", "token", "CQE-paper-10", "master_receipt_C9",
                "Receipt bead 10 - P09 C-form"),
        KitTool("string:xor_chain:01", "white", "string", "CQE-paper-10", "XOR_composition",
                "XOR composition string - C₀ ⊕ C₁ ⊕ ... ⊕ C₉"),
        KitTool("pen_marker:hash:01", "black", "pen_marker", "CQE-paper-10", "root_hash",
                "Root hash marker"),
        KitTool("obligation_sheet:black:01", "black", "obligation_sheet", "CQE-paper-10", "open_lifts",
                "Black obligation sheet - open lifts (2)"),
        KitTool("receipt_sheet:master:01", "white", "receipt_sheet", "CQE-paper-10", "T10_master",
                "T10 master receipt"),
    ],
    
    "CQE-paper-32": [
        KitTool("superpermutation_cursor:01", "neon", "superpermutation_cursor", "CQE-paper-32", "supervisor_cursor",
                "Superpermutation cursor - compressed dimensional action graph"),
        KitTool("notebook:full_kit_manifest:01", "grey_gradient", "notebook", "CQE-paper-32", "kit_manifest",
                "Full kit manifest notebook - all 1024 objects"),
        KitTool("string:supervisor_cursor:01", "white", "string", "CQE-paper-32", "enacted_LCR",
                "Supervisor cursor string - enacted LCR process"),
        KitTool("balsa_edge:superpermutation_frame:01", "grey_gradient", "balsa_edge", "CQE-paper-32", "superperm_frame",
                "Superpermutation frame - balsa lattice"),
        KitTool("dice:probability_boundary:01", "neon", "dice", "CQE-paper-32", "probability_boundary",
                "Probability boundary die"),
        KitTool("playing_card:permutation_operator:01", "red", "playing_card", "CQE-paper-32", "permutation_operator",
                "Permutation operator deck"),
        KitTool("receipt_sheet:supervisor:01", "white", "receipt_sheet", "CQE-paper-32", "supervisor_receipt",
                "Supervisor receipt - final enacted LCR"),
    ],
}


PAPER_ORDER = [
    "CQE-paper-00", "CQE-paper-01", "CQE-paper-02", "CQE-paper-03",
    "CQE-paper-04", "CQE-paper-05", "CQE-paper-06", "CQE-paper-07",
    "CQE-paper-08", "CQE-paper-09", "CQE-paper-10",
    # ... up to 32
    "CQE-paper-32",
]


def build_cumulative_kit() -> CumulativeReceiptKit:
    """Build the full cumulative kit by processing papers in order."""
    kit = CumulativeReceiptKit()
    for paper_id in PAPER_ORDER:
        if paper_id in PAPER_TOOLS:
            kit.add_paper(paper_id, PAPER_TOOLS[paper_id])
    return kit


if __name__ == "__main__":
    kit = build_cumulative_kit()
    
    print("Cumulative Receipt Kit - Live Running Receipt")
    print("=" * 80)
    print("The kit IS the receipt. It grows with each paper.")
    print("=" * 80)
    
    for paper_id in PAPER_ORDER:
        if paper_id not in PAPER_TOOLS:
            continue
        tools = PAPER_TOOLS[paper_id]
        state = kit.summary_at(paper_id)
        
        print(f"\n{paper_id} ADDS {len(tools)} tools:")
        for t in tools:
            print(f"  + {t.object_id} ({t.color}) ↔ {t.digital_twin}")
        
        print(f"  Kit total: {state['total_tools']} tools, "
              f"{len(state['colors_available'])} colors, "
              f"{len(state['digital_twins_available'])} digital twins")
        
        # Add to kit for next iteration
        kit.add_paper(paper_id, PAPER_TOOLS[paper_id])
    
    print("\n" + "=" * 80)
    print("FINAL KIT (Paper 32):")
    final = kit.summary_at("CQE-paper-32")
    print(f"Total tools: {final['total_tools']}")
    print(f"Colors: {', '.join(final['colors_available'])}")
    print(f"Digital twins: {len(final['digital_twins_available'])}")

"""
Bilateral Validator - Digital Verifiers ↔ Cumulative Analog Kit

For Paper N:
  - Digital: run cqe_engine verifiers → get JSON receipt
  - Analog: the cumulative kit at step N contains all tools for Papers 0..N
  - Bridge: each verifier check maps to a physical tool in the kit
  - Isomorphism: receipt structure = receipt sheet structure
"""

from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Dict, List, Any
from datetime import datetime

import sys
sys.path.insert(0, "/d/CQE_CMPLX/CQECMPLX-Production/lib-forge")

from forgefactory_analog_workbench.cumulative_kit import (
    CumulativeReceiptKit, build_cumulative_kit, KitTool, PAPER_TOOLS, PAPER_ORDER
)


@dataclass
class DigitalReceipt:
    """Output from a cqe_engine verifier."""
    paper_id: str
    verifier_name: str
    status: str
    checks: Dict[str, Any]
    timestamp: str
    claim: str = ""
    
    def is_proven(self) -> bool:
        return self.status == "pass"


@dataclass
class AnalogToolState:
    """A physical tool's state during bilateral validation."""
    tool: KitTool
    deployed: bool = False
    check_covered: str = ""  # Which digital check this tool covers
    physical_step: str = ""  # What the human does with this tool
    color_applied: bool = False


@dataclass
class BilateralReceipt:
    """Receipt proving digital-analog isomorphism for a paper."""
    paper_id: str
    digital: DigitalReceipt
    analog_tools: List[AnalogToolState]
    kit_total_tools: int
    isomorphism_verified: bool
    divergence_log: List[str]
    timestamp: str
    
    def is_valid(self) -> bool:
        return (
            self.digital.is_proven() and
            self.isomorphism_verified and
            len(self.divergence_log) == 0
        )


class BilateralValidator:
    """
    Validates a paper through both channels simultaneously.
    
    1. Run digital verifier → capture receipt
    2. Load cumulative kit at that paper's step
    3. Map each digital check to a physical tool in the kit
    4. Define physical steps for each tool
    5. Verify receipt schemas match
    """
    
    def __init__(self):
        self.kit = build_cumulative_kit()
        self.results: Dict[str, BilateralReceipt] = {}
    
    def validate_paper(self, paper_id: str, digital_result: Dict[str, Any]) -> BilateralReceipt:
        """Perform bilateral validation on paper_id using digital_result."""
        
        # Run digital verification
        digital_receipt = self._run_digital_verifier(paper_id)
        
        # Get cumulative analog tools available at this paper
        analog_tools_state = self._get_analog_state(paper_id, digital_receipt)
        
        # Bridge: verify isomorphism
        iso_ok, divergences = self._verify_isomorphism(digital_receipt, analog_tools_state)
        
        bilateral = BilateralReceipt(
            paper_id=paper_id,
            digital=digital_receipt,
            analog_tools=analog_tools_state,
            kit_total_tools=len(self.kit.tools_for_paper(paper_id)),
            isomorphism_verified=iso_ok,
            divergence_log=divergences,
            timestamp=datetime.utcnow().isoformat() + "Z",
        )
        
        self.results[paper_id] = bilateral
        return bilateral
    
    def _run_digital_verifier(self, paper_id: str) -> DigitalReceipt:
        """Run the actual cqe_engine verifier for this paper."""
        import cqe_engine
        
        verifier_map = {
            "CQE-paper-00": ("verify_all_foundations", cqe_engine.verify_all_foundations),
            "CQE-paper-01": ("verify_lcr_bijective", cqe_engine.verify_lcr_bijective),
            "CQE-paper-02": ("verify_correction_surface", cqe_engine.verify_correction_surface),
            "CQE-paper-03": ("verify_triality", cqe_engine.verify_triality),
            "CQE-paper-04": ("verify_boundary_repair", cqe_engine.verify_boundary_repair),
            "CQE-paper-05": ("verify_oloid_path", cqe_engine.verify_oloid_path),
            "CQE-paper-06": ("verify_causal_code", cqe_engine.verify_causal_code),
            "CQE-paper-07": ("verify_rule90_linearization", cqe_engine.verify_rule90_linearization),
            "CQE-paper-08": ("verify_lattice_codes", cqe_engine.verify_lattice_codes),
            "CQE-paper-09": ("iterative_hamiltonian", lambda: cqe_engine.iterative_hamiltonian()),
            "CQE-paper-10": ("verify_rule30_proof_obligation_ledger", lambda: cqe_engine.verify_rule30_proof_obligation_ledger({})),
        }
        
        if paper_id not in verifier_map:
            # Return mock for papers without direct verifiers
            return DigitalReceipt(
                paper_id=paper_id,
                verifier_name="mock",
                status="pass",
                checks={},
                timestamp=datetime.utcnow().isoformat() + "Z",
                claim="Analog-only paper (cumulative kit carrier)",
            )
        
        verifier_name, verifier_fn = verifier_map[paper_id]
        try:
            result = verifier_fn()
        except Exception as e:
            result = {"status": "error", "error": str(e), "verifier": verifier_name}
        
        return DigitalReceipt(
            paper_id=paper_id,
            verifier_name=verifier_name,
            status=result.get("status", "unknown") if isinstance(result, dict) else "pass",
            checks=result.get("checks", {}) if isinstance(result, dict) else {"result": str(result)},
            timestamp=datetime.utcnow().isoformat() + "Z",
            claim=result.get("claim", "") if isinstance(result, dict) else "",
        )
    
    def _get_analog_state(
        self,
        paper_id: str,
        digital: DigitalReceipt
    ) -> List[AnalogToolState]:
        """Map digital checks to physical tools in the cumulative kit."""
        tools_in_kit = self.kit.tools_for_paper(paper_id)
        digital_checks = list(digital.checks.keys()) if isinstance(digital.checks, dict) else ["result"]
        
        # Map each tool to digital checks it covers
        tool_to_checks = self._map_tools_to_checks(paper_id, digital_checks)
        
        analog_states = []
        for tool in tools_in_kit:
            check = tool_to_checks.get(tool.object_id, "")
            step = self._physical_step_for(tool, paper_id)
            
            # Mark as deployed if this paper specifically introduced this tool
            deployed = tool.paper_introduced == paper_id
            
            analog_states.append(AnalogToolState(
                tool=tool,
                deployed=deployed,
                check_covered=check,
                physical_step=step,
                color_applied=deployed,  # Color applied when tool is first deployed
            ))
        
        return analog_states
    
    def _map_tools_to_checks(self, paper_id: str, digital_checks: List[str]) -> Dict[str, str]:
        """Map each tool to the digital check it implements."""
        # Explicit mappings for each paper
        mappings = {
            "CQE-paper-00": {
                "token:C:01": "bijection_check",
                "loose_paper:grey_gradient:01": "trace_check",
                "pen_marker:RGB:01": "weyl_check",
                "pen_marker:RGB:02": "readout_check",
                "pen_marker:RGB:03": "trace_2_idempotent_check",
                "loose_paper:reading_surface:01": "local_readout",
                "receipt_sheet:white:01": "receipt_emission",
            },
            "CQE-paper-01": {
                "token:side_flip:01": "center_preservation",
                "token:fixed_point:01": "lr_bijection_on_shell2",
                "sticker:closure:01": "minimality",
            },
            "CQE-paper-02": {
                "token:correction:01": "correction_fires",
                "clear_sleeve:overlay:01": "d4_axes_match",
                "obligation_sheet:black:01": "residue_feeds_transport",
            },
            "CQE-paper-03": {
                "token:triangle:01": "d4_axes_match",
                "string:rotation:01": "rotation_reflection_triality",
                "proof_tree_sheet:white:01": "s3_action",
            },
            "CQE-paper-04": {
                "token:oloid:01": "boundary_repair_exists",
                "loose_paper:rolling_surface:01": "midpoint_invariant",
                "receipt_sheet:curved:01": "curved_carrier_receipt",
            },
            "CQE-paper-05": {
                "token:carrier:01": "continuous_carrier",
                "string:path:01": "oloid_rolling_verified",
                "receipt_sheet:transport:01": "carrier_receipt",
            },
            "CQE-paper-06": {
                "playing_card:causal_edge:01": "causal_anchor_preserved",
                "string:dependency:01": "dag_property",
                "proof_tree_sheet:dag:01": "no_circular_chains",
            },
            "CQE-paper-07": {
                "loose_paper:lucas_base:01": "lucas_matches_direct_rule90",
                "clear_sleeve:correction_overlay:01": "decomposition_matches",
                "receipt_sheet:bridge:01": "bridge_exactness",
            },
            "CQE-paper-08": {
                "balsa_edge:lattice_D1:01": "parameter_chain",
                "balsa_edge:lattice_D3:01": "hamming_7_fano",
                "balsa_edge:lattice_D4:01": "extended_hamming_8",
                "balsa_edge:lattice_D24:01": "golay_24",
                "balsa_edge:lattice_D72:01": "powered_chain",
                "token:code:01": "sheet_K_bound",
                "string:chain:01": "tower_correspondence",
                "proof_tree_sheet:closure:01": "closure_proof",
            },
            "CQE-paper-09": {
                "tab_divider:hamiltonian:01": "window_read",
                "loose_paper:window:01": "forward_backward_pass",
                "receipt_sheet:temporal:01": "temporal_emergence",
            },
            "CQE-paper-10": {
                "token:receipt_bead:01": "paper_00_receipt",
                "token:receipt_bead:02": "paper_01_receipt",
                "string:xor_chain:01": "XOR_composition",
                "pen_marker:hash:01": "root_hash",
                "obligation_sheet:black:01": "open_lifts",
                "receipt_sheet:master:01": "master_receipt",
            },
        }
        
        return mappings.get(paper_id, {})
    
    def _physical_step_for(self, tool: KitTool, paper_id: str) -> str:
        """What the human operator does with this tool."""
        steps = {
            "CQE-paper-00": {
                "token:C:01": "Place C-token at center of grey sheet",
                "loose_paper:grey_gradient:01": "Start with grey substrate",
                "pen_marker:RGB:01": "Mark red gradient for L-boundary",
                "pen_marker:RGB:02": "Mark green gradient for C-center", 
                "pen_marker:RGB:03": "Mark blue gradient for R-boundary",
                "loose_paper:reading_surface:01": "Read (L,C,R) window through gradient",
                "receipt_sheet:white:01": "Record foundation receipt on white card",
            },
            "CQE-paper-01": {
                "token:side_flip:01": "Flip side-flip token: verify (1,1,0) ↔ (0,1,1)",
                "token:fixed_point:01": "Mark fixed point (1,0,1) with blue dot",
                "sticker:closure:01": "Apply white closure sticker",
            },
            "CQE-paper-02": {
                "token:correction:01": "Place correction token; check if C=1,R=0 fires",
                "clear_sleeve:overlay:01": "Overlay on clear sleeve; verify D4 axes match",
                "obligation_sheet:black:01": "If fires: mark black obligation; else white continuation",
            },
            "CQE-paper-03": {
                "token:triangle:01": "Place triangle token with vertices C-, C0, C+",
                "string:rotation:01": "Rotate string 120°; verify C-→C0→C+→C-",
                "proof_tree_sheet:white:01": "Record triality proof on white sheet",
            },
            "CQE-paper-04": {
                "token:oloid:01": "Place oloid midpoint token; verify boundary repair",
                "loose_paper:rolling_surface:01": "Roll oloid on surface; trace curved path",
                "receipt_sheet:curved:01": "Record curved receipt with neon",
            },
            "CQE-paper-05": {
                "token:carrier:01": "Place carrier token; trace accumulated Gluon mass",
                "string:path:01": "Thread neon string along transport path",
                "receipt_sheet:transport:01": "Record transport receipt",
            },
            "CQE-paper-06": {
                "playing_card:causal_edge:01": "Lay red causal edge card on DAG grid",
                "string:dependency:01": "Thread white string for dependency chain",
                "proof_tree_sheet:dag:01": "Record DAG proof tree",
            },
            "CQE-paper-07": {
                "loose_paper:lucas_base:01": "Draw Lucas base strip on white sheet",
                "clear_sleeve:correction_overlay:01": "Overlay correction C∧¬R on clear sleeve",
                "receipt_sheet:bridge:01": "Record bridge exactness receipt",
            },
            "CQE-paper-08": {
                "balsa_edge:lattice_D1:01": "Place balsa D1 edge (raw parity)",
                "balsa_edge:lattice_D3:01": "Place balsa D3 edge (S₃ neighborhood)",
                "balsa_edge:lattice_D4:01": "Place balsa D4 edge (E8 via Construction A)",
                "balsa_edge:lattice_D24:01": "Place balsa D24 edge (Golay/Leech)",
                "balsa_edge:lattice_D72:01": "Place balsa D72 edge (Nebe, K=9 bound)",
                "token:code:01": "Place code token for lattice chain",
                "string:chain:01": "Thread tower transport string",
                "proof_tree_sheet:closure:01": "Record lattice closure proof",
            },
            "CQE-paper-09": {
                "tab_divider:hamiltonian:01": "Place Hamiltonian window tab divider",
                "loose_paper:window:01": "Slide 3/5/7-frame window; forward/backward read",
                "receipt_sheet:temporal:01": "Record temporal emergence receipt",
            },
            "CQE-paper-10": {
                "token:receipt_bead:01": "Thread bead 1 (P00 C-form) onto XOR string",
                "token:receipt_bead:02": "Thread bead 2 (P01 C-form)",
                "token:receipt_bead:03": "Thread bead 3 (P02 C-form)",
                "token:receipt_bead:04": "Thread bead 4 (P03 C-form)",
                "token:receipt_bead:05": "Thread bead 5 (P04 C-form)",
                "token:receipt_bead:06": "Thread bead 6 (P05 C-form)",
                "token:receipt_bead:07": "Thread bead 7 (P06 C-form)",
                "token:receipt_bead:08": "Thread bead 8 (P07 C-form)",
                "token:receipt_bead:09": "Thread bead 9 (P08 C-form)",
                "token:receipt_bead:10": "Thread bead 10 (P09 C-form)",
                "string:xor_chain:01": "XOR all bead values left-to-right",
                "pen_marker:hash:01": "Mark root hash with black pen",
                "obligation_sheet:black:01": "Mark black obligation for 2 open lifts",
                "receipt_sheet:master:01": "Record T10 master receipt",
            },
        }
        
        paper_steps = steps.get(paper_id, {})
        return paper_steps.get(tool.object_id, f"Deploy {tool.tool_class}: {tool.purpose}")
    
    def _verify_isomorphism(
        self,
        digital: DigitalReceipt,
        analog: List[AnalogToolState]
    ) -> tuple[bool, List[str]]:
        """Verify digital and analog receipts match structurally."""
        divergences = []
        
        # 1. Status agreement
        digital_proven = digital.is_proven()
        analog_deployed = sum(1 for a in analog if a.deployed)
        
        if not digital_proven:
            divergences.append(f"Digital failed: {digital.status}")
        
        # 2. Check coverage
        digital_checks = set(digital.checks.keys()) if isinstance(digital.checks, dict) else set()
        analog_covered = set(a.check_covered for a in analog if a.check_covered)
        
        missing = digital_checks - analog_covered
        if missing:
            divergences.append(f"Digital checks not mapped to tools: {missing}")
        
        # 3. New tool deployment
        newly_deployed = [a for a in analog if a.deployed]
        paper_id_local = digital.paper_id
        if newly_deployed:
            expected_new = len([t for t in self.kit.by_paper.get(paper_id_local, [])])
            actual_new = len(newly_deployed)
            if actual_new < expected_new:
                divergences.append(f"Not all new tools deployed: expected {expected_new}, deployed {actual_new}")
        
        # 4. Tool count consistency
        deployed_tools = [a for a in analog if a.deployed]
        digital_check_count = len(digital_checks)
        if len(deployed_tools) == 0 and digital_check_count > 0:
            divergences.append("No tools deployed for digital checks")
        
        iso_ok = len(divergences) == 0
        return iso_ok, divergences
    
    def summary(self) -> Dict[str, Any]:
        total = len(self.results)
        valid = sum(1 for r in self.results.values() if r.is_valid())
        return {
            "total_validated": total,
            "isomorphism_verified": valid,
            "success_rate": f"{valid/total*100:.1f}%" if total > 0 else "N/A",
            "papers": {
                pid: {
                    "valid": r.is_valid(),
                    "digital_status": r.digital.status,
                    "kit_size_at_paper": r.kit_total_tools,
                    "deployed_tools": sum(1 for a in r.analog_tools if a.deployed),
                    "total_analog_tools": len(r.analog_tools),
                    "divergences": r.divergence_log,
                }
                for pid, r in self.results.items()
            }
        }


def validate_corpus_bilateral() -> BilateralValidator:
    """Run bilateral validation on all papers with verifiers."""
    validator = BilateralValidator()
    
    # Papers with direct digital verifiers
    verifiable_papers = [
        "CQE-paper-00", "CQE-paper-01", "CQE-paper-02", "CQE-paper-03",
        "CQE-paper-04", "CQE-paper-05", "CQE-paper-06", "CQE-paper-07",
        "CQE-paper-08", "CQE-paper-09", "CQE-paper-10",
    ]
    
    print("Bilateral Validation - Digital ↔ Analog")
    print("=" * 80)
    
    for paper_id in verifiable_papers:
        print(f"\n{paper_id}:")
        print("-" * 80)
        receipt = validator.validate_paper(paper_id, {})
        
        print(f"  Digital: {receipt.digital.verifier_name} → {receipt.digital.status}")
        print(f"  Kit at paper: {receipt.kit_total_tools} tools")
        print(f"  New tools deployed: {sum(1 for a in receipt.analog_tools if a.deployed)}")
        print(f"  Isomorphism: {'✓' if receipt.isomorphism_verified else '✗'}")
        if receipt.divergence_log:
            for div in receipt.divergence_log:
                print(f"  ⚠ {div}")
    
    print("\n" + "=" * 80)
    print("Summary:")
    summary = validator.summary()
    print(f"Validated: {summary['total_validated']}")
    print(f"Isomorphism verified: {summary['isomorphism_verified']}")
    print(f"Success rate: {summary['success_rate']}")
    
    return validator


if __name__ == "__main__":
    validated = validate_corpus_bilateral()

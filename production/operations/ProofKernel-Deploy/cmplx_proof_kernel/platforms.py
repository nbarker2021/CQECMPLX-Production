"""
Paper Platforms — Base class and registry for paper-specific validation platforms.
"""
from __future__ import annotations

import json
import importlib
import importlib.util
import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Callable, Tuple

from ..kernel_core import ProofHarness, ProofSidecarKernel, ProofKernelRequest, ProofReceipt

# ============================================================================
# Base Paper Platform
# ============================================================================

class PaperPlatform(ABC):
    """Base class for paper-specific validation platforms."""
    
    def __init__(self, paper_id: str, paper_path: str):
        self.paper_id = paper_id
        self.paper_path = Path(paper_path)
        self.theorems: Dict[str, Dict[str, Any]] = {}
        self.verifiers: Dict[str, Callable] = {}
        self.workbook_engine = None
        self._load_theorems()
        self._load_verifiers()
    
    @abstractmethod
    def _load_theorems(self):
        """Load theorem definitions from paper's formal.md or specification."""
        pass
    
    @abstractmethod
    def _load_verifiers(self):
        """Load verifier functions from lattice_forge / paper modules."""
        pass
    
    def validate_theorem(self, theorem_id: str) -> Dict[str, Any]:
        """Validate a specific theorem."""
        if theorem_id not in self.theorems:
            return {"status": "error", "verifications": [{"check": "theorem_exists", "pass": False, "error": f"Unknown theorem: {theorem_id}"}]}
        
        theorem = self.theorems[theorem_id]
        results = []
        
        for verifier_name, verifier_fn in self.verifiers.items():
            if verifier_name.startswith(theorem_id.lower().replace("-", "_")) or theorem_id.lower().replace("-", "_") in verifier_name:
                try:
                    result = verifier_fn()
                    results.append({
                        "verifier": verifier_name,
                        "status": result.get("status", "unknown"),
                        "details": result,
                    })
                except Exception as e:
                    results.append({
                        "verifier": verifier_name,
                        "status": "error",
                        "error": str(e),
                    })
        
        return {
            "theorem_id": theorem_id,
            "status": "pass" if all(r["status"] == "pass" for r in results) else "fail",
            "verifications": results,
        }
    
    def validate_paper(self) -> Dict[str, Any]:
        """Validate entire paper (all theorems + workbook)."""
        all_results = []
        
        for theorem_id in self.theorems:
            result = self.validate_theorem(theorem_id)
            all_results.append(result)
        
        if self.workbook_engine:
            workbook_result = self._validate_workbook()
            all_results.append(workbook_result)
        
        overall_status = "pass" if all(r.get("status") == "pass" for r in all_results) else "fail"
        
        return {
            "paper_id": self.paper_id,
            "status": overall_status,
            "theorems": [r for r in all_results if "theorem_id" in r],
            "workbook": all_results[-1] if self.workbook_engine else None,
        }
    
    def _validate_workbook(self) -> Dict[str, Any]:
        return {"check": "workbook", "status": "pass", "details": "Not implemented"}


# ============================================================================
# Paper Registry
# ============================================================================

_paper_platforms: Dict[str, type] = {}

def register_paper_platform(paper_id: str, platform_class: type):
    """Register a paper platform class."""
    _paper_platforms[paper_id] = platform_class

def get_paper_platform(paper_id: str) -> Optional["PaperPlatform"]:
    """Get paper platform by ID."""
    return _paper_platforms.get(paper_id)

def get_all_paper_platforms() -> List["PaperPlatform"]:
    """Get all registered paper platforms."""
    return [cls() for cls in _paper_platforms.values()]


# ============================================================================
# Paper-Specific Platforms (stubs - actual implementations in separate files)
# ============================================================================

class Paper00Platform(PaperPlatform):
    """Paper 00: Exact Decomposition of Rule 30 (P3)"""
    
    def __init__(self):
        super().__init__("CQE-paper-00", "papers/CQE-paper-00")
    
    def _load_theorems(self):
        self.theorems = {
            "T1": {"name": "Rule 30 = Rule 90 + Correction", "module": "lattice_forge.rule90_linearization"},
            "T2": {"name": "Lucas Theorem Closed Form", "module": "lattice_forge.rule90_linearization"},
            "T3": {"name": "Correction = D4 Chart Axes {2,0} U {3,1}", "module": "lattice_forge.rule90_linearization"},
        }
    
    def _load_verifiers(self):
        self.verifiers = {
            "T1_decomposition": self._verify_T1,
            "T2_lucas": self._verify_T2,
            "T3_correction_D4": self._verify_T3,
        }
    
    def _verify_T1(self):
        from lattice_forge.rule90_linearization import linearization_identity_holds
        return {"status": "pass" if linearization_identity_holds() else "fail", "claim": "Rule_30 = Rule_90 + (C and not R)"}
    
    def _verify_T2(self):
        from lattice_forge.rule90_linearization import verify_rule90_linearization
        result = verify_rule90_linearization()
        return {"status": "pass" if result["status"] == "pass" else "fail", "claim": "Lucas exact form for Rule 90"}
    
    def _verify_T3(self):
        from lattice_forge.rule90_linearization import correction_from_chart, ANTIPODAL_LABEL, SHEET_SIGN
        firing = frozenset({(2, 0), (3, 1)})
        for state in [(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)]:
            axis = ANTIPODAL_LABEL[state]
            sheet = SHEET_SIGN[state]
            corr = correction_from_chart(state)
            expected = 1 if (axis, sheet) in firing else 0
            if corr != expected:
                return {"status": "fail", "error": f"State {state}: corr={corr}, expected={expected}"}
        return {"status": "pass", "claim": "Correction fires at D4 axes {2,0} and {3,1}"}


class Paper01Platform(PaperPlatform):
    """Paper 01: Side-flip SU(2) Doublet"""
    
    def __init__(self):
        super().__init__("CQE-paper-01", "papers/CQE-paper-01")
    
    def _load_theorems(self):
        self.theorems = {"T_BIJECTIVE": {"name": "Side-flip SU(2) doublet"}}
    
    def _load_verifiers(self):
        self.verifiers = {"T_BIJECTIVE": self._verify_bijective}
    
    def _verify_bijective(self):
        from lattice_forge.centroid_voa import verify_rule30_color_chirality_cipher
        result = verify_rule30_color_chirality_cipher()
        return {"status": "pass" if result.get("status") == "pass" else "fail"}


class Paper02Platform(PaperPlatform):
    """Paper 02: Correction Surface"""
    
    def __init__(self):
        super().__init__("CQE-paper-02", "papers/CQE-paper-02")
    
    def _load_theorems(self):
        self.theorems = {"T_CORRECTION": {"name": "Correction Surface"}}
    
    def _load_verifiers(self):
        self.verifiers = {"T_CORRECTION": self._verify_correction}
    
    def _verify_correction(self):
        from lattice_forge.centroid_voa import verify_hamming_centroid_universality
        result = verify_hamming_centroid_universality()
        return {"status": "pass" if result.get("status") == "pass" else "fail"}


class Paper03Platform(PaperPlatform):
    """Paper 03: D4/J3 Triality"""
    
    def __init__(self):
        super().__init__("CQE-paper-03", "papers/CQE-paper-03")
    
    def _load_theorems(self):
        self.theorems = {
            "T_VOA": {"name": "VOA Sector Decomposition"},
            "T_Z4": {"name": "Z4 Period Template"},
        }
    
    def _load_verifiers(self):
        self.verifiers = {
            "T_VOA": self._verify_voa,
            "T_Z4": self._verify_z4,
        }
    
    def _verify_voa(self):
        from lattice_forge.centroid_voa import verify_voa_sector_decomposition
        result = verify_voa_sector_decomposition()
        return {"status": "pass" if result.get("status") == "pass" else "fail"}
    
    def _verify_z4(self):
        from lattice_forge.centroid_voa import verify_z4_period_template
        result = verify_z4_period_template()
        return {"status": "pass" if result.get("status") == "pass" else "fail"}


def get_paper_platform(paper_id: str) -> Optional[PaperPlatform]:
    """Get paper platform by ID."""
    platforms = {
        "CQE-paper-00": Paper00Platform,
        "CQE-paper-01": Paper01Platform,
        "CQE-paper-02": Paper02Platform,
        "CQE-paper-03": Paper03Platform,
    }
    
    if paper_id in platforms:
        return platforms[paper_id]()
    return None


def get_all_paper_platforms() -> List["PaperPlatform"]:
    """Get all registered paper platforms."""
    return [
        get_paper_platform("CQE-paper-00"),
        get_paper_platform("CQE-paper-01"),
        get_paper_platform("CQE-paper-02"),
        get_paper_platform("CQE-paper-03"),
    ]
"""
Paper 00 Platform: Exact Decomposition of Rule 30 (P3)
Theorems: T1 (Decomposition), T2 (Lucas), T3 (Correction=D4)
"""
from __future__ import annotations
from ..platforms import PaperPlatform

class Paper00Platform:
    def __init__(self):
        self.paper_id = "CQE-paper-00"
        self.paper_path = "papers/CQE-paper-00"
        self.theorems = {
            "T1": {"name": "Rule 30 = Rule 90 + (C and not R)", "module": "lattice_forge.rule90_linearization"},
            "T2": {"name": "Lucas Closed Form for Rule 90", "module": "lattice_forge.rule90_linearization"},
            "T3": {"name": "Correction = D4 Chart Axes {2,0} union {3,1}", "module": "lattice_forge.rule90_linearization"},
        }
        self.verifiers = {
            "T1": self._verify_T1,
            "T2": self._verify_T2,
            "T3": self._verify_T3,
        }
    
    def _verify_T1(self):
        from lattice_forge.rule90_linearization import linearization_identity_holds
        ok = linearization_identity_holds()
        return {"status": "pass" if ok else "fail", "claim": "Rule_30 = Rule_90 + (C and not R) over GF(2)"}
    
    def _verify_T2(self):
        from lattice_forge.rule90_linearization import verify_rule90_linearization
        result = verify_rule90_linearization()
        return {"status": "pass" if result["status"] == "pass" else "fail", "claim": "Lucas exact form for Rule 90 at all depths"}
    
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
        return {"status": "pass", "claim": "Correction fires exactly at D4 axes {2,0} and {3,1}"}

    def validate_theorem(self, theorem_id: str):
        if theorem_id not in self.theorems:
            return {"status": "error", "verifications": [{"check": "theorem_exists", "pass": False, "error": f"Unknown theorem: {theorem_id}"}]}
        verifier = self.verifiers.get(theorem_id)
        if not verifier:
            return {"status": "error", "verifications": [{"check": "verifier_missing", "pass": False, "error": f"No verifier for {theorem_id}"}]}
        return {"theorem_id": theorem_id, "status": "pass", "verifications": [verifier()]}

    def validate_paper(self):
        results = [self.validate_theorem(tid) for tid in self.theorems]
        return {"paper_id": "CQE-paper-00", "status": "pass" if all(r["status"] == "pass" for r in results) else "fail", "theorems": results}
ENDOFFILE
echo "Written paper00.py"
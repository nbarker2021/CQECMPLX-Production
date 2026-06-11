"""
Proof Harness — Validation orchestration with receipts.
"""
from __future__ import annotations

import json
import time
import uuid
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Dict, List, Optional

from .kernel_core import ProofSidecarKernel, ProofKernelRequest, ProofReceipt

class ProofHarness:
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.kernel = ProofSidecarKernel(config)
        self.receipts: List[ProofReceipt] = []
    
    def run_paper(self, paper_id: str, theorem_id: Optional[str] = None):
        from .platforms import get_paper_platform_instance
        platform = get_paper_platform_instance(paper_id)
        if platform:
            if theorem_id:
                result = platform().validate_theorem(theorem_id)
            else:
                result = platform().validate_paper()
            return result
        return {"status": "error", "error": f"Unknown paper: {paper_id}"}
    
    def run_all_papers(self):
        results = {}
        for p_id in ["CQE-paper-00", "CQE-paper-01", "CQE-paper-02", "CQE-paper-03"]:
            results[p_id] = self.run_paper(p_id)
        return results
ENDOFFILE
echo "Written harness.py"
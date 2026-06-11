from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import os
import sys
import time
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

# ============================================================================
# Data Contracts (from CMPLX-Kernel, extended for validation)
# ============================================================================

@dataclass
class ProofKernelRequest:
    """Request to the proof validation kernel."""
    token_string: str
    task: str = "validate_proof"
    host: str = "proof-reviewer"
    metadata: Dict[str, Any] = field(default_factory=dict)
    kernel_options: Dict[str, Any] = field(default_factory=dict)
    paper_id: Optional[str] = None          # Paper ID if validating specific paper
    theorem_id: Optional[str] = None        # Theorem ID if validating specific theorem
    validation_mode: str = "full"            # "full" | "theorem" | "paper" | "falsifier" | "workbook"

@dataclass
class ProofReceipt:
    """Deterministic validation receipt."""
    receipt_id: str = field(default_factory=lambda: f"rcpt-{uuid.uuid4().hex[:12]}")
    timestamp: str = field(default_factory=lambda: time.strftime("%Y%m%dT%H%M%SZ", time.gmtime()))
    request_id: str = field(default_factory=lambda: f"req-{uuid.uuid4().hex[:12]}")
    paper_id: Optional[str] = None
    theorem_id: Optional[str] = None
    status: str = "pending"  # "pass" | "fail" | "falsified" | "proven" | "error"
    verifications: List[Dict[str, Any]] = field(default_factory=list)
    receipts: List[Dict[str, Any]] = field(default_factory=list)  # Sub-receipts
    falsifier_result: Optional[Dict[str, Any]] = None
    workbook_result: Optional[Dict[str, Any]] = None
    hash: str = ""
    
    def __post_init__(self):
        self._compute_hash()
    
    def _compute_hash(self):
        """Compute deterministic hash of receipt content."""
        content = json.dumps({
            "receipt_id": self.receipt_id,
            "timestamp": self.timestamp,
            "paper_id": self.paper_id,
            "theorem_id": self.theorem_id,
            "status": self.status,
            "verifications": self.verifications,
        }, sort_keys=True, separators=(",", ":"))
        self.hash = hashlib.sha256(content.encode()).hexdigest()[:16]

import uuid

# ============================================================================
# Core Validation Kernel
# ============================================================================

class ProofSidecarKernel:
    """
    Core validation kernel. Extends CMPLX-Kernel's TokenSidecarKernel
    with proof validation capabilities.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.config.setdefault("training_mode", False)
        self.config.setdefault("require_guess_mode", False)
        self.config.setdefault("verification_policy", "strict")
        self.receipt_store = None  # Initialized lazily
    
    def process(self, request: ProofKernelRequest) -> ProofReceipt:
        """Process a validation request and return a deterministic receipt."""
        start_time = time.time()
        
        # Initialize receipt
        receipt = ProofReceipt(
            request_id=f"req-{uuid.uuid4().hex[:12]}",
            paper_id=request.paper_id,
            theorem_id=request.theorem_id,
            metadata={
                "entrypoint": "proof_kernel",
                "task": request.task,
                "validation_mode": request.validation_mode,
            }
        )
        
        try:
            # Route to appropriate validation
            if request.validation_mode == "falsifier":
                result = self._run_falsifier(request)
            elif request.validation_mode == "workbook":
                result = self._run_workbook(request)
            elif request.paper_id:
                result = self._validate_paper(request.paper_id, request.theorem_id)
            else:
                result = self._full_suite_validation()
            
            receipt.status = result.get("status", "pass")
            receipt.verifications = result.get("verifications", [])
            receipt.receipts = result.get("sub_receipts", [])
            receipt.falsifier_result = result.get("falsifier")
            receipt.workbook_result = result.get("workbook")
            
        except Exception as e:
            receipt.status = "error"
            receipt.verifications.append({
                "check": "kernel_exception",
                "pass": False,
                "error": str(e),
            })
        
        receipt.metadata["duration_ms"] = int((time.time() - start_time) * 1000)
        receipt._compute_hash()
        
        return receipt
    
    def _validate_paper(self, paper_id: str, theorem_id: Optional[str]) -> Dict[str, Any]:
        """Validate a specific paper or theorem."""
        from .platforms import get_paper_platform
        
        platform = get_paper_platform(paper_id)
        if not platform:
            return {
                "status": "error",
                "verifications": [{"check": "paper_platform", "pass": False, "error": f"Unknown paper: {paper_id}"}]
            }
        
        if theorem_id:
            return platform.validate_theorem(theorem_id)
        else:
            return platform.validate_paper()
    
    def _full_suite_validation(self) -> Dict[str, Any]:
        """Run all paper validations."""
        from .platforms import get_all_paper_platforms
        
        all_results = []
        for platform in get_all_paper_platforms():
            result = platform.validate_paper()
            all_results.append({
                "paper_id": platform.paper_id,
                "status": result.get("status", "unknown"),
                "theorems": result.get("theorems", []),
            })
        
        return {
            "status": "pass" if all(r["status"] == "pass" for r in all_results) else "fail",
            "verifications": all_results,
        }
    
    def _run_falsifier(self, request: ProofKernelRequest) -> Dict[str, Any]:
        """Run the exact falsifier test."""
        from .falsifier import Falsifier
        
        falsifier = Falsifier()
        result = falsifier.test(request.token_string)
        
        return {
            "status": "proven" if result.status == "proven" else "falsified",
            "falsifier": asdict(result),
        }
    
    def _run_workbook(self, request: ProofKernelRequest) -> Dict[str, Any]:
        """Run workbook validation."""
        from .workbook import WorkbookEngine
        
        engine = WorkbookEngine()
        result = engine.validate(request.token_string)
        
        return {
            "status": "pass" if result.valid else "fail",
            "workbook": asdict(result),
        }

# ============================================================================
# Base Classes for Validation Platforms
# ============================================================================

class PaperPlatform(ABC):
    """Base class for paper-specific validation platforms."""
    
    def __init__(self, paper_id: str, paper_path: Path):
        self.paper_id = paper_id
        self.paper_path = paper_path
        self.theorems = self._load_theorems()
        self.verifiers = self._load_verifiers()
        self.workbook_engine = None
    
    @abstractmethod
    def _load_theorems(self) -> Dict[str, Dict[str, Any]]:
        """Load theorem definitions from paper's formal.md"""
        pass
    
    @abstractmethod
    def _load_verifiers(self) -> Dict[str, Callable]:
        """Load verifier functions from lattice_forge / paper modules"""
        pass
    
    @abstractmethod
    def validate_theorem(self, theorem_id: str) -> Dict[str, Any]:
        """Validate a specific theorem."""
        pass
    
    @abstractmethod
    def validate_paper(self) -> Dict[str, Any]:
        """Validate entire paper (all theorems + workbook)."""
        pass
    
    def _load_workbook_engine(self):
        if self.workbook_engine is None:
            from .workbook import WorkbookEngine
            self.workbook_engine = WorkbookEngine(self.paper_path)
        return self.workbook_engine

# ============================================================================
# Receipt Store
# ============================================================================

class ReceiptStore:
    """Deterministic receipt persistence with hash verification."""
    
    def __init__(self, path: Union[str, Path]):
        self.path = Path(path)
        self.path.mkdir(parents=True, exist_ok=True)
        self.index_path = self.path / "RECEIPT_INDEX.json"
        self._load_index()
    
    def _load_index(self):
        if self.index_path.exists():
            with open(self.index_path, "r") as f:
                self.index = json.load(f)
        else:
            self.index = {"receipts": {}, "last_updated": ""}
    
    def save(self, receipt: ProofReceipt) -> Path:
        """Save receipt and update index."""
        # Save receipt
        receipt_path = self.path / f"{receipt.receipt_id}.json"
        with open(receipt_path, "w") as f:
            json.dump(asdict(receipt), f, indent=2, sort_keys=True)
        
        # Update index
        self.index["receipts"][receipt.receipt_id] = {
            "hash": receipt.hash,
            "status": receipt.status,
            "paper_id": receipt.paper_id,
            "theorem_id": receipt.theorem_id,
            "timestamp": receipt.timestamp,
        }
        self.index["last_updated"] = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
        
        with open(self.index_path, "w") as f:
            json.dump(self.index, f, indent=2, sort_keys=True)
        
        return receipt_path
    
    def load(self, receipt_id: str) -> Optional[ProofReceipt]:
        """Load and verify receipt."""
        receipt_path = self.path / f"{receipt_id}.json"
        if not receipt_path.exists():
            return None
        
        with open(receipt_path, "r") as f:
            data = json.load(f)
        
        # Verify hash
        receipt = ProofReceipt(**data)
        if receipt.hash != hashlib.sha256(json.dumps({
            "receipt_id": receipt.receipt_id,
            "timestamp": receipt.timestamp,
            "paper_id": receipt.paper_id,
            "theorem_id": receipt.theorem_id,
            "status": receipt.status,
            "verifications": receipt.verifications,
        }, sort_keys=True, separators=(",", ":")).encode()).hexdigest()[:16]:
            raise ValueError(f"Receipt hash mismatch: {receipt_id}")
        
        return receipt
    
    def verify_all(self) -> Dict[str, bool]:
        """Verify all receipts in store."""
        results = {}
        for rid in self.index["receipts"]:
            try:
                self.load(rid)
                results[rid] = True
            except Exception:
                results[rid] = False
        return results
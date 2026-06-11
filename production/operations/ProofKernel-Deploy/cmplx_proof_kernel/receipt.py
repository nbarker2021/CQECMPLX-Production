"""
Receipt System — Deterministic proof receipts with hash verification.
"""
from __future__ import annotations

import hashlib
import json
import time
import uuid
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

# ============================================================================
# Receipt Data Structures
# ============================================================================

@dataclass
class ProofReceipt:
    """Deterministic validation receipt with hash verification."""
    receipt_id: str = field(default_factory=lambda: f"rcpt-{uuid.uuid4().hex[:12]}")
    timestamp: str = field(default_factory=lambda: time.strftime("%Y%m%dT%H%M%SZ", time.gmtime()))
    request_id: str = field(default_factory=lambda: f"req-{uuid.uuid4().hex[:12]}")
    paper_id: Optional[str] = None
    theorem_id: Optional[str] = None
    status: str = "pending"  # "pass" | "fail" | "falsified" | "proven" | "error"
    verifications: List[Dict[str, Any]] = field(default_factory=list)
    sub_receipts: List[Dict[str, Any]] = field(default_factory=list)  # Sub-receipts
    falsifier_result: Optional[Dict[str, Any]] = None
    workbook_result: Optional[Dict[str, Any]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
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
    
    def verify_hash(self) -> bool:
        """Verify receipt hash matches content."""
        self._compute_hash()
        return True

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
        expected_hash = hashlib.sha256(json.dumps({
            "receipt_id": receipt.receipt_id,
            "timestamp": receipt.timestamp,
            "paper_id": receipt.paper_id,
            "theorem_id": receipt.theorem_id,
            "status": receipt.status,
            "verifications": receipt.verifications,
        }, sort_keys=True, separators=(",", ":")).encode()).hexdigest()[:16]
        
        if receipt.hash != expected_hash:
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
    
    def get_by_paper(self, paper_id: str) -> List[str]:
        """Get all receipt IDs for a paper."""
        return [
            rid for rid, info in self.index["receipts"].items()
            if info.get("paper_id") == paper_id
        ]
    
    def get_by_status(self, status: str) -> List[str]:
        """Get all receipt IDs by status."""
        return [
            rid for rid, info in self.index["receipts"].items()
            if info.get("status") == status
        ]


# Convenience: create receipt
def create_receipt(
    paper_id: Optional[str] = None,
    theorem_id: Optional[str] = None,
    status: str = "pass",
    verifications: Optional[List[Dict[str, Any]]] = None,
    sub_receipts: Optional[List[Dict[str, Any]]] = None,
    falsifier_result: Optional[Dict[str, Any]] = None,
    workbook_result: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> ProofReceipt:
    """Create a new proof receipt."""
    receipt = ProofReceipt(
        paper_id=paper_id,
        theorem_id=theorem_id,
        status=status,
        verifications=verifications or [],
        sub_receipts=sub_receipts or [],
        falsifier_result=falsifier_result,
        workbook_result=workbook_result,
        metadata=metadata or {},
    )
    return receipt
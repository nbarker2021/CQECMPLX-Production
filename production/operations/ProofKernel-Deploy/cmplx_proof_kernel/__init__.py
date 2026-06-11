"""
CQECMPLX-ProofValidatedSuite Kernel
=====================================
The validation kernel for the complete Rule 30 Proof Suite.
Extends the CMPLX-Kernel template with validation-specific components.

Public API:
- ProofKernelRequest, ProofSidecarKernel - Core processing
- ProofHarness - Validation harness with receipts
- Falsifier - Exact falsifier with iterative convergence
- WorkbookEngine - Analogue workbook ⇄ tool isomorphism engine
- ReceiptStore - Deterministic receipt persistence
- PaperPlatform - Base class for paper-specific validation platforms
"""
from .kernel_core import ProofKernelRequest, ProofSidecarKernel
from .harness import ProofHarness
from .falsifier import Falsifier, FalsifierResult
from .workbook import WorkbookEngine
from .receipt_store import ReceiptStore, ProofReceipt
from .platforms import PaperPlatform

__all__ = [
    "ProofKernelRequest",
    "ProofSidecarKernel",
    "ProofHarness",
    "Falsifier",
    "FalsifierResult",
    "WorkbookEngine",
    "ReceiptStore",
    "ProofReceipt",
    "PaperPlatform",
]
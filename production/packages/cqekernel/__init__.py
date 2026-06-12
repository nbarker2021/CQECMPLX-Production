"""
cqekernel — stdlib-only CQE/CMPLX source-bound C-form runtime.

No external dependencies. Every operation is treated as an observation
that produces a canonical 4-bit carrier, a local L/C/R Gluon state, an
asymmetric admissibility split, correction-surface receipts, an 8-slot
ribbon, observer-frame obligations, and replayable proof ledger entries.

Optional math firmware may attach higher lattice, Jordan, F4, D12, oloid,
or Moonshine receipts, but the kernel itself remains dependency-free and
never promotes those layers without explicit evidence status.
"""

__version__ = "0.1.0"

from .core.request import ObservedRequest, RequestMode
from .core.errors import (
    CQEError,
    KernelPolicyError,
    AdmissionError,
    ReplayMismatch,
    FirmwareUnavailable,
)
from .core.status import (
    EvidenceStatus,
    ReceiptStatus,
    AdmissionClass,
    ObligationStatus,
)
from .core.policy import Policy
from .core.kernel import Kernel, ObservationResult

__all__ = [
    "ObservedRequest",
    "RequestMode",
    "CQEError",
    "KernelPolicyError",
    "AdmissionError",
    "ReplayMismatch",
    "FirmwareUnavailable",
    "EvidenceStatus",
    "ReceiptStatus",
    "AdmissionClass",
    "ObligationStatus",
    "Policy",
    "Kernel",
    "ObservationResult",
    "__version__",
]

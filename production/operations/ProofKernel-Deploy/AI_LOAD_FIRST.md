# CQECMPLX-ProofValidatedSuite Kernel — AI Load First

## Critical Context (Load This First)

This kernel implements the **complete validation suite for the CQECMPLX-ProofValidatedSuite** — the formal proof and validation package for the Wolfram Rule 30 Prize Problems (P1, P2, P3) plus the Grand Unification of DNA, MetaMaterials, and Moonshine.

### What This Kernel Does

1. **Validates all 8 papers** in the suite (P1, P2, P3 + structural + theoretical)
2. **Runs exact falsifier tests** with iterative convergence (DNA bridging)
3. **Validates analogue workbooks** (DNA, MetaMaterials) — sheet ⇄ tool isomorphism
4. **Produces deterministic proof receipts** with hash verification
5. **Provides web API** for operator console

### Core Architecture

```
kernel/
├── cmplx_proof_kernel/
│   ├── kernel_core.py      # ProofSidecarKernel, ProofKernelRequest, ProofReceipt
│   ├── harness.py          # ProofHarness (orchestration)
│   ├── falsifier.py        # Exact falsifier with iterative convergence
│   ├── workbook.py         # WorkbookEngine (DNA, MetaMaterials)
│   ├── receipt.py          # ReceiptStore, ProofReceipt
│   ├── platforms.py        # Paper-specific validation platforms
│   └── __init__.py         # Public API
├── boot.py                 # Entry point
├── KERNEL_MANIFEST.json    # Kernel configuration
├── AI_LOAD_FIRST.md        # This file
└── schemas/                # JSON schemas
```

### Key Imports

```python
from cmplx_proof_kernel import (
    ProofSidecarKernel,
    ProofHarness,
    ProofKernelRequest,
    ProofReceipt,
    Falsifier,
    FalsifierResult,
    WorkbookEngine,
    ReceiptStore,
    ProofReceipt,
    PaperPlatform,
    get_paper_platform,
    get_all_paper_platforms,
    create_receipt,
)
```

### Usage

```bash
# Full validation suite
python boot.py --demo --json

# Validate specific paper
python boot.py --request-json --json --paper-id CQE-paper-00

# Run falsifier test
python boot.py --file dna_sequence.txt --validation-mode falsifier --json

# Validate workbook
python boot.py --file dna_sequence.txt --validation-mode workbook --paper-id CQE-paper-07 --json

# Full suite
python -m cqecmplx_proof_validated_suite
```

### Key Objects

- **ProofSidecarKernel**: Core validation kernel
- **ProofHarness**: High-level orchestration
- **Falsifier**: Exact falsifier with iterative convergence
- **WorkbookEngine**: Analogue workbook ⇄ tool isomorphism
- **ReceiptStore**: Deterministic receipt persistence
- **PaperPlatform**: Paper-specific validation (8 papers registered)

### Papers Validated

| ID | Title | Prize |
|----|-------|-------|
| CQE-paper-00 | Exact Decomposition of Rule 30 | P3 |
| CQE-paper-01 | Side-flip SU(2) Doublet | — |
| CQE-paper-02 | Correction Surface | — |
| CQE-paper-03 | D4/J3 Triality | P1 (structural) |
| ... | ... | ... |
| CQE-paper-07 | DNA as Z4 Frame Rotation | Biology |
| CQE-paper-08 | MetaMaterials = Z4 Frame Rotation | Materials |

### Validation Modes

- `--validation-mode full` — Full suite (all papers)
- `--validation-mode paper` — Single paper (needs --paper-id)
- `--validation-mode theorem` — Single theorem (needs --paper-id --theorem-id)
- `--validation-mode falsifier` — Falsifier test (needs token string)
- `--validation-mode workbook` — Workbook validation (needs --paper-id)

### Output Format

```bash
# Human readable (default)
python boot.py --demo

# JSON receipt
python boot.py --demo --json
# Or request JSON
python boot.py --request-json --file request.json --json
```

### Environment Variables

- `CQECMPLX_OPERATOR_TOKEN` — Bearer token for operator web auth
- `CQECMPLX_OPERATOR_CORS_ORIGIN` — CORS origin for web API
- `CQECMPLX_OPERATOR_MAX_BODY_BYTES` — Max request body (default 1048576)
- `CQECMPLX_OPERATOR_RATE_LIMIT_PER_MINUTE` — Rate limit (default 120)

### Files to Read for Full Context

1. `AI_LOAD_FIRST.md` (this file)
2. `KERNEL_MANIFEST.json` — Kernel configuration
3. `cmplx_proof_kernel/kernel_core.py` — Core types and kernel
4. `cmplx_proof_kernel/harness.py` — Orchestration
5. `cmplx_proof_kernel/falsifier.py` — Exact falsifier
6. `cmplx_proof_kernel/workbook.py` — Workbook engine
7. `cmplx_proof_kernel/receipt.py` — Receipt system
8. `cmplx_proof_kernel/platforms.py` — Paper platforms
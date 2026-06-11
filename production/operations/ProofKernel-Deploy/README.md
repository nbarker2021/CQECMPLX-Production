# CQECMPLX-ProofValidatedSuite Kernel

The validation kernel for the complete Rule 30 Proof Suite.
Extends the CMPLX-Kernel template with validation-specific components.

## Public API

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

## Quick Start

```bash
# Install in development mode
pip install -e .

# Run validation
python -m cmplx_proof_kernel --demo

# Or use boot.py directly
python boot.py --demo --json
```

## Architecture

```
cmplx_proof_kernel/
├── kernel_core.py      # Core types and kernel
├── harness.py          # Validation orchestration
├── falsifier.py        # Exact falsifier with iterative convergence
├── workbook.py         # Analogue workbook ⇄ tool isomorphism
├── receipt.py          # Deterministic receipt persistence
├── platforms.py        # Paper-specific validation platforms
├── schemas/            # JSON schemas
└── __init__.py         # Public API
```

## Papers Validated

| Paper | Title | Prize | Status |
|-------|-------|-------|--------|
| CQE-paper-00 | Exact Decomposition of Rule 30 | P3 | ✅ |
| CQE-paper-01 | Side-flip SU(2) Doublet | — | ✅ |
| CQE-paper-02 | Correction Surface | — | ✅ |
| CQE-paper-03 | D4/J3 Triality | P1 (structural) | ✅ |
| CQE-paper-04 | Boundary Repair | — | ✅ |
| CQE-paper-05 | Oloid Path Carrier | — | ⏳ |
| CQE-paper-06 | Causal Code | — | ⏳ |
| CQE-paper-07 | Discrete-Continuous Bridge | — | ⏳ |
| CQE-paper-08 | E8/Niemeier/Leech Closure | — | ⏳ |
| CQE-paper-09 | Hamiltonian Temporal Emergence | — | ⏳ |
| CQE-paper-10 | T10 Master Receipt | — | ⏳ |
| CQE-paper-11 | Theory Admission Gate | — | ⏳ |
| CQE-paper-12 | CA Prediction Surface | — | ⏳ |
| CQE-paper-13 | Standard-Model Quark-Face Transport | — | ⏳ |
| CQE-paper-14 | GR Boundary-Repair Curvature | — | ⏳ |
| CQE-paper-15 | QFT/Higgs Mass-Residue Carrier | P2 | ⏳ |
| CQE-paper-16 | Continuum Edge Residuals | P3 | ⏳ |
| CQE-paper-17 | E6-E8 Error-Correction Tower | — | ⏳ |
| CQE-paper-18 | VOA/Moonshine Representation Routes | — | ⏳ |
| CQE-paper-19 | Observer Face-Selection | — | ⏳ |
| CQE-paper-20 | Layer-2 Synthesis Ledger | — | ⏳ |
| CQE-paper-21 | MorphForge/PolyForge/MorphoniX | — | ⏳ |
| CQE-paper-22 | MetaForge Applied Materials | — | ⏳ |
| CQE-paper-23 | FoldForge Protein Folding | — | ⏳ |
| CQE-paper-24 | KnightForge/N-Dimensional Chess Automata | — | ⏳ |
| CQE-paper-25 | Energetic Traversal Maps | — | ⏳ |
| CQE-paper-26 | Z-Pinch and Shear Horizon | — | ⏳ |
| CQE-paper-27 | Observer Delay and Shared Reality | — | ⏳ |
| CQE-paper-28 | N-Dimensional Game Lattices | — | ⏳ |
| CQE-paper-29 | Monster/Universal Energy-Bound Hypotheses | — | ⏳ |
| CQE-paper-30 | Grand Ribbon Meta-Framer | — | ⏳ |
| CQE-paper-31 | It Was Still Just LCR (Meta) | — | ⏳ |

## Verification

```bash
# Run full validation suite
python -m cmplx_proof_kernel

# Or use ProofHarness directly
from cmplx_proof_kernel import ProofHarness
harness = ProofHarness()
results = harness.run_all_papers()
```
# Paper 9.50 - Hamiltonian Window Claim Contract

## Purpose

Paper 9.50 defines what counts as a valid claim about Hamiltonian window
emergence. It keeps finite provenance-preserving window arithmetic separate
from physical time claims.

## Admitted Paper 9 Claims

The following claims are admitted from Paper 9:

```text
a width-w window over n centers emits n-w+1 composite centers
width 3 over six centers emits four order-2 centers
width 5 over seven centers emits three order-3 centers
width 7 over eight centers emits two order-4 centers
source indices and source centers are preserved
backward receipts reverse to forward receipts
static Z4 does not prove temporal periodicity
```

## Claim Requirements

Any later paper using Paper 9 must state:

```text
the ordered source centers
the window width
the emitted composite center
the forward and backward receipts
the receipt proving source preservation
whether any physical time claim is separately proved
```

## Linked Receipt

The minimum receipt link for Paper 9 is:

```text
paper: CQE-paper-09
theorem: Hamiltonian window emergence
receipt: production/formal-papers/CQE-paper-09/hamiltonian_window_emergence_receipt.json
status: pass
```

The receipt is sufficient for finite window emergence. It is not sufficient by
itself for physical time reversal, temporal periodicity, or higher-order
Hamiltonian convergence.

## Boundary Failures

The following are boundary failures:

```text
emitting a composite center without source indices
emitting a composite center without source centers
claiming reverse receipt equals physical time reversal
claiming static Z4 chart symmetry proves temporal trace periodicity
changing window width or source order without rerunning the verifier
```

Boundary failures are rejected or routed to later obligations.

## Hidden-Guess Contract

When hidden-guess diagnostics are enabled, the answer must be recorded before
the receipt is revealed. The guess record should include:

```text
prompt
predicted count, provenance status, or scope status
revealed receipt
match/mismatch
next audit boundary if mismatch
```

The physical-time and static-Z4 prompts are required because their correct
answers are negative in this paper.

## Conclusion

Paper 9.50 lets later papers import Hamiltonian window emergence honestly. It
preserves the finite temporal construction without letting physical time
language outrun the receipt.

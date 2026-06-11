# CQE_MORSR Binary Boundary Adapter

CQE_MORSR requires the Binary Boundary Adapter for validation boundaries, hidden-result traces, and handshake input/output checks.

## Binding

Canonical source:

```text
CMPLX-R30-main/PROOF/src/lattice_forge/binary_boundary_adapter.py
```

## Use In CQE_MORSR

- Read validation input boundaries without mutation.
- Classify prediction/reveal trace edges.
- Attach cascade/emission context to hidden-result scoring.
- Decide whether the boundary event is library-bound or a candidate new datum.

## Rule

The validation layer observes boundary structure before scoring or repair.

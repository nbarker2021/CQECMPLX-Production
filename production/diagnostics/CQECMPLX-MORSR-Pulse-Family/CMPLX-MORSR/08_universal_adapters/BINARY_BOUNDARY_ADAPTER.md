# CMPLX-MORSR Binary Boundary Adapter

CMPLX-MORSR requires the Binary Boundary Adapter for boundary reads on pulse inputs, active-node traces, and handshake edges.

## Binding

Canonical source:

```text
CMPLX-R30-main/PROOF/src/lattice_forge/binary_boundary_adapter.py
```

## Use In CMPLX-MORSR

- Read binary-compatible pulse input without mutation.
- Classify head/tail boundary of active-node traces.
- Detect matched or crossing arcs before recentering.
- Record cascade/emission levels as diagnostic context.
- Feed BBA output into CQE before deciding whether anything is a new datum.

## Rule

BBA observation happens before repair, networking, or recenter action.

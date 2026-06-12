# Paper 6.50 - Causal Code Claim Contract

## Purpose

Paper 6.50 defines what counts as a valid causal-code claim. It ensures that
proof dependencies, review loops, open obligations, and rejected paths remain
distinguishable.

## Admitted Paper 6 Claims

The following claims are admitted from Paper 6:

```text
valid causal edges require source, target, edge_type, receipt, status
allowed edge types are uses, proves, refines, obligates, transports, repairs, constrains, verifies
allowed statuses are open, closed, deferred, rejected
closed proof-support edges must be acyclic
open obligations remain open
missing receipt, unknown type, and hidden proof cycle are rejected
```

## Claim Requirements

Any later paper using causal code must state:

```text
which dependency is being represented
which edge type is used
which receipt supports the edge
which status the edge has
whether the edge belongs to closed proof support or review/obligation routing
```

## Linked Receipt

The minimum receipt link for Paper 6 is:

```text
paper: CQE-paper-06
theorem: Typed causal edge contract
receipt: production/formal-papers/CQE-paper-06/causal_code_receipt.json
status: pass
```

The receipt is sufficient for the typed dependency theorem. It is not
sufficient by itself to claim the full 32-paper graph is populated or all
obligations are closed.

## Boundary Failures

The following are boundary failures:

```text
using a dependency without a receipt
inventing an edge type without updating the verifier
counting open obligations as closed
hiding proof cycles under prose
treating administrative metadata as proof without graph validation
```

Boundary failures are rejected or routed to obligations.

## Hidden-Guess Contract

When hidden-guess diagnostics are enabled, the answer must be recorded before
the receipt is revealed. The guess record should include:

```text
prompt
predicted edge validity or graph status
revealed receipt
match/mismatch
next obligation if mismatch
```

The hidden-cycle prompt is required because it tests whether the reviewer can
spot circular support before the verifier reveals the result.

## Conclusion

Paper 6.50 lets later papers import causal code honestly. It keeps the graph
useful as proof infrastructure without allowing open or circular support to be
mistaken for closure.

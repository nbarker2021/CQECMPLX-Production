# Paper 16.25 - Toolkit for Continuum Edge Residuals

## Purpose

This support paper exposes the tools for Paper 16. The proof is the local
edge-residual receipt; this toolkit shows how to inspect it.

## Digital Route

Run:

```text
python production/formal-papers/CQE-paper-16/verify_continuum_edge_residuals.py
```

The verifier checks:

```text
<=3 S3 anneal closure
four Lie-conjugate rest states
edge residue = C AND NOT R
decade window receipts
open global McKay-Thompson obligation
```

## Analog Route

Use stacked bars labelled:

```text
1, 10, 100, 1000
```

Each bar must roll out and return to rest before the next bar is trusted.
At the edge between bars, mark a residue only when:

```text
C = 1 and R = 0
```

## Hidden-Guess Diagnostic

Before revealing the receipt, ask:

```text
Does this state close in <=3 steps?
Does edge residue fire?
Is this a local window claim or a global continuum claim?
```

Reveal only after the guess is recorded.

## Boundary

This toolkit proves local windowing. It does not prove the continuum limit.

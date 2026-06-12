# Paper 16.50 - Continuum Edge Residual Claim Contract

## Purpose

This contract governs Paper 16 claims and keeps window receipts separate from
global continuum closure.

## Admitted Claims

Admit a claim when it provides:

```text
local chart state
anneal steps
rest-state result
edge-residue value
window depth
open/global boundary, if any
```

## Rejected Promotions

Reject by default:

```text
power-of-ten window -> continuum solution
local residue -> closed global correction sum
oracle/local nth-bit pass -> O(log N) extractor
```

## Hidden-Guess Rule

Every diagnostic must hide the answer until classification:

```text
closed local
open global
invalid overclaim
bounded/oracle evidence
```

## Linked Receipt

Current receipt:

```text
production/formal-papers/CQE-paper-16/continuum_edge_residuals_receipt.json
```

Current verdict:

```text
local edge-residual windowing: pass
global continuum collapse: open
```

## Boundary Failure

The contract fails if a later paper says Paper 16 solves the continuum limit.

The contract passes if a later paper says Paper 16 supplies local residual
windows that expose the still-open continuum-depth problem.

## Conclusion

Paper 16.50 keeps the local instrument useful and the global obligation visible.

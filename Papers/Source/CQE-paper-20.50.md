# Paper 20.50 - Layer-2 Synthesis Ledger Claim Contract

## Purpose

This contract governs suite-level aggregation. It keeps solved, open,
forbidden, and transported rows distinct.

## Admitted Claims

Admit a row when it gives:

```text
source paper
claim or route
classification
witness
proof boundary
current status
```

## Rejected Promotions

Reject by default:

```text
unknown -> solved
forbidden -> discarded
pass_with_open_lifts -> pass
registered target -> computed closure
accepted-looking row without validator
```

## Hidden-Guess Rule

Diagnostics hide the answer until after the reviewer assigns:

```text
solved
open
forbidden
transported
invalid
```

## Linked Receipt

Current receipt:

```text
production/formal-papers/CQE-paper-20/layer2_synthesis_ledger_receipt.json
```

Current verdict:

```text
ledger accounting: pass
source-claim reproof by aggregation: not claimed
open lift closure: open
```

## Boundary Failure

The contract fails if aggregation silently promotes rows.

It passes if aggregation preserves every row's source status.

## Conclusion

Paper 20.50 keeps the synthesis layer honest.

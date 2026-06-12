# Paper 0.25 - Toolkit for the First Section

## Purpose

Paper 0.25 describes the tools a reader may use while reviewing the first
section of papers. It is a supplement, not a substitute for the scientific
papers. Its job is to make the tests reproducible in multiple media.

## Tool Classes

The first section uses four visible tool classes.

```text
formal paper source
executable verifier
receipt or proof ledger
analog exposure route
```

A claim may be reviewed entirely from the paper if the proof is clear. The
tools exist so the same claim can also be replayed, inspected, or challenged.

## Digital Tools

The digital layer includes:

- paper source files,
- verifier scripts,
- JSON receipts,
- kernel manifests,
- lib-forge package bindings,
- lookup caches,
- archive indexes.

These should be used to answer concrete review questions:

```text
What exactly is claimed?
What input does the test use?
What output counts as success?
What output counts as failure?
Where is the receipt?
Can the result be regenerated?
What remains an obligation?
```

## Analog Tools

The analog layer exists to expose the same state in ordinary visible form:

- a center mark,
- left/right boundary marks,
- a transform arrow,
- a receipt line,
- a proof/obligation split,
- a next-state page.

The analog route is not a ritual. It is a way of showing that the formal claim
does not depend on hidden code. If the claim can be reduced to a center, a
boundary, a transform, and a receipt, then a reviewer can inspect the
structure independently of the software.

## Use Rule

For each integer paper in the first section, the toolkit asks:

```text
Can the claim be read as a center/boundary state?
Can the transform be stated?
Can the receipt be regenerated?
Can a failure be preserved without changing the claim?
Can the same state be exposed without the original software?
```

If the answer is no, the paper should carry an obligation rather than a proof
claim.

## Boundary

Paper 0.25 does not prove any mathematical or physical result. It defines the
review tools available for testing the papers that follow.

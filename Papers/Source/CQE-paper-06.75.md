# Paper 6.75 - Causal Code as Next-State Precondition

## Purpose

Paper 6.75 explains how causal code becomes the precondition for Paper 7 and
the remaining suite.

## Exported State

Paper 6 exports:

```text
typed causal edge schema
allowed edge types
allowed statuses
closed proof-support acyclicity rule
open-obligation rule
falsifiers for missing receipt, unknown type, hidden cycle
```

## Use in Paper 7

Paper 7 may build a discrete-continuous bridge only if the original discrete
receipt remains attached as a causal edge. Interpolation, visualization, or
presentation cannot erase the proof dependency that produced the samples.

The allowed transition is:

```text
sample receipt -> typed edge -> bridge presentation
```

The disallowed transition is:

```text
smooth presentation -> erased discrete receipt
```

## Use in Later Papers

Later papers may use causal code for:

- proof graph construction,
- obligation ledgers,
- tool and package receipts,
- product route validation,
- paper-to-paper dependency maps,
- hidden-guess training records.

Every use must preserve edge type, receipt, and status.

## Precondition Rule

Before a later paper uses Paper 6, it should be able to answer:

```text
What dependency is being represented?
What edge type is used?
What receipt supports the edge?
Is the status open, closed, deferred, or rejected?
Does the closed proof-support subgraph remain acyclic?
```

## Conclusion

Paper 6.75 turns causal code into portable proof infrastructure. It lets later
papers move, visualize, compose, and deploy results while preserving the
dependency record that keeps the suite auditable.

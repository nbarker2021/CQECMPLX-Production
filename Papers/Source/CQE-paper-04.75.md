# Paper 4.75 - Boundary Repair as Next-State Precondition

## Purpose

Paper 4.75 explains how boundary repair becomes the precondition for Paper 5's
path carrier and for later causal-code review.

## Exported State

Paper 4 exports:

```text
repaired constraint rows
original LCR states
Paper 3 axis/sheet coordinates
reason: Paper 2 correction fired
status: constraint
next legal routes
source and target paper labels
```

## Use in Paper 5

Paper 5 may attach a Paper 4 repair row as a payload only if the payload does
not alter the path rule.

The allowed transition is:

```text
repair_boundary(s) = constraint row r
attach_payload(q_t, r) = carried receipt at path state q_t
payload_alters_path_rule = false
```

Paper 5 proves the path-carrier rule. Paper 4 supplies the payload object.

## Use in Paper 6

Paper 6 may register Paper 4 repair rows as typed causal edges. The edge must
name its source, target, edge type, receipt, and status. Paper 4 proves the
row; Paper 6 proves the dependency graph discipline.

## Use in Later Papers

Later papers may lift boundary repair into:

- rolling path carriers,
- causal proof graphs,
- curvature and geometry repair language,
- mass-residue or Hamiltonian accumulated-center claims,
- product and adapter workflows.

Every lift must state which later theorem closes the added structure.

## Precondition Rule

Before a later paper uses Paper 4, it should be able to answer:

```text
What failed?
What state and coordinate were preserved?
Why is the row a constraint rather than proof?
Which next route consumes it?
Which receipt proves the repair row?
```

## Conclusion

Paper 4.75 turns repair into portable state. It exports failure as structured
constraint so Paper 5 can carry it and Paper 6 can audit it.

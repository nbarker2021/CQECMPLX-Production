# Paper 5.50 - Oloid Path Carrier Claim Contract

## Purpose

Paper 5.50 defines what counts as a valid claim about the Paper 5 rolling
carrier. It protects the verified carrier theorem from being confused with
unproven prediction or physical-geometry claims.

## Admitted Paper 5 Claims

The following claims are admitted from Paper 5:

```text
valid binary input produces a continuous rolling trace
every adjacent pair is one legal roll step
head/tail dyads remain binary
Paper 4 payloads can be carried without changing the path rule
invalid bits are rejected
discontinuous jumps are rejected
Rule 30 prediction is out of scope for this receipt
```

## Claim Requirements

Any later paper using the Paper 5 carrier must state:

```text
the initial carrier state
the input stream or local step being used
the trace state receiving any payload
whether the payload changes the path rule
which receipt proves legal continuity
whether prediction, geometry, or physics claims are separately proved
```

## Linked Receipt

The minimum receipt link for Paper 5 is:

```text
paper: CQE-paper-05
theorem: Rolling path carrier
receipt: production/formal-papers/CQE-paper-05/oloid_path_carrier_receipt.json
status: pass
```

The receipt is sufficient for finite path continuity. It is not sufficient by
itself for Rule 30 prediction, physical Oloid geometry, Wilson loops, or
mass-residue claims.

## Boundary Failures

The following are boundary failures:

```text
accepting a nonbinary input bit
accepting a skipped rolling successor as continuous
allowing payload to mutate roll(q,b)
using a carried payload as proof of the payload's downstream claim
presenting prediction as closed by this carrier receipt
```

Boundary failures are rejected or routed to obligations.

## Hidden-Guess Contract

When hidden-guess diagnostics are enabled, the answer must be recorded before
the receipt is revealed. The guess record should include:

```text
prompt
predicted step/dyad/scope result
revealed receipt
match/mismatch
next obligation if mismatch
```

The "does this prove prediction?" prompt is required because the correct answer
is negative.

## Conclusion

Paper 5.50 lets later papers import the rolling carrier honestly. It preserves
the path-continuity theorem while keeping prediction and physical geometry as
separate proof obligations.

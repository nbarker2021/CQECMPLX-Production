# Paper 20 - Layer-2 Synthesis Ledger

## Abstract

This paper defines the Layer-2 synthesis ledger: the suite-level accounting
surface that aggregates solved, open, failed, forbidden, and transported rows
without changing their source-paper status. The closed result is ledger
behavior. The seed ledger verifies, the rank-24 terminal registry contains
twenty-four forms, reachability distinguishes `yes_with_template_glue`, `no`,
and `unknown`, the transport-obligation verifier returns
`pass_with_open_lifts`, and the contributions registry admits rows only through
a named validator.

The paper does not re-prove any source-paper claim. Aggregation is accounting,
not automatic closure.

## Claims

**Claim 20.1.** The seeded morphism ledger verifies its internal invariants.

**Claim 20.2.** The ledger contains a populated object/edge/terminal summary
with twenty-four registered terminal forms.

**Claim 20.3.** Ledger reachability preserves status distinctions:
`yes_with_template_glue`, `no`, and `unknown`.

**Claim 20.4.** The transport layer contains four rows, two demonstrated and
two open lifts, with verdict `pass_with_open_lifts`.

**Claim 20.5.** The contributions registry accepts a durable row only after a
named validator accepts it, and records rejected proposals.

## Definitions

A **ledger row** is a typed record carrying a source, target, status,
classification, witness, and proof boundary.

A **synthesis ledger** is the suite-level collection of those rows.

A **transported row** is useful but not closed; it carries its open boundary
with the row.

A **forbidden row** is a retained obstruction, not discarded data.

An **unknown row** is an obligation to seed, refute, or prove a path.

## Theorem 20

The Layer-2 synthesis ledger is a verified accounting surface:

```text
source receipt -> ledger row -> preserved status -> aggregate report
```

and no aggregate row may be promoted beyond its source evidence.

## Proof

The verifier builds a fresh seed ledger and runs `Ledger.verify()`. The result
is `status=pass`, proving Claim 20.1.

The ledger summary contains populated object, vector, edge, terminal,
discriminant, and obstruction tables. It reports twenty-four terminal forms.
This proves Claim 20.2.

The verifier checks three reachability cases. `A1 -> Niemeier:A1^24` returns
`yes_with_template_glue`; `G2 -> Niemeier:Leech` returns `no`; an unseeded
source returns `unknown`. These are different ledger states and are not
collapsed into one verdict. This proves Claim 20.3.

The transport verifier reports four rows, two demonstrated rows, two open
lifts, and `all_lifts_demonstrated=false`. This proves Claim 20.4 and keeps
open lifts visible.

The registry probe registers a validator that requires a classification field.
A valid proposal is accepted and can be looked up; a bare assertion is rejected
with a rationale. This proves Claim 20.5.

Together these claims prove the theorem.

## Receipt

Promoted verifier:

```text
production/formal-papers/CQE-paper-20/verify_layer2_synthesis_ledger.py
```

Receipt:

```text
production/formal-papers/CQE-paper-20/layer2_synthesis_ledger_receipt.json
```

Closed layers:

```text
seed ledger verifies
ledger summary tables are populated
24 terminal forms are registered
can_close distinguishes yes_with_template_glue, no, and unknown
transport obligations pass with two demonstrated and two open-lift rows
contributions registry accepts validated rows and records rejected rows
```

Open layers:

```text
source-paper claims are not re-proved by aggregation
unknown reachability rows remain obligations
forbidden rows remain recorded obstructions
open transport lifts remain open until their source verifiers close them
```

## Falsifiers

The paper fails if `Ledger.verify()` fails.

It fails if `unknown` reachability is treated as solved.

It fails if a forbidden row is discarded.

It fails if `pass_with_open_lifts` is promoted to `pass`.

It fails if a contribution enters without validator acceptance.

## Role in the Suite

Papers 17, 18, and 19 export verified rows and open residues. Paper 20 is the
ledger that keeps those rows visible: solved where solved, open where open,
forbidden where forbidden, and transported where transported.

## Conclusion

Paper 20 closes the suite's aggregation discipline. It makes the corpus easier
to audit by refusing to let aggregation become promotion.

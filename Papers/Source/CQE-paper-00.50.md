# Paper 0.50 - Claim Validation Contract

## Purpose

Paper 0.50 defines when a statement is allowed to become a claim in the
CQECMPLX papers. Anything else may still be useful, but it must be carried as
a candidate, boundary failure, analogy, motivation, or open obligation.

## Claim Contract

A statement becomes a claim only when it has:

```text
1. a named object,
2. a stated context,
3. a predicted result,
4. a test protocol,
5. a receipt format,
6. a falsifier,
7. a scope boundary,
8. a source binding.
```

The contract is intentionally strict because the papers make unusual claims.
Strictness is not meant to restrict the reader. It makes the error state
visible.

## Boundary Failure

A failed or incomplete test is not discarded. It is classified as:

```text
boundary
obligation
candidate
misfit
recenter-required
insufficient-source
```

This lets the failure remain useful. It may show that the claim was too broad,
that the center moved, that the tool binding was incomplete, or that a later
paper must carry the result instead.

## Merkle-Style Paper Link

Between neighboring papers, this contract acts like a linked review layer. A
paper must carry forward only what it can identify:

```text
previous receipt hash or source binding
current claim identity
current verifier or proof route
current obligation set
next paper dependency
```

The word "Merkle" here means linked accountability: a later paper should not
silently depend on an earlier result without naming the earlier result and its
receipt.

## Reader-Facing Review

The `.50` papers are allowed to speak directly to the reader because their job
is meta-review. They explain how the surrounding papers connect and how the
reader can test the connection.

The integer papers should not rely on that voice. They should present the
claim formally.

## Conclusion

Paper 0.50 is the admission contract for claims. It allows strong claims, but
only when their proof burden is visible.

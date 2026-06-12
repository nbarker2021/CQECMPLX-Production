# Paper 09 - Hamiltonian Window Emergence

## Abstract

Paper 09 formalizes temporal emergence as an iterated local-window read over
already transported centers. The theorem is finite and exact: given an ordered
list of carried centers, a Hamiltonian window of width `w` reads a contiguous
slice forward, reads the same slice backward as a well-formed reverse receipt,
and emits a composite center that preserves the source-center sequence. The
first production instance uses widths `3`, `5`, and `7`, corresponding to the
1-3, 1-5, and 1-7 bar reads. Starting with six base centers, the iteration
emits four order-2 windows, three order-3 windows, and two order-4 windows.

This paper proves the local temporal-construction mechanism. It does not
claim that the static four-frame Z4 label template by itself determines the
Rule 30 temporal trace; the temporal Z4 verifier records that as a boundary.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions,
lemmas, constructions, examples, and receipts that establish the claimed
result. Paper 00, hand routes, analog tools, workbook language, and obligation
ledgers are supplemental validation and exposure layers. They exist to make
the math inspectable, reproducible, and accessible without requiring a
particular software stack. The hand route is not the purpose of the paper; it
is a way to expose the same state transitions with ordinary marks, tokens,
lines, or any equivalent physical substitute.

## Definitions

A **center state** is a pair `(paper_id, center)` where `center` is the
surviving local quantity carried from that paper.

A **Hamiltonian window** is a contiguous slice of fixed odd width `w` over an
ordered center-state sequence.

A **forward read** preserves the source order:

```text
C_i -> C_{i+1} -> ... -> C_{i+w-1}
```

A **backward read** records the reverse receipt:

```text
C_{i+w-1} <- ... <- C_{i+1} <- C_i
```

A **surviving composite center** is the ordered join of every center in the
window. It is accepted only when the forward and backward receipts contain the
same source centers in opposite order.

## Main Claim

**Theorem 9.1, Hamiltonian Window Emergence.** For any finite ordered sequence
of center states and any fixed window width `w <= n`, the Hamiltonian window
read emits exactly `n - w + 1` surviving composite centers. Each composite
center preserves its source centers, source indices, forward receipt, and
backward receipt. Iterating widths `3`, `5`, and `7` over the CQECMPLX base
centers produces the order counts `4`, `3`, and `2`.

### Proof

Let `S = [s_0, ..., s_{n-1}]` be a finite ordered sequence and let `w <= n`.
The valid window starts are:

```text
0, 1, ..., n - w
```

There are therefore `n - w + 1` windows. For each start index `i`, define the
window slice:

```text
W_i = [s_i, s_{i+1}, ..., s_{i+w-1}]
```

The forward read records the centers of `W_i` in source order. The backward
read records the same centers in reverse order. Since reversal is an
involution, reversing the backward read recovers the forward center sequence.
Thus the emitted composite center preserves the source centers and their
provenance.

For the CQECMPLX production instance, begin with six base center states.
Width `3` produces `6 - 3 + 1 = 4` order-2 reads. Appending the resulting
order-2 state gives seven states, so width `5` produces `7 - 5 + 1 = 3`
order-3 reads. Appending that state gives eight states, so width `7` produces
`8 - 7 + 1 = 2` order-4 reads. QED.

## Relation to Earlier Papers

Papers 01-08 establish carrier, correction, coordinate, repair, path, causal,
bridge, and closure-template layers. Paper 09 adds temporal construction:
the ordered global object is read from local center windows rather than
assumed as an external timeline.

```text
local centers
-> width-3 reads
-> width-5 reads
-> width-7 reads
-> composite temporal states with receipts
```

## Falsifier

The verifier rejects these overclaims:

```text
"the static Z4 chart template proves the temporal trace is period 4"
"a reverse receipt proves physical time reversal"
"a composite center is valid without source-window provenance"
```

Paper 09 proves window emergence and receipt-preserving reverse readability.
It does not claim that static chart symmetry alone proves temporal dynamics.

## Code Reconstruction

The production verifier is:

```text
production/formal-papers/CQE-paper-09/verify_hamiltonian_window_emergence.py
```

It verifies:

```text
1. Width-3 reads over six base centers produce four surviving centers.
2. Width-5 reads after appending order 2 produce three surviving centers.
3. Width-7 reads after appending order 3 produce two surviving centers.
4. Every surviving center carries source indices and source centers.
5. Every backward receipt reverses to the forward receipt.
6. The temporal Z4 scope verifier records static-template-only status.
```

## Open Audit Boundaries

1. The reverse read is a receipt-level reverse, not a proof of physical time
   reversal.
2. The static Z4 chart template does not force the Rule 30 temporal trace.
3. Higher-order convergence beyond width 7 is not claimed by this paper.
4. Any Hamiltonian or physical dynamics assigned to the composite centers
   require a later theorem.

## Conclusion

Paper 09 proves that temporal structure can be built from local carried
centers by finite Hamiltonian-window reads. The proof is the window arithmetic
and provenance preservation. The supplemental hand/workbook route merely
exposes the same construction; the mathematical result is the receipt-bearing
emergence of composite centers from local windows.

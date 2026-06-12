# Paper 9 - Hamiltonian Window Emergence

## Abstract

Paper 9 begins the second block of the CQECMPLX suite by proving finite
Hamiltonian window emergence over carried centers. Paper 8 supplies the
closure frame from the first block. Paper 9 reads ordered local centers through
odd-width windows and emits composite centers with explicit forward and
backward receipts.

The production instance uses widths:

```text
3, 5, 7
```

Starting with six base center states, these reads emit:

```text
width 3 -> 4 surviving centers
width 5 -> 3 surviving centers
width 7 -> 2 surviving centers
```

The theorem proves finite window arithmetic and provenance preservation. It
does not prove physical time reversal, static-Z4 temporal periodicity, or
higher-order convergence.

## Claims

**Claim 9.1.** A Hamiltonian window of width `w` over an ordered sequence of
`n` center states emits exactly `n-w+1` composite centers.

**Claim 9.2.** Each emitted composite center preserves source indices, source
papers, source centers, forward receipt, and backward receipt.

**Claim 9.3.** In the production sequence, width-3, width-5, and width-7 reads
emit exactly four, three, and two composite centers.

**Claim 9.4.** A reverse receipt is receipt-level reversibility, not proof of
physical time reversal.

## Definitions

A **center state** is:

```text
(paper_id, center)
```

A **Hamiltonian window** is a contiguous slice of fixed odd width `w` over an
ordered center-state sequence.

A **forward receipt** records the center sequence in source order:

```text
C_i -> C_{i+1} -> ... -> C_{i+w-1}
```

A **backward receipt** records the same centers in reverse order:

```text
C_{i+w-1} <- ... <- C_{i+1} <- C_i
```

A **surviving composite center** is:

```text
C[C_i|C_{i+1}|...|C_{i+w-1}]
```

accepted only when the source indices and centers are preserved.

## Theorem 9.1 - Hamiltonian Window Emergence

For any finite ordered sequence of center states and any fixed window width
`w <= n`, the Hamiltonian window read emits exactly `n-w+1` surviving
composite centers. Each composite center preserves its source indices, source
centers, forward receipt, and backward receipt.

## Proof

Let:

```text
S = [s_0, s_1, ..., s_{n-1}]
```

be a finite ordered sequence. For width `w <= n`, the valid starts are:

```text
0, 1, ..., n-w
```

There are `n-w+1` valid starts and therefore `n-w+1` windows.

For each start index `i`, define:

```text
W_i = [s_i, s_{i+1}, ..., s_{i+w-1}]
```

The forward receipt records centers in the order of `W_i`. The backward
receipt records the same centers in reverse order. Reversing the backward
receipt recovers the forward center sequence, so the source-center provenance
is preserved. The composite center is the ordered join of those same source
centers.

For the production instance, begin with six base centers. Width `3` yields:

```text
6 - 3 + 1 = 4
```

Appending the order-2 state gives seven states. Width `5` yields:

```text
7 - 5 + 1 = 3
```

Appending the order-3 state gives eight states. Width `7` yields:

```text
8 - 7 + 1 = 2
```

This proves the reported counts and the provenance-preserving construction.

## Receipt

The primary executable receipt is:

```text
production/formal-papers/CQE-paper-09/verify_hamiltonian_window_emergence.py
production/formal-papers/CQE-paper-09/hamiltonian_window_emergence_receipt.json
```

The receipt status is `pass`. It verifies:

```text
order2_width3_count_is_four                 = true
order3_width5_count_is_three                = true
order4_width7_count_is_two                  = true
all_reads_preserve_source_indices           = true
all_reads_preserve_source_centers           = true
all_backward_receipts_reverse_to_forward    = true
static_z4_does_not_prove_temporal_periodicity = true
```

## Falsifiers

The verifier rejects:

```text
the static Z4 chart template proves the temporal trace is period 4
a reverse receipt proves physical time reversal
a composite center is valid without source-window provenance
```

These are overclaims relative to the finite window theorem.

## Role in the Suite

Paper 9 turns the first-block closure scaffold into ordered center-window
construction:

```text
verified closure scaffold
-> ordered carried centers
-> width-3, width-5, width-7 reads
-> composite temporal states with receipts
```

This is the suite's first controlled temporal-emergence rule. It is controlled
because every composite center must carry its source provenance.

## Open Audit Boundaries

1. Reverse readability is not physical time reversal.
2. Static Z4 chart symmetry does not force Rule 30 temporal periodicity.
3. Higher-order convergence beyond width 7 is not claimed here.
4. Physical Hamiltonian dynamics assigned to composite centers require a later
   theorem.

## Conclusion

Paper 9 proves temporal construction as finite local-window emergence. It
shows how carried centers become composite centers with replayable receipts
while refusing to confuse receipt reversal or static labels with physical time
dynamics.

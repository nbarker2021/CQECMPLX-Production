# Paper 8 - Lattice Closure Template

## Abstract

Paper 8 closes the first eight-paper window by proving the local lattice
closure template used by the CQECMPLX suite. Papers 1-7 build local carrier,
correction, registration, repair, path, causal, and bridge machinery. Paper 8
places that machinery inside a verified code/lattice ladder:

```text
1 -> 3 -> 7 -> 8 -> 24
```

with powered terminal:

```text
1^2 = 1
3^2 = 9
7^2 = 49
8 x 9 = 72
```

The theorem proves the local combinatorial scaffold and binds the current
Niemeier/Leech enumeration receipt: deterministic selectors, E8^3 carriers,
Leech type-1/2/3 orbit checks, and the Nebe 72 contract. It does not promote
exact integer-vector glue-coset representatives, the rootless Leech landing,
Gamma72 polarization action, or uniqueness of all possible closure chains as
closed theorems.

## Claims

**Claim 8.1.** The chain `(1,3,7,8,24)` provides a verified local closure
template for transporting local states into larger code/lattice frames.

**Claim 8.2.** The dimension-7 rung passes the Fano/Hamming identity checks.

**Claim 8.3.** The dimension-8 rung passes the extended Hamming/E8 seed checks.

**Claim 8.4.** The dimension-24 rung supplies Golay ingredients and `24 = 3 x
8` carrier geometry without proving the rootless Leech landing.

**Claim 8.5.** The powered terminal records `72 = 8 x 9` with sheet bound
`K = 9`.

**Claim 8.6.** Gamma72 three-sheet transport is verified as transport, not as
a closed Gamma72 landing proof.

**Claim 8.7.** Niemeier/Leech enumeration verifies deterministic selectors,
E8^3 carriers, Leech type-1/2/3 orbit checks, and the Nebe 72 contract, while
leaving exact final glue-coset representatives as pending invariants.

**Claim 8.8.** The rebuilt seed ledger contains the eight canonical T8 `F4` to
Niemeier terminal paths, each returning `yes_with_template_glue`.

## Definitions

A **lattice closure template** is a sequence of finite code or lattice objects
that lets a local state carrier be lifted into a larger transport frame while
preserving the proof boundary of every step.

The Paper 8 template is:

```text
D1 raw bit                 -> 1
S3 / three-cell carrier    -> 3
Fano / Hamming / octonion  -> 7
extended Hamming / E8 seed -> 8
Golay / Leech ingredient   -> 24
Nebe sheet bound           -> 72
```

A **local certified fact** is a claim checked at a fixed dimension by a finite
verifier.

A **global landing claim** is a stronger statement that a local certified fact
has been glued into a terminal lattice object such as the rootless Leech
lattice or a Gamma72 action.

## Theorem 8.1 - Local Lattice Closure Template

The finite code chain `(1,3,7,8,24)` and powered terminal `72 = 8 x 9` provide
a verified local closure template for CQECMPLX transport. Every admitted rung
is backed by a finite combinatorial check, and every unproved global landing
is preserved as an explicit proof boundary.

## Theorem 8.2 - Niemeier/Leech Enumeration Boundary

The Niemeier/Leech enumeration receipt closes deterministic selector, E8^3
carrier, Leech type-1/2/3 orbit, and Nebe 72 contract checks. It advances O7
as a partial resolution. It does not close the exact integer-vector glue-coset
representatives at the final edge and does not claim the rootless Leech landing
as proved.

## Theorem 8.3 - T8 Commutability Tree

A rebuilt lattice-forge seed ledger contains the eight canonical `F4` to
Niemeier terminal paths recorded by T8. Each queried target returns
`yes_with_template_glue`, every path matches the historical path table, and the
eight terminal targets are distinct. This closes the seed-ledger path theorem
without claiming exact glue-coset representatives.

## Proof

The verifier establishes the following local facts.

At dimension 7, the `(7,4,3)` Hamming code has 16 codewords, minimum weight 3,
weight distribution:

```text
{0:1, 3:7, 4:7, 7:1}
```

and exactly seven weight-3 codewords whose supports are the seven Fano-plane
lines. This identifies the Hamming, Fano, and octonion-imaginary incidence
structure at the local dimension-7 rung.

At dimension 8, the `(8,4,4)` extended Hamming code has 16 codewords, minimum
weight 4, weight distribution:

```text
{0:1, 4:14, 8:1}
```

all weights divisible by 4, and pairwise self-orthogonality. This supplies the
self-dual doubly-even binary code used as the E8 Construction A seed.

At dimension 24, the Golay generator layer has 12 length-24 rows, zero
generator-pair orthogonality errors, and the carrier geometry:

```text
24 = 3 x 8
```

This supplies Golay ingredients and three-copy D4 carrier geometry. It does
not by itself prove a rootless Leech landing.

For the powered terminal:

```text
1^2 = 1
3^2 = 9
7^2 = 49
8 x 9 = 72
```

The verifier records `sheet_K_bound = 9` and dimension-72 extremal minimum
norm:

```text
2 * floor(72/24) + 2 = 8
```

The Gamma72 contract checks 260 payloads and confirms exact round trips into
three Leech sheets, while also recording:

```text
polarization_matrices_supplied = false
gamma72_landing_proved = false
```

Together these checks prove the local closure template and its audit boundary.

The Niemeier/Leech enumeration verifier separately runs the enumerated-glue
selector contract, Leech minimal/type-1/type-2/type-3 orbit checks, and the
Nebe 72 contract. These checks paper-bind the finite enumeration layer. The
receipt also records pending invariants and `leech_landing_proved = false`,
so the proof cannot silently promote the stronger landing.

The T8 verifier builds a temporary seed database and queries
`Forge.can_close("F4", target)` for the eight named Niemeier terminals. It
checks the returned path, terminal uniqueness, trunk nodes, and
`yes_with_template_glue` answer for each target. Since the answer is template
glue, not exact glue, the theorem closes the commutability path table and
leaves exact representatives as a separate obligation.

## Receipt

The primary executable receipt is:

```text
production/formal-papers/CQE-paper-08/verify_lattice_closure_template.py
production/formal-papers/CQE-paper-08/lattice_closure_template_receipt.json
production/formal-papers/CQE-paper-08/verify_niemeier_leech_enumeration.py
production/formal-papers/CQE-paper-08/niemeier_leech_enumeration_receipt.json
production/formal-papers/CQE-paper-08/verify_t8_commutability_tree.py
production/formal-papers/CQE-paper-08/t8_commutability_tree_receipt.json
```

The receipt status is `pass`. It verifies:

```text
chain_passes                                      = true
fano_hamming_identity_passes                      = true
extended_hamming_e8_seed_passes                   = true
golay_24_ingredient_passes_without_leech_overclaim = true
powered_72_sheet_bound_passes                     = true
gamma72_transport_passes_without_landing_overclaim = true
leech_landing_overclaim_rejected                  = true
gamma72_landing_overclaim_rejected                = true
enumerated_glue_selector_contract                 = true
leech_type1_orbit                                 = true
leech_type2_orbit                                 = true
leech_type3_orbit                                 = true
nebe_gamma72_contract                             = true
exact_final_glue_coset_representatives_pending    = true
t8_paths_count_is_8                               = true
t8_all_paths_match_historical_report              = true
t8_answers_are_yes_with_template_glue             = true
```

## Falsifiers

The verifier rejects:

```text
Golay ingredients alone prove the rootless Leech landing
three Leech-sheet round trips prove the Gamma72 polarization action
the chain proves that no other higher-dimensional closure template exists
```

These statements exceed the certified local checks.

## Role in the Suite

Paper 8 receives the first block:

```text
LCR carrier
-> correction surface
-> D4/J3 coordinate surface
-> boundary repair
-> path carrier
-> causal code
-> discrete-continuous bridge
-> lattice closure template
```

It also wraps the block back to Paper 1 by showing how the local carrier can
enter a higher-dimensional scaffold without changing the proof status of any
unclosed global landing.

## Open Audit Boundaries

1. Exact integer-vector glue-coset representatives for the final Niemeier:E8^3
   edge remain pending.
2. A rootless Leech landing proof requires an explicit glue-action verifier
   that sets `leech_landing_proved = true`.
3. A Gamma72 landing proof requires selected Hermitian polarization matrices.
4. A cold-start map from arbitrary depth to a Niemeier/Leech fingerprint
   remains outside this paper.
5. The claim that this is the only possible closure chain is not part of the
   theorem.

## Conclusion

Paper 8 proves the first-block closure scaffold. Local lattice facts are
certified, their transport role is explicit, and stronger global landings are
kept visible as named audit boundaries rather than hidden inside the theorem.

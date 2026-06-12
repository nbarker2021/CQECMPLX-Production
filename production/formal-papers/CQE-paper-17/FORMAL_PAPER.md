# Paper 17 - E6-E8 Error-Correction Tower

## Abstract

This paper proves a bounded error-correction tower as a sequence of verified
code and lattice receipts:

```text
1 -> 3 -> 7 -> 8 -> 24 -> 72
```

The closed result is not a new coding theorem and not a completed Leech or
Weyl-extractor construction. The closed result is that the CQE transport stack
has a reproducible forced backbone: the local `Z/2` bit, the `S3`
neighborhood, the `(7,4,3)` Hamming/Fano rung, the `(8,4,4)` extended
Hamming/E8 seed, the `(24,12,8)` Golay ingredient layer, and the Nebe
dimension-72 terminal bound. The verifier also admits the determinant-one
`E8^3` Niemeier direct-sum root-shell landing. Rootless Leech glue action,
semantic terminal selection from an arbitrary `N`, and the `W(E8)` extraction
table remain open obligations.

## Claims

**Claim 17.1.** The parameter chain `1,3,7,8,24` passes as the local-to-global
code backbone.

**Claim 17.2.** The `n=7` rung is the `(7,4,3)` Hamming code whose seven
weight-3 codewords are the seven Fano-plane lines.

**Claim 17.3.** The `n=8` rung is the `(8,4,4)` extended Hamming code; it is
self-dual, doubly-even, and supplies the E8 Construction-A seed used by the
tower.

**Claim 17.4.** The `n=24` rung verifies Golay-code ingredients and the `3 x 8`
carrier geometry while explicitly not proving the Leech glue action.

**Claim 17.5.** The powered chain `1^2=1`, `3^2=9`, `7^2=49`, and `8x9=72`
passes, with the Nebe dimension-72 extremal minimum norm `8` setting the
current sheet bound `K_max=9`.

**Claim 17.6.** The `E8^3` Niemeier determinant-one direct-sum landing is
verified at root-shell level, but no semantic map from arbitrary `N` to a
terminal landing is proved here.

## Definitions

A **tower rung** is one accepted carrier size in the sequence
`1,3,7,8,24,72`.

A **closure frame** is the code or lattice object that receives the local state
at a rung.

A **forced parameter** is a rung value admitted only when its verifier closes
the relevant code parameters, such as length, dimension, minimum weight,
self-duality, or bounded extremality.

A **root-shell landing** is a rank-24 ADE/Niemeier terminal profile admitted at
profile level. It is not automatically a proved glue construction.

An **open promotion** is a mathematically meaningful continuation that is not
closed by this paper's receipt.

## Theorem 17

The CQE error-correction tower has a verified bounded backbone:

```text
local bit -> S3 neighborhood -> Hamming/Fano -> extended Hamming/E8
-> Golay ingredients -> Nebe-72 sheet bound
```

and its exceptional `E6/E7/E8` interpretation is admissible only as a
transport reading over verified code and root-shell receipts, not as a
completed physical or Leech-glue theorem.

## Proof

The chain verifier reports `status=pass` and the parameter verifier reports
the chain `[1,3,7,8,24]`. This proves Claim 17.1.

For the `n=7` rung, the verifier reports sixteen codewords, minimum weight
`3`, and weight distribution `{0:1, 3:7, 4:7, 7:1}`. The seven weight-3
supports are exactly the Fano-plane lines. This proves Claim 17.2 and fixes the
octonion/Fano transport layer as a checked code receipt rather than metaphor.

For the `n=8` rung, the verifier reports sixteen codewords, minimum weight
`4`, self-duality, and weight distribution `{0:1, 4:14, 8:1}`. This admits the
extended Hamming E8 seed used by the tower. This proves Claim 17.3.

For the `n=24` rung, the verifier reports twelve Golay generators,
self-orthogonal ingredient behavior, and `24 = 3 x 8` carrier geometry. The
same receipt reports `leech_construction_proved=false`. The verified
ingredient layer is therefore closed, while the rootless Leech overlattice
glue action is not. This proves Claim 17.4 with its boundary intact.

For the powered layer, the verifier reports `{1^2:1, 3^2:9, 7^2:49, 8x9:72}`,
Nebe dimension `72`, extremal minimum norm `8`, and sheet bound `K_max=9`.
This proves Claim 17.5.

For the rank-24 terminal profile layer, the direct-sum verifier reports
`Niemeier:E8^3`, `exact_at_root_shell_level=true`, and
`semantic_landing_from_n_proved=false`. The root-shell profile verifier reports
twenty-three rootful terminal profiles, one rootless profile, integral indices,
matching Coxeter numbers, and `exact_glue_cosets_proved=false`. This proves
Claim 17.6 and prevents terminal registration from being mistaken for a glue
construction.

Together these claims prove the theorem.

## Receipt

Promoted verifier:

```text
production/formal-papers/CQE-paper-17/verify_error_correction_tower.py
```

Receipt:

```text
production/formal-papers/CQE-paper-17/error_correction_tower_receipt.json
```

Closed layers:

```text
parameter chain 1,3,7,8,24
Hamming (7,4,3) Fano-plane rung
extended Hamming (8,4,4) self-dual E8 seed
Golay (24,12,8) ingredient layer and 3x8 carrier geometry
powered chain 1,9,49,72 and Nebe-72 K-bound
Niemeier E8^3 determinant-one direct-sum root-shell landing
rank-24 root-shell profile registry at bounded profile level
```

Open layers:

```text
rootless Leech overlattice glue action
semantic map from arbitrary N to a Niemeier terminal
W(E8) lookup table or sub-O(N) extractor
physical error-correction theorem beyond the verified code tower
```

## Falsifiers

The paper fails if any code rung reports a failed status.

It fails if the Hamming weight distribution is not `{0:1, 3:7, 4:7, 7:1}`.

It fails if the extended Hamming rung is not self-dual or has minimum weight
other than `4`.

It fails if the Golay ingredient receipt is used to claim a completed Leech
construction.

It fails if the Niemeier registry is used to claim a proved semantic
`N -> terminal` map.

## Role in the Suite

Paper 16 exports local edge-residual windows. Paper 17 places those windows in
an error-correction tower whose verified rungs can carry faults into larger
closure frames. Paper 18 may use these closure frames to discuss glue and
representation routes, but it must inherit the open Leech and `W(E8)`
obligations.

## Conclusion

Paper 17 closes the bounded code-tower backbone. It gives the suite a rigorous
ladder from local bit receipts to E8 and rank-24 root-shell targets, while
preserving the exact boundary between verified rungs and still-open promotion
claims.

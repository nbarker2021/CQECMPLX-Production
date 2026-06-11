# Paper 18 - VOA / Moonshine Representation Routes

## Status

Transport paper. Treats representation routes between the chart's VOA seed and the Monster Moonshine boundary as explicit upward/downward transport choices with strict receipt requirements. The finite VOA-sector seed is verified; the McKay-Thompson route (the modular-form fingerprint) is the open computational obligation O1'. Proof-facing for the seed, obligation-facing for the route.

## Abstract

This paper organizes the corpus's contact with Monstrous Moonshine as a set of *representation routes*: directed transport choices that either climb (D2 vignette -> D4 Monster boundary) or descend (Monster representation -> chart-level correction tape), each requiring a replayable receipt and each carrying its unresolved residue explicitly. Two layers are surfaced. (1) A finite, verified seed: the 3-conjugate VOA sector decomposition of the 8 chart states yields the seed partition function `Z(q) = 2q^0 + 6q^5` (2 true vacua at weight 0, 6 excited states at weight 5), and the `Z4` 4-frame template gives exactly 2 fixed points and 6 period-4 states matching the D12 orbit structure. These are finite chart identities verified by `verify_centroid_voa_chain`. (2) The open route: the umbrella's load-bearing hypothesis (D4, IDENTITY 2.7) is that the Rule 30 correction tape factors through a McKay-Thompson series of the Monster, with the Monster scalar `196883 = 47 * 59 * 71` realized as the modular `S`-involution. The primitive `mckay_thompson_coefficient_parity(g, k)` is declared but raises `NotImplementedError` — it is open obligation O1'. The paper makes the strict-receipt discipline explicit: any "50% Bernoulli split" against a direct period test is logged not as a falsifier but as the signature that the bijective modular companion has not been brought into the comparison.

## Central Thesis

Treat representation routes as upward/downward transport choices with strict receipt requirements.

## Scope Boundary

This paper claims the finite VOA-sector seed and `Z4` template exactly as `centroid_voa.py` verifies them, and it claims the *architecture* of the McKay-Thompson route exactly as `voa_lookup.py` declares it. It does NOT claim a computed McKay-Thompson coefficient, an `O(log N)` Rule 30 extractor, an observed SPINOR signature, or any Moonshine identification beyond the finite chart identities. The VOA/Moonshine reading of the seed requires an additional transport theorem and is logged as obligation.

## Definitions

- **Representation route**: a directed transport choice between two graded objects (chart VOA seed, `S_3` vignette, `E_8` relational qubit, Monster boundary), tagged upward (toward larger symmetry) or downward (toward chart correction).
- **VOA weight**: `voa_weight(s) = sum of the 3-conjugate wrap-step label (w1, w2, w3)`; the conformal-weight grading of a chart state (`centroid_voa.voa_weight`).
- **Seed partition function**: `Z(q) = 2q^0 + 6q^5`, the weight-graded generating function of the 8 chart states.
- **McKay-Thompson route**: the hypothesized factorization of the Rule 30 correction tape through `T_g(tau) = q^{-1} + sum a_n q^n` for a Monster conjugacy class `g`; its primitive is `mckay_thompson_coefficient_parity`.
- **Monster scalar**: `196883 = 47 * 59 * 71`, the dimension of the smallest faithful Monster representation, realized as the modular `S`-involution `tau -> -1/tau`.
- **Strict receipt requirement**: every route step records inputs, output, residue, and — for any direct period/modular test — whether the bijective companion was included.
- **Receipt / Transport row / Workbook sheet / Tool binding**: as fixed in Paper 00.

## Axioms

Axiom 18.1 - Locality: every representation route begins at a local chart-VOA reading before it is lifted to a Monster-scale frame.

Axiom 18.2 - Receipt Preservation: no route step is accepted unless its grading, transform, and residue are logged and replayable; an unimplemented primitive (O1') is logged as residue, not bypassed.

Axiom 18.3 - Boundary Positivity: a 50% Bernoulli split in a direct period/modular test is data — the signature of a missing modular companion — not a silent failure or a falsifier.

Axiom 18.4 - Analog Equivalence: the route has a physical workbook analogue (a graded card ladder with upward/downward string and a black "open route" card for O1').

## Lemmas

Lemma 18.1 - VOA sector seed. The 3-conjugate wrap-step weight partitions the 8 chart states into 2 true vacua `(0,0,0), (1,1,1)` at weight 0 and 6 excited states at weight 5, giving `Z(q) = 2q^0 + 6q^5`. (Verified: `verify_voa_sector_decomposition`; PROOF Paper 15 T_VOA_SECTORS.)

Lemma 18.2 - `Z4` route template. The 4-frame `Z4` composite label has exactly 2 fixed points (label `(0,0,0,0)`) and 6 period-4 states, with no period-2 states, matching the D12 orbit split 2 + 6. (Verified: `verify_z4_period_template`.)

Lemma 18.3 - Monster boundary scalar. The Monster scalar `MONSTER_SCALAR = 47 * 59 * 71 = 196883` is the product of the three largest supersingular primes and the dimension of the Monster's smallest faithful complex representation, with McKay's `196884 = 1 + 196883`. (Source: `voa_lookup.MONSTER_SCALAR`; IDENTITY D4; PROOF Paper 05.)

## Formalism / Calculus Sketch

A paper state is `P = (C, L, R, B, T, O)` (Paper 00). A representation route is a typed edge with a direction and a receipt:

```text
route(direction, source_grade, target_grade, T) accepted when:
  T maps source_grade -> target_grade
  receipt records grading, transform, residue
  if T is a direct period/modular test:
     receipt records whether the bijective modular companion was included
  any unimplemented primitive (O1') is logged in O, not assumed
```

The seed and the open route:

```text
seed (verified):    Z(q) = 2q^0 + 6q^5 ; Z4 split = 2 fixed + 6 period-4
upward route:       D2 (S_3 vignette) -> D4 (Monster boundary, scalar 196883)
downward route:     Rule_30_center(N) = LucasBit(N,0)
                        XOR sum over Lucas-sparse cone of
                        mckay_thompson_coefficient_parity(g(axis,sheet), k(t,x))
correction classes: (axis 2, sheet 0) -> "2A" ; (axis 3, sheet 1) -> "3A"  [hypothesis]
open primitive:     mckay_thompson_coefficient_parity(g, k)  -> NotImplementedError (O1')
```

Tool binding:

```text
cqe_engine  (lattice_forge.centroid_voa: voa_weight, verify_voa_sector_decomposition,
             verify_z4_period_template, verify_centroid_voa_chain;
             lattice_forge.voa_lookup: MONSTER_SCALAR, correction_class_for,
             mckay_thompson_coefficient_parity [O1'], architecture_summary)
```

## Proof Tree

```text
claim (representation routes = receipted upward/downward transport choices)
-> local chart-VOA reading (3-conjugate weight)
-> seed partition function Z(q) = 2q^0 + 6q^5 (Lemma 18.1)
-> Z4 route template 2 + 6 (Lemma 18.2)
-> upward route to Monster boundary (scalar 196883, Lemma 18.3)
-> downward route to correction tape (McKay-Thompson)
   -> primitive mckay_thompson_coefficient_parity  [OPEN: O1']
-> worked example (seed verifier + architecture summary)
-> workbook analogue (graded card ladder)
-> receipt (incl. companion-inclusion flag)
-> proof (seed) / obligation (McKay-Thompson route, SPINOR signature)
```

## Practical Solved Example

**Domain:** the chart-VOA seed of the Rule 30 center column and its declared route to the Monster boundary.

**Procedure:** run `verify_centroid_voa_chain()` for the seed; call `architecture_summary()` (from `voa_lookup`) to read the route contract; attempt `mckay_thompson_coefficient_parity("2A", 5)` to confirm the route's open boundary.

**Solved Output:**
- Seed: `verify_voa_sector_decomposition` returns `status = "pass"` with `seed_partition_function = "2q^0 + 6q^5"`; `verify_z4_period_template` returns `fixed_point_count = 2`, `period_4_count = 6`, `period_2_count = 0`.
- Route contract: `architecture_summary()` reports `monster_scalar = 196883`, factorization `47 * 59 * 71`, correction firing classes `{(2,0): "2A", (3,1): "3A"}`, and `open_obligation = "O1'"`.
- Open primitive: `mckay_thompson_coefficient_parity("2A", 5)` raises `NotImplementedError` pointing to O1' — the route is correctly logged as open, not silently filled.

The example is solved (for the seed) because the partition function and `Z4` split reproduce identically from the formal table, the `centroid_voa` verifier, and the workbook card ladder; the downward route is faithfully surfaced as obligation.

## Tool Binding

- Module: `cqe_engine` (`lattice_forge.centroid_voa`, `lattice_forge.voa_lookup`).
- Functions: `voa_weight`, `verify_voa_sector_decomposition`, `verify_z4_period_template`, `verify_centroid_voa_chain`; `MONSTER_SCALAR`, `correction_class_for`, `architecture_summary`, `mckay_thompson_coefficient_parity` (open).
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: confirm the seed verifier `status == "pass"`; confirm `mckay_thompson_coefficient_parity` raises `NotImplementedError`; emit one proof row (the seed) and one obligation row (O1').

## Analog Workbook Sheet

- Start with grey loose substrate.
- Lay a graded card ladder: weight-0 cards for the 2 vacua, weight-5 cards for the 6 excited states (the `Z(q) = 2q^0 + 6q^5` seed).
- Place the `C` (gluon) token at the center of each card; color red/green/blue for the 3 conjugate settings.
- Use upward string for the climb to the Monster-boundary card (label `196883 = 47*59*71`); use downward string for the correction-tape route.
- White follow-up = the verified seed; black follow-up = the McKay-Thompson route card (O1') and the unobserved SPINOR card.
- Bind the finished ladder into the matching color notebook.

## IRL Citation Anchors

- [ConwayNorton1979] J. H. Conway, S. P. Norton, Monstrous Moonshine, Bull. London Math. Soc. 11, 308-339. Use: McKay-Thompson series and the Monster character table.
- [Borcherds1992] R. Borcherds, Monstrous Moonshine and monstrous Lie superalgebras, Invent. Math. 109, 405-444. Use: the VOA realization of Moonshine.
- [FrenkelLepowskyMeurman1988] I. Frenkel, J. Lepowsky, A. Meurman, Vertex Operator Algebras and the Monster, Academic Press. Use: the moonshine VOA `V^natural` and graded dimension.
- [Wolfram1983] S. Wolfram, Statistical mechanics of cellular automata, Rev. Mod. Phys. 55(3), 601-644. Use: the Rule 30 correction tape the route targets.
- [W3C_PROV] W3C PROV provenance model. URL: https://www.w3.org/TR/prov-overview/ Use: route receipts and the companion-inclusion flag.

## Open Obligations

- **O1' (McKay-Thompson primitive):** `mckay_thompson_coefficient_parity(g, k)` is unimplemented (raises `NotImplementedError`); without it, `correction_via_voa` and the `O(log N)` Rule 30 extractor cannot be evaluated. This is the VOA companion to the `W(E_8)` obligation O1 (Paper 17). Carried open.
- **Correction-class assignment:** the map `{(2,0): "2A", (3,1): "3A"}` in `voa_lookup` is a stated hypothesis, not a proved assignment; verification is open.
- **SPINOR signature (IDENTITY 8.3):** the `(0, eps, 0)` Moonshine ground-state signature has not been observed in tested sequences; its stabilization at the 27-dimensional meta-vignette scale is open.
- **Moonshine identification:** `verify_centroid_voa_chain` states explicitly that any VOA/Moonshine identification of the finite seed requires an additional transport theorem; carried open.
- Replace citation anchors with final bibliography entries; add a falsifier the tool must reject (a route that omits the companion-inclusion receipt).

## Back-Propagation Targets

- Paper 00 receives the "representation route" and "strict receipt / companion-inclusion" contract terms.
- Paper 17 receives the Golay/Leech landing forms that seed the Monster-scale frames used here.
- Paper 19 receives the upward/downward route discipline for its face-selection obligations.
- Paper 20 receives O1', the correction-class hypothesis, and the SPINOR obligation as ledger rows.
- The analog workbook manual receives the graded card-ladder rule.
- Paper 31 records how the seed-then-route presentation order is itself an enacted `(L, C, R)` lift.

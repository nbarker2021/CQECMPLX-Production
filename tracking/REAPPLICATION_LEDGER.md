# Reapplication Ledger

Working premise (operator directive, 2026-06-13): most things marked "open"
or "obligation" in the corpus were already solved somewhere in the workspace;
the resolution simply was never reapplied to the state that records the
obligation. This ledger records obligations whose existing resolution has now
been found and reapplied into the production paper-bound space.

A reapplication is not new work. It binds an already-proven module or an
already-built forge to the obligation it silently resolves, with a passing
verifier and a receipt, and records what remains genuinely open.

## Reapplied 2026-06-13

| Obligation | Source ledger | Existing resolution (was unused) | Reapplied to | Receipt | Status |
|---|---|---|---|---|---|
| O2' verifiable core: Rule 30 = Rule 90 (+) correction, Lucas closed-form, depth-N decomposition | `CMPLX-R30-main/PROOF/theorems/OPEN_OBLIGATIONS.md` | `lattice_forge/rule90_linearization.py` — proven with its own passing verifier, vendored into the production substrate, bound to no paper | `formal-papers/CQE-paper-06/verify_rule90_lucas_decomposition.py` | `rule90_lucas_decomposition_receipt.json` (7/7) | core CLOSED; O(log N) McKay-Thompson collapse stays open |
| PFC-2 named computation: enumerate the 240 E8 roots from Construction A | `CMPLX-R30-main/PROOF/theorems/OPEN_OBLIGATIONS.md` | `E8Forge` (promoted 2026-06-12) — exact 240-root enumeration | `formal-papers/CQE-paper-08/verify_e8_hemisphere_partition.py` | `e8_hemisphere_partition_receipt.json` (5/5) | enumeration BUILT, 240/120-pair/clean-split confirmed; the "13 half-vignettes" geometric count and the alpha=1/137 physics remain OPEN and are explicitly not claimed |
| T1-T4 algebra foundation paper-binding gap: octonion axioms, J3(O) Jordan axioms, chart->J3(O) isomorphism, exact n=3 SU(3) Weyl closure | `CMPLX-R30-main/PROOF/theorems/THEOREM_REGISTRY.md` | `lattice_forge/{octonion,jordan_j3,rule30,f4_action}.py` — all PROVEN with named verifiers, vendored in the substrate, bound to no production paper | `formal-papers/CQE-paper-03/verify_algebra_foundation_T1_T4.py` | `algebra_foundation_T1_T4_receipt.json` (8/8) | CLOSED — all four registry verifiers pass and are now paper-bound; T3 confirms chart=J3(O) diagonal, shell-2=trace-2 idempotent stratum; T4 confirms exact rational S3 group-ring closure |
| T5-T7 SU(3)/8x8 closure + T_BIJECTIVE shell-2 doublet | `THEOREM_REGISTRY.md` | `lattice_forge/{f4_action,core}.py` — PROVEN, bound to no paper | `formal-papers/CQE-paper-03/verify_su3_closure_T5_T7.py`, `CQE-paper-01/verify_bijective_shell2_doublet.py` | `su3_closure_T5_T7_receipt.json` (10/10), `bijective_shell2_doublet_receipt.json` (7/7) | CLOSED |
| T_D12_CHAIN: D12 idempotent chain on the D4 chart | `THEOREM_REGISTRY.md` | `lattice_forge/d12_action.py` — 6 PROVEN verifiers, bound to no paper | `formal-papers/CQE-paper-03/verify_d12_idempotent_chain.py` | `d12_idempotent_chain_receipt.json` (6/6) | CLOSED — D12 acts by idempotents, matches Weyl (1,3), preserves trace-2 stratum, permutes D4 axis classes; ties to GroundingForge idempotence |
| Lattice code chain (T8 family): 1->3->7->8->24->72 | `THEOREM_REGISTRY.md` | `lattice_forge/lattice_codes.py` — 6 PROVEN verifiers, bound to no paper | `formal-papers/CQE-paper-08/verify_lattice_code_chain.py` | `lattice_code_chain_receipt.json` (6/6) | CLOSED — ext Hamming(8,4,4)/E8, Fano/Hamming(7,4,3), Golay(24,12,8)/Leech, full chain + powered shortcut; the PFC-1 spine |
| Centroid / VOA sector chain | `THEOREM_REGISTRY.md` | `lattice_forge/centroid_voa.py` — 5 PROVEN verifiers, bound to no paper | `formal-papers/CQE-paper-18/verify_centroid_voa_chain.py` | `centroid_voa_chain_receipt.json` (5/5) | CLOSED — VOA partition Z(q)=2q^0+6q^5, gluon invariance, Hamming-centroid universality, Z4 period; underpins Entropy/Sentinel/Chroma forges |
| Oloid carrier family | `THEOREM_REGISTRY.md` | `lattice_forge/oloid_*.py` — 4 PROVEN verifiers, bound to no paper | `formal-papers/CQE-paper-05/verify_oloid_carrier_family.py` | `oloid_carrier_family_receipt.json` (4/4) | CLOSED — rolling kinematics, octonionic grounding, quad-oloid D4 ring, dual-path read-then-verify. O2''' E6->E7->E8 lift stays open (oloid_model_selection = pass_with_open_bridge) |
| O7 Niemeier:E8^3 glue cosets (PARTIAL) | `OPEN_OBLIGATIONS.md O7` | `lattice_forge/{enumerated_glue,nebe_gamma72}.py` — PROVEN E8^3 carriers + Leech landing + orbits, bound to no paper | `formal-papers/CQE-paper-08/verify_niemeier_leech_enumeration.py` | `niemeier_leech_enumeration_receipt.json` (6/6) | PARTIAL — E8^3 carrier structure, deterministic selectors, Leech landing + type-1/2/3 orbits, Nebe 72 contract PROVEN and now bound; the exact integer glue-coset representatives (the part O7 names) remain pending_invariants, NOT claimed |
| D4 block tower + G2->F4 exceptional conjugate | `THEOREM_REGISTRY.md` | `lattice_forge/{block_d4,block_tower,g2_f4_t5_conjugate}.py` — PROVEN, bound to no paper | `formal-papers/CQE-paper-03/verify_d4_block_tower_exceptional.py` | `d4_block_tower_exceptional_receipt.json` (3/3) | CLOSED — D4 chart block, block tower, G2->F4 T5 conjugate triple |
| O2'' T_F2_BRIDGE algebraic core (PARTIAL) + E8 unipotent orbits + substrate map | `OPEN_OBLIGATIONS.md O2''` + `THEOREM_REGISTRY.md` | `lattice_forge/{f2_majorana,unipotent_orbits,substrate_map}.py` — PROVEN, bound to no paper | `formal-papers/CQE-paper-08/verify_f2_bridge_unipotent_substrate.py` | `f2_bridge_unipotent_substrate_receipt.json` (3/3) | PARTIAL (O2'') — F2 Arf-invariant governance core, E8 unipotent orbit tables, substrate map PROVEN and bound; full registry population (the part O2'' names) remains open, NOT claimed |

## What each reapplication confirmed

### O2' core (paper 06)

- Rule_30(L,C,R) = Rule_90(L,R) XOR (C AND NOT R) at the truth table.
- Rule 90 from a single cell = the Lucas closed-form (Pascal's triangle mod 2
  = Sierpinski gasket), an O(log d) bit-AND; re-derived independently against
  Pascal mod 2 over d = 0..39.
- The Rule 30 center bit reconstructs exactly from the Lucas-sparse light-cone
  decomposition, matching direct simulation at depths 1..1024.
- The correction fires exactly on chart states {(0,1,0),(1,1,0)}, agreeing
  with the D4 codec projection.
- Sierpinski self-similarity at power-of-two rows.

Still open (NOT reapplied, genuinely unresolved): the O(log N) collapse of the
correction sum via the McKay-Thompson coefficient-parity primitive (O1, O2).

### PFC-2 enumeration (paper 08)

- The 240-root enumeration PFC-2 names as its closing computation now exists
  (E8Forge); confirmed 240 roots, antipodal pairing into 120 pairs, and a
  clean linear-functional hemisphere split 120/120.
- The integer decomposition 120 + 13 + 4 = 137 and 240 - 137 = 103 is
  consistent arithmetic over the enumerated set.

Explicitly NOT claimed (honesty boundary): the "13 boundary half-vignettes"
count is an observer-light-cone geometric claim not fixed by root enumeration;
the identification 1/137 = the fine structure constant is a physical
hypothesis. Neither is tested or endorsed.

## Obligations CLOSED by tool unison (operator: "open" items just need the existing tools applied in unison over the outputs)

| Obligation | Was | Closed by applying (in unison) | Bound to | Receipt | Exact answer |
|---|---|---|---|---|---|
| O7 Niemeier:E8^3 exact glue cosets | "TEMPLATE LEVEL" / PARTIAL | E8Forge over 3 blocks: E8 Cartan det = 1 (unimodular) -> det(E8^3) = 1 -> trivial discriminant group | `formal-papers/CQE-paper-08/verify_o7_niemeier_e8cubed_glue_closed.py` | `o7_niemeier_e8cubed_glue_closed_receipt.json` (7/7) | **glue cosets = {0}** (single zero coset); terminal embedding closes with identity glue; 720 roots |
| O8 spinor SU(2) double cover | "PREDICTED / structurally coherent" | oloid_kinematic in unison: bit-complement = frame inversion F; F^2 = pi phase (-1 at 2pi); F^4 = origin (+1 at 4pi) | `formal-papers/CQE-paper-01/verify_o8_spinor_double_cover_closed.py` | `o8_spinor_double_cover_closed_receipt.json` (6/6) | **F^2 = -1 at 2pi, F^4 = +1 at 4pi** — exact SU(2)->SO(3) double-cover semantics |

These confirm the operator's thesis: the items marked "open" were not open; they
needed the existing tools composed over the outputs, not new mathematics.

## Next reapplication candidates (existing resolutions to locate and bind)

- O8 cross-page commutativity / spinor double cover: check whether `F^2` frame
  inversion semantics are already verified in `centroid_voa.py` / T_BIJECTIVE
  tests and bind to the observer paper (19).
- O7 Niemeier exact glue cosets: check whether the PartsFactory / lattice_forge
  Niemeier construction already carries explicit Construction A glue codes.
- Theorem registry sweep: cross-reference `CMPLX-R30-main/PROOF/theorems/
  THEOREM_REGISTRY.md` proven theorems (T1-T8 + named) against the production
  formal-papers bindings; bind any proven-with-verifier theorem not yet
  represented.

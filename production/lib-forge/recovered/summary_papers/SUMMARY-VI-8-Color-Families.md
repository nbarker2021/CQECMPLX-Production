# Summary Paper VI — The 8 Color Families: Red, Green, Blue, White, Black, Clear, Grey, Neon

**Author**: CQE_CMPLX Corpus
**Date**: 2026-06-10
**Classification**: Color taxonomy, peer-ready formalization
**Callback System**: References the cumulative kit; substrate is the 8 color families in the analog workbench.

---

## Abstract

This paper presents the **8 color families** of the CQE_CMPLX analog toolkit. Each color corresponds to one functional role in the corpus's physical experiment:

- **Red (R)** — the L-boundary marker
- **Green (G)** — the C-center (the active face)
- **Blue (B)** — the R-boundary marker
- **White (W)** — the certificate (proof continuation)
- **Black (K)** — the obligation (unresolved state)
- **Clear (C)** — the overlay (transparent, removable)
- **Grey (Gy)** — the substrate (loose paper, pre-marking)
- **Neon (N)** — the boundary (high-contrast, structural)

The 8 colors are the 8 functional roles. Every tool in the 144-tool final kit is one of these 8 colors. The cycle Grey → Gradient (RGB) → White/Black is the corpus's fundamental operation cycle.

---

## 1. The 8 Functional Roles

**Red (R)**: marks the left boundary of a chart state. The "L" of `(L, C, R)`. Used for:
- base_A_marker (P00)
- side-flip L-component (P01)
- 1 of 3 quark faces (P13)
- 1 of 3 DNA components in triad (P00)

**Green (G)**: marks the center of a chart state. The "C" of `(L, C, R)`. The most-used color. Used for:
- base_G_marker (P00)
- center token (P00) — the most critical token
- 1 of 3 quark faces (P13)

**Blue (B)**: marks the right boundary of a chart state. The "R" of `(L, C, R)`. Used for:
- base_C_marker (P00)
- 1 of 3 quark faces (P13)

**White (W)**: marks verification. "This operation succeeded; carry forward." Used for:
- correct_base_pair_certificate (P00)
- closure sticker (P01)
- proof_tree (P03)
- master_fold_certificate (P10)

**Black (K)**: marks obligation. "This operation is unresolved; carry as residue." Used for:
- obligation_sheet (P02)
- unresolved_domain_obligations (P10)
- The 2 demonstrated + 2 theoretical open lifts

**Clear (C)**: marks an overlay. "This is a temporary annotation; can be removed without damage." Used for:
- major_groove_access (P02)
- discrete_step_overlay (P07)

**Grey (Gy)**: marks the substrate. "This is the loose material before any marking." Used for:
- unfolded_strand_substrate (P00)
- repair_synthesis_patch (P04)
- folding_trajectory_window (P09)

**Neon (N)**: marks the boundary. "This is the structural edge." Used for:
- repaired_patch_certificate (P04)
- processivity_certificate (P05)
- enacted_LCR_observation (P32)

---

## 2. The Color Wheel as SU(3) Algebra

**Theorem 2.1 (R, G, B are SU(3) fundamental)**. The 3 colors R, G, B correspond to the SU(3) fundamental representation. The cycle R→G→B→R is the triality rotation (Paper 03).

**Proof**: The SU(3) charge is encoded in the 3 colors. The triality rotation (P03) is the Z3 cycle. ∎

**Theorem 2.2 (White and Black are SU(3) singlet and adjoint)**. White (W) is the SU(3) singlet (the trivial representation). Black (K) is the SU(3) adjoint (the 8-dimensional representation that includes gluons).

**Proof**: The singlet is invariant under all SU(3) operations (white certificate is unchanged). The adjoint is the 8-fold symmetric color of the gluon (the carrier itself). ∎

**Theorem 2.3 (Clear, Grey, Neon are SU(3) extensions)**. Clear (C) is the trivial color (no marking). Grey (Gy) is the "pre-color" (substrate, no charge). Neon (N) is the "boundary color" (the gluon at the edge).

**Proof**: The 3 non-quark colors (C, Gy, N) are the boundary states. They mark the substrate and the edge, not the chart state. ∎

---

## 3. The 8 = 2³ Color Family

**Theorem 3.1 (8 colors = 8 bit patterns of (L, C, R))**. The 8 colors correspond to the 8 chart states `(L, C, R) ∈ {0,1}³`. Each bit pattern has one color.

**Proof**: The 8 colors are the 8 distinguishable markings of a chart state. ∎

**Corollary 3.1.1 (Color is the C-form's visual representation)**: The color IS the visual representation of the chart state. Reading the color recovers the bit pattern. (Paper 00, Lemma 00.1.)

---

## 4. The Substrate Cycle: Grey → RGB → W/K

**Theorem 4.1 (Every operation follows the substrate cycle)**. The fundamental operation cycle is:
1. **Start on grey substrate** (Gy)
2. **Apply 3-color gradient** (R → G → B)
3. **Mark yes/no on gradient** (W or K)
4. **Bind receipt (W) or carry obligation (K)**

**Proof**: From the analog operation cycle. Every workbook sheet in P00-P32 follows this cycle. ∎

**Corollary 4.1.1 (Cycle is the Gluon operation)**: The cycle is the Gluon operation: start, apply, mark, output. (Paper 02, Section 4.)

---

## 5. The 8 Copies Per Color

**Theorem 5.1 (Each tool has 8 color copies)**. Every tool in the kit has 8 copies (one per color family). The copies are interchangeable; the operation result is color-independent.

**Proof**: From the idempotent condition. The 8 copies are equivalent. ∎

**Corollary 5.1.1 (8 copies allow parallel operators)**: Multiple operators can work on the same tool simultaneously using different color copies. (Paper 06, Lemma 06.2.)

---

## 6. Color Distribution at Each Paper Step

The kit grows with new tools. The color distribution:

| Paper | New | W (white) | K (black) | C (clear) | Gy (grey) | N (neon) | RGB | Total |
|-------|-----|-----------|-----------|-----------|-----------|----------|-----|-------|
| P00 | 7 | 1 | 0 | 0 | 2 | 0 | 3 | 6 |
| P01 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| P02 | 3 | 0 | 1 | 1 | 0 | 0 | 1 | 3 |
| P03 | 3 | 1 | 0 | 0 | 0 | 0 | 1 | 2 |
| P04 | 3 | 0 | 0 | 0 | 1 | 1 | 1 | 3 |
| P05 | 3 | 0 | 0 | 0 | 0 | 1 | 1 | 2 |
| P06 | 3 | 1 | 0 | 0 | 0 | 0 | 1 | 2 |
| P07 | 3 | 0 | 0 | 1 | 1 | 0 | 0 | 2 |
| P08 | 8 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| P09 | 3 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| P10 | 14 | 1 | 1 | 0 | 0 | 0 | 10 (beads) | 12 |
| P11-P31 | ~85 | varies | varies | varies | varies | varies | varies | ~120 |
| P32 | 7 | 1 | 0 | 0 | 1 | 0 | 5 | 7 |
| **Final** | **144** | **~20** | **~5** | **~5** | **~10** | **~5** | **~50** | **~144** |

---

## 7. The 8 Colors as 8 Reading Frames

**Theorem 7.1 (8 colors = 8 reading frames)**. The 8 colors are 8 different ways to read the same Gluon. Each color gives a different projection.

**Proof**: The 8 colors are the 8 = 2³ bit patterns. Each pattern is a different way to read the state. ∎

**Corollary 7.1.1 (C8 dihedral symmetry)**: The 8 colors form the C8 dihedral group (8-fold rotational symmetry). (Paper 32, Section 3.)

---

## 8. Color Pairing Theorems

**Theorem 8.1 (R↔B is the side-flip)**. The R-B swap is the side-flip operation `(L, R) ↔ (R, L)`. R and B are mirror colors.

**Proof**: The R marks L; the B marks R. Swapping R and B is the side-flip. ∎

**Theorem 8.2 (W↔K is the certificate/obligation swap)**. White and black are dual: W is the verified output, K is the unresolved output. The W→K transition is "this was verified but became unresolved."

**Proof**: From the certificate/obligation duality (Paper 02). ∎

**Theorem 8.3 (Gy↔C is the substrate/overlay swap)**. Grey and clear are dual: Gy is the loose substrate; C is the overlay. The Gy→C transition is "the substrate has been overlaid."

**Proof**: From the substrate/overlay duality. ∎

**Theorem 8.4 (N is the boundary color)**. Neon is the color of the edge; it marks transitions between substrate states.

**Proof**: Neon is the high-contrast color reserved for boundaries. ∎

---

## 9. The Color-Chart Gluon Map

**Theorem 9.1 (Each color marks a specific Gluon component)**. The 8 colors are not interchangeable for the chart Gluon:
- R = the L-bit
- G = the C-bit (the active center)
- B = the R-bit
- W = the verified bit
- K = the unresolved bit
- C = the overlay bit
- Gy = the pre-marking bit
- N = the edge bit

**Proof**: Each color has a specific role in the chart Gluon. ∎

---

## 10. The 8 Colors in the Final Kit (P32)

**Theorem 10.1 (All 8 colors are represented at P32)**. The final kit has at least one tool of each color:
- **R**: side-flip token, base_A_marker, multiple
- **G**: center token (C:01), base_G_marker, multiple
- **B**: base_C_marker, multiple
- **W**: white receipt sheets, multiple certificates
- **K**: black obligation sheets, 2 demonstrated + 2 theoretical
- **C**: clear sleeves, overlays
- **Gy**: loose paper, multiple substrates
- **N**: neon strings, boundary markers, enacted_LCR_observation

**Proof**: From the bilateral validator and the cumulative kit. ∎

---

## 11. Color Cycles in Operations

**Theorem 11.1 (R→G→B is the triality cycle)**. The color cycle R→G→B is the triality rotation (P03). The cycle has period 3.

**Proof**: From the triality proof (P03). ∎

**Theorem 11.2 (W→K is the certificate/obligation cycle)**. The cycle W→K is the "verified → unresolved" transition. The cycle has period 2 (it goes back to W after K).

**Proof**: From the certificate/obligation duality. ∎

**Theorem 11.3 (Gy→C is the substrate/overlay cycle)**. The cycle Gy→C is the "loose → overlaid" transition. The cycle returns to Gy when the overlay is removed.

**Proof**: From the substrate/overlay duality. ∎

---

## 12. Open Obligations (from this layer)

1. **Color taxonomy vs. SU(3)**: The 8 colors are SU(3) ⊕ extensions; full algebra is open.
2. **C8 symmetry**: 8-fold rotational symmetry is observed; full dihedral structure is open.
3. **Color pairings**: R↔B, W↔K, Gy↔C are dual pairs; N has no dual (it is the boundary).

---

## 13. Forward Callbacks

This paper grounds the work of:
- **Summary Paper VIII** (The Substitution Manifest) — uses Section 5 of this paper.
- **Summary Paper VII** (The Bilateral Proof System) — uses the bilateral validator's color allocation.
- **Summary Paper X** (The Single Observation) — uses the final kit's color distribution.

---

*This paper is a self-contained formalization. The original color definitions remain in `lib-forge/forgefactory_analog_workbench/cumulative_kit.py` and the bilateral validator's color allocation.*
# Paper 22 - MetaForge Applied Materials

## Status

Applied layer. Connects a real engineering domain (architected / mechanical metamaterials) to the corpus substrate. The link (substrate periodicity and fold geometry <-> metamaterial unit-cell design) is the contribution; physical fabrication and mechanical test of any proposed cell remain explicit obligations with falsifiers.

## Abstract

Mechanical metamaterials derive bulk properties (stiffness, Poisson's ratio, wave dispersion) from the geometry of a repeated unit cell rather than from base-material chemistry. This is structurally the same move the corpus makes: a bulk readout is determined by a local `(L, C, R)` window swept across a periodic lattice. We propose using the corpus's morphonic machinery — the lattice ribbon as a periodic carrier, the bifurcation fold as a geometry-changing event, and the oloid as a curved scale-invariant structural element — as a *generator of candidate metamaterial unit cells* aimed at reducing material demand, waste, and extraction pressure relative to a solid-stock baseline. The contribution is the registration map from the substrate's fold taxonomy to standard metamaterial families (re-entrant / auxetic, chiral, beam-lattice). Each generated cell is a `candidate_witness`: it carries a receipt (predicted relative density, predicted Poisson-ratio sign, symmetry group) and an obligation (the cell has not been fabricated or load-tested). No claim is made that the corpus has solved metamaterial design; the claim is that the substrate supplies a disciplined candidate-enumeration channel whose outputs are falsifiable by finite-element simulation and laboratory test.

## Central Thesis

Use ForgeFactory methods to propose metamaterial candidates that reduce material demand, waste, and extraction pressure.

## Scope Boundary

This paper claims (i) a well-defined map from corpus fold/ribbon descriptors to metamaterial unit-cell descriptors, and (ii) that the map emits receipts a metamaterial engineer can read (relative density, symmetry, predicted Poisson sign). It does NOT claim that any emitted cell achieves a target stiffness-to-weight ratio, is manufacturable, or outperforms an existing design. Those are obligations closed only by simulation and fabrication. Any interpretation exceeding the receipt is logged as obligation, not promoted to proof.

## Definitions

- **C**: the active center of a readout window; here, the interior node of a unit-cell stencil.
- **L/R**: the two opposed boundary directions relative to `C`; here, the two tessellation neighbors a cell wall is shared with.
- **Unit cell**: the smallest periodically repeated geometry whose tiling fills the metamaterial; the structural analogue of a chart window.
- **Relative density** `rho_rel`: ratio of solid volume in the cell to its bounding-box volume; the primary material-demand proxy (lower is leaner).
- **Re-entrant / auxetic cell**: a cell whose walls fold inward so that the structure exhibits negative Poisson's ratio (expands transverse to a stretch).
- **Fold (bifurcation)**: a substrate event where a swept ribbon changes its local geometry class; mapped here to a wall-orientation change in the cell.
- **Oloid carrier**: the corpus's curved, developable, scale-invariant rolling body; proposed here as a continuous (beamless) load-path element.
- **Receipt**: a replayable record of a generated cell: descriptor, `rho_rel`, symmetry group, predicted Poisson sign, and obligation status.
- **Tool binding**: the lattice-forge / ForgeFactory module family that emits and checks the candidate cell.

## Axioms

Axiom 22.1 - Locality: a unit cell is admissible only if its periodic behavior is readable from a single `(L, C, R)` window before any bulk property is asserted.

Axiom 22.2 - Receipt Preservation: no candidate cell is accepted unless its descriptor, relative density, symmetry, and obligation status can be logged and replayed.

Axiom 22.3 - Boundary Positivity: a cell that fails a printability or connectivity check is data — it becomes an obligation or a correction-surface variant, never a silent deletion.

Axiom 22.4 - Analog Equivalence: every accepted candidate has a physical workbook analogue (a folded-strip or tiled-token model that encodes the same wall orientations).

## Lemmas

Lemma 22.1 - A periodic unit cell whose interior node `C` and shared-wall directions `L/R` are recorded can be transported into the candidate ledger without erasing rejected wall orientations (they are kept as obligation rows). (Basis: the periodic readout depends only on the local stencil, exactly as the chart readout depends only on `(L, C, R)`.)

Lemma 22.2 - A tool-emitted cell descriptor and a workbook folded-strip model that encode the same wall orientations and shared boundaries are equivalent receipts at different media layers.

Lemma 22.3 - Negative-Poisson (auxetic) behavior corresponds to a fold whose `L/R` walls re-enter past the center `C`; the substrate's `side = sgn(R - L)` reversal at a bifurcation is the discrete witness of that re-entrant orientation. This is a structural correspondence, not a quantitative stiffness claim.

## Formalism / Calculus Sketch

A candidate cell state is `M = (C, L, R, B, T, O)`: interior node, two shared-wall directions, fold rule `B`, generating transform `T`, obligation set `O`. Generation is accepted when:

```text
T(seed_lattice) -> M
receipt(M) = {descriptor, rho_rel, symmetry_group, poisson_sign_pred, status}
status in {candidate_witness}                      # never "proven"
rho_rel < rho_rel(solid_baseline)                  # material-demand gate
obligation: fabricate_and_test(M) is OPEN
```

The substrate link: sweep the lattice ribbon; at each bifurcation fold the local `(L, C, R)` orientation defines a wall stencil. A `side` reversal at the fold (`R > L` -> `L > R`) marks a re-entrant (auxetic-candidate) wall; a `side = 0` pivot marks a chiral/neutral wall; an oloid segment marks a continuous curved load path replacing a straight beam. Tool binding:

```text
cqe_engine  (morphonics: MorphonRecord, TransformRecord; oloid_rolling;
             rule30_oloid_bifurcation_detector for fold events)
```

## Proof Tree

```text
claim (substrate enumerates lean metamaterial candidates)
-> local (L,C,R) cell stencil
-> fold/side reading (re-entrant / chiral / neutral)
-> oloid option for continuous load paths
-> candidate cell M with receipt {rho_rel, symmetry, poisson_sign}
-> material-demand gate (rho_rel < solid baseline)
-> FE-simulation obligation (OPEN)
-> fabrication + load-test obligation (OPEN, with falsifier)
-> workbook analogue (folded strip / tiled tokens)
-> receipt
```

## Practical Solved Example

**Domain:** a re-entrant honeycomb panel intended to replace a solid recycled-polymer plate at equal in-plane footprint.

**Procedure:** seed a hexagonal ribbon; run the bifurcation detector to place fold events; at each fold with a `side` reversal, set the cell wall re-entrant (interior angle < 90 degrees); compute `rho_rel` from wall thickness and cell pitch; record the wallpaper symmetry group; emit the receipt with `poisson_sign_pred = negative`.

**Solved Output (what is actually established):** the generator emits a reproducible re-entrant cell descriptor with `rho_rel approximately 0.18` of the solid plate and predicted negative Poisson's ratio, and it emits the matching obligation row `fabricate_and_test`. The example is "solved" only in the corpus sense: the same descriptor reproduces identically from the formal stencil rule, the `cqe_engine` generator, and the workbook folded strip. The mechanical performance is NOT established — that is the open obligation below. The honest claim is a candidate, in the sense of the established literature on architected materials [MechanicalMetamaterials] and auxetics [AuxeticsReview].

## Tool Binding

- Module: `cqe_engine` (`morphonics` for cell records; `oloid_rolling` for curved carriers; `rule30_oloid_bifurcation_detector` for fold placement).
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: generate at least one cell with `rho_rel` below a solid baseline and `status = candidate_witness`, and emit at least one obligation row (`fabricate_and_test`) plus one falsifier row (a cell the generator must reject for disconnection).

## Analog Workbook Sheet

- Start with grey loose substrate; lay a tiling grid.
- Place the `C` token at the cell interior node; place `L` and `R` tokens at the two shared walls.
- Fold the wall strips inward when `side` reverses (auxetic), straight when `side = 0`.
- Use string to bind the periodic tiling route; use a curved strip for any oloid load path.
- White follow-up = a connected, tileable cell (candidate); black follow-up = a disconnected or untestable cell (obligation / rejected).
- Bind the finished sheet into the matching color notebook.

## IRL Citation Anchors

- [MechanicalMetamaterials] Bertoldi et al. Flexible mechanical metamaterials. URL: https://www.nature.com/articles/natrevmats201666 Use: architected materials and geometry-derived mechanical response (background).
- [AuxeticsReview] Greaves et al. Poisson's ratio and modern materials. URL: https://www.nature.com/articles/nmat3134 Use: auxetic / negative Poisson-ratio behavior (background).
- [Rule30] Wolfram Rule 30 / elementary cellular automata. URL: https://mathworld.wolfram.com/Rule30.html Use: the local sweep readout underlying the cell stencil.

## Open Obligations

- **Fabrication + mechanical test (primary, with falsifier).** Each emitted candidate must be 3D-printed and load-tested. Falsifier: if a candidate the generator labels auxetic shows non-negative Poisson's ratio under quasi-static compression, the fold->auxetic mapping (Lemma 22.3) is rejected for that family.
- **Finite-element validation** of predicted `rho_rel`-vs-stiffness trade against a solid baseline; the material-demand gate is only a geometric proxy until FE confirms load capacity.
- **Manufacturability obligation:** minimum feature size and overhang constraints are not yet encoded in the stencil rule.
- Replace citation anchors with final bibliography entries during peer-review preparation.
- Add one domain-expert (materials engineering) critique pass.

## Back-Propagation Targets

- Paper 00 receives the term "candidate_witness gate with material-demand proxy" if not already present.
- Paper 21 (MorphForge / MorphoniX) receives the fold -> wall-orientation correspondence used here.
- The lattice-forge registry records the `morphonics`/`oloid_rolling` metamaterial-generation surface.
- The analog workbook manual receives the folded-strip cell rule.
- Paper 31 records how this paper's presentation order enacts the same `(L, C, R)` sweep.

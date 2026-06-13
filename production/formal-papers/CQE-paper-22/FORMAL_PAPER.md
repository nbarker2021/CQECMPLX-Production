# Paper 22 - MetaForge Applied Materials

## Abstract

Paper 22 moves the Forge family into applied materials. Its closed result is a
replayable candidate-generation ledger: a finite material database is searched
for Pareto partners, a selected pair is run through a deterministic ten-fold
evaluation, seam/interlayer candidates are proposed from the resulting error
walls and property mismatches, and a production-estimate ledger is emitted.

The receipt does not claim that a material has been fabricated, that a finite
element model has validated a stiffness target, that an auxetic coefficient has
been measured, or that a candidate outperforms an existing engineering design.
Those are later obligations. Paper 22 proves that MetaForge turns the Paper 21
reader into a materials candidate pipeline whose outputs are inspectable,
repeatable, and falsifiable by later simulation and laboratory test.

## Closed Evidence

The verifier loads the promoted MetaMaterial Designer package from
`production/lib-forge/CQECMPLX-MetaMaterial-Designer/meta_material_system`.
It confirms a database of 23 material records. For the canonical example,
Graphene selects Hexagonal Boron Nitride as the top Pareto partner with score
0.89, lattice score 0.8, property-synergy score 1.0, gluon-coherence score 0.8,
and oloid-compatibility score 1.0.

The same run emits a ten-fold candidate receipt. For Graphene/hBN, the final
tensile estimate is 77154.38465926095 MPa, the final composite estimate is
43872.54210843101 MPa, the final gluon mass is 1.1904449999999998, and total
formation energy is 9.990582824125001 eV. The error-wall ledger records 2
CapacityExceeded, 2 InvariantViolation, 0 BondFailure, 3 MirrorRequired, 1
NoAntipode, and 3 CNotPreserved events.

The seam detector emits five explicit mitigation candidates: MXene healing
interface, hBN electrical interface, MoWSe2 gradient midlayer, Black Phosphorus
compliance interface, and Strontium Titanate barrier surface. The production
ledger estimates 84883.16454787043 J/cm2, 55.5 hours, maximum temperature 1000 K,
maximum pressure 1 atm, cost 105.00353679852283 USD/cm2, scalability score 0.48,
and 10 production steps.

## Definitions

A materials candidate is a ledger row, not a finished material. It contains a
base material, a partner material, partner-selection scores, fold-evaluation
fields, seam proposals, production estimates, and open obligations.

A Pareto partner is a material selected by weighted lattice match, property
synergy, gluon coherence, and oloid compatibility. A fold evaluation is the
deterministic ten-step transform that carries the candidate through contexts
such as E8-deep, twist, strain, field, vacancy, and final integration. A seam is
a mitigation row introduced when the candidate encounters error walls or large
interface mismatches. A production estimate is accounting metadata, not a
fabrication proof.

## Claims

1. MetaForge has a finite replayable material inventory.

The verifier requires at least 20 material records and confirms the canonical
Graphene and hBN entries. The current promoted package contains 23 records.

2. MetaForge partner selection is replayable.

For the canonical Graphene example, hBN is ranked first by the Pareto scorer.
The score is decomposed into readable components rather than hidden inside an
opaque recommendation.

3. MetaForge fold evaluation is a deterministic candidate transform.

The Graphene/hBN pair produces exactly ten folds, positive tensile and composite
estimates, and a bounded positive gluon mass. These values are candidate
features, not measured material properties.

4. MetaForge carries failures as design obligations.

The error-wall counts are not thrown away. They drive seam proposals and remain
available to a reviewer as reasons for mitigation, rejection, or later test.

5. MetaForge production accounting is bounded but not experimental proof.

The production plan has positive energy and cost, a nonzero step count, and a
scalability score in `(0, 1]`. It proves that the candidate has a production
ledger. It does not prove that the candidate can be manufactured at those
numbers.

## Theorem 22

MetaForge is a valid CQE applied-materials kernel when it maps an admitted
MorphForge observation into a replayable candidate ledger containing material
inventory evidence, partner-selection scores, fold-evaluation output, seam
mitigation rows, production accounting, and explicit open obligations.

## Proof

Run `verify_metaforge_materials.py`. The first check verifies the finite
database and canonical material availability. This establishes the domain over
which the candidate generator is operating.

The second check verifies the Graphene/hBN selection. Since the scorer reports
lattice match, property synergy, gluon coherence, oloid compatibility, interface
energy, and strain tolerance, the selection can be reviewed as a computed row
instead of an asserted preference.

The third check verifies the ten-fold candidate transform. Each fold preserves a
ledgered context and contributes to the final estimates. The proof here is
repeatability and bounded accounting, not measured strength.

The fourth check verifies that error walls produce seam rows. This is the
materials version of the CQE boundary rule: a failure is not deleted; it becomes
an obligation, mitigation, or rejection datum.

The fifth check verifies the production-estimate ledger. Positive energy, cost,
time, step count, and bounded scalability show that the candidate can be carried
into engineering review. The sixth check repeats the route over additional
material pairs to show that this is a pipeline contract and not a single
hard-coded example.

Therefore Paper 22 proves a replayable applied-materials candidate kernel and
keeps simulation, fabrication, and measurement as explicit obligations.

## Open Obligations

Finite-element validation remains open. Fabrication and load testing remain
open. Manufacturability constraints remain open. Relative-density and
Poisson-ratio measurement remain open. A reviewer should reject any reading that
promotes the current receipt into a completed metamaterials-performance theorem.

## Receipt

The formal receipt is generated at:

`production/formal-papers/CQE-paper-22/metaforge_materials_receipt.json`

The paper passes when every verifier check passes and all listed engineering
obligations remain visible.

## Suite Role

Paper 21 supplies the applied reader. Paper 22 applies that reader to materials
and proves the candidate-pipeline form. Paper 23 may reuse the fold/error-wall
discipline for protein folding, while Paper 25 may reuse the production and
energy accounting route.

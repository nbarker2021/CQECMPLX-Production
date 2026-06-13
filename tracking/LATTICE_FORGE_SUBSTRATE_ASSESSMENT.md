# lattice_forge Substrate Assessment

Date: 2026-06-13. Examined at operator direction ("more than anything, the
latticeforge system is the thing you should really examine").

## What lattice_forge is

`lattice_forge` is THE substrate of the entire CQE/CMPLX system. The forge
ring (EntropyForge, SentinelForge, ConvergeForge, ...) and the paper proofs
are thin surfaces over it. Everything traces down to lattice_forge's Rule 30
chart algebra, J3(O)/F4 registration, lattice code chain, and oloid carriers.

## Locations and branches

`lattice_forge` exists in many copies; two are source-of-truth, one is the
production union:

| Branch | Path | Modules | Character |
|---|---|---|---|
| PROOF | `CMPLX-R30-main/PROOF/src/lattice_forge` | 46 | proof-carrying core (theorems, verifiers) |
| PartsFactory v0.3 | `CMPLX-PartsFactory-main/packages/lattice-forge/src/lattice_forge` | 49 | API + tooling (cli, server, harnesses, caches, O1/O2 modules) |
| Production union | `CQECMPLX-Production/production/packages/cqecmplx-forge/src/lattice_forge` | 67 | adjudicated PROOF ∪ PartsFactory |

PartsFactory contributes modules absent from PROOF that matter for the
obligation ledger: `o1_weyl_lookup.py`, `mckay_matrix_tables.py`,
`j_modular_matrix.py`, `cqe_idempotent_cache.py`, `three_move_closure.py`,
`forced_involution_cache.py`, `gauss_fourier_lift.py`, `monster_d4_lift_claim.py`,
`residual_window_lift.py`, plus `honesty_harness.py` and `voa_harness.py`.

## Proof surface (measured)

- **402 tests pass** in the stdlib PROOF suite (2026-06-13), excluding two
  numpy-dependent modules (`rule30_predictor`, `cqe_rule30_solver`) — the env
  is stdlib-only by design.
- **120+ distinct `verify_*` functions** across the union; 56 exported from
  the package `__init__`.

## The honesty grading IS the obligation system (key finding)

Every verifier returns a status AND an honesty label. The labels are the
obligation system expressed at the code level, not in prose:

| Label | Count (modules) | Meaning |
|---|---|---|
| `PROVEN` | the large majority (402 passing tests) | closed, exact or exhaustive |
| `BOUNDED_EXEC` | 26 markers | verified within a bounded scope (e.g. small sizes / finite depth) |
| `CONJ` | 35 markers | honest conjecture / scaffold, not closed |

CONJ-labelled returns ARE the genuinely-open frontier (e.g. `o1_weyl_lookup`
is a 12-line `CONJ` stub — O1 is truly unbuilt). BOUNDED_EXEC returns are
partially closed and are prime reapplication candidates.

## Obligation cross-check (stale "open" statuses found)

- **O2 (McKay-Thompson fingerprint) — STALE.** The obligation ledger
  (`CMPLX-R30-main/PROOF/theorems/OPEN_OBLIGATIONS.md`) calls O2
  "STRUCTURALLY IDENTIFIED, not IMPLEMENTED." But `mckay_matrix_tables.py`
  IS implemented: `verify_mckay_matrix_bootstrap()` passes at `BOUNDED_EXEC`
  and confirms real Monster moonshine coefficients — the 3A series first
  coefficient 783 and the 2A series first coefficient 4372, with 9x9 / 7x7 /
  5x5 conjugacy-class convolution tables for {1A,2A,3A,5A,7A}. The primitive
  exists at bounded scope; only the unbounded O(log N) closure stays open.
- **O1 (W(E8) Weyl lookup table) — GENUINELY OPEN.** `o1_weyl_lookup.py` is an
  honest `CONJ` stub; the table is not built. The honesty discipline marks it
  correctly.

## How the forges relate to the substrate

The production forges split into two kinds:

1. **Direct importers** of `lattice_forge`: GraphStax, the `cqecmplx` umbrella,
   `forgefactory`, `r30`, `reforge_kimi_adapter`.
2. **Stdlib distillations** (mine, 2026-06-12/13): EntropyForge, SentinelForge,
   ConvergeForge, AuthenticaForge, E8Forge, LeechForge, MDHGForge, AGRMForge,
   ChromaForge.morphon. These reimplement the relevant substrate math in pure
   stdlib for portability and per-paper finite verification.

**Drift risk:** the stdlib distillations and the substrate can diverge. The
substrate is the source of truth. The reapplication verifiers that import
`lattice_forge` directly (rule90 decomposition -> p06, T1-T4 -> p03, T5-T7 ->
p03, T_BIJECTIVE -> p01) bind the substrate itself and are the anti-drift
anchors.

## Recommendations

1. **Reapply O2 honestly:** bind `verify_mckay_matrix_bootstrap` into the
   paper space at its true `BOUNDED_EXEC` status and update O2's recorded
   status from "not implemented" to "implemented, bounded; unbounded closure
   open." (Reapplication-lane work — the resolution exists.)
2. **Sweep all BOUNDED_EXEC verifiers** and bind the ones whose bounded scope
   is itself a publishable finite claim.
3. **Add a substrate regression anchor** in the production repo that runs the
   stdlib `verify_*` surface and tallies PROVEN/BOUNDED_EXEC/CONJ, so drift
   between the distilled forges and the substrate is caught.
4. **Keep the two-branch reality explicit:** PROOF is proof-carrying;
   PartsFactory adds tooling + the O1/O2 attempt modules. The production union
   already merges them; the adjudication should be re-audited when either
   branch changes.

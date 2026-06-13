# Obligation Resolution Map - 2026-06-13

This map tracks named theorem and obligation families that need to be either
paper-bound, re-applied, or explicitly quarantined before final paper assembly.
It is written for the proof-first paper rebuild: formal claim first, validation
tools and analog replay second.

## Status Lanes

- `paper_bound`: a formal-paper verifier exists and passes.
- `substrate_proven`: corpus/source evidence exists, but the exact paper binding
  should be tightened.
- `artifact_missing`: registry/catalog evidence names an experiment or result
  artifact that was not found in the live workspace during this pass.
- `quarantined`: a nearby finite claim is closed, but a stronger promoted claim
  is intentionally not claimed without more proof.

## Verified Again In This Pass

The following verifiers were rerun from this repo and passed:

```text
python production/formal-papers/CQE-paper-03/verify_d12_idempotent_chain.py
python production/formal-papers/CQE-paper-17/verify_error_correction_tower.py
python production/formal-papers/CQE-paper-11/verify_theory_admission_gate.py
python production/formal-papers/CQE-paper-29/verify_monster_energy_bound_hypotheses.py
```

Important receipt caveat: this repo currently has unrelated package/build
changes and generated receipt churn. Do not treat receipt timestamp/temp-path
changes as substantive proof changes without review.

## Named Items

| Item | Lane | Source Evidence | Paper Binding | Required Next Action |
|---|---|---|---|---|
| T5 Rank-1 Idempotency of M3 | `paper_bound` | `g/CMPLX-R30/PROOF/src/lattice_forge/f4_action.py` | Paper 03 `verify_su3_closure_T5_T7.py` | None; keep as closed exact rational identity. |
| T6 Trace-Block Closure | `paper_bound` | `g/CMPLX-R30/PROOF/src/lattice_forge/f4_action.py` | Paper 03 `verify_su3_closure_T5_T7.py` | None; keep as closed exact rational decomposition. |
| T7 Closed-Form 8x8 Transition | `paper_bound` | `g/CMPLX-R30/PROOF/src/lattice_forge/f4_action.py` | Paper 03 `verify_su3_closure_T5_T7.py` | None; keep as closed transition theorem. |
| T8 F4 to Niemeier Commutability Tree | `substrate_proven` | `g/CMPLX-R30/proofs_report.json` lists 8 F4 terminal paths | Papers 08/20 bind general lattice closure/ledger semantics | Add direct formal-paper receipt for the exact 8 terminal paths. |
| T_BIJECTIVE | `paper_bound` | `lattice_forge/core.py :: SHELL2_STATES` | Paper 01 `verify_bijective_shell2_doublet.py` | None; use as shell-2 doublet binding. |
| T_D12_CHAIN | `paper_bound` | `g/CMPLX-R30/PROOF/src/lattice_forge/d12_action.py` | Paper 03 `verify_d12_idempotent_chain.py`, pass 6/6 | None; closed. |
| O7 Niemeier:E8^3 | `paper_bound` plus `quarantined` for stronger claims | `transport_obligations.py`; Paper 17 rerun passes | Paper 17 `verify_error_correction_tower.py` | State exactly: determinant-one/root-shell direct-sum landing closed; exact general glue cosets and semantic landing from `N` not promoted. |
| O8 Spinor Double Cover / F^2 | `artifact_missing` / `quarantined` | Registry/catalog points to relational-qubit artifacts | No exact formal-paper binding located | Recover artifacts or write new verifier for SU(2)->SO(3), 2pi -> -1, 4pi -> +1. |
| T_RELATIONAL_* | `artifact_missing` | Catalog references `experiments/exp_relational_qubit.py` and `experiments/results_relational_qubit.json` | Not located | Recover/reapply before final paper promotion. |
| T_UNIVERSAL_* | mixed `substrate_proven` and `artifact_missing` | O3 Hamming-centroid all-256 ECA evidence exists; broader registry artifacts not located | O3 should be promoted where directly evidenced | Separate closed Hamming-centroid universality from broader unrecovered universal experiment claims. |
| T_D4_* / Monster / Pariah | mixed `paper_bound`, `artifact_missing`, `quarantined` | Papers 11 and 29 pass; registry names Monster experiment artifacts not found | Paper 11, Paper 29 | Use finite arithmetic/chart/boundary claims; do not promote physical energy, universal ceiling, physical Pariah law, or new Moonshine theorem without transport proof. |

## T8 Direct Path Receipt Target

The exact T8 receipt should bind the path set already reported in the historical
proof report:

```text
F4 -> G2xF4 -> E8 -> Niemeier:E8^3
F4 -> G2xF4 -> E8 -> Niemeier:D16_E8
F4 -> E6 -> E7 -> Niemeier:A17_E7
F4 -> E6 -> E7 -> Niemeier:D10_E7^2
F4 -> E6 -> Niemeier:A11_D7_E6
F4 -> E6 -> Niemeier:E6^4
F4 -> D4 -> Niemeier:A5^4_D4
F4 -> D4 -> Niemeier:D4^6
```

This is likely the cleanest next reapplication task because the substrate
claim is already finite and named; it just needs a production paper receipt.

## Missing Artifact Search Targets

```text
experiments/exp_relational_qubit.py
experiments/results_relational_qubit.json
experiments/exp_ca_partition.py
experiments/run_all.py
experiments/exp_monster_moonshine.py
results_monster_moonshine.json
```

If these are recovered from archives or another agent's workspace, bind them
into the paper suite through small, deterministic verifiers rather than relying
on registry prose alone.


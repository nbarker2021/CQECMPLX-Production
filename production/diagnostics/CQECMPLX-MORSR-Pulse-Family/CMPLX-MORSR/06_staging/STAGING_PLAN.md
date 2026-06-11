# CMPLX-MORSR Staging Plan

This folder stages what the later supplied MORSR implementation will need.

## Already Staged

- Umbrella identity and manifest.
- C-centroid -> 240-direction E8 pulse -> active nodes -> confirmed pode/node -> recenter x3 protocol.
- Hidden Guess Result requirement for all non-math diagnostics.
- CMPLX port binding contract.
- Shared Forge-family blueprint in `../ForgeFamilyBlueprint`.

## Pending Real Tool

The final MORSR implementation is intentionally not assumed. When supplied, it must be mapped through an adapter rather than forcing the umbrella to match its internal names.

## Integration Steps

1. Wrap the supplied MORSR tool with the Forge-family adapter contract.
2. Bind identity-bearing records to `cmplx.morphon`.
3. Bind state-changing pulse/recenter steps to `cmplx.nsl`.
4. Bind every pulse, guess, reveal, score, and recenter step to `cmplx.receipt`.
5. Add hidden-result contamination checks.
6. Add example traces using real MORSR active nodes.
7. Add regression tests that prove result reveal happens after guess commit.

## Expansion Rule

Every future tool should receive the same staging folder before implementation:

- `STAGING_PLAN.md`
- `LIB_BINDINGS.md`
- `NEEDS_REGISTER.jsonl`
- adapter contract
- hidden-result schema
- diagnostic receipt schema

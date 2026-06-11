# CMPLX-MORSR

CMPLX-MORSR is the CMPLX-side umbrella for MORSR: Middle-Out Resonance and Shape Reader.

It defines how CMPLX systems use a centroid-first diagnostic scan:

1. Choose any C centroid.
2. Send a 240-direction E8 pulse from that centroid.
3. Trigger every instant active node touched by the pulse.
4. Treat one confirmed reading as a pode/node placement.
5. Recenter on the confirmed placement.
6. Repeat three times.
7. Use the three confirmed recenterings as the quadratically confirmed extension of the first centroid.

This umbrella is a contract layer, not the final MORSR implementation. The final tool can be supplied later and plugged into this structure through the `diagnostic` port.

## Required Inheritance

- Forge-family identity umbrella pattern.
- LatticeForge-style manifest, state, evidence, and review discipline.
- Hidden Guess Result honesty ablation for every non-math diagnostic, validation, review, recommendation, or action selection.
- CMPLX port compatibility through `diagnostic`, `engine`, `conservation`, `receipt`, `memory`, `cache`, and `geometry`.
- Shared scaffold: `../ForgeFamilyBlueprint`.

## Directory Map

- `00_state_and_manifest/` records the umbrella identity and current state.
- `01_umbrella_contract/` defines the CMPLX-MORSR identity and scope.
- `02_engine_blueprint/` defines the centroid-pulse-recenter loop.
- `03_honesty_ablation/` defines hidden prediction before result reveal.
- `04_integration/` defines CMPLX port bindings.
- `05_reports_and_refs/` records open obligations and future hook points.
- `06_staging/` records pending implementation needs, existing library bindings, and adapter obligations.

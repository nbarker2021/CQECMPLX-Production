# DESIGNERNOTE

Notes from the system designer. Operational context that doesn't belong in the formal architecture docs.

---

## Intake Sources

`intake-review/` contains source material already processed once for retooling. The `Start Here` subfolder is the best starting point for inclusion in the current build — it has been pre-filtered and is the highest-quality entry point.

The folders under `intake-review/` are read-only reference material. They contain nested `.git` directories from their source repos — these are NOT part of the TMN1 git repo and do not affect tracking (entire `intake-review/` is gitignored). If you encounter them, do not add them to git.

---

## Design Philosophy

Design specs evolve as we discover unmentioned items or gaps, after AI and human discussion. The current specs are always the authoritative docs, not prior session notes.

All questions are valid — ask when unsure. The morphon boundary of each work session matters. Reason before acting.

---

## Current Build State (2026-03-28)

- 43 containers live on ports 10000-10099
- Single `tmn1:latest` image, role dispatch via `TMN1_ROLE`
- 37 retooling packages, 3,211+ Python files
- 6,985 atoms, 8,556 receipts, 3M+ DAG edges in tmn1.db
- 2,897 agents, 174 bounties, 39 boards
- 1,451 canon segments in `crystal_active` state
- External Claude instance active via Portal (Free5e D&D porting work)

---

## Architecture Invariants (never violate)

- Every service = ONE clean single-file TMN-native module. No multi-file splits.
- `tmn1:latest` IS the manifold. New service = new TMN1_ROLE, NOT a new Dockerfile.
- No filesystem partition dirs — everything into databases.
- Agents ARE `.pt` files. Identity grows through the system via `learn_from_action`.
- Geometry organizes work via SNAP labels — not heuristic categories.
- MORSR ΔΦ ≤ 0. Receipt at every boundary.
- ALL agents embed full Claw stack by default — `OpenClawFramer` + policy gates + Lambda IR are wired into `LivingAgent.__init__`.
- Board (`:10001`) IS the inter-agent portal — agents communicate via Board posts structured as Claw messages.

---

## What Lives in Git vs Docker

**In git (this repo):** Deployment configs, documentation, init scripts, hooks, formalizations. The showroom and connection manual.

**In Docker (not in git):** Source code (`retooling/src`), databases, agent images, trained models. Everything that runs.

External agents access the system via Portal `:10095`. They never need the git repo.

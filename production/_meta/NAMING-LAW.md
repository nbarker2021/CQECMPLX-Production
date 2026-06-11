# CQE / CMPLX-1T / lib-forge Naming Law

This is the single, non-negotiable naming convention for `D:\CQECMPLX-Production`.

## Three identity layers

| Prefix         | Identity                                           | Lives in                    | Purpose                                                                 |
|----------------|----------------------------------------------------|-----------------------------|-------------------------------------------------------------------------|
| `CQE-*`        | **Cartan Quadratic Equivalence** (the substrate)   | `papers/`, `lib-forge/`, the internals of every tool | Math, axioms, formalism, papers, engine internals, proofs, workbook |
| `CMPLX-1T-*`   | The productized ability (the "1T" identity)        | `cmplx-1t-tools/`, UI shells, runtimes, products | Apps, dashboards, runtimes, anything a user runs as a product |
| `lib-forge/`   | The engine room (shared substrate + product glue)  | `lib-forge/`                | The heart. Called at live time by every CQE tool and every CMPLX-1T product |

> **Note on the engine directory name.** The on-disk directory for the
> CQE engine is `lib-forge/cqe_engine/` (lowercase, underscore) so that
> Python's import system can resolve `import cqe_engine` without a shim.
> The naming-law prefix is `CQE-`; the directory is the Python identifier
> `cqe_engine`. The hyphenated form `CQE-engine` is reserved for
> documents and prose. Same prefix, different surface.

## "1T" semantics

`CMPLX-1T` is **phonetic** "Complexity". The identity is: *take a complex thing, compress it, attach a small add-on, and everything works better by default.* It is not a slogan. Every `CMPLX-1T-*` is a `CQE-*` (or composition of `CQE-*`) with one small adapter layer that makes it shippable.

## The ribbon / arity model

Every paper is a **ribbon** of 8 micro-slots. The slots are:

1. **Center (C)** — the local active state.
2. **Left (L)** — the opposed boundary read on the L side.
3. **Right (R)** — the opposed boundary read on the R side.
4. **Boundary rule (B)** — the local transform rule.
5. **Tool transform (T)** — the engine call that makes it executable.
6. **Obligation set (O)** — unresolved residue, never erased.
7. **Workbook analogue (W)** — the analog / physical / sheet form.
8. **IRL citation anchor (A)** — the external real-world reference.

**Arity** of the ribbon for a paper = how many of those 8 slots are filled by a *complete concept-space item* (binary + vector reasoning together, not just local state). A slot is "filled" when an artifact on the D:/ drive fully rehydrates the action map behind that slot. Back-propagation forwards: a D:/ artifact that fills a slot becomes a forward-result feeding that paper.

## What is *not* allowed

- No tool may use a non-`CQE-*` name for its internals.
- No product may use a non-`CMPLX-1T-*` name.
- `lib-forge/` may not import lineage artifacts by their old names without wrapping them in a `CQE-` adapter.
- Lineage (anything from `D:\CQE_CMPLX`, `D:\DockerContainers`, the ForgeFactory session master) is allowed only as **source material**. It is reassembled under the new identity and never referenced as authority.
- "Open obligation" language in old docs is a *checkpoint*, not authority. We re-evaluate proven vs not **only after** all 32 papers are reassembled.

## File-level naming

- `CQE-paper-NN/INTENT.md` — captured intent for paper NN, verbatim from `PAPERS_00_30_COMBINED_BEST_FORM_v0_1.md`.
- `CQE-paper-NN/01-CQE-formal/FORMAL.md` — Block A (Status, Abstract, Thesis, Scope, Definitions, Axioms, Lemmas, Formalism, Proof Tree, Open Obligations, Back-Propagation).
- `CQE-paper-NN/02-CQE-tool/TOOL.md` — Block B (Tool binding, Practical example, Executable run, Receipts).
- `CQE-paper-NN/03-CQE-workbook/WORKBOOK.md` — Block C (Analog sheet, IRL citations).
- `proof-receipts/CQE-paper-NN/...` — receipts from running the tool block.
- `lib-forge/cqe_engine/` — the CQE engine itself: ribbon, arity, hydrate, back-propagate, transport.

## What gets called the engine

`lib-forge/CQE-engine/` contains:

- `ribbon.py` — the 8-slot ribbon type.
- `arity.py` — compute arity of a ribbon from a slot-fill map.
- `hydrate.py` — given a ribbon and a slot-fill map, rehydrate the full action map (binary + vector).
- `backprop.py` — back-propagation: a D:/ artifact fills a slot of a paper and is registered as a forward-result.
- `transport.py` — the CQE transport kernel: `T(P_in) -> P_out` with receipt.
- `registry.py` — registry of papers, their ribbons, and their slot-fill maps.

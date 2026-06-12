# CQE/CMPLX Distribution Plan

This is the master plan for turning the loose CQE/CMPLX source tree
into a set of pip-installable Python packages. It is the *contract*
for the `D:\CQE_CMPLX\cqekernel\`, the `CQECMPLX-Production\lib-forge\`
tree, and the seven forge families.

**TL;DR — three things to do today:**

1. `cd D:\CQE_CMPLX\cqekernel && pip install -e .` — the stdlib kernel is now a package.
2. `cd D:\CQE_CMPLX\CQECMPLX-AirLock\cqe-production-v0.1 && make bootstrap` — installs everything editable.
3. Read `CQECMPLX-AirLock/cqe-production-v0.1/DISTRIBUTION.md` for the full design.

---

## Package map

| PyPI name | Source of truth | Purpose | Runtime deps |
|---|---|---|---|
| `cqe-kernel` | `D:\CQE_CMPLX\cqekernel\` | stdlib-only C-form runtime | **none** |
| `cqe-engine` | `CQECMPLX-Production/lib-forge/cqe_engine/` | ribbon transport, arity, hydrate, backprop | `cqe-shared-memory` |
| `cqe-shared-memory` | `.../cqe_shared_memory/` | JSONL ledger, fermionic/bosonic split | none |
| `cqe-spawner` | `.../CQE_spawner/` | Stream A: formalization | `cqe-shared-memory`, `cqe-engine` |
| `cqe-spawner-patent` | `.../CQE_spawner_patent/` | Stream B: patent / legal / IRL | `cqe-shared-memory`, `cqe-engine` |
| `lattice-forge` | `CMPLX-PartsFactory-main/packages/lattice-forge/` | math substrate, 8-state sweep, M3 idempotent, D4, J3, etc. | none (extras for sympy, fastapi, etc.) |
| `mandleforge` | `CQECMPLX-Production/lib-forge/MandleForge/` | M-set / manifold substrate | none (extras for sympy) |
| `maniforge` | `.../ManiForge/` | color / manifold operations | none (extras for sympy) |
| `chromaforge` | `.../ChromaForge/` | color conservation, MDHG, MMDB, speedlight | none (extras for numpy) |
| `fridgeforge` | `.../FridgeForge/` | lexicon + recipes for forge composition | none |
| `linkforge` | `.../LinkForge/` | link / join / citation primitives | none |
| `pixelforge` | `.../PixelForge/` | frame / ink / projection / surface | none (extras for Pillow) |
| `graphstax` | `.../GraphStax/` | Rule 30, permutation, algebraic stacks | none |
| `cqe-production` (umbrella) | `CQECMPLX-AirLock/cqe-production-v0.1/` | white-room install of everything | depends on all of the above |

## Already-pip-installable today

- **`cqe-kernel`** — `D:\CQE_CMPLX\cqekernel\pyproject.toml` written, `pip install -e .` works, wheel built, `cqe-kernel` CLI registered.
- **`lattice-forge 0.3.0`** — already publishes from `CMPLX-PartsFactory-main/packages/lattice-forge/pyproject.toml`.
- **`cqe-production 0.2.0`** — the umbrella `pyproject.toml` parses; `make bootstrap` wires it all together.

## Scaffolds (copy → publish) ready

The 11 per-forge / per-cqe_* scaffolds live at:
`CQECMPLX-AirLock/cqe-production-v0.1/pyproject-scaffolds/`

To publish any of them, copy the matching scaffold into a fresh
git repo and copy the vendored source from
`CQECMPLX-Production/lib-forge/<Name>/` into the same root. Then
`pip install -e .` from that repo.

```
cqecmplx-forges/
  mandleforge/      <- scaffold  +  CQECMPLX-Production/lib-forge/MandleForge/
  maniforge/        <- scaffold  +  .../ManiForge/
  chromaforge/      <- scaffold  +  .../ChromaForge/
  fridgeforge/      <- scaffold  +  .../FridgeForge/
  linkforge/        <- scaffold  +  .../LinkForge/
  pixelforge/       <- scaffold  +  .../PixelForge/
  graphstax/        <- scaffold  +  .../GraphStax/
```

## Install commands

| Want | Command |
|---|---|
| Just the kernel | `pip install cqe-kernel` |
| Kernel + everything | `pip install cqe-production[all]` |
| Just the math substrate | `pip install lattice-forge[all]` |
| Just one forge | `pip install chromaforge` (etc.) |
| Editable dev install of everything | `make bootstrap` in `cqe-production-v0.1/` |
| Smoke test the install | `python scripts/bootstrap.py` (from `cqe-production-v0.1/`) |

## Where the full design lives

- **`CQECMPLX-AirLock/cqe-production-v0.1/DISTRIBUTION.md`** — the full design doc: package architecture, scaffolding, Makefile, publishing to a private index, verification after install, known follow-ups.
- **`CQECMPLX-AirLock/cqe-production-v0.1/pyproject.toml`** — the umbrella.
- **`CQECMPLX-AirLock/cqe-production-v0.1/Makefile`** — `make bootstrap` / `make install` / `make test` / etc.
- **`CQECMPLX-AirLock/cqe-production-v0.1/scripts/render_forge_scaffolds.py`** — regenerates the 11 scaffolds from a single source of truth.
- **`CQECMPLX-AirLock/cqe-production-v0.1/scripts/bootstrap.py`** — runs the install + smoke-import + kernel unit tests in one command.
- **`D:\CQE_CMPLX\cqekernel\pyproject.toml`** — the stdlib kernel's pyproject.

## Status

| Item | State |
|---|---|
| `cqe-kernel` is pip-installable | **done** (wheel built, `cqe-kernel` CLI works) |
| `lattice-forge` is pip-installable | **done** (in PartsFactory) |
| `cqe-production` umbrella parses | **done** (10 extras, 4 entry points) |
| 11 per-package scaffolds generated | **done** (all parse via tomllib) |
| Per-forge repos published on internal PyPI | **TODO** (scaffold ready) |
| Per-forge repos extracted from `lib-forge/` | **TODO** (currently vendored in white room) |

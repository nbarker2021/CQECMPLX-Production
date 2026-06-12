# CQECMPLX-Production

**Canonical production repo for the CQE/CMPLX tool family.**

This repository is the production body for staged local roots. The frontpage centers on **`cqekernel`** — the stdlib-only C-form runtime — with the full **Forge ring** integrated around it.

---

## Quick Start

```bash
# Install the kernel (stdlib-only, zero external deps)
pip install cqe-kernel

# Install the full Forge ring (optional predictors extra)
pip install cqecmplx-forge          # stdlib-only core
pip install cqecmplx-forge[predictors]   # + numpy/scipy spectral predictors
```

```python
# Kernel entry point
from cqekernel import Kernel, RequestMode
k = Kernel()
res = k.observe("hello world", mode=RequestMode.AUDIT)

# Forge ring (optional, layered on kernel)
from lattice_forge.binary_boundary_adapter import adapt
from ChromaForge import ChromaForgeEngine
from GraphStax import coverage_check, SUPERPERM_N4
```

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                        CQECMPLX-PRODUCTION                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │                    CQEKERNEL (core)                         │  │
│   │  stdlib-only C-form runtime • 64 files • ~150KB             │  │
│   │  core → carrier → ribbon → projection → ledger → verification│  │
│   │  firmware (optional) → adapters → workbook → storage        │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                              │                                      │
│          ┌───────────────────┼───────────────────┐                │
│          ▼                   ▼                   ▼                │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐         │
│   │ LATTICE     │    │ REFORGE     │    │ FORGE       │         │
│   │ FORGE       │    │ RING        │    │ ENGINES     │         │
│   ├─────────────┤    ├─────────────┤    ├─────────────┤         │
│   │ • Rule 30   │    │ • forgefactory          │ • ChromaForge  │
│   │   chart     │    │ • reforge_engine_       │   Event Law,   │
│   │   algebra   │    │   contracts             │   Merkle       │
│   │ • J3(O)/F4  │    │ • reforge_engine_       │   receipts     │
│   │   registration│  │   hardening             │ • GraphStax    │
│   │ • Binary    │    │ • reforge_frameforge    │   bit→C-gluon, │
│   │   Boundary  │    │ • reforge_glyphforge    │   AGRM,        │
│   │   Adapter   │    │ • reforge_kimi_adapter  │   PermForge    │
│   │ • oloid     │    │ • reforge_pixl8forge    │ • PixelForge   │
│   │   carriers  │    │ • reforge_pixleforge    │   adaptive     │
│   │ • ledgers   │    │ • reforge_researchcraft │   resolution   │
│   │ • lattice   │    │ • reforge_wireforge     │   surfaces     │
│   │   code      │    │ • rhenium_engine        │ • FridgeForge  │
│   │   chains    │    │                         │   inventory,   │
│   └─────────────┘    └─────────────┘           │   meal lanes   │
│                                                  │ • LinkForge    │
│                                                  │   external DBs │
│                                                  │ • MandleForge  │
│                                                  │ • ManiForge    │
│                                                  │ • SceneForge   │
│                                                  │   world/intent │
│                                                  └─────────────┘
└─────────────────────────────────────────────────────────────────────┘
```

---

## The Kernel: `cqekernel`

**Location:** `production/packages/cqekernel/`

The kernel is a **64-file, ~150KB Python package** implementing the full CQE/CMPLX spec without `numpy`, `pandas`, `pydantic`, `fastapi`, `sympy`, `networkx`, `lattice_forge`, or any external math library.

### 11 Layers (all stdlib)

| Layer | Path | Responsibility |
|-------|------|----------------|
| Core | `core/` | request, kernel, policy, status, errors |
| Carrier | `carrier/` | binary_boundary, fourbit, lcr, cform, correction |
| Ribbon | `ribbon/` | slot, ribbon, arity, hydrate, transport |
| Projection | `projection/` | observer_frame, light_cone, boundary_aperture, closure, eversion |
| Ledger | `ledger/` | event, receipt, store, snapshot, replay |
| Verification | `verification/` | verifier, falsifier, honesty, socratic |
| Firmware | `firmware/` | abi, registry, manifest (optional, importlib-discovered) |
| Adapters | `adapters/` | text, bytes, json, csv, filesystem, host_packet |
| Workbook | `workbook/` | analog_schema, workbook_engine, token_map |
| Storage | `storage/` | json_store, sqlite_store, paths |
| Tests | `tests/` | 26 unit + 19 integration tests, all stdlib |

### Determinism Guarantees

- Ribbon hash = deterministic function of request (same input → same hash)
- Frame IDs, ribbon IDs, carrier IDs derived from request hashes (not `uuid4()`)
- Slot identity hash covers `(name, source_kind, provenance, status)` only

### CLI

```bash
python -m cqekernel observe input.txt --mode AUDIT
python -m cqekernel verify
python -m cqekernel packet '{"op":"observe","payload":"x","mode":"AUDIT"}'
```

---

## The Forge Ring: `cqecmplx-forge`

**Location:** `production/packages/cqecmplx-forge/`

The installable Forge ring — eight top-level packages mounted under the `cqecmplx` namespace.

### Package Registry

| Package | Role | Key Modules |
|---------|------|-------------|
| `lattice_forge` | Proven substrate: Rule 30 chart algebra, J3(O)/F4 registration, Binary Boundary Adapter, lattice code chains, oloid carriers, ledgers | `rule30`, `core`, `binary_boundary_adapter`, `d12_action`, `voa_lookup`, `forge`, `g2_f4_t5_conjugate`, `rule30_predictor`, `rule30_spectral_predictor`, `algebra/`, `decomposition/`, `empirical/`, `falsify/`, `tools/`, `witness/`, `backwalk/`, `cqe/` |
| `ChromaForge` | Event Law machinery: Merkle receipts, conservation, idempotent cache (`f(f(x))=f(x)`), crystal store | `ChromaForgeEngine`, `CrystalVault`, `receipt` |
| `GraphStax` | Graph identity: bit → C-gluon resolution, AGRM routing, superpermutation supervisor cursor (PermForge) | `coverage_check`, `SUPERPERM_N4`, `PermForge` |
| `PixelForge` | Display/input plane: adaptive-resolution surfaces, stylus/touch ink with pressure+tilt, E8 projection, deterministic frame streams | `RGB=LCR pixel layer`, `T_EMISSION`, `Picture`, `VideoSynth`, `FrameStream`, `paint` |
| `FridgeForge` | Applied engine: inventory lexicon, kid/adult meal lanes with hard constraints, templated shopping lists | `inventory`, `meal_lanes`, `shopping_list` |
| `LinkForge` | External databases as lib items: json/csv/ics linked once, receipted, reused | `JsonLink`, `CsvLink`, `IcsLink` |
| `MandleForge` / `ManiForge` | Forge conventions for Mandelbrot/manifold surfaces | `mandelbrot`, `manifold` |
| `SceneForge` | Harvested from historical donors: worldforge (P5→B_obs→Rrho→B_soft→B_higgs→B_ward→Bridge compose, receipt-trailed), intent (Scene8 Intent-as-Slice stdlib: 240-root E8 lattice walks, UNITY/TERNARY/ATTRACTOR actions), imagedb (real saved pictures indexed + deterministic casting) | `worldforge`, `intent`, `imagedb` |

### ReForge Ring (ForgeFactory v0.3 lineage)

| Module | Purpose |
|--------|---------|
| `forgefactory` | Factory orchestration |
| `reforge_engine_contracts` | Engine contract definitions |
| `reforge_engine_hardening` | Hardening & receipt trail |
| `reforge_frameforge` | Frame operations |
| `reforge_glyphforge` | Glyph encoding/decoding |
| `reforge_kimi_adapter` | KIMI adapter |
| `reforge_pixl8forge` / `reforge_pixleforge` | Pixel forge variants |
| `reforge_researchcraft` | Research workflow engine |
| `reforge_wireforge` | Wire/transport forge |
| `rhenium_engine` | Rhenium/Re/75 identity-aligned engine |

### Quick Verification

```bash
# Kernel verification
python -m cqekernel verify

# Forge verification (10/10 passing)
cqecmplx-verify
```

---

## Source Map: Where Everything Lives

### Production Packages (git-tracked)

```
production/packages/
├── cqekernel/                    # ← FRONTPAGE: the kernel itself
│   ├── core/ carrier/ ribbon/ projection/ ledger/
│   ├── verification/ firmware/ adapters/ workbook/ storage/
│   ├── cli.py, __main__.py, pyproject.toml
│   └── tests/ (45 tests, all stdlib)
│
├── cqecmplx-forge/               # ← FORGE RING: unified namespace
│   └── src/
│       ├── lattice_forge/        # Union: PROOF (54) + PartsFactory (116), 9 diverged adjudicated
│       ├── ChromaForge/
│       ├── GraphStax/
│       ├── PixelForge/
│       ├── FridgeForge/
│       ├── LinkForge/
│       ├── MandleForge/
│       ├── ManiForge/
│       ├── SceneForge/
│       ├── forgefactory/
│       ├── reforge_engine_contracts/
│       ├── reforge_engine_hardening/
│       ├── reforge_frameforge/
│       ├── reforge_glyphforge/
│       ├── reforge_kimi_adapter/
│       ├── reforge_pixl8forge/
│       ├── reforge_pixleforge/
│       ├── reforge_researchcraft/
│       ├── reforge_wireforge/
│       └── rhenium_engine/
```

### Lib-Forge (Production Workspace)

```
production/lib-forge/
├── engines/                      # Forge engine sources
│   ├── ChromaForge/
│   ├── FridgeForge/
│   ├── GraphStax/
│   ├── LinkForge/
│   ├── PixelForge/
│   └── SceneForge/
├── recovered/                    # Recovered papers, MASTER_PDF, workbench
└── CQECMPLX-MetaMaterial-Designer/
```

### CMPLX-Kernel Ring (Sidecar + Companion Kernels)

```
CMPLX-Kernel/
├── kernel/                       # Deployable sidecar runtime
│   ├── boot.py, AI_LOAD_FIRST.md, KERNEL_MANIFEST.json
│   ├── web/, cmplx_kernel/
│   └── modules/MODULE_REGISTRY.json
├── kernel_ring/
│   ├── lib_kernel/               # Reusable libs, rule libs, proofs, lib-forge surfaces
│   ├── lattice_kernel/           # LatticeForge, E8/lattice proof geometry, pulse-node diagnostics
│   └── reforge_kernel/           # ReForge + Forge-family package identity blueprints
└── lib-forge/                    # (mirrors production/lib-forge with build scripts)
```

### AirLock Lineage (Staged Intake)

```
CQECMPLX-AirLock/
├── cqe-production-v0.1/
│   └── lib-forge/
│       ├── MandleForge/
│       ├── ManiForge/
│       └── ...
├── forgefactory-v0.3-lineage-read/
│   └── ForgeFactory_v0_3/
│       ├── docs/ (reforge_engine_hardening_v0_1, reforge_glyphforge_fumu_v0_1, ...)
│       └── src/ (forgefactory, lattice_forge, reforge_*)
└── ...
```

---

## Promotion History (Recent)

| Slice | Date | Note |
|-------|------|------|
| `CQECMPLX-Forge-Package-v0.9.0` | 2026-06-12 | Metamorph: motion INSIDE correction space; morph_video, transport_video; 10/10 verify |
| `CQECMPLX-Forge-Package-v0.8.0` | 2026-06-12 | Genesis: layered rule90+correction INVERSION; request→picture generation; 9/9 verify |
| `CQECMPLX-Forge-Package-v0.7.0` | 2026-06-12 | SceneForge harvested: worldforge, intent, imagedb; PixelForge PNG/BMP; 13.3s live video |
| `CQECMPLX-Forge-Package-v0.6.2` | 2026-06-12 | paint.py: color-as-numbering machine; deterministic BMPs |
| `CQECMPLX-Forge-Package-v0.6.1` | 2026-06-12 | Request-to-video demo + AVI codec; 10.4s live |
| `CQECMPLX-Forge-Package-v0.6.0` | 2026-06-12 | RGB=LCR pixel layer; VideoSynth; 8/8 verify |
| `CQECMPLX-Forge-Package-v0.5.0` | 2026-06-11 | Two-tier storage law; CrystalVault; 7/7 verify |
| `CQECMPLX-Forge-Package-v0.4.0` | 2026-06-11 | 9 diverged adjudicated; predictor fork split; cache-poisoning fix; 6/6 verify |
| `CQECMPLX-Forge-Package` | 2026-06-11 | Unified cqecmplx namespace; lattice_forge union; stdlib-only |
| `CQECMPLX-Worktree-Unification` | 2026-06-11 | WSL worktree reconciliation; engine ring, MASTER_PDF, PaneForge |

---

## Development Workflow

### Working with the Kernel

```bash
# Editable install
cd production/packages/cqekernel
pip install -e .

# Run tests
python -m pytest tests/ -v

# Verify
python -m cqekernel verify
```

### Working with the Forge Ring

```bash
# Editable install
cd production/packages/cqecmplx-forge
pip install -e .

# Run verifier
cqecmplx-verify

# Examples
python examples/request_to_video.py
python examples/live_video.py
```

### Adding a New Forge

1. Create package under `production/packages/cqecmplx-forge/src/<NewForge>/`
2. Follow the engine pattern: `Engine` class + receipt trail + stdlib-only core
3. Add to `pyproject.toml` under `[project.optional-dependencies]`
4. Register in this frontpage's Package Registry table
5. Run `cqecmplx-verify` to confirm integration

---

## Key Principles

1. **Kernel First** — `cqekernel` is the frontpage, zero-dep, stdlib-only foundation
2. **Forge Rings Layer On** — `cqecmplx-forge` packages are optional, importlib-discovered firmware
3. **Identity-Aligned Names** — Rhenium/Re/75 atomic alignment preferred; names emerge from ability semantics
4. **Receipts Over Claims** — Every layer produces verifiable receipts (CQE, lattice_forge, Event Law)
5. **No Blind Copies** — Promotion by explicit slices with manifest, portability review, proof anchors
6. **Stdlib Core** — External deps (`numpy`, `scipy`) only in `[predictors]` extra, never in kernel

---

## Canonical Remote

```text
https://github.com/nbarker2021/CQECMPLX-Production
```

**Current head:** `main`  
**Intake branch:** `intake/production-kernel-map`

---

## QED

The kernel is the anchor. The Forge ring extends it. Every component has a receipt.
Every name carries identity. The frontpage is `cqekernel` — all else orbits it.
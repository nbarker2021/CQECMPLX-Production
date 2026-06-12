# Promotion Slice — PaneForge Workspace Tool (2026-06-12)

## Identity

`paneforge-tool` v0.1.0 — the **PaneForge-Stick** product layer
(`production/products/PaneForge-Stick`) turned into an installable local
workspace tool with a `paneforge` console command.

The product is the Event Law reference implementation:

```text
compute (BBA) -> save (crystal) -> validate -> receipt (2 links) -> reuse free
```

The tool wraps it without modifying the kernel. The kernel remains the single
source of behavior; the tool only resolves the product root, sets the data
boundary (`PANEFORGE_DATA`), and exposes lifecycle commands.

## What Was Promoted

| Path | Role |
|---|---|
| `production/tool-families/PaneForge-Workspace-Tool/pyproject.toml` | pip-installable package, console script `paneforge` |
| `.../src/paneforge_tool/__init__.py` | product-root resolver (env -> vendored -> repo-relative -> known roots) + data-dir boundary |
| `.../src/paneforge_tool/cli.py` | `where` / `serve` / `demo` / `info` / `test` subcommands |
| `.../README.md` | install + use + resolution contract |

The repo copy ships **without** a vendored product: when installed from this
location it resolves `production/products/PaneForge-Stick` repo-relatively.
The local workspace install at `D:\CQE_CMPLX\workspace-tools\paneforge`
carries a vendored product copy for position independence (USB-stick layout).

## Verification (run 2026-06-12, local workspace install)

| Check | Result |
|---|---|
| `pip install -e .` | pass — `paneforge-tool 0.1.0` installed, CLI registered |
| `paneforge where` | pass — product + 6-forge ring resolved (ChromaForge, FridgeForge, GraphStax, LinkForge, PixelForge, lattice_forge) |
| `paneforge serve` + `/api/health` | pass — `ok: true`, gluon wired, chain at genesis |
| Event Law live check | pass — `event.add` minted receipt with exactly 2 links: `link[0]` = crystal id, `link[1]` = prev receipt hash; `valid:True`; `delta_phi = -0.0300757...` (= -ln(phi)/16) |
| SpeedLight reuse | pass — identical second event did not mint a second receipt (chain stayed length 1) |
| `paneforge test` (full product suite) | pass — **83 passed, 0 failed** (PixelForge units + kernel HTTP integration + persistence/restart) |
| Repo-relative resolution from this directory | pass — resolves `production/products/PaneForge-Stick` |

## Data Boundary

Receipts/crystals never enter the package or the repo: `PANEFORGE_DATA`
(default `~/.paneforge`) is set by every CLI subcommand before the kernel
starts.

## Open Obligations

- Publish `paneforge-tool` to the internal package index alongside the
  per-forge scaffolds in `DISTRIBUTION_PLAN.md`.
- Add a `paneforge pack` command that builds the USB-stick image (product +
  tool, position independent).
- Wire `paneforge info` receipts output into the proof-receipt schema used by
  `production/proof-receipts/`.
- Repeat this promotion pattern for the remaining built product layers
  (Product Fourpack: entropy and sentinel already have pyproject + src).

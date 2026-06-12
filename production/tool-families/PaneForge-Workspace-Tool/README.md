# paneforge-tool

The **PaneForge-Stick** product — Event Law calendar kernel + PWA + vendored
lib-forge ring (lattice_forge BBA chain, ChromaForge, PixelForge, FridgeForge,
LinkForge, GraphStax) — packaged as an installable local workspace tool.

The kernel is the Event Law reference implementation:

```text
compute (BBA) -> save (crystal) -> validate -> receipt (2 links) -> reuse free
```

## Install

```bash
cd D:\CQE_CMPLX\workspace-tools\paneforge
pip install -e .
```

Stdlib-only at runtime — the kernel and every vendored forge import nothing
outside the Python standard library.

## Use

| Command | What it does |
|---|---|
| `paneforge where` | show resolved product root, forge ring, data dir |
| `paneforge serve [--port 8770]` | run the kernel in the foreground |
| `paneforge demo` | start the kernel, wait for health, open the calendar PWA |
| `paneforge info` | query a running kernel: health, Event Law status, receipt chain head |
| `paneforge test` | run the product test suite (PixelForge units + kernel HTTP integration) |

Receipts and crystals are written to `PANEFORGE_DATA` (default `~/.paneforge`),
never into the package.

## Product resolution

1. `PANEFORGE_PRODUCT` env var
2. vendored copy inside the package (`src/paneforge_tool/_product/`)
3. repo-relative `production/products/PaneForge-Stick` (when the tool lives in
   `production/tool-families/` of CQECMPLX-Production)
4. known workspace roots

Source of truth for the product:
`CQECMPLX-Production/production/products/PaneForge-Stick` (git: nbarker2021/CQECMPLX-Production).

# Promotion Slice: CMPLXUNI Docs and Configs

Date: 2026-06-11

Manifest:
`tracking/promotion-manifests/CQECMPLX-CMPLXUNI-Swarm-Frontend.manifest.json`

## Scope

This slice promotes CMPLXUNI documentation, architecture notes, swarm/chat
interface docs, MCP config templates, and package metadata. It establishes the
front-end/orchestration surface without promoting the full app source or any
runtime payloads.

## Included Source Root

- `D:\CQE_CMPLX\g\CMPLXUNI`

## Included Content

- CMPLXUNI root README, agent guide, navigation, contribution, disclaimer, and
  task notes;
- Next.js architecture and chat interface documentation;
- expanded swarm and ThinkTank/CQE tool documentation;
- MCP configuration guides and template JSON files;
- root Python package metadata;
- `cmplx-nextjs` README and package metadata;
- `the-library` README, Dockerfile, and Compose file.

## Normalization Applied

Local absolute machine paths in MCP config JSON files were replaced with the
portable `${CMPLXUNI_ROOT}` placeholder in the promoted copy.

## Exclusions

- `node_modules`, `.next`, build outputs, runtime databases, caches, logs,
  archives, generated bundles, and virtual environments;
- local secrets and `.env` files;
- full UI/API source pending build and route review.

## Production Interpretation

This is the first UI/orchestration slice for the kernel-bound package. Future
passes should map UI controls to kernel options, especially training mode and
Hidden Guess Result behavior for diagnostics.

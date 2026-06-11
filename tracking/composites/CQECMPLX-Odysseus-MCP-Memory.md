# CQECMPLX-Odysseus-MCP-Memory

Status: `needs-portability-review`

Route: `production/adapters` + `production/memory`

## Composite Identity

`CQECMPLX-Odysseus-MCP-Memory` is the adapter and memory part of the Odysseus
surface. It includes MCP servers, memory routes, vector memory, Docker compose
forms, integration docs, and a broad test suite.

## Production Boundary

This is not a wholesale app import. The production shape should be split into:

- MCP adapter layer;
- memory persistence layer;
- Docker boundary layer;
- tests that prove isolation, ownership, and adapter behavior;
- optional UI/application material only after portability review.

## Risks

- `.env` and secret-bearing configuration exists locally.
- `data/` contains databases and runtime state.
- docs include large media assets.
- the test surface is large and should be filtered by adapter/memory relevance.

## Promotion Rule

Promote reviewed adapter/memory code and relevant tests first. Runtime data,
secrets, media, and app-wide material stay out until a separate publication
manifest exists.

## Source Bindings

- `tracking/source-bindings/CQECMPLX-Odysseus-MCP-Memory.json`
- `tracking/promotion-manifests/CQECMPLX-Odysseus-MCP-Memory.manifest.json`

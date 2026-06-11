# Kernel Bound Package Evaluation

## Added In This Pass

- Local operator web console.
- Stdlib HTTP API for sidecar processing.
- Dynamic module registry.
- SQLite event and module state store.
- Kernel ring endpoint for lib, lattice, and ReForge companion kernels.
- Bearer-token auth hook, CORS policy hook, request size limit, and rate limit.
- Proof browser, repo-form explorer, and package manifest inspector.
- Docker tool root adapter for `D:\DockerContainers`.
- Kernel-only Docker-in-Docker Compose deployment.
- Package/proof docs for the operator and dynamic data layer.

## Still Needed

### Hosting Boundary

The current server is local-first and now has authentication, CORS, request
size, and rate-limit hooks. Before remote web hosting, add:

- TLS/reverse-proxy deployment notes;
- remote state backup/export receipts.

### Database Boundary

SQLite is enough for local and file-fed operation. Larger deployments need
adapter modules for:

- Postgres-compatible stores;
- object storage for payload bodies;
- vector/index stores;
- append-only proof ledgers;
- snapshot export/import through the Binary Boundary Adapter.

### Module Boundary

The registry is ready for preinstalled and staged tools. Next modules should
enter through:

```text
module identity -> registry entry -> adapter proof -> UI/API surface -> receipt
```

Useful next built-ins:

- lattice/MORSR readiness viewer;
- lib promotion queue;
- hidden-guess-result training receipt browser;
- deployment proof generator.

Already installed as built-ins:

- proof browser;
- package boundary inspector;
- repo-form explorer;
- Docker tool root adapter;
- operator security guardrails.
- kernel DinD deployment scaffold.

### Production Boundary

Do not make the runtime heavy. Anything that requires external services should
be a module with a declared adapter, not a hard dependency of `boot.py`.

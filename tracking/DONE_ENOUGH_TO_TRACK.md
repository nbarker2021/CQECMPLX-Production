# Done Enough To Track

This file defines the first production-tracking threshold for
`CQECMPLX-Production`.

The goal is not to choose the best duplicate. If multiple sources say the same
thing, the production path is to combine them into a composite form and track
that composite as a new production candidate.

## Definition

A thing is done enough to track when it has:

- a stable name or repeated identity across roots;
- at least one local evidence source;
- enough file/profile/proof/deployment evidence to follow it without guessing;
- an obvious production family or composite family;
- known missing work recorded separately.

This does not mean the thing is ready to publish as final code. It means the
thing is mature enough to receive a tracking row, a composite route, and later
promotion gates.

## Evidence Types

Trackable evidence includes:

- deployment proofs;
- repo zip content profiles;
- kernel manifests;
- package manifests;
- Docker/Compose files;
- API/MCP/server surfaces;
- paper/proof/formalization paths;
- database payload candidates;
- sidecar receipts;
- lib/kernel ring forms;
- repeated named-thing candidates across archives.

## Status Terms

| Status | Meaning |
|---|---|
| `trackable-composite` | multiple sources describe the same identity family; build a composite candidate |
| `trackable-slice` | one source has a clear production-shaped slice |
| `trackable-payload` | binary/database/archive payload is identified but not expanded |
| `trackable-proof` | proof/paper/formalization evidence exists and can bind claims |
| `not-yet-trackable` | identity or evidence is too thin |

## Current Source Facts

The repo zip accounting database under:

```text
D:\CQE_CMPLX\Claude-Codex-Memory\Codex work\CX-Repo-Literal-Accounting
```

reports:

```text
12 top-level repo zips content-profile-complete
66,582 archive entries
62,691 profiled file bodies
2,994,867,153 bytes streamed
29 queued payload candidates
```

Remaining work:

- nested archive expansion;
- SQLite/database payload introspection;
- full text indexing beyond lightweight profiles;
- dedupe/consolidation;
- paper-claim binding to Production/AirLock/Kernel roots.

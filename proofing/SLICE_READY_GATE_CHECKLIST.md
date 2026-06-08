# Slice-Ready Gate Checklist

This checklist applies to every deployment proof marked `slice-ready`.

Current slice-ready roots:

- `CMPLX-Kernel`
- `CMPLX-1T`
- `CMPLX-Monorepo`
- `CMPLX`

## Gate 1: Identity

- Root name is stable.
- Production role is stated.
- Destination path is named.
- Source remote/local path is recorded.

## Gate 2: Manifest

- Exact files are listed in a promotion manifest.
- Explicit exclusions are listed.
- Large artifacts are routed to release/LFS/corpus storage, not normal git.

## Gate 3: Credential Safety

- `.env.example` files are templates only.
- No real tokens, passwords, keys, or private keys are promoted.
- Default credentials are marked as local/demo only.
- Production deployment requires environment injection or secret manager.

## Gate 4: Source Of Truth

- Vendored/nested sibling repos are classified.
- Duplicate monolith/generated files are not promoted without owner decision.
- Generated files identify their generator or remain airlocked.

## Gate 5: Adapter Boundary

- Binary Boundary Adapter is used for file/data ingress when applicable.
- Universal Adapter is used for host/tool handshakes.
- MCP/API/network surfaces declare ports, auth, and expected payloads.

## Gate 6: Hidden Guess Result

- Quiet/default mode is preserved for non-local agents.
- `training_mode=true` enables Hidden Guess Result.
- Local full-program mode may require guess diagnostics.
- Diagnostic proof docs identify whether guess mode is optional or required.

## Gate 7: Test And Verification

- Focused tests are identified before copy.
- Test limitations are documented.
- If tests cannot run, blocker is recorded as a proof note.

## Gate 8: Promotion Receipt

Every promotion commit should include:

- source root;
- source commit;
- selected files;
- exclusions;
- proof doc link;
- promotion manifest link;
- verification performed.


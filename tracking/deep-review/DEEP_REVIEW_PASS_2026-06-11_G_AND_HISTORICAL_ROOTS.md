# Deep Review Pass: g and Historical Roots

Date: 2026-06-11

## Reason

The production review cannot rely on cautious publish-only scanning. Several
roots contain finished or near-finished systems that are not obvious until the
repo is reviewed iteratively by name density, deployment markers, docs, tests,
and cross-family concepts.

## Roots Counted

| Root | Non-cache files | Structural markers | Markdown | Python | JSON | YAML |
|---|---:|---:|---:|---:|---:|---:|
| `D:\CQE_CMPLX\CMPLX-PartsFactory-main` | 1472 | 58 | 338 | 940 | 50 | 33 |
| `D:\CQE_CMPLX\CMPLX-R30` | 7 | 0 | 6 | 1 | 0 | 0 |
| `D:\CQE_CMPLX\CMPLX-R30-main` | 311 | 11 | 85 | 159 | 37 | 0 |
| `D:\CQE_CMPLX\CQECMPLX_project` | 10 | 1 | 0 | 3 | 0 | 0 |
| `D:\CQE_CMPLX\CQECMPLX-AirLock` | 261 | 5 | 55 | 160 | 7 | 0 |
| `D:\CQE_CMPLX\CQECMPLX-ProofValidatedSuite` | 278 | 15 | 99 | 41 | 64 | 5 |
| `D:\CQE_CMPLX\cqekernel` | 79 | 2 | 1 | 66 | 1 | 0 |
| `D:\CQE_CMPLX\historical_pastworks` | 760 | 25 | 278 | 98 | 85 | 6 |
| `D:\CQE_CMPLX\odysseus` | 1033 | 12 | 17 | 763 | 6 | 13 |
| `D:\CQE_CMPLX\_analog_workbench` | 34 | 2 | 10 | 10 | 6 | 0 |
| `D:\CQE_CMPLX\g` | 62700 | 1017 | 2840 | 42676 | 10139 | 352 |

Excluded from counts: `.git`, `node_modules`, virtual environments,
`__pycache__`, and `.pytest_cache`.

## Newly Elevated Findings

| Candidate | Evidence found | Production implication |
|---|---|---|
| `CQECMPLX-DevKit-MCPOS-MORSR-Runtime` | `g\CMPLXDevKit\...\CMPLXLOCALMCP\mcp_os` has an MCP server/client, 33 exposed tools, 37 CMPLX registry tools, handle-based heavy data, validation framework, AGRM/MDHG subsystem, and `l3_morsr_optimize`. | This is not just DevKit support. It is a sidecar/tool-port runtime candidate and should be tracked above generic MCP tooling. |
| `CQECMPLX-CMPLXUNI-Swarm-Frontend` | `g\CMPLXUNI` documents E8/Leech, unified families, MMDB, ThinkTank, MCP, agent hub, CLI, and a Next.js chat interface. | This is a front-end and enterprise orchestration candidate for the kernel-bound package. |
| `CQECMPLX-Product-Fourpack` | `historical_pastworks\product_authentica`, `product_converge`, `product_entropy`, and `product_sentinel` each show product-shaped deployment evidence. `product_entropy` has FastAPI, Docker, Python SDK, TypeScript SDK, verification, and tests. | These should be treated as deployable product composites, not old scraps. Claims need proof binding before public publish language is finalized. |
| `CQECMPLX-TMN1-Conservation-Fullstack` | `g\CMPLX-TMN1` repeatedly names MORSR pulses, E8 transforms, conservation checks, agent identity, channels, and Docker roles. | This should be a sibling of the TMN role family, with fullstack operations tracked separately from role taxonomy. |
| `CQECMPLX-R30-Formal-Proof-Bridge` | `CMPLX-R30-main` includes verification scripts and a CQE Rule 30 solver path; historical harness docs include Rule 30, Barker Market Engine, multi-tool ablation, and lattice_forge. | R30 should not stay only under paper/proof buckets; it is a proof-to-tool bridge candidate. |

## Immediate Tracking Decision

The next first-class record should be
`CQECMPLX-DevKit-MCPOS-MORSR-Runtime`, because it directly supplies a portable
MCP sidecar/tool runtime shape that overlaps the kernel mission, MORSR, CQE,
Universal Adapter Programs, and Hidden Guess Result validation needs.

## Review Rule Added

Every deep-review pass should record:

- roots scanned;
- count summary;
- newly elevated candidates;
- why each candidate is production-relevant;
- whether it should become a source binding, manifest, composite, or payload
  ledger entry next.

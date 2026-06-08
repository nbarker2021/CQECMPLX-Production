# Deployment Proof Index

This is the proofing spine for the CQE/CMPLX production family.

Purpose:

```text
deployment root -> identity -> deployment surface -> proof receipts -> promotion decision
```

The production repo is not a dumping ground. It is the proof-backed assembly
body. Every massive deployment, repo, archive, airlock intake, and kernel
runtime gets a proof document before promotion.

## Canonical Production Repo

```text
https://github.com/nbarker2021/CQECMPLX-Production
```

## Proof States

| State | Meaning |
|---|---|
| `raw` | cloned or discovered, not reviewed |
| `airlock` | quarantined for review or source-of-truth uncertainty |
| `staged` | reviewed but not production-shaped |
| `slice-ready` | exact promotion slice identified |
| `production-shaped` | manifest, receipt, proof, adapter, and risk gates satisfied |
| `production` | accepted into canonical production tree |

## Global Gates

Every deployment proof must answer:

- What is this root's identity?
- What deployment surfaces does it expose?
- What proof/receipt artifacts exist?
- What is reusable lib behavior versus product/source/corpus material?
- What adapter or boundary does it require?
- Does it use Hidden Guess Result only when `training_mode` is enabled?
- What must be excluded from production?
- What is the first safe promotion slice?

## Deployment Proofs

| Root | Proof Doc | State |
|---|---|---|
| `CQECMPLX-Production` | `deployments/CQECMPLX-Production_DEPLOYMENT_PROOF.md` | `production-shaped` |
| `CMPLX-Kernel` | `deployments/CMPLX-Kernel_DEPLOYMENT_PROOF.md` | `slice-ready` |
| `CMPLX Operator Web` | `deployments/CMPLX-Operator-Web_DEPLOYMENT_PROOF.md` | `slice-ready` |
| `Lib Kernel` | `deployments/Lib-Kernel_DEPLOYMENT_PROOF.md` | `slice-ready` |
| `Lattice Kernel` | `deployments/Lattice-Kernel_DEPLOYMENT_PROOF.md` | `slice-ready` |
| `ReForge Kernel` | `deployments/ReForge-Kernel_DEPLOYMENT_PROOF.md` | `slice-ready` |
| `CQECMPLX-AirLock` | `deployments/CQECMPLX-AirLock_DEPLOYMENT_PROOF.md` | `airlock` |
| `CQE_CMPLX` | `deployments/CQE_CMPLX_WORKSPACE_PROOF.md` | `staged` |
| `CMPLX-1T` | `deployments/CMPLX-1T_DEPLOYMENT_PROOF.md` | `slice-ready` |
| `CMPLX-Monorepo` | `deployments/CMPLX-Monorepo_DEPLOYMENT_PROOF.md` | `slice-ready` |
| `CMPLX` | `deployments/CMPLX_DEPLOYMENT_PROOF.md` | `slice-ready` |
| `CMPLXUNI` | `deployments/CMPLXUNI_DEPLOYMENT_PROOF.md` | `cloned-pending-review` |
| `CMPLXMCP` | `deployments/CMPLXMCP_DEPLOYMENT_PROOF.md` | `cloned-pending-review` |
| `CMPLXDevKit` | `deployments/CMPLXDevKit_DEPLOYMENT_PROOF.md` | `cloned-pending-review` |
| `CMPLX-Formalization` | `deployments/CMPLX-Formalization_DEPLOYMENT_PROOF.md` | `cloned-pending-review` |
| `CMPLX-TMN1` | `deployments/CMPLX-TMN1_DEPLOYMENT_PROOF.md` | `cloned-pending-review` |
| `CMPLX-TMN-main` | `deployments/CMPLX-TMN-main_DEPLOYMENT_PROOF.md` | `cloned-pending-review` |
| `CMPLX-Manny` | `deployments/CMPLX-Manny_DEPLOYMENT_PROOF.md` | `cloned-pending-review` |
| `CMPLX-PartsFactory` | `deployments/CMPLX-PartsFactory_DEPLOYMENT_PROOF.md` | `cloned-pending-review` |
| `CMPLX-R30` | `deployments/CMPLX-R30_DEPLOYMENT_PROOF.md` | `cloned-pending-review` |
| `scout-demo-service` | `deployments/scout-demo-service_DEPLOYMENT_PROOF.md` | `cloned-pending-review` |

## Next Required Work

1. Clone and review `CMPLXUNI`.
2. Convert `CMPLXUNI` review into a deployment proof.
3. Continue repo-by-repo until all public/private roots have proof documents.
4. Promote only exact slices named in promotion manifests.

# Cloned Roots

Short-path clone lane:

```text
D:\g
```

Reason:

`CMPLX-1T` proved that normal longer Windows clone paths can fail on deep
legacy/corpus paths. All review clones use `D:\g` with `core.longpaths=true`.

## Current Clones

| Repo | Local Path | Review Branch | State |
|---|---|---|---|
| `CQECMPLX-Production` | `D:\CQE_CMPLX\git-hosted-roots\CQECMPLX-Production` | `intake/production-kernel-map` | production anchor |
| `CMPLX-1T` | `D:\g\CMPLX-1T` | `intake/review-for-cqecmplx-production` | reviewed |
| `CMPLX-Monorepo` | `D:\g\CMPLX-Monorepo` | `intake/review-for-cqecmplx-production` | reviewed |
| `CMPLX` | `D:\g\CMPLX` | `intake/review-for-cqecmplx-production` | reviewed |
| `CMPLXUNI` | `D:\g\CMPLXUNI` | `intake/review-for-cqecmplx-production` | cloned, pending review |
| `CMPLXMCP` | `D:\g\CMPLXMCP` | `intake/review-for-cqecmplx-production` | cloned, pending review |
| `CMPLXDevKit` | `D:\g\CMPLXDevKit` | `intake/review-for-cqecmplx-production` | cloned, pending review |
| `scout-demo-service` | `D:\g\scout-demo-service` | `intake/review-for-cqecmplx-production` | cloned, pending review |
| `CMPLX-Formalization` | `D:\g\CMPLX-Formalization` | `intake/review-for-cqecmplx-production` | cloned, pending review |
| `CMPLX-TMN1` | `D:\g\CMPLX-TMN1` | `intake/review-for-cqecmplx-production` | cloned, pending review |
| `CMPLX-TMN-main` | `D:\g\CMPLX-TMN-main` | `intake/review-for-cqecmplx-production` | cloned, pending review |
| `CMPLX-Manny` | `D:\g\CMPLX-Manny` | `intake/review-for-cqecmplx-production` | cloned, pending review |
| `CMPLX-PartsFactory` | `D:\g\CMPLX-PartsFactory` | `intake/review-for-cqecmplx-production` | cloned, pending review |
| `CMPLX-R30` | `D:\g\CMPLX-R30` | `intake/review-for-cqecmplx-production` | cloned, pending review |

## Explicit Skip

Any repo named `docker-scout` is excluded from this intake lane.

Current check:

```text
D:\g contains no docker-scout clone.
```

Note: `scout-demo-service` was cloned because its name does not match the
explicit `docker-scout` exclusion.

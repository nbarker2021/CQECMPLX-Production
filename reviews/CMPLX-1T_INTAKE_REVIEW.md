# CMPLX-1T Intake Review

Source repo:

```text
https://github.com/nbarker2021/CMPLX-1T
```

Local clone:

```text
D:\g\CMPLX-1T
```

Review branch created in source clone:

```text
intake/review-for-cqecmplx-production
```

## Clone Result

Initial clone under `D:\CQE_CMPLX\git-hosted-roots\CMPLX-1T` failed checkout
because Windows filename limits were exceeded by deep legacy paths under
`docs/3_staged/family_exemplar_starters`.

Successful clone used a short path and Git long paths:

```text
D:\g\CMPLX-1T
core.longpaths=true
```

This is a production finding. Any future production checkout or CI lane that
uses this repo must either shorten paths, enable long paths, or restructure
deep staged material.

## Repository State

- Current branch at intake: `master`
- Review branch created: `intake/review-for-cqecmplx-production`
- Head commit observed: `01faad8a docs: Add Phase 2 10-Layer Architecture Definition`
- Working tree after branch creation: clean

## Inventory

- Files: `38,709`
- Directories: `2,781`
- Size including `.git`: about `1.56 GB`
- Dominant extensions:
  - `.py`: `20,775`
  - `.json`: `9,948`
  - `.md`: `1,767`
  - `.rst`: `1,120`
  - no extension: `967`

Largest notable files:

- `.git/objects/pack/...pack`: `224,700,073` bytes
- `docs/directory_manifest.csv`: `64,263,137` bytes
- `docker/unified/cqe_unified_family/unified_cqe1.py`: `53,970,313` bytes
- `docs/directory_manifest_UPDATED.csv`: `34,883,946` bytes
- `docker/unified/cqe_models/models.py`: `30,800,221` bytes
- `Wolfram study/CMPLX-Alpha-Housing.tar.gz`: `30,363,871` bytes
- `docs/1_intake/inventory_raw.txt`: `28,898,630` bytes
- `data/cmplx_training.db`: `28,377,088` bytes

Top-level weight:

- `docs`: `29,199` files, about `969 MB`
- `docker`: `8,998` files, about `289 MB`
- `src`: `59` files, about `730 KB`
- `SHOWROOM`: `59` files, about `3.2 MB`

## Identity Read

`CMPLX-1T` presents itself as the flagship showroom/display floor for the CMPLX
ecosystem. It explicitly says it is not daily development code and not a peer
review/prize claim surface.

Production interpretation:

- It is an identity and showcase root.
- It contains valuable navigation, architecture, Docker, source, and showroom
  materials.
- It also contains large staged/legacy/corpus material that must not be promoted
  wholesale into `CQECMPLX-Production`.

## Production-Candidate Slices

Promote after focused review:

- `README.md`, `NAVIGATION.md`, `AGENTS.md`, `INDEX-V5.md`, `QUICKSTART-V5.md`
- `ARCHITECTURE-V5.md`
- `SHOWROOM/`
- `src/` core engines and controller/decomposer/agent modules
- `scripts/` automation scripts after safety review
- `docker-compose.master.yml`, `docker-compose.task-template.yml`, Docker docs
- `reports/`, `security-reports/`, and selected `plans/`
- `repos/cmplx-unified` as a cross-repo reference, not as nested source of truth

## Staged Or Airlock-Only Slices

Keep indexed and gated:

- `docs/3_staged/**`
- deep `family_exemplar_starters/**`
- generated directory manifests and tree dumps
- `data/*.db`
- bundled archives such as tarballs/zip-like release payloads
- giant generated files under `docker/unified/**`
- any embedded copied third-party/library corpus

## Risks Before Promotion

1. Deep paths break normal Windows checkouts unless long paths and/or short clone
   paths are used.
2. Default passwords and placeholder credentials appear in Docker/docs examples.
   These should be parameterized or quarantined before production use.
3. The repo contains generated mega-files and bundled corpus/archive material.
   Those should be moved to release assets, LFS, or indexed corpus storage rather
   than normal git promotion.
4. `docs/README_DO_NOT_EDIT_HERE.md` indicates some docs are generated/staged;
   production edits need to respect source-of-truth boundaries.
5. Test execution was not attempted during intake because the dependency and
   Docker surface is broad; this review is structural only.

## Production Decision

Do not merge `CMPLX-1T` wholesale.

Use it as:

- showroom identity source;
- architecture/navigation source;
- source-code candidate pool;
- corpus/staged archive index.

Promote by explicit slices into `CQECMPLX-Production`, each with manifest,
portability review, and receipt.

## Next Actions

1. Build a `CMPLX-1T` promotion manifest listing exact files for the first slice.
2. Start with docs/navigation/showroom/runtime contracts, not deep staged corpus.
3. Add a long-path warning to production contributor docs.
4. Review default credentials before any Docker material is promoted.


# Promotion Slice: MetaMaterial Designer Source Package

Date: 2026-06-11

Manifest:
`tracking/promotion-manifests/CQECMPLX-MetaMaterial-Designer.manifest.json`

## Scope

This slice promotes the portable source/package surface for MetaMaterial
Designer. It includes package metadata, Python source, tests, Docker metadata,
configuration, and the package paper.

## Included Source Root

- `D:\CQE_CMPLX\CMPLX-Kernel\kernel\lib-forge\meta_material_system`

This active source root is already listed in the source binding. The manifest's
older `CQECMPLX-Production\lib-forge` path is treated as a stale mirrored path,
not as the only valid body source.

## Included Content

- Python package/source files;
- `pyproject.toml` and `requirements.txt`;
- `README.md` and `META_MATERIAL_DESIGNER_PAPER.md`;
- `config.yaml`;
- Dockerfile and Compose metadata;
- package tests.

## Exclusions

- generated JSON reports and test outputs;
- generated HTML visualization outputs;
- pickle/cache payloads, bytecode, virtual environments, and pytest caches.

## Verification

- all promoted Python files parsed successfully with Python `ast.parse`;
- no generated JSON/HTML/PKL files were promoted;
- no embedded credential values were found during targeted scan.

## Production Interpretation

This is now a production-trackable lib-forge package slice. Generated reports
and visualization bodies remain deferred until a publication or payload manifest
admits them.

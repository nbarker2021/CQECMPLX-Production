# Promotion Slice: Repo Forms Index

Date: 2026-06-11

Source binding:

```text
tracking/source-bindings/CQECMPLX-Repo-Forms-Accounting.json
```

Promotion manifest:

```text
tracking/promotion-manifests/CQECMPLX-Repo-Forms-Accounting.manifest.json
```

## Included

- `production/workspace-corpus-index/repo_forms/README.md`
- `production/workspace-corpus-index/repo_forms/REPO_FORM_INDEX.json`
- per-repo `FORM.md`
- per-repo `FORM.json`
- per-repo `archive_exclusions.txt` where present

## Counts

- Repo form files: 33
- Approximate bytes: 162251

## Deferred

- `file_index.curated.txt`
- literal accounting SQLite database
- raw repo zips
- nested archives
- database payloads

## Reason

This slice makes the repo accounting visible in production without importing
large generated indexes or raw archives.

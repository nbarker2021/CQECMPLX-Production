# Curated Repo Forms

The kernel now carries curated repo forms instead of repo zip/archive bodies.

Location:

```text
D:\CMPLX-Kernel\kernel\repo_forms
```

Policy:

- Include repo identity, remote, local clone path, review branch, head commit,
  top directories, key docs, curated file indexes, and archive-exclusion
  receipts.
- Exclude `.zip`, `.tar`, `.tar.gz`, `.gz`, `.7z`, `.rar`, database files,
  SQLite files, and git pack payloads.
- Treat archive/database payloads as corpus or release assets, not kernel
  runtime content.

Purpose:

```text
repo clone -> curated form -> proof doc -> promotion manifest -> production slice
```

This keeps the kernel useful to AI agents that accept files without forcing them
to ingest massive deployment archives.


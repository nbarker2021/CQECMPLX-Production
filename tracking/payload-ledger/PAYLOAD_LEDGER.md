# Payload Ledger

Created: 2026-06-11

This ledger records binary and nested payload candidates found during literal
repo accounting. It does not promote the payload bodies.

## Policy

- Record exact archive and entry paths first.
- Do not dedupe during literal accounting.
- Do not commit database, zip, tar, tgz, pack, or nested archive bodies through
  this ledger.
- Promote payload bodies only after introspection, expansion, and artifact policy
  are complete.

## Payload Families

| Family | Entries | Action |
|---|---:|---|
| `CMPLX-1T databases` | 3 | inspect schemas later |
| `CMPLX-1T nested archives` | 12 | expand only in payload pass |
| `CMPLX-1T git pack` | 1 | keep metadata only unless lineage requires |
| `CMPLX/CMPLXUNI MMDB` | 4 | inspect schemas later |
| `E8 databases` | 3 | inspect schemas later |
| `Vector stores` | 3 | inspect schemas later |
| `Manny memory/instruction DBs` | 2 | inspect schemas later |
| `PartsFactory morphism ledger` | 1 | inspect as LatticeForge payload |

## Source

Source accounting file:

```text
D:\CQE_CMPLX\Claude-Codex-Memory\Codex work\CX-Repo-Literal-Accounting\CX_nested_archive_and_database_entries.csv
```

Machine-readable ledger:

```text
tracking/payload-ledger/PAYLOAD_LEDGER.json
```

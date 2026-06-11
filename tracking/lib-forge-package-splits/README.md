# Lib-Forge Package Splits

This directory splits `CQECMPLX-LibForge-Lattice-ReForge-Ring` into production
package families.

The rule is simple: `lib-forge` is an umbrella, not a single package. Each
family needs its own source boundary, generated-artifact boundary, adapter
boundary, and proof/receipt route before code is promoted.

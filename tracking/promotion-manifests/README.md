# Promotion Manifests

Promotion manifests describe exact production slices before any source body is
copied into this repository.

Each manifest answers:

- what identity is being promoted;
- which source paths are allowed;
- which destination route receives the slice;
- which files are excluded;
- which gates must pass before code or payload movement.

These manifests are intentionally stricter than the population queue. The queue
tracks what can populate production. The manifests define how each slice may
enter production.

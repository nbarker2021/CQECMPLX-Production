# Lattice Kernel Handshake

Main kernel calls this ring by identity, not by raw path crawling. The ring returns a form, a proof route, and adapter requirements. Any file body transfer is a separate Binary Boundary Adapter event.

Handshake order: identity request -> CQE match -> form lookup -> adapter decision -> optional hidden guess result ablation -> proof artifact update.

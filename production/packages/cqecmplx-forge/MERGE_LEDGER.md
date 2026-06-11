# MERGE_LEDGER — lattice_forge union (v0.2.0)

Branches: PROOF (submission line, 54 modules) + PartsFactory v0.3 (service line, 116 files).
Rule: disjoint modules = pure union. Diverged shared modules = PROOF kept as primary
(stdlib-clean import chain, submission-proven); PartsFactory variant preserved at
lattice_forge/variants_partsfactory/<name>.py for adjudication. Nothing dropped.

- union dir from PartsFactory: algebra/
- union dir from PartsFactory: backwalk/
- union dir from PartsFactory: cmplx/
- DIVERGED core.py: PROOF kept; PartsFactory variant -> variants_partsfactory/core.py
- union dir from PartsFactory: cqe/
- DIVERGED d12_action.py: PROOF kept; PartsFactory variant -> variants_partsfactory/d12_action.py
- union dir from PartsFactory: decomposition/
- union dir from PartsFactory: empirical/
- union dir from PartsFactory: falsify/
- DIVERGED forge.py: PROOF kept; PartsFactory variant -> variants_partsfactory/forge.py
- DIVERGED g2_f4_t5_conjugate.py: PROOF kept; PartsFactory variant -> variants_partsfactory/g2_f4_t5_conjugate.py
- DIVERGED rule30.py: PROOF kept; PartsFactory variant -> variants_partsfactory/rule30.py
- DIVERGED rule30_block_extractor.py: PROOF kept; PartsFactory variant -> variants_partsfactory/rule30_block_extractor.py
- DIVERGED rule30_predictor.py: PROOF kept; PartsFactory variant -> variants_partsfactory/rule30_predictor.py
- union dir from PartsFactory: tools/
- DIVERGED voa_lookup.py: PROOF kept; PartsFactory variant -> variants_partsfactory/voa_lookup.py
- union dir from PartsFactory: witness/
- DIVERGED __init__.py: PROOF kept; PartsFactory variant -> variants_partsfactory/_init_variant.py

Union additions from PartsFactory: 30; diverged preserved: 9

ReForge ring promoted from ForgeFactory_v0_3/src: forgefactory, reforge_engine_contracts, reforge_engine_hardening, reforge_frameforge, reforge_glyphforge, reforge_kimi_adapter, reforge_pixl8forge, reforge_pixleforge, reforge_researchcraft, reforge_wireforge, rhenium_engine
(ForgeFactory_v0_3 lattice_forge branch superseded by the union above; its 06-03 snapshot remains at the AirLock lineage path.)
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
## Curated best forms (v0.4.0 adjudication — user-authorized merge)

- core.py: PartsFactory form — PROOF had hardcoded sandbox sys.path bug; PF uses clean relative import
- rule30.py: PartsFactory form — PF adds honesty_harness ledger overrides + block-addressed obligation + safe .get
- voa_lookup.py: PartsFactory form — PF superset: adds verify_voa_lookup_harness
- forge.py: PartsFactory form — PF adds WitnessStateStore integration (witness_state_store.py in union)
- rule30_block_extractor.py: PartsFactory form — PF adds MDHG/MORSR/Speedlight tool integration (tools.py in union)
- g2_f4_t5_conjugate.py: PROOF form — the honesty-hardened bounded route classifier (explicit boundary fields); PF carried the older umbrella framing
- d12_action.py: PROOF base (full Jordanian-envelope exposition + z3_color_rotate) + PF's d12_acts_on_d4_state ported in
- rule30_predictor.py: two unrelated modules shared the name. PF's stdlib prediction-first receipts keeps the name; PROOF's numpy spectral predictor lives on as rule30_spectral_predictor.py (requires the [predictors] extra)
- __init__.py: merged import surface — PF base + 2 PROOF-only module blocks + 7 __all__ entries
- variants_partsfactory/: retired — adjudication complete; both source branches remain on disk (PROOF tree, PartsFactory tree) as the permanent record

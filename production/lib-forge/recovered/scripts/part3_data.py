PAPER_THEOREMS = {
    "CQE-paper-00": ["T3", "T4", "T5", "T6", "T7"],
    "CQE-paper-01": ["T_BIJECTIVE"],
    "CQE-paper-02": ["T_CORRECTION"],
    "CQE-paper-03": ["T_TRIALITY", "VOA_2_6"],
    "CQE-paper-04": ["T_BOUNDARY_REPAIR", "T_WRAP"],
    "CQE-paper-05": ["T_OLOID_PATH"],
    "CQE-paper-06": ["T_CAUSAL"],
    "CQE-paper-07": ["T_BRIDGE"],
    "CQE-paper-08": ["LATTICE_CHAIN", "VOA_2_6"],
    "CQE-paper-09": ["T_HAMILTONIAN"],
    "CQE-paper-10": ["T10_MASTER"],
    "CQE-paper-11": ["T_ADMISSION"],
    "CQE-paper-12": ["T_CA_PREDICTION"],
    "CQE-paper-13": ["T_QUARK_FACE"],
    "CQE-paper-14": ["T_GR_CURVATURE"],
    "CQE-paper-15": ["T_HIGGS"],
    "CQE-paper-16": ["T_EDGE", "T_WRAP"],
    "CQE-paper-17": ["T_TOWER"],
    "CQE-paper-18": ["T_MOONSHINE"],
    "CQE-paper-19": ["T_OBSERVER"],
    "CQE-paper-20": ["T_SYNTHESIS"],
    "CQE-paper-21": ["T_MORPHIC"],
    "CQE-paper-22": ["T_METAFORGE"],
    "CQE-paper-23": ["T_FOLDFORGE"],
    "CQE-paper-24": ["T_KNIGHTFORGE"],
    "CQE-paper-25": ["T_TRAVERSAL"],
    "CQE-paper-26": ["T_ZPINCH"],
    "CQE-paper-27": ["T_DELAY"],
    "CQE-paper-28": ["T_GAME_LATTICE"],
    "CQE-paper-29": ["T_MONSTER"],
    "CQE-paper-30": ["T_GRAND_RIBBON"],
    "CQE-paper-31": ["T_META_LCR"],
    "CQE-paper-32": ["T_SUPERVISOR", "T_OBSERVATION"],
    "CQE-paper-32-obs": ["T_OBSERVATION"],
}

VERIFICATION_COMMANDS = {
    "CQE-paper-00": "python -m cqe_engine.foundation",
    "CQE-paper-01": "python -m cqe_engine.foundation T_BIJECTIVE",
    "CQE-paper-02": "python -m cqe_engine.foundation T_CORRECTION",
    "CQE-paper-03": "python -m cqe_engine.foundation T_TRIALITY",
    "CQE-paper-04": "python -m cqe_engine.foundation T_BOUNDARY_REPAIR",
    "CQE-paper-05": "python -m cqe_engine.foundation T_OLOID_PATH",
    "CQE-paper-06": "python -m cqe_engine.foundation T_CAUSAL",
    "CQE-paper-07": "python -m cqe_engine.bridge",
    "CQE-paper-08": "python -m cqe_engine.closure",
    "CQE-paper-09": "python -m cqe_engine.hamiltonian 2 3 4",
    "CQE-paper-10": "python -m cqe_engine.master_receipt",
    "CQE-paper-11": "python -m cqe_engine.admission",
    "CQE-paper-12": "python -m cqe_engine.ca_prediction",
    "CQE-paper-13": "python -m cqe_engine.quark_face",
    "CQE-paper-14": "python -m cqe_engine.gr_curvature",
    "CQE-paper-15": "python -m cqe_engine.higgs",
    "CQE-paper-16": "python -m cqe_engine.edge_residual",
    "CQE-paper-17": "python -m cqe_engine.tower",
    "CQE-paper-18": "python -m cqe_engine.moonshine",
    "CQE-paper-19": "python -m cqe_engine.observer",
    "CQE-paper-20": "python -m cqe_engine.synthesis",
    "CQE-paper-21": "python -m cqe_engine.morphforge",
    "CQE-paper-22": "python -m cqe_engine.metaforge",
    "CQE-paper-23": "python -m cqe_engine.foldforge",
    "CQE-paper-24": "python -m cqe_engine.knightforge",
    "CQE-paper-25": "python -m cqe_engine.traversal",
    "CQE-paper-26": "python -m cqe_engine.zpinch",
    "CQE-paper-27": "python -m cqe_engine.observer_delay",
    "CQE-paper-28": "python -m cqe_engine.game_lattice",
    "CQE-paper-29": "python -m cqe_engine.monster",
    "CQE-paper-30": "python -m cqe_engine.grand_ribbon",
    "CQE-paper-31": "python -m cqe_engine.meta_lcr",
    "CQE-paper-32": "python -m cqe_engine.meta_lcr",
    "CQE-paper-32-obs": "python -m cqe_engine.meta_lcr",
}

CUMULATIVE_KIT = {
    "CQE-paper-00": {"new_tools": 7, "total_tools": 7, "colors": 5, "digital_twins": 5,
        "tools": ["token:C:01 (H_bond_under_examination)", "loose_paper:grey_gradient:01 (unfolded_strand_substrate)", "pen_marker:RGB:01 (base_A_marker)", "pen_marker:RGB:02 (base_G_marker)", "pen_marker:RGB:03 (base_C_marker)", "loose_paper:reading_surface:01 (ribosome_A_site)", "receipt_sheet:white:01 (correct_base_pair_certificate)"]},
    "CQE-paper-01": {"new_tools": 3, "total_tools": 10, "colors": 5, "digital_twins": 8,
        "tools": ["token:side_flip:01", "token:fixed_point:01", "sticker:closure:01"]},
    "CQE-paper-02": {"new_tools": 3, "total_tools": 13, "colors": 7, "digital_twins": 11,
        "tools": ["token:correction:01", "clear_sleeve:overlay:01", "obligation_sheet:black:01"]},
    "CQE-paper-03": {"new_tools": 3, "total_tools": 16, "colors": 7, "digital_twins": 14,
        "tools": ["token:triangle:01", "string:rotation:01", "proof_tree_sheet:white:01"]},
    "CQE-paper-04": {"new_tools": 3, "total_tools": 19, "colors": 8, "digital_twins": 17,
        "tools": ["token:oloid:01", "loose_paper:rolling_surface:01", "receipt_sheet:curved:01"]},
    "CQE-paper-05": {"new_tools": 3, "total_tools": 22, "colors": 8, "digital_twins": 20,
        "tools": ["token:carrier:01", "string:path:01", "receipt_sheet:transport:01"]},
    "CQE-paper-06": {"new_tools": 3, "total_tools": 25, "colors": 8, "digital_twins": 23,
        "tools": ["playing_card:causal_edge:01", "string:dependency:01", "proof_tree_sheet:dag:01"]},
    "CQE-paper-07": {"new_tools": 3, "total_tools": 28, "colors": 8, "digital_twins": 26,
        "tools": ["loose_paper:lucas_base:01", "clear_sleeve:correction_overlay:01", "receipt_sheet:bridge:01"]},
    "CQE-paper-08": {"new_tools": 8, "total_tools": 36, "colors": 8, "digital_twins": 34,
        "tools": ["balsa_edge:lattice_D1:01", "balsa_edge:lattice_D3:01", "balsa_edge:lattice_D4:01", "balsa_edge:lattice_D24:01", "balsa_edge:lattice_D72:01", "token:code:01", "string:chain:01", "proof_tree_sheet:closure:01"]},
    "CQE-paper-09": {"new_tools": 3, "total_tools": 39, "colors": 8, "digital_twins": 37,
        "tools": ["tab_divider:hamiltonian:01", "loose_paper:window:01", "receipt_sheet:temporal:01"]},
    "CQE-paper-10": {"new_tools": 14, "total_tools": 53, "colors": 8, "digital_twins": 51,
        "tools": ["token:receipt_bead:01-10", "string:xor_chain:01", "pen_marker:hash:01", "obligation_sheet:black:01", "receipt_sheet:master:01"]},
    "CQE-paper-11": {"new_tools": 3, "total_tools": 56, "colors": 8, "digital_twins": 54,
        "tools": ["admission_gate:01", "token:theory:01", "receipt_sheet:admission:01"]},
    "CQE-paper-12": {"new_tools": 3, "total_tools": 59, "colors": 8, "digital_twins": 57,
        "tools": ["ca_sheet:01", "token:rule30:01", "receipt_sheet:ca:01"]},
    "CQE-paper-13": {"new_tools": 3, "total_tools": 62, "colors": 8, "digital_twins": 60,
        "tools": ["token:quark_face:01", "string:color:01", "receipt_sheet:quark:01"]},
    "CQE-paper-14": {"new_tools": 3, "total_tools": 65, "colors": 8, "digital_twins": 63,
        "tools": ["balsa_edge:curvature:01", "tensor:einstein:01", "receipt_sheet:gr:01"]},
    "CQE-paper-15": {"new_tools": 3, "total_tools": 68, "colors": 8, "digital_twins": 66,
        "tools": ["token:higgs:01", "string:mass:01", "receipt_sheet:higgs:01"]},
    "CQE-paper-16": {"new_tools": 3, "total_tools": 71, "colors": 8, "digital_twins": 69,
        "tools": ["loose_paper:powers_of_ten:01", "string:residual:01", "receipt_sheet:edge:01"]},
    "CQE-paper-17": {"new_tools": 7, "total_tools": 78, "colors": 8, "digital_twins": 76,
        "tools": ["balsa_edge:e6:01", "balsa_edge:e7:01", "balsa_edge:e8:01", "string:tower:01", "token:tower_gate:01", "proof_tree_sheet:tower:01", "receipt_sheet:tower:01"]},
    "CQE-paper-18": {"new_tools": 3, "total_tools": 81, "colors": 8, "digital_twins": 72,
        "tools": ["token:voa:01", "string:moonshine:01", "receipt_sheet:voa:01"]},
    "CQE-paper-19": {"new_tools": 3, "total_tools": 84, "colors": 8, "digital_twins": 75,
        "tools": ["token:observer:01", "string:face:01", "receipt_sheet:observer:01"]},
    "CQE-paper-20": {"new_tools": 14, "total_tools": 98, "colors": 8, "digital_twins": 89,
        "tools": ["token:bead:11-20", "string:xor_chain:02", "pen_marker:hash:02", "receipt_sheet:synthesis:01"]},
    "CQE-paper-21": {"new_tools": 5, "total_tools": 103, "colors": 8, "digital_twins": 94,
        "tools": ["morphforge:01", "polyforge:01", "morphonix:01", "token:morph:01", "receipt_sheet:morph:01"]},
    "CQE-paper-22": {"new_tools": 3, "total_tools": 106, "colors": 8, "digital_twins": 97,
        "tools": ["metaforge:01", "token:material:01", "receipt_sheet:metaforge:01"]},
    "CQE-paper-23": {"new_tools": 3, "total_tools": 109, "colors": 8, "digital_twins": 100,
        "tools": ["foldforge:01", "token:protein:01", "receipt_sheet:foldforge:01"]},
    "CQE-paper-24": {"new_tools": 3, "total_tools": 112, "colors": 8, "digital_twins": 103,
        "tools": ["knightforge:01", "string:l_conjugate:01", "receipt_sheet:knight:01"]},
    "CQE-paper-25": {"new_tools": 3, "total_tools": 115, "colors": 8, "digital_twins": 106,
        "tools": ["traversal:01", "string:energy:01", "receipt_sheet:traversal:01"]},
    "CQE-paper-26": {"new_tools": 3, "total_tools": 118, "colors": 8, "digital_twins": 109,
        "tools": ["zpinch:01", "string:shear:01", "receipt_sheet:zpinch:01"]},
    "CQE-paper-27": {"new_tools": 3, "total_tools": 121, "colors": 8, "digital_twins": 112,
        "tools": ["observer_delay:01", "shared_reality:01", "receipt_sheet:delay:01"]},
    "CQE-paper-28": {"new_tools": 3, "total_tools": 124, "colors": 8, "digital_twins": 115,
        "tools": ["gamelattice:01", "string:move:01", "receipt_sheet:game:01"]},
    "CQE-paper-29": {"new_tools": 3, "total_tools": 127, "colors": 8, "digital_twins": 118,
        "tools": ["monster_bond:01", "string:supersingular:01", "receipt_sheet:monster:01"]},
    "CQE-paper-30": {"new_tools": 7, "total_tools": 134, "colors": 8, "digital_twins": 125,
        "tools": ["token:grand_ribbon:01", "string:grand_ribbon:01", "token:bead:01-31", "string:lcr_chain:01", "pen_marker:hash:03", "receipt_sheet:ribbon:01", "receipt_sheet:meta:01"]},
    "CQE-paper-31": {"new_tools": 3, "total_tools": 137, "colors": 8, "digital_twins": 128,
        "tools": ["meta_lcr:01", "actor_object_distinction:01", "receipt_sheet:meta_lcr:01"]},
    "CQE-paper-32": {"new_tools": 7, "total_tools": 144, "colors": 8, "digital_twins": 135,
        "tools": ["superpermutation_cursor:01", "notebook:full_kit_manifest:01", "string:supervisor_cursor:01", "balsa_edge:superpermutation_frame:01", "dice:probability_boundary:01", "playing_card:permutation_operator:01", "receipt_sheet:supervisor:01"]},
    "CQE-paper-32-obs": {"new_tools": 0, "total_tools": 144, "colors": 8, "digital_twins": 135,
        "tools": []},
}

SUBSTITUTION_RULES = """# Substitution Rules (12 classes - all idempotent)

## Common (can be improvised with anything satisfying the condition)

| Tool Class | DNA Component | Idempotent Condition | Common Substitutes |
|------------|---------------|---------------------|-------------------|
| token | H_bond_under_examination | read(action) -> state; read(state) -> same state | Any distinguishable marker |
| loose_paper | unfolded_strand_substrate | Accepts gradient without preferred orientation | Paper, cardboard, fabric |
| pen_marker | base_A/G/C_marker | Distinguishable from other two colors in triad | 3 colored pencils, nail polish, markers |
| string | phosphate_backbone | Continuous, flexible, accepts beads/knots | Thread, yarn, fishing line, wire |
| clear_sleeve | major_groove_access | Transparent, writable, removable without damaging base | Sheet protector, ziplock, acetate |
| sticker | correct_base_pair_certificate | Fixed, non-movable, indicates verified state | Tape, post-it, glue dots |
| balsa_edge | primary_structure_lock | Rigid, uniform length, stackable | Coffee stirrers, toothpicks, popsicle sticks |
| gradient_page | major_groove_chemical_shift | Gradient from C1->C2->C3 readable as triad | Gradient-colored paper, watercolor wash |
| playing_card | folding_event | 52 distinct objects with red/black polarity, 4 suits | Index cards with suits drawn |
| dice | quantum_measurement_boundary | Bounded randomness with known state space | Spinner, random number app |
| receipt_sheet | base_pair_certificate | Replayable record of (input, output, residue) | Index card, notebook page |
| black_sticker | mismatch_repair_obligation | Dark, fixed, indicates unresolved state carried forward | Black marker dot, electrical tape |

## Improvised (use when no substitute available)

| Tool Class | Idempotent Condition | Improvised From |
|------------|---------------------|-----------------|
| gradient_page | Gradient from C1->C2->C3 readable as triad | Any 3-color progression on flat surface |
| playing_card | 52 distinct objects with red/black, 4 suits | Numbered paper squares (1-13)x4 suits |
| dice | Bounded randomness, known state space | Numbered paper in hat, random.org |
| receipt_sheet | Replayable record (input, output, residue) | Structured log entry in any medium |
| black_sticker | Dark, fixed, indicates unresolved state | Permanent marker dot, charcoal |
"""
"""
MetaForge-AI: Metamaterial Design System
=========================================

Thin orchestration layer on top of the actual Forge engines:
- lattice_forge: Rule30, Oloid, J3O, F4, Mandelbrot, lattice codes
- MandleForge: Gluon mass → Mandelbrot parameter space (K_max=9)
- ManiForge: Braid B₃, knot invariants, seams, creases
- ChromaForge: Receipt ledger, conservation, MDHG, SpeedLight, MMDB, TarPit, SNAP
- PixelForge: Surfaces, ink, projection, frames
- cqe_engine: Scope, ribbon, paper registry, shared memory, Hamiltonian windows
"""

from __future__ import annotations
import sys
from pathlib import Path

# ─── Locate and wire lattice_forge ───
_ENGINE_DIR = Path(__file__).resolve().parent
_LIB_FORGE_DIR = _ENGINE_DIR.parent

def _find_lattice_forge_src():
    for base in (_LIB_FORGE_DIR, *_LIB_FORGE_DIR.parents):
        for rel in (("CMPLX-R30-main", "PROOF", "src"),
                    ("CQE_CMPLX", "CMPLX-R30-main", "PROOF", "src")):
            cand = base.joinpath(*rel)
            if (cand / "lattice_forge").is_dir():
                return cand
    return None

_LF_SRC = _find_lattice_forge_src()
if _LF_SRC is not None and str(_LF_SRC) not in sys.path:
    sys.path.insert(0, str(_LF_SRC))

for _p in (str(_ENGINE_DIR), str(_LIB_FORGE_DIR)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

# ─── Import ALL actual Forge engines ───

# lattice_forge complete substrate
from lattice_forge.rule30 import (
    rule30_mandelbrot_boundary_scalar,
    rule30_oloid_winding_from_n,
    rule30_oloid_antipodal_winding,
    rule30_nth_bit_expression,
    rule30_julia_resolution,
    rule30_nth_bit_expression as rule30_predict,
    verify_rule30_mandelbrot_boundary_scalar,
    verify_rule30_oloid_winding_from_n,
    verify_rule30_oloid_antipodal_winding,
)

from lattice_forge.centroid_voa import (
    gluon,
    swap_LR, swap_LC, swap_CR,
    hamming_to_centroid,
    anneal_to_lie_conjugate,
    verify_gluon_invariance,
    three_conjugate_label,
    voa_weight,
    z4_period,
)

from lattice_forge.f4_action import (
    closed_form_rule30_8x8_transition_exact,
    closed_form_shell2_3x3,
    decompose_3x3_in_s3_group_ring,
    search_for_su3_closure_scale,
    verify_n3_su3_closure_exact,
)

from lattice_forge.jordan_j3 import (
    J3O,
    verify_j3o_axioms,
)

from lattice_forge.octonion import (
    Octonion,
    verify_octonion_axioms,
)

from lattice_forge.cayley_dickson_oloid import (
    CayleyDicksonOloidNormalForm,
    cayley_dickson_oloid_normal_form,
    verify_cayley_dickson_oloid_normal_form,
)

from lattice_forge.lattice_codes import (
    verify_parameter_chain,
    verify_hamming_7_fano,
    verify_extended_hamming_8,
    verify_golay_24,
)

from lattice_forge.morphonics import (
    morphonics_model_v0_2,
    verify_morphonics_model,
)

from lattice_forge.oloid_model_selection import (
    evaluate_candidate,
    rank_candidates,
    verify_oloid_model_selection,
)

from lattice_forge.morphonics import (
    MorphonRecord,
    TransformRecord,
    ProjectionRecord,
    AccountingRecord,
    BridgeRecord,
    ClaimStatusRecord,
    FailureRecord,
)

# MandleForge - Gluon mass → Mandelbrot parameter space
from MandleForge import (
    GluonMassPoint,
    mandelbrot_escape_time,
    mandelbrot_basin_depth,
    JuliaFiber,
    MandelbrotPath,
    diagnose_C_convergence,
)

# ManiForge - Braid B₃, knot invariants, seams, creases
from ManiForge import (
    BraidGenerator,
    BraidWord,
    Z4_CYCLE,
    TRIALITY_ROTATION,
    KnotType,
    KnotInvariant,
    SeamType,
    Seam,
    CreaseType,
    Crease,
    WORKBOOK_TO_MANIFORGE,
)

# ChromaForge - Receipt ledger, conservation, MDHG, SpeedLight, MMDB, TarPit, SNAP
from ChromaForge import (
    ChromaForgeEngine,
    engine as chroma_engine,
    ReceiptLedger,
    ConservationLedger,
    MDHGEngine,
    SpeedLightEngine,
    MMDBEngine,
    TarPitEngine,
    SNAPEngine,
    COUPLING,
    PHI,
    execute as chroma_execute,
    store as chroma_store,
    status as chroma_status,
)

# PixelForge - Surfaces, ink, projection, frames
from PixelForge import (
    PixelForgeEngine,
    engine as pixel_engine,
    Surface,
    SurfaceRegistry,
    InkEngine,
    Stroke,
    PointerSample,
    PROJECTIONS,
    project,
    to_screen,
    project_state,
    Frame,
    FrameStream,
)

# cqe_engine layer - Scope, ribbon, paper, shared memory, Hamiltonian
from cqe_engine import (
    Scope,
    scope,
    is_local, is_meso, is_global,
    Ribbon,
    Slot,
    SlotName,
    SLOT_NAMES,
    Paper,
    Registry,
    transport,
    Receipt,
    verify_all_foundations,
    iterative_hamiltonian,
    hamiltonian_read,
    BASE_C_FORMS,
)

__all__ = [
    # lattice_forge
    "rule30_mandelbrot_boundary_scalar",
    "rule30_oloid_winding_from_n",
    "rule30_oloid_antipodal_winding",
    "rule30_nth_bit_expression",
    "rule30_predict",
    "rule30_julia_resolution",
    "verify_rule30_mandelbrot_boundary_scalar",
    "verify_rule30_oloid_winding_from_n",
    "verify_rule30_oloid_antipodal_winding",
    "gluon",
    "swap_LR", "swap_LC", "swap_CR",
    "hamming_to_centroid",
    "anneal_to_lie_conjugate",
    "verify_gluon_invariance",
    "three_conjugate_label",
    "voa_weight",
    "z4_period",
    "closed_form_rule30_8x8_transition_exact",
    "closed_form_shell2_3x3",
    "decompose_3x3_in_s3_group_ring",
    "search_for_su3_closure_scale",
    "verify_n3_su3_closure_exact",
    "J3O",
    "verify_j3o_axioms",
    "Octonion",
    "verify_octonion_axioms",
    "CayleyDicksonOloidNormalForm",
    "cayley_dickson_oloid_normal_form",
    "verify_cayley_dickson_oloid_normal_form",
    "verify_parameter_chain",
    "verify_hamming_7_fano",
    "verify_extended_hamming_8",
    "verify_golay_24",
    "morphonics_model_v0_2",
    "verify_morphonics_model",
    "evaluate_candidate",
    "rank_candidates",
    "verify_oloid_model_selection",
    "MorphonRecord",
    "TransformRecord",
    "ProjectionRecord",
    "AccountingRecord",
    "BridgeRecord",
    "ClaimStatusRecord",
    "FailureRecord",
    
    # MandleForge
    "GluonMassPoint",
    "mandelbrot_escape_time",
    "mandelbrot_basin_depth",
    "JuliaFiber",
    "MandelbrotPath",
    "diagnose_C_convergence",
    
    # ManiForge
    "BraidGenerator",
    "BraidWord",
    "Z4_CYCLE",
    "TRIALITY_ROTATION",
    "KnotType",
    "KnotInvariant",
    "SeamType",
    "Seam",
    "CreaseType",
    "Crease",
    "WORKBOOK_TO_MANIFORGE",
    
    # ChromaForge
    "ChromaForgeEngine",
    "chroma_engine",
    "ReceiptLedger",
    "ConservationLedger",
    "MDHGEngine",
    "SpeedLightEngine",
    "MMDBEngine",
    "TarPitEngine",
    "SNAPEngine",
    "COUPLING",
    "PHI",
    "chroma_execute",
    "chroma_store",
    "chroma_status",
    
    # PixelForge
    "PixelForgeEngine",
    "pixel_engine",
    "Surface",
    "SurfaceRegistry",
    "InkEngine",
    "Stroke",
    "PointerSample",
    "PROJECTIONS",
    "project",
    "to_screen",
    "project_state",
    "Frame",
    "FrameStream",
    
    # cqe_engine
    "Scope",
    "scope",
    "is_local", "is_meso", "is_global",
    "Ribbon",
    "Slot",
    "SlotName",
    "SLOT_NAMES",
    "Paper",
    "Registry",
    "Rhyme",
    "RhymeScheme",
    "transport",
    "Receipt",
    "verify_all_foundations",
    "iterative_hamiltonian",
    "hamiltonian_read",
    "BASE_C_FORMS",
]

__version__ = "0.1.0"
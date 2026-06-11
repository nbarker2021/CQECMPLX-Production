"""lattice_forge (slim stick build) — Binary Boundary Adapter chain only.

Full substrate lives in the production tree; the stick carries exactly what
the Event Law kernel computes with: BBA + centroid_voa (pure stdlib).
"""
from .centroid_voa import (
    STATES, LIE_CONJUGATES, TRUE_VACUA,
    gluon, swap_LR, swap_LC, swap_CR, TRANSPOSITIONS,
    hamming_to_centroid, anneal_to_lie_conjugate, voa_weight,
)
from .binary_boundary_adapter import (
    adapt, BinaryBoundaryAdapter, cascade_level, emission_level,
    from_bytes, from_hex, from_int, from_file,
)

"""ManiForge — Braid, Knot, Seam, Crease Algebra

Public surface for the string topology engine underlying workbook operations.
All workbook strings map to these primitives.
"""
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple, Optional

# ---------------------------------------------------------------------------
# Braid Group B₃ (3 strands = L, C, R / 3 frames = C/R/L-centroid)
# ---------------------------------------------------------------------------

class BraidGenerator(Enum):
    """Generators of B₃ = ⟨σ₁, σ₂, σ₃ | σ₁σ₂σ₁=σ₂σ₁σ₂, σ₁σ₃=σ₃σ₁, ...⟩"""
    SIGMA_1 = "σ₁"   # swap_LR (antipodal) — red string, side-flip
    SIGMA_2 = "σ₂"   # swap_LC — blue string, frame transition C→L
    SIGMA_3 = "σ₃"   # swap_CR — gold string, frame transition C→R


@dataclass(frozen=True)
class BraidWord:
    """A word in B₃ generators."""
    generators: Tuple[BraidGenerator, ...]
    
    def __mul__(self, other: "BraidWord") -> "BraidWord":
        return BraidWord(self.generators + other.generators)
    
    def inverse(self) -> "BraidWord":
        return BraidWord(tuple(reversed(self.generators)))
    
    def __str__(self) -> str:
        return "".join(g.value for g in self.generators)

# Important braid words
Z4_CYCLE = BraidWord((BraidGenerator.SIGMA_1, BraidGenerator.SIGMA_2, 
                       BraidGenerator.SIGMA_3, BraidGenerator.SIGMA_2))  # σ₁σ₂σ₃σ₂
TRIALITY_ROTATION = BraidWord((BraidGenerator.SIGMA_1, BraidGenerator.SIGMA_2, 
                                BraidGenerator.SIGMA_3))  # σ₁σ₂σ₃

# ---------------------------------------------------------------------------
# Knot Invariants
# ---------------------------------------------------------------------------

class KnotType(Enum):
    UNKNOT = "unknot"                    # Period-1 true vacuum
    TORUS_2_5 = "torus(2,5)"             # Period-4 excited state
    TORUS_3_4 = "torus(3,4)"             # Higher excitation
    COMPOSITE = "composite"              # Decay product knot

@dataclass(frozen=True)
class KnotInvariant:
    """Knot invariant bundle for a closed braid word."""
    knot_type: KnotType
    alexander_poly: str                  # e.g., "1", "t-1+t^-1"
    jones_poly: str                      # e.g., "1", "q+q^-1-q^2"
    homfly_pt: str                       # Full HOMFLY-PT
    
    @classmethod
    def from_period(cls, z4_period: int) -> "KnotInvariant":
        if z4_period == 1:
            return cls(KnotType.UNKNOT, "1", "1", "1")
        elif z4_period == 4:
            return cls(KnotType.TORUS_2_5, "t-1+t^-1", "q+q^-1-q^2", "...")
        return cls(KnotType.COMPOSITE, "...", "...", "...")


# ---------------------------------------------------------------------------
# Seams (frame boundaries where Gluon crosses)
# ---------------------------------------------------------------------------

class SeamType(Enum):
    C_TO_R = "C→R"        # Frame 0→1
    R_TO_CFLIP = "R→C'"   # Frame 1→2  
    CFLIP_TO_L = "C'→L"   # Frame 2→3
    L_TO_C = "L→C"        # Frame 3→0


@dataclass(frozen=True)
class Seam:
    """A frame boundary crossing with Gluon transport."""
    seam_type: SeamType
    gluon_before: int        # C value before crossing
    gluon_after: int         # C value after crossing (invariant)
    certificate: str         # "C invariant across seam"
    
    @classmethod
    def from_transition(cls, frame_from: int, frame_to: int, C: int) -> "Seam":
        seam_map = {
            (0, 1): SeamType.C_TO_R,
            (1, 2): SeamType.R_TO_CFLIP,
            (2, 3): SeamType.CFLIP_TO_L,
            (3, 0): SeamType.L_TO_C,
        }
        return cls(seam_map[(frame_from, frame_to)], C, C, "Gluon invariant")


# ---------------------------------------------------------------------------
# Creases (sharp topological transitions)
# ---------------------------------------------------------------------------

class CreaseType(Enum):
    OLOID_FOLD = "oloid_fold"          # N|-N midpoint formation
    CHAMBER_REFLECTION = "reflection"  # L=R boundary reflection
    ANTIPODE_FLIP = "antipode_flip"    # LR swap
    K_WINDOW_BREACH = "k_breach"       # K>9 boundary


@dataclass(frozen=True)
class Crease:
    """A non-smooth topological transition with certificates."""
    crease_type: CreaseType
    location: str                    # "oloid_midpoint", "L=R_plane", etc.
    gluon_invariant: bool            # C preserved?
    certificate: str

    @classmethod
    def oloid_fold(cls, C: int) -> "Crease":
        return cls(CreaseType.OLOID_FOLD, "s* = (N+-N)/2", True, f"C={C} mediator invariant")
    
    @classmethod
    def chamber_reflection(cls, C: int) -> "Crease":
        return cls(CreaseType.CHAMBER_REFLECTION, "L=R plane", True, f"C={C} invariant under LR swap")


# ---------------------------------------------------------------------------
# Workbook String → ManiForge Primitive Map
# ---------------------------------------------------------------------------

WORKBOOK_TO_MANIFORGE = {
    "red_string": BraidGenerator.SIGMA_1,      # side-flip / antipodal
    "blue_string": BraidGenerator.SIGMA_2,     # C↔L frame transition
    "gold_string": BraidGenerator.SIGMA_3,     # C↔R frame transition / repair
    "white_string": Z4_CYCLE,                  # Z4 period template
    "knot_true_vacuum": KnotType.UNKNOT,       # period-1
    "knot_excited": KnotType.TORUS_2_5,        # period-4
    "seam_C_R": SeamType.C_TO_R,
    "seam_R_Cflip": SeamType.R_TO_CFLIP,
    "seam_Cflip_L": SeamType.CFLIP_TO_L,
    "seam_L_C": SeamType.L_TO_C,
    "crease_oloid": CreaseType.OLOID_FOLD,
    "crease_reflection": CreaseType.CHAMBER_REFLECTION,
    "crease_antipode": CreaseType.ANTIPODE_FLIP,
    "crease_k_breach": CreaseType.K_WINDOW_BREACH,
}


# ---------------------------------------------------------------------------
# Public Surface
# ---------------------------------------------------------------------------

__all__ = [
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
]
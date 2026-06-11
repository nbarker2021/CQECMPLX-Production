"""
Pareto Partnering Algorithm - Finds most compatible material pairs
"""
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional
import numpy as np
from material_db import MaterialProperties, get_material, list_materials


@dataclass
class ParetoPartner:
    """A material pair with compatibility scores"""
    material_a: MaterialProperties
    material_b: MaterialProperties
    lattice_match: float  # 0-1, how well lattices match
    property_synergy: float  # 0-1, complementary properties
    gluon_coherence: float  # 0-1, gluon mass alignment
    oloid_compatibility: float  # 0-1, both have oloid closure
    pareto_score: float  # Overall Pareto optimality
    interface_energy: float  # Estimated interface energy (eV/Å²)
    strain_tolerance: float  # Max tolerable strain before failure


def compute_lattice_match(mat_a: MaterialProperties, mat_b: MaterialProperties) -> float:
    """Compute lattice matching score between two materials"""
    # Get lattice constants
    a_a = mat_a.lattice_constants.get("a", 0)
    a_b = mat_b.lattice_constants.get("a", 0)
    
    if a_a == 0 or a_b == 0:
        return 0.5  # Unknown, neutral
    
    # Mismatch percentage
    mismatch = abs(a_a - a_b) / max(a_a, a_b)
    
    # Score: 1.0 for perfect match, decays with mismatch
    if mismatch < 0.01:
        return 1.0
    elif mismatch < 0.05:
        return 0.8
    elif mismatch < 0.1:
        return 0.5
    else:
        return 0.2


def compute_property_synergy(mat_a: MaterialProperties, mat_b: MaterialProperties) -> float:
    """Compute how well material properties complement each other"""
    score = 0.0
    
    # Mechanical complementarity (one stiff, one tough)
    stiffness_ratio = mat_a.youngs_modulus / max(mat_b.youngs_modulus, 1)
    if 0.1 < stiffness_ratio < 10:
        score += 0.25
    
    # Thermal complementarity
    thermal_ratio = mat_a.thermal_conductivity / max(mat_b.thermal_conductivity, 1)
    if 0.01 < thermal_ratio < 100:
        score += 0.2
    
    # Electronic complementarity (one conductive, one insulating)
    cond_a = mat_a.electrical_conductivity
    cond_b = mat_b.electrical_conductivity
    if (cond_a > 1e4 and cond_b < 1e2) or (cond_b > 1e4 and cond_a < 1e2):
        score += 0.3  # Excellent for heterostructures
    
    # Band gap engineering potential
    gap_a = mat_a.band_gap
    gap_b = mat_b.band_gap
    if abs(gap_a - gap_b) > 1.0:
        score += 0.15  # Can create type-II heterojunctions
    
    # Hardness complementarity
    if (mat_a.hardness > 10 and mat_b.hardness < 1) or (mat_b.hardness > 10 and mat_a.hardness < 1):
        score += 0.1
    
    return min(score, 1.0)


def compute_gluon_coherence(mat_a: MaterialProperties, mat_b: MaterialProperties) -> float:
    """Compute gluon mass alignment from lattice_forge"""
    g_a = mat_a.gluon_mass
    g_b = mat_b.gluon_mass
    
    # Difference in gluon mass
    diff = abs(g_a - g_b)
    
    # Coherence: closer gluon masses = better coherence
    if diff < 0.1:
        return 1.0
    elif diff < 0.3:
        return 0.8
    elif diff < 0.5:
        return 0.5
    else:
        return 0.2


def compute_oloid_compatibility(mat_a: MaterialProperties, mat_b: MaterialProperties) -> float:
    """Both materials must support oloid closure"""
    if mat_a.oloid_closure and mat_b.oloid_closure:
        return 1.0
    elif mat_a.oloid_closure or mat_b.oloid_closure:
        return 0.5
    else:
        return 0.1


def estimate_interface_energy(mat_a: MaterialProperties, mat_b: MaterialProperties) -> float:
    """Estimate interface energy in eV/Å²"""
    # Simplified model based on surface energies
    surface_energy_a = mat_a.youngs_modulus * 1e-3  # Approximate
    surface_energy_b = mat_b.youngs_modulus * 1e-3
    
    # Mismatch penalty
    mismatch = abs(mat_a.lattice_constants.get("a", 1) - mat_b.lattice_constants.get("a", 1))
    mismatch /= max(mat_a.lattice_constants.get("a", 1), mat_b.lattice_constants.get("a", 1))
    
    interface = (surface_energy_a + surface_energy_b) / 2 * (1 + mismatch * 10)
    return interface * 1e-3  # Convert to eV/Å²


def compute_strain_tolerance(mat_a: MaterialProperties, mat_b: MaterialProperties) -> float:
    """Compute max tolerable strain before failure"""
    # Based on tensile strength and modulus
    strain_a = mat_a.tensile_strength / mat_a.youngs_modulus
    strain_b = mat_b.tensile_strength / mat_b.youngs_modulus
    
    # Interface strain tolerance is limited by weaker material
    return min(strain_a, strain_b) * 0.5  # Safety factor


def find_pareto_partners(
    base_material: MaterialProperties,
    candidate_materials: List[MaterialProperties],
    weights: Optional[Dict[str, float]] = None
) -> List[ParetoPartner]:
    """
    Find Pareto-optimal material partners for a base material.
    
    Args:
        base_material: The primary material to partner
        candidate_materials: List of candidate partner materials
        weights: Optional weights for scoring: lattice, property, gluon, oloid
        
    Returns:
        List of ParetoPartner objects sorted by Pareto score
    """
    if weights is None:
        weights = {
            "lattice": 0.25,
            "property": 0.25,
            "gluon": 0.3,
            "oloid": 0.2
        }
    
    partners = []
    for candidate in candidate_materials:
        if candidate.name == base_material.name:
            continue
            
        lattice = compute_lattice_match(base_material, candidate)
        prop = compute_property_synergy(base_material, candidate)
        gluon = compute_gluon_coherence(base_material, candidate)
        oloid = compute_oloid_compatibility(base_material, candidate)
        
        pareto_score = (
            weights["lattice"] * lattice +
            weights["property"] * prop +
            weights["gluon"] * gluon +
            weights["oloid"] * oloid
        )
        
        interface = estimate_interface_energy(base_material, candidate)
        strain = compute_strain_tolerance(base_material, candidate)
        
        partners.append(ParetoPartner(
            material_a=base_material,
            material_b=candidate,
            lattice_match=lattice,
            property_synergy=prop,
            gluon_coherence=gluon,
            oloid_compatibility=oloid,
            pareto_score=pareto_score,
            interface_energy=interface,
            strain_tolerance=strain
        ))
    
    # Sort by Pareto score descending
    partners.sort(key=lambda p: p.pareto_score, reverse=True)
    return partners


def print_pareto_results(partners: List[ParetoPartner], top_n: int = 5):
    """Print Pareto partnering results"""
    print(f"\n{'='*80}")
    print(f"PARETO PARTNERING RESULTS for {partners[0].material_a.name}")
    print(f"{'='*80}")
    print(f"{'Rank':<5} {'Partner':<25} {'Pareto':<8} {'Lattice':<8} {'Property':<8} {'Gluon':<8} {'Oloid':<8} {'Interface':<10} {'Strain':<8}")
    print(f"{'-'*80}")
    for i, p in enumerate(partners[:top_n]):
        print(f"{i+1:<5} {p.material_b.name:<25} {p.pareto_score:<8.3f} "
              f"{p.lattice_match:<8.3f} {p.property_synergy:<8.3f} "
              f"{p.gluon_coherence:<8.3f} {p.oloid_compatibility:<8.3f} "
              f"{p.interface_energy:<10.4f} {p.strain_tolerance:<8.4f}")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    # Test
    from material_db import get_material, list_materials
    
    base = get_material("graphene")
    all_mats = [get_material(k) for k in list_materials()]
    
    partners = find_pareto_partners(base, all_mats)
    print_pareto_results(partners)
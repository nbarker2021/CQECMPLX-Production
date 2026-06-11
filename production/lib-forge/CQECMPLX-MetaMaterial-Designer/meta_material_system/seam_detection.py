"""
Seam Material Detection Logic
Identifies sub-forms that act as seam/interlayer materials rather than direct inclusions
"""
from dataclasses import dataclass
from typing import List, Dict, Optional
import math
from material_db import MaterialProperties, get_material, list_materials, MATERIAL_DATABASE
from fold_evaluation import FoldSequence, ErrorWallType
from pareto_partnering import ParetoPartner


@dataclass
class SeamCandidate:
    """A material identified as a potential seam/interlayer"""
    material: MaterialProperties
    role: str  # "compliance", "barrier", "gradient", "healing", "electrical"
    placement: str  # "interface", "midlayer", "surface", "gradient"
    effectiveness: float  # 0-1
    reason: str
    required_thickness: float  # nm
    processing_compatibility: float  # 0-1


# Seam material roles and their requirements
SEAM_ROLES = {
    "compliance": {
        "description": "Soft layer to absorb lattice mismatch strain",
        "target_properties": {"youngs_modulus": "< 100", "poisson_ratio": "> 0.3"},
        "best_materials": ["bp", "mxene"],
    },
    "barrier": {
        "description": "Dense layer to block diffusion/reaction",
        "target_properties": {"density": "> 4", "hardness": "> 5"},
        "best_materials": ["sto", "mowse2", "mxene"],
    },
    "gradient": {
        "description": "Graded composition for smooth property transition",
        "target_properties": {"band_gap": "intermediate", "lattice_constant": "intermediate"},
        "best_materials": ["mowse2", "mos2"],
    },
    "healing": {
        "description": "Self-healing layer using CNP/CA dust mechanisms",
        "target_properties": {"gluon_mass": "> 1.5", "oloid_closure": False},
        "best_materials": ["mxene", "mowse2", "tbg"],
    },
    "electrical": {
        "description": "Conductive/insulating interlayer for device function",
        "target_properties": {"electrical_conductivity": "targeted"},
        "best_materials": ["graphene", "hbn", "mxene"],
    },
}


def detect_seam_candidates(
    base: MaterialProperties,
    partner: MaterialProperties,
    fold_seq: FoldSequence
) -> List[SeamCandidate]:
    """
    Analyze fold sequence to identify needed seam materials.
    
    Looks at:
    1. Error walls that weren't opportunities (need mitigation)
    2. Large property mismatches
    3. Interface energy hotspots
    4. Lattice mismatch
    5. Thermal expansion mismatch
    """
    candidates = []
    
    # 1. Check for unresolved error walls needing seam mitigation
    for wall_type, count in fold_seq.error_wall_summary.items():
        if count > 0 and wall_type in [ErrorWallType.CNP, ErrorWallType.IV, ErrorWallType.BF, ErrorWallType.NA]:
            # Need seam to handle these
            if wall_type == ErrorWallType.CNP:
                # Vacancy/defect issues -> healing seam
                candidates.append(SeamCandidate(
                    material=get_material("mxene"),
                    role="healing",
                    placement="interface",
                    effectiveness=0.85,
                    reason=f"CNP dust at folds: {count} occurrences - MXene provides self-healing vacancy network",
                    required_thickness=2.0,
                    processing_compatibility=0.7
                ))
            elif wall_type == ErrorWallType.IV:
                # Symmetry breaking -> gradient seam
                candidates.append(SeamCandidate(
                    material=get_material("mowse2"),
                    role="gradient",
                    placement="midlayer",
                    effectiveness=0.75,
                    reason=f"IV symmetry violation: {count} - MoWSe2 alloy provides graded valley symmetry transition",
                    required_thickness=5.0,
                    processing_compatibility=0.8
                ))
            elif wall_type == ErrorWallType.BF:
                # Bond failure -> compliance seam
                candidates.append(SeamCandidate(
                    material=get_material("bp"),
                    role="compliance",
                    placement="interface",
                    effectiveness=0.80,
                    reason=f"BF bond failure: {count} - BP puckered structure accommodates shear",
                    required_thickness=3.0,
                    processing_compatibility=0.75
                ))
            elif wall_type == ErrorWallType.NA:
                # Terminal -> barrier seam
                candidates.append(SeamCandidate(
                    material=get_material("sto"),
                    role="barrier",
                    placement="surface",
                    effectiveness=0.70,
                    reason=f"NA no antipode: {count} - STO perovskite provides stable termination",
                    required_thickness=10.0,
                    processing_compatibility=0.6
                ))
    
    # 2. Lattice mismatch seam
    lattice_mismatch = abs(
        base.lattice_constants.get("a", 0) - partner.lattice_constants.get("a", 0)
    ) / max(base.lattice_constants.get("a", 1), partner.lattice_constants.get("a", 1))
    
    if lattice_mismatch > 0.05:
        candidates.append(SeamCandidate(
            material=get_material("mowse2"),
            role="gradient",
            placement="midlayer",
            effectiveness=min(0.9, 1.0 - lattice_mismatch * 5),
            reason=f"Lattice mismatch {lattice_mismatch*100:.1f}% - MoWSe2 graded alloy bridges lattice constants",
            required_thickness=max(3.0, lattice_mismatch * 50),
            processing_compatibility=0.8
        ))
    
    # 3. Thermal expansion mismatch
    te_mismatch = abs(base.thermal_expansion - partner.thermal_expansion) / max(abs(base.thermal_expansion), abs(partner.thermal_expansion), 1e-6)
    
    if te_mismatch > 0.5:
        candidates.append(SeamCandidate(
            material=get_material("bp"),
            role="compliance",
            placement="interface",
            effectiveness=0.75,
            reason=f"Thermal expansion mismatch {te_mismatch*100:.0f}% - BP anisotropic expansion buffers thermal cycling",
            required_thickness=2.0,
            processing_compatibility=0.8
        ))
    
    # 4. Electronic property mismatch (for device applications)
    cond_ratio = base.electrical_conductivity / max(partner.electrical_conductivity, 1)
    if cond_ratio > 1e6 or cond_ratio < 1e-6:
        # Need electrical seam
        if base.electrical_conductivity > partner.electrical_conductivity:
            seam_mat = get_material("hbn")  # Insulating seam
            role = "electrical"
        else:
            seam_mat = get_material("graphene")  # Conductive seam
            role = "electrical"
        
        candidates.append(SeamCandidate(
            material=seam_mat,
            role=role,
            placement="interface",
            effectiveness=0.85,
            reason=f"Electrical conductivity mismatch 10^{abs(math.log10(cond_ratio)):.0f} - {seam_mat.name} provides targeted interface control",
            required_thickness=1.0,
            processing_compatibility=0.9
        ))
    
    # 5. Mechanical property mismatch
    modulus_ratio = base.youngs_modulus / max(partner.youngs_modulus, 1)
    if modulus_ratio > 10 or modulus_ratio < 0.1:
        candidates.append(SeamCandidate(
            material=get_material("bp"),
            role="compliance",
            placement="gradient",
            effectiveness=0.7,
            reason=f"Modulus mismatch {modulus_ratio:.1f}x - BP gradient layer provides mechanical transition",
            required_thickness=5.0,
            processing_compatibility=0.75
        ))
    
    # 6. Check fold sequence for late-stage degradation
    if len(fold_seq.folds) >= 5:
        late_tensile_drop = (fold_seq.folds[4].tensile_strength - fold_seq.folds[-1].tensile_strength) / fold_seq.folds[4].tensile_strength
        if late_tensile_drop > 0.15:
            candidates.append(SeamCandidate(
                material=get_material("mxene"),
                role="healing",
                placement="interface",
                effectiveness=0.9,
                reason=f"Late-fold tensile degradation {late_tensile_drop*100:.0f}% - MXene surface termination enables healing",
                required_thickness=2.0,
                processing_compatibility=0.7
            ))
    
    # Deduplicate and sort by effectiveness
    unique_candidates = []
    seen = set()
    for c in candidates:
        key = (c.material.name, c.role, c.placement)
        if key not in seen:
            seen.add(key)
            unique_candidates.append(c)
    
    unique_candidates.sort(key=lambda x: x.effectiveness, reverse=True)
    return unique_candidates


def evaluate_seam_integration(
    base: MaterialProperties,
    partner: MaterialProperties,
    seam: SeamCandidate,
    fold_seq: FoldSequence
) -> Dict:
    """Evaluate how a seam material integrates into the stack"""
    
    # Compute new effective properties with seam
    seam_mat = seam.material
    
    # Effective composite with seam (three-layer)
    v_base = 0.45
    v_partner = 0.45
    v_seam = 0.10
    
    # Tensile with seam
    tensile = (v_base * base.tensile_strength + 
               v_partner * partner.tensile_strength + 
               v_seam * seam_mat.tensile_strength)
    
    # Interface energy reduction
    base_interface = (base.youngs_modulus + partner.youngs_modulus) / 2 * 1e-3
    with_seam_interface = base_interface * 0.6  # Seam reduces interface energy
    
    # Thermal stability
    thermal_stability = 1.0 / (
        v_base * abs(base.thermal_expansion) + 
        v_partner * abs(partner.thermal_expansion) + 
        v_seam * abs(seam_mat.thermal_expansion)
    )
    
    # Processing compatibility
    proc_compat = (base.melting_point + partner.melting_point + seam_mat.melting_point) / 3
    proc_compat = min(proc_compat, 2000) / 2000  # Normalize
    
    return {
        "effective_tensile": tensile,
        "interface_energy_reduction": (base_interface - with_seam_interface) / base_interface * 100,
        "thermal_stability": thermal_stability,
        "processing_compatibility": proc_compat * seam.processing_compatibility,
        "total_thickness_nm": seam.required_thickness,
        "added_formation_energy": seam_mat.gluon_mass ** 2 * v_seam
    }


def print_seam_analysis(seams: List[SeamCandidate], base: MaterialProperties, partner: MaterialProperties, fold_seq: FoldSequence):
    """Print seam candidate analysis"""
    print(f"\n{'='*100}")
    print(f"SEAM MATERIAL ANALYSIS: {base.name} + {partner.name}")
    print(f"{'='*100}")
    
    if not seams:
        print("No seam materials required - direct interface is optimal")
        return
    
    for i, seam in enumerate(seams):
        eval_result = evaluate_seam_integration(base, partner, seam, fold_seq)
        print(f"\n{i+1}. {seam.material.name} ({seam.role.upper()}) - Effectiveness: {seam.effectiveness:.0%}")
        print(f"   Placement: {seam.placement}, Thickness: {seam.required_thickness:.1f} nm")
        print(f"   Reason: {seam.reason}")
        print(f"   Integration Results:")
        print(f"     Effective Tensile: {eval_result['effective_tensile']:.0f} MPa")
        print(f"     Interface Energy Reduction: {eval_result['interface_energy_reduction']:.1f}%")
        print(f"     Thermal Stability: {eval_result['thermal_stability']:.2f}")
        print(f"     Processing Compatibility: {eval_result['processing_compatibility']:.0%}")
        print(f"     Added Formation Energy: {eval_result['added_formation_energy']:.3f} eV")
    
    print(f"\n{'='*100}\n")


if __name__ == "__main__":
    from material_db import get_material
    from fold_evaluation import run_10_fold_evaluation
    
    base = get_material("graphene")
    partner = get_material("tbg")
    
    seq = run_10_fold_evaluation(base, partner)
    seams = detect_seam_candidates(base, partner, seq)
    print_seam_analysis(seams, base, partner, seq)
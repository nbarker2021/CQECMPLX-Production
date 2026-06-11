"""
Production Energy & Requirements Calculator
Computes exact energy and production needs for the metamaterial stack
"""
from dataclasses import dataclass
from typing import Dict, List, Optional
from material_db import MaterialProperties, get_material
from fold_evaluation import FoldSequence
from seam_detection import SeamCandidate
import math


@dataclass
class ProductionStep:
    """A single production step with energy requirements"""
    name: str
    description: str
    energy_per_cm2: float  # Joules/cm²
    time_seconds: float
    temperature_K: float
    pressure_atm: float
    equipment: List[str]
    yield_rate: float  # 0-1
    critical_parameters: Dict[str, float]


@dataclass
class ProductionPlan:
    """Complete production plan for the metamaterial"""
    base_material: MaterialProperties
    partner_material: MaterialProperties
    seam_materials: List[SeamCandidate]
    total_energy_joules_per_cm2: float
    total_time_hours: float
    max_temperature_K: float
    max_pressure_atm: float
    steps: List[ProductionStep]
    estimated_cost_usd_per_cm2: float
    scalability_score: float  # 0-1
    batch_size_cm2: float
    notes: List[str]


# Known production methods for each material
PRODUCTION_METHODS = {
    "graphene": {
        "cvd": ProductionStep(
            name="CVD Growth",
            description="Chemical vapor deposition on Cu/Ni foil",
            energy_per_cm2=5000,
            time_seconds=3600,
            temperature_K=1300,
            pressure_atm=1e-3,
            equipment=["CVD furnace", "Gas delivery", "Vacuum pump"],
            yield_rate=0.85,
            critical_parameters={"CH4_flow": 10, "H2_flow": 100, "growth_time": 30}
        ),
        "transfer": ProductionStep(
            name="PMMA Transfer",
            description="Polymer-assisted transfer to target substrate",
            energy_per_cm2=200,
            time_seconds=1800,
            temperature_K=450,
            pressure_atm=1,
            equipment=["Spin coater", "Etchant bath", "DI water rinse"],
            yield_rate=0.9,
            critical_parameters={"PMMA_thickness": 200, "etch_time": 60}
        ),
    },
    "hbn": {
        "cvd": ProductionStep(
            name="CVD Growth",
            description="CVD on Cu or Ni substrate",
            energy_per_cm2=6000,
            time_seconds=7200,
            temperature_K=1350,
            pressure_atm=1e-3,
            equipment=["CVD furnace", "B precursor", "N precursor"],
            yield_rate=0.8,
            critical_parameters={"B_flow": 5, "N_flow": 50}
        ),
        "transfer": ProductionStep(
            name="Transfer",
            description="Similar to graphene transfer",
            energy_per_cm2=200,
            time_seconds=1800,
            temperature_K=450,
            pressure_atm=1,
            equipment=["Spin coater", "Etchant", "DI water"],
            yield_rate=0.85,
            critical_parameters={}
        ),
    },
    "mos2": {
        "cvd": ProductionStep(
            name="CVD Growth",
            description="MoO3 + Sulfur CVD on SiO2/Sapphire",
            energy_per_cm2=3000,
            time_seconds=1800,
            temperature_K=1050,
            pressure_atm=1,
            equipment=["CVD furnace", "MoO3 source", "Sulfur source"],
            yield_rate=0.75,
            critical_parameters={"MoO3_temp": 750, "S_temp": 200}
        ),
    },
    "bp": {
        "mechanical_exfoliation": ProductionStep(
            name="Mechanical Exfoliation",
            description="Scotch tape method from bulk BP crystal",
            energy_per_cm2=50,
            time_seconds=600,
            temperature_K=300,
            pressure_atm=1,
            equipment=["Tape", "Microscope", "Substrate"],
            yield_rate=0.3,
            critical_parameters={"bulk_quality": 1.0}
        ),
        "vapor_transport": ProductionStep(
            name="Vapor Transport Growth",
            description="Chemical vapor transport for bulk crystals",
            energy_per_cm2=10000,
            time_seconds=86400,
            temperature_K=800,
            pressure_atm=1,
            equipment=["Tube furnace", "Transport agent", "Quartz tubes"],
            yield_rate=0.6,
            critical_parameters={"I2_concentration": 5, "gradient": 100}
        ),
    },
    "tbg": {
        "tear_stack": ProductionStep(
            name="Tear & Stack",
            description="Mechanical assembly with twist control",
            energy_per_cm2=100,
            time_seconds=1800,
            temperature_K=300,
            pressure_atm=1,
            equipment=["Micromanipulator", "Rotation stage", "Optical alignment"],
            yield_rate=0.4,
            critical_parameters={"angle_precision": 0.01, "alignment": 0.1}
        ),
        "rsp": ProductionStep(
            name="Rotated Sequential Growth",
            description="CVD growth with substrate rotation",
            energy_per_cm2=8000,
            time_seconds=7200,
            temperature_K=1300,
            pressure_atm=1e-3,
            equipment=["CVD with rotation", "Precise angle control"],
            yield_rate=0.5,
            critical_parameters={"rotation_speed": 0.1, "angle": 1.1}
        ),
    },
    "mxene": {
        "etching": ProductionStep(
            name="Selective Etching",
            description="HF/HCl etching of MAX phase",
            energy_per_cm2=500,
            time_seconds=86400,
            temperature_K=350,
            pressure_atm=1,
            equipment=["Etching bath", "Fume hood", "Centrifuge"],
            yield_rate=0.7,
            critical_parameters={"HF_conc": 50, "time_hours": 24}
        ),
        "delamination": ProductionStep(
            name="Delamination",
            description="Intercalation and sonication",
            energy_per_cm2=2000,
            time_seconds=3600,
            temperature_K=300,
            pressure_atm=1,
            equipment=["Sonicator", "Intercalant", "Centrifuge"],
            yield_rate=0.6,
            critical_parameters={"power": 100, "time": 60}
        ),
    },
    "sto": {
        "mbe": ProductionStep(
            name="Molecular Beam Epitaxy",
            description="MBE growth on single crystal substrates",
            energy_per_cm2=50000,
            time_seconds=14400,
            temperature_K=900,
            pressure_atm=1e-10,
            equipment=["MBE system", "Effusion cells", "RHEED"],
            yield_rate=0.9,
            critical_parameters={"Sr_flux": 1, "Ti_flux": 1, "O2_pressure": 1e-6}
        ),
        "pld": ProductionStep(
            name="Pulsed Laser Deposition",
            description="PLD from stoichiometric target",
            energy_per_cm2=10000,
            time_seconds=7200,
            temperature_K=850,
            pressure_atm=0.1,
            equipment=["PLD laser", "Target", "Vacuum chamber"],
            yield_rate=0.8,
            critical_parameters={"fluence": 2, "rep_rate": 10, "O2_pressure": 0.1}
        ),
    },
    "mowse2": {
        "cvd": ProductionStep(
            name="Co-CVD",
            description="Co-evaporation of Mo, W, Se",
            energy_per_cm2=4000,
            time_seconds=3600,
            temperature_K=1000,
            pressure_atm=1,
            equipment=["Multi-source CVD", "Se cracker", "Mo/W sources"],
            yield_rate=0.65,
            critical_parameters={"Mo_rate": 1, "W_rate": 1, "Se_pressure": 10}
        ),
    },
    "bp": {
        "exfoliation": ProductionStep(
            name="Mechanical Exfoliation",
            description="Scotch tape method from bulk BP crystal",
            energy_per_cm2=50,
            time_seconds=600,
            temperature_K=300,
            pressure_atm=1,
            equipment=["Tape", "Microscope", "Substrate"],
            yield_rate=0.3,
            critical_parameters={"bulk_quality": 1.0}
        ),
        "vapor_transport": ProductionStep(
            name="Vapor Transport Growth",
            description="Chemical vapor transport for bulk crystals",
            energy_per_cm2=10000,
            time_seconds=86400,
            temperature_K=800,
            pressure_atm=1,
            equipment=["Tube furnace", "Transport agent", "Quartz tubes"],
            yield_rate=0.6,
            critical_parameters={"I2_concentration": 5, "gradient": 100}
        ),
    },
    "mxene": {
        "etching": ProductionStep(
            name="Selective Etching",
            description="HF/HCl etching of MAX phase",
            energy_per_cm2=500,
            time_seconds=86400,
            temperature_K=350,
            pressure_atm=1,
            equipment=["Etching bath", "Fume hood", "Centrifuge"],
            yield_rate=0.7,
            critical_parameters={"HF_conc": 50, "time_hours": 24}
        ),
        "delamination": ProductionStep(
            name="Delamination",
            description="Intercalation and sonication",
            energy_per_cm2=2000,
            time_seconds=3600,
            temperature_K=300,
            pressure_atm=1,
            equipment=["Sonicator", "Intercalant", "Centrifuge"],
            yield_rate=0.6,
            critical_parameters={"power": 100, "time": 60}
        ),
    },
}


def get_production_method(material: MaterialProperties) -> ProductionStep:
    """Get the primary production method for a material"""
    # Use the production_key from the material database
    key = material.production_key
    
    if not key:
        # Fallback to name-based key generation
        key = material.name.lower().replace(" ", "").replace("@", "").replace("°", "").replace(".", "").replace("(", "").replace(")", "")
        
        # Normalize unicode subscripts to regular numbers
        subscript_map = {
            '₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4',
            '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9',
        }
        for sub, num in subscript_map.items():
            key = key.replace(sub, num)
    
    methods = PRODUCTION_METHODS.get(key, {})
    if not methods:
        # Default generic method
        return ProductionStep(
            name="Generic Synthesis",
            description=f"Standard synthesis for {material.name}",
            energy_per_cm2=10000,
            time_seconds=7200,
            temperature_K=material.melting_point * 0.5,
            pressure_atm=1,
            equipment=["Furnace", "Precursors", "Vacuum"],
            yield_rate=0.5,
            critical_parameters={}
        )
    
    # Return the method with highest yield
    return max(methods.values(), key=lambda m: m.yield_rate)


def compute_stack_energy(
    base: MaterialProperties,
    partner: MaterialProperties,
    folds: FoldSequence,
    seams: List[SeamCandidate],
    area_cm2: float = 1.0
) -> Dict:
    """Compute total energy for producing the full stack"""
    
    # Get individual production methods
    base_method = get_production_method(base)
    partner_method = get_production_method(partner)
    
    # Seam production methods
    seam_methods = [get_production_method(s.material) for s in seams]
    
    # Base energies
    base_energy = base_method.energy_per_cm2 / base_method.yield_rate
    partner_energy = partner_method.energy_per_cm2 / partner_method.yield_rate
    seam_energies = sum(m.energy_per_cm2 / m.yield_rate for m in seam_methods)
    
    # Assembly energy (stacking + alignment)
    num_layers = 2 + len(seams)
    assembly_energy = 500 * (num_layers - 1)  # Per interface
    
    # Annealing/post-processing
    max_temp = max(
        base_method.temperature_K,
        partner_method.temperature_K,
        *[m.temperature_K for m in seam_methods]
    )
    annealing_energy = 0.1 * max_temp * num_layers
    
    # Quality control (characterization)
    qc_energy = 200 * num_layers
    
    total = (base_energy + partner_energy + seam_energies + 
             assembly_energy + annealing_energy + qc_energy) * area_cm2
    
    return {
        "base_energy": base_energy * area_cm2,
        "partner_energy": partner_energy * area_cm2,
        "seam_energy": seam_energies * area_cm2,
        "assembly_energy": assembly_energy * area_cm2,
        "annealing_energy": annealing_energy * area_cm2,
        "qc_energy": qc_energy * area_cm2,
        "total_energy": total,
        "max_temperature": max_temp,
        "total_time": (base_method.time_seconds + partner_method.time_seconds + 
                       sum(m.time_seconds for m in seam_methods) + 3600) / 3600,  # hours
    }


def estimate_cost(energy_dict: Dict, area_cm2: float = 1.0) -> float:
    """Estimate production cost in USD"""
    # Energy cost: ~$0.10/kWh industrial
    energy_kwh = energy_dict["total_energy"] / 3.6e6
    energy_cost = energy_kwh * 0.10
    
    # Equipment amortization (rough)
    equipment_cost = 50 * area_cm2  # $/cm² for shared facility
    
    # Precursor materials
    precursor_cost = 20 * area_cm2
    
    # Labor/yield loss
    yield_factor = 1.5  # 50% overhead for yield < 100%
    
    total = (energy_cost + equipment_cost + precursor_cost) * yield_factor
    return total


def generate_production_plan(
    base: MaterialProperties,
    partner: MaterialProperties,
    folds: FoldSequence,
    seams: List[SeamCandidate],
    target_area_cm2: float = 1.0
) -> ProductionPlan:
    """Generate complete production plan"""
    
    # Compute energy breakdown
    energy = compute_stack_energy(base, partner, folds, seams, target_area_cm2)
    cost = estimate_cost(energy, target_area_cm2)
    
    # Build step list
    steps = []
    base_method = get_production_method(base)
    partner_method = get_production_method(partner)
    
    steps.append(base_method)
    steps.append(partner_method)
    
    for seam in seams:
        steps.append(get_production_method(seam.material))
    
    # Add assembly step
    steps.append(ProductionStep(
        name="Layer Assembly",
        description=f"Assemble {2 + len(seams)}-layer stack with alignment",
        energy_per_cm2=500,
        time_seconds=3600,
        temperature_K=300,
        pressure_atm=1,
        equipment=["Transfer stage", "Optical alignment", "Cleanroom"],
        yield_rate=0.9,
        critical_parameters={"alignment_accuracy": 0.1, "cleanliness": "ISO5"}
    ))
    
    # Add annealing
    max_temp = energy["max_temperature"]
    steps.append(ProductionStep(
        name="Post-Assembly Annealing",
        description="Thermal annealing for interface bonding",
        energy_per_cm2=0.1 * max_temp,
        time_seconds=3600,
        temperature_K=min(max_temp * 0.8, 800),
        pressure_atm=1e-3,
        equipment=["Annealing furnace", "Vacuum", "Inert gas"],
        yield_rate=0.95,
        critical_parameters={"ramp_rate": 10, "hold_time": 60}
    ))
    
    # Add QC
    steps.append(ProductionStep(
        name="Quality Control",
        description="Raman, AFM, Electrical, Optical characterization",
        energy_per_cm2=200,
        time_seconds=1800,
        temperature_K=300,
        pressure_atm=1,
        equipment=["Raman spectrometer", "AFM", "Probe station", "Ellipsometer"],
        yield_rate=1.0,
        critical_parameters={"resolution": 1, "speed": 10}
    ))
    
    # Scalability assessment
    max_yield = min(base_method.yield_rate, partner_method.yield_rate, *[get_production_method(s.material).yield_rate for s in seams])
    scalability = max_yield * 0.8  # Assembly reduces scalability
    
    return ProductionPlan(
        base_material=base,
        partner_material=partner,
        seam_materials=seams,
        total_energy_joules_per_cm2=energy["total_energy"] / target_area_cm2,
        total_time_hours=energy["total_time"],
        max_temperature_K=energy["max_temperature"],
        max_pressure_atm=max(s.pressure_atm for s in steps),
        steps=steps,
        estimated_cost_usd_per_cm2=cost / target_area_cm2,
        scalability_score=scalability,
        batch_size_cm2=target_area_cm2,
        notes=[
            f"Gluon mass target: {folds.final_gluon_mass:.3f} (formation energy: {folds.total_formation_energy:.2f} eV)",
            f"Target tensile: {folds.final_tensile:.0f} MPa, Composite: {folds.final_composite:.0f} MPa",
            f"Error walls encountered: {sum(folds.error_wall_summary.values())}",
            f"Seam layers required: {len(seams)}",
        ]
    )


def print_production_plan(plan: ProductionPlan):
    """Print formatted production plan"""
    print(f"\n{'='*100}")
    print(f"PRODUCTION PLAN: {plan.base_material.name}/{plan.partner_material.name} Metamaterial Stack")
    print(f"{'='*100}")
    print(f"Total Energy: {plan.total_energy_joules_per_cm2/1e6:.2f} MJ/cm²")
    print(f"Total Time: {plan.total_time_hours:.1f} hours")
    print(f"Max Temperature: {plan.max_temperature_K:.0f} K")
    print(f"Max Pressure: {plan.max_pressure_atm:.2e} atm")
    print(f"Estimated Cost: ${plan.estimated_cost_usd_per_cm2:.2f}/cm²")
    print(f"Scalability Score: {plan.scalability_score:.0%}")
    print(f"Batch Size: {plan.batch_size_cm2:.1f} cm²")
    
    print(f"\n{'Step':<5} {'Name':<25} {'Energy(J/cm²)':<15} {'Time(h)':<8} {'Temp(K)':<8} {'Pressure(atm)':<14} {'Yield':<7} {'Equipment'}")
    print(f"{'-'*100}")
    
    for i, step in enumerate(plan.steps):
        print(f"{i+1:<5} {step.name:<25} {step.energy_per_cm2:<15.0f} "
              f"{step.time_seconds/3600:<8.1f} {step.temperature_K:<8.0f} "
              f"{step.pressure_atm:<14.2e} {step.yield_rate:<7.0%} {', '.join(step.equipment[:3])}")
    
    print(f"\nNotes:")
    for note in plan.notes:
        print(f"  - {note}")
    
    print(f"{'='*100}\n")


if __name__ == "__main__":
    from material_db import get_material
    from fold_evaluation import run_10_fold_evaluation
    from seam_detection import detect_seam_candidates
    
    base = get_material("graphene")
    partner = get_material("hbn")
    
    folds = run_10_fold_evaluation(base, partner)
    seams = detect_seam_candidates(base, partner, folds)
    plan = generate_production_plan(base, partner, folds, seams)
    print_production_plan(plan)
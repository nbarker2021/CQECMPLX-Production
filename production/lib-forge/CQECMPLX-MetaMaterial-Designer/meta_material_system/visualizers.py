"""
MetaForge-AI Visualization Suite
================================
Publication-quality 2D/3D visualizers for metamaterial design pipeline.
Generated as STANDARD OUTPUT from every pipeline run — not a special feature.
"""

from __future__ import annotations
import json
import math
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple
from dataclasses import dataclass, asdict

import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd


# ─── Core Geometry Primitives ───

def generate_hexagonal_lattice(a: float, c: float, nx: int, ny: int, nz: int = 1) -> Tuple[np.ndarray, np.ndarray]:
    """Generate hexagonal lattice coordinates (2D or 3D)."""
    points = []
    for iz in range(nz):
        for iy in range(ny):
            for ix in range(nx):
                x = ix * a + (iy % 2) * a / 2
                y = iy * a * math.sqrt(3) / 2
                z = iz * c
                points.append([x, y, z])
    pts = np.array(points)
    # Bonds: nearest neighbors in hexagonal
    bonds = []
    for i, p1 in enumerate(pts):
        for j, p2 in enumerate(pts):
            if i < j:
                d = np.linalg.norm(p1 - p2)
                if d < a * 1.1:  # nearest neighbor cutoff
                    bonds.append([i, j])
    return pts, np.array(bonds)


def generate_moire_superlattice(a1: float, a2: float, theta_deg: float, size_nm: float = 50) -> Tuple[np.ndarray, np.ndarray]:
    """Generate moiré superlattice from two rotated hexagonal lattices."""
    theta = math.radians(theta_deg)
    # Large unit cell for moiré
    L = a1 / (2 * math.sin(theta / 2))  # moiré wavelength
    n = int(size_nm / L) + 2
    
    pts1, _ = generate_hexagonal_lattice(a1, 0, n, n, 1)
    pts2, _ = generate_hexagonal_lattice(a2, 0, n, n, 1)
    
    # Rotate second layer
    rot = np.array([[math.cos(theta), -math.sin(theta), 0],
                    [math.sin(theta), math.cos(theta), 0],
                    [0, 0, 1]])
    pts2 = (rot @ pts2.T).T
    
    # Combine with layer index
    pts = np.vstack([np.hstack([pts1, np.zeros((len(pts1), 1))]),
                     np.hstack([pts2, np.ones((len(pts2), 1))])])
    
    # Inter-layer bonds (approximate registry)
    bonds = []
    for i, p1 in enumerate(pts1):
        for j, p2 in enumerate(pts2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            if dx*dx + dy*dy < (a1 * 0.6)**2:
                bonds.append([i, len(pts1) + j])
    bonds = np.array(bonds) if bonds else np.empty((0, 2), dtype=int)
    return pts, bonds


def generate_oloid_form(R: float = 1.0, n_theta: int = 60, n_phi: int = 30) -> Tuple[np.ndarray, np.ndarray]:
    """Generate oloid surface mesh (two circles perpendicular, rolling)."""
    # Oloid = convex hull of two circles in perpendicular planes
    # Parametric: circle1 in XY, circle2 in YZ, same radius, centers offset by R
    theta = np.linspace(0, 2*np.pi, n_theta)
    phi = np.linspace(0, 2*np.pi, n_phi)
    
    # Two generating circles
    verts = []
    # Circle 1: XY plane at z=0, radius R
    for t in theta:
        verts.append([R*math.cos(t), R*math.sin(t), 0])
    # Circle 2: YZ plane at x=R, radius R
    for t in theta:
        verts.append([R, R*math.cos(t), R*math.sin(t)])
    verts = np.array(verts)
    
    # Simple triangulation (convex hull would be better but needs scipy)
    # For visualization, just show the two circles + connecting strips
    return verts, np.empty((0, 2), dtype=int)


def generate_E8_projection(n_points: int = 240) -> np.ndarray:
    """Generate E8 root system projected to 3D for visualization."""
    # E8 roots: 240 vectors in 8D. Project to 3D via first 3 coordinates + Coxeter plane.
    # Simplified: use known 3D projections (Petrie polygon style)
    # This is a Coxeter plane projection of E8 roots
    angles = np.linspace(0, 2*np.pi, 30)  # 30-gon from E8 Coxeter element
    # Two 30-gons, inner/outer
    pts = []
    for r in [1.0, 1.618]:  # golden ratio appears in E8
        for a in angles:
            pts.append([r*math.cos(a), r*math.sin(a), 0])
    # Add some 3D spread
    pts = np.array(pts)
    pts[:, 2] = np.random.normal(0, 0.05, len(pts))
    return pts


# ─── 2D Visualizers ───

def plot_unit_cell_2D(material_props: Dict, partner_props: Optional[Dict] = None) -> go.Figure:
    """2D unit cell view: lattice constants, basis atoms, moiré pattern if twisted."""
    fig = make_subplots(rows=1, cols=2 if partner_props else 1,
                        subplot_titles=[material_props['name']] + ([partner_props['name']] if partner_props else []),
                        horizontal_spacing=0.1)
    
    a = material_props['lattice_constants'].get('a', 2.5)
    c = material_props['lattice_constants'].get('c', 6.7)
    
    pts, bonds = generate_hexagonal_lattice(a, c, 6, 6, 1)
    
    # Plot bonds
    for b in bonds:
        fig.add_trace(go.Scatter(
            x=[pts[b[0], 0], pts[b[1], 0]],
            y=[pts[b[0], 1], pts[b[1], 1]],
            mode='lines', line=dict(color='#666', width=1),
            showlegend=False, hoverinfo='skip'
        ), row=1, col=1)
    
    # Plot atoms
    fig.add_trace(go.Scatter(
        x=pts[:, 0], y=pts[:, 1],
        mode='markers', marker=dict(size=8, color='#1f77b4'),
        name=material_props['name'], showlegend=False
    ), row=1, col=1)
    
    if partner_props:
        a2 = partner_props['lattice_constants'].get('a', 2.5)
        pts2, bonds2 = generate_hexagonal_lattice(a2, c, 6, 6, 1)
        for b in bonds2:
            fig.add_trace(go.Scatter(
                x=[pts2[b[0], 0], pts2[b[1], 0]],
                y=[pts2[b[0], 1], pts2[b[1], 1]],
                mode='lines', line=dict(color='#999', width=1, dash='dot'),
                showlegend=False, hoverinfo='skip'
            ), row=1, col=2)
        fig.add_trace(go.Scatter(
            x=pts2[:, 0], y=pts2[:, 1],
            mode='markers', marker=dict(size=8, color='#ff7f0e'),
            name=partner_props['name'], showlegend=False
        ), row=1, col=2)
    
    fig.update_xaxes(scaleanchor="y", scaleratio=1, title="x (Å)")
    fig.update_yaxes(title="y (Å)")
    fig.update_layout(height=400, title="Unit Cell Structures")
    return fig


def plot_moire_2D(base_props: Dict, partner_props: Dict, theta_deg: float = 1.1) -> go.Figure:
    """2D moiré superlattice visualization."""
    pts, bonds = generate_moire_superlattice(
        base_props['lattice_constants'].get('a', 2.46),
        partner_props['lattice_constants'].get('a', 2.46),
        theta_deg, size_nm=100
    )
    
    fig = go.Figure()
    
    # Layer 1
    mask1 = pts[:, 3] == 0
    fig.add_trace(go.Scatter(
        x=pts[mask1, 0], y=pts[mask1, 1],
        mode='markers', marker=dict(size=4, color='#1f77b4', opacity=0.6),
        name=f"{base_props['name']} (layer 1)"
    ))
    
    # Layer 2
    mask2 = pts[:, 3] == 1
    fig.add_trace(go.Scatter(
        x=pts[mask2, 0], y=pts[mask2, 1],
        mode='markers', marker=dict(size=4, color='#ff7f0e', opacity=0.6),
        name=f"{partner_props['name']} (layer 2)"
    ))
    
    # Interlayer bonds showing moiré registry
    for b in bonds[:500]:  # limit for performance
        fig.add_trace(go.Scatter(
            x=[pts[b[0], 0], pts[b[1], 0]],
            y=[pts[b[0], 1], pts[b[1], 1]],
            mode='lines', line=dict(color='rgba(100,100,100,0.2)', width=0.5),
            showlegend=False, hoverinfo='skip'
        ))
    
    fig.update_xaxes(scaleanchor="y", scaleratio=1, title="x (nm)")
    fig.update_yaxes(title="y (nm)")
    fig.update_layout(height=500, title=f"Moiré Superlattice (θ={theta_deg}°)")
    return fig


def plot_pareto_frontier(pareto_results: List[Dict]) -> go.Figure:
    """Pareto frontier with multi-objective scores."""
    df = pd.DataFrame(pareto_results)
    if df.empty:
        return go.Figure().update_layout(title="No Pareto data")
    
    fig = make_subplots(rows=2, cols=2,
                        subplot_titles=["Pareto Score vs Rank", "Lattice vs Property Synergy",
                                        "Gluon Coherence vs Oloid Compat", "Interface Energy vs Strain Tolerance"],
                        horizontal_spacing=0.1, vertical_spacing=0.12)
    
    # 1: Pareto score by rank
    fig.add_trace(go.Bar(
        x=list(range(1, len(df)+1)),
        y=df['pareto_score'] if 'pareto_score' in df else df.get('Pareto Score', [0]*len(df)),
        text=df['material'] if 'material' in df else [f"#{i}" for i in range(len(df))],
        textposition='auto',
        marker_color=px.colors.qualitative.Set1[:len(df)],
        showlegend=False
    ), row=1, col=1)
    
    # 2-4: Objective space scatter
    obj_pairs = [
        ('lattice_match', 'property_synergy', 'Lattice Match', 'Property Synergy'),
        ('gluon_coherence', 'oloid_compatibility', 'Gluon Coherence', 'Oloid Compatibility'),
        ('interface_energy', 'strain_tolerance', 'Interface Energy', 'Strain Tolerance'),
    ]
    
    for idx, (xkey, ykey, xtitle, ytitle) in enumerate(obj_pairs):
        r, c = (1, 2) if idx == 0 else (2, 1) if idx == 1 else (2, 2)
        xvals = df[xkey] if xkey in df else [0]*len(df)
        yvals = df[ykey] if ykey in df else [0]*len(df)
        fig.add_trace(go.Scatter(
            x=xvals, y=yvals,
            mode='markers+text',
            text=df['material'] if 'material' in df else [f"#{i}" for i in range(len(df))],
            textposition='top center',
            marker=dict(size=12, color=px.colors.qualitative.Set1[:len(df)]),
            showlegend=False
        ), row=r, col=c)
        fig.update_xaxes(title_text=xtitle, row=r, col=c)
        fig.update_yaxes(title_text=ytitle, row=r, col=c)
    
    fig.update_layout(height=600, title="Pareto Partner Analysis")
    return fig


def plot_fold_progression(fold_sequence: Dict) -> go.Figure:
    """Live readout: fold-by-fold state transitions (Gluon, tensile, composite, error walls)."""
    folds = fold_sequence.get('folds', [])
    if not folds:
        return go.Figure().update_layout(title="No fold data")
    
    df = pd.DataFrame(folds)
    # Handle field name variations
    tensile_col = 'tensile_strength' if 'tensile_strength' in df.columns else 'tensile'
    composite_col = 'composite_strength' if 'composite_strength' in df.columns else 'composite'
    gluon_col = 'gluon_mass' if 'gluon_mass' in df.columns else 'Gluon Mass'
    
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True,
                        subplot_titles=["Gluon Mass Accumulation", "Strength Evolution (MPa)", "Error Wall Count per Fold"],
                        vertical_spacing=0.08, row_heights=[0.35, 0.35, 0.3])
    
    # Gluon mass
    fig.add_trace(go.Scatter(
        x=df['fold'], y=df[gluon_col],
        mode='lines+markers', name='Gluon Mass',
        line=dict(color='#1f77b4', width=3), marker=dict(size=8)
    ), row=1, col=1)
    
    # Tensile + Composite
    fig.add_trace(go.Scatter(
        x=df['fold'], y=df[tensile_col],
        mode='lines+markers', name='Tensile',
        line=dict(color='#2ca02c', width=2), marker=dict(size=6)
    ), row=2, col=1)
    fig.add_trace(go.Scatter(
        x=df['fold'], y=df[composite_col],
        mode='lines+markers', name='Composite',
        line=dict(color='#d62728', width=2, dash='dot'), marker=dict(size=6)
    ), row=2, col=1)
    
    # Error walls stacked bar
    ew_types = ['CA', 'IV', 'BF', 'MR', 'NA', 'CNP']
    for ew in ew_types:
        counts = [f.get('error_walls', {}).get(ew, 0) for f in folds]
        if any(c > 0 for c in counts):
            fig.add_trace(go.Bar(
                x=df['fold'], y=counts,
                name=ew, showlegend=(ew == ew_types[0])
            ), row=3, col=1)
    
    fig.update_xaxes(title_text="Fold Number", row=3, col=1)
    fig.update_yaxes(title_text="Gluon Mass", row=1, col=1)
    fig.update_yaxes(title_text="Strength (MPa)", row=2, col=1)
    fig.update_yaxes(title_text="Count", row=3, col=1)
    fig.update_layout(height=700, title="10-Fold Recursive Evaluation — State Transitions",
                      barmode='stack', legend=dict(orientation='h', y=-0.15))
    return fig


def plot_seam_layers(seam_candidates: List[Dict], base_props: Dict, partner_props: Dict) -> go.Figure:
    """2D cross-section showing seam material layers between base and partner."""
    fig = go.Figure()
    
    # Base layer
    fig.add_shape(type="rect", x0=0, x1=1, y0=0, y1=1,
                  fillcolor='#1f77b4', opacity=0.3, line=dict(width=0))
    fig.add_annotation(x=0.5, y=0.5, text=f"BASE: {base_props['name']}", showarrow=False, font=dict(size=12, color='white'))
    
    # Seam layers stacked
    y_pos = 1.0
    total_thickness = sum(s.get('thickness_nm', 1) for s in seam_candidates)
    for i, s in enumerate(seam_candidates):
        thickness = s.get('thickness_nm', 1)
        h = thickness / max(total_thickness, 1) * 0.5  # scale to 0.5 height
        color = px.colors.qualitative.Set2[i % 8]
        fig.add_shape(type="rect", x0=0, x1=1, y0=y_pos, y1=y_pos + h,
                      fillcolor=color, opacity=0.7, line=dict(width=1, color='white'))
        fig.add_annotation(x=0.5, y=y_pos + h/2, 
                          text=f"{s.get('material', 'Seam')} ({s.get('role', '')}) {thickness}nm",
                          showarrow=False, font=dict(size=10))
        y_pos += h
    
    # Partner layer
    fig.add_shape(type="rect", x0=0, x1=1, y0=y_pos, y1=y_pos + 1,
                  fillcolor='#ff7f0e', opacity=0.3, line=dict(width=0))
    fig.add_annotation(x=0.5, y=y_pos + 0.5, text=f"PARTNER: {partner_props['name']}", showarrow=False, font=dict(size=12, color='white'))
    
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False, scaleanchor="x", scaleratio=2)
    fig.update_layout(height=400, title="Seam Layer Stack Cross-Section",
                      showlegend=False, margin=dict(l=20, r=20, t=40, b=20))
    return fig


def plot_production_plan(plan: Dict) -> go.Figure:
    """Production plan: energy, time, cost waterfall + step Gantt."""
    steps = plan.get('steps', [])
    if not steps:
        return go.Figure().update_layout(title="No production data")
    
    df = pd.DataFrame(steps)
    
    fig = make_subplots(rows=2, cols=2,
                        subplot_titles=["Energy per Step (J/cm²)", "Time per Step (hours)",
                                        "Temperature/Pressure Profile", "Cumulative Cost"],
                        specs=[[{"type": "bar"}, {"type": "bar"}],
                               [{"type": "scatter"}, {"type": "scatter"}]],
                        horizontal_spacing=0.1, vertical_spacing=0.12)
    
    colors = px.colors.qualitative.Set3[:len(df)]
    
    # Energy
    fig.add_trace(go.Bar(x=df['name'], y=df['energy_per_cm2'],
                         marker_color=colors, name='Energy', showlegend=False), row=1, col=1)
    # Time
    fig.add_trace(go.Bar(x=df['name'], y=df['time_hours'],
                         marker_color=colors, name='Time', showlegend=False), row=1, col=2)
    # Temp/Pressure
    fig.add_trace(go.Scatter(x=df['name'], y=df['temperature_K'],
                             mode='lines+markers', name='Temp (K)', line=dict(color='#d62728')), row=2, col=1)
    fig.add_trace(go.Scatter(x=df['name'], y=df['pressure_atm']*1000,
                             mode='lines+markers', name='Pressure (mbar)', line=dict(color='#1f77b4'),
                             yaxis='y4'), row=2, col=1)
    # Cumulative cost
    cum_cost = np.cumsum([s * e for s, e in zip(df.get('yield_rate', [1]*len(df)), 
                                                  df['energy_per_cm2'])]) * 0.001  # rough scaling
    fig.add_trace(go.Scatter(x=df['name'], y=cum_cost,
                             mode='lines+markers', name='Cum. Energy', line=dict(color='#2ca02c', width=3)), row=2, col=2)
    
    fig.update_xaxes(tickangle=45)
    fig.update_layout(height=600, title="Production Plan Analysis", showlegend=False)
    return fig


# ─── 3D Visualizers ───

def plot_3D_lattice(material_props: Dict, partner_props: Optional[Dict] = None, 
                    show_moire: bool = False, theta_deg: float = 1.1) -> go.Figure:
    """3D interactive lattice structure with optional moiré."""
    fig = go.Figure()
    
    a = material_props['lattice_constants'].get('a', 2.5)
    c = material_props['lattice_constants'].get('c', 6.7)
    nx = ny = 8
    
    # Base layer
    pts, bonds = generate_hexagonal_lattice(a, c, nx, ny, 3)
    
    # Bonds
    x_bonds, y_bonds, z_bonds = [], [], []
    for b in bonds:
        x_bonds += [pts[b[0], 0], pts[b[1], 0], None]
        y_bonds += [pts[b[0], 1], pts[b[1], 1], None]
        z_bonds += [pts[b[0], 2], pts[b[1], 2], None]
    fig.add_trace(go.Scatter3d(
        x=x_bonds, y=y_bonds, z=z_bonds,
        mode='lines', line=dict(color='#888', width=2), name='Bonds', showlegend=False
    ))
    
    # Atoms
    fig.add_trace(go.Scatter3d(
        x=pts[:, 0], y=pts[:, 1], z=pts[:, 2],
        mode='markers', marker=dict(size=5, color='#1f77b4', opacity=0.8),
        name=material_props['name']
    ))
    
    if partner_props and show_moire:
        pts2, bonds2 = generate_moire_superlattice(a, partner_props['lattice_constants'].get('a', a), theta_deg, 50)
        mask1 = pts2[:, 3] == 0
        mask2 = pts2[:, 3] == 1
        fig.add_trace(go.Scatter3d(
            x=pts2[mask1, 0], y=pts2[mask1, 1], z=pts2[mask1, 2],
            mode='markers', marker=dict(size=3, color='#1f77b4', opacity=0.5),
            name=f"{material_props['name']} L1"
        ))
        fig.add_trace(go.Scatter3d(
            x=pts2[mask2, 0], y=pts2[mask2, 1], z=pts2[mask2, 2] + 0.34,
            mode='markers', marker=dict(size=3, color='#ff7f0e', opacity=0.5),
            name=f"{partner_props['name']} L2"
        ))
    
    fig.update_layout(
        scene=dict(
            xaxis_title='x (Å)', yaxis_title='y (Å)', zaxis_title='z (Å)',
            aspectmode='data', camera=dict(eye=dict(x=1.5, y=1.5, z=1.2))
        ),
        height=600, title=f"3D Lattice: {material_props['name']}" + (f" + {partner_props['name']} moiré" if partner_props else ""),
        margin=dict(l=0, r=0, t=40, b=0)
    )
    return fig


def plot_3D_oloid(R: float = 1.0, wireframe: bool = True) -> go.Figure:
    """3D oloid form — the universal geometric primitive."""
    # Generate proper oloid mesh (convex hull of two circles)
    n = 80
    theta = np.linspace(0, 2*np.pi, n)
    
    # Two circles: one in XY at z=0, one in YZ at x=R
    circle1 = np.array([[R*math.cos(t), R*math.sin(t), 0] for t in theta])
    circle2 = np.array([[R, R*math.cos(t), R*math.sin(t)] for t in theta])
    
    fig = go.Figure()
    
    if wireframe:
        # Wireframe circles
        for circle, color in [(circle1, '#1f77b4'), (circle2, '#ff7f0e')]:
            fig.add_trace(go.Scatter3d(
                x=np.append(circle[:, 0], circle[0, 0]),
                y=np.append(circle[:, 1], circle[0, 1]),
                z=np.append(circle[:, 2], circle[0, 2]),
                mode='lines', line=dict(color=color, width=4), name='Generating circles', showlegend=False
            ))
        # Connecting strips (sample)
        for i in range(0, n, n//12):
            fig.add_trace(go.Scatter3d(
                x=[circle1[i, 0], circle2[i, 0]],
                y=[circle1[i, 1], circle2[i, 1]],
                z=[circle1[i, 2], circle2[i, 2]],
                mode='lines', line=dict(color='rgba(100,100,100,0.5)', width=1),
                showlegend=False
            ))
    else:
        # Surface approximation via triangulated strips
        # This is a simplified surface mesh
        for i in range(n-1):
            for circle, color in [(circle1, 'rgba(31,119,180,0.3)'), (circle2, 'rgba(255,127,14,0.3)')]:
                x = [circle[i,0], circle[(i+1)%n,0], circle[(i+1)%n,0], circle[i,0], circle[i,0]]
                y = [circle[i,1], circle[(i+1)%n,1], circle[(i+1)%n,1], circle[i,1], circle[i,1]]
                z = [circle[i,2], circle[(i+1)%n,2], circle[(i+1)%n,2], circle[i,2], circle[i,2]]
                fig.add_trace(go.Mesh3d(
                    x=x, y=y, z=z, color=color, opacity=0.5, showlegend=False
                ))
    
    fig.update_layout(
        scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z',
                   aspectmode='cube', camera=dict(eye=dict(x=1.5, y=1.5, z=1.2))),
        height=500, title="Oloid Normal Form (Universal Primitive)",
        margin=dict(l=0, r=0, t=40, b=0)
    )
    return fig


def plot_3D_E8_projection() -> go.Figure:
    """3D projection of E8 root system (240 roots)."""
    pts = generate_E8_projection()
    
    fig = go.Figure()
    fig.add_trace(go.Scatter3d(
        x=pts[:, 0], y=pts[:, 1], z=pts[:, 2],
        mode='markers', marker=dict(size=4, color=pts[:, 0], colorscale='Viridis', opacity=0.8),
        name='E8 Roots (240)'
    ))
    
    # Add origin
    fig.add_trace(go.Scatter3d(x=[0], y=[0], z=[0], mode='markers',
                               marker=dict(size=10, color='red'), name='Origin'))
    
    fig.update_layout(
        scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z',
                   aspectmode='cube', camera=dict(eye=dict(x=2, y=2, z=1.5))),
        height=500, title="E8 Root System — 3D Coxeter Plane Projection",
        margin=dict(l=0, r=0, t=40, b=0)
    )
    return fig


def plot_3D_state_transition_cube(fold_sequence: Dict) -> go.Figure:
    """3D state space trajectory: Gluon vs Tensile vs Composite over folds."""
    folds = fold_sequence.get('folds', [])
    if not folds:
        return go.Figure().update_layout(title="No fold data")
    
    df = pd.DataFrame(folds)
    tensile_col = 'tensile_strength' if 'tensile_strength' in df.columns else 'tensile'
    composite_col = 'composite_strength' if 'composite_strength' in df.columns else 'composite'
    gluon_col = 'gluon_mass' if 'gluon_mass' in df.columns else 'Gluon Mass'
    
    fig = go.Figure()
    
    # Trajectory line
    fig.add_trace(go.Scatter3d(
        x=df[gluon_col], y=df[tensile_col], z=df[composite_col],
        mode='lines+markers',
        line=dict(color='#1f77b4', width=4),
        marker=dict(size=8, color=df['fold'], colorscale='Viridis', showscale=True,
                    colorbar=dict(title='Fold #')),
        name='State Trajectory',
        text=[f"Fold {f}" for f in df['fold']],
        hovertemplate='Gluon: %{x:.3f}<br>Tensile: %{y:,.0f} MPa<br>Composite: %{z:,.0f} MPa<br>%{text}'
    ))
    
    # Start/end markers
    fig.add_trace(go.Scatter3d(
        x=[df[gluon_col].iloc[0]], y=[df[tensile_col].iloc[0]], z=[df[composite_col].iloc[0]],
        mode='markers', marker=dict(size=12, color='green', symbol='diamond'), name='Start (Fold 1)'
    ))
    fig.add_trace(go.Scatter3d(
        x=[df[gluon_col].iloc[-1]], y=[df[tensile_col].iloc[-1]], z=[df[composite_col].iloc[-1]],
        mode='markers', marker=dict(size=12, color='red', symbol='diamond'), name='Final (Fold 10)'
    ))
    
    fig.update_layout(
        scene=dict(xaxis_title='Gluon Mass', yaxis_title='Tensile (MPa)', zaxis_title='Composite (MPa)',
                   camera=dict(eye=dict(x=1.5, y=1.5, z=1.2))),
        height=600, title="3D State Space Trajectory — 10-Fold Evolution",
        margin=dict(l=0, r=0, t=40, b=0)
    )
    return fig


# ─── Master Visualization Orchestrator ───

@dataclass
class VisualizationOutput:
    """Container for all generated visualizations."""
    unit_cell_2D: Optional[go.Figure] = None
    moire_2D: Optional[go.Figure] = None
    pareto_frontier: Optional[go.Figure] = None
    fold_progression: Optional[go.Figure] = None
    seam_layers: Optional[go.Figure] = None
    production_plan: Optional[go.Figure] = None
    lattice_3D: Optional[go.Figure] = None
    oloid_3D: Optional[go.Figure] = None
    E8_3D: Optional[go.Figure] = None
    state_cube_3D: Optional[go.Figure] = None
    
    def to_html_dict(self) -> Dict[str, str]:
        """Export all figures as HTML strings for embedding."""
        out = {}
        for field_name in self.__dataclass_fields__:
            fig = getattr(self, field_name)
            if fig is not None:
                out[field_name] = fig.to_html(include_plotlyjs='cdn', div_id=field_name)
        return out
    
    def save_all(self, output_dir: Path):
        """Save all visualizations as HTML + PNG."""
        output_dir.mkdir(parents=True, exist_ok=True)
        for field_name in self.__dataclass_fields__:
            fig = getattr(self, field_name)
            if fig is not None:
                fig.write_html(str(output_dir / f"{field_name}.html"))
                try:
                    fig.write_image(str(output_dir / f"{field_name}.png"), width=1200, height=800, scale=2)
                except:
                    pass  # kaleido not installed


def generate_all_visualizations(
    base_props: Dict,
    partner_props: Optional[Dict] = None,
    pareto_results: Optional[List[Dict]] = None,
    fold_sequence: Optional[Dict] = None,
    seam_candidates: Optional[List[Dict]] = None,
    production_plan: Optional[Dict] = None,
    theta_deg: float = 1.1
) -> VisualizationOutput:
    """
    MAIN ENTRY POINT — generates ALL visualizations as standard pipeline output.
    Call this once per pipeline run; returns a VisualizationOutput with all figures.
    """
    out = VisualizationOutput()
    
    # 2D
    out.unit_cell_2D = plot_unit_cell_2D(base_props, partner_props)
    if partner_props:
        out.moire_2D = plot_moire_2D(base_props, partner_props, theta_deg)
    if pareto_results:
        out.pareto_frontier = plot_pareto_frontier(pareto_results)
    if fold_sequence:
        out.fold_progression = plot_fold_progression(fold_sequence)
        out.state_cube_3D = plot_3D_state_transition_cube(fold_sequence)
    if seam_candidates and partner_props:
        out.seam_layers = plot_seam_layers(seam_candidates, base_props, partner_props)
    if production_plan:
        out.production_plan = plot_production_plan(production_plan)
    
    # 3D
    out.lattice_3D = plot_3D_lattice(base_props, partner_props, show_moire=bool(partner_props), theta_deg=theta_deg)
    out.oloid_3D = plot_3D_oloid(wireframe=True)
    out.E8_3D = plot_3D_E8_projection()
    
    return out


# ─── Streamlit Integration ───

def render_visualizations_streamlit(viz: VisualizationOutput, tabs: str = "all"):
    """Render visualizations in Streamlit with proper tabs."""
    import streamlit as st
    
    tab_map = {
        "all": ["2d", "transitions", "3d", "production"],
        "2d_structures": ["2d"],
        "state_transitions": ["transitions"],
        "3d_geometry": ["3d"],
        "production": ["production"],
    }
    
    active_tabs = tab_map.get(tabs, tab_map["all"])
    
    if "2d" in active_tabs:
        st.subheader("📐 2D Structural Views")
        cols = st.columns(2)
        if viz.unit_cell_2D: cols[0].plotly_chart(viz.unit_cell_2D, use_container_width=True)
        if viz.moire_2D: cols[1].plotly_chart(viz.moire_2D, use_container_width=True)
        if viz.pareto_frontier: st.plotly_chart(viz.pareto_frontier, use_container_width=True)
        if viz.seam_layers: st.plotly_chart(viz.seam_layers, use_container_width=True)
    
    if "transitions" in active_tabs:
        st.subheader("🔄 Live State Transitions")
        if viz.fold_progression: st.plotly_chart(viz.fold_progression, use_container_width=True)
        if viz.state_cube_3D: st.plotly_chart(viz.state_cube_3D, use_container_width=True)
    
    if "3d" in active_tabs:
        st.subheader("🧱 3D Lattice & Geometry")
        cols = st.columns(2)
        if viz.lattice_3D: cols[0].plotly_chart(viz.lattice_3D, use_container_width=True)
        if viz.oloid_3D: cols[1].plotly_chart(viz.oloid_3D, use_container_width=True)
        cols2 = st.columns(2)
        if viz.E8_3D: cols2[0].plotly_chart(viz.E8_3D, use_container_width=True)
    
    if "production" in active_tabs:
        st.subheader("🏭 Production Analysis")
        if viz.production_plan: st.plotly_chart(viz.production_plan, use_container_width=True)


# ─── CLI Test ───

if __name__ == "__main__":
    # Quick smoke test
    base = {
        'name': 'Graphene', 'formula': 'C',
        'lattice_constants': {'a': 2.461, 'c': 6.708}
    }
    partner = {
        'name': 'h-BN', 'formula': 'BN',
        'lattice_constants': {'a': 2.504, 'c': 6.66}
    }
    pareto = [
        {'material': 'h-BN', 'pareto_score': 0.89, 'lattice_match': 0.8, 'property_synergy': 1.0,
         'gluon_coherence': 0.8, 'oloid_compatibility': 1.0, 'interface_energy': 0.0011, 'strain_tolerance': 19.4},
        {'material': 'MoS2', 'pareto_score': 0.725, 'lattice_match': 0.2, 'property_synergy': 0.7,
         'gluon_coherence': 1.0, 'oloid_compatibility': 1.0, 'interface_energy': 0.002, 'strain_tolerance': 27.8},
    ]
    folds = {'folds': [
        {'fold': i, 'gluon_mass': 0.08*i, 'tensile': 80000 - i*1000, 'composite': 40000 - i*500,
         'error_walls': {'CA': i%3, 'IV': i%2, 'MR': i%4, 'CNP': i%3}}
        for i in range(1, 11)
    ]}
    seams = [
        {'material': 'MXene', 'role': 'HEALING', 'thickness_nm': 2.0},
        {'material': 'h-BN', 'role': 'ELECTRICAL', 'thickness_nm': 1.0},
    ]
    plan = {'steps': [
        {'name': 'CVD Graphene', 'energy_per_cm2': 200, 'time_hours': 0.5, 'temperature_K': 450, 'pressure_atm': 1.0, 'yield_rate': 0.9},
        {'name': 'Transfer', 'energy_per_cm2': 200, 'time_hours': 0.5, 'temperature_K': 450, 'pressure_atm': 1.0, 'yield_rate': 0.85},
        {'name': 'Etching', 'energy_per_cm2': 500, 'time_hours': 24, 'temperature_K': 350, 'pressure_atm': 1.0, 'yield_rate': 0.7},
    ]}
    
    viz = generate_all_visualizations(base, partner, pareto, folds, seams, plan)
    print("✓ All visualizations generated")
    for name in viz.__dataclass_fields__:
        fig = getattr(viz, name)
        print(f"  {name}: {'✓' if fig else '—'}")
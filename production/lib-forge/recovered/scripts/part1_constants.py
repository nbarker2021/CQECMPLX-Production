#!/usr/bin/env python3
"""Constants for paper generation"""
from datetime import datetime
from pathlib import Path

VERIFIED_THEOREMS = {
    "T3": "Chart <-> J3(O) bijection: phi(L,C,R)=diag(L,C,R) structure-preserving",
    "T4": "n=3 SU(3) closure: M3 = 1/3(T12+T13+T23) exact over Q",
    "T5": "M3^2 = M3 exactly (idempotent, rank-1, eigenvalues {1,0,0})",
    "T6": "Trace-1 block = Trace-2 block at n=3 (cross-mass 9/8)",
    "T7": "8x8 transition entries in {0,1/4,1/2}; row sums = 1 exact",
    "T_BIJECTIVE": "Side-flip = (1 3) on J3(O) shell=2; fixed point (1,0,1)",
    "T_CORRECTION": "Correction = C and not R fires at D4 axes {2,0},{3,1}",
    "T_TRIALITY": "D4/J3 triality: 4 axes x 2 sheets = 8 states; 2+6 VOA split; Z4 periods",
    "T_WRAP": "Local rollout: all 8 states -> Lie conjugate in <=3 S3 steps",
    "LATTICE_CHAIN": "D1->D3->D4->D24->D72; Leech minimal shell = 196560 vectors",
    "VOA_2_6": "VOA sector: Z(q) = 2q^0 + 6q^5; 2 weight-0 vacua, 6 weight-5 excited",
    "T_BRIDGE": "Rule30 = Rule90 + (C and not R); Bridge Gluon = lucas_bit + correction",
    "T_HAMILTONIAN": "Hamiltonian Gluon = C_accumulated as time; MORSR Z4 cycle",
    "T10_MASTER": "C_T10 = sum C_i; status = pass_with_open_lifts",
    "T_ADMISSION": "Admission Gluon = Gluon mass filter at K=9; T10 = trust anchor",
    "T_CA_PREDICTION": "64/256 ECAs close at n=3; correction Gluon = local correction field",
    "T_QUARK_FACE": "6 faces = 6 excited VOA states; 2 vacua = leptons; SU(3) Z3 cycle",
    "T_GR_CURVATURE": "Curvature Gluon = Riemann from torsion; G_uv = kT_uv",
    "T_HIGGS": "Higgs Gluon = Gluon mass C_accumulated",
    "T_EDGE": "Edge residual Gluon = correction at K=10^k; continuum limit = sequence",
    "T_TOWER": "E6->E7->E8 tower; C wraps in Z4; top = E8 dim 248",
    "T_MOONSHINE": "j(tau) = 1/q + 744 + 196884q...; 196884 = 1 + 196883; D12 Z4",
    "T_OBSERVER": "Observer Gluon = frame selector; Z4 face cycle = enacted LCR",
    "T_SYNTHESIS": "Synthesis Gluon = ledger root hash = hash(sum C_i); MorphForge = subtree",
    "T_MORPHIC": "Morphic Gluon = SK-combinator transport; S K K = I",
    "T_METAFORGE": "Material Gluon = ForgeFactory candidates; Gluon mass = formation energy",
    "T_FOLDFORGE": "Fold Gluon = contact-map/topo Gluon; homology barcodes",
    "T_KNIGHTFORGE": "Chess Gluon = L-conjugate CA Gluon; N-dim board = powered lattice",
    "T_TRAVERSAL": "Traversal Gluon = energy/ledger; geodesic = minimal energy; energy Z4",
    "T_ZPINCH": "Pinch/Shear Gluon = boundary Gluon at K=9; shear Z4 = pinch/shear/torsion/relief",
    "T_DELAY": "Delay/Shared Gluon = sampling buffer + shared state; observer Z4 cycle",
    "T_GAME_LATTICE": "Game Lattice Gluon = N-dim CA Gluon; powered chain = board dims",
    "T_MONSTER": "Monster Gluon = universal energy bound; dim = 196883 = 47*59*71",
    "T_GRAND_RIBBON": "Grand Ribbon Gluon = meta-framer; 31 beads = LCR sequence; couples P31",
    "T_META_LCR": "Meta Gluon = enacted LCR; grand ribbon = object, walkthrough = actor",
    "T_SUPERVISOR": "Supervisor cursor = compressed action graph; n=4->5 = 4D->8D; torsor",
    "T_OBSERVATION": "Single H-bond reads identically from both strands; C = H_bond_under_examination"
}

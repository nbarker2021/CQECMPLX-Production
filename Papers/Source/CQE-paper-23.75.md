# Paper 23.75 - FoldForge Next-State Bridge

## Bridge Role

Paper 23 exports a chain-descriptor pattern. It starts with a local sequence,
builds contact or adjacency receipts, marks candidate transitions, and keeps
global interpretation open until a domain verifier closes it.

## Exported Artifacts

The next state receives:

- local chain-window discipline,
- contact-map receipt discipline,
- candidate transition marks,
- bounded topology/winding witness status,
- explicit validation obligations,
- invalid-promotion labels.

## Use in Paper 24

Paper 24 may translate the chain and contact-map idea into paths on a board or
automaton lattice. A chess or game-state path may be read as a local sequence
with adjacency receipts, but it must prove its own rules and reachability.

## Use in Later Applied Papers

Later biological, material, CAD, or game papers may use the FoldForge pattern
when an object behaves like a constrained chain. The claim remains a descriptor
until its own verifier supplies measurement, simulation, or formal reachability.

## Boundary

Paper 23 exports the receipt form. It does not export biological closure.

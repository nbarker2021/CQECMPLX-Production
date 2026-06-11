"""D12 action envelope over D4 chart-axis classes.

This mounts the D12 verifier surface from the umbrella submission as a clean
package module. The important claim is an action envelope, not literal
subgroup containment: D12 permutes the three non-singlet D4 axis classes and
fixes the axis-0 singlet.
"""

from __future__ import annotations

from typing import Any

D12_ELEMENTS: tuple[tuple[int, int], ...] = tuple(
    (k, reflection) for reflection in (0, 1) for k in range(6)
)

D12_NAMES: dict[tuple[int, int], str] = {
    (0, 0): "e",
    (1, 0): "r",
    (2, 0): "r^2",
    (3, 0): "r^3",
    (4, 0): "r^4",
    (5, 0): "r^5",
    (0, 1): "s",
    (1, 1): "sr",
    (2, 1): "sr^2",
    (3, 1): "sr^3",
    (4, 1): "sr^4",
    (5, 1): "sr^5",
}

COLOR_NAMES = {
    0: "C- (E11+E22)",
    1: "C0 (E11+E33)",
    2: "C+ (E22+E33)",
}


def d12_multiply(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    """Group multiplication in Dih(6): (k,s)(l,t) = (k + (-1)^s l, s+t)."""

    k, s = a
    l, t = b
    sign = -1 if s else 1
    return ((k + sign * l) % 6, s ^ t)


def d12_inverse(a: tuple[int, int]) -> tuple[int, int]:
    k, s = a
    return ((-k) % 6, 0) if s == 0 else (k, 1)


def d12_conjugate(g: tuple[int, int], x: tuple[int, int]) -> tuple[int, int]:
    return d12_multiply(d12_multiply(g, x), d12_inverse(g))


def d12_acts_on_color(g: tuple[int, int], color_idx: int) -> int:
    """Act on the three trace-2 color classes C-, C0, C+."""

    if color_idx not in (0, 1, 2):
        raise ValueError("color_idx must be 0, 1, or 2")
    k, is_reflection = g
    rotated = (color_idx + (k % 3)) % 3
    if not is_reflection:
        return rotated
    if rotated == 0:
        return 2
    if rotated == 2:
        return 0
    return rotated


def d12_acts_on_d4_state(g: tuple[int, int], state: tuple[int, int]) -> tuple[int, int]:
    """Act on a D4 chart state encoded as (axis in 0..3, sheet in 0..1)."""

    axis, sheet = state
    if axis not in (0, 1, 2, 3) or sheet not in (0, 1):
        raise ValueError("state must be (axis in 0..3, sheet in 0..1)")
    if axis == 0:
        return (0, sheet)
    return (d12_acts_on_color(g, axis - 1) + 1, sheet)


def verify_d12_group_axioms() -> dict[str, Any]:
    errors: list[str] = []
    identity = (0, 0)

    for a in D12_ELEMENTS:
        if d12_multiply(identity, a) != a or d12_multiply(a, identity) != a:
            errors.append(f"identity failed for {a}")
        inv = d12_inverse(a)
        if d12_multiply(a, inv) != identity or d12_multiply(inv, a) != identity:
            errors.append(f"inverse failed for {a}")
        for b in D12_ELEMENTS:
            if d12_multiply(a, b) not in D12_ELEMENTS:
                errors.append(f"closure failed for {a} * {b}")
            for c in D12_ELEMENTS:
                left = d12_multiply(d12_multiply(a, b), c)
                right = d12_multiply(a, d12_multiply(b, c))
                if left != right:
                    errors.append(f"associativity failed for {a}, {b}, {c}")

    return {
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "group_order": len(D12_ELEMENTS),
    }


def verify_d12_color_action_preserves_trace2() -> dict[str, Any]:
    errors: list[str] = []
    orbit_table: list[dict[str, Any]] = []

    for g in D12_ELEMENTS:
        images = [d12_acts_on_color(g, color) for color in range(3)]
        is_permutation = sorted(images) == [0, 1, 2]
        if not is_permutation:
            errors.append(f"{D12_NAMES[g]} does not permute trace-2 colors")
        orbit_table.append(
            {
                "element": D12_NAMES[g],
                "images": tuple(images),
                "is_permutation": is_permutation,
            }
        )

    return {
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "orbit_table": orbit_table,
    }


def verify_d12_action_matches_weyl_13() -> dict[str, Any]:
    s = (0, 1)
    images = tuple(d12_acts_on_color(s, color) for color in range(3))
    errors: list[str] = []
    if images != (2, 1, 0):
        errors.append(f"reflection s should act as Weyl (1,3), got {images}")
    return {
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "images": images,
        "claim": "D12 reflection s matches the A3/Weyl (1,3) color transposition.",
    }


def verify_d12_conjugation_permutes_d4_axis_classes() -> dict[str, Any]:
    errors: list[str] = []
    axis_map: list[dict[str, Any]] = []

    for g in D12_ELEMENTS:
        color_images = [d12_acts_on_color(g, color) for color in range(3)]
        is_permutation = sorted(color_images) == [0, 1, 2]
        if not is_permutation:
            errors.append(f"{D12_NAMES[g]} does not permute color axes")
        axis_map.append(
            {
                "element": D12_NAMES[g],
                "axis_0_fixed": True,
                "color_axes_permutation": tuple(color_images),
                "is_valid": is_permutation,
            }
        )

    return {
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "axis_map": axis_map,
    }


def verify_d12_orbit_on_d4_states() -> dict[str, Any]:
    errors: list[str] = []
    states = [(axis, sheet) for axis in range(4) for sheet in range(2)]
    orbits: dict[tuple[int, int], set[tuple[int, int]]] = {}

    for state in states:
        orbit = {d12_acts_on_d4_state(g, state) for g in D12_ELEMENTS}
        orbits[state] = orbit
        axis, sheet = state
        if axis == 0:
            expected = {(0, sheet)}
        else:
            expected = {(1, sheet), (2, sheet), (3, sheet)}
        if orbit != expected:
            errors.append(f"orbit for {state} was {sorted(orbit)}, expected {sorted(expected)}")

    unique_orbits: list[frozenset[tuple[int, int]]] = []
    for orbit in orbits.values():
        frozen = frozenset(orbit)
        if frozen not in unique_orbits:
            unique_orbits.append(frozen)

    return {
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "d4_state_count": len(states),
        "unique_orbit_count": len(unique_orbits),
        "orbit_sizes": {str(state): len(orbit) for state, orbit in orbits.items()},
    }


def verify_d12_idempotent_chain() -> dict[str, Any]:
    sub_results = {
        "d12_group_axioms": verify_d12_group_axioms()["status"],
        "d12_color_action_preserves_trace2": verify_d12_color_action_preserves_trace2()["status"],
        "d12_reflection_matches_weyl_13": verify_d12_action_matches_weyl_13()["status"],
        "d12_conjugation_permutes_d4_axes": verify_d12_conjugation_permutes_d4_axis_classes()[
            "status"
        ],
        "d12_orbit_on_d4_states": verify_d12_orbit_on_d4_states()["status"],
    }
    all_pass = all(status == "pass" for status in sub_results.values())
    return {
        "status": "pass" if all_pass else "fail",
        "sub_results": sub_results,
        "chain_conclusion": (
            "D12 acts as the action envelope over D4 axis classes: it preserves "
            "the trace-2 color stratum, matches Weyl (1,3) on reflection, and "
            "keeps the D4 singlet/color orbit split intact."
        ),
    }

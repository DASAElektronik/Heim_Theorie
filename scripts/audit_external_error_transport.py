"""Conditional error algebra, not an external field or a repaired Heim solver.

With a fixed mass scale, alpha4=1, polynomial coefficients, and w, preserve
the empty-state subtraction and the skeleton reference on BOTH sides.
Raw correction h gives dR=h(n)-w*h(q)+(w-1)*h(0). Coalesce repeated
arguments before forming interval bounds. No physical h or error budget
is inferred from this arithmetic. This script writes no files.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F

import audit_coupled_existence as old

GAP = F("0.057144067635")
W_FACTOR_LO = F("73.1277926806")
W_FACTOR_HI = F("73.1277926811")


def exact(value):
    if type(value) not in (int, F):
        raise TypeError("Only exact integers and Fractions are supported")
    return F(value)


def raw_weights(n, reference, w):
    """Weights on DISTINCT arguments of the same raw error function h."""
    n, reference, w = map(exact, (n, reference, w))
    if n < 0 or reference <= 0 or w <= 0:
        raise ValueError("Require n>=0, reference>0, w>0")
    result = {}
    for key, weight in ((n, F(1)), (reference, -w), (F(0), w-1)):
        result[key] = result.get(key, F(0))+weight
    return {key: weight for key, weight in result.items() if weight}


def raw_change(n, reference, w, values):
    weights = raw_weights(n, reference, w)
    return sum((weight*exact(values[key]) for key, weight in weights.items()), F(0))


def raw_box(n, reference, w, boxes):
    """Outer image of pointwise bounds, not proof of functional attainability.

    Same-argument identities are enforced; other functional correlations
    can narrow this box further. The fixed positive w is exact here.
    """
    lower = upper = F(0)
    for key, weight in raw_weights(n, reference, w).items():
        lo, hi = map(exact, boxes[key])
        if lo > hi:
            raise ValueError("Reversed pointwise interval")
        endpoints = (weight*lo, weight*hi)
        lower += min(endpoints)
        upper += max(endpoints)
    return lower, upper


def effective_change(w, delta_n, delta_reference):
    """For already normalized delta=h-h(0); caller must preserve delta(0)=0."""
    w, delta_n, delta_reference = map(exact, (w, delta_n, delta_reference))
    if w <= 0:
        raise ValueError("Positive w required")
    return delta_n-w*delta_reference


def residual(P, B, w, phi_n, phi_reference, phi_zero):
    """Own fixed-coefficient extension of the printed reference subtraction."""
    P, B, w, phi_n, phi_reference, phi_zero = map(
        exact, (P, B, w, phi_n, phi_reference, phi_zero))
    if w <= 0:
        raise ValueError("Positive w required")
    return P+1+phi_n-phi_zero-w*(B+1+phi_reference-phi_zero)


def joint_change(w, delta_P, delta_B, delta_w, g_old, delta_n, delta_reference):
    """Exact additional terms if coefficients/w also change; no fitting."""
    w, delta_P, delta_B, delta_w, g_old, delta_n, delta_reference = map(
        exact, (w, delta_P, delta_B, delta_w, g_old, delta_n, delta_reference))
    if w <= 0 or w+delta_w <= 0:
        raise ValueError("Both old and new w must be positive")
    return (delta_P+delta_n-w*(delta_B+delta_reference)
            -delta_w*(g_old+delta_B+delta_reference))


def robust_gap(gap, uniform_error_bound):
    """Sufficient positive lower bound, or None if THIS test is inconclusive.

    The caller must justify the error bound on the whole candidate domain;
    failure/equality does not assert the existence of a root.
    """
    gap, uniform_error_bound = map(exact, (gap, uniform_error_bound))
    if gap <= 0 or uniform_error_bound < 0:
        raise ValueError("Require gap>0 and a nonnegative error bound")
    return gap-uniform_error_bound if uniform_error_bound < gap else None


def fixed_book_factors():
    """Recheck ONLY unchanged book constants, not a sourced approximation error."""
    rows = old.certify()
    factors = []
    for row in rows:
        if min(old.energy_margins(row).values()) < GAP:
            raise ArithmeticError("Previous uniform gap not certified")
        w = 1+row["eta11"]*row["A16"]
        if not W_FACTOR_LO < w.lo <= w.hi < W_FACTOR_HI:
            raise ArithmeticError("Fixed w factor escaped its rational enclosure")
        factors.append((row["profile"], w))
    return factors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check unchanged constants (default)")
    args = parser.parse_args()
    for profile, _ in fixed_book_factors():
        print(f"{profile}: {W_FACTOR_LO} < w < {W_FACTOR_HI}; old gap retained")
    print("Raw transport: h(n)-w*h(1)+(w-1)*h(0)")
    print("For normalized delta=h-h(0), conditional sufficient budget:")
    print("  eps_n+w*eps_reference < old gap (uniform on the full candidate domain)")
    print("For raw h and w>1: eps_n+w*eps_reference+(w-1)*eps_zero < old gap")
    print("No sourced error function/budget, corrected state, or physical robustness certified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

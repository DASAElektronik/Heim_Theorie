"""Exact, separate Lorentz/geometry/literal-matrix diagnostics; no source repair.

NORM-LORENTZ-MEANING-001. Standard library only, exact rational examples.
The static circle is not a rotating Heim shell. No fitted or measured inputs.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from math import isqrt

import audit_alpha as core
from audit_energy_kinematics import SOURCES as BOOK_SOURCES

OUTPUT = core.ROOT / "05_analysis/lorentz_meaning_diagnostics.json"
SOURCES = [dict(BOOK_SOURCES[0], locator="printed12/PDF20; printed21/PDF29 literal block; printed56/PDF63 contextual matrix; printed81/PDF88 and288/PDF294 energy"),
           dict(BOOK_SOURCES[1], locator="printed276-277/PDF282-283 author motivation; printed300-301/PDF306-307 H construction")] + [{
    "path": "01_sources/mainstream_reference/Einstein_1905_Elektrodynamik.pdf",
    "sha256": "F907CD496A6A1ABF07E7E78C2111A63DAB1E9D8F2491BCC0C391B872CB3C49B4",
    "locator": "printed902-903/PDF12-13; coordinate boost and equal-time geometry",
}]
ONE, ZERO = F(1), F(0)
IDENTITY = ((ONE, ZERO), (ZERO, ONE))
METRIC = ((ONE, ZERO), (ZERO, -ONE))
SPEED = F(3, 5)


def gamma_exact(b: F) -> F:
    """Restricted exact-rational examples; reject irrational gamma, do not round."""
    if not isinstance(b, F):
        raise TypeError("Pass an exact Fraction for the boost speed")
    if abs(b) >= 1:
        raise ValueError("Boost speed must satisfy |b| < 1")
    square = ONE/(ONE-b*b)
    n, d = isqrt(square.numerator), isqrt(square.denominator)
    if n*n != square.numerator or d*d != square.denominator:
        raise ValueError("This exact diagnostic requires rational gamma")
    return F(n, d)


def transpose(matrix):
    return tuple(zip(*matrix))


def multiply(left, right):
    """Internal 2x2 rational matrix helper."""
    return tuple(tuple(sum(left[i][k]*right[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def boost_matrix(b: F):
    g = gamma_exact(b)
    return ((g, -g*b), (-g*b, g))


def transform_pair(first: F, second: F, b: F) -> tuple[F, F]:
    """(ct,x) or (epsilon,q); algebraic helper does not impose a mass shell."""
    matrix = boost_matrix(b)
    return (matrix[0][0]*first+matrix[0][1]*second,
            matrix[1][0]*first+matrix[1][1]*second)


def momentum_summary(epsilon: F, q: F) -> dict:
    if epsilon < 1 or epsilon*epsilon-q*q != 1:
        raise ValueError("Summary requires the future unit massive shell")
    return {"epsilon": epsilon, "q_signed": q, "mass_shell": epsilon**2-q**2,
            "pc_magnitude_over_m0c2": abs(q), "T_over_m0c2": epsilon-ONE}


def static_circle_event(x: F, y: F, b: F) -> dict:
    """Unit static circle worldline sampled on ct'=0, not on ct=0."""
    if x*x+y*y != 1:
        raise ValueError("Sample must lie on the unit static circle")
    ct = b*x
    ct_prime, x_prime = transform_pair(ct, x, b)
    return {"x": x, "y": y, "ct_selected": ct,
            "ct_prime": ct_prime, "x_prime": x_prime, "y_prime": y}


def perimeter_bounds(b: F) -> dict:
    s = ONE/gamma_exact(b)
    return {"uniform_contraction_hypothesis": s,
            "actual_perimeter_ratio_lower": (ONE+s)/2,
            "actual_perimeter_ratio_upper_squared": (ONE+s*s)/2,
            "bounds_strict": b != ZERO,
            "scope": "Equal-time image of a static circle, not a rotating Heim shell"}


def source_literal_block(b: F):
    """EDM1 p21 after ordinary tan(psi)=i*b substitution, positive cos branch."""
    g = gamma_exact(b)
    return ((g, -g*b), (g*b, g))


def serialize(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {key: serialize(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [serialize(item) for item in value]
    return value


def build_report() -> dict:
    b = SPEED
    standard = boost_matrix(b)
    literal = source_literal_block(b)
    product = multiply(literal, transpose(literal))
    cases = []
    for label, initial in (("initially_resting", (ONE, ZERO)),
                           ("boost_into_particle_rest_frame", (F(5, 4), F(3, 4)))):
        final = transform_pair(*initial, b)
        cases.append({"label": label, "before": momentum_summary(*initial),
                      "after": momentum_summary(*final)})
    samples = ((ONE, ZERO), (ZERO, ONE), (-ONE, ZERO), (ZERO, -ONE), (F(3, 5), F(4, 5)))
    return serialize({
        "schema_version": 1, "audit_date": "2026-09-06",
        "normalization_id": "NORM-LORENTZ-MEANING-001", "sources": SOURCES,
        "arithmetic": "Exact rational fractions; no floating-point arithmetic",
        "modern_reference_inputs": [], "target_fitting": False,
        "boost_speed_b": b, "gamma_b": gamma_exact(b),
        "speed_scope": "Relative frame speed, not silently identified with source alpha",
        "standard_reference": {
            "status": "our_explicit_reference_not_a_silent_source_matrix_repair",
            "basis": "(ct,x) or dimensionless (epsilon,q)",
            "matrix": standard,
            "transformed_metric": multiply(multiply(transpose(standard), METRIC), standard),
            "preserves_metric": multiply(multiply(transpose(standard), METRIC), standard) == METRIC,
            "momentum_cases": cases,
        },
        "static_circle": {"samples": [static_circle_event(x, y, b) for x, y in samples],
                          "perimeter_bounds": perimeter_bounds(b)},
        "book_p21_literal": {
            "status": "conditional_source_algebra_under_ordinary_complex_trigonometry",
            "source_locator": "EDM1 printed21/PDF29",
            "basis": "(x1,x4), x4=ict; not the real (ct,x) reference basis",
            "printed_block": "[[cos(psi),i*sin(psi)],[-i*sin(psi),cos(psi)]]; tan(psi)=i*b",
            "substituted_block": literal, "A_times_transpose": product,
            "claimed_orthogonal": True, "is_orthogonal_under_stated_reading": product == IDENTITY,
            "two_by_two_factor": (ONE+b*b)/(ONE-b*b),
            "full_four_by_four_diagonal": (product[0][0], ONE, ONE, product[1][1]),
            "interpretation": "Local printed-matrix issue; no inference about intent or whole-theory validity",
        },
        "limits": [
            "No author intention is computed",
            "Form invariance is not scalar-value invariance",
            "The static circle does not determine the circumference of the Heim shell",
            "The source literal block and standard reference remain separate",
        ],
    })


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify-sources", action="store_true")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.verify_sources:
        errors = core.verify_sources({"sources": SOURCES})
        if errors:
            print("\n".join(errors))
            return 1
        print("Book and historical reference hashes verified.")
    report = build_report()
    encoded = json.dumps(report, ensure_ascii=False, indent=2)+"\n"
    if args.write:
        OUTPUT.write_text(encoded, encoding="utf-8", newline="\n")
        print(f"Wrote {OUTPUT.relative_to(core.ROOT).as_posix()}")
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != encoded:
            print("Diagnostic snapshot missing/stale; review before --write.")
            return 1
        print("Lorentz meaning snapshot matches fresh exact calculation.")
    print(f"Reference metric preserved: {report['standard_reference']['preserves_metric']}")
    print("Static-circle perimeter ratio: 9/10 < P < sqrt(41/50), not 4/5.")
    print(f"Book p21 literal 2x2 A*A^T factor: {report['book_p21_literal']['two_by_two_factor']} (identity would require 1)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

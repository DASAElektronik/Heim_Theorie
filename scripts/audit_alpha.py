"""Reproduce the scoped Heim/IGW alpha audit using only Python's standard library.

Equations and all interpretation choices: NORM-ALPHA-AUDIT-SCOPE.
No source macros/programs are executed; experimental values are comparison-only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUTS = ROOT / "04_reconstruction/alpha_audit/inputs.json"
OUTPUT = ROOT / "05_analysis/alpha_audit_results.json"
D = Decimal
ONE = D(1)
TWO = D(2)


def decimal_token(token: str) -> Decimal:
    """Retain lexical precision while accepting source decimal commas."""
    value = D(token.replace(",", "."))
    if not value.is_finite():
        raise ValueError("Expected a finite decimal token")
    return value


def printing_interval(token: str) -> tuple[Decimal, Decimal]:
    value = decimal_token(token)
    half_ulp = D(5).scaleb(value.as_tuple().exponent - 1)
    return value - half_ulp, value + half_ulp


def reciprocal_interval(bounds: tuple[Decimal, Decimal]) -> tuple[Decimal, Decimal]:
    lo, hi = bounds
    if not D(0) < lo <= hi:
        raise ValueError("Reciprocal interval must be positive and ordered")
    with localcontext() as ctx:
        ctx.rounding = ROUND_FLOOR
        inverse_lo = ONE / hi
        ctx.rounding = ROUND_CEILING
        inverse_hi = ONE / lo
    return inverse_lo, inverse_hi


def intervals_overlap(left: tuple[Decimal, Decimal], right: tuple[Decimal, Decimal]) -> bool:
    return max(left[0], right[0]) <= min(left[1], right[1])


def mathematical_pi() -> Decimal:
    """Gauss-Legendre iteration in the caller's Decimal context."""
    a, b, t, weight = ONE, ONE / TWO.sqrt(), ONE / D(4), ONE
    previous = D(0)
    for _ in range(20):
        next_a = (a + b) / TWO
        b = (a * b).sqrt()
        t -= weight * (a - next_a) ** 2
        a, weight = next_a, weight * TWO
        estimate = (a + b) ** 2 / (D(4) * t)
        if estimate == previous:
            return +estimate
        previous = estimate
    raise ArithmeticError("Pi iteration did not converge")


def eta_k_q(pi: Decimal, *, k: int, q: int) -> Decimal:
    return pi / (pi**4 + D(4 + k) * D(q)**4).sqrt().sqrt()


def equation_rhs(pi: Decimal, model: dict) -> dict[str, Decimal]:
    """NORM-1982-ETA-INDEX; 1982 reconciliation; 1989 B59; audit scope."""
    eta = pi / (pi**4 + D(4)).sqrt().sqrt()
    vartheta = D(5) * eta + TWO * eta.sqrt() + ONE
    eta11 = eta_k_q(pi, k=1, q=1)
    eta12 = eta_k_q(pi, k=model["eta12_k"], q=model["eta12_q"])
    common = {"eta": eta, "vartheta": vartheta, "eta11": eta11, "eta12": eta12}
    if model["equation"] == "1982":
        a1 = eta11.sqrt() * (ONE - eta11.sqrt()) / (ONE + eta11.sqrt())
        a2 = eta12.sqrt() * (ONE - eta12.sqrt()) / (ONE + eta12.sqrt())
        correction = ONE - a1 * a2
        common.update(A1=a1, A2=a2)
    elif model["equation"] == "1989":
        eta22 = eta_k_q(pi, k=2, q=2)
        c_prime = (ONE + eta22) / (eta * eta11 * eta12) * (
            (ONE - eta.sqrt()) / (ONE + eta.sqrt())
        ) ** 2
        correction = ONE - c_prime
        common.update(eta22=eta22, C_prime=c_prime, K_alpha=correction)
    else:
        raise ValueError(f"Unknown equation {model['equation']}")
    common["rhs"] = D(9) * vartheta * correction / (TWO * pi) ** 5
    return common


def solve_branches(rhs: Decimal) -> tuple[Decimal, Decimal]:
    """Positive branches, small then large; stable even when rhs is tiny."""
    if not rhs.is_finite() or not D(0) < rhs <= ONE / TWO:
        raise ValueError("Two positive branches require 0 < rhs <= 1/2")
    large = ((ONE + (ONE - D(4) * rhs**2).sqrt()) / TWO).sqrt()
    return rhs / large, large


def check_printed_pair(plus: str, minus: str, *, reciprocal: bool) -> dict:
    left, right = printing_interval(plus), printing_interval(minus)
    a, b = decimal_token(plus), decimal_token(minus)
    if reciprocal:
        left, right = reciprocal_interval(left), reciprocal_interval(right)
        a, b = ONE / a, ONE / b
    if min(left[0], right[0]) < 0:
        raise ValueError("Squared-sum check requires positive intervals")
    with localcontext() as ctx:
        ctx.rounding = ROUND_FLOOR
        sum_lo = left[0]**2 + right[0]**2
        ctx.rounding = ROUND_CEILING
        sum_hi = left[1]**2 + right[1]**2
    bounds = (sum_lo, sum_hi)
    if not D(0) < a < ONE:
        raise ValueError("Printed small branch must be between 0 and 1")
    expected_large = (ONE - a*a).sqrt()
    return {
        "printed_plus": plus, "printed_minus": minus, "values_are_reciprocals": reciprocal,
        "squared_sum": a*a + b*b, "squared_sum_minus_one": a*a + b*b - ONE,
        "squared_sum_rounding_interval": bounds,
        "compatible_with_complementary_branches": bounds[0] <= ONE <= bounds[1],
        "large_alpha_implied_by_central_small": expected_large,
        "large_inverse_implied_by_central_small": ONE / expected_large,
    }


def check_printed_reciprocal(alpha: str, inverse: str) -> dict:
    implied = reciprocal_interval(printing_interval(alpha))
    stated = printing_interval(inverse)
    return {
        "printed_alpha": alpha, "printed_inverse": inverse,
        "inverse_of_central_alpha": ONE / decimal_token(alpha),
        "inverse_interval_from_alpha": implied, "printed_inverse_interval": stated,
        "compatible_after_rounding": intervals_overlap(implied, stated),
    }


def stringify(value):
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, dict):
        return {key: stringify(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [stringify(item) for item in value]
    return value


def build_report(inputs: dict, precision: int = 80) -> dict:
    if not 40 <= precision <= 200:
        raise ValueError("Audit precision must be between 40 and 200 digits")
    with localcontext() as ctx:
        ctx.prec = precision
        pi_math = mathematical_pi()
        reference = inputs["modern_reference"]
        ref = decimal_token(reference["value"])
        rows = []
        for profile in inputs["pi_profiles"]:
            if profile["kind"] == "gauss_legendre":
                pi = pi_math
            elif profile["kind"] == "decimal_literal":
                pi = decimal_token(profile["value"])
            else:
                raise ValueError(f"Unknown pi profile {profile['kind']}")
            for model in inputs["models"]:
                terms = equation_rhs(pi, model)
                rhs = terms["rhs"]
                small, large = solve_branches(rhs)
                printed = inputs["printed"][model["equation"]]
                inv_small, inv_large = ONE / small, ONE / large
                target = decimal_token(printed["inverse_plus"])
                envelope = printing_interval(printed["inverse_plus"])
                rows.append({
                    "model": model["id"], "interpretation_status": model["status"],
                    "normalization_decisions": model["decisions"],
                    "pi_profile": profile["id"], "pi": pi, "intermediates": terms,
                    "alpha_plus": small, "alpha_minus": large,
                    "inverse_plus": inv_small, "inverse_minus": inv_large,
                    "squared_sum_error": small*small + large*large - ONE,
                    "product_error": small*large - rhs,
                    "small_unsquared_equation_error": small*(ONE-small*small).sqrt() - rhs,
                    "large_unsquared_equation_error": large*(ONE-large*large).sqrt() - rhs,
                    "inverse_plus_minus_printed": inv_small - target,
                    "matches_printed_inverse_plus_rounding": envelope[0] <= inv_small <= envelope[1],
                    "inverse_plus_minus_codata2022": inv_small - ref,
                    "relative_difference_to_codata2022_ppm": (inv_small-ref)/ref*D(1000000),
                })
        p82, p89 = inputs["printed"]["1982"], inputs["printed"]["1989"]
        checks = {
            "1982_printed_inverse_pair": check_printed_pair(p82["inverse_plus"], p82["inverse_minus"], reciprocal=True),
            "1989_printed_alpha_pair": check_printed_pair(p89["alpha_plus"], p89["alpha_minus"], reciprocal=False),
            "1989_printed_inverse_pair": check_printed_pair(p89["inverse_plus"], p89["inverse_minus"], reciprocal=True),
            "1989_plus_reciprocal": check_printed_reciprocal(p89["alpha_plus"], p89["inverse_plus"]),
            "1989_minus_reciprocal": check_printed_reciprocal(p89["alpha_minus"], p89["inverse_minus"]),
        }
        canonical_inputs = json.dumps(inputs, sort_keys=True, ensure_ascii=True, separators=(",", ":")).encode("ascii")
        return stringify({
            "schema_version": 1, "audit_date": inputs["audit_date"],
            "input_content_sha256": hashlib.sha256(canonical_inputs).hexdigest(),
            "arithmetic": {"engine": "Python standard-library Decimal", "precision": precision, "pi_algorithm": "Gauss-Legendre", "root_algorithm": "large square root then small=rhs/large"},
            "rounding_envelope_policy": "Closed half-last-place envelopes assuming rounding to nearest; not physical/statistical uncertainty",
            "sources": inputs["sources"], "modern_reference": reference,
            "models": rows, "printed_value_checks": checks,
            "claim_scope": "IGW formula/value consistency only; no mass-spectrum implementation or historical prediction validation",
        })


def verify_sources(inputs: dict) -> list[str]:
    failures = []
    for source in inputs["sources"]:
        path = ROOT / source["path"]
        if not path.is_file():
            failures.append(f"Missing local source: {source['path']}")
        elif hashlib.sha256(path.read_bytes()).hexdigest().upper() != source["sha256"]:
            failures.append(f"Source hash mismatch: {source['path']}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=80)
    parser.add_argument("--verify-sources", action="store_true", help="Check local PDF hashes; not required for arithmetic-only reruns")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="Regenerate the tracked JSON result")
    mode.add_argument("--check", action="store_true", help="Fail if the tracked JSON differs from a fresh calculation")
    args = parser.parse_args()
    inputs = json.loads(INPUTS.read_text(encoding="utf-8"))
    if args.verify_sources:
        failures = verify_sources(inputs)
        if failures:
            for failure in failures:
                print(failure)
            return 1
        print(f"Source hashes verified: {len(inputs['sources'])}")
    report = build_report(inputs, args.precision)
    encoded = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.write:
        OUTPUT.write_text(encoded, encoding="utf-8", newline="\n")
        print(f"Wrote {OUTPUT.relative_to(ROOT).as_posix()}")
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != encoded:
            print("Result snapshot missing/stale. Review changes before running --write.")
            return 1
        print("Result snapshot matches fresh calculation.")
    for row in report["models"]:
        print(f"{row['model']} [{row['pi_profile']}]: inverse_plus={D(row['inverse_plus']):.12f}; printed_match={row['matches_printed_inverse_plus_rounding']}")
    print("Printed checks (False means source numbers are incompatible, not a software failure):")
    for name, check in report["printed_value_checks"].items():
        compatible = check.get("compatible_with_complementary_branches", check.get("compatible_after_rounding"))
        print(f"  {name}: compatible={compatible}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

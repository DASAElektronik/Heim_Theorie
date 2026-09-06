"""NORM-CONFIGURATION-SELECTION-001: separate the three printed selection levels.

Only dimensionless book relations. No measured inputs or silent source repair.
"""

from __future__ import annotations

import argparse
from decimal import Decimal as D, getcontext, localcontext
from fractions import Fraction as F
import json

import audit_alpha as core

OUTPUT = core.ROOT / "05_analysis/configuration_selection_diagnostics.json"
SOURCE = {
    "path": "01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf",
    "sha256": "F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849",
    "locator": "printed263-269 / PDF269-275; L*Delta=k; (98); potential ratios; (98a)",
    "edition": "Second unchanged edition1996; local hash-verified copy",
}
CLAIMED_INTERVALS = {1: (2, 3), 2: (2, 3), 3: (1, 2), 4: (0, 1)}


def _integer(value, *, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(f"Expected integer >= {minimum}, not bool/float/string")


def _positive_decimal(value):
    if not isinstance(value, D) or not value.is_finite() or value <= 0:
        raise ValueError("Expected finite positive Decimal")


def eta_qk(pi: D, *, q: int, k: int) -> D:
    _positive_decimal(pi)
    _integer(q)
    _integer(k)
    return pi / (pi**4 + D(q)**4 * D(4 + k)).sqrt().sqrt()


def charge_change(k: int, dimensions: int = 4) -> dict:
    """Positive ratio/magnitude from L*Delta=k; dimensions!=4 is only diagnostic."""
    _integer(k, minimum=1)
    _integer(dimensions, minimum=1)
    delta = D(k) / D(dimensions)
    return {"delta": delta, "charge_ratio": (1 + delta).sqrt().sqrt()}


def ratio_levels(e: D, a: D, x: D) -> dict:
    """Printed Q2=sqrt(e), never sqrt(a); D is our algebraic re-expression."""
    for value in (e, a, x):
        _positive_decimal(value)
    if not a <= e <= 1:
        raise ValueError("Selection ratios require 0 < eta_q <= eta <= 1")
    first = (1 + a.sqrt())**2 / (4 * e * a)
    b_bound = first + (1 - a / e) * e.sqrt()
    d_bound = first + (1 / a - a / e) * e.sqrt()
    v1, v2 = a*x, (1+a.sqrt())**2/(4*e)
    q1, q2 = a*a/e.sqrt(), e.sqrt()
    return {
        "V1": v1, "V2": v2, "Q1": q1, "Q2": q2,
        "B_printed": b_bound, "D_from_VQ": d_bound,
        "D_minus_B": d_bound-b_bound,
        "D_minus_B_identity": e.sqrt()*(1/a-1),
        "delta_VQ": v1+q1-v2-q2,
        "delta_from_D": a*(x-d_bound),
    }


def threshold(pi: D, q: int, bound: D) -> D:
    _positive_decimal(pi)
    _positive_decimal(bound)  # fourth power is monotone on this domain
    _integer(q, minimum=1)
    return (pi/D(q))**4 * (bound**4-1)-4


def strict_compare(left: D, right: D) -> int:
    """Refuse unresolved near-equalities; a guard, not interval certification."""
    if not all(isinstance(v, D) and v.is_finite() for v in (left, right)):
        raise ValueError("Comparison requires finite Decimals")
    scale = max(abs(left), abs(right), D(1))
    if abs(left-right) <= scale*D(10)**(8-getcontext().prec):
        raise ArithmeticError("Comparison too close at current precision")
    return 1 if left > right else -1


def configuration(pi: D, *, q: int, k: int) -> dict:
    _integer(q, minimum=1)
    _integer(k, minimum=1)
    e = eta_qk(pi, q=1, k=0)
    a = eta_qk(pi, q=q, k=0)
    internal = eta_qk(pi, q=q, k=k)
    x = 1/internal
    levels = ratio_levels(e, a, x)
    ub = threshold(pi, q, levels["B_printed"])
    ud = threshold(pi, q, levels["D_from_VQ"])
    delta_sign = strict_compare(levels["delta_VQ"], D(0))
    return {
        "q": q, "k": k, "eta_q": a, "eta_qk": internal, "x": x,
        **levels, "u_B": ub, "u_D": ud,
        "upstream_positive_condition": delta_sign < 0,
        "printed_VQ_inequality": delta_sign > 0,
        "printed_eta_inequality": strict_compare(x, levels["B_printed"]) < 0,
        "printed_k_bound": strict_compare(D(k), ub) < 0,
        "derived_upstream_k_bound": strict_compare(D(k), ud) < 0,
    }


def rational_tail_certificate() -> dict:
    """For positive integer q>=5; uses standard exact 3<pi<22/7."""
    e_lower, a_upper, sqrt_a_upper = F(49, 50), F(9, 20), F(84, 125)
    f_upper = (1+sqrt_a_upper)**2/(4*e_lower) + a_upper-a_upper**2
    checks = {
        "eta_lower_via_pi_gt_3": F(81, 85) > e_lower**4,
        "sqrt2_gt_7_over_5": F(7, 5)**2 < 2,
        "eta5_upper_via_pi_lt_22_over_7": F(22, 49) < a_upper,
        "F_increasing_domain": 2*a_upper < e_lower,
        "sqrt_eta5_upper": sqrt_a_upper**2 > a_upper,
        "F_upper_less_than_one": f_upper < 1,
    }
    return {
        "domain": "positive integer q>=5; no claim for every real q>4",
        "premise": "standard exact bound 3<pi<22/7",
        "method": "a*B=F(a); 0<a<=eta5<9/20<eta/2; F increasing; F(a)<upper<1; B<1/a implies u_B<0",
        "F_upper_rational": str(f_upper), "exact_rational_checks": checks,
        "all_checks_hold": all(checks.values()),
    }


def build_report(precision: int = 80) -> dict:
    if type(precision) is not int or not 40 <= precision <= 200:
        raise ValueError("Diagnostic precision must be integer40..200")
    with localcontext() as ctx:
        ctx.prec = precision
        pi = core.mathematical_pi()
        e = eta_qk(pi, q=1, k=0)
        bounds, cases, pairs = [], [], []
        for q in range(1, 11):
            row = configuration(pi, q=q, k=1)
            claim = CLAIMED_INTERVALS.get(q)
            bounds.append({
                "q": q, "eta_q": row["eta_q"],
                "B_printed": row["B_printed"], "D_from_VQ": row["D_from_VQ"],
                "u_B": row["u_B"], "u_D": row["u_D"],
                "claimed_interval": claim if claim else "u_B<0 (integer q>=5)",
                "matches_claim": (strict_compare(row["u_B"], D(claim[0])) > 0 and
                                  strict_compare(row["u_B"], D(claim[1])) < 0)
                                 if claim else strict_compare(row["u_B"], D(0)) < 0,
            })
            for k in range(1, 21):
                case = configuration(pi, q=q, k=k)
                if case["printed_k_bound"]:
                    pairs.append([q, k])
                if k in (1, 2, 3, 6, 7):
                    cases.append(case)
        return core.stringify({
            "schema_version": 1, "audit_date": "2026-09-06", "precision": precision,
            "normalization_id": "NORM-CONFIGURATION-SELECTION-001", "source": SOURCE,
            "scope": "Separate printed relations, conditional algebra, and integer selection; no intended correction or complete physical selection theory",
            "modern_reference_inputs": [], "target_fitting": False,
            "pi": pi, "eta": e,
            "charge_change_L4": [{"k": k, **charge_change(k)} for k in (1, 2)],
            "bounds": bounds, "cases": cases,
            "positive_integer_pairs_from_printed_bound": pairs,
            "pair_completeness": "q1..4 checked with u_B<3; all integer q>=5 excluded by separate rational tail certificate; k>=1",
            "tail_certificate": rational_tail_certificate(),
            "asymptotic_u_B": 1/(64*e**4)-4,
            "asymptotic_u_D": 4*(1/(4*e)+e.sqrt())**4-4,
        })


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=80)
    parser.add_argument("--verify-sources", action="store_true")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.verify_sources:
        errors = core.verify_sources({"sources": [SOURCE]})
        if errors:
            print("\n".join(errors))
            return 1
        print("EDM2 source hash verified.")
    report = build_report(args.precision)
    encoded = json.dumps(report, ensure_ascii=False, indent=2)+"\n"
    if args.write:
        OUTPUT.write_text(encoded, encoding="utf-8", newline="\n")
        print(f"Wrote {OUTPUT.relative_to(core.ROOT).as_posix()}")
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != encoded:
            print("Diagnostic snapshot missing/stale; review before --write.")
            return 1
        print("Configuration selection snapshot matches fresh calculation.")
    for row in report["bounds"][:5]:
        print(f"q={row['q']}: u_B={D(row['u_B']):.12f}; printed interval matches={row['matches_claim']}")
    print("Pairs from printed bound:", report["positive_integer_pairs_from_printed_bound"])
    print("Separate upstream/VQ/B relations; not a validated physical selection rule.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

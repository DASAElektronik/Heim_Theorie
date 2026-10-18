"""Etappe 40: printed-endpoint diagnostics, NOT an original-input mass fit.

H004 p371 SI tokens; historical c: M006 p15. H003 p248 (29) is a
declared cross-edition bridge. See CONSTANTS_ANCHOR_PLAN.md for scope.
"""
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
import argparse
import json
from pathlib import Path

try:
    from .audit_alpha import mathematical_pi
except ImportError:
    from audit_alpha import mathematical_pi

TOKENS = dict(h="6.626173e-34", gamma="6.672131e-11",
              epsilon0="8.854323e-12", mu0="1.256618e-6", e="1.602188e-19")
C = F(299792458)
C_SIGMA = F("1.2")
OUTPUT = Path(__file__).resolve().parents[1] / "05_analysis/constants_anchor_results.json"


def rational_print_interval(token):
    value = D(token)
    if not value.is_finite() or value <= 0:
        raise ValueError("Expected a positive finite print token")
    half = F(10) ** value.as_tuple().exponent / 2
    return F(value) - half, F(value) + half


def decimal_fraction(value):
    return D(value.numerator) / D(value.denominator)


def c_product_bounds(epsilon_bounds, mu_bounds, c_bounds):
    """Exact rational range of c² epsilon mu on a positive rectangular box."""
    if any(not 0 < lo <= hi for lo, hi in (epsilon_bounds, mu_bounds, c_bounds)):
        raise ValueError("Positive ordered bounds required")
    return tuple(c_bounds[i] ** 2 * epsilon_bounds[i] * mu_bounds[i] for i in (0, 1))


def mass_scale(gamma, hbar, c, s0, pi):
    # Original H004 (97) expression; fractional powers require positive inputs.
    return pi ** (D(1)/4) * (3*pi*s0*gamma*hbar) ** (D(1)/3) * (
        c*hbar/(3*gamma)).sqrt() / (c*s0)


def gamma_from_anchor(me, de, hbar, c, s0, pi):
    """Conditional inversion only: fixed positive dimensionless de."""
    if min(me, de, hbar, c, s0, pi) <= 0:
        raise ValueError("Positive inputs required")
    return pi**3 * pi.sqrt() * hbar**5 * de**6 / (3*c**3*s0**4*me**6)


def diagnose(precision=60):
    with localcontext() as ctx:
        ctx.prec = precision
        pi = mathematical_pi()
        p = {k: D(v) for k, v in TOKENS.items()}
        b = {k: rational_print_interval(v) for k, v in TOKENS.items()}
        bounds_c = c_product_bounds(b["epsilon0"], b["mu0"], (C, C))
        bounds_sigma = c_product_bounds(b["epsilon0"], b["mu0"], (C-C_SIGMA, C+C_SIGMA))
        eplo, ephi = map(decimal_fraction, b["epsilon0"])
        mulo, muhi = map(decimal_fraction, b["mu0"])
        hlo, hhi = map(decimal_fraction, b["h"])
        r = (p["mu0"]/p["epsilon0"]).sqrt()
        rlo, rhi = (mulo/ephi).sqrt(), (muhi/eplo).sqrt()
        eta = pi/(pi**4+4).sqrt().sqrt()
        theta = 5*eta+2*eta.sqrt()+1
        factor = 9*theta/(16*pi**5)  # e² = factor*h/R, not factor*hbar/R
        charge = (factor*p["h"]/r).sqrt()
        charge_lo, charge_hi = (factor*hlo/rhi).sqrt(), (factor*hhi/rlo).sqrt()
        elo, ehi = map(decimal_fraction, b["e"])
        fmt = lambda x: format(x, ".11E")
        return {
            "scope": "Printed-endpoint checks only; conditional H003(29) bridge; no mass fit",
            "source_tokens_SI": TOKENS,
            "historical_c_m_s": str(C), "historical_c_sigma_m_s": "1.2",
            "rounding_assumption": "nearest final printed digit, half-unit closed intervals",
            "c_implied_m_s": fmt(1/(p["epsilon0"]*p["mu0"]).sqrt()),
            "c_implied_rounding_range_m_s": [fmt(1/(ephi*muhi).sqrt()), fmt(1/(eplo*mulo).sqrt())],
            "R_implied_ohm": fmt(r),
            "c2_epsilon_mu_central": fmt(decimal_fraction(C)**2*p["epsilon0"]*p["mu0"]),
            "exact_product_range_at_c": [str(v) for v in bounds_c],
            "exact_product_contains_one_at_c": bounds_c[0] <= 1 <= bounds_c[1],
            "exact_product_contains_one_over_c_sigma": bounds_sigma[0] <= 1 <= bounds_sigma[1],
            "eq29_charge_C": fmt(charge),
            "eq29_charge_rounding_range_C": [fmt(charge_lo), fmt(charge_hi)],
            "printed_charge_rounding_range_C": [fmt(elo), fmt(ehi)],
            "eq29_charge_ranges_overlap_numeric": max(charge_lo, elo) <= min(charge_hi, ehi),
            "irrational_bounds_status": "Decimal endpoint estimates, not certified outward intervals",
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = diagnose(60)
    if result != diagnose(90):
        raise SystemExit("60/90-digit stability check failed")
    if args.check:
        if json.loads(OUTPUT.read_text(encoding="utf-8")) != result:
            raise SystemExit("Stored diagnostic differs")
        print("Stored diagnostic reproduced; 60/90-digit agreement at 12 significant figures.")
    elif args.write:
        OUTPUT.write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
        print(OUTPUT)
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

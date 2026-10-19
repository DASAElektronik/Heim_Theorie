"""NORM-EXPONENTIAL-CONTEXT-001: conditional scalar image of book (79).

E=1, mu;n -> r, fixed scalar parameters, amplitude normalized at r=0.
Not an implementation of metronic operators, F/G, or a physical field theory.
"""

from __future__ import annotations

import argparse
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
import json

import audit_alpha as core

OUTPUT = core.ROOT / "05_analysis/exponential_context_diagnostics.json"
SOURCE = {
    "path": "01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf",
    "sha256": "F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849",
    "locator": "printed 175-179 / PDF 181-185, (79)-(79c); printed 269 / PDF 275",
    "edition": "Second unchanged edition 1996; local hash-verified copy",
}


def _finite(value):
    if not isinstance(value, D) or not value.is_finite():
        raise ValueError("Expected finite Decimal, not float/bool/string")


def _parameters(lam: D, a: D, b: D):
    for value in (lam, a, b):
        _finite(value)
    if lam <= 0 or a <= 0 or not -1 < b < 1:
        raise ValueError("Scalar diagnostic requires lambda>0, a>0, -1<b<1")


def _one_minus_exp_negative(x: D) -> D:
    """Stable -expm1(-x) for x>=0; small-x alternating Taylor series."""
    if x > D("0.1"):
        return 1-(-x).exp()
    term = total = x
    n = 2
    while True:
        term *= -x/D(n)
        updated = total+term
        if updated == total:
            return total
        total = updated
        n += 1


def profile(lam: D, a: D, b: D, r: D) -> dict:
    """Stable factored expression, including nondecaying diagnostic controls.

    The exact scalar image is exp(x)*[D(w)/(2(1-b))]**(-p).
    This is not asserted to be an exact scalar solution of Heim's operators.
    """
    _parameters(lam, a, b)
    _finite(r)
    if r < 0:
        raise ValueError("Radial distance must be nonnegative")
    x, p = lam*r, a/(2*lam)
    t = (-x).exp()
    one_minus_t = _one_minus_exp_negative(x)
    # 1-2*b*t+t*t, evaluated without cancellation near b=1, r=0.
    correction_base = one_minus_t**2 + 2*(1-b)*t
    log_amplitude = p*(2*(1-b)).ln()
    log_leading = log_amplitude+(lam-a)*r
    log_ratio = -p*correction_base.ln()
    real_selector = (one_minus_t+(1-b)*t)/correction_base
    s = 2*abs(b)*t+t*t
    bound = p*s*((-p-1)*(1-s).ln()).exp() if s < 1 else None
    return {
        "lambda": lam, "a": a, "b": b, "r": r, "x": x, "p": p,
        "H": (log_leading+log_ratio).exp(),
        "leading_amplitude": log_amplitude.exp(),
        "leading_profile": log_leading.exp(),
        "H_over_leading_minus_one": log_ratio.exp()-1,
        "relative_error_absolute_bound": bound,
        "bound_condition_s": s,
        "real_selector": real_selector,
        "logarithmic_slope": lam-a*real_selector,
        "asymptotic_slope": lam-a,
        "decays_at_infinity": a > lam,
        # Ratio of leading amplitudes, not a source error when amplitude is free.
        "p178_over_p79_leading_amplitude": (-p/2*((1-b)*(1+b)).ln()).exp(),
    }


def stationary_polynomial(lam: D, a: D, b: D, w: D) -> D:
    _parameters(lam, a, b)
    _finite(w)
    if w < 1:
        raise ValueError("Radial branch has w=exp(lambda*r)>=1")
    ratio = lam/a
    return (1-ratio)*w*w+b*(2*ratio-1)*w-ratio


def exact_counterexample() -> dict:
    """Rational certificate: stationary positive radii do not force decay."""
    lam, a, b = F(1), F(10, 11), F(3, 5)
    ratio = lam/a
    roots = (F(11, 5), F(5))
    residuals = [(1-ratio)*w*w+b*(2*ratio-1)*w-ratio for w in roots]
    def slope(w):
        return lam-a*w*(w-b)/(w*w-2*b*w+1)
    probes = (F(1), F(3), F(6))
    slopes = [slope(w) for w in probes]
    return {
        "scope": "ordinary scalar image only; outside the asserted decaying branch",
        "lambda": str(lam), "a": str(a), "b": str(b), "A_lambda_over_a": str(ratio),
        "polynomial_integer_multiple": "5*w^2-36*w+55=0",
        "w_roots": [str(w) for w in roots],
        "r_roots": "ln(11/5), ln(5); lambda=1 in arbitrary consistent length units",
        "root_residuals": [str(v) for v in residuals],
        "all_roots_radial": all(w > 1 for w in roots),
        "all_residuals_zero": all(v == 0 for v in residuals),
        "w_slope_probes": [str(w) for w in probes],
        "logarithmic_slopes": [str(v) for v in slopes],
        "maximum_then_minimum": slopes[0] > 0 and slopes[1] < 0 and slopes[2] > 0,
        "asymptotic_slope": str(lam-a), "a_greater_than_lambda": a > lam,
    }


def build_report(precision: int = 80) -> dict:
    if type(precision) is not int or not 40 <= precision <= 200:
        raise ValueError("Precision must be integer 40..200")
    with localcontext() as ctx:
        ctx.prec = precision
        rows = [profile(D(1), D("1.5"), D(b), D(r))
                for b in ("-0.6", "0", "0.6") for r in (0, 1, 2, 5, 10, 20)]
        controls = [profile(D(1), a, D("0.6"), D(20))
                    for a in (D(10)/11, D(1), D("1.5"))]
        return core.stringify({
            "schema_version": 1, "audit_date": "2026-09-06", "precision": precision,
            "normalization_id": "NORM-EXPONENTIAL-CONTEXT-001", "source": SOURCE,
            "scope": "Conditional normalized scalar image, not metronic operator validation or F/G reconstruction",
            "parameter_provenance": "synthetic dimensionless examples (lambda=1 fixes an arbitrary length unit); no empirical values",
            "modern_reference_inputs": [], "target_fitting": False,
            "domain": "lambda>0, a>0, -1<b<1, r>=0; source-positive b branch is a subset; b=0 is (79a)",
            "normalization": "H(0)=1; tensor amplitude omitted by explicit choice; E=1",
            "exact_scalar_profile": "H=exp(lambda*r)*[(exp(2*lambda*r)-2*b*exp(lambda*r)+1)/(2*(1-b))]^(-a/(2*lambda))",
            "asymptotic_profile": "H~[2*(1-b)]^p*exp((lambda-a)*r), p=a/(2*lambda), ratio tends to 1",
            "relative_error_formula": "H/leading-1=(1-2*b*t+t^2)^(-p)-1, t=exp(-lambda*r)",
            "relative_error_bound": "For s=2*abs(b)*t+t^2<1, abs(error)<=p*s/(1-s)^(p+1), from mean value theorem",
            "stationary_polynomial": "(1-A)*w^2+b*(2*A-1)*w-A=0; A=lambda/a, w=exp(lambda*r)",
            "rows": rows, "asymptotic_controls": controls,
            "exact_extremum_counterexample": exact_counterexample(),
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
        print("Exponential context snapshot matches fresh calculation.")
    print("Conditional scalar rate reproduced: decay iff a>lambda on this domain.")
    print("Exact scalar counterexample: stationary radii ln(11/5), ln(5), but asymptotic growth.")
    print("No metronic operator, physical amplitude, or F/G identification is validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

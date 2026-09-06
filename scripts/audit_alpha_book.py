"""EDM2 (105): explicitly ex-post Y3 diagnostics and arithmetic-error checks.

Scope: NORM-BOOK-ALPHA-Y3-DIAGNOSTICS. Does not modify the first alpha audit.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from decimal import Decimal as D, ROUND_CEILING, ROUND_FLOOR, localcontext

import audit_alpha as core

OUTPUT = core.ROOT / "05_analysis/alpha_book_diagnostics.json"
ONE, TWO = D(1), D(2)


def required_rhs(inverse: D) -> D:
    if not inverse.is_finite() or inverse < ONE:
        raise ValueError("Inverse must be finite and at least 1")
    square = inverse*inverse
    return (square-ONE).sqrt()/square


def rhs_interval(bounds: tuple[D, D]) -> tuple[D, D]:
    lo, hi = bounds
    if not lo.is_finite() or not hi.is_finite() or not ONE <= lo <= hi:
        raise ValueError("Inverse interval must be finite, ordered and >=1")
    lows, highs = [], []
    for endpoint in bounds:
        square = endpoint*endpoint
        with localcontext() as ctx:
            ctx.rounding = ROUND_FLOOR
            lower_root = (square-ONE).sqrt()
            # Decimal.sqrt is correctly rounded HALF_EVEN irrespective of
            # context rounding. Expand by one representable value explicitly.
            lower_root = lower_root.next_minus() if lower_root else D(0)
            lows.append(lower_root/square)
            ctx.rounding = ROUND_CEILING
            upper_root = (square-ONE).sqrt()
            upper_root = upper_root.next_plus() if upper_root else D(0)
            highs.append(upper_root/square)
    maximum = ONE/TWO if lo*lo <= TWO <= hi*hi else max(highs)
    return min(lows), maximum


def implied_y3(inverse: D, base_rhs: D, product: D) -> D:
    if base_rhs <= 0 or product <= 0:
        raise ValueError("R0 and A1*A2 must be positive")
    return (ONE-required_rhs(inverse)/base_rhs)/product


def implied_y3_interval(bounds: tuple[D, D], base_rhs: D, product: D) -> tuple[D, D]:
    if base_rhs <= 0 or product <= 0:
        raise ValueError("R0 and A1*A2 must be positive")
    low_r, high_r = rhs_interval(bounds)
    with localcontext() as ctx:
        ctx.rounding = ROUND_CEILING
        high_ratio = high_r/base_rhs
        ctx.rounding = ROUND_FLOOR
        low_y = (ONE-high_ratio)/product
        low_ratio = low_r/base_rhs
        ctx.rounding = ROUND_CEILING
        high_y = (ONE-low_ratio)/product
    return low_y, high_y


def cancellation_diagnostic(rhs: D, printed_inverse_minus: str) -> dict:
    _, stable_large = core.solve_branches(rhs)
    exact_inverse = ONE/stable_large
    r64 = float(rhs)
    b64 = 1/(2*r64*r64)
    unstable64 = math.sqrt(b64*(1-math.sqrt(1-2/b64)))
    stable64 = 1/math.sqrt((1+math.sqrt(1-4*r64*r64))/2)
    decimal_trials = []
    for precision in (8, 10, 12, 16, 24):
        with localcontext() as ctx:
            ctx.prec = precision
            r = +rhs
            b = ONE/(TWO*r*r)
            trial = (b*(ONE-(ONE-TWO/b).sqrt())).sqrt()
        decimal_trials.append({"precision": precision, "inverse_minus": trial, "error_against_high_precision": trial-exact_inverse})
    return {
        "reference_inverse_minus": exact_inverse,
        "binary64_unstable_inverse_minus": repr(unstable64),
        "binary64_stable_inverse_minus": repr(stable64),
        "binary64_unstable_error": D.from_float(unstable64)-exact_inverse,
        "binary64_stable_error": D.from_float(stable64)-exact_inverse,
        "printed_inverse_minus_error": core.decimal_token(printed_inverse_minus)-exact_inverse,
        "decimal_cancellation_trials": decimal_trials,
        "interpretation": "Arithmetic experiments, not a reconstruction of the historical calculator or rounding policy",
    }


def build_report(inputs: dict, precision: int = 80) -> dict:
    if not 50 <= precision <= 200:
        raise ValueError("Diagnostic precision must be between 50 and 200")
    with localcontext() as ctx:
        ctx.prec = precision
        pi = core.mathematical_pi()
        printed = inputs["printed"]["1982"]
        reference = inputs["modern_reference"]
        modern_value = core.decimal_token(reference["value"])
        modern_uncertainty = core.decimal_token(reference["standard_uncertainty"])
        profiles = []
        for model in inputs["models"]:
            if model["equation"] != "1982":
                continue
            terms = core.equation_rhs(pi, model)
            product = terms["A1"]*terms["A2"]
            base_rhs = D(9)*terms["vartheta"]/(TWO*pi)**5
            targets = []
            for branch in ("plus", "minus"):
                token = printed[f"inverse_{branch}"]
                value = core.decimal_token(token)
                bounds = core.printing_interval(token)
                targets.append({
                    "target": f"printed_1982_inverse_{branch}", "input_literal": token,
                    "input_interval": bounds, "input_interval_kind": "conditional_printing_half_last_place",
                    "required_rhs": required_rhs(value),
                    "implied_y3": implied_y3(value, base_rhs, product),
                    "implied_y3_interval": implied_y3_interval(bounds, base_rhs, product),
                })
            modern_y = implied_y3(modern_value, base_rhs, product)
            modern_bounds = (modern_value-modern_uncertainty, modern_value+modern_uncertainty)
            targets.append({
                "target": "codata2022_inverse_plus", "input_literal": reference["value"],
                "input_interval": modern_bounds,
                "input_interval_kind": "reference_plus_minus_one_standard_uncertainty_not_theory_uncertainty",
                "required_rhs": required_rhs(modern_value), "implied_y3": modern_y,
                "implied_y3_interval": implied_y3_interval(modern_bounds, base_rhs, product),
            })
            _, calibrated_large = core.solve_branches(base_rhs*(ONE-product*modern_y))
            profiles.append({
                "model": model["id"], "original_interpretation_status": model["status"],
                "R0": base_rhs, "A1_A2": product, "targets": targets,
                "one_y3_can_fit_both_printed_branches": core.intervals_overlap(targets[0]["implied_y3_interval"], targets[1]["implied_y3_interval"]),
                "calibrated_companion_inverse": ONE/calibrated_large,
                "calibrated_companion_status": "algebraic consequence of fitting alpha, not an independently validated physical coupling",
                "cancellation_at_source_y3_1": cancellation_diagnostic(terms["rhs"], printed["inverse_minus"]),
            })
        input_hash = hashlib.sha256(json.dumps(inputs, sort_keys=True, ensure_ascii=True, separators=(",", ":")).encode("ascii")).hexdigest()
        return core.stringify({
            "schema_version": 1, "audit_date": "2026-09-06", "input_content_sha256": input_hash,
            "precision": precision, "pi_profile": "mathematical_pi",
            "source": "EDM2 printed pp301-302, equation105, Y3=1 numerical example",
            "normalization": "NORM-BOOK-ALPHA-Y3-DIAGNOSTICS",
            "diagnostic_scope": "Every inferred Y3 uses its target explicitly; this is calibration/diagnosis, never a prediction",
            "profiles": profiles,
            "modern_reference": reference,
        })


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    inputs = json.loads(core.INPUTS.read_text(encoding="utf-8"))
    report = build_report(inputs)
    encoded = json.dumps(report, ensure_ascii=False, indent=2)+"\n"
    if args.write:
        OUTPUT.write_text(encoded, encoding="utf-8", newline="\n")
        print(f"Wrote {OUTPUT.relative_to(core.ROOT).as_posix()}")
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != encoded:
            print("Diagnostic snapshot missing/stale; review before --write.")
            return 1
        print("Diagnostic snapshot matches fresh calculation.")
    for profile in report["profiles"]:
        print(f"{profile['model']}: common Y3 compatible={profile['one_y3_can_fit_both_printed_branches']}")
        for target in profile["targets"]:
            print(f"  {target['target']}: ex-post Y3={D(target['implied_y3']):.12f}")
        print(f"  binary64 cancellation error={profile['cancellation_at_source_y3_1']['binary64_unstable_error']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

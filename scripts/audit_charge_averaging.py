"""EDM1 (27b)-(29a): charge/energy means and an unfitted diagnostic family.

NORM-CHARGE-001. No modern reference data, no Y3, no complete mass model.
"""

from __future__ import annotations

import argparse
import json
from decimal import Decimal as D, localcontext

import audit_alpha as core

OUTPUT = core.ROOT / "05_analysis/charge_averaging_diagnostics.json"
ZERO, ONE, TWO, FOUR, EIGHT = map(D, (0, 1, 2, 4, 8))
SOURCE = {
    "path": "01_sources/heim_primary/Burkhard Heim - 1998 - Elementarstrukuren der Materie 1.pdf",
    "sha256": "49C79028C4F5B4FEE97F0541EF1655C37755C3C3C2FD3A10DD6E72CB454DE459",
    "url": "https://burkhardheim.de/assets/Burkhard%20Heim%20-%201998%20-%20Elementarstrukuren%20der%20Materie%201.pdf",
    "locator": "PDF251/253/254; printed245/247/248; (27b), (28), (28a), (29), (29a)",
    "edition": "Third changed edition1998; no unverified backdating to1980",
}
WEIGHTS = (D("0"), D("0.25"), D("0.5"), D("0.75"), D("1"))


def component_ratios(eta: D) -> dict[str, D]:
    if not eta.is_finite() or not ZERO < eta <= ONE:
        raise ValueError("Components require finite 0 < eta <= 1")
    t = eta.sqrt()
    return {"reduced": t, "difference": ONE-t, "mean": (ONE+t)/TWO}


def energy_mean_ratio(eta: D, weight: D) -> D:
    """Squared effective/raw charge ratio; weight multiplies reduced energy."""
    if not weight.is_finite() or not ZERO <= weight <= ONE:
        raise ValueError("Diagnostic weight must be finite and in [0,1]")
    components = component_ratios(eta)
    return weight*eta + (ONE-weight)*components["mean"]**2


def inverse_alpha_prime(pi: D, rho: D) -> D:
    if not pi.is_finite() or not rho.is_finite() or pi <= ZERO or rho <= ZERO:
        raise ValueError("pi and squared charge ratio must be positive and finite")
    return FOUR*pi**5/(D(9)*rho)


def build_report(precision: int = 80) -> dict:
    if not 40 <= precision <= 200:
        raise ValueError("Diagnostic precision must be between40 and200")
    with localcontext() as ctx:
        ctx.prec = precision
        pi = core.mathematical_pi()
        eta = pi/(pi**4+FOUR).sqrt().sqrt()
        components = component_ratios(eta)
        t = components["reduced"]
        vartheta = D(5)*eta+TWO*t+ONE
        rows = []
        for weight in WEIGHTS:
            rho = energy_mean_ratio(eta, weight)
            rows.append({
                "lambda": weight,
                "status": "source_equal_mean" if weight == D("0.5") else "our_unfitted_interpolation_not_a_source_assertion",
                "squared_effective_to_raw_charge_ratio": rho,
                "effective_to_raw_charge_ratio": rho.sqrt(),
                "theta_diagnostic": EIGHT*rho,
                "inverse_alpha_prime": inverse_alpha_prime(pi, rho),
            })
        source_row = rows[2]
        charge_mean_squared = ((components["reduced"]+components["mean"])/TWO)**2
        difference = (components["reduced"]-components["mean"])**2/FOUR
        printed = "137,038"
        bounds = core.printing_interval(printed)
        inverse = source_row["inverse_alpha_prime"]
        return core.stringify({
            "schema_version": 1, "audit_date": "2026-09-06", "precision": precision,
            "normalization_id": "NORM-CHARGE-001", "source": SOURCE,
            "scope": "Local conditional reconstruction of EDM1 (29a); lambda is our unfitted logical diagnostic, not Heim parameter or physical uncertainty",
            "modern_reference_inputs": [], "target_fitting": False,
            "pi": pi, "eta": eta, "component_to_raw_charge_ratios": components,
            "vartheta_source": vartheta,
            "equal_mean_identity_residual": EIGHT*source_row["squared_effective_to_raw_charge_ratio"]-vartheta,
            "profiles": rows,
            "equal_energy_mean_minus_squared_charge_mean": difference,
            "squared_arithmetic_charge_mean": charge_mean_squared,
            "d_rho_d_lambda": (D(3)*t+ONE)*(t-ONE)/FOUR,
            "printed_approximation_check": {
                "input_literal": printed, "conditional_rounding_interval": bounds,
                "computed_inverse_alpha_prime": inverse,
                "matches_printed_rounding": bounds[0] <= inverse <= bounds[1],
                "interpretation": "Arithmetic reproduction of the preliminary book approximation, not physical validation",
            },
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
        print("EDM1 source hash verified.")
    report = build_report(args.precision)
    encoded = json.dumps(report, ensure_ascii=False, indent=2)+"\n"
    if args.write:
        OUTPUT.write_text(encoded, encoding="utf-8", newline="\n")
        print(f"Wrote {OUTPUT.relative_to(core.ROOT).as_posix()}")
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != encoded:
            print("Diagnostic snapshot missing/stale; review before --write.")
            return 1
        print("Charge diagnostic snapshot matches fresh calculation.")
    for row in report["profiles"]:
        print(f"lambda={row['lambda']}: inverse_alpha_prime={D(row['inverse_alpha_prime']):.12f} [{row['status']}]")
    print(f"Printed137.038 reproduction: {report['printed_approximation_check']['matches_printed_rounding']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

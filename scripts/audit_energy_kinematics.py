"""Conditional EDM energy/wavelength diagnostics, not a repaired physical theory.

NORM-ENERGY-KINEMATICS-001. All reported quantities are dimensionless.
No modern measured inputs, fits, or changes to earlier source profiles.
"""

from __future__ import annotations

import argparse
import json
from decimal import Decimal as D, localcontext

import audit_alpha as core

OUTPUT = core.ROOT / "05_analysis/energy_kinematics_diagnostics.json"
ONE = D(1)
BETAS = tuple(map(D, ("0.001", "0.01", "0.1", "0.6", "0.9")))
SOURCES = [
    {
        "path": "01_sources/heim_primary/Burkhard Heim - 1998 - Elementarstrukuren der Materie 1.pdf",
        "sha256": "49C79028C4F5B4FEE97F0541EF1655C37755C3C3C2FD3A10DD6E72CB454DE459",
        "locator": "printed81/PDF88; printed288/PDF294; 1998 third changed edition",
    },
    {
        "path": "01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf",
        "sha256": "F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849",
        "locator": "printed267/PDF273 (98); printed300-302/PDF306-308 (105); 1996 second unchanged edition",
    },
]


def kinematic_ratios(beta: D) -> dict[str, D]:
    """Assume the same m=gamma*m0 and beta=v/c in all compared expressions."""
    if not beta.is_finite() or not D(0) < beta < ONE:
        raise ValueError("Kinematic ratios require finite 0 < beta < 1")
    # Product form preserves the near-one distance. Rationalization avoids
    # cancellation of 1-s for small beta, even when s itself rounds to one.
    s = ((ONE-beta)*(ONE+beta)).sqrt()
    kinetic_over_mc2 = beta**2/(ONE+s)
    return {
        "beta": beta,
        "s": s,
        "gamma": ONE/s,
        "source_pc_over_m0c2": beta/s,
        "kinetic_T_over_m0c2": kinetic_over_mc2/s,
        "source_pc_over_kinetic_T": (ONE+s)/beta,
        "source_pc_over_mc2": beta,
        "kinetic_T_over_mc2": kinetic_over_mc2,
        "lambda_dB_over_lambda_H": ONE/beta,
        "source_r_H_over_L0": s,
        "source_y_over_L0": (ONE-beta)*(ONE+beta),
        "K_source_pc": beta*s,
        "K_kinetic_energy_only": s*kinetic_over_mc2,
        "K_kinetic_energy_and_dB": beta*s/(ONE+s),
    }


def book_source_branch(pi: D) -> dict[str, D]:
    """Book-local q,k chain, Y3=1. No empirical alpha is imported."""
    eta = pi/(pi**4+D(4)).sqrt().sqrt()
    theta = D(5)*eta+D(2)*eta.sqrt()+ONE
    eta11 = core.eta_k_q(pi, k=1, q=1)
    eta12 = core.eta_k_q(pi, k=2, q=1)
    t1, t2 = eta11.sqrt(), eta12.sqrt()
    a1, a2 = t1*(ONE-t1)/(ONE+t1), t2*(ONE-t2)/(ONE+t2)
    alpha_prime = D(9)*theta/(D(2)*pi)**5
    correction_c = a1*a2
    k = alpha_prime*(ONE-correction_c)
    small, large = core.solve_branches(k)
    return {"pi": pi, "eta": eta, "vartheta": theta, "eta11": eta11,
            "eta12": eta12, "A1": a1, "A2": a2, "Y3": ONE,
            "C": correction_c, "alpha_prime": alpha_prime,
            "K": k, "small_beta": small, "large_beta": large}


def build_report(precision: int = 80) -> dict:
    if not 40 <= precision <= 200:
        raise ValueError("Diagnostic precision must be between 40 and 200")
    with localcontext() as ctx:
        ctx.prec = precision
        branch = book_source_branch(core.mathematical_pi())
        book_row = kinematic_ratios(branch["small_beta"])
        return core.stringify({
            "schema_version": 1, "audit_date": "2026-09-06", "precision": precision,
            "normalization_id": "NORM-ENERGY-KINEMATICS-001", "sources": SOURCES,
            "scope": "Conditional source meanings and unfitted forward diagnostics, not physical validation or a replacement theory",
            "modern_reference_inputs": [], "target_fitting": False,
            "all_numeric_outputs_dimensionless": True,
            "mass_bridge_assumption": "Same beta and m=gamma*m0 from EDM1 used in EDM2; m0 is a unit, not a supplied measured mass",
            "profile_status": {
                "source_pc": "conditional_source_reconstruction",
                "kinetic_energy_only": "our_unfitted_energy_substitution",
                "kinetic_energy_and_dB": "our_unfitted_energy_and_wavelength_substitutions",
            },
            "fixed_beta_examples": [kinematic_ratios(b) for b in BETAS],
            "book_Y3_one_profile": branch,
            "book_small_branch_ratios": book_row,
            "source_closure_residual": book_row["K_source_pc"]-branch["K"],
            "interpretation_limits": [
                "pc and T are different functions, not numerical errors",
                "h/p and h/(mc) conflict only when identified as the same wavelength at the same m,p,beta",
                "r_H/L0 and y/L0 are conditional lengths, not measured hydrogen radii",
                "No radius derivation from a full circular-motion Lorentz transformation has been established here",
                "The two substitution profiles retain other source assumptions; neither is a self-consistent alternative atom model",
            ],
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
        errors = core.verify_sources({"sources": SOURCES})
        if errors:
            print("\n".join(errors))
            return 1
        print("Both Heim book source hashes verified.")
    report = build_report(args.precision)
    encoded = json.dumps(report, ensure_ascii=False, indent=2)+"\n"
    if args.write:
        OUTPUT.write_text(encoded, encoding="utf-8", newline="\n")
        print(f"Wrote {OUTPUT.relative_to(core.ROOT).as_posix()}")
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != encoded:
            print("Diagnostic snapshot missing/stale; review before --write.")
            return 1
        print("Energy/wavelength diagnostic snapshot matches fresh calculation.")
    for row in report["fixed_beta_examples"]:
        print(f"beta={row['beta']}: pc/T={D(row['source_pc_over_kinetic_T']):.12f}; lambda_dB/lambda_H={D(row['lambda_dB_over_lambda_H']):.12f}")
    row = report["book_small_branch_ratios"]
    print(f"Unfitted book branch: beta={D(row['beta']):.12f}; pc/T={D(row['source_pc_over_kinetic_T']):.12f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

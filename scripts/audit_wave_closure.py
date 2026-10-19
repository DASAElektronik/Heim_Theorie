"""Explicit scalar-ring and phase diagnostics, not a solved Heim atom model.

NORM-WAVE-CLOSURE-001. All numeric outputs are dimensionless. The spatial
eigenproblem is proved in the accompanying note, not by these calculations.
No empirical alpha, fitted parameters, or source-profile changes.
"""

from __future__ import annotations

import argparse
import json
from decimal import Decimal as D, localcontext
from fractions import Fraction as F

import audit_energy_kinematics as energy

core = energy.core
ONE = D(1)
OUTPUT = core.ROOT / "05_analysis/wave_closure_diagnostics.json"
SOURCES = [
    *[dict(row) for row in energy.SOURCES],
    {
        "path": "01_sources/heim_primary/author_rationale_search/M0042-Magnetfeld-und-Drehimpuls-B-Heim-1981.pdf",
        "sha256": "CACC6E9258CB106A82409C908C5E8E940B9F2DA447DBC7EA391C6C9CE9AA8A11",
        "locator": "manuscript5/PDF5: wave/closure rationale; not normalized as numeric input",
    },
    {
        "path": "01_sources/mainstream_reference/deBroglie_1929_Nobel_Lecture.pdf",
        "sha256": "52502BF6DE0F7C46058D049ED14D821D0DF710345187010F289F64F9918DB144",
        "locator": "printed247-249/PDF4-6: English Nobel Lecture, historical free-particle reference only",
    },
]


def positive(value: D, name: str) -> D:
    if not isinstance(value, D) or not value.is_finite() or value <= 0:
        raise ValueError(f"{name} must be a finite positive Decimal")
    return value


def mode_number(n: int, *, nonzero: bool = True) -> int:
    if type(n) is not int or (nonzero and n == 0):
        raise ValueError("Expected a nonzero integer mode" if nonzero else "Expected an integer mode")
    return abs(n)


def scalar_mode(n: int) -> dict:
    """Consequences of a periodic scalar field; positive operator -d2/dphi2."""
    size = mode_number(n, nonzero=False)
    return {
        "n": n, "angular_laplacian_eigenvalue": n*n,
        "constant_spatial_mode": size == 0,
        "wavelength_over_circumference": ONE/D(size) if size else None,
        "travelling_angular_generator_over_hbar": n,
        "balanced_standing_generator_mean_over_hbar": 0,
        "balanced_standing_generator_square_over_hbar2": n*n,
    }


def wave_ratios(beta: D, zeta: D, n: int = 1) -> dict:
    """Same-frame mc2=h nu, nu=zeta*c/lambda; y=R*s is retained, not proved."""
    size = D(mode_number(n))
    positive(zeta, "phase-speed ratio")
    r = energy.kinematic_ratios(beta)
    return {
        "beta": beta, "zeta": zeta, "n": n, "s": r["s"],
        "lambda_over_h_mc": zeta,
        "R_over_hbar_mc": size*zeta,
        "component_pwave_over_mc": ONE/zeta,
        "corpuscular_p_over_mc": beta,
        "component_pwave_over_corpuscular_p": ONE/(zeta*beta),
        "same_wave_required_zeta": ONE/beta,
        "K_pc": size*zeta*beta*r["s"],
        "K_T_comparator": size*zeta*r["kinetic_T_over_mc2"]*r["s"],
    }


def correction_family(alpha_prime: D, product: D, rho: D, y3: D) -> dict:
    """Our extra proportionality factor rho; not a source-authorized fit.

    C here is our effective correction rho*P*Y3, not a quoted source
    definition including Y3. Only rho*Y3 is identified by this term. P is
    the book's A1*A2, never silently the manuscript's differently defined Ak.
    """
    positive(alpha_prime, "alpha prime")
    positive(product, "book A1*A2")
    positive(rho, "our proportionality factor")
    if not isinstance(y3, D) or not y3.is_finite() or y3 == 0:
        raise ValueError("Y3 must be finite and nonzero")
    effective = rho*y3
    correction = product*effective
    return {"rho": rho, "Y3": y3, "rho_times_Y3": effective,
            "C": correction, "K": alpha_prime*(ONE-correction)}


def constant_phase_branches(k: D, n: int = 1, zeta: D = ONE) -> dict:
    """Solve K=N*zeta*beta*sqrt(1-beta2) for fixed phase speed and pc energy."""
    size = D(mode_number(n))
    positive(k, "K")
    positive(zeta, "phase-speed ratio")
    exact_scaled = F(k)/(F(size)*F(zeta))
    if exact_scaled > F(1, 2):
        raise ValueError("This closure requires exact 0 < K/(abs(n)*zeta) <= 1/2")
    scaled = k/(size*zeta)
    if exact_scaled == F(1, 2):
        # The coincident root must be rounded once, not independently via
        # sqrt(1/2) and (1/2)/sqrt(1/2), which can reverse their ordering.
        small = large = D("0.5").sqrt()
    else:
        if not D(0) < scaled < D("0.5"):
            raise ArithmeticError("Insufficient precision to distinguish the maximum")
        small, large = core.solve_branches(scaled)
    if not D(0) < small <= large < ONE:
        raise ArithmeticError("Insufficient precision for interior branch separation")
    return {"n": n, "zeta": zeta, "K": k, "small_beta": small,
            "large_beta": large, "inverse_small_beta": ONE/small,
            "inverse_large_beta": ONE/large}


def same_wave_pc_branch(k: D, n: int = 1) -> dict:
    """Own substitution zeta=1/beta, retaining pc and y=Rs: K=N*s.

    This is not a full dispersion/bound-state solution. Endpoints and
    insufficient precision are rejected rather than reported as massive roots.
    """
    size = D(mode_number(n))
    positive(k, "K")
    exact_s = F(k)/F(size)
    if not 0 < exact_s < 1:
        raise ValueError("This interior branch requires exact 0 < K/abs(n) < 1")
    s = k/size
    if not D(0) < s < ONE:
        raise ArithmeticError("Insufficient precision to distinguish the endpoint")
    beta = ((ONE-s)*(ONE+s)).sqrt()
    if not D(0) < beta < ONE:
        raise ArithmeticError("Insufficient precision for interior beta")
    return {"n": n, "K": k, "s": s, "beta": beta,
            "zeta": ONE/beta, "inverse_beta": ONE/beta}


def build_report(precision: int = 80) -> dict:
    if type(precision) is not int or not 40 <= precision <= 200:
        raise ValueError("Diagnostic precision must be an integer from 40 to 200")
    with localcontext() as ctx:
        ctx.prec = precision
        book = energy.book_source_branch(core.mathematical_pi())
        k = book["K"]
        pairs = (("1", "1"), ("2", "0.5"), ("0.5", "2"))
        return core.stringify({
            "schema_version": 1, "audit_date": "2026-09-06", "precision": precision,
            "normalization_id": "NORM-WAVE-CLOSURE-001", "sources": SOURCES,
            "scope": "Own scalar-ring closure diagnostics, not a reconstructed Heim eigenproblem or a physical replacement theory",
            "modern_reference_inputs": [], "target_fitting": False,
            "all_numeric_outputs_dimensionless": True,
            "definitions": {"N": "abs(n), nonzero integer ring mode",
                            "angular_laplacian_eigenvalue": "n^2 for the positive operator -d2/dphi2",
                            "zeta": "positive phase-speed magnitude/c, not group or particle speed",
                            "f": "energy in balance divided by mc2; source-like f=beta",
                            "K": "alpha_prime*(1-C) = N*zeta*f*sqrt(1-beta2)",
                            "rho": "our additional proportionality multiplier, not a new source constant"},
            "scalar_spatial_modes": [scalar_mode(n) for n in (-2, -1, 0, 1, 2)],
            "fixed_beta_examples": [wave_ratios(D("0.6"), zeta, n)
                                    for n, zeta in ((1, ONE), (2, ONE), (1, D(5)/3))],
            "book_Y3_one_profile": book,
            "constant_c_phase_forward_diagnostics": [constant_phase_branches(k, n) for n in (1, 2, 3)],
            "same_wave_pc_forward_diagnostic": same_wave_pc_branch(k),
            "proportionality_degeneracy": [correction_family(book["alpha_prime"], book["C"], D(r), D(y))
                                         for r, y in pairs],
            "interpretation_limits": [
                "Scalar periodic S1 is our assumption; source shell is described as spherical and standing",
                "Periodicity alone supplies neither n=1, radius, temporal dynamics, nor a beta branch",
                "n=0 is valid spatially; finite-wavelength diagnostics exclude it, not the hydrogen ground state",
                "p_wave denotes travelling tangential component magnitude, not total standing-wave or Cartesian momentum",
                "Same-wave identification requires same frame, energy and momentum conventions; field effects unresolved",
                "Retaining y=R*s and pc does not resolve the earlier energy-order or Lorentz-geometry issues",
                "Manuscript Ak and Y are not substituted into book Ak and Y3",
                "All mode/parameter examples are preselected, not fitted or physically validated alpha predictions",
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
        print("Books, manuscript and historical phase-reference hashes verified.")
    report = build_report(args.precision)
    encoded = json.dumps(report, ensure_ascii=False, indent=2)+"\n"
    if args.write:
        OUTPUT.write_text(encoded, encoding="utf-8", newline="\n")
        print(f"Wrote {OUTPUT.relative_to(core.ROOT).as_posix()}")
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != encoded:
            print("Wave closure snapshot missing/stale; review before --write.")
            return 1
        print("Wave closure snapshot matches fresh calculation.")
    for row in report["constant_c_phase_forward_diagnostics"]:
        print(f"Own ring N={row['n']}: inverse small beta={D(row['inverse_small_beta']):.12f}")
    row = report["same_wave_pc_forward_diagnostic"]
    print(f"Own same-wave substitution retaining pc: beta={D(row['beta']):.12f}; not a validated alpha prediction.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

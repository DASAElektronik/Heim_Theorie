"""Fixed 64-cell H006/H010 electron N0 comparison; never execute foreign code.

Real-arithmetic idealization, analytic K4 certificate and historical-only
output comparison. No target-based choice of formulas or particle states.
"""

from __future__ import annotations

import argparse
import json
from decimal import Decimal as D, localcontext

import audit_alpha as core
import audit_n0_electron as n0

INPUTS = core.ROOT / "04_reconstruction/alpha_audit/historical_n0_inputs.json"
OUTPUT = core.ROOT / "05_analysis/historical_n0_results.json"
AXES = ("a3_first_power", "a3_root_factor", "alpha_input", "xi", "hbar", "gamma")
ONE, TWO, THREE = D(1), D(2), D(3)
BASELINE = dict(pi="mathematical", e_base="mathematical", xi="1.61803399",
                alpha_model="1982_source_literal", eta12_k=1, eta12_q=2,
                a3_first_power=3, a3_root_factor="sqrt_xi_times_d_inside_root",
                hbar_Js="1.0545887e-34", gamma_m3_per_kg_s2="6.6732e-11")
HISTORICAL = dict(pi="mathematical_real_arithmetic_idealization",
                  e_base="mathematical_real_arithmetic_idealization", xi="golden_ratio",
                  alpha_inverse="137.03599976", beta_inverse="1.00001411",
                  a3_first_power=1, a3_root_factor="xi_times_d_without_root",
                  hbar_Js="1.054571596e-34", gamma_m3_per_kg_s2="6.6733198e-11")


def validate_inputs(inputs: dict) -> None:
    if inputs["state"] != n0.STATE or inputs["axes_in_forward_order"] != list(AXES):
        raise ValueError("Only the declared state and six ordered axes are supported")
    if inputs["baseline"] != BASELINE or inputs["historical"] != HISTORICAL:
        raise ValueError("Formula and constant profiles are frozen; review changes first")
    if inputs["shared"] != dict(c_m_per_s="2.99792458e8", s0_m="1"):
        raise ValueError("Shared constants differ from the frozen contract")
    if inputs["units"]["comparison_factor_kg_to_MeV_c2"] != "5.6095892e29":
        raise ValueError("Only the historical conversion is supported")
    if inputs["target_fitting"] is not False:
        raise ValueError("No target fitting permitted")


def evaluate_cell(mask: int, inputs: dict, *, alternate_root_scope=False) -> dict:
    """Mask bit 0 follows AXES[0]; no comparison value is read here."""
    validate_inputs(inputs)
    if type(mask) is not int or not 0 <= mask < 64:
        raise ValueError("Mask must be an integer in 0..63")
    if alternate_root_scope and mask != 0:
        raise ValueError("Additional root reading is restricted to the baseline")
    active = {axis for bit, axis in enumerate(AXES) if mask & (1 << bit)}
    base, hist = inputs["baseline"], inputs["historical"]
    pi, eb = core.mathematical_pi(), ONE.exp()
    xi = (ONE+D(5).sqrt())/TWO if "xi" in active else D(base["xi"])
    eta = pi/(pi**4+4).sqrt().sqrt()
    d = core.eta_k_q(pi, k=1, q=1)
    s = d.sqrt()
    alpha_h006, beta_h006 = core.solve_branches(core.equation_rhs(pi,
        dict(id="1982_source_literal", equation="1982", eta12_k=1, eta12_q=2))["rhs"])
    alpha = ONE/D(hist["alpha_inverse"]) if "alpha_input" in active else alpha_h006
    beta_h010 = ONE/D(hist["beta_inverse"])
    # Both beta profiles must be regular BEFORE reducing zero coefficients.
    a36 = {name: ONE-pi*eb*(xi*eb)**2*(ONE-beta**2)
           for name, beta in (("H006", beta_h006), ("H010", beta_h010))}
    if any(not v.is_finite() or v <= 0 for v in a36.values()):
        raise ValueError("A36 domain check failed")
    power = hist["a3_first_power"] if "a3_first_power" in active else base["a3_first_power"]
    root_factor = xi*d if "a3_root_factor" in active else (xi*d).sqrt()
    if alternate_root_scope:
        root_factor = xi.sqrt()*d
    a3_first = alpha*xi**3*(ONE+s)**power/(THREE*d**3)
    a3_second = TWO*root_factor/eb*((ONE-s)/(ONE+s))**2
    a1, a2, a3 = (ONE+s)/TWO, ONE/d, ONE-a3_first-a3_second
    selection = n0.zero_selection(a1, a2, a3)
    t = ONE-TWO/THREE*xi*eta**2*(ONE-eta.sqrt())
    ap = t/(eta**2*n0.cbrt(eta))-ONE
    am = t/(eta*n0.cbrt(eta))-ONE
    if not ZERO < am < ap:
        raise ValueError("Invalid mass factors")
    # Reduced N0 expressions; the old full H006 evaluation stays untouched.
    G = 144*a1+56*a2+12*a3+4
    L = 12*s/pi*(ONE-alpha/THREE)*(ONE+4*pi*alpha/(eta*eta.sqrt()))+8*alpha/xi**2
    phi = (ONE-am/ap)*L+4*am/ap
    hbar = D(hist["hbar_Js"] if "hbar" in active else base["hbar_Js"])
    gamma = D(hist["gamma_m3_per_kg_s2"] if "gamma" in active else base["gamma_m3_per_kg_s2"])
    speed, s0 = (D(inputs["shared"][key]) for key in ("c_m_per_s", "s0_m"))
    mu = pi.sqrt().sqrt()*n0.cbrt(3*pi*s0*gamma*hbar)*(hbar/(3*speed*gamma)).sqrt()/s0
    mass = mu*ap*(G+phi)
    step = 4*mu*ap
    conversion = D(inputs["units"]["comparison_factor_kg_to_MeV_c2"])
    return dict(mask=mask, changed_axes=[axis for axis in AXES if axis in active],
                alternate_root_scope=bool(alternate_root_scope), alpha=alpha, xi=xi,
                alpha3=a3, alpha3_subtrahends=[a3_first, a3_second],
                mass_plus=ap, mass_minus=am, G_aux=G, Phi_aux=phi, L_reduced=L,
                A36_denominators=a36, mu_kg=mu, mass_kg=mass,
                mass_MeV_c2=mass*conversion,
                one_n4_step_kg=step, diagnostic_n4_minus1_mass_kg=mass-step,
                diagnostic_n4_minus1_mass_MeV_c2=(mass-step)*conversion,
                occupations=selection["occupations"],
                first_three_upper_margins=[v["upper_margin"] for v in selection["greedy_steps"]],
                K4_method=selection["integerization_method"])


ZERO = D(0)


def attribution(rows: list[dict], order) -> list[dict]:
    order = tuple(order)
    if sorted(order) != list(range(len(AXES))):
        raise ValueError("Attribution order must be a permutation of all six axes")
    mask = 0
    steps = []
    for bit in order:
        after = mask | (1 << bit)
        delta = rows[after]["mass_kg"]-rows[mask]["mass_kg"]
        steps.append(dict(axis=AXES[bit], before_mask=mask, after_mask=after,
                          delta_kg=delta, ppm_of_baseline=delta/rows[0]["mass_kg"]*D("1e6")))
        mask = after
    return steps


def build_report(precision: int = 80, inputs: dict | None = None) -> dict:
    if type(precision) is not int or not 40 <= precision <= 200:
        raise ValueError("Precision must be an integer between 40 and 200")
    if inputs is None:
        inputs = json.loads(INPUTS.read_text(encoding="utf-8"))
    validate_inputs(inputs)
    with localcontext() as ctx:
        ctx.prec = precision
        rows = [evaluate_cell(mask, inputs) for mask in range(64)]
        extra = evaluate_cell(0, inputs, alternate_root_scope=True)
        forward = attribution(rows, range(6))
        reverse = attribution(rows, reversed(range(6)))
        ranges = []
        for bit, axis in enumerate(AXES):
            deltas = [rows[mask | (1 << bit)]["mass_kg"]-rows[mask]["mass_kg"]
                      for mask in range(64) if not mask & (1 << bit)]
            ranges.append(dict(axis=axis, min_delta_kg=min(deltas), max_delta_kg=max(deltas),
                alone_delta_kg=rows[1 << bit]["mass_kg"]-rows[0]["mass_kg"]))
        total = rows[63]["mass_kg"]-rows[0]["mass_kg"]
        # This is the ONLY use of the stored output mass. It cannot affect cells.
        saved = D(inputs["comparison_only"]["saved_program_mass_MeV_c2"])
        comparison = dict(saved_program_mass_MeV_c2=saved,
            own_historical_minus_saved_MeV_c2=rows[63]["mass_MeV_c2"]-saved,
            relative_to_saved=(rows[63]["mass_MeV_c2"]-saved)/saved,
            total_delta_kg=total, total_ppm_of_baseline=total/rows[0]["mass_kg"]*D("1e6"),
            forward_telescope_residual=sum(v["delta_kg"] for v in forward)-total,
            reverse_telescope_residual=sum(v["delta_kg"] for v in reverse)-total,
            sum_of_isolated_deltas_minus_total=sum(v["alone_delta_kg"] for v in ranges)-total,
            alternate_root_scope_delta_kg=extra["mass_kg"]-rows[0]["mass_kg"])
        return core.stringify(dict(schema_version=1, precision=precision, inputs=inputs,
            cells=rows, baseline_alternate_root_scope=extra, forward_attribution=forward,
            reverse_attribution=reverse, marginal_ranges=ranges, comparison=comparison,
            limits="Not historical binary replay, a modern empirical test, or a derivation of alpha3"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=80)
    parser.add_argument("--verify-sources", action="store_true")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    inputs = json.loads(INPUTS.read_text(encoding="utf-8"))
    if args.verify_sources:
        errors = core.verify_sources(inputs)
        if errors:
            print("\n".join(errors))
            return 1
        print("H006 and three H010 file hashes verified.")
    report = build_report(args.precision, inputs)
    encoded = json.dumps(report, ensure_ascii=False, indent=2)+"\n"
    if args.write:
        OUTPUT.write_text(encoded, encoding="utf-8", newline="\n")
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != encoded:
            print("Historical N0 snapshot missing/stale; review before --write.")
            return 1
        print("Historical N0 snapshot matches fresh calculation.")
    for label, mask in (("H006 baseline", 0), ("H010 real-arithmetic profile", 63)):
        row = report["cells"][mask]
        print(f"{label}: {D(row['mass_kg']):.14E} kg; {D(row['mass_MeV_c2']):.14f} MeV/c^2")
    print(f"Difference: {D(report['comparison']['total_ppm_of_baseline']):.8f} ppm of baseline")
    print("64 fixed counterfactual cells; no foreign execution, target fitting or modern reference.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

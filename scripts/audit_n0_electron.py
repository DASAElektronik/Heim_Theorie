"""H006-only x2/e-, N=0: explicit XXVI selection and conditional mass.

NORM-N0-ELECTRON-AUDIT. No empirical inputs, foreign code execution, or
general multiplet enumeration. Literal XIV is a separate conflict.
"""

from __future__ import annotations

import argparse
import json
from decimal import Decimal as D, ROUND_FLOOR, localcontext

import audit_alpha as core

INPUTS = core.ROOT / "04_reconstruction/alpha_audit/n0_electron_inputs.json"
OUTPUT = core.ROOT / "05_analysis/n0_electron_results.json"
ZERO, ONE, TWO, THREE = map(D, (0, 1, 2, 3))
STATE = dict(multiplet="x2", component="e-", epsilon=1, k=1, P=1, Q=1,
             kappa=0, C=0, x=1, qx=-1, q=1, N=0)


def cbrt(value: D) -> D:
    if not value.is_finite() or value <= 0:
        raise ValueError("Positive finite cube-root argument required")
    return (value.ln()/THREE).exp()


def auxiliary_terms(n, nj_coeff, qj=(3, 3, 2, 1)) -> dict:
    """XI polynomials; includes negative occupations, not a state selector."""
    if len(n) != 4 or any(type(x) is not int for x in n):
        raise ValueError("Four integer occupations required")
    if any(x < -q for x, q in zip(n, qj)):
        raise ValueError("H006 requires K_j=n_j+Q_j >= 0")
    n1, n2, n3, n4 = n
    q1, q2, q3, q4 = qj
    N1, N2, N3 = nj_coeff
    def polynomial(a, b, c, d):
        return a*a*(1+a)**2*N1 + b*(2*b*b+3*b+1)*N2 + c*(1+c)*N3 + 4*d
    K = polynomial(n1, n2, n3, n4)
    G = polynomial(q1, q2, q3, q4)
    H = (2*n1*q1*(1+3*(n1+q1+n1*q1)+2*(n1*n1+q1*q1))*N1
         + 6*n2*q2*(1+n2+q2)*N2 + 2*n3*q3*N3)
    shifted = polynomial(n1+q1, n2+q2, n3+q3, n4+q4)
    return dict(K=K, G=G, H=H, shifted_sum=shifted,
                shifted_identity_residual=K+G+H-shifted)


def zero_selection(a1: D, a2: D, a3: D) -> dict:
    """Only W=g at k=1. Final integer has an analytic identity certificate."""
    if any(not x.is_finite() or x <= 0 for x in (a1, a2, a3)):
        raise ValueError("Positive finite selection coefficients required")
    exponential = (-ONE/THREE).exp()
    g = 27*a1+9*a2+2*a3+exponential
    remaining = g
    integers, trace = [], []
    for coeff, exponent in ((a1, 3), (a2, 2), (a3, 1)):
        # This bounded case has tiny integers. No floating root rounding.
        integer = 0
        while coeff*(integer+1)**exponent <= remaining:
            integer += 1
            if integer > 100:
                raise ValueError("Outside bounded electron selection domain")
        residual = remaining-coeff*integer**exponent
        trace.append(dict(K=integer, remaining_before=remaining, residual=residual,
                          upper_margin=coeff*(integer+1)**exponent-remaining))
        integers.append(integer)
        remaining = residual
    if integers != [3, 3, 2]:
        raise ValueError("W=g zero-state certificate requires K1..3=(3,3,2)")
    if not ZERO < remaining <= ONE:
        raise ValueError("This case requires source W4 branch (b)")
    raw = -THREE*remaining.ln()
    # Algebra: W=g and K1..3=Q1..3 imply W4=exp(-1/3) EXACTLY.
    # Therefore -3 ln W4=1. No decimal epsilon or generic promotion rule.
    integers.append(1)
    occupations = [x-q for x, q in zip(integers, (3, 3, 2, 1))]
    xiii = [2*a3-1, 9*a2-2*a3, 27*a3-9*a2]  # printed alpha3 at right
    xxxii = [2*a3-1, 18*a2-6*a3, 162*a1-84*a2]
    if min(xiii+xxxii) < 0:
        raise ValueError("Printed structural inequality failed")
    return dict(W=g, w=1, f=0, integers=integers, occupations=occupations,
                greedy_steps=trace, W4_raw=remaining, W4_exact_expression="exp(-1/3)",
                W4_cancellation_residual=remaining-exponential, raw_K4=raw,
                integerized_K4=1, integerization_method="analytic_identity_W_equals_g",
                naive_decimal_floor=int(raw.to_integral_value(rounding=ROUND_FLOOR)),
                XIII_margins=xiii, XXXII_margins=xxxii,
                XIV_minus_XXVI_at_zero=(ONE/THREE).exp()-exponential)


def evaluate_profile(profile: dict, inputs: dict) -> dict:
    if inputs["state"] != STATE:
        raise ValueError("Only the frozen H006 x2/e-, N=0 state is implemented")
    if inputs["alpha_model"] != dict(id="1982_source_literal", equation="1982", eta12_k=1, eta12_q=2):
        raise ValueError("Only the declared source-literal alpha profile is implemented")
    if inputs["experimental_inputs"] or inputs["target_fitting"]:
        raise ValueError("This audit must not use empirical inputs or target fitting")
    pi = core.mathematical_pi() if profile["pi"] == "mathematical" else D(profile["pi"])
    eb = ONE.exp() if profile["e_base"] == "mathematical" else D(profile["e_base"])
    xi = (ONE+D(5).sqrt())/TWO if profile["xi"] == "golden_ratio" else D(profile["xi"])
    eta = pi/(pi**4+4).sqrt().sqrt()
    d = core.eta_k_q(pi, k=1, q=1)
    s = d.sqrt()
    alpha, beta = core.solve_branches(core.equation_rhs(pi, inputs["alpha_model"])["rhs"])
    t = ONE-TWO/THREE*xi*eta**2*(ONE-eta.sqrt())
    mass_plus = t/(eta**2*cbrt(eta))-ONE
    mass_minus = t/(eta*cbrt(eta))-ONE
    if mass_plus <= 0 or mass_minus <= 0:
        raise ValueError("Positive AUX mass factors required")
    ratio = mass_minus/mass_plus
    a1, a2 = (ONE+s)/TWO, ONE/d
    a3 = ONE-(alpha/THREE*((ONE+s)*(xi/d**2))**3*d**3
              + (ONE/eb)*(TWO*(xi*d).sqrt())*((ONE-s)/(ONE+s))**2)
    # Finite original matrix coefficients before multiplying their zero factors.
    a36_denominator = ONE-pi*eb*(xi*eb)**2*(ONE-beta**2)
    a24 = TWO*xi**2/(THREE*eta)
    domains = dict(eta=eta, eta11=d, alpha=alpha, mass_plus=mass_plus,
                   A36_denominator=a36_denominator, XVIII_A24_denominator=ONE,
                   XVI_alternate_A24_denominator=ONE-a24,
                   three_minus_q=TWO, eight_minus_A66_power=D(7))
    if any(not v.is_finite() or v == 0 for v in domains.values()):
        raise ValueError("Zero or nonfinite domain value before zero reduction")
    selection = zero_selection(a1, a2, a3)
    n = selection["occupations"]
    Nj = (a1, TWO*a2/THREE, TWO*a3)
    parts = auxiliary_terms(n, Nj)
    # Nine factors from the existing XI normalization, evaluated for fixed state.
    phi_factors = [THREE/(pi*s), ONE-ratio, TWO, ONE-alpha/THREE,
                   ONE, ONE, TWO*s*s, ONE+4*pi*alpha/(eta*eta.sqrt()),
                   ONE+D(n[0])/THREE]
    product = ONE
    for factor in phi_factors:
        product *= factor
    phi_add1, phi_add2 = 8*(ONE-ratio)*alpha/xi**2, 4*ratio
    phi = product+phi_add1+phi_add2
    phi_reduced = ((ONE-ratio)*(12*s/pi*(ONE-alpha/THREE)
                   *(ONE+4*pi*alpha/(eta*eta.sqrt()))*(ONE+D(n[0])/THREE)
                   + 8*alpha/xi**2)+4*ratio)
    constants = inputs["dimensional_constants"]
    hbar, speed, gamma, s0 = (D(constants[key]) for key in
        ("hbar_Js", "c_m_per_s", "gamma_m3_per_kg_s2", "s0_m"))
    mu = pi.sqrt().sqrt()*cbrt(3*pi*gamma*hbar*s0)*(hbar/(3*speed*gamma)).sqrt()/s0
    scale = mu*mass_plus
    return dict(profile=profile, pure_numbers=dict(pi=pi, e_base=eb, xi=xi),
                alpha=alpha, beta=beta, alpha_inverse=ONE/alpha,
                eta=eta, eta11=d, alpha_mass_plus=mass_plus, alpha_mass_minus=mass_minus,
                selection_coefficients=[a1, a2, a3], N_coefficients=Nj, Qj=[3, 3, 2, 1],
                domain_checks=domains, selection=selection,
                mass_terms=dict(K_aux=parts["K"], G_aux=parts["G"], H_aux=parts["H"],
                                Phi_aux=phi, Phi_factors=phi_factors,
                                Phi_addends=[phi_add1, phi_add2]),
                identity_residuals=dict(KGH=parts["shifted_identity_residual"],
                                        Phi=phi-phi_reduced),
                mu_kg=mu, mass_element_scale_kg=scale,
                contribution_kg={key: scale*value for key, value in
                                 (("K", parts["K"]), ("G", parts["G"]),
                                  ("H", parts["H"]), ("Phi", phi))},
                mass_kg=scale*(parts["K"]+parts["G"]+parts["H"]+phi),
                diagnostic_one_n4_step_kg=4*scale)


def build_report(precision: int = 80) -> dict:
    if not 40 <= precision <= 200:
        raise ValueError("Precision must be between 40 and 200")
    inputs = json.loads(INPUTS.read_text(encoding="utf-8"))
    with localcontext() as ctx:
        ctx.prec = precision
        return core.stringify(dict(schema_version=1, precision=precision, inputs=inputs,
            scope="Conditional H006 explicit N0 pathway; XIV conflict retained; no modern mass comparison",
            profiles=[evaluate_profile(p, inputs) for p in inputs["profiles"]]))


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
        errors = core.verify_sources({"sources": [inputs["source"]]})
        if errors:
            print("\n".join(errors))
            return 1
        print("H006 source hash verified.")
    report = build_report(args.precision)
    encoded = json.dumps(report, ensure_ascii=False, indent=2)+"\n"
    if args.write:
        OUTPUT.write_text(encoded, encoding="utf-8", newline="\n")
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != encoded:
            print("N0 snapshot missing/stale; review before --write.")
            return 1
        print("N0 snapshot matches fresh calculation.")
    for row in report["profiles"]:
        print(f"{row['profile']['id']}: n={row['selection']['occupations']}, mass={D(row['mass_kg']):.12E} kg")
    print("Explicit XXVI pathway only; no empirical validation or XIV repair.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

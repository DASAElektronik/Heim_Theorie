"""H006 x3/mu-, N=0: source-bound W and selection only, never a mass.

Twelve predeclared coefficient/reading profiles; no fit/measurement input.
Decimal stability is not a certified interval or physical uncertainty bound.
Only pure alpha arithmetic is reused; no old mass evaluator is called.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal as D, ROUND_FLOOR, localcontext

import audit_alpha as core

INPUTS = core.ROOT / "04_reconstruction/alpha_audit/muon_selection_inputs.json"
OUTPUT = core.ROOT / "05_analysis/muon_selection_results.json"
ZERO, ONE, TWO, THREE = map(D, (0, 1, 2, 3))
STATE = dict(multiplet="x3", component="mu-", epsilon=1, k=1, P=1, Q=1,
             kappa=1, C=0, component_indices=[0, 1], qx=-1, q=1, N=0)
PROFILES = [
    dict(id="h006_math_pi_e_printed_xi", pi="mathematical", e_base="mathematical", xi="1.61803399"),
    dict(id="h006_math_pi_e_golden_xi", pi="mathematical", e_base="mathematical", xi="golden_ratio"),
    dict(id="h006_printed_pure_number_inputs", pi="3.1415926535", e_base="2.71828183", xi="1.61803399"),
]
A16_READINGS = ["denominator_product", "left_associative_sensitivity"]
ROOT_READINGS = ["sqrt_xi_times_d", "sqrt_xi_then_times_d_sensitivity"]
ALPHA_MODEL = dict(id="1982_source_literal", equation="1982", eta12_k=1, eta12_q=2)
FIXED_POLICY = dict(
    schema_version=1, audit_date="2026-09-06", normalization_id="NORM-MUON-SELECTION-AUDIT",
    source=dict(
        id="H006", path="01_sources/heim_primary/Massenformel_nach_B_Heim_1982.pdf",
        sha256="F74DA0DAC8496BCD01226F54D88598152D67E1C954943AF61D0EC1811F5527BE",
        locator="Printed/PDF2-9: I-III, V, VII, IX/X, XIII, XV-XIX, A16/A26/A31 in XXIV, XXV/XXVI and p9 selection/XXXII",
        provenance="Heim-attributed 1982 material in IGW 2002/2003 rendering; not authenticated original",
    ),
    exp_ln_policy="mathematical natural functions even when the coefficient e_base is a printed numeral",
    selection_path="grouped XV/XXVI/XXX/XXXI; literal XIV excluded, not corrected",
    comparison_or_fit_inputs=[], dimensional_constants={}, target_fitting=False, mass_evaluation=False,
)


def validate_inputs(inputs):
    allowed = set(FIXED_POLICY) | {"audit_date", "source", "state", "profiles", "alpha_model",
                                  "a16_readings", "alpha3_root_readings", "default_a16_reading",
                                  "default_alpha3_root_reading"}
    if set(inputs) != allowed:
        raise ValueError("Unexpected or missing input fields")
    for key, value in FIXED_POLICY.items():
        if json.dumps(inputs[key], sort_keys=True) != json.dumps(value, sort_keys=True):
            raise ValueError(f"Fixed scope/policy field: {key}")
    # JSON comparison also rejects bool values substituted for integer states.
    if json.dumps(inputs["state"], sort_keys=True) != json.dumps(STATE, sort_keys=True):
        raise ValueError("Only the declared x3/mu-, N=0 pair of component indices")
    if (json.dumps(inputs["profiles"], sort_keys=True) != json.dumps(PROFILES, sort_keys=True)
            or json.dumps(inputs["alpha_model"], sort_keys=True) != json.dumps(ALPHA_MODEL, sort_keys=True)
            or inputs["a16_readings"] != A16_READINGS
            or inputs["alpha3_root_readings"] != ROOT_READINGS
            or inputs["default_a16_reading"] != A16_READINGS[0]
            or inputs["default_alpha3_root_reading"] != ROOT_READINGS[0]):
        raise ValueError("Only the twelve predeclared source/reading profiles")


def component_charge(x):
    if type(x) is not int or x not in (0, 1):
        raise ValueError("Only the source's two pre-collapse x indices")
    s = STATE
    k, P, Q, kap = (s[key] for key in ("k", "P", "Q", "kappa"))
    twice_q = ((P-2*x)*(1-kap*Q*(2-k))
               + s["epsilon"]*(k-1-(1+kap)*Q*(2-k))+s["C"])
    return D(twice_q)/TWO


def maximal_integer_trace(coefficients, target):
    """Bounded scalar greedy diagnostic; not a general Heim-state solver."""
    if (len(coefficients) != 3 or any(not a.is_finite() or a <= 0 for a in coefficients)
            or not target.is_finite() or target < 0):
        raise ValueError("Three positive finite coefficients and nonnegative target")
    remaining, trace, integers = target, [], []
    for coeff, power in zip(coefficients, (3, 2, 1)):
        integer = 0
        while coeff*(integer+1)**power <= remaining:
            integer += 1
            if integer > 10000:
                raise ValueError("Outside bounded scalar diagnostic")
        residual = remaining-coeff*integer**power
        trace.append(dict(K=integer, power=power, remaining_before=remaining,
                          remaining_after=residual,
                          next_integer_margin=coeff*(integer+1)**power-remaining))
        integers.append(integer)
        remaining = residual
    return integers, remaining, trace


def structural_margins(coefficients, integers):
    a1, a2, a3 = coefficients
    k1, k2, k3, k4 = integers
    return dict(
        XIII=[a3*k3-k4, a2*k2**2-a3*k3, a3*k1**3-a2*k2**2],
        XXXII=[a3*k3-k4, 2*a2*k2**2-a3*k3*(1+k3),
               6*a1*k1**3-a2*k2*(2*k2**2+3*k2+1)],
    )


def evaluate_profile(profile, a16_reading, root_reading):
    if profile not in PROFILES or a16_reading not in A16_READINGS or root_reading not in ROOT_READINGS:
        raise ValueError("Unknown predeclared profile or reading")
    pi = core.mathematical_pi() if profile["pi"] == "mathematical" else D(profile["pi"])
    eb = ONE.exp() if profile["e_base"] == "mathematical" else D(profile["e_base"])
    xi = (ONE+D(5).sqrt())/TWO if profile["xi"] == "golden_ratio" else D(profile["xi"])
    terms = core.equation_rhs(pi, ALPHA_MODEL)
    alpha, beta = core.solve_branches(terms["rhs"])
    eta, d = terms["eta"], core.eta_k_q(pi, k=1, q=1)
    s = d.sqrt()
    charges = [component_charge(x) for x in STATE["component_indices"]]
    if any(value != STATE["qx"] or abs(value) != STATE["q"] for value in charges):
        raise ValueError("Source charge formula disagrees with fixed configuration")
    a1, a2 = (ONE+s)/TWO, ONE/d
    radical = (xi*d).sqrt() if root_reading == ROOT_READINGS[0] else xi.sqrt()*d
    a3 = ONE-alpha/THREE*((ONE+s)*xi/d**2)**3*d**3 \
        - TWO*radical/eb*((ONE-s)/(ONE+s))**2
    a16_correction = alpha*(ONE+6*alpha/pi)/5
    a16_correction = a16_correction/eta if a16_reading == A16_READINGS[0] else a16_correction*eta
    A16 = (pi*eb)**2*(ONE+a16_correction)
    A26 = TWO*(ONE-pi*(eb*xi*alpha)**2*eta.sqrt()/TWO)/(eb*xi**2)
    A31 = (pi*eb*alpha)**2*(ONE-(pi*eb)**2*(ONE-beta**2))
    A24 = TWO*xi**2/(THREE*eta)
    domain = dict(eta=eta, d=d, pi=pi, e_base=eb, xi=xi, alpha=alpha, beta=beta,
                  A14_denominator=alpha, A26_denominator=eb*xi**2,
                  A36_denominator=ONE-pi*eb*(xi*eb)**2*(ONE-beta**2),
                  A41_denominator=TWO*beta-alpha, A61_denominator=12*beta,
                  XVI_inactive_A24_denominator=ONE-A24,
                  XVIII_inactive_A24_denominator=ONE,
                  three_minus_q=TWO, eight_minus_A66_zero_power=D(7),
                  XXIII_denominator=THREE+eta)
    if any(not value.is_finite() or value == 0 for value in domain.values()):
        raise ValueError("Undefined term before inactive-factor reduction")
    w1, w2 = d*A16, A26+d**2*A31
    if not (ONE+w2).is_finite() or ONE+w2 == 0:
        raise ValueError("Shifted exponent-zero base must be defined and nonzero")
    w = w1+(ONE+w2)**0
    coefficients = (a1, a2, a3)
    g = 27*a1+9*a2+2*a3+(-ONE/THREE).exp()
    W = g*w
    integers, r, trace = maximal_integer_trace(coefficients, W)
    row = dict(profile=profile, a16_reading=a16_reading, alpha3_root_reading=root_reading,
               pure_numbers=dict(pi=pi, e_base=eb, xi=xi), alpha=alpha, beta=beta,
               eta=eta, eta11=d, coefficients=coefficients,
               component_charges=charges,
               A16=A16, A26=A26, A31=A31, w1=w1, w2=w2, shifted_w2_base=ONE+w2,
               w=w, g=g, f_N0=0, W=W, domain_checks=domain, greedy_steps=trace, W4=r)
    # The scoped implementation explicitly refuses to invent special-case rules.
    if not ZERO < r <= ONE:
        row.update(selection_case="a" if r == 0 else "c", status="special_case_requires_separate_contract")
        return row
    raw = -THREE*r.ln()
    k4 = int(raw.to_integral_value(rounding=ROUND_FLOOR))
    integers.append(k4)
    selected_exp = (-D(k4)/THREE).exp()
    residual = selected_exp-r
    sum_value = a1*integers[0]**3+a2*integers[1]**2+a3*integers[2]+selected_exp
    margins = structural_margins(coefficients, integers)
    row.update(selection_case="b", status="conditional_integer_selection_not_exact_solution",
               raw_K4=raw, K4_floor=k4, K4_floor_lower_margin=raw-k4,
               K4_floor_upper_margin=k4+1-raw, integerization_method="decimal_floor_no_promotion",
               integers=integers, occupations=[n-q for n,q in zip(integers, (3,3,2,1))],
               selected_exponential=selected_exp, equation_residual=residual,
               equation_residual_direct=sum_value-W,
               real_inverse_residual=(-raw/THREE).exp()-r,
               relative_exponential_residual=residual/r, relative_W_residual=residual/W,
               absolute_b_bound=ONE-(-ONE/THREE).exp(),
               relative_exponential_b_bound=(ONE/THREE).exp()-ONE,
               structural_margins=margins,
               structural_inequalities_satisfied=all(v>=0 for group in margins.values() for v in group),
               exact_zone_boundary_in_decimal_evaluation=any(v==0 for group in margins.values() for v in group))
    return row


def build_report(inputs=None, precision=80):
    if type(precision) is not int or not 40 <= precision <= 200:
        raise ValueError("Require precision from 40 through 200")
    if inputs is None:
        inputs = json.loads(INPUTS.read_text(encoding="utf-8"))
    validate_inputs(inputs)
    with localcontext() as ctx:
        ctx.prec = precision
        rows = [evaluate_profile(p, a16, root) for p in inputs["profiles"]
                for a16 in A16_READINGS for root in ROOT_READINGS]
        digest = hashlib.sha256(json.dumps(inputs, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        return core.stringify(dict(schema_version=1, audit_date=inputs["audit_date"], precision=precision,
                                   input_content_sha256=digest, inputs=inputs, profiles=rows,
                                   scope="Conditional x3 W/selection only; no mass, physical uncertainty, or global theory verdict"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=80)
    parser.add_argument("--verify-sources", action="store_true")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    inputs = json.loads(INPUTS.read_text(encoding="utf-8"))
    validate_inputs(inputs)
    if args.verify_sources:
        failures = core.verify_sources(dict(sources=[inputs["source"]]))
        if failures:
            print("\n".join(failures))
            return 1
        print("Source hash verified: H006")
    report = build_report(inputs, args.precision)
    encoded = json.dumps(report, ensure_ascii=False, indent=2)+"\n"
    if args.write:
        OUTPUT.write_text(encoded, encoding="utf-8", newline="\n")
        print(f"Wrote {OUTPUT.relative_to(core.ROOT).as_posix()}")
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != encoded:
            print("Result snapshot missing/stale; inspect before --write")
            return 1
        print("Result snapshot matches fresh calculation")
    for row in report["profiles"]:
        print(f"{row['profile']['id']}/{row['a16_reading']}/{row['alpha3_root_reading']}: "
              f"case={row['selection_case']}, K={row.get('integers')}, "
              f"W4={D(row['W4']):.15f}, R={D(row.get('equation_residual', 'NaN')):.15f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

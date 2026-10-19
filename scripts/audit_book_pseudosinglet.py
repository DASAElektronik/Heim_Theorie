"""Fixed H004 pseudosinglet, N=0: selection and separate structure diagnostics.

The two profiles were committed before evaluation. No mass, fitted Y value,
H006/H010 coefficient profile, or general metronic state solver is used.
Only generic Decimal pi/root/serialization helpers are reused from audit_alpha.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal as D, ROUND_FLOOR, localcontext

import audit_alpha as core

INPUTS = core.ROOT / "04_reconstruction/alpha_audit/book_pseudosinglet_inputs.json"
OUTPUT = core.ROOT / "05_analysis/book_pseudosinglet_results.json"
INPUT_DIGEST = "8b320903bfe148c2956168e46c2279c1a16cd1b2b1837cb5b6efba47188affb7"
ONE, TWO, THREE = D(1), D(2), D(3)


def input_digest(inputs):
    return hashlib.sha256(json.dumps(inputs, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def validate_inputs(inputs):
    if input_digest(inputs) != INPUT_DIGEST:
        raise ValueError("Only the two precommitted H004 input profiles are allowed")


def eta(q, k, pi):
    """H004 (98): first index q, second k; k=0 is formal external marker."""
    if type(q) is not int or type(k) is not int or q < 0 or k < 0:
        raise ValueError("Nonnegative integer q,k required")
    if not pi.is_finite() or pi <= 0:
        raise ValueError("Positive finite pi required")
    return pi / (pi**4 + D(q**4*(4+k))).sqrt().sqrt()


def offsets(k):
    if type(k) is not int or k not in (1, 2):
        raise ValueError("Book internal k must be 1 or 2 in this diagnostic")
    s = k*k+1
    return [3*2**(s-2), 2**s-1, 2**s+2*(-1)**k, 2**(s-1)-1]


def first_three(coefficients, total):
    if (len(coefficients) != 3 or not total.is_finite() or total < 0
            or any(not a.is_finite() or a <= 0 for a in coefficients)):
        raise ValueError("Three positive finite coefficients and finite total>=0 required")
    integers, trace = [], []
    for coefficient, power in zip(coefficients, (3, 2, 1), strict=True):
        integer = 0
        while coefficient*(integer+1)**power <= total:
            integer += 1
            if integer > 10000:
                raise ValueError("Outside the bounded diagnostic's search domain")
        rest = total-coefficient*integer**power
        trace.append(dict(integer=integer, power=power, remaining_before=total,
                          remaining_after=rest,
                          next_integer_margin=coefficient*(integer+1)**power-total))
        integers.append(integer)
        total = rest
    return integers, total, trace


def structure_diagnostics(integers, alpha3):
    """Unweighted 98e/323/107 and the distinct 107b expression, not merged."""
    if (len(integers) != 4
            or any(type(n) is not int or n < 0 for n in integers)
            or not alpha3.is_finite() or alpha3 <= 0):
        raise ValueError("Four nonnegative integer occupations and positive alpha3 required")
    a, b, c, d = integers
    G = [a*a*(a+1)**2//4, b*(b+1)*(2*b+1)//6, c*(c+1)//2, d]
    delta_G = [a**3, b*b, c, 1]
    bandwidths = [delta_G[j]-G[j+1] for j in range(3)]
    second_row = [delta_G[j]-delta_G[j+1] for j in range(3)]
    sigma = alpha3*c-d
    return dict(G_unweighted=G, delta_G_unweighted=delta_G,
                beta_107a_unweighted=bandwidths,
                margins_107_second_row=second_row,
                central_margin=delta_G[0],
                noncollapsed_107a_passes=all(b >= 1 for b in bandwidths),
                second_row_passes=all(v >= 0 for v in second_row),
                beta4_107b_sigma=sigma, sigma_positive=sigma > 0,
                sigma_at_least_one=sigma >= 1,
                sigma_minus_unweighted_beta4=sigma-bandwidths[2],
                sigma_difference_identity=(alpha3-1)*c,
                sigma_is_integer_in_decimal_evaluation=sigma == sigma.to_integral_value(),
                upper_L_bounds="not numerically specified or validated",
                complete_state_predicate="not established; printed stages kept separate")


def evaluate_profile(profile, inputs):
    pi, e = core.mathematical_pi(), ONE.exp()
    xi = (ONE+D(5).sqrt())/TWO
    eta_external, d, t = eta(1, 0, pi), eta(1, 1, pi), eta(1, 2, pi)
    vartheta = 5*eta_external+2*eta_external.sqrt()+1
    A1 = d.sqrt()*(1-d.sqrt())/(1+d.sqrt())
    A2 = t.sqrt()*(1-t.sqrt())/(1+t.sqrt())
    rhs = 9*vartheta*(1-A1*A2*inputs["Y_values"]["Y3"])/(2*pi)**5
    small, _ = core.solve_branches(rhs)
    alpha = small if profile["rule"] == "small_positive_root_of_105" else D(profile["alpha"])
    if not 0 < alpha < 1:
        raise ValueError("Require alpha in (0,1)")
    sqrt_d = d.sqrt()
    ratio = (1-sqrt_d)/(1+sqrt_d)
    correction_H = alpha*(1+sqrt_d)*xi**3/(3*d**3)
    correction_G = 2*xi*d/e*ratio**2
    coefficients = [(1+sqrt_d)/2, 1/d, 1-correction_H-correction_G]
    A16 = (pi*e)**2*(1+alpha/(5*eta_external)*(1+6*alpha/pi))*inputs["Y_values"]["Y9"]
    Qj = offsets(inputs["state"]["k"])
    g = sum((a*D(q)**p for a, q, p in zip(coefficients, Qj[:3], (3, 2, 1))), D(0)) \
        + (-ONE/THREE).exp()
    w = 1+d*A16
    W = g*w
    integers, rest, trace = first_three(coefficients, W)
    row = dict(profile=profile, pi=pi, e=e, xi=xi, eta=eta_external,
               eta11=d, eta12_q1_k2=t, vartheta=vartheta, A1=A1, A2=A2,
               alpha=alpha, inverse_alpha=1/alpha, alpha105_rhs=rhs,
               alpha105_residual=alpha*(1-alpha*alpha).sqrt()-rhs,
               correction_H=correction_H, correction_G=correction_G,
               coefficients=coefficients, Q_j=Qj, A16=A16, w=w, g=g,
               f_N0=D(0), W=W, W1=W, greedy_steps=trace, W4=rest,
               first_three=integers.copy())
    if rest == 0 or rest > 1:
        row.update(selection_case="zero_rest" if rest == 0 else "transfer_needed",
                   status="requires_separate_branch_contract")
        return row
    if rest < 0:
        raise ArithmeticError("Greedy remainder must be nonnegative")
    raw = -THREE*rest.ln()
    cap = coefficients[2]*integers[2]
    row.update(raw_N4=raw, raw_cap=cap, raw_cap_margin=cap-raw)
    if raw > cap:
        row.update(selection_case="saturation_needed", status="requires_separate_branch_contract")
        return row
    n4 = int(raw.to_integral_value(rounding=ROUND_FLOOR))
    integers.append(n4)
    occupations = [n-q for n, q in zip(integers, Qj, strict=True)]
    selected_exp = (-D(n4)/THREE).exp()
    residual = selected_exp-rest
    direct = sum((a*D(n)**p for a, n, p in zip(coefficients, integers[:3], (3, 2, 1))), D(0)) \
        + selected_exp-W
    row.update(selection_case="ordinary_positive_rest", status="conditional_selection_not_exact_solution",
               integerization_method="ordinary_floor; finite-nine promotion not specified",
               integers=integers, occupations=occupations,
               lower_occupation_bounds_pass=all(n >= -q for n, q in zip(occupations, Qj)),
               raw_integer_lower_margin=raw-n4, raw_integer_upper_margin=n4+1-raw,
               selected_exponential=selected_exp, equation_residual=residual,
               equation_residual_direct=direct, relative_W_residual=residual/W,
               real_inverse_residual=(-raw/THREE).exp()-rest,
               structure=structure_diagnostics(integers, coefficients[2]))
    return row


def build_report(inputs=None, precision=80):
    if type(precision) is not int or not 40 <= precision <= 200:
        raise ValueError("Require integer precision from 40 through 200")
    if inputs is None:
        inputs = json.loads(INPUTS.read_text(encoding="utf-8"))
    validate_inputs(inputs)
    with localcontext() as ctx:
        ctx.prec = precision
        rows = [evaluate_profile(p, inputs) for p in inputs["alpha_profiles"]]
        return core.stringify(dict(schema_version=1, audit_date=inputs["audit_date"],
                                   precision=precision, input_content_sha256=input_digest(inputs),
                                   inputs=inputs, profiles=rows,
                                   scope="Conditional H004 forward path; no mass, fit, full state predicate or physical error bound"))


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
        print("H004 source hash verified")
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
        print(f"{row['profile']['id']}: {row['selection_case']}, N_j={row.get('integers')}, "
              f"W4={D(row['W4']):.15f}, R={row.get('equation_residual')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

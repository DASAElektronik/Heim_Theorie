"""Four precommitted joint decay cells; own diagnostics, no mass or fitted A.

Keep the original coefficient/w contract and alter exp(-A*n) and its
reference in g/W together. Certify ordinary branch OR report its boundary.
Fresh finite bounds plus monotone interval images decide integer existence
and a separately declared real-N4 relaxation. No files are written.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal as D, localcontext
from fractions import Fraction as F

import audit_coupled_existence as base

I = base.Interval
INPUTS = base.ROOT / "04_reconstruction/alpha_audit/decay_sensitivity_inputs.json"
DIGEST = "36173ed155513a29b8b1834b32a9c1845bb96c9b1083642d1053f9d33f9ac75a"


def load_contract():
    contract = json.loads(INPUTS.read_text(encoding="utf-8"))
    digest = hashlib.sha256(json.dumps(contract, sort_keys=True,
                                       separators=(",", ":")).encode()).hexdigest()
    if digest != DIGEST:
        raise ValueError("Precommitted decay comparison changed")
    if contract["base_input_canonical_sha256"] != base.INPUT_DIGEST:
        raise ValueError("Base input binding changed")
    return contract


def exp_minus(x):
    """Exact rational argument >=0, range reduction then certified Taylor."""
    x = base.rational(x)
    if x < 0:
        raise ValueError("Nonnegative argument required")
    m = max(1, -(-x.numerator//x.denominator))
    return base.exp_positive_bounds(x/m).reciprocal()**m


def exp_cap(A, cap):
    return I(exp_minus(A*cap.hi).lo, exp_minus(A*cap.lo).hi)


def finite_box(row):
    """Fresh necessary outer box, from W and strict unweighted gates."""
    a1, a2, a3, W = (row[k] for k in ("a1", "a2", "a3", "W"))
    if min(a1.lo, a2.lo, a3.lo, W.lo) <= 0:
        raise ValueError("Positive coefficients and budget required")
    n1 = 0
    while a1.lo*(n1+1)**3 <= W.hi:
        n1 += 1
    n2 = 0
    while base.G2(n2+1) < n1**3:
        n2 += 1
    n3 = 0
    while base.G3(n3+1) < n2**2:
        n3 += 1
    return (n1, n2, n3, n3-1)


def gates(n1, n2, n3, n4):
    """Exact direct integer gate diagnostics, NOT the separate sigma rule."""
    if any(type(n) is not int or n < 0 for n in (n1, n2, n3, n4)):
        raise ValueError("Nonnegative integer occupations required")
    betas = (n1**3-base.G2(n2), n2*n2-base.G3(n3), n3-n4)
    second = (n1**3-n2*n2, n2*n2-n3, n3-1)
    return dict(beta=betas, second_row=second,
                passes=min(betas) >= 1 and min(second) >= 0 and n1 > 0)


def forward(row):
    A, remaining = row["A"], row["W"]
    integers, trace = [], []
    for key, power in (("a1", 3), ("a2", 2), ("a3", 1)):
        coefficient, n = row[key], 0
        while (coefficient*(n+1)**power).hi <= remaining.lo:
            n += 1
        next_margin = coefficient*(n+1)**power-remaining
        if next_margin.lo <= 0:
            raise ArithmeticError("Integer stage undecided by interval")
        remaining = remaining-coefficient*n**power
        if remaining.lo <= 0:
            raise ArithmeticError("Positive remainder branch not certified")
        integers.append(n)
        trace.append(dict(integer=n, next_margin=next_margin, remainder=remaining))
    if remaining.hi >= 1:
        return dict(case="outside_positive_subunit_contract", N123=integers, W4=remaining)
    cap = row["a3"]*integers[2]
    cap_exp = exp_cap(A, cap)
    result = dict(N123=integers.copy(), W4=remaining, cap=cap, exp_at_cap=cap_exp,
                  trace=trace)
    if remaining.hi < cap_exp.lo:
        return dict(result, case="saturation_required_not_implemented",
                    branch_margin=cap_exp-remaining)
    if remaining.lo <= cap_exp.hi:
        raise ArithmeticError("Cap comparison undecided")
    n4 = 0
    while exp_minus(A*(n4+1)).lo > remaining.hi:
        n4 += 1
    high, low = exp_minus(A*n4), exp_minus(A*(n4+1))
    if not (high.lo > remaining.hi and low.hi < remaining.lo):
        raise ArithmeticError("Log-floor undecided")
    integers.append(n4)
    return dict(result, case="ordinary_positive_rest", integers=integers,
                residual=high-remaining, gates=gates(*integers),
                sigma=row["a3"]*integers[2]-n4,
                branch_margin=remaining-cap_exp)


def existence(row):
    """Monotone endpoint pruning covers ALL gate-admissible integer states.

    The declared relaxation uses 0<=real N4<=N3-1, not N4 unbounded.
    An explicitly additional enclosure covers the larger direct real gate
    0<=N4<N3 via its open lower exponential endpoint. Neither is a physical
    state. The original comparison inputs are not altered by this extra proof.
    """
    upper = finite_box(row)
    a1, a2, a3, W, A = (row[k] for k in ("a1", "a2", "a3", "W", "A"))
    exps = [exp_minus(A*n) for n in range(upper[2]+1)]
    triples = states = 0
    gap = a1.lo*(upper[0]+1)**3-W.hi  # all energy-excluded N1 above the box
    direct_real_gap = gap
    integer_unresolved, real_intersections, direct_real_intersections = [], [], []
    for n1 in range(upper[0]+1):
        for n2 in range(upper[1]+1):
            if n1**3 <= base.G2(n2):
                continue
            for n3 in range(1, upper[2]+1):
                if not gates(n1, n2, n3, 0)["passes"]:
                    continue
                triples += 1
                states += n3
                polynomial = a1*n1**3+a2*n2*n2+a3*n3
                low, high = polynomial+exps[n3-1]-W, polynomial+1-W
                # Additional open-domain proof, separate from the predeclared test.
                direct_low = polynomial+exps[n3]-W
                if direct_low.lo > 0:
                    direct_real_gap = min(direct_real_gap, direct_low.lo)
                elif high.hi < 0:
                    direct_real_gap = min(direct_real_gap, -high.hi)
                else:
                    direct_real_intersections.append([n1, n2, n3])
                if low.lo > 0:
                    gap = min(gap, low.lo)
                    continue
                if high.hi < 0:
                    gap = min(gap, -high.hi)
                    continue
                real_intersections.append(dict(N123=[n1, n2, n3],
                    low_endpoint_residual=low, high_endpoint_residual=high,
                    certified_interior_root=low.hi < 0 < high.lo))
                for n4 in range(n3):
                    R = polynomial+exps[n4]-W
                    if R.lo > 0:
                        gap = min(gap, R.lo)
                    elif R.hi < 0:
                        gap = min(gap, -R.hi)
                    else:
                        integer_unresolved.append([n1, n2, n3, n4])
    return dict(finite_box=upper, triples=triples, integer_states=states,
                integer_unresolved=integer_unresolved,
                integer_excluded=not integer_unresolved,
                certified_integer_gap=gap if not integer_unresolved else None,
                real_intersections=real_intersections,
                declared_real_relaxation_excluded=not real_intersections,
                additional_direct_real_intersections=direct_real_intersections,
                additional_direct_real_gate_excluded=not direct_real_intersections,
                additional_direct_real_gap=(direct_real_gap if not direct_real_intersections else None))


def build_report():
    contract = load_contract()
    original = base.book_intervals(base.load_inputs())
    if [r["profile"] for r in original] != contract["alpha_profiles"]:
        raise ValueError("Profile order or scope changed")
    rows = []
    for old in original:
        w = 1+old["eta11"]*old["A16"]
        B = 27*old["a1"]+9*old["a2"]+2*old["a3"]
        old_exp = exp_minus(F(1, 3))
        for setting in contract["decay_profiles"]:
            A = F(setting["A_numerator"], setting["A_denominator"])
            ext = exp_minus(A)
            g = B+ext
            delta_g = I.point(0) if A == F(1, 3) else ext-old_exp
            row = dict(old, decay_id=setting["id"], A=A, w=w, g=g, W=g*w,
                       reference_exp=ext, delta_g=delta_g, delta_W=w*delta_g)
            row["forward"] = forward(row)
            row["existence"] = existence(row)
            rows.append(row)
    return rows


def show(interval, digits=12):
    """Decimal midpoint for readable display ONLY; certificates remain rational."""
    with localcontext() as ctx:
        ctx.prec = 50
        midpoint = (interval.lo+interval.hi)/2
        return f"{D(midpoint.numerator)/D(midpoint.denominator):.{digits}f}"


def raw_log_display(row):
    with localcontext() as ctx:
        ctx.prec = 60
        r = (row["forward"]["W4"].lo+row["forward"]["W4"].hi)/2
        A = row["A"]
        return -(D(r.numerator)/D(r.denominator)).ln()*A.denominator/A.numerator


def show_lower(value, digits=12):
    """Finite decimal rounded DOWN, so displayed lower bounds stay valid."""
    scale = 10**digits
    units = value.numerator*scale//value.denominator
    with localcontext() as ctx:
        ctx.prec = max(50, digits+20)
        return f"{D(units)/scale:.{digits}f}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Recompute certificates (default)")
    parser.add_argument("--verify-sources", action="store_true")
    args = parser.parse_args()
    if args.verify_sources:
        source = base.load_inputs()["source"]
        if hashlib.sha256((base.ROOT/source["path"]).read_bytes()).hexdigest().lower() != source["sha256"].lower():
            raise ValueError("Source hash changed")
        print("H004 source hash verified")
    for row in build_report():
        fwd, result = row["forward"], row["existence"]
        print(f"{row['profile']}/{row['decay_id']}: A={row['A']}, g={show(row['g'])}, "
              f"W={show(row['W'])}, delta_W={show(row['delta_W'])}")
        print(f"  {fwd['case']}; N123={fwd['N123'][:3]}, W4={show(fwd['W4'])}, "
              f"raw_N4~{raw_log_display(row):.12f}, cap={show(fwd['cap'])}")
        if 'integers' in fwd:
            print(f"  N={fwd['integers']}, R={show(fwd['residual'])}, beta={fwd['gates']['beta']}")
        print(f"  fresh_box={result['finite_box']}; integer_states={result['integer_states']}; "
              f"integer_excluded={result['integer_excluded']}; "
              f"declared_real_relaxation_excluded={result['declared_real_relaxation_excluded']}")
        gap = result['certified_integer_gap']
        if gap is not None:
            print(f"  certified integer gap >= {show_lower(gap)} (rounded down)")
        real_gap = result['additional_direct_real_gap']
        if real_gap is not None:
            print(f"  additional proof for 0<=real N4<N3: gap >= {show_lower(real_gap)}")
    print("No saturation continuation, mass, physical correction, or fitted parameter selected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Source-shaped saturation of the fixed stage-35 counterfactual, no fit.

All old inputs and calculators stay unchanged. This is not a complete TRC,
transfer, collapse or physical-state solver. Rational outward intervals
certify the reached cap and residual; no promotion tolerance is invented.
"""

import argparse
import hashlib
import json

import audit_decay_sensitivity as decay

I = decay.I
F = decay.F
INPUTS = decay.base.ROOT / "04_reconstruction/alpha_audit/saturation_inputs.json"
DIGEST = "902f775de16e96628825c7ebab93881e58cae1a334f2f1a4710b7528eec98f98"


def load_contract():
    document = json.loads(INPUTS.read_text(encoding="utf-8"))
    digest = hashlib.sha256(json.dumps(document, sort_keys=True,
                                       separators=(",", ":")).encode()).hexdigest()
    if digest != DIGEST:
        raise ValueError("Precommitted saturation input changed")
    if document["base_input_canonical_sha256"] != decay.DIGEST:
        raise ValueError("Stage-35 binding changed")
    return document


def cap_selection(cap):
    """Own TRC envelope: truncation or promotion to next integer, then cap.

    Does not assert that promotion is actually allowed at a given number.
    At integer caps ceil equals floor; never replace this with ceil(cap)-1.
    Refuse intervals crossing integer cells instead of choosing a tolerance.
    """
    if cap.lo < 0:
        raise ValueError("Nonnegative cap required")
    integer = cap.lo // 1
    if cap.hi >= integer+1:
        raise ArithmeticError("Cap integer cell not certified")
    candidates = [integer]
    if cap.hi > integer:
        candidates.append(integer+1)
    branches = []
    for candidate in candidates:
        if candidate > cap.hi:
            corrected = candidate-1
        elif candidate <= cap.lo:
            corrected = candidate
        else:
            raise ArithmeticError("Conditional cap correction undecided")
        branches.append((candidate, corrected))
    if any(corrected != integer for _, corrected in branches):
        raise ArithmeticError("TRC envelope did not produce a unique result")
    return dict(N4=integer, trc_envelope=branches)


def extend(row):
    """Keep the certified old prefix; extend only the certified cap branch."""
    fwd = row["forward"]
    if fwd["case"] == "saturation_required_not_implemented":
        if fwd["branch_margin"].lo <= 0:
            raise ArithmeticError("Saturation trigger not certified")
        choice = cap_selection(fwd["cap"])
        numbers = fwd["N123"] + [choice["N4"]]
        kind = "saturated_counterfactual"
    elif fwd["case"] == "ordinary_positive_rest":
        numbers = fwd["integers"].copy()
        choice, kind = None, "unchanged_ordinary_control"
    else:
        raise ValueError("No continuation specified for this branch")
    n1, n2, n3, n4 = numbers
    exponential = decay.exp_minus(row["A"]*n4)
    direct = row["a1"]*n1**3+row["a2"]*n2**2+row["a3"]*n3+exponential-row["W"]
    identity = exponential-fwd["W4"]
    if max(direct.lo, identity.lo) > min(direct.hi, identity.hi):
        raise ArithmeticError("Direct and rest-identity enclosures disagree")
    # Q is the fixed book state, not a new parameter choice.
    Q = (3, 3, 2, 1)
    small = tuple(n-q for n, q in zip(numbers, Q, strict=True))
    return dict(profile=row["profile"], A=row["A"], kind=kind,
                integers=numbers, small_n=small, cap_choice=choice,
                direct_gates=decay.gates(*numbers),
                small_n_lower_bounds_pass=all(n >= -q for n, q in zip(small, Q, strict=True)),
                sigma_107b=row["a3"]*n3-n4,
                R_direct=direct, R_identity=identity,
                exact_scalar_excluded=(direct.lo > 0 or direct.hi < 0))


def build_report():
    load_contract()
    return [extend(row) for row in decay.build_report()]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--verify-sources", action="store_true")
    args = parser.parse_args()
    if args.verify_sources:
        source = decay.base.load_inputs()["source"]
        digest = hashlib.sha256((decay.base.ROOT/source["path"]).read_bytes()).hexdigest()
        if digest.lower() != source["sha256"].lower():
            raise ValueError("H004 hash changed")
        print("H004 source hash verified")
    for row in build_report():
        print(f"{row['profile']}, A={row['A']}: {row['kind']}")
        print(f"  N={row['integers']}, n={row['small_n']}, "
              f"beta={row['direct_gates']['beta']}, direct_pass={row['direct_gates']['passes']}")
        print(f"  sigma107b={decay.show(row['sigma_107b'], 18)}, "
              f"R={decay.show(row['R_identity'], 18)}")
        if not row["exact_scalar_excluded"]:
            raise ArithmeticError("Expected fixed-case exclusion not certified")
        print(f"  R >= {decay.show_lower(row['R_identity'].lo, 15)} (rounded down)")
    print("Local gates and exact scalar equality are separate; no mass or global physical admission")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

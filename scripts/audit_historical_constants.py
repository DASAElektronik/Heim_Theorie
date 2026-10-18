"""Replay only the photographed H015 GINIT constants, never the old program."""
from decimal import Decimal as D, localcontext
from pathlib import Path
import argparse
import json

try:
    from .audit_alpha import printing_interval
except ImportError:
    from audit_alpha import printing_interval

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "04_reconstruction/alpha_audit/historical_constants_inputs.json"
OUTPUT = ROOT / "05_analysis/historical_constants_results.json"


def number(token):
    return D(token.replace("Q", "E"))


def initialize(tokens, precision=60):
    with localcontext() as ctx:
        ctx.prec = precision
        v = {k: number(t) for k, t in tokens.items()}
        if min(v.values()) <= 0:
            raise ValueError("Positive initialization values required")
        pi, hq, c, gam, rg, s0, xi = (v[k] for k in ("PI", "HQ", "C", "GAM", "RG", "S0", "XI"))
        v["EBN"] = D(1).exp()
        eta = v["ETA"] = pi/(4+pi**4)**D(".25")
        theta = v["THETA"] = 5*eta+2*eta.sqrt()+1
        v["EQ"] = D(3)/(4*pi**2)*(2*theta*hq/rg).sqrt()
        v["ALFA"] = 1/v.pop("ALFA_inverse")
        v["BETA"] = 1/v.pop("BETA_inverse")
        v["AMU"] = pi**D(".25")*(3*pi*s0*gam*hq)**(D(1)/3)*(c*hq/(3*gam)).sqrt()/(c*s0)
        temp1 = 1-D(2)/3*xi*eta**2*(1-eta.sqrt())
        v["ALFP"] = temp1/(eta**2*eta**(D(1)/3))-1
        v["ALFM"] = temp1/(eta*eta**(D(1)/3))-1
        return v


def audit(precision=60):
    doc = json.loads(INPUT.read_text(encoding="utf-8"))
    values = initialize(doc["inputs"], precision)
    with localcontext() as ctx:
        ctx.prec = precision
        rows = []
        for name, token in doc["printed_outputs"].items():
            lo, hi = printing_interval(token.replace("Q", "E"))
            rows.append({"name": name, "printed": token,
                         "reconstructed": format(values[name], ".15E"),
                         "within_assumed_print_rounding": lo <= values[name] <= hi})
        return {"profile": doc["profile"], "input_path": str(INPUT.relative_to(ROOT)).replace("\\", "/"),
                "scope": doc["scope"], "rounding_assumption": doc["comparison"],
                "rows": rows, "all_rows_match": all(r["within_assumed_print_rounding"] for r in rows),
                "not_established": doc["not_established"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = audit(60)
    if result != audit(90):
        raise SystemExit("60/90-digit stability check failed")
    if args.check:
        if json.loads(OUTPUT.read_text(encoding="utf-8")) != result:
            raise SystemExit("Stored diagnostic differs")
        print(f"H015 initialization: {len(result['rows'])} rows reproduced; all_match={result['all_rows_match']}")
    elif args.write:
        OUTPUT.write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
        print(OUTPUT)
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

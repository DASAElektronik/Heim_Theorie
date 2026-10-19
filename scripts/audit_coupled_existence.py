"""Own rational certificate for the fixed H004 noncollapsed existence question.

No floating-point arithmetic, mass, tolerance fitting, source-program import,
TRC implementation, or replacement occupation selection. No files are written.
Closed rational intervals enclose both precommitted book profiles. Five energy
bounds exclude a superset of the strict unweighted (107)/(107a) states.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUTS = ROOT / "04_reconstruction/alpha_audit/book_pseudosinglet_inputs.json"
INPUT_DIGEST = "8b320903bfe148c2956168e46c2279c1a16cd1b2b1837cb5b6efba47188affb7"
SCALE = 10**40


def rational(value):
    if type(value) not in (int, F):
        raise TypeError("Only exact integers and Fractions are accepted")
    return F(value)


def down(value):
    return F(value.numerator*SCALE // value.denominator, SCALE)


def up(value):
    return -down(-value)


@dataclass(frozen=True)
class Interval:
    lo: F
    hi: F

    def __post_init__(self):
        lo, hi = rational(self.lo), rational(self.hi)
        if lo > hi:
            raise ValueError("Reversed interval")
        object.__setattr__(self, "lo", down(lo))
        object.__setattr__(self, "hi", up(hi))

    @staticmethod
    def point(value):
        value = rational(value)
        return Interval(value, value)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Interval) else Interval.point(value)

    def __add__(self, other):
        other = self.coerce(other)
        return Interval(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        other = self.coerce(other)
        products = [a*b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def reciprocal(self):
        if self.lo <= 0 <= self.hi:
            raise ValueError("Division by an interval containing zero")
        return Interval(1/self.hi, 1/self.lo)

    def __truediv__(self, other):
        return self*self.coerce(other).reciprocal()

    def __rtruediv__(self, other):
        return self.coerce(other)*self.reciprocal()

    def __pow__(self, exponent):
        if type(exponent) is not int or exponent < 0:
            raise ValueError("Only nonnegative integer powers")
        result = Interval.point(1)
        for _ in range(exponent):
            result = result*self
        return result

    def sqrt(self):
        if self.lo < 0:
            raise ValueError("Negative square root argument")
        low = isqrt(self.lo.numerator*SCALE*SCALE // self.lo.denominator)
        high = isqrt(self.hi.numerator*SCALE*SCALE // self.hi.denominator)
        if F(high*high, SCALE*SCALE) < self.hi:
            high += 1
        return Interval(F(low, SCALE), F(high, SCALE))

    def inside(self, lo, hi):
        return rational(lo) <= self.lo <= self.hi <= rational(hi)


def atan_reciprocal_bounds(inverse, terms=48):
    """Alternating series: consecutive partial sums enclose atan(1/inverse)."""
    if type(inverse) is not int or inverse < 2 or type(terms) is not int or terms < 1:
        raise ValueError("Require integer inverse>=2 and positive term count")
    partial = sum((F((-1)**j, (2*j+1)*inverse**(2*j+1))
                   for j in range(terms)), F(0))
    following = partial + F((-1)**terms, (2*terms+1)*inverse**(2*terms+1))
    return Interval(min(partial, following), max(partial, following))


def exp_positive_bounds(x, terms=64):
    """For 0<=x<=1, sum j=0..terms plus a geometric bound on its tail."""
    x = rational(x)
    if not 0 <= x <= 1 or type(terms) is not int or terms < 1:
        raise ValueError("Require 0<=x<=1 and positive integer term count")
    term = total = F(1)
    for j in range(1, terms+1):
        term *= x/j
        total += term
    next_term = term*x/(terms+1)
    tail = next_term/(1-x/(terms+2))
    return Interval(total, total+tail)


def load_inputs():
    inputs = json.loads(INPUTS.read_text(encoding="utf-8"))
    digest = hashlib.sha256(json.dumps(inputs, sort_keys=True,
                                       separators=(",", ":")).encode()).hexdigest()
    if digest != INPUT_DIGEST:
        raise ValueError("The precommitted book input contract changed")
    return inputs


def book_intervals(inputs):
    """Same fixed book equations, independent of the old Decimal calculator."""
    pi = 16*atan_reciprocal_bounds(5)-4*atan_reciprocal_bounds(239)
    e = exp_positive_bounds(F(1))
    exp_minus_third = exp_positive_bounds(F(1, 3)).reciprocal()
    xi = (1+Interval.point(5).sqrt())/2

    def eta(k):
        return pi/(pi**4+4+k).sqrt().sqrt()

    external, d, t = (eta(k) for k in (0, 1, 2))
    s, st = d.sqrt(), t.sqrt()
    vartheta = 5*external+2*external.sqrt()+1
    A1, A2 = s*(1-s)/(1+s), st*(1-st)/(1+st)
    rhs = 9*vartheta*(1-A1*A2*inputs["Y_values"]["Y3"])/(2*pi)**5
    if not rhs.inside(F(0), F(1, 2)) or rhs.lo == 0:
        raise ArithmeticError("Small-root domain not certified")
    small_alpha = ((1-(1-4*rhs**2).sqrt())/2).sqrt()
    rows = []
    for profile in inputs["alpha_profiles"]:
        alpha = (small_alpha if profile["rule"] == "small_positive_root_of_105"
                 else Interval.point(F(profile["alpha"])))
        a1, a2 = (1+s)/2, 1/d
        a3 = 1-alpha*(1+s)*xi**3/(3*d**3)-2*xi*d/e*((1-s)/(1+s))**2
        A16 = (pi*e)**2*(1+alpha/(5*external)*(1+6*alpha/pi))*inputs["Y_values"]["Y9"]
        g = 27*a1+9*a2+2*a3+exp_minus_third
        W = g*(1+d*A16)
        rows.append(dict(profile=profile["id"], pi=pi, e=e, xi=xi, eta=external,
                         eta11=d, eta12=t, alpha=alpha, A16=A16, g=g,
                         a1=a1, a2=a2, a3=a3, W=W))
    return rows


# Coarse convenient rational boxes, not fitted inputs or physical tolerances.
# Certification below derives containment from the fixed source formulas.
PROOF_BOX = {"a1": (F(249, 250), F(9969, 10000)),
             "a2": (F(1), F(5063, 5000)),
             "a3": (F(978, 1000), F(9787, 10000)),
             "W": (F(141513, 50), F(2831))}


def energy_margins(row):
    a1, a2, a3, W = (row[key] for key in ("a1", "a2", "a3", "W"))
    if min(a1.lo, a2.lo, a3.lo, W.lo) <= 0:
        raise ValueError("Positive coefficients and total required")
    return {
        "N1_ge_15": a1.lo*15**3-W.hi,
        "N1_le_13": W.lo-(a1.hi*13**3+a2.hi*18**2+a3.hi*24+1),
        "N1_eq_14_N2_ge_10": a1.lo*14**3+a2.lo*10**2-W.hi,
        "N1_eq_14_N2_le_8": W.lo-(a1.hi*14**3+a2.hi*8**2+a3.hi*10+1),
        "N1_eq_14_N2_eq_9": W.lo-(a1.hi*14**3+a2.hi*9**2+a3.hi*12+1),
    }


def G2(n):
    return n*(n+1)*(2*n+1)//6


def G3(n):
    return n*(n+1)//2


def structure_thresholds():
    # Strict gates, monotone integer G2/G3: these first forbidden values
    # bound all larger values too. No unbounded brute-force cutoff is used.
    return {"N1_le_13_N2_le_18": G2(19)-13**3,
            "N2_le_18_N3_le_24": G3(25)-18**2,
            "N2_le_8_N3_le_10": G3(11)-8**2,
            "N2_eq_9_N3_le_12": G3(13)-9**2,
            "N1_le_14_N2_le_19": G2(20)-14**3,
            "N2_le_19_N3_le_26": G3(27)-19**2}


def certify():
    rows = book_intervals(load_inputs())
    if not all(v > 0 for v in structure_thresholds().values()):
        raise ArithmeticError("Structural case bounds failed")
    for row in rows:
        for key, bounds in PROOF_BOX.items():
            if not row[key].inside(*bounds):
                raise ArithmeticError(f"{row['profile']}: {key} escaped proof box")
        if not all(v > 0 for v in energy_margins(row).values()):
            raise ArithmeticError("A case is not excluded")
    box = {key: Interval(*bounds) for key, bounds in PROOF_BOX.items()}
    if not all(v > 0 for v in energy_margins(box).values()):
        raise ArithmeticError("Coarse rational proof failed")
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Recompute all certificates (also the default)")
    parser.add_argument("--verify-sources", action="store_true")
    args = parser.parse_args()
    if args.verify_sources:
        source = load_inputs()["source"]
        digest = hashlib.sha256((ROOT/source["path"]).read_bytes()).hexdigest()
        if digest.lower() != source["sha256"].lower():
            raise ValueError("H004 source hash differs")
        print("H004 source hash verified")
    rows = certify()
    box = {key: Interval(*bounds) for key, bounds in PROOF_BOX.items()}
    for key, value in energy_margins(box).items():
        print(f"Common rational certificate {key}: margin >= {value} > 0")
    for row in rows:
        margin = energy_margins(row)["N1_eq_14_N2_eq_9"]
        print(f"{row['profile']}: all five cases excluded; final margin >= {margin}")
    print("Conditional nonexistence certified; no collapse rule or mass evaluated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

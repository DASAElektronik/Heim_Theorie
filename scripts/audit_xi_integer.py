"""Exact, bounded diagnosis of MAIN's early integer division (H01748).

No historical source is executed or modified. H006 PDF3 supplies the
closed state domain and independent table expectations, not mass inputs.
"""
import argparse
from fractions import Fraction
import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / '05_analysis/xi_integer_results.json'
# k, PG, QG, KAPPA; EPS=+1. H006 PDF3 III/IV, including pseudosinglett.
STATES = (
    (1, 0, 0, 0), (1, 1, 1, 0), (1, 1, 1, 1), (1, 1, 0, 1),
    (1, 2, 0, 0), (2, 0, 1, 0), (2, 0, 3, 0), (2, 1, 1, 0),
    (2, 1, 1, 1), (2, 2, 1, 0), (2, 3, 1, 0), (2, 3, 3, 0),
)
EXPECTED = (
    (0, [0]), (0, [0, -1]), (0, [-1, -1]), (1, [1, 0]),
    (0, [1, 0, -1]), (-1, [0]), (-3, [-1]), (0, [1, 0]),
    (-2, [0, -1]), (-1, [1, 0, -1]), (-2, [1, 0, -1, -2]),
    (0, [2, 1, 0, -1]),
)


def trunc_div(a, b):
    """Integer division toward zero, including negative test operands."""
    if b == 0:
        raise ZeroDivisionError
    magnitude = abs(a) // abs(b)
    return -magnitude if (a < 0) != (b < 0) else magnitude


def evaluate(state, mode):
    if state not in STATES or mode not in ('listing_integer', 'rational_diagnostic'):
        raise ValueError('Outside the twelve contracted EPS=+1 states/modes')
    k, pg, qg, kap = state
    eps = 1
    epsp = eps * (-1) ** (qg * (kap + comb(pg, 2)) % 2)
    epsq = eps * (-1) ** (qg * (qg * (k - 1) + comb(pg, 2)) % 2)
    denominator = k * (1 + kap)
    factor = (trunc_div(2, denominator) if mode == 'listing_integer'
              else Fraction(2, denominator))
    total = factor * (pg * epsp + qg * epsq) * (k - 1 + kap)
    if Fraction(total).denominator != 1:
        raise ValueError('Nonintegral strangeness outside this contract')
    cs = int(total)
    numerators = [(pg + 2 - 2 * ix) * (1 - kap * qg * (2 - k))
                  + cs + eps * (k - 1 - (1 + kap) * qg * (2 - k))
                  for ix in range(1, pg + 2)]
    if any(n % 2 for n in numerators):
        raise ValueError('Charge numerator is odd')
    charges = [trunc_div(n, 2) for n in numerators]
    return dict(prefactor=str(factor), epsp=epsp, epsq=epsq, CS=cs,
                IQX=charges, KQ=[abs(q) for q in charges])


def calculate():
    rows = []
    for number, (state, expected) in enumerate(zip(STATES, EXPECTED), 1):
        integer = evaluate(state, 'listing_integer')
        rational = evaluate(state, 'rational_diagnostic')
        target = dict(CS=expected[0], IQX=expected[1])
        rows.append(dict(multiplet=number, state=dict(zip(('K', 'PG', 'QG', 'KAPPA'), state)),
                         EPS=1, source_table=target, listing_integer=integer,
                         rational_diagnostic=rational,
                         integer_matches_table=all(integer[k] == v for k, v in target.items()),
                         rational_matches_table=all(rational[k] == v for k, v in target.items())))
    return dict(scope='H01748 MAIN; same CS expression H015 PDF18. H006 PDF3 table, EPS=+1 only.',
                interpretation='Python exact arithmetic diagnostic, not historical compiler emulation or mass reconstruction.',
                rows=rows,
                affected_multiplets=[r['multiplet'] for r in rows if not r['integer_matches_table']],
                all_rational_match=all(r['rational_matches_table'] for r in rows))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    result = calculate()
    if args.check:
        if json.loads(OUTPUT.read_text(encoding='utf-8')) != result:
            raise SystemExit('Snapshot differs')
    else:
        OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print('Affected multiplets:', result['affected_multiplets'])
    print('Rational diagnostic matches all twelve table rows:', result['all_rational_match'])


if __name__ == '__main__':
    main()

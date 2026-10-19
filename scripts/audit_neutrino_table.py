"""H004 table relation: use two table entries, never claim a mass prediction."""
import argparse
from decimal import Decimal, localcontext
from fractions import Fraction as F
import json
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / '05_analysis/neutrino_table_results.json'
TABLE_EV = {'e_field': F('5375.675'), 'beta': F('4.006'), 'pi': F('1441.793')}


def xi_bounds(digits=40):
    scale = 10**digits
    n = isqrt(5*scale*scale)
    assert n*n < 5*scale*scale < (n+1)**2
    return (1+F(n, scale))/2, (1+F(n+1, scale))/2


def project(factor, e_field, beta, xi):
    if factor not in (1, 2):
        raise ValueError('Only the two predeclared source alternatives')
    return beta+factor*(e_field-beta)/(1+4*xi)


def projected_bounds(factor, *, halfwidth=F(1, 2000)):
    if halfwidth <= 0 or halfwidth >= 1:
        raise ValueError('Positive sub-eV print envelope required')
    lo, hi = xi_bounds()
    e, b = TABLE_EV['e_field'], TABLE_EV['beta']
    # All three inputs enter monotonically on this fixed positive domain.
    assert 1+4*lo > factor and e-halfwidth > b+halfwidth
    return (project(factor, e-halfwidth, b-halfwidth, hi),
            project(factor, e+halfwidth, b+halfwidth, lo))


def overlaps(left, right):
    return max(left[0], right[0]) <= min(left[1], right[1])


def approx(value):
    with localcontext() as ctx:
        ctx.prec = 60
        return format(Decimal(value.numerator)/Decimal(value.denominator), '.12f')


def calculate():
    xi = xi_bounds()
    rows = []
    for width in (F(1, 2000), F(1, 1000)):
        target = (TABLE_EV['pi']-width, TABLE_EV['pi']+width)
        for factor in (1, 2):
            bounds = projected_bounds(factor, halfwidth=width)
            center = project(factor, TABLE_EV['e_field'], TABLE_EV['beta'], sum(xi)/2)
            rows.append(dict(factor=factor, print_halfwidth_eV=str(width),
                             relation_value_eV_approx=approx(center),
                             projected_bounds_eV_exact=list(map(str, bounds)),
                             projected_bounds_eV_approx=list(map(approx, bounds)),
                             target_bounds_eV_exact=list(map(str, target)),
                             rounding_envelopes_overlap=overlaps(bounds, target)))
    return dict(source='H004 printed275 and376, plus111/118a/118b reviewed in52',
                assignment='Table nu(e0) assigned to neutral e field state from352',
                table_eV={k: str(v) for k, v in TABLE_EV.items()},
                xi_bounds_exact=list(map(str, xi)),
                formula='m_pi=m_beta+a*(m_e_field-m_beta)/(1+4*xi)',
                alternatives={'1': 'printed118b', '2': '111 reduction'},
                primary_halfwidth_eV='1/2000', sensitivity_halfwidth_eV='1/1000',
                rows=rows, independent_mass_prediction=False,
                original_program_execution_proven=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    result = calculate()
    if args.check:
        if json.loads(OUTPUT.read_text(encoding='utf-8')) != result:
            raise SystemExit('Snapshot differs')
        print('OK: exact table relation snapshot')
    else:
        OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
        print(OUTPUT.relative_to(ROOT))


if __name__ == '__main__':
    main()

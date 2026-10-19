"""H011 printed-pair provenance and separately conditional formula arithmetic."""
import argparse
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
import json
from pathlib import Path

try:
    from .audit_alpha import mathematical_pi, eta_k_q, equation_rhs, solve_branches, printing_interval
except ImportError:
    from audit_alpha import mathematical_pi, eta_k_q, equation_rhs, solve_branches, printing_interval

ROOT=Path(__file__).resolve().parents[1]
OUTPUT=ROOT/'05_analysis/alpha_literal_origin_results.json'
PRINTED_INVERSES=('137.03602725','1.00001411')


def exact_pair_bounds():
    # Positive inverse intervals; reciprocal squares decrease monotonically.
    intervals=[(F(t)-F(1,200000000), F(t)+F(1,200000000)) for t in PRINTED_INVERSES]
    return (sum((1/hi**2 for lo,hi in intervals),F(0)),
            sum((1/lo**2 for lo,hi in intervals),F(0)))


def calculate(precision=80):
    with localcontext() as ctx:
        ctx.prec=precision
        def s(x): return format(x,'.15E')
        printed=D(PRINTED_INVERSES[0]);lo,hi=printing_interval(PRINTED_INVERSES[0])
        rows=[]
        for profile,pi in [('mathematical_pi',mathematical_pi()),('H015_PI_literal',D('3.1415926535'))]:
            eta=pi/(pi**4+4).sqrt().sqrt()
            theta=5*eta+2*eta.sqrt()+1
            r0=9*theta/(2*pi)**5
            a_values=[]
            for k in (1,2):
                z=eta_k_q(pi,k=k,q=1)
                a_values.append((1-z.sqrt())/(z*(1+z.sqrt())))
            candidates=[('29a_base_R_not_a_quadratic_root',r0,False),
                        ('uncorrected_quadratic',r0,True),
                        ('H011_A_conditional_eta_bridge',r0*(1-a_values[0]*a_values[1]),True)]
            for name,k,q in [('1982_existing_local_index',1,2),('1982_existing_swapped_index',2,1)]:
                rhs=equation_rhs(pi,dict(equation='1982',eta12_k=k,eta12_q=q))['rhs']
                candidates.append((name,rhs,True))
            for name,rhs,quadratic in candidates:
                if quadratic:
                    small,large=solve_branches(rhs)
                    if max(abs(small*small+large*large-1),abs(small*large-rhs))>D(10)**(-precision+5):
                        raise ValueError('Independent quadratic identities fail')
                else:
                    small,large=rhs,None
                inv=1/small
                rows.append(dict(pi_profile=profile,formula=name,inverse_small=s(inv),
                                 inverse_large=None if large is None else s(1/large),
                                 small_inverse_minus_print=s(inv-printed),
                                 small_inverse_within_print_rounding=lo<=inv<=hi))
        lower,upper=exact_pair_bounds()
        implied_large_inverse=1/(1-1/printed**2).sqrt()
        return dict(source='H011 PDF5(A),PDF6 reciprocal pair; date PDF20. Pair agrees lexically with H015 GINIT.',
                    printed_inverses=list(PRINTED_INVERSES),
                    conditional_formula='H011 A_k=(1-sqrt(eta_1k))/(eta_1k*(1+sqrt(eta_1k))); Y=1. eta bridge q=1,k=1,2 declared, not silently imported.',
                    rows=rows,
                    pair=dict(exact_lower=str(lower),exact_upper=str(upper),
                              lower_decimal=s(D(lower.numerator)/D(lower.denominator)),
                              upper_decimal=s(D(upper.numerator)/D(upper.denominator)),
                              contains_one=lower<=1<=upper,
                              implied_large_inverse_from_printed_small=s(implied_large_inverse)),
                    limits='A pair incompatibility independent of eta/Y; no cause, authorship chain, new mass or empirical exclusion established.')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    modes=parser.add_mutually_exclusive_group()
    modes.add_argument('--write',action='store_true');modes.add_argument('--check',action='store_true')
    args=parser.parse_args();result=calculate()
    if result!=calculate(110): raise SystemExit('80/110-digit display stability failed')
    if args.write: OUTPUT.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    if args.check and json.loads(OUTPUT.read_text(encoding='utf-8'))!=result: raise SystemExit('Snapshot differs')
    for row in result['rows']:
        print(row['pi_profile'],row['formula'],row['inverse_small'],row['small_inverse_within_print_rounding'])
    print('Printed pair interval contains1:',result['pair']['contains_one'])


if __name__=='__main__': main()

"""H004111 ->118b at k=1,q=0,Y=1; exact synthetic algebra, no masses."""
import argparse
from fractions import Fraction as F
import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / '05_analysis/neutrino_book_algebra_results.json'
STATES = {'e': (1, 1, 0), 'mu': (1, 1, 1), 'pi': (2, 0, 0)}


def from_111(state, *, A, B, alpha, sqrt_eta11, xi, eta_squared):
    """Only the three source states; no extension to arbitrary k or charge.

    Fq=2*(3-alpha)*sqrt(eta11): eta_qk cancels at k=1,q=0.
    Y42 multiplies q*eta²*(k-1) and drops out, not all of Fq.
    The (P-Q) correction in Fkappa drops out for these three states.
    """
    if state not in STATES.values():
        raise ValueError('Outside the three reviewed neutral k=1 states')
    A, B, alpha, sqrt_eta11, xi, eta_squared = map(
        F, (A, B, alpha, sqrt_eta11, xi, eta_squared))
    if min(A, B, sqrt_eta11, xi, eta_squared) <= 0 or not 0 < alpha < 3:
        raise ValueError('Requires positive regular coefficients and 0<alpha<3')
    P, Q, kappa = state
    f1 = P*(P+Q)*(-1)**(P+Q)
    f2 = 1+4*xi*comb(P, 2)
    fq = 2*(3-alpha)*sqrt_eta11
    fkappa = 1+2*kappa*xi/(3*eta_squared)
    return A*f1*fq*fkappa/f2+B*(P+Q)


def printed_118b(label, *, A, B, alpha, sqrt_eta11, xi, eta_squared):
    """Separate transcription of the printed expressions, not a repair."""
    A, B, alpha, sqrt_eta11, xi, eta_squared = map(
        F, (A, B, alpha, sqrt_eta11, xi, eta_squared))
    base = 4*A*(3-alpha)*sqrt_eta11
    if label == 'e':
        return base+2*B
    if label == 'mu':
        return base*(1+2*xi/(3*eta_squared))+2*B
    if label == 'pi':
        return base/(1+4*xi)+2*B
    raise ValueError('Unknown source label')


def calculate():
    params = dict(A=F(3), B=F(5), alpha=F(1, 100),
                  sqrt_eta11=F(2), xi=F(1, 2), eta_squared=F(4))
    rows = []
    for label, state in STATES.items():
        direct = from_111(state, **params)
        printed = printed_118b(label, **params)
        rows.append(dict(label=label, k=1, q=0, P=state[0], Q=state[1],
                         kappa=state[2], phi_111=str(direct),
                         phi_118b=str(printed), difference=str(direct-printed)))
    return dict(source='H004 printed342/343,352/353; introduction1',
                profile='k=1,q=0,Y41=Y43=1; B includes common Y44; Y42 drops out',
                scope='Synthetic rational witnesses only, not historical constants or masses',
                synthetic_inputs={k: str(v) for k, v in params.items()}, rows=rows,
                pi_difference='4*A*(3-alpha)*sqrt_eta11/(1+4*xi)',
                pi_nonconstant_term_ratio='2', total_mass_ratio_is_two=False,
                historical_mass_computed=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    result = calculate()
    if args.check:
        if json.loads(OUTPUT.read_text(encoding='utf-8')) != result:
            raise SystemExit('Snapshot differs')
        print('OK: exact book algebra snapshot')
    else:
        OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
        print(OUTPUT.relative_to(ROOT))


if __name__ == '__main__':
    main()

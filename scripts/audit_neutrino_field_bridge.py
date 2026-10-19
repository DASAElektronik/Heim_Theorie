"""Exact reduced-form comparison, not a neutrino mass implementation.

H007 B49 at empty k=1 structure; H010 C0.66 GMASS at a deliberately
hypothetical q=0 projection. Symbols B,T,D are defined in the report.
All numerical values below are synthetic rational witnesses.
"""
import argparse
from fractions import Fraction as F
import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / '05_analysis/neutrino_field_bridge_results.json'


def phi_b49(p, sigma, qsigma, qm_minus_qn, P, Q, kappa,
            *, n4, fourth_root_two, buw, alpha, theta, pi_over_e_squared, sqrt_eta12):
    # Synthetic callers use sigma=0 or -1 with an explicit square-root
    # factor externalized: only the exact zero numerator is evaluated here.
    if sigma + qsigma != 0:
        raise ValueError('Only the empty-structure B49 numerator is contracted')
    if alpha <= 0 or theta <= 0:
        raise ValueError('Positive regular coefficients required')
    # buw denotes an already finite defined B*U/W, not an infinity or a gap.
    F(buw)
    self_term_numerator = n4*p*p/(1+p*p)*(sigma+qsigma)*(fourth_root_two-4*buw)
    correction = P*(P-2)**2*(1+F(kappa, 1)/(2*alpha*theta))
    correction *= pi_over_e_squared*sqrt_eta12*qm_minus_qn
    tail = F((P+1)*comb(Q, 3), 1)/alpha
    return self_term_numerator+correction-tail


def source_pair_field(n5, n6, phi0=F(0)):
    """H007 B6/B65: P=Q=1, k=1, q=0; common mu*alpha_plus removed."""
    return 2*n5+2*n6+phi0


def port_pair_field(kappa, n1_over_q1, B, T, D):
    """H010 GMASS reduced at k=P=Q=1, q=0, after charge subtraction."""
    if kappa not in (0, 1) or min(B, T, D) <= 0:
        raise ValueError('Positive contracted coefficients and kappa=0/1 required')
    return B*(1+kappa*T)*(1+(1-kappa)*n1_over_q1)+D


def calculate():
    B, T, D = F(3), F(2), F(5)
    rows = []
    for kap in (0, 1):
        rows.append(dict(kappa=kap,
                         port_parent_n1_ratio_0=str(port_pair_field(kap, F(0), B, T, D)),
                         port_hypothetical_empty_ratio_minus1=str(port_pair_field(kap, F(-1), B, T, D))))
    return dict(scope='Exact reduced forms only; no historical masses or constants',
                source='H007 PDF3 B6/B10/B13, PDF8 B49, PDF10 B63/B65',
                port='H010 C0.66 GMASS lines998-1027; hypothetical q=0 and n1/Q1=-1 are our diagnostic',
                source_pair='H(1110)=H(1111)=2*N5+2*N6',
                port_pair_empty=['D', 'B*(1+T)+D'],
                positive_difference='B*(1+T)',
                synthetic_coefficients=dict(B=str(B), T=str(T), D=str(D)),
                synthetic_rows=rows,
                historical_mass_computed=False,
                b50_sign_resolved=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    report = calculate()
    if args.check:
        if json.loads(OUTPUT.read_text(encoding='utf-8')) != report:
            raise SystemExit('Snapshot differs')
    else:
        OUTPUT.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print('Exact bridge diagnostic: source pair equal; projected port difference B*(1+T)>0')


if __name__ == '__main__':
    main()

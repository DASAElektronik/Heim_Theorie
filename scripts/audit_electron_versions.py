"""Factor the fixed H015/H010 electron endpoints; no fitted/intermediate profile."""
import argparse
from decimal import Decimal as D, localcontext
import json
from pathlib import Path

try:
    from .audit_h015_electron import evaluate, STATE
    from .audit_alpha import mathematical_pi
except ImportError:
    from audit_h015_electron import evaluate, STATE
    from audit_alpha import mathematical_pi

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT/'05_analysis/electron_versions_results.json'


def build_report(precision=90):
    h15_path = '04_reconstruction/alpha_audit/historical_constants_inputs.json'
    h10_path = '05_analysis/historical_n0_results.json'
    h15_tokens = json.loads((ROOT/h15_path).read_text(encoding='utf-8'))['inputs']
    old = json.loads((ROOT/h10_path).read_text(encoding='utf-8'))
    with localcontext() as ctx:
        ctx.prec = precision
        h15 = evaluate(h15_tokens, STATE, precision)
        h10 = old['cells'][63]
        mu_ratio = D(h10['mu_kg'])/h15['AMU_kg']
        d15 = h15['ALFP']*(h15['mass_terms']['KGH']+h15['mass_terms']['FIG'])
        d10 = D(h10['mass_plus'])*(D(h10['G_aux'])+D(h10['Phi_aux']))
        d_ratio = d10/d15
        f15 = h15['conversion']
        f10 = D(old['inputs']['units']['comparison_factor_kg_to_MeV_c2'])
        f_ratio = f10/f15
        kg_ratio = D(h10['mass_kg'])/h15['mass_kg']
        mev_ratio = D(h10['mass_MeV_c2'])/h15['mass_MeV']
        pi_ratio = mathematical_pi()/D(h15_tokens['PI'].replace('Q','E'))
        hbar_ratio = D(old['inputs']['historical']['hbar_Js'])/D(h15_tokens['HQ'].replace('Q','E'))
        gamma_ratio = D(old['inputs']['historical']['gamma_m3_per_kg_s2'])/D(h15_tokens['GAM'].replace('Q','E'))
        expected_mu = pi_ratio**(D(7)/12)*hbar_ratio**(D(5)/6)*gamma_ratio**(-D(1)/6)
        # Different algebraic forms and saved endpoint independently cross-check.
        residuals = [mu_ratio/expected_mu-1, mu_ratio*d_ratio/kg_ratio-1,
                     mu_ratio*d_ratio*f_ratio/mev_ratio-1,
                     (mu_ratio.ln()+d_ratio.ln()+f_ratio.ln())-mev_ratio.ln()]
        if max(map(abs,residuals)) > D('1e-65'):
            raise ValueError('Endpoint factorization fails; inspect source contracts')
        def s(x):
            return format(x, '.15E')
        factors = {name:dict(ratio=s(value), relative_ppm=s((value-1)*D('1e6')),
                            log_ppm=s(value.ln()*D('1e6')))
                   for name,value in [('mass_scale_mu',mu_ratio),('dimensionless_D',d_ratio),('conversion',f_ratio)]}
        return dict(scope='H015 to H010 fixed endpoints; not an empirical error or historical causal reconstruction',
                    inputs=[h15_path,h10_path],
                    H015=dict(mass_kg=s(h15['mass_kg']),mass_MeV=s(h15['mass_MeV']),D=s(d15),conversion=s(f15)),
                    H010=dict(mass_kg=s(D(h10['mass_kg'])),mass_MeV=s(D(h10['mass_MeV_c2'])),D=s(d10),conversion=s(f10)),
                    factors=factors,
                    totals=dict(kg_ratio=s(kg_ratio),MeV_ratio=s(mev_ratio),
                                kg_relative_ppm=s((kg_ratio-1)*D('1e6')),
                                MeV_relative_ppm=s((mev_ratio-1)*D('1e6')),
                                MeV_log_ppm=s(mev_ratio.ln()*D('1e6'))),
                    scale_log_ppm={name:s(value.ln()*power*D('1e6'))
                                   for name,value,power in [('pi',pi_ratio,D(7)/12),('hbar',hbar_ratio,D(5)/6),('gamma',gamma_ratio,-D(1)/6)]},
                    checks='Algebraic scale and product/log identities below 1e-65; saved H010 endpoint precision limits comparison',
                    limits='Ordinary ppm components are multiplicative; only log contributions add. No new H004 mass inferred.')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    modes=parser.add_mutually_exclusive_group()
    modes.add_argument('--write',action='store_true')
    modes.add_argument('--check',action='store_true')
    args=parser.parse_args()
    result=build_report(90)
    if result != build_report(110):
        raise SystemExit('90/110-digit display stability failed')
    if args.write:
        OUTPUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    if args.check and json.loads(OUTPUT.read_text(encoding='utf-8'))!=result:
        raise SystemExit('Version comparison snapshot differs')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()

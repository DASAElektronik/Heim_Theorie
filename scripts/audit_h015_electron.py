"""Bounded H015 charged E/N0 reconstruction from photographed FORTRAN."""
import argparse
from decimal import Decimal as D, localcontext
import hashlib
import json
from pathlib import Path

try:
    from .audit_historical_constants import initialize
    from .audit_alpha import printing_interval
except ImportError:
    from audit_historical_constants import initialize
    from audit_alpha import printing_interval

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "04_reconstruction/alpha_audit/h015_electron_inputs.json"
OUTPUT = ROOT / "05_analysis/h015_electron_results.json"
STATE = dict(K=1, PG=1, QG=1, KAPPA=0, EPS=1, IX=2, N=0)


def evaluate(tokens, state, precision=60):
    """No printed output is accepted here. Only the contracted state is supported."""
    if state != STATE:
        raise ValueError("Only the contracted H015 charged E/N0 state is supported")
    with localcontext() as ctx:
        ctx.prec = precision
        v = initialize(tokens, precision)
        pi, xi, alpha, beta, eta = (v[k] for k in ("PI", "XI", "ALFA", "BETA", "ETA"))
        k, pg, qg, kap, eps, ix = (state[n] for n in ("K", "PG", "QG", "KAPPA", "EPS", "IX"))
        # MAIN ISN0028-0037, with binomial(PG,2)=0 in this fixed state.
        epsp = eps*(-1)**(qg*kap % 2)
        epsq = eps*(-1)**(qg*(qg*(k-1)) % 2)
        cs = (2//(k*(1+kap)))*(pg*epsp+qg*epsq)*(k-1+kap)
        numerator = (pg+2-2*ix)*(1-kap*qg*(2-k))+cs+eps*(k-1-(1+kap)*qg*(2-k))
        assert numerator % 2 == 0
        qx, q = numerator//2, abs(numerator//2)
        is_ = k*k+1
        Q = [3*2**(is_-2), 2*is_-1, 2*is_+2*(-1)**k, 2**(is_-1)-1]
        d = pi/(q**4*(4+k)+pi**4)**D('.25')
        s = d.sqrt()
        a1, a2 = (1+s)/2, 1/d
        a3 = 1-alpha*xi**3*(1+s)/(3*d**3)-2*xi*d/v['EBN']*((1-s)/(1+s))**2
        if min(a1, a2, a3) <= 0:
            raise ValueError("Selection requires positive coefficients")
        # Relevant initialization denominators remain regular before reduction.
        domains = {'A36_denominator': 1-pi*v['EBN']*(xi*v['EBN'])**2*(1-beta**2),
                   'A41_denominator': 2*eta**2-alpha,
                   'eta': eta, 'eta_qk': d, 'alpha': alpha, 'xi': xi,
                   'ALFP': v['ALFP']}
        if any(not x.is_finite() or x <= 0 for x in domains.values()):
            raise ValueError("Nonregular fixed-state coefficient domain")
        # GBASE: label50 has factor (1-QG)=0, PG=1 and KAPPA=0.
        # Thus TEMP1=1. K=1 jumps to label53, assigning TEMP2=1.
        wg_factor = D(1)
        exponential = (-D(1)/3).exp()
        gkq = Q[0]**3*a1+Q[1]**2*a2+Q[2]*a3+exponential
        fn_prefactor = 1-qg*(2-k)*(1-kap)
        assert fn_prefactor == 0
        fn = D(0)  # Also N=0 makes both finite excitation terms zero.
        remaining = gkq*wg_factor*(1+fn)
        trace, integers = [], []
        for coeff, power in ((a1, 3), (a2, 2), (a3, 1)):
            integer = 0
            while coeff*(integer+1)**power <= remaining:
                integer += 1
                if integer > 100:
                    raise ValueError("Outside bounded selection domain")
            lower = remaining-coeff*integer**power
            upper = coeff*(integer+1)**power-remaining
            trace.append(dict(integer=integer, lower_margin=lower, upper_margin=upper))
            integers.append(integer)
            remaining = lower
        if integers != Q[:3] or not 0 < remaining < 1:
            raise ValueError("Exact N0 final-step certificate not applicable")
        raw_k4 = -3*remaining.ln()
        # Identity W4=exp(-1/3), rather than a rounded logarithm, fixes K4.
        integers.append(1)
        occupations = [a-b for a, b in zip(integers, Q)]
        i1, i2, i3, i4 = integers
        kgh = 4*(a1*i1**2*(1+i1)**2/4+a2*i2*(2*i2**2+3*i2+1)/6+a3*i3*(i3+1)/2+i4)
        r = v['ALFM']/v['ALFP']
        # GMASS ISN0008 product, reduced only by the fixed state's zero/unit factors.
        fig_factors = [3/(pi*s), 1-r, D(2), 1-alpha/3, D(1), D(1),
                       2*s*s, 1+4*pi*alpha/(eta*eta.sqrt()), 1+D(occupations[0])/Q[0]]
        product = D(1)
        for factor in fig_factors:
            product *= factor
        fig = product+8*(1-r)*alpha/xi**2+4*r
        fig_reduced = (1-r)*(12*s/pi*(1-alpha/3)*(1+4*pi*alpha/(eta*eta.sqrt()))+8*alpha/xi**2)+4*r
        mass = v['AMU']*v['ALFP']*(kgh+fig)
        return dict(state_derived=dict(CS=cs, QX=qx, KQ=q, Q=Q),
                    coefficients=dict(d=d, a1=a1, a2=a2, a3=a3), domains=domains,
                    selection=dict(GKQ=gkq, WGX_factor=wg_factor, FN=fn, steps=trace,
                                   K=integers, n=occupations, W4=remaining,
                                   final_identity="W4=exp(-1/3); -3*ln(W4)=1",
                                   raw_K4=raw_k4, raw_truncation=int(raw_k4),
                                   cancellation_residual=remaining-exponential),
                    mass_terms=dict(KGH=kgh, FIG=fig, FIG_reduced=fig_reduced,
                                    FIG_product_factors=fig_factors, FIG_identity_residual=fig-fig_reduced),
                    AMU_kg=v['AMU'], ALFP=v['ALFP'], conversion=v['FAKMEV'],
                    mass_kg=mass, mass_MeV=mass*v['FAKMEV'])


def strings(value):
    if isinstance(value, D):
        return format(value, '.15E')
    if isinstance(value, dict):
        return {k: strings(v) for k, v in value.items()}
    if isinstance(value, list):
        return [strings(v) for v in value]
    return value


def build_report():
    doc = json.loads(INPUT.read_text(encoding='utf-8'))
    if doc['target_fitting'] is not False:
        raise ValueError("No fitting permitted")
    tokens = json.loads((ROOT/doc['constant_input_path']).read_text(encoding='utf-8'))['inputs']
    runs = {p: evaluate(tokens, doc['state'], p) for p in (60, 90)}
    diagnostics = []
    for precision, row in runs.items():
        sel, mass = row['selection'], row['mass_terms']
        diagnostics.append(dict(precision=precision, raw_K4=str(sel.pop('raw_K4')),
                                raw_truncation=sel.pop('raw_truncation'),
                                cancellation_residual=str(sel.pop('cancellation_residual')),
                                FIG_identity_residual=str(mass.pop('FIG_identity_residual'))))
    if strings(runs[60]) != strings(runs[90]):
        raise ValueError("60/90-digit significant-output stability failed")
    result = runs[90]
    # Printed results enter only after reconstruction and stability checking.
    printed = doc['comparison_only']
    with localcontext() as ctx:
        ctx.prec = 90
        token = printed['printed_mass_MeV'].replace('Q', 'E')
        lo, hi = printing_interval(token)
        comparison = dict(printed=printed['printed_mass_MeV'], lower=lo, upper=hi,
                          difference=result['mass_MeV']-D(token),
                          mass_matches=lo <= result['mass_MeV'] <= hi,
                          K_matches=result['selection']['K'] == printed['printed_K'],
                          n_matches=result['selection']['n'] == printed['printed_n'])
    return dict(profile=doc['profile'], scope=doc['scope'], result=strings(result),
                precision_diagnostics=diagnostics, comparison=strings(comparison),
                limits="Analytic final integer; no historical compiler replay, empirical validation or original input-calibration proof")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--write', action='store_true')
    mode.add_argument('--check', action='store_true')
    parser.add_argument('--verify-sources', action='store_true')
    args = parser.parse_args()
    if args.verify_sources:
        source = json.loads(INPUT.read_text(encoding='utf-8'))['source']
        if hashlib.sha256((ROOT/source['path']).read_bytes()).hexdigest().upper() != source['sha256']:
            raise SystemExit('H015 hash differs')
        print('H015 source hash verified.')
    result = build_report()
    if args.write:
        OUTPUT.write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    if args.check and json.loads(OUTPUT.read_text(encoding='utf-8')) != result:
        raise SystemExit('Stored H015 electron diagnostic differs')
    print(json.dumps(result['comparison'], indent=2))
    print('Own mass (MeV):', result['result']['mass_MeV'])
    if not all(result['comparison'][k] for k in ('mass_matches', 'K_matches', 'n_matches')):
        raise SystemExit('Photographed output comparison failed; no parameters changed')


if __name__ == '__main__':
    main()

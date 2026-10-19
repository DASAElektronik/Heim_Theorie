"""Independent arithmetic, branch and scope checks for one H015 electron."""
from decimal import Decimal as D, localcontext
import json
import math
import unittest

from scripts.audit_h015_electron import INPUT, ROOT, STATE, build_report, evaluate


class H015ElectronTests(unittest.TestCase):
    def setUp(self):
        doc = json.loads(INPUT.read_text(encoding='utf-8'))
        self.tokens = json.loads((ROOT/doc['constant_input_path']).read_text(encoding='utf-8'))['inputs']

    def test_photographed_output(self):
        report = build_report()
        for key in ('mass_matches', 'K_matches', 'n_matches'):
            self.assertTrue(report['comparison'][key])
        # Require the actual photographed state, not merely internal agreement.
        self.assertEqual(report['result']['selection']['K'], [3, 3, 2, 1])
        self.assertEqual(report['result']['selection']['n'], [0, 0, 0, 0])
        self.assertEqual(report['comparison']['printed'], '0.51100326Q+00')

    def test_independent_binary64_source_expression(self):
        # Direct GBASE expression before the d-power cancellation; scale via
        # its sixth-power identity rather than the production cube/square roots.
        pi, xi, a = 3.1415926535, 1.61803399, 1/137.03602725
        eta = pi/(4+pi**4)**.25
        d = pi/(5+pi**4)**.25
        a1, a2 = (1+math.sqrt(d))/2, 1/d
        a3 = math.exp(0)-((a/3)*(1+math.sqrt(d))*(xi/d**2)**3*d**3
                         +d/(math.e*d)*(2*xi*d)*((1-math.sqrt(d))/(1+math.sqrt(d)))**2)
        t = 1-2/3*xi*eta**2*(1-math.sqrt(eta))
        ap, am = t/eta**(7/3)-1, t/eta**(4/3)-1
        scale = (pi**3.5*(1.0545887e-34)**5/(3*6.6732e-11*(2.99792458e8)**3))**(1/6)
        g = 27*a1+9*a2+2*a3+math.exp(-1/3)
        k1 = math.floor((g/a1)**(1/3))
        w2 = g-a1*k1**3
        k2 = math.floor(math.sqrt(w2/a2))
        w3 = w2-a2*k2**2
        k3 = math.floor(w3/a3)
        self.assertEqual([k1, k2, k3], [3, 3, 2])
        # K4=1 is the analytic identity; don't emulate truncation in binary64.
        kgh = a1*k1**2*(k1+1)**2+2/3*a2*k2*(2*k2*k2+3*k2+1)+2*a3*k3*(k3+1)+4
        fig = ((1-am/ap)*(12*math.sqrt(d)/pi*(1-a/3)*(1+4*pi*a/eta**1.5)
                         +8*a/xi**2)+4*am/ap)
        mass = scale*ap*(kgh+fig)*5.609545e29
        result = evaluate(self.tokens, STATE)
        self.assertAlmostEqual(mass, float(result['mass_MeV']), delta=2e-13)
        self.assertGreater(mass, .511003255)
        self.assertLess(mass, .511003265)

    def test_selection_and_fig_identities(self):
        with localcontext() as ctx:
            ctx.prec = 90
            row = evaluate(self.tokens, STATE, 90)
            a1, a2, a3 = (row['coefficients'][k] for k in ('a1', 'a2', 'a3'))
            w = row['selection']['GKQ']
            for coeff, exponent, integer in ((a1, 3, 3), (a2, 2, 3), (a3, 1, 2)):
                self.assertGreater(w, coeff*integer**exponent)
                self.assertLess(w, coeff*(integer+1)**exponent)
                w -= coeff*integer**exponent
            self.assertLess(abs(w-(-D(1)/3).exp()), D('1e-85'))
            self.assertLess(abs(row['selection']['raw_K4']-1), D('1e-85'))
            self.assertLess(abs(row['mass_terms']['FIG_identity_residual']), D('1e-85'))
            self.assertLess(abs(row['mass_terms']['KGH']-(144*a1+56*a2+12*a3+4)), D('1e-85'))
            self.assertLess(abs(row['mass_MeV']/row['mass_kg']-D('5.609545e29')), D('1e-55'))

    def test_beta_is_inactive_in_this_reduced_mass(self):
        baseline = evaluate(self.tokens, STATE)
        changed = evaluate(self.tokens | {'BETA_inverse': '1.00002Q0'}, STATE)
        self.assertNotEqual(baseline['domains']['A36_denominator'], changed['domains']['A36_denominator'])
        self.assertEqual(baseline['mass_kg'], changed['mass_kg'])
        self.assertEqual(baseline['selection']['K'], changed['selection']['K'])

    def test_other_states_are_rejected(self):
        for changed in (STATE | {'IX': 1}, STATE | {'N': 1}, STATE | {'KAPPA': 1}):
            with self.assertRaises(ValueError):
                evaluate(self.tokens, changed)


if __name__ == '__main__':
    unittest.main()

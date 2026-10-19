"""Conditional (98) component-curve diagnostics, not a physical path solver.

The relaxed s interval includes formal boundary values, not a declaration
of continuous or physically permitted charge states.  A positive common
potential factor and matching epsilon sign are assumed.  No Heim inputs,
mass profiles, field dynamics or metronic grid are reconstructed here.
"""

import unittest
from fractions import Fraction as F


def components(s):
    s = F(s)
    return dict(u=(1+s)/2, r=s*s, o=(1+s)**2/4, d=(1-s)**2)


def tied_h_path(sequence, a=F(1, 10), k=1):
    """Extra common-grid/a*delta assumption, X constant; positive U/R/H only."""
    value = F(1)
    for old, new in zip(sequence, sequence[1:]):
        prev, curr = components(old), components(new)
        ru, rr = 1-prev['u']/curr['u'], 1-prev['r']/curr['r']
        jump = a*(ru+(1-4*k)*rr)
        if jump >= 1:
            raise ValueError('No positive H continuation for these synthetic steps')
        value /= 1-jump
    return value


class PotentialPathTests(unittest.TestCase):
    def test_four_component_identities(self):
        for s in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1)):
            c = components(s)
            self.assertEqual(c['o'], c['u']**2)
            self.assertEqual(c['r'], (2*c['u']-1)**2)
            self.assertEqual(c['d'], 4*(1-c['u'])**2)

    def test_relaxed_ranges_and_boundary_values(self):
        for s in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1)):
            c = components(s)
            self.assertTrue(F(1, 2) <= c['u'] <= 1)
            self.assertTrue(0 <= c['r'] <= 1)
            self.assertTrue(F(1, 4) <= c['o'] <= 1)
            self.assertTrue(0 <= c['d'] <= 1)
        self.assertEqual(components(0), dict(u=F(1, 2), r=0, o=F(1, 4), d=1))
        self.assertEqual(components(1), dict(u=1, r=1, o=1, d=0))

    def test_charge_relation_inversion_in_relaxed_domain(self):
        # qbar=q/pi; neither qbar nor s here asserts an integer charge state.
        for k in (1, 2, 5):
            for s in (F(1, 4), F(1, 2), F(3, 4), F(1)):
                qbar_fourth = (s**(-8)-1)/(4+k)
                self.assertGreaterEqual(qbar_fourth, 0)
                self.assertEqual(s**8*(1+(4+k)*qbar_fourth), 1)

    def test_components_cannot_vary_independently_on_the_curve(self):
        values = [components(s) for s in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1))]
        for a, b in zip(values, values[1:]):
            for key in ('u', 'r', 'o'):
                self.assertGreater(b[key], a[key])
            self.assertLess(b['d'], a['d'])

    def test_two_h_lower_limits_require_different_curve_points(self):
        self.assertEqual(components(0)['u'], F(1, 2))
        self.assertEqual(components(0)['r'], 0)
        self.assertEqual(components(1)['r'], 1)
        self.assertEqual(components(1)['u'], 1)
        # The identities yield a direct incompatibility, including the closure.
        self.assertNotEqual((2*F(1, 2)-1)**2, 1)

    def test_weighted_h_upper_limit_is_outside_unrescaled_u_range(self):
        for alpha in (F(1, 137), F(1, 2), F(99, 100)):
            for final_s in (F(0), F(1, 4), F(3, 4), F(1)):
                beta = alpha*components(final_s)['u']/3
                self.assertGreater(beta, 0)
                self.assertLess(beta, F(1, 2))
                self.assertLess(2*beta-1, 0)  # Required s would leave the branch.

    def test_coupled_finite_differences(self):
        for s, t in ((F(3, 4), F(1, 2)), (F(1, 3), F(2, 3))):
            new, old = components(s), components(t)
            ds = s-t
            self.assertEqual(new['u']-old['u'], ds/2)
            self.assertEqual(new['r']-old['r'], (s+t)*ds)
            self.assertEqual(new['o']-old['o'], (2+s+t)*ds/4)
            self.assertEqual(new['d']-old['d'], (s+t-2)*ds)
            self.assertEqual((new['u']-old['u'])/new['u'], ds/(1+s))
            self.assertEqual((new['r']-old['r'])/new['r'], (s*s-t*t)/(s*s))

    def test_tied_component_paths_retain_finite_step_dependence(self):
        first = (F(1, 2), F(3, 4), F(1))
        second = (F(1, 2), F(7, 8), F(1))
        self.assertEqual(tied_h_path(first), F(16800, 21659))
        self.assertEqual(tied_h_path(second), F(98000, 123261))
        self.assertNotEqual(tied_h_path(first), tied_h_path(second))
        # At final s=1 D=0; this H-only witness never evaluates lnD or G.
        self.assertEqual(components(first[-1])['d'], 0)

    def test_independent_positive_channel_interpolation_is_not_ruled_out(self):
        # Own auxiliary channels, NOT raw (98) components or Heim dynamics.
        alpha, sf = F(1, 137), F(3, 4)
        beta = alpha*components(sf)['u']/3
        for t in (F(0), F(1, 3), F(2, 3), F(1)):
            channel_u = (1-t)*F(1, 2)+t*beta
            channel_r = (1-t)+t*sf*sf
            self.assertGreater(channel_u, 0)
            self.assertGreater(channel_r, 0)
        self.assertNotEqual((2*F(1, 2)-1)**2, 1)

    def test_w_endpoint_ratio_is_a_component_switch_with_weight(self):
        for k in (1, 2):
            for sf in (F(1, 4), F(1, 2), F(3, 4)):
                c = components(sf)
                ck = F(2)**(k-2)
                self.assertEqual(ck*c['d']/c['o'], 2**k*((1-sf)/(1+sf))**2)


if __name__ == '__main__':
    unittest.main()

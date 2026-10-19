from fractions import Fraction as F
from itertools import product
import unittest

from scripts.audit_neutrino_table import (
    TABLE_EV, calculate, overlaps, project, projected_bounds, xi_bounds,
)


class NeutrinoTableTests(unittest.TestCase):
    def test_golden_ratio_bounds_have_exact_polynomial_certificate(self):
        lo, hi = xi_bounds()
        self.assertLess(lo*lo-lo-1, 0)
        self.assertGreater(hi*hi-hi-1, 0)
        self.assertLess(hi-lo, F(1, 10**39))

    def test_analytic_bounds_enclose_all_rational_corners(self):
        w = F(1, 2000)
        e, b = TABLE_EV['e_field'], TABLE_EV['beta']
        for a in (1, 2):
            bounds = projected_bounds(a)
            corners = [project(a, E, B, X) for E, B, X in product(
                (e-w, e+w), (b-w, b+w), xi_bounds())]
            self.assertEqual(bounds, (min(corners), max(corners)))

    def test_only_111_alternative_overlaps_printed_pi_interval(self):
        results = calculate()['rows']
        self.assertEqual([r['rounding_envelopes_overlap'] for r in results],
                         [False, True, False, True])
        self.assertLess(projected_bounds(1)[1], 723)
        self.assertTrue(overlaps(projected_bounds(2), (F('1441.7925'), F('1441.7935'))))

    def test_common_scale_cancels_in_relation(self):
        # Synthetic phi constants with original F1 factors, independently
        # constructed before multiplication by an arbitrary common scale.
        xi = F(8, 5)
        C, B, scale = F(7, 3), F(2, 5), F(13, 11)
        e, beta = scale*(C+2*B), scale*2*B
        pi_from_111 = scale*(2*C/(1+4*xi)+2*B)
        self.assertEqual(project(2, e, beta, xi), pi_from_111)
        with self.assertRaises(ValueError):
            project(3, e, beta, xi)


if __name__ == '__main__':
    unittest.main()

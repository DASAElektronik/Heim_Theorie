"""Exact scalar checks of a declared recurrence, not a Heim field solution."""

import itertools
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"scripts"))
import audit_xi_recurrence as audit


class XiRecurrenceTests(unittest.TestCase):
    def test_backward_selector_identity(self):
        for xn, p, pp in itertools.product((F(-2), F(1, 3), F(5)), repeat=3):
            d = xn-p
            d2 = xn-2*p+pp
            self.assertEqual(d2-3*d+xn, audit.selector_residual(xn, p, pp))

    def test_recurrence_annuls_selector(self):
        for n in range(2, 35):
            self.assertEqual(audit.selector_residual(
                audit.fibonacci(n), audit.fibonacci(n-1), audit.fibonacci(n-2)), 0)

    def test_exact_exponential_does_not_force_selector(self):
        # x[n]=2**n; r[n]=n*ell and alpha*ell=ln(2) is an exact exponential.
        for n in range(2, 20):
            self.assertEqual(audit.selector_residual(2**n, 2**(n-1), 2**(n-2)),
                             -2**(n-2))

    def test_all_declared_positive_starts_inside_uniform_hull(self):
        starts = (F(1, 1000000), F(1, 3), F(1), F(1000000))
        for a, b, n in itertools.product(starts, starts, range(2, 30)):
            x, y = audit.sequence_pair(a, b, n)
            lo, hi = audit.ratio_window(n)
            self.assertLess(lo, y/x)
            self.assertLess(y/x, hi)

    def test_cassini_and_hull_width(self):
        for n in range(2, 40):
            fm, fn, fp = (audit.fibonacci(k) for k in (n-1, n, n+1))
            self.assertEqual(fp*fm-fn*fn, (-1)**n)
            lo, hi = audit.ratio_window(n)
            self.assertEqual(hi-lo, F(1, fn*fm))

    def test_nested_hulls_enclose_positive_golden_root(self):
        for n in range(2, 40):
            lo, hi = audit.ratio_window(n)
            next_lo, next_hi = audit.ratio_window(n+1)
            self.assertLess(audit.golden_polynomial(lo), 0)
            self.assertGreater(audit.golden_polynomial(hi), 0)
            self.assertTrue(lo <= next_lo < next_hi <= hi)

    def test_scale_invariance(self):
        for n in range(15):
            x, y = audit.sequence_pair(F(1, 3), F(7, 2), n)
            u, v = audit.sequence_pair(F(5, 9), F(35, 6), n)
            self.assertEqual(y/x, v/u)

    def test_two_step_ratio_is_one_plus_one_step_ratio(self):
        for n in range(1, 30):
            x, y = audit.sequence_pair(3, 7, n)
            self.assertEqual((x+y)/x, 1+y/x)
        # phi^2=1+phi explains Y-limit; not a rule for a separate divisor z.

    def test_eight_decimal_rounding_cell_is_uniform_at_n22(self):
        cell_lo, cell_hi = F("1.618033985"), F("1.618033995")
        lo, hi = audit.ratio_window(22)
        self.assertTrue(cell_lo < lo < hi < cell_hi)
        lo21, hi21 = audit.ratio_window(21)
        self.assertFalse(cell_lo < lo21 < hi21 < cell_hi)
        self.assertEqual((lo, hi), (F(17711, 10946), F(28657, 17711)))

    def test_identity_with_five_is_polynomial_consequence(self):
        for x in (F(-4), F(0), F(3, 2), F(5)):
            self.assertEqual((2*x-1)**2-5, 4*audit.golden_polynomial(x))

    def test_both_divisors_survive_without_extra_rule(self):
        self.assertEqual(audit.divisor_candidates(), (3, 5))
        for z in audit.divisor_candidates():
            self.assertTrue(1 < z < 15 and 15 % z == 0)
            self.assertGreater(F(z, 15), F(1, 15))
        self.assertEqual(tuple(z for z in audit.divisor_candidates() if z == 5), (5,))

    def test_domain_validation(self):
        for n in (True, -1, F(2), 1.5):
            with self.assertRaises(ValueError):
                audit.ratio_window(n)
        for a in (True, 0.5, "1/2"):
            with self.assertRaises(TypeError):
                audit.sequence_pair(a, 1, 2)
        for a in (0, -1):
            with self.assertRaises(ValueError):
                audit.sequence_pair(a, 1, 2)


if __name__ == "__main__":
    unittest.main()

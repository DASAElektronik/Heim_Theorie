"""Conditional scalar witnesses for M7 and the mixed H/G step, not masses.

No actual metronic potential path or common argument grid is asserted.
All finite values, steps and paths below are synthetic.  The existing
exact rational logarithm enclosure is reused only as a numerical helper.
"""

import unittest
from fractions import Fraction as F

from test_metronic_integration import fib_sequence, log_interval


def linear_interval(terms):
    lower, upper = F(0), F(0)
    for weight, (lo, hi) in terms:
        lower += weight*(lo if weight >= 0 else hi)
        upper += weight*(hi if weight >= 0 else lo)
    return lower, upper


def log_residual(c, r):
    """ln[1/(1-c*r)] - c*ln[1/(1-r)], on its positive domain."""
    if r >= 1 or c*r >= 1:
        raise ValueError("positive neighbouring values required")
    return linear_interval(((1, log_interval(1/(1-c*r))),
                            (-c, log_interval(1/(1-r)))))


def path_multiplier(values, c):
    result = F(1)
    for previous, current in zip(values, values[1:]):
        r = 1-F(previous, current)
        if c*r >= 1:
            raise ValueError("positive recurrence multiplier required")
        result /= 1-c*r
    return result


class MetronicStepTests(unittest.TestCase):
    def test_exponential_scaled_difference_and_inner_shift_disagree_exactly(self):
        # exp(phi)=4, exp(phi_previous)=1, a=1/2; exp(a*ln4)=2.
        self.assertEqual(F(1, 2)*(4-1), F(3, 2))
        self.assertEqual(4-2, 2)
        self.assertNotEqual(F(3, 2), 2)
        # Opposite exponent jump: exp(phi)=1, exp(phi_previous)=4.
        self.assertGreater(1-2, F(1, 2)*(1-4))

    def test_square_identity_separates_scaling_from_value_shift(self):
        for a in (F(1, 2), F(1, 100), F(1, 10**12)):
            for phi, jump in ((F(3), F(1)), (F(2), F(-1)), (F(7, 3), F(2, 5))):
                scaled = a*(phi**2-(phi-jump)**2)
                shifted = phi**2-(phi-a*jump)**2
                self.assertEqual(shifted-scaled, a*(1-a)*jump**2)
                self.assertGreater(shifted-scaled, 0)

    def test_affine_functions_are_an_exact_overlap_not_general_equivalence(self):
        a, phi, jump = F(1, 7), F(9, 4), F(3, 8)
        f = lambda x: 3*x-5
        self.assertEqual(a*(f(phi)-f(phi-jump)), f(phi)-f(phi-a*jump))

    def test_mixed_hg_recurrence_retains_unscaled_x_term(self):
        a, rx = F(1, 100), F(2, 5)
        rv1, rv3, rvg, rw = F(1, 5), F(-1, 8), F(1, 7), F(-1, 10)
        for k in (1, 2):
            ah, bg = F(2*k+1, 2), F(k, 2)
            sh = ah*rx+a*(rv1+(1-4*k)*rv3)
            sg = bg*rx+a*(rvg+k*rv3+rw)
            # k=2 with rx=2/5 gives sh>1: no positive H recurrence here.
            if k == 2:
                self.assertGreaterEqual(sh, 1)
            for s in ((sh, sg) if k == 1 else (sg,)):
                previous = F(7, 5)
                current = previous/(1-s)
                self.assertGreater(current, 0)
                self.assertEqual((current-previous)/current, s)
            self.assertNotEqual(sh, a*(ah*rx+rv1+(1-4*k)*rv3))

    def test_x_only_log_residuals_have_opposite_signs(self):
        seq = fib_sequence(82)
        for n in (40, 80):
            r = F(seq[n]-seq[n-1], seq[n])
            lo_g, hi_g = log_residual(F(1, 2), r)
            lo_h, hi_h = log_residual(F(3, 2), r)
            self.assertLess(hi_g, 0)
            self.assertGreater(lo_h, 0)
            self.assertLess(lo_g, hi_g)
            self.assertLess(lo_h, hi_h)

    def test_x_only_k2_h_is_positive_but_sensitive(self):
        seq = fib_sequence(82)
        r = F(seq[80]-seq[79], seq[80])
        margin = 1-F(5, 2)*r
        self.assertGreater(margin, F(4, 100))
        self.assertLess(margin, F(5, 100))
        # More log-series terms for the larger positive multiplier.
        actual = log_interval(1/margin, terms=300)
        expected = log_interval(1/(1-r))
        lo, hi = linear_interval(((1, actual), (-F(5, 2), expected)))
        self.assertGreater(lo, F(18, 10))
        self.assertLess(hi, F(20, 10))

    def test_c1_recurrence_telescopes_without_approximation(self):
        for values in ([1, 2, 4], [1, 3, 4], [4, 2, 1], [3, 7, 2]):
            self.assertEqual(path_multiplier(values, F(1)), F(values[-1], values[0]))

    def test_same_endpoints_do_not_determine_weighted_finite_path(self):
        first, second = path_multiplier([1, 2, 4], F(1, 2)), path_multiplier([1, 3, 4], F(1, 2))
        self.assertEqual(first, F(16, 9))
        self.assertEqual(second, F(12, 7))
        self.assertNotEqual(first, second)
        # Both would give sqrt(4/1)=2 after the logarithmic replacement.
        self.assertNotEqual(first, 2)
        self.assertNotEqual(second, 2)

    def test_mixed_residual_identity_with_signed_potential_weights(self):
        a, c, rx = F(1, 10), F(3, 2), F(3, 8)
        weights, jumps = (F(1), F(-3)), (F(1, 5), F(-1, 8))
        total = c*rx+a*sum(w*r for w, r in zip(weights, jumps))
        args = [(1, total), (-c, rx)]+[(-a*w, r) for w, r in zip(weights, jumps)]
        direct = linear_interval([(w, log_interval(1/(1-r))) for w, r in args])
        errors = linear_interval([(w, tuple(v-r for v in log_interval(1/(1-r)))) for w, r in args])
        self.assertEqual(direct, errors)  # The linear terms cancel exactly.

    def test_recurrence_requires_a_positive_denominator(self):
        with self.assertRaises(ValueError):
            path_multiplier([1, 2], F(2))
        with self.assertRaises(ValueError):
            log_residual(F(3), F(1, 2))


if __name__ == "__main__":
    unittest.main()

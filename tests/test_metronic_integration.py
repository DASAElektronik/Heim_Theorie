"""H003 M2/M2a/M3a/M7/M8: exact diagnostics, not a Heim mass solver.

All potential paths and finite test values are synthetic.  Fibonacci
recurrence tests the specific large-index argument under the literal M2
backward step.  No microscopic step, physical error tolerance, or new
coefficient/mass fit is supplied.  Logarithms are enclosed by exact
rational atanh series and an explicit tail bound, not binary floats.
"""

import unittest
from fractions import Fraction as F
from math import prod


def log_interval(value, terms=40):
    """Certified rational enclosure of ordinary ln(value), value>0."""
    value = F(value)
    if value <= 0 or terms < 1:
        raise ValueError("positive argument and at least one term required")
    if value < 1:
        lo, hi = log_interval(1/value, terms)
        return -hi, -lo
    z = (value-1)/(value+1)
    partial = 2*sum((z**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    tail = 2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
    return partial, partial+tail


def log_error_interval(r):
    lo, hi = log_interval(1/(1-r))
    return lo-r, hi-r


def fib_sequence(last):
    sequence = [1, 1]
    for _ in range(2, last+1):
        sequence.append(sequence[-1]+sequence[-2])
    return sequence


class MetronicIntegrationTests(unittest.TestCase):
    def test_inclusive_backward_sum_telescopes(self):
        for values in ([n*n for n in range(10)], [F(1, n+1) for n in range(10)]):
            for a in range(1, 6):
                for b in range(a+1, 9):
                    actual = sum(values[n]-values[n-1] for n in range(a, b+1))
                    self.assertEqual(actual, values[b]-values[a-1])

    def test_start_shift_produces_the_desired_lower_value(self):
        values = [n*n for n in range(10)]
        for a in range(1, 6):
            b = a+2
            actual = sum(values[n]-values[n-1] for n in range(a+1, b+1))
            self.assertEqual(actual, values[b]-values[a])

    def test_potential_shift_requires_the_increment_at_the_correct_index(self):
        a = 3
        v = lambda n: n*n
        self.assertEqual(v(a)+(v(a+1)-v(a)), v(a+1))
        self.assertNotEqual(v(a)+(v(a)-v(a-1)), v(a+1))
        self.assertEqual(v(a)+(v(a)-v(a-1)), 14)
        self.assertEqual(v(a+1), 16)

    def test_corrected_product_rule(self):
        for u, up, v, vp in ((F(3), F(1), F(5), F(2)),
                              (F(2, 3), F(7, 8), F(-3, 4), F(2, 5))):
            du, dv = u-up, v-vp
            self.assertEqual(u*v-up*vp, u*dv+v*du-du*dv)
            self.assertNotEqual(u*v-up*vp, u*dv+v*du)

    def test_corrected_quotient_rule(self):
        for u, up, v, vp in ((F(3), F(1), F(5), F(2)),
                              (F(2, 3), F(7, 8), F(-3, 4), F(2, 5))):
            du, dv = u-up, v-vp
            self.assertEqual(u/v-up/vp, (v*du-u*dv)/(v*vp))

    def test_divided_difference_is_not_instantaneous_derivative(self):
        x, dx = F(3, 2), F(1, 4)
        finite = x*x-(x-dx)**2
        self.assertEqual(finite, (2*x-dx)*dx)
        self.assertNotEqual(finite, 2*x*dx)

    def test_logarithmic_telescope_has_the_two_step_ratio(self):
        seq = fib_sequence(82)
        for z in (5, 20, 40, 80):
            ratio = prod(F(seq[n], seq[n-1]) for n in (z, z+1))
            self.assertEqual(ratio, F(seq[z+1], seq[z-1]))
            lo1, hi1 = log_interval(F(seq[z], seq[z-1]))
            lo2, hi2 = log_interval(F(seq[z+1], seq[z]))
            lo, hi = log_interval(ratio)
            # Overlap checks independent series evaluations; exact identity is above.
            self.assertLessEqual(lo1+lo2, hi)
            self.assertGreaterEqual(hi1+hi2, lo)

    def test_log_relative_jump_error_has_signed_jump_bounds(self):
        rho = F(1, 2)
        for r in (F(-1, 2), F(-1, 4), F(1, 1000), F(1, 4), F(1, 2)):
            lo, hi = log_error_interval(r)
            self.assertGreater(lo, 0)
            self.assertGreaterEqual(lo, r*r/(2*(1+rho)))
            self.assertLessEqual(hi, r*r/(2*(1-rho)))

    def test_weighted_accumulation_bound_uses_absolute_weights(self):
        rho = F(1, 2)
        jumps = (F(1, 4), F(-1, 3), F(1, 100))
        weights = (F(3, 2), F(-3), F(2))
        lower, upper, bound = F(0), F(0), F(0)
        for weight, r in zip(weights, jumps):
            lo, hi = log_error_interval(r)
            lower += weight*(lo if weight >= 0 else hi)
            upper += weight*(hi if weight >= 0 else lo)
            bound += abs(weight)*r*r/(2*(1-rho))
        self.assertLessEqual(max(abs(lower), abs(upper)), bound)

    def test_scalar_operator_rescaling_does_not_reduce_relative_error(self):
        r = F(1, 2)
        lo, hi = log_error_interval(r)
        for scale in (F(1), F(1, 10**8), F(1, 10**20)):
            self.assertEqual(scale*lo/(scale*r), lo/r)
            self.assertEqual(scale*hi/(scale*r), hi/r)
        # This is scale*backward_delta, NOT evaluation at a shorter argument step.

    def test_genuinely_smaller_relative_steps_improve_log_approximation(self):
        last_lower = None
        for r in (F(1, 2), F(1, 4), F(1, 8), F(1, 1000)):
            lo, hi = log_error_interval(r)
            relative_lo, relative_hi = lo/r, hi/r
            if last_lower is not None:
                self.assertLess(relative_hi, last_lower)
            last_lower = relative_lo

    def test_large_fibonacci_index_does_not_remove_one_step_gap(self):
        seq = fib_sequence(82)
        for n in (20, 40, 80):
            r = F(seq[n]-seq[n-1], seq[n])
            lo, hi = log_error_interval(r)
            self.assertGreater(lo, F(9, 100))
            self.assertLess(hi, F(11, 100))
            self.assertGreater(r, F(38, 100))
            self.assertLess(r, F(39, 100))

    def test_two_step_fibonacci_relative_sum_is_not_log_y(self):
        seq = fib_sequence(82)
        for z in (20, 40, 80):
            relative_sum = sum((F(seq[n]-seq[n-1], seq[n]) for n in (z, z+1)), F(0))
            lo, hi = log_interval(F(seq[z+1], seq[z-1]))
            self.assertGreater(lo-relative_sum, F(19, 100))
            self.assertLess(hi-relative_sum, F(21, 100))

    def test_four_potential_ratios_under_common_factor_assumption(self):
        # Conditional reconstruction from H004(98) and the chosen endpoints.
        # Common proportionality factor/radius and epsilon are held fixed.
        epsilon, common, alpha, eta11, eb = F(3, 2), F(7, 11), F(1, 137), F(8, 9), F(19, 7)
        for s in (F(1, 2), F(2, 3)):
            d = s*s
            eomega, erho, edelta = epsilon*(1+s)/2, epsilon*s, epsilon*(1-s)
            ve = common*epsilon**2
            vrho = common*erho**2
            valpha, vbeta = ve/2, alpha*common*eomega*epsilon/3
            self.assertEqual(vbeta/valpha, alpha*(1+s)/3)
            self.assertEqual(vrho/ve, d)
            va, vb = vrho, common*epsilon**2*eta11/eb
            self.assertEqual(vb/va, eta11/(eb*d))
            for k in (1, 2):
                wa = common*eomega**2
                wb = F(2)**(k-2)*common*edelta**2
                self.assertEqual(wb/wa, 2**k*((1-s)/(1+s))**2)


if __name__ == "__main__":
    unittest.main()

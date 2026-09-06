"""Conditional scalar checks of literal W4 rules, not a Heim-state solver.

Only synthetic rational inputs and certified elementary-function intervals.
No historical program, existing audit evaluator or particle data is imported.
"""

import unittest
from fractions import Fraction as F


def greedy_remainder(alpha3, w3):
    """The specified local maximum, not the full occupation algorithm."""
    alpha3, w3 = F(alpha3), F(w3)
    if alpha3 <= 0 or w3 < 0:
        raise ValueError("Require alpha3 > 0 and W3 >= 0")
    k3 = w3 // alpha3
    return k3, w3 - alpha3 * k3


def exponent_coefficient(k, q4):
    k, q4 = F(k), F(q4)
    if k < 1 or q4 <= 0:
        raise ValueError("Require k >= 1 and Q4 > 0")
    return (2 * k - 1) / (3 * q4)


def log_interval(value, terms=48):
    """ln(x) via 2*atanh((x-1)/(x+1)); exact geometric tail bound."""
    value = F(value)
    if value <= 0 or not isinstance(terms, int) or terms < 1:
        raise ValueError("Positive argument and positive integer term count")
    t = (value - 1) / (value + 1)
    total = 2 * sum((t ** (2 * j + 1) / (2 * j + 1)
                     for j in range(terms)), F(0))
    tail = 2 * abs(t) ** (2 * terms + 1) / (
        (2 * terms + 1) * (1 - t * t))
    return (total, total + tail) if t >= 0 else (total - tail, total)


def exp_interval(value, terms=48):
    """Taylor interval for exp(x>=0), reciprocal interval for x<0."""
    value = F(value)
    if not isinstance(terms, int) or terms < 1 or abs(value) >= terms + 2:
        raise ValueError("Positive term count with geometric tail ratio < 1")
    if value < 0:
        lower, upper = exp_interval(-value, terms)
        return 1 / upper, 1 / lower
    term = total = F(1)
    for index in range(1, terms + 1):
        term *= value / index
        total += term
    next_term = term * value / (terms + 1)
    tail = next_term / (1 - value / (terms + 2))
    return total, total + tail


def negative_log_interval(value, coefficient):
    coefficient = F(coefficient)
    if coefficient <= 0:
        raise ValueError("Positive exponent coefficient")
    lower, upper = log_interval(value)
    return -upper / coefficient, -lower / coefficient


def certified_floor(interval):
    lower, upper = interval
    if lower > upper or lower // 1 != upper // 1:
        raise ArithmeticError("The interval does not certify a unique floor")
    return lower // 1


class K4W4SelectionTests(unittest.TestCase):
    def test_greedy_maximum_has_half_open_remainder_interval(self):
        for alpha3 in (F(1, 4), F(1), F(3, 2), F(3)):
            for w3 in (F(0), F(1, 3), F(1), F(11, 2), F(8)):
                with self.subTest(alpha3=alpha3, w3=w3):
                    k3, remainder = greedy_remainder(alpha3, w3)
                    self.assertGreaterEqual(k3, 0)
                    self.assertGreaterEqual(remainder, 0)
                    self.assertLess(remainder, alpha3)
                    self.assertEqual(alpha3 * k3 + remainder, w3)
                    self.assertLess(w3 - alpha3 * (k3 + 1), 0)

    def test_case_c_requires_alpha3_above_one_but_is_reachable(self):
        for alpha3 in (F(1, 4), F(1, 2), F(1)):
            for w3 in (F(0), F(1, 3), F(1), F(11, 2), F(8)):
                self.assertLess(greedy_remainder(alpha3, w3)[1], 1)
        self.assertEqual(greedy_remainder(3, 8), (2, F(2)))

    def test_zero_case_finite_saturation_and_floor_leave_positive_error(self):
        coefficient = exponent_coefficient(1, 1)
        for alpha3, k3 in ((F(2), 1), (F(3, 2), 1), (F(1), 0)):
            w3 = alpha3 * k3
            self.assertEqual(greedy_remainder(alpha3, w3), (k3, F(0)))
            raw = alpha3 * k3
            integer = raw // 1
            self.assertLessEqual(integer, alpha3 * k3)
            for k4 in (raw, F(integer)):
                # With the same K3, equation error is precisely exp(-c*K4).
                self.assertGreater(exp_interval(-coefficient * k4)[0], 0)

    def test_zero_case_does_not_prove_no_other_k3_solution(self):
        # Own boundary witness: greedy gives (K3,W4)=(1,0), but (0,0)
        # solves the unmodified equation for alpha3=W3=1 via exp(0)=1.
        self.assertEqual(greedy_remainder(1, 1), (1, F(0)))
        other_k3 = other_k4 = 0
        self.assertEqual(F(other_k3) + exp_interval(0)[0], 1)
        self.assertLessEqual(other_k4, F(other_k3))

    def test_case_b_floor_has_exact_nonzero_error_despite_structure_cap(self):
        alpha3, w3, coefficient = F(1), F(11, 4), F(1, 3)
        k3, remainder = greedy_remainder(alpha3, w3)
        self.assertEqual((k3, remainder), (2, F(3, 4)))
        raw_interval = negative_log_interval(remainder, coefficient)
        self.assertGreater(raw_interval[0], 0)
        self.assertLess(raw_interval[1], 1)
        k4 = certified_floor(raw_interval)
        self.assertEqual(k4, 0)
        self.assertLessEqual(k4, alpha3 * k3)
        self.assertEqual(alpha3 * k3 + 1 - w3, F(1, 4))

    def test_case_b_global_and_floor_specific_error_bounds(self):
        for coefficient in (F(1, 3), F(1), F(2)):
            for remainder in (F(1, 4), F(1, 2), F(3, 4), F(1)):
                with self.subTest(c=coefficient, remainder=remainder):
                    k4 = certified_floor(negative_log_interval(remainder, coefficient))
                    exp_low, exp_high = exp_interval(-coefficient * k4)
                    error_low, error_high = exp_low - remainder, exp_high - remainder
                    one_step_exp_high = exp_interval(-coefficient)[1]
                    self.assertGreaterEqual(error_low, 0)
                    self.assertLess(error_high, 1 - one_step_exp_high)
                    self.assertLess(error_high, exp_low * (1 - one_step_exp_high))
                    relative_upper = exp_interval(coefficient)[0] - 1
                    self.assertLess(error_high / remainder, relative_upper)

    def test_exact_integer_exponent_identity_is_not_epsilon_promotion(self):
        # Analytic premise r=exp(-c*j), hence ln(r)=-c*j, is explicit.
        # This does not infer an identity from finitely many decimal nines.
        for coefficient in (F(1, 3), F(1), F(2)):
            for exact_integer in range(8):
                log_r = -coefficient * exact_integer
                raw = -log_r / coefficient
                self.assertEqual(raw, exact_integer)
                self.assertEqual(raw // 1, exact_integer)
        almost_one = F(10 ** 60 - 1, 10 ** 60)
        self.assertEqual(almost_one // 1, 0)
        self.assertNotEqual(almost_one, 1)

    def test_structure_cap_is_separate_from_equation_and_nonnegativity(self):
        k3, remainder = greedy_remainder(1, F(1, 2))
        raw_low, raw_high = negative_log_interval(remainder, 1)
        self.assertEqual(k3, 0)
        self.assertGreater(raw_low, 0)  # Reell K4 violates the additional cap 0.
        self.assertLess(raw_high, 1)
        k4 = certified_floor((raw_low, raw_high))
        self.assertEqual(k4, 0)        # Floored K4 satisfies the cap, not the equation.
        self.assertEqual(exp_interval(-k4)[0] - remainder, F(1, 2))

    def test_case_c_pre_post_can_change_nonnegative_acceptance(self):
        alpha3, before, remainder = F(3), 1, F(2)
        self.assertEqual(greedy_remainder(alpha3, 5), (before, remainder))
        raw_low, raw_high = negative_log_interval(remainder, 1)
        after = before - 1
        self.assertLess(raw_high + alpha3 * after, 0)
        self.assertGreater(raw_low + alpha3 * before, 0)
        self.assertEqual(certified_floor((raw_low + 3, raw_high + 3)), 2)

    def test_case_c_both_integer_variants_can_pass_cap_and_fail_equation(self):
        # Root's separately checked synthetic witness; no source-state claim.
        alpha3, before, remainder, coefficient = F(2), 2, F(3, 2), F(1, 3)
        w3 = alpha3 * before + remainder
        self.assertEqual(greedy_remainder(alpha3, w3), (before, remainder))
        raw_low, raw_high = negative_log_interval(remainder, coefficient)
        self.assertGreater(raw_low, -2)
        self.assertLess(raw_high, -1)
        after = before - 1
        for shifted_index, expected_k4 in ((after, 0), (before, 2)):
            k4 = certified_floor((raw_low + alpha3 * shifted_index,
                                  raw_high + alpha3 * shifted_index))
            self.assertEqual(k4, expected_k4)
            self.assertGreaterEqual(k4, 0)
            self.assertLessEqual(k4, alpha3 * after)
            residual_upper = alpha3 * after + exp_interval(-coefficient * k4)[1] - w3
            self.assertLess(residual_upper, 0)
            if k4 == 0:
                self.assertEqual(residual_upper, F(-5, 2))

    def test_case_c_no_nonnegative_exponential_can_fill_any_integer_remainder(self):
        # Finite witnesses of the general proof in the independent review.
        for alpha3, before, remainder in ((F(3), 2, F(2)),
                                          (F(2), 2, F(3, 2)),
                                          (F(3), 0, F(2))):
            w3 = alpha3 * before + remainder
            self.assertEqual(greedy_remainder(alpha3, w3), (before, remainder))
            for candidate in range(before + 5):
                required_exp = w3 - alpha3 * candidate
                if candidate <= before:
                    self.assertGreater(required_exp, 1)
                else:
                    self.assertLess(required_exp, 0)
                # Neither interval intersects exp(-c*K4) in (0,1] for K4>=0.

    def test_case_c_recomputed_remainder_would_still_require_negative_k4(self):
        alpha3, before, remainder = F(3), 2, F(2)
        w3, after = alpha3 * before + remainder, before - 1
        recomputed = w3 - alpha3 * after
        self.assertEqual(recomputed, remainder + alpha3)
        self.assertGreater(recomputed, 1)
        self.assertLess(negative_log_interval(recomputed, F(1, 3))[1], 0)

    def test_synthetic_cases_can_pass_earlier_greedy_and_named_inequalities(self):
        # Independent alpha_i inputs, not a common Heim coefficient profile.
        # Checking XIII/XXXII inequalities does not validate boundary dynamics.
        alpha1, alpha2, alpha3 = F(1), F(2), F(2)
        k1, k2 = 3, 2
        for w3, greedy_k3, output_k4s in ((F(2), 1, (2,)),
                                          (F(11, 2), 2, (0, 2))):
            w2 = alpha2 * k2 ** 2 + w3
            w1 = alpha1 * k1 ** 3 + w2
            self.assertLessEqual(alpha1 * k1 ** 3, w1)
            self.assertLess(w1, alpha1 * (k1 + 1) ** 3)
            self.assertLessEqual(alpha2 * k2 ** 2, w2)
            self.assertLess(w2, alpha2 * (k2 + 1) ** 2)
            self.assertEqual(greedy_remainder(alpha3, w3)[0], greedy_k3)
            self.assertLessEqual(alpha3 * greedy_k3 * (1 + greedy_k3),
                                 2 * alpha2 * k2 ** 2)
            after_k3 = 1
            for k4 in output_k4s:
                self.assertLessEqual(k4, alpha3 * after_k3)
                self.assertLessEqual(alpha3 * after_k3, alpha2 * k2 ** 2)
                self.assertLessEqual(alpha2 * k2 ** 2, alpha3 * k1 ** 3)
                self.assertLessEqual(alpha3 * after_k3 * (1 + after_k3),
                                     2 * alpha2 * k2 ** 2)
                self.assertLessEqual(alpha2 * k2 * (2 * k2 ** 2 + 3 * k2 + 1),
                                     6 * alpha1 * k1 ** 3)

    def test_auxiliary_certificate_domains_and_ambiguous_floor(self):
        for arguments in ((0, 1), (-1, 1), (1, -1)):
            with self.assertRaises(ValueError):
                greedy_remainder(*arguments)
        for arguments in ((F(1, 2), 1), (1, 0), (1, -1)):
            with self.assertRaises(ValueError):
                exponent_coefficient(*arguments)
        self.assertGreater(exponent_coefficient(F(3, 2), 2), 0)
        with self.assertRaises(ValueError):
            log_interval(0)
        with self.assertRaises(ValueError):
            log_interval(1, 0)
        with self.assertRaises(ValueError):
            exp_interval(4, 2)
        with self.assertRaises(ValueError):
            negative_log_interval(1, 0)
        with self.assertRaises(ArithmeticError):
            certified_floor((F(9, 10), F(11, 10)))


if __name__ == '__main__':
    unittest.main()

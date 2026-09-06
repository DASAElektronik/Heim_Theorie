"""Synthetic diagnostics of the book's selection rules, not a mass solver.

Ordinary nonnegative TRC is tested as floor, with no invented 99-promotion
tolerance. Reuse exact rational log/exp certificates from the stage-25 tests.
Source alpha profiles, Y9, masses and old snapshots are never modified.
"""

from fractions import Fraction as F
import unittest

from test_k4_w4_selection import (
    certified_floor, exp_interval, negative_log_interval,
)


def greedy_power(total, coefficient, power):
    """Maximum nonnegative integer, using exact rational comparisons."""
    total, coefficient = F(total), F(coefficient)
    if total < 0 or coefficient <= 0 or power not in (1, 2, 3):
        raise ValueError("require total>=0, coefficient>0, power in 1..3")
    number = 0
    while coefficient * (number + 1)**power <= total:
        number += 1
    return number, total - coefficient * number**power


def first_three(total, coefficients):
    numbers = []
    for coefficient, power in zip(coefficients, (3, 2, 1), strict=True):
        number, total = greedy_power(total, coefficient, power)
        numbers.append(number)
    return tuple(numbers), total


def transfer_addition(alpha3, before_n3, steps):
    """Declared cumulative reading: h successive additions a*m,...,a*(m-h+1).

    This arithmetic helper does not assert a physically valid full transfer.
    """
    if alpha3 <= 0 or before_n3 < 0 or not 0 <= steps <= before_n3:
        raise ValueError("positive alpha3, 0<=steps<=before_n3 required")
    return F(alpha3) * (steps * before_n3 - F(steps * (steps - 1), 2))


class BookSelectionTests(unittest.TestCase):
    def test_successive_maxima_have_explicit_cells(self):
        for total in (F(0), F(151, 4), F(189, 5), F(159, 2)):
            numbers, residual = first_three(total, (F(1), F(2), F(1)))
            current = total
            for number, coefficient, power in zip(numbers, (1, 2, 1), (3, 2, 1)):
                self.assertLessEqual(coefficient * number**power, current)
                self.assertLess(current, coefficient * (number + 1)**power)
                current -= coefficient * number**power
            self.assertEqual(current, residual)
            self.assertGreaterEqual(residual, 0)
            self.assertLess(residual, 1)

    def test_two_distinct_inputs_have_same_integer_output(self):
        # Synthetic alpha=(1,2,1), lambda=1/3; no source particle inputs.
        results = []
        for total in (F(151, 4), F(189, 5)):
            first, residual = first_three(total, (F(1), F(2), F(1)))
            self.assertEqual(first, (3, 2, 2))
            raw = negative_log_interval(residual, F(1, 3))
            self.assertGreater(raw[0], 0)
            self.assertLess(raw[1], 1)
            final = certified_floor(raw)
            self.assertEqual(final, 0)
            self.assertGreaterEqual(F(first[2]) - final, 1)  # beta4 only.
            results.append(first + (final,))
        self.assertEqual(results[0], results[1])

    def test_affine_inverse_does_not_restore_lost_integer_information(self):
        # Toy W1=g*(1+d*A), with fixed g=2,d=1/2,f=0.
        a_values = []
        for total in (F(151, 4), F(189, 5)):
            a_value = (total / 2 - 1) / F(1, 2)
            self.assertEqual(2 * (1 + F(1, 2) * a_value), total)
            a_values.append(a_value)
        self.assertNotEqual(*a_values)

    def test_normal_branch_exact_remainders_are_not_zero(self):
        for residual, expected in ((F(3, 4), F(1, 4)), (F(4, 5), F(1, 5))):
            n4 = certified_floor(negative_log_interval(residual, F(1, 3)))
            self.assertEqual(exp_interval(-F(n4, 3)), (F(1), F(1)))
            self.assertEqual(1 - residual, expected)

    def test_finite_zero_rest_saturation_is_not_exact_solution(self):
        alpha3, n3, coefficient = F(2), 1, F(1, 15)
        cap = alpha3 * n3
        n4 = cap // 1
        self.assertEqual(n4, 2)
        self.assertGreater(exp_interval(-coefficient * n4)[0], 0)

    def test_ordinary_cap_correction_does_not_trigger_at_equality(self):
        # Conditional boundary audit, NOT proof of a reachable Heim state.
        cap = F(2)
        truncated = cap // 1
        self.assertFalse(truncated > cap)
        self.assertEqual(cap - truncated, 0)
        # It satisfies <=cap but not the active-zone beta4>=1 condition.
        self.assertLess(cap - truncated, 1)

    def test_decreasing_transfer_sum_matches_repeated_additions(self):
        for before in range(1, 7):
            for steps in range(before + 1):
                explicit = sum((F(3, 2) * (before - index)
                                for index in range(steps)), F(0))
                self.assertEqual(transfer_addition(F(3, 2), before, steps), explicit)

    def test_one_transfer_can_pass_cap_and_leave_negative_equation_error(self):
        alpha3, before, residual, coefficient = F(2), 4, F(3, 2), F(1, 15)
        low, high = negative_log_interval(residual, coefficient)
        shift = transfer_addition(alpha3, before, 1)
        raw = low + shift, high + shift
        after = before - 1
        self.assertGreater(raw[0], 1)
        self.assertLess(raw[1], 2)
        self.assertLess(raw[1], alpha3 * after)
        n4 = certified_floor(raw)
        self.assertEqual(n4, 1)
        self.assertGreaterEqual(alpha3 * after - n4, 1)
        error_low, error_high = exp_interval(-coefficient * n4)
        self.assertLess(error_high - residual - alpha3, 0)
        self.assertLess(error_low - residual - alpha3, error_high - residual - alpha3)

    def test_nonnegative_transfer_value_alone_does_not_pass_raw_cap(self):
        alpha3, before, residual = F(2), 4, F(21, 20)
        low, high = negative_log_interval(residual, F(1, 15))
        shift = transfer_addition(alpha3, before, 1)
        self.assertGreater(low + shift, alpha3 * (before - 1))
        self.assertGreater(low + shift, 0)

    def test_two_steps_are_not_automatically_structurally_allowed(self):
        alpha3, before = F(2), 3
        low, high = negative_log_interval(F(3, 2), F(1, 15))
        self.assertLess(high + transfer_addition(alpha3, before, 1), 0)
        shift = transfer_addition(alpha3, before, 2)
        self.assertGreater(low + shift, 0)
        self.assertGreater(low + shift, alpha3 * (before - 2))

    def test_exhausting_n3_can_fail_to_make_transfer_nonnegative(self):
        alpha3, before = F(2), 2
        _, high = negative_log_interval(F(3, 2), F(1, 15))
        self.assertLess(high + transfer_addition(alpha3, before, before), 0)

    def test_transfer_error_identity_for_synthetic_pairs(self):
        # exp term represented by a rational 0<t<=1; no invented log solution.
        alpha3, before, residual = F(2), 4, F(3, 2)
        w3 = alpha3 * before + residual
        for steps in (1, 2, 3, 4):
            for term in (F(1), F(1, 2), F(1, 100)):
                error = alpha3 * (before - steps) + term - w3
                self.assertEqual(error, term - residual - alpha3 * steps)
                self.assertLess(error, 0)

    def test_explicit_domains(self):
        for args in ((-1, 1, 3), (1, 0, 2), (1, 1, 0)):
            with self.assertRaises(ValueError):
                greedy_power(*args)
        for args in ((0, 2, 1), (1, -1, 0), (1, 2, 3)):
            with self.assertRaises(ValueError):
                transfer_addition(*args)


if __name__ == "__main__":
    unittest.main()

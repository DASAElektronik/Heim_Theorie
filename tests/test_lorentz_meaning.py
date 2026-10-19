"""Exact examples independent of source intent and of measured constants."""

import sys
import unittest
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"scripts"))
import audit_lorentz_meaning as lorentz


class LorentzMeaningTests(unittest.TestCase):
    def test_exact_gamma_domain(self):
        self.assertEqual(lorentz.gamma_exact(F(3, 5)), F(5, 4))
        self.assertEqual(lorentz.gamma_exact(F(0)), F(1))
        for invalid in (F(-1), F(1), F(2), F(1, 2)):
            with self.subTest(b=invalid), self.assertRaises(ValueError):
                lorentz.gamma_exact(invalid)
        with self.assertRaises(TypeError):
            lorentz.gamma_exact(0.6)

    def test_two_exact_momentum_cases(self):
        self.assertEqual(lorentz.transform_pair(F(1), F(0), F(3, 5)), (F(5, 4), F(-3, 4)))
        self.assertEqual(lorentz.transform_pair(F(5, 4), F(3, 4), F(3, 5)), (F(1), F(0)))

    def test_mass_shell_and_inverse_general_examples(self):
        for b in (F(0), F(3, 5), F(-3, 5), F(5, 13), F(-8, 17)):
            for epsilon, q in ((F(1), F(0)), (F(5, 4), F(3, 4)), (F(13, 12), F(-5, 12))):
                e_new, q_new = lorentz.transform_pair(epsilon, q, b)
                self.assertEqual(e_new*e_new-q_new*q_new, 1)
                self.assertEqual(lorentz.transform_pair(e_new, q_new, -b), (epsilon, q))

    def test_metric_matrix_identity(self):
        for b in (F(0), F(3, 5), F(-5, 13)):
            matrix = lorentz.boost_matrix(b)
            actual = lorentz.multiply(lorentz.multiply(lorentz.transpose(matrix), lorentz.METRIC), matrix)
            self.assertEqual(actual, lorentz.METRIC)

    def test_energy_values_not_scalar_invariants(self):
        before = lorentz.momentum_summary(F(1), F(0))
        after = lorentz.momentum_summary(F(5, 4), F(-3, 4))
        self.assertEqual(after["pc_magnitude_over_m0c2"], F(3, 4))
        self.assertEqual(after["T_over_m0c2"], F(1, 4))
        self.assertNotEqual(before["pc_magnitude_over_m0c2"], after["pc_magnitude_over_m0c2"])
        self.assertNotEqual(before["T_over_m0c2"], after["T_over_m0c2"])
        for invalid in ((F(-1), F(0)), (F(2), F(0))):
            with self.assertRaises(ValueError):
                lorentz.momentum_summary(*invalid)

    def test_circle_simultaneity_and_ellipse(self):
        for x, y in ((F(1), F(0)), (F(0), F(1)), (F(3, 5), F(4, 5))):
            row = lorentz.static_circle_event(x, y, F(3, 5))
            self.assertEqual(row["ct_prime"], 0)
            self.assertEqual(row["x_prime"], F(4, 5)*x)
            self.assertEqual(row["y_prime"], y)
            self.assertEqual((row["x_prime"]/F(4, 5))**2+row["y_prime"]**2, 1)
        with self.assertRaises(ValueError):
            lorentz.static_circle_event(F(1), F(1), F(3, 5))

    def test_simultaneous_events_must_be_selected_in_target_frame(self):
        ct_prime, x_prime = lorentz.transform_pair(F(0), F(1), F(3, 5))
        self.assertEqual(ct_prime, F(-3, 4))
        self.assertEqual(x_prime, F(5, 4))
        self.assertNotEqual(ct_prime, 0)  # Not the target-frame shape section.

    def test_perimeter_bounds_exclude_uniform_contraction(self):
        bounds = lorentz.perimeter_bounds(F(3, 5))
        self.assertEqual(bounds["actual_perimeter_ratio_lower"], F(9, 10))
        self.assertEqual(bounds["actual_perimeter_ratio_upper_squared"], F(41, 50))
        self.assertLess(bounds["uniform_contraction_hypothesis"], bounds["actual_perimeter_ratio_lower"])
        self.assertLess(bounds["actual_perimeter_ratio_lower"]**2, bounds["actual_perimeter_ratio_upper_squared"])
        self.assertTrue(bounds["bounds_strict"])

    def test_zero_boost_geometry(self):
        bounds = lorentz.perimeter_bounds(F(0))
        self.assertEqual(bounds["actual_perimeter_ratio_lower"], 1)
        self.assertEqual(bounds["actual_perimeter_ratio_upper_squared"], 1)
        self.assertFalse(bounds["bounds_strict"])

    def test_literal_source_matrix_not_orthogonal(self):
        literal = lorentz.source_literal_block(F(3, 5))
        self.assertEqual(literal, ((F(5, 4), F(-3, 4)), (F(3, 4), F(5, 4))))
        self.assertEqual(lorentz.multiply(literal, lorentz.transpose(literal)),
                         ((F(17, 8), F(0)), (F(0), F(17, 8))))
        self.assertNotEqual(literal, lorentz.boost_matrix(F(3, 5)))
        self.assertEqual(lorentz.source_literal_block(F(0)), lorentz.IDENTITY)

    def test_literal_factor_with_both_signs(self):
        for b in (F(3, 5), F(-3, 5), F(5, 13)):
            matrix = lorentz.source_literal_block(b)
            factor = (1+b*b)/(1-b*b)
            product = lorentz.multiply(matrix, lorentz.transpose(matrix))
            self.assertEqual(product, ((factor, F(0)), (F(0), factor)))

    def test_report_separates_profiles_and_no_fit(self):
        r = lorentz.build_report()
        self.assertFalse(r["target_fitting"])
        self.assertEqual(r["modern_reference_inputs"], [])
        self.assertTrue(r["standard_reference"]["preserves_metric"])
        self.assertFalse(r["book_p21_literal"]["is_orthogonal_under_stated_reading"])
        self.assertEqual(r["book_p21_literal"]["full_four_by_four_diagonal"], ["17/8", "1", "1", "17/8"])


if __name__ == "__main__":
    unittest.main()

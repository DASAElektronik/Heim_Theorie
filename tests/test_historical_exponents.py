"""Exact algebra of two explicitly separated source readings, not Heim validity.

No old calculator or historical program is imported.  Test occupations satisfy
only the declared local domain; physical admissibility is not asserted.
"""

import unittest
from fractions import Fraction as F


def literal_exponents(k, q4, n4):
    """A has an external 1; B multiplies the entire (1-2*k) bracket."""
    q4, n4 = F(q4), F(n4)
    if type(k) is not int or k not in (1, 2) or q4 <= 0 or n4 + q4 < 0:
        raise ValueError('Require k=1 or 2, Q4>0 and n4+Q4>=0')
    a = 1 - F(2*k)*(n4+q4)/(3*q4)
    b = F(1-2*k)*(n4+q4)/(3*q4)
    return a, b


class HistoricalExponentTests(unittest.TestCase):
    def test_exact_gap_is_independent_of_k(self):
        for q4 in (F(1), F(3, 2), F(15)):
            for n4 in (-q4, F(0), q4, 2*q4, 3*q4):
                for k in (1, 2):
                    a, b = literal_exponents(k, q4, n4)
                    self.assertEqual(a-b, (2*q4-n4)/(3*q4))

    def test_equality_occurs_only_at_the_special_local_occupation(self):
        for k in (1, 2):
            for q4 in (1, 3, 15):
                for n4 in range(-q4, 3*q4+1):
                    a, b = literal_exponents(k, q4, n4)
                    self.assertEqual(a == b, n4 == 2*q4)
                    if a == b:
                        self.assertEqual(a, 1-2*k)

    def test_declared_n0_point_discriminates_the_readings(self):
        a, b = literal_exponents(1, 1, 0)
        self.assertEqual((a, b), (F(1, 3), F(-1, 3)))
        self.assertEqual(a-b, F(2, 3))

    def test_neighbours_of_an_agreement_point_disprove_formula_identity(self):
        for k in (1, 2):
            for q4 in (1, 3, 15):
                self.assertEqual(literal_exponents(k, q4, 2*q4), (1-2*k, 1-2*k))
                for offset in (-1, 1):
                    a, b = literal_exponents(k, q4, 2*q4+offset)
                    self.assertEqual(a-b, F(-offset, 3*q4))
                    self.assertNotEqual(a, b)

    def test_negative_occupation_at_zero_shifted_index_is_allowed(self):
        for k in (1, 2):
            for q4 in (1, 3, 15):
                self.assertEqual(literal_exponents(k, q4, -q4), (1, 0))

    def test_source_log_inverse_matches_only_b_as_a_formula(self):
        # Substitute ln(exp(E))=E symbolically; no numerical exponential.
        # This checks the displayed relation, not a piecewise algorithm run.
        for k in (1, 2):
            for q4 in (F(1), F(3, 2), F(15)):
                for multiple in (0, 1, 2, 3, 4):
                    shifted_k4 = multiple*q4
                    a, b = literal_exponents(k, q4, shifted_k4-q4)
                    inverse_a = -3*q4*a/(2*k-1)
                    inverse_b = -3*q4*b/(2*k-1)
                    self.assertEqual(inverse_b, shifted_k4)
                    self.assertEqual(inverse_a-shifted_k4, (shifted_k4-3*q4)/(2*k-1))
                    self.assertEqual(3*q4*(1-a)/(2*k), shifted_k4)
        a, b = literal_exponents(1, 1, 0)
        self.assertEqual((-3*a, -3*b), (-1, 1))

    def test_only_the_declared_local_domain_is_supported(self):
        for args in ((0, 1, 0), (3, 1, 0), (True, 1, 0),
                     (1, 0, 0), (1, -1, 1), (2, 3, -4)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                literal_exponents(*args)


if __name__ == '__main__':
    unittest.main()

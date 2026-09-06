"""Exact conditional A16 identities, not a mass fit or metronic derivation."""

import unittest
from fractions import Fraction as F
from itertools import product


def forms(p, eb, alpha, eta):
    """Rational stand-ins test algebra; they are not complete Heim profiles."""
    base = (p*eb)**2
    correction = alpha*(1+6*alpha/p)/5
    return base, base*(1+correction/eta), base*(1+correction*eta)


def exp_negative_bounds(x, terms=24):
    x = F(x)
    if type(terms) is not int or terms < 1 or not 0 <= x < terms+2:
        raise ValueError("Nonnegative exponent magnitude and bounded Taylor tail")
    term = total = F(1)
    for j in range(1, terms+1):
        term *= x/j
        total += term
    upper = total+term*x/(terms+1)/(1-x/(terms+2))
    return 1/upper, 1/total


class A16OriginTests(unittest.TestCase):
    def test_expansion_separates_basis_linear_and_quadratic_parts(self):
        for p, eb, alpha, eta in product((F(3), F(22, 7)), (F(2), F(11, 4)),
                                          (F(0), F(1, 100), F(1, 10)), (F(1, 2), F(99, 100))):
            base, P, L = forms(p, eb, alpha, eta)
            linear = p**2*eb**2*alpha/5
            quadratic = 6*p*eb**2*alpha**2/5
            self.assertEqual(P, base+linear/eta+quadratic/eta)
            self.assertEqual(L, base+linear*eta+quadratic*eta)

    def test_difference_and_positive_ordering_need_positive_alpha(self):
        p, eb, eta = F(3), F(2), F(4, 5)
        for alpha in (F(1, 100), F(1, 10), F(1)):
            base, P, L = forms(p, eb, alpha, eta)
            expected = p*eb**2*alpha*(p+6*alpha)*(1-eta**2)/(5*eta)
            self.assertEqual(P-L, expected)
            self.assertGreater(P, L)
            self.assertGreater(L, base)
        _, P, L = forms(p, eb, F(-1, 4), eta)
        self.assertLess(P, L)  # eta<1 alone does not prove the sign.

    def test_coincidences_do_not_make_eta_one_a_finite_pi_solution(self):
        for p in (F(1, 10), F(3), F(22, 7), F(1000)):
            eta4 = p**4/(p**4+4)
            self.assertGreater(eta4, 0)
            self.assertLess(eta4, 1)
        for alpha, eta in ((F(0), F(4, 5)), (F(1, 10), F(1))):
            _, P, L = forms(F(3), F(2), alpha, eta)
            self.assertEqual(P, L)

    def test_eta_ratio_applies_to_corrections_not_whole_coefficients(self):
        for eta in (F(1, 2), F(4, 5), F(99, 100)):
            base, P, L = forms(F(3), F(2), F(1, 100), eta)
            self.assertEqual((P-base)/(L-base), 1/eta**2)
            self.assertNotEqual(P/L, 1/eta**2)

    def test_w_difference_requires_same_g_d_and_same_greedy_subtraction(self):
        _, P, L = forms(F(3), F(2), F(1, 100), F(99, 100))
        for g, d, subtraction in product((F(1), F(7)), (F(3, 4), F(1)), (F(0), F(19, 7))):
            WP, WL = g*(1+d*P), g*(1+d*L)
            self.assertEqual(WP-WL, g*d*(P-L))
            self.assertEqual((WP-subtraction)-(WL-subtraction), g*d*(P-L))
            self.assertNotEqual((WP-subtraction-1)-(WL-subtraction), g*d*(P-L))

    def test_exact_floor_intervals_in_exponent_coordinate(self):
        # r=exp(-x/3) decreases strictly: j<=x<j+1 becomes
        # exp(-(j+1)/3)<r<=exp(-j/3). Equality belongs to the upper r end.
        for x, floor in ((F(0), 0), (F(3, 4), 0), (F(1), 1),
                          (F(11, 10), 1), (F(2), 2)):
            self.assertEqual(x//1, floor)
            self.assertLess(-(floor+1)/F(3), -x/3)
            self.assertLessEqual(-x/3, -F(floor)/3)

    def test_exp_thresholds_have_rational_enclosures(self):
        lo1, hi1 = exp_negative_bounds(F(1, 3))
        lo2, hi2 = exp_negative_bounds(F(2, 3))
        self.assertLess(F("0.7165"), lo1)
        self.assertLess(hi1, F("0.7166"))
        self.assertLess(F("0.5134"), lo2)
        self.assertLess(hi2, F("0.5135"))
        self.assertLess(hi2, lo1)
        self.assertEqual(exp_negative_bounds(0), (F(1), F(1)))
        for x, terms in ((-1, 24), (1, 0), (1, True), (26, 24)):
            with self.assertRaises(ValueError):
                exp_negative_bounds(x, terms)

    def test_previously_quoted_remainders_cross_threshold_not_full_interval_audit(self):
        lo1, hi1 = exp_negative_bounds(F(1, 3))
        _, hi2 = exp_negative_bounds(F(2, 3))
        pairs = (
            (".7755039220886995", ".6927848240193449"),
            (".7755120560046683", ".6927929576918099"),
            (".7755039502393991", ".6927848521692018"),
            (".7755120841553648", ".6927929858416636"),
            (".7755069136887019", ".6927878155092382"),
            (".7755150476046777", ".6927959491817101"),
        )
        for P, L in pairs:
            self.assertLess(hi1, F(P))
            self.assertLess(F(P), 1)
            self.assertLess(hi2, F(L))
            self.assertLess(F(L), lo1)
        # These are quoted decimal rationals, not certified source-input bounds.

    def test_book_y9_multiplies_entire_a16_not_only_correction(self):
        base, P, _ = forms(F(3), F(2), F(1, 100), F(99, 100))
        for y in (F(1, 2), F(1), F(3, 2)):
            book = y*P
            self.assertEqual(book, y*base+y*(P-base))
            self.assertEqual(book-P, (y-1)*P)
            if y != 1:
                self.assertNotEqual(book, base+y*(P-base))
        self.assertEqual(F(1)*P, P)  # Local formula only, no edition-wide equivalence.

    def test_book_y9_w_is_affine_only_under_frozen_other_inputs(self):
        _, P, _ = forms(F(3), F(2), F(1, 100), F(99, 100))
        for g, d, y in product((F(1), F(7)), (F(3, 4), F(1)), (F(1, 2), F(1), F(3, 2))):
            WY, W1 = g*(1+d*y*P), g*(1+d*P)
            self.assertEqual(WY-W1, g*d*P*(y-1))
            self.assertEqual(WY-y*W1, g*(1-y))
        # No Y9 is estimated or selected from a particle mass or K4 target.


if __name__ == "__main__":
    unittest.main()

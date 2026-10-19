"""Local determinacy witnesses for H004 pp272-275, not new particle models.

The source's integrated log ansatz is assumed.  Helpers evaluate its
monomials for integer A1,A3,B1,B3,B4 and integer twice-A2/twice-B2, with
Y=xi**2 and positive rational xi.  All numeric inputs are synthetic.
The s=1 evaluations are continuous extensions, never evaluations of ln(0).
Neither metronic integration nor a full physical admissibility test is
implemented.  All previous calculators and their snapshots stay untouched.
"""

import unittest
from fractions import Fraction as F


def h_term(s, xi, alpha, a1, twice_a2, a3):
    d = s*s
    return (alpha*(1+s)/3)**a1 * xi**twice_a2 * d**a3


def g_term(s, xi, eta11, eb, k, b1, twice_b2, b3, b4):
    d = s*s
    ratio = (1-s)/(1+s)
    return ((eta11/(eb*d))**b1 * xi**twice_b2 * d**b3
            * (2**k * ratio**2)**b4)


class Alpha3AssumptionsTests(unittest.TestCase):
    def test_a3_shift_changes_h_without_changing_the_ansatz(self):
        for k in (1, 2):
            for s in (F(1, 2), F(2, 3), F(4, 5)):
                h = h_term(s, F(7, 5), F(1, 137), 1, 2*k+1, 1-4*k)
                shifted = h_term(s, F(7, 5), F(1, 137), 1, 2*k+1, 2-4*k)
                self.assertEqual(shifted/h, s*s)
                self.assertGreater(shifted, 0)
                self.assertLess(shifted, h)

    def test_b3_shift_changes_g_without_changing_the_ansatz(self):
        for k in (1, 2):
            for s in (F(1, 2), F(2, 3), F(4, 5)):
                g = g_term(s, F(7, 5), F(8, 9), F(19, 7), k, 1, k, k, 1)
                shifted = g_term(s, F(7, 5), F(8, 9), F(19, 7), k, 1, k, k+1, 1)
                self.assertEqual(shifted/g, s*s)
                self.assertGreater(shifted, 0)
                self.assertLess(shifted, g)

    def test_h_boundary_extension_does_not_select_a3(self):
        for k in (1, 2):
            xi, alpha = F(7, 5), F(1, 137)
            expected = 2*alpha/3 * xi**(2*k+1)
            for shift in (-2, 0, 1, 3):
                self.assertEqual(h_term(F(1), xi, alpha, 1, 2*k+1, 1-4*k+shift), expected)

    def test_g_boundary_extension_does_not_select_b3_or_positive_b4(self):
        for k in (1, 2):
            for shift in (-2, 0, 1, 3):
                for b4 in (1, 2, 3):
                    self.assertEqual(g_term(F(1), F(7, 5), F(8, 9), F(19, 7),
                                            k, 1, k, k+shift, b4), 0)

    def test_quadratic_zero_cofactor_is_unchanged_by_b3_shift(self):
        # For B1=B4=1, G/(d-1)^2 = eta11/e * xi^k * 2^k
        #                               * d^(B3-1)/(1+s)^4.
        for k in (1, 2):
            xi, eta11, eb = F(7, 5), F(8, 9), F(19, 7)
            for shift in (-2, 0, 1, 3):
                for s in (F(1, 2), F(2, 3)):
                    d = s*s
                    cofactor = eta11/eb * xi**k * 2**k * d**(k+shift-1)/(1+s)**4
                    g = g_term(s, xi, eta11, eb, k, 1, k, k+shift, 1)
                    self.assertEqual(g/(d-1)**2, cofactor)
                s, d = F(1), F(1)
                limit_cofactor = eta11/eb * xi**k * 2**k * d**(k+shift-1)/(1+s)**4
                self.assertEqual(limit_cofactor, eta11/eb*(2*xi)**k/16)

    def test_added_linearity_requirements_do_not_select_a3_or_b3(self):
        for k in (1, 2):
            for shift in (0, 1):
                s, xi, alpha, eta11, eb = F(2, 3), F(7, 5), F(1, 137), F(8, 9), F(19, 7)
                h = h_term(s, xi, alpha, 1, 2*k+1, 1-4*k+shift)
                self.assertEqual(h_term(s, xi, 2*alpha, 1, 2*k+1, 1-4*k+shift), 2*h)
                g = g_term(s, xi, eta11, eb, k, 1, k, k+shift, 1)
                self.assertEqual(g_term(s, xi, 2*eta11, eb, k, 1, k, k+shift, 1), 2*g)

    def test_charge_free_prefactor_is_not_a_coefficient_condition(self):
        # q=0 cancels the entire correction; f is just a fixed synthetic value.
        # d is held fixed: no physical q=0 -> eta(q,k)=1 limit is asserted.
        f, q = F(13, 7), 0
        for k in (1, 2):
            for shift in (0, 1):
                h = h_term(F(2, 3), F(7, 5), F(1, 137), 1, 2*k+1, 1-4*k+shift)
                g = g_term(F(2, 3), F(7, 5), F(8, 9), F(19, 7), k, 1, k, k+shift, 1)
                self.assertEqual(f-q*(h+g), f)

    def test_nonzero_charge_sees_the_perturbation(self):
        # Formal q changes at fixed synthetic d, not a source eta(q,k) path.
        s, f = F(2, 3), F(13, 7)
        for k in (1, 2):
            h = h_term(s, F(7, 5), F(1, 137), 1, 2*k+1, 1-4*k)
            g = g_term(s, F(7, 5), F(8, 9), F(19, 7), k, 1, k, k, 1)
            for q in (1, 2):
                old = f-q*(h+g)
                shifted = f-q*s*s*(h+g)
                self.assertEqual(shifted-old, q*(1-s*s)*(h+g))
                self.assertGreater(shifted, old)

    def test_one_synthetic_h_anchor_does_not_determine_a2_and_a3(self):
        # k=1, xi=2, alpha=1/2, d0=1/4.  A1 stays 1.
        # A2->A2+t, A3->A3+t multiplies H by (Y*d)^t, equal to 1 here.
        xi, alpha, s0, s1 = F(2), F(1, 2), F(1, 2), F(2, 3)
        for t in (-1, 0, 1, 2):
            self.assertEqual(h_term(s0, xi, alpha, 1, 3+2*t, -3+t), F(128))
        self.assertEqual(h_term(s1, xi, alpha, 1, 3, -3), F(405, 16))
        self.assertEqual(h_term(s1, xi, alpha, 1, 5, -2), F(45))

    def test_two_independent_synthetic_constraints_can_remove_that_freedom(self):
        # Fix A1, Y=4 and compare d0=1/4 with d1=1/16.
        # Null equations have log(4) times matrix [[1,-1],[1,-2]].
        # Its determinant is -1, so both exponent shifts must vanish.
        matrix = ((F(1), F(-1)), (F(1), F(-2)))
        determinant = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        self.assertEqual(determinant, -1)
        self.assertNotEqual(determinant, 0)

    def test_sigma_connection_determines_ck_conditionally(self):
        # H004 p274: (2*Ck)^(k+1)=(1+Qsigma)/2, Qsigma=2^(s-1)-1,
        # s=k^2+1.  The positive solution is Ck=2^(k-2).
        # The connection equation is assumed, not derived from zone geometry.
        for k in (1, 2):
            s = k*k+1
            qsigma = F(2)**(s-1)-1
            ck = F(2)**(k-2)
            self.assertEqual((2*ck)**(k+1), (1+qsigma)/2)
            self.assertGreater(ck, 0)


if __name__ == "__main__":
    unittest.main()

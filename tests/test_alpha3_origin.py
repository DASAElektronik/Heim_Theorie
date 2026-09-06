"""Elementary algebra after H004 pp274-275; not a metronic integration test.

All rational values below are synthetic witnesses, not particle constants.
Xi>0 and d=s**2>0 supply the positive logarithm/root domain. The source's
empirically chosen A_i/B_i are assumed, never inferred from these checks.
"""

import unittest
from fractions import Fraction as F


class Alpha3OriginTests(unittest.TestCase):
    def test_h_factorization_from_chosen_exponents(self):
        for k in (1, 2):
            for s in (F(2, 3), F(3, 4)):
                for xi in (F(7, 5), F(9, 4)):
                    d, alpha = s*s, F(1, 137)
                    # Y**A2=xi**(2*k+1); A1=1, A3=1-4*k.
                    from_logs = xi**(2*k+1)*(alpha*(1+s)/3)*d**(1-4*k)
                    collected = alpha/3*(1+s)*(xi/d**2)**(2*k+1)*d**3
                    self.assertEqual(from_logs, collected)

    def test_g_factorization_from_chosen_exponents(self):
        for k in (1, 2):
            for s in (F(2, 3), F(3, 4)):
                d, xi, eta11, eb = s*s, F(7, 5), F(8, 9), F(19, 7)
                ratio2 = ((1-s)/(1+s))**2
                # Y**B2=xi**k; B1=B4=1, B3=k.
                from_logs = xi**k*(eta11/(eb*d))*d**k*(2**k*ratio2)
                collected = eta11/(eb*d)*(2*xi*d)**k*ratio2
                self.assertEqual(from_logs, collected)

    def test_printed_h006_power_is_a_different_term(self):
        for k in (1, 2):
            s, xi, alpha = F(3, 4), F(7, 5), F(1, 137)
            d = s*s
            book = alpha/3*(1+s)*(xi/d**2)**(2*k+1)*d**3
            h006 = alpha/3*((1+s)*(xi/d**2))**(2*k+1)*d**3
            self.assertEqual(h006/book, (1+s)**(2*k))
            self.assertGreater(h006, book)

    def test_both_h006_root_scopes_differ_from_book_for_synthetic_values(self):
        # Choose xi=t**2, d=s**2 to keep all square roots exact rational.
        t, s = F(3, 2), F(4, 5)
        xi, d = t*t, s*s
        for k in (1, 2):
            book = (2*xi*d)**k
            product_root = (2*t*s)**k
            narrow_root = (2*t*d)**k
            self.assertNotEqual(book, product_root)
            self.assertNotEqual(book, narrow_root)

    def test_book_alpha3_division_introduces_no_extra_k(self):
        for k in (1, 2):
            for q in (0, 1, 2):
                f_numerator, h, g = F(13, 7), F(3, 17), F(5, 19)
                alpha3 = (f_numerator-k*q*(h+g))/k
                self.assertEqual(alpha3, f_numerator/k-q*(h+g))

    def test_log_coefficient_is_not_determined_by_exponentiation(self):
        # Synthetic positive base: both A1 choices give valid but different H.
        # Demonstrates freedom after assuming the log ansatz, not a physical fit.
        base, common = F(5, 7), F(11, 13)
        self.assertNotEqual(common*base, common*base**2)
        self.assertGreater(common*base, 0)
        self.assertGreater(common*base**2, 0)


if __name__ == "__main__":
    unittest.main()

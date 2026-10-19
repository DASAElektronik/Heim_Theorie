"""Test conditional inversion and exact rounding logic; no empirical refit."""
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
import unittest
from scripts.audit_alpha import mathematical_pi
from scripts.audit_constants_anchor import (
    c_product_bounds, diagnose, gamma_from_anchor, mass_scale,
    rational_print_interval,
)


class ConstantsAnchorTests(unittest.TestCase):
    def test_print_precision_is_lexical(self):
        self.assertEqual(rational_print_interval("1.20"), (F("1.195"), F("1.205")))
        self.assertEqual(rational_print_interval("1.2e-3"), (F(".00115"), F(".00125")))

    def test_product_exact_boundaries_and_invalid_domain(self):
        self.assertEqual(c_product_bounds((F(1), F(2)), (F(3), F(4)), (F(2), F(3))), (12, 72))
        with self.assertRaises(ValueError):
            c_product_bounds((F(-1), F(2)), (F(3), F(4)), (F(2), F(3)))

    def test_anchor_roundtrip_against_original_97(self):
        with localcontext() as ctx:
            ctx.prec = 70
            pi = mathematical_pi()
            for gamma, hbar, c, s0, de in [(D(2), D(3), D(5), D(7), D(11)),
                                         (D("6e-11"), D("1e-34"), D("3e8"), D(1), D(".05"))]:
                me = mass_scale(gamma, hbar, c, s0, pi)*de
                recovered = gamma_from_anchor(me, de, hbar, c, s0, pi)
                self.assertLess(abs(recovered/gamma-1), D("1e-65"))

    def test_anchor_sixth_power_sensitivity(self):
        with localcontext() as ctx:
            ctx.prec = 60
            args = dict(me=D(2), de=D(3), hbar=D(5), c=D(7), s0=D(11), pi=mathematical_pi())
            base = gamma_from_anchor(**args)
            self.assertLess(abs(gamma_from_anchor(**(args | {"de": D(6)}))/base-64), D("1e-56"))
            self.assertLess(abs(gamma_from_anchor(**(args | {"me": D(4)}))/base-D(1)/64), D("1e-58"))

    def test_mass_scale_units(self):
        # Exponents (mass,length,time): mu^6 = hbar^5 / (gamma*c^3*s0^4).
        hbar, gamma, c, s0 = (1,2,-1), (-1,3,-2), (0,1,-1), (0,1,0)
        self.assertEqual(tuple(5*hbar[i]-gamma[i]-3*c[i]-4*s0[i] for i in range(3)), (6,0,0))

    def test_numeric_precision_stability(self):
        self.assertEqual(diagnose(60), diagnose(90))


if __name__ == "__main__":
    unittest.main()

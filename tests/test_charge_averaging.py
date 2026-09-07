"""Independent rational cases and source-conditional charge mean checks."""

import sys
import unittest
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"scripts"))
import audit_charge_averaging as charge


class ChargeAveragingTests(unittest.TestCase):
    def test_independent_rational_components(self):
        self.assertEqual(charge.component_ratios(D("0.25")),
                         {"reduced": D("0.5"), "difference": D("0.5"), "mean": D("0.75")})
        self.assertEqual(charge.energy_mean_ratio(D("0.25"), D("0.5")), D(13)/D(32))

    def test_equal_energy_mean_not_equal_charge_mean(self):
        eta, w = D("0.25"), D("0.5")
        rho = charge.energy_mean_ratio(eta, w)
        arithmetic_squared = ((D("0.5")+D("0.75"))/2)**2
        self.assertEqual(rho-arithmetic_squared, D(1)/D(64))

    def test_exact_polynomial_identity_without_decimal_roots(self):
        # Let t=sqrt(eta). Expansion of 8*[lambda*t^2+(1-lambda)*(1+t)^2/4].
        w = F(1, 2)
        self.assertEqual((8*w+2*(1-w), 4*(1-w), 2*(1-w)), (5, 2, 1))
        for t in (F(1, 4), F(1, 2), F(3, 4)):
            rho = (t*t + ((1+t)/2)**2)/2
            self.assertEqual(8*rho, 5*t*t+2*t+1)

    def test_weight_endpoints_and_degenerate_eta_one(self):
        eta = D("0.25")
        self.assertEqual(charge.energy_mean_ratio(eta, D(0)), D(9)/16)
        self.assertEqual(charge.energy_mean_ratio(eta, D(1)), eta)
        for w in charge.WEIGHTS:
            self.assertEqual(charge.energy_mean_ratio(D(1), w), D(1))

    def test_invalid_domains(self):
        for eta in map(D, ("0", "-1", "1.1", "NaN", "Infinity")):
            with self.subTest(eta=eta), self.assertRaises(ValueError):
                charge.component_ratios(eta)
        for w in map(D, ("-0.1", "1.1", "NaN", "Infinity")):
            with self.subTest(w=w), self.assertRaises(ValueError):
                charge.energy_mean_ratio(D("0.25"), w)

    def test_conditional_scale_cancellation_with_exact_rationals(self):
        # Synthetic positive constants satisfying R*epsilon0*c=1.
        # Not empirical input and not a physical determination of E0.
        p, hbar, eps0, speed, rho = F(3), F(7), F(2), F(5), F(13, 32)
        impedance = 1/(eps0*speed)
        raw_charge_sq = 9*hbar/(p**4*impedance)
        alpha = raw_charge_sq*rho/(4*p*eps0*hbar*speed)
        self.assertEqual(alpha, 9*rho/(4*p**5))
        self.assertEqual(charge.inverse_alpha_prime(D(3), D(1)), D(108))

    def test_inverse_helper_invalid_domain(self):
        for invalid in map(D, ("0", "-1", "NaN", "Infinity")):
            with self.subTest(pi=invalid), self.assertRaises(ValueError):
                charge.inverse_alpha_prime(invalid, D(1))
            with self.subTest(rho=invalid), self.assertRaises(ValueError):
                charge.inverse_alpha_prime(D(3), invalid)

    def test_precision_limits(self):
        for precision in (39, 201):
            with self.subTest(precision=precision), self.assertRaises(ValueError):
                charge.build_report(precision)
        for precision in (40, 200):
            self.assertTrue(charge.build_report(precision)["printed_approximation_check"]["matches_printed_rounding"])

    def test_source_specialization_monotonicity_and_no_fit(self):
        report = charge.build_report()
        self.assertEqual(report["modern_reference_inputs"], [])
        self.assertFalse(report["target_fitting"])
        rows = report["profiles"]
        self.assertEqual([D(r["lambda"]) for r in rows], list(charge.WEIGHTS))
        self.assertEqual(rows[2]["status"], "source_equal_mean")
        self.assertTrue(report["printed_approximation_check"]["matches_printed_rounding"])
        self.assertLess(abs(D(report["equal_mean_identity_residual"])), D("1e-70"))
        self.assertLess(D(report["d_rho_d_lambda"]), D(0))
        for left, right in zip(rows, rows[1:]):
            self.assertLess(D(left["inverse_alpha_prime"]), D(right["inverse_alpha_prime"]))

    def test_precision_convergence(self):
        low, high = charge.build_report(80), charge.build_report(120)
        with localcontext() as ctx:
            ctx.prec = 140
            for a, b in zip(low["profiles"], high["profiles"]):
                self.assertLess(abs(D(a["inverse_alpha_prime"])-D(b["inverse_alpha_prime"])), D("1e-70"))


if __name__ == "__main__":
    unittest.main()

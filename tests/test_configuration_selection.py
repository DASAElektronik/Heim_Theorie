"""Independent algebraic, numerical and scope regressions for book (98a)."""

from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"scripts"))
import audit_configuration_selection as selection


class ConfigurationSelectionTests(unittest.TestCase):
    def test_exact_synthetic_ratio_identity_and_q2_reading(self):
        # eta=1/4, eta_q=1/16 distinguish sqrt(eta) from sqrt(eta_q).
        row = selection.ratio_levels(D("0.25"), D("0.0625"), D(32))
        self.assertEqual(row["Q2"], D("0.5"))
        self.assertEqual(row["B_printed"], D(203)/8)
        self.assertEqual(row["D_from_VQ"], D(263)/8)
        self.assertEqual(row["D_minus_B"], D("7.5"))
        self.assertEqual(row["delta_VQ"], -D(7)/128)
        self.assertEqual(row["delta_VQ"], row["delta_from_D"])

    def test_all_three_levels_distinguished(self):
        with localcontext() as ctx:
            ctx.prec = 80
            pi = selection.core.mathematical_pi()
            one = selection.configuration(pi, q=1, k=1)
            three = selection.configuration(pi, q=1, k=3)
            seven = selection.configuration(pi, q=1, k=7)
            self.assertTrue(one["upstream_positive_condition"])
            self.assertFalse(one["printed_VQ_inequality"])
            self.assertTrue(one["printed_k_bound"])
            self.assertTrue(three["upstream_positive_condition"])
            self.assertFalse(three["printed_k_bound"])
            self.assertTrue(seven["printed_VQ_inequality"])
            self.assertFalse(seven["printed_k_bound"])

    def test_independent_numeric_u2(self):
        with localcontext() as ctx:
            ctx.prec = 80
            row = selection.configuration(selection.core.mathematical_pi(), q=2, k=2)
            expected = D("1.963489198102715361385288774899")
            self.assertLess(abs(row["u_B"]-expected), D("1e-29"))
            self.assertFalse(row["printed_k_bound"])

    def test_snapshot_pair_set_and_scope(self):
        report = selection.build_report()
        self.assertEqual(report["positive_integer_pairs_from_printed_bound"],
                         [[1, 1], [1, 2], [2, 1], [3, 1]])
        self.assertEqual([r["q"] for r in report["bounds"] if not r["matches_claim"]], [2])
        self.assertEqual(report["modern_reference_inputs"], [])
        self.assertFalse(report["target_fitting"])
        self.assertTrue(report["tail_certificate"]["all_checks_hold"])

    def test_80_120_convergence_and_algebra(self):
        low, high = selection.build_report(80), selection.build_report(120)
        with localcontext() as ctx:
            ctx.prec = 130
            for a, b in zip(low["bounds"], high["bounds"]):
                for field in ("u_B", "u_D", "B_printed", "D_from_VQ"):
                    self.assertLess(abs(D(a[field])-D(b[field])), D("1e-70"))
            for row in high["cases"]:
                self.assertEqual(row["printed_eta_inequality"], row["printed_k_bound"])
                self.assertEqual(row["upstream_positive_condition"], row["derived_upstream_k_bound"])
                self.assertNotEqual(row["upstream_positive_condition"], row["printed_VQ_inequality"])
                self.assertLess(abs(D(row["delta_VQ"])-D(row["delta_from_D"])), D("1e-110"))
                self.assertLess(abs(D(row["D_minus_B"])-D(row["D_minus_B_identity"])), D("1e-110"))

    def test_eta_limits_and_conditional_L_delta(self):
        with localcontext() as ctx:
            ctx.prec = 80
            pi = selection.core.mathematical_pi()
            self.assertEqual(selection.eta_qk(pi, q=0, k=2), D(1))
            self.assertLess(selection.eta_qk(pi, q=1, k=2), selection.eta_qk(pi, q=1, k=1))
            for k in (1, 2):
                row = selection.charge_change(k)
                self.assertEqual(4*row["delta"], k)
                self.assertLess(abs(row["charge_ratio"]**4-1-row["delta"]), D("1e-75"))
            self.assertEqual(selection.charge_change(15, 1)["charge_ratio"], D(2))

    def test_exact_tail_certificate_inequalities(self):
        e, a, root_a = F(49, 50), F(9, 20), F(84, 125)
        self.assertGreater(F(81, 85), e**4)
        self.assertLess(F(7, 5)**2, 2)
        self.assertLess(F(22, 49), a)
        self.assertLess(2*a, e)
        self.assertGreater(root_a**2, a)
        upper = (1+root_a)**2/(4*e)+a-a*a
        self.assertLess(upper, 1)
        self.assertEqual(str(upper), selection.rational_tail_certificate()["F_upper_rational"])

    def test_positive_monotone_threshold_and_strict_boundary(self):
        self.assertEqual(selection.threshold(D(2), 1, D(1)), D(-4))
        self.assertEqual(selection.threshold(D(2), 1, D(2)), D(236))
        with self.assertRaises(ArithmeticError):
            selection.strict_compare(D(2), D(2))
        self.assertEqual(selection.strict_compare(D(2), D("1.999")), 1)
        with localcontext() as ctx:
            ctx.prec = 80
            near = D(2)+D("1e-75")
            self.assertNotEqual(near, D(2))
            with self.assertRaises(ArithmeticError):
                selection.strict_compare(near, D(2))

    def test_invalid_domains_and_types(self):
        for bad in (True, 1.0, "1", -1):
            with self.assertRaises(ValueError):
                selection.eta_qk(D(3), q=bad, k=0)
            with self.assertRaises(ValueError):
                selection.charge_change(bad)
        for bad in (D(0), D(-1), D("NaN"), D("Infinity"), 3.0):
            with self.assertRaises(ValueError):
                selection.threshold(bad, 1, D(2))
        with self.assertRaises(ValueError):
            selection.ratio_levels(D("0.5"), D("0.6"), D(1))
        for q, k in ((0, 1), (1, 0)):
            with self.assertRaises(ValueError):
                selection.configuration(D(3), q=q, k=k)
        for precision in (True, 39, 201, 80.0):
            with self.assertRaises(ValueError):
                selection.build_report(precision)
        for precision in (40, 200):
            self.assertEqual(selection.build_report(precision)["precision"], precision)


if __name__ == "__main__":
    unittest.main()

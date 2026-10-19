"""Independent identities, published-number checks, and numerical stability."""

import copy
import json
import sys
import unittest
from decimal import Decimal as D, localcontext
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import audit_alpha as audit


class AlphaAuditTests(unittest.TestCase):
    def test_known_root_pair(self):
        with localcontext() as ctx:
            ctx.prec = 80
            small, large = audit.solve_branches(D("0.48"))
            self.assertEqual((small, large), (D("0.6"), D("0.8")))

    def test_coincident_roots(self):
        with localcontext() as ctx:
            ctx.prec = 80
            small, large = audit.solve_branches(D("0.5"))
            self.assertLess(abs(small-large), D("1e-78"))
            self.assertLess(abs(small*small-D("0.5")), D("1e-78"))

    def test_tiny_root_avoids_cancellation(self):
        with localcontext() as ctx:
            ctx.prec = 80
            rhs = D("1e-60")
            small, large = audit.solve_branches(rhs)
            self.assertEqual(small, rhs)
            self.assertEqual(large, D(1))
            self.assertEqual(small*large, rhs)

    def test_invalid_rhs(self):
        for value in ["0", "-0.1", "0.50001", "NaN", "Infinity"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                audit.solve_branches(D(value))

    def test_pi_against_independent_digits(self):
        with localcontext() as ctx:
            ctx.prec = 80
            reference = D("3.141592653589793238462643383279502884197169399375105820974944592307816406286")
            self.assertLess(abs(audit.mathematical_pi()-reference), D("1e-74"))

    def test_printing_precision_and_locale(self):
        self.assertEqual(audit.printing_interval("1,2300"), (D("1.22995"), D("1.23005")))
        self.assertEqual(audit.printing_interval("1.23"), (D("1.225"), D("1.235")))

    def test_inverse_interval_and_endpoint_tie(self):
        self.assertEqual(audit.reciprocal_interval((D(2), D(4))), (D("0.25"), D("0.5")))
        self.assertTrue(audit.intervals_overlap((D(1), D(2)), (D(2), D(3))))
        with self.assertRaises(ValueError):
            audit.reciprocal_interval((D(0), D(1)))

    def test_consistent_and_inconsistent_printed_pairs(self):
        self.assertTrue(audit.check_printed_pair("0.6000", "0.8000", reciprocal=False)["compatible_with_complementary_branches"])
        check = audit.check_printed_pair("137,03596147", "1,00001363", reciprocal=True)
        self.assertFalse(check["compatible_with_complementary_branches"])
        self.assertGreater(check["squared_sum_rounding_interval"][0], D(1))

    def test_b62_reciprocals_fail_even_with_rounding(self):
        for alpha, inverse in [("0.0072973525253328589", "137,03601"), ("0.999985890199089", "1,0000142")]:
            with self.subTest(alpha=alpha):
                self.assertFalse(audit.check_printed_reciprocal(alpha, inverse)["compatible_after_rounding"])
        self.assertTrue(audit.check_printed_reciprocal("0.2500", "4.000")["compatible_after_rounding"])

    def test_precision_convergence_and_unsquared_equations(self):
        inputs = json.loads(audit.INPUTS.read_text(encoding="utf-8"))
        lower, higher = audit.build_report(inputs, 80), audit.build_report(inputs, 120)
        for a, b in zip(lower["models"], higher["models"]):
            with self.subTest(model=a["model"], pi=a["pi_profile"]):
                self.assertLess(abs(D(a["inverse_plus"])-D(b["inverse_plus"])), D("1e-65"))
                for key in ["squared_sum_error", "product_error", "small_unsquared_equation_error", "large_unsquared_equation_error"]:
                    self.assertLess(abs(D(a[key])), D("1e-70"))

    def test_independent_1982_reference_and_fit_is_not_printed_match(self):
        inputs = json.loads(audit.INPUTS.read_text(encoding="utf-8"))
        rows = audit.build_report(inputs)["models"]
        self.assertLess(abs(D(rows[0]["inverse_plus"])-D("137.0491880266639604664053491")), D("1e-24"))
        self.assertLess(abs(D(rows[1]["inverse_plus"])-D("137.0359609951515777422060897")), D("1e-24"))
        self.assertFalse(rows[1]["matches_printed_inverse_plus_rounding"])

    def test_modern_reference_cannot_change_equation_results(self):
        inputs = json.loads(audit.INPUTS.read_text(encoding="utf-8"))
        changed = copy.deepcopy(inputs)
        changed["modern_reference"]["value"] = "999"
        first, second = audit.build_report(inputs), audit.build_report(changed)
        for a, b in zip(first["models"], second["models"]):
            self.assertEqual(a["intermediates"], b["intermediates"])
            self.assertEqual(a["alpha_plus"], b["alpha_plus"])
            self.assertEqual(a["alpha_minus"], b["alpha_minus"])
        self.assertEqual(first["printed_value_checks"], second["printed_value_checks"])

    def test_independent_1989_cross_reference_result(self):
        inputs = json.loads(audit.INPUTS.read_text(encoding="utf-8"))
        rows = audit.build_report(inputs)["models"]
        row = next(item for item in rows if item["model"] == "1989_source_cross_reference" and item["pi_profile"] == "mathematical_pi")
        self.assertLess(abs(D(row["inverse_plus"])-D("137.0360395297220016297477588")), D("1e-24"))


if __name__ == "__main__":
    unittest.main()

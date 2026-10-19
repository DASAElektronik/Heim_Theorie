"""Y3 inversion, interval extrema and independent arithmetic diagnostics."""

import json
import sys
import unittest
from decimal import Decimal as D, localcontext
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"scripts"))
import audit_alpha as core
import audit_alpha_book as book


class BookDiagnosticsTests(unittest.TestCase):
    def test_known_inverse_and_y3_without_heim_constants(self):
        # alpha=.8, R=.48; R0=.5 and A1*A2=.1 imply Y3=.4.
        self.assertEqual(book.required_rhs(D("1.25")), D("0.48"))
        self.assertEqual(book.implied_y3(D("1.25"), D("0.5"), D("0.1")), D("0.4"))

    def test_rhs_interval_includes_turning_point(self):
        lo, hi = book.rhs_interval((D("1.2"), D("1.6")))
        self.assertEqual(hi, D("0.5"))
        self.assertLessEqual(lo, book.required_rhs(D("1.2")))
        self.assertLessEqual(lo, book.required_rhs(D("1.6")))

    def test_domain_boundaries(self):
        self.assertEqual(book.required_rhs(D(1)), D(0))
        self.assertEqual(book.rhs_interval((D(1), D(1))), (D(0), D(0)))
        for value in ["0", "0.999", "NaN", "Infinity"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                book.required_rhs(D(value))
        with self.assertRaises(ValueError):
            book.implied_y3(D(2), D(0), D("0.1"))

    def test_y3_interval_covers_independent_target(self):
        lo, hi = book.implied_y3_interval((D("1.2499"), D("1.2501")), D("0.5"), D("0.1"))
        self.assertLess(lo, D("0.4"))
        self.assertGreater(hi, D("0.4"))

    def test_near_one_requires_exact_endpoint_arithmetic(self):
        inverse = D("1." + "0"*60 + "1")
        with localcontext() as ctx:
            ctx.prec = 28
            with self.assertRaisesRegex(ValueError, "precision"):
                book.required_rhs(inverse)
            with self.assertRaisesRegex(ValueError, "precision"):
                book.rhs_interval((inverse, inverse))
        with localcontext() as ctx:
            ctx.prec = 180
            lower, upper = book.rhs_interval((inverse, inverse))
            self.assertGreater(lower, D(0))
            ctx.prec = 220
            # Independent reference through alpha, not the inverse formula.
            alpha = D(1)/inverse
            reference = alpha*(D(1)-alpha*alpha).sqrt()
            self.assertLessEqual(lower, reference)
            self.assertGreaterEqual(upper, reference)

    def test_inexact_square_rejected_away_from_boundary(self):
        with localcontext() as ctx:
            ctx.prec = 6
            with self.assertRaisesRegex(ValueError, "precision"):
                book.required_rhs(D("137.036"))

    def test_both_monotonic_regions_and_outward_bounds(self):
        with localcontext() as ctx:
            ctx.prec = 80
            for left, right in [("1.001", "1.002"), ("100", "101")]:
                bounds = book.rhs_interval((D(left), D(right)))
                for sample in [D(left), (D(left)+D(right))/2, D(right)]:
                    value = book.required_rhs(sample)
                    self.assertLessEqual(bounds[0], value)
                    self.assertGreaterEqual(bounds[1], value)

    def test_source_pair_disjoint_y3_intervals(self):
        inputs = json.loads(core.INPUTS.read_text(encoding="utf-8"))
        report = book.build_report(inputs)
        for profile in report["profiles"]:
            self.assertFalse(profile["one_y3_can_fit_both_printed_branches"])
            self.assertEqual(len(profile["targets"]), 3)

    def test_precision_convergence(self):
        inputs = json.loads(core.INPUTS.read_text(encoding="utf-8"))
        lower, higher = book.build_report(inputs, 80), book.build_report(inputs, 120)
        for a, b in zip(lower["profiles"], higher["profiles"]):
            for x, y in zip(a["targets"], b["targets"]):
                self.assertLess(abs(D(x["implied_y3"])-D(y["implied_y3"])), D("1e-60"))

    def test_binary64_cancellation_cannot_explain_source_mismatch(self):
        inputs = json.loads(core.INPUTS.read_text(encoding="utf-8"))
        for profile in book.build_report(inputs)["profiles"]:
            check = profile["cancellation_at_source_y3_1"]
            self.assertLess(abs(D(check["binary64_unstable_error"])), D("1e-10"))
            self.assertGreater(abs(D(check["printed_inverse_minus_error"])), D("1e-5"))
            self.assertEqual([trial["precision"] for trial in check["decimal_cancellation_trials"]], [8, 10, 12, 16, 24])


if __name__ == "__main__":
    unittest.main()

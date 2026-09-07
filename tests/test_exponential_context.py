"""Independent identities and boundaries for the conditional scalar (79) image."""

from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"scripts"))
import audit_exponential_context as exp_context


class ExponentialContextTests(unittest.TestCase):
    def test_scalar_p79_bracket_identity_exact(self):
        for b in (F(-3, 5), F(0), F(3, 5)):
            for w in (F(1), F(2), F(5)):
                original = (1+b)/2*(1+(w-b)**2/(1-b*b))
                self.assertEqual(original, (w*w-2*b*w+1)/(2*(1-b)))

    def test_normalization_and_direct_p79_evaluation(self):
        with localcontext() as ctx:
            ctx.prec = 90
            for b in map(D, ("-0.6", "0", "0.6")):
                self.assertLess(abs(exp_context.profile(D(1), D("1.5"), b, D(0))["H"]-1), D("1e-85"))
                for r in map(D, ("0.1", "2", "10")):
                    w = r.exp()
                    bracket = (1+b)/2*(1+(w-b)**2/(1-b*b))
                    direct = w*(-D("0.75")*bracket.ln()).exp()
                    stable = exp_context.profile(D(1), D("1.5"), b, r)["H"]
                    self.assertLess(abs(stable/direct-1), D("1e-85"))

    def test_p79a_b_zero_is_sech_for_a_twice_lambda(self):
        with localcontext() as ctx:
            ctx.prec = 80
            for r in map(D, ("0", "1", "5")):
                result = exp_context.profile(D(1), D(2), D(0), r)
                sech = 2/(r.exp()+(-r).exp())
                self.assertLess(abs(result["H"]-sech), D("1e-75"))

    def test_all_three_asymptotic_regimes(self):
        rows = exp_context.build_report()["asymptotic_controls"]
        self.assertEqual([row["decays_at_infinity"] for row in rows], [False, False, True])
        self.assertGreater(D(rows[0]["asymptotic_slope"]), 0)
        self.assertEqual(D(rows[1]["asymptotic_slope"]), 0)
        self.assertLess(D(rows[2]["asymptotic_slope"]), 0)

    def test_relative_error_bound_and_special_order(self):
        with localcontext() as ctx:
            ctx.prec = 90
            for b in map(D, ("-0.6", "0", "0.6")):
                for r in map(D, ("1", "2", "5", "20")):
                    row = exp_context.profile(D(1), D("1.5"), b, r)
                    self.assertLessEqual(abs(row["H_over_leading_minus_one"]), row["relative_error_absolute_bound"])
                row = exp_context.profile(D(1), D("1.5"), b, D(30))
                t = D(-30).exp()
                scaled = row["H_over_leading_minus_one"]/(t*t if b == 0 else t)
                expected = -D("0.75") if b == 0 else D("1.5")*b
                self.assertLess(abs(scaled-expected), D("1e-12"))
            self.assertIsNone(exp_context.profile(D(1), D(2), D(0), D(0))["relative_error_absolute_bound"])

    def test_amplitude_difference_is_not_a_rate_difference(self):
        with localcontext() as ctx:
            ctx.prec = 80
            row = exp_context.profile(D(1), D(2), D("0.6"), D(10))
            self.assertLess(abs(row["p178_over_p79_leading_amplitude"]-D("1.25")), D("1e-75"))
            self.assertEqual(exp_context.profile(D(1), D(2), D(0), D(10))["p178_over_p79_leading_amplitude"], D(1))

    def test_exact_extremum_counterexample(self):
        a, b, ratio = F(10, 11), F(3, 5), F(11, 10)
        for w in (F(11, 5), F(5)):
            self.assertEqual((1-ratio)*w*w+b*(2*ratio-1)*w-ratio, 0)
            self.assertEqual(1-a*w*(w-b)/(w*w-2*b*w+1), 0)
        proof = exp_context.exact_counterexample()
        self.assertTrue(proof["all_residuals_zero"])
        self.assertTrue(proof["all_roots_radial"])
        self.assertTrue(proof["maximum_then_minimum"])
        self.assertFalse(proof["a_greater_than_lambda"])
        self.assertEqual(F(proof["asymptotic_slope"]), F(1, 11))

    def test_stationary_decimal_function_and_numerical_slope(self):
        with localcontext() as ctx:
            ctx.prec = 90
            for w in (D("2.2"), D(5)):
                self.assertLess(abs(exp_context.stationary_polynomial(D(1), D(10)/11, D("0.6"), w)), D("1e-85"))
            r, h = D(2), D("1e-20")
            plus = exp_context.profile(D(1), D("1.5"), D("0.6"), r+h)["H"].ln()
            minus = exp_context.profile(D(1), D("1.5"), D("0.6"), r-h)["H"].ln()
            slope = exp_context.profile(D(1), D("1.5"), D("0.6"), r)["logarithmic_slope"]
            self.assertLess(abs((plus-minus)/(2*h)-slope), D("1e-38"))

    def test_precision_convergence_and_scope(self):
        low, high = exp_context.build_report(80), exp_context.build_report(120)
        with localcontext() as ctx:
            ctx.prec = 130
            for first, second in zip(low["rows"], high["rows"]):
                for field in ("H", "leading_profile", "H_over_leading_minus_one", "logarithmic_slope"):
                    self.assertLess(abs(D(first[field])-D(second[field])), D("1e-70"))
        self.assertFalse(low["target_fitting"])
        self.assertEqual(low["modern_reference_inputs"], [])
        self.assertIn("synthetic", low["parameter_provenance"])

    def test_domains_and_near_endpoint_stability(self):
        for params in ((D(0), D(1), D(0), D(1)), (D(1), D(0), D(0), D(1)),
                       (D(1), D(1), D(1), D(1)), (D(1), D(1), D(-1), D(1)),
                       (D(1), D(1), D(0), D(-1))):
            with self.assertRaises(ValueError):
                exp_context.profile(*params)
        for bad in (True, 1.0, "1", D("NaN"), D("Infinity")):
            for slot in range(4):
                params = [D(1), D(2), D(0), D(1)]
                params[slot] = bad
                with self.assertRaises(ValueError):
                    exp_context.profile(*params)
        with self.assertRaises(ValueError):
            exp_context.stationary_polynomial(D(1), D(2), D(0), D("0.5"))
        for precision in (True, 39, 201, 80.0):
            with self.assertRaises(ValueError):
                exp_context.build_report(precision)
        with localcontext() as ctx:
            ctx.prec = 90
            row = exp_context.profile(D(1), D(2), 1-D("1e-70"), D(0))
            self.assertLess(abs(row["H"]-1), D("1e-85"))
        for precision in (40, 200):
            self.assertEqual(exp_context.build_report(precision)["precision"], precision)

    def test_finite_amplitude_for_input_closer_to_endpoint_than_precision(self):
        # Preserve the exact input string; 1-D('1e-100') would round to 1.
        with localcontext() as ctx:
            ctx.prec = 80
            for prefix in ("", "-"):
                b = D(prefix+"0."+"9"*100)
                row = exp_context.profile(D(1), D(2), b, D(0))
                amplitude_ratio = row["p178_over_p79_leading_amplitude"]
                self.assertTrue(amplitude_ratio.is_finite())
                expected = (D(2)*D("1e-100")).sqrt()
                self.assertLess(abs(amplitude_ratio*expected-1), D("1e-75"))
                self.assertLess(abs(row["H"]-1), D("1e-75"))
                self.assertEqual(row["real_selector"], D("0.5"))
                self.assertEqual(row["logarithmic_slope"], D(0))

    def test_small_positive_radius_retains_resolved_selector(self):
        b = D("0."+"9"*100)
        with localcontext() as ctx:
            ctx.prec = 220
            r = D("1e-100")
            t = (-r).exp()
            direct_selector = (1-b*t)/(1-2*b*t+t*t)
        with localcontext() as ctx:
            ctx.prec = 80
            row = exp_context.profile(D(1), D(2), b, r)
            self.assertLess(abs(row["real_selector"]-direct_selector), D("1e-75"))
            self.assertLess(abs(row["logarithmic_slope"]+1), D("1e-75"))
            for x in map(D, ("0", "0.001", "0.1", "0.10001", "1")):
                self.assertLess(abs(exp_context._one_minus_exp_negative(x)-(1-(-x).exp())), D("1e-75"))


if __name__ == "__main__":
    unittest.main()

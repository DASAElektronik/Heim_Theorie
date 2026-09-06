"""Fixed book inputs: conditional selection, not a full physical state solver."""

import copy
import json
import sys
import unittest
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"scripts"))
import audit_book_pseudosinglet as audit


class BookPseudosingletTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inputs = json.loads(audit.INPUTS.read_text(encoding="utf-8"))
        cls.report = audit.build_report(precision=80)
        cls.rows = cls.report["profiles"]

    def test_contract_rejects_changed_profiles_state_types_or_fit_inputs(self):
        paths = [("state", "k", True), ("state", "N", 1),
                 ("Y_values", "Y9", 1.0), ("Y_values", "Y3", 2),
                 ("pure_numbers", "xi", "1.61803399"),
                 (None, "target_fitting", True), (None, "mass_evaluation", 0)]
        for group, key, value in paths:
            inputs = copy.deepcopy(self.inputs)
            (inputs if group is None else inputs[group])[key] = value
            with self.subTest(group=group, key=key), self.assertRaises(ValueError):
                audit.validate_inputs(inputs)
        inputs = copy.deepcopy(self.inputs)
        inputs["alpha_profiles"].reverse()
        with self.assertRaises(ValueError):
            audit.validate_inputs(inputs)

    def test_book_index_order_and_external_eta_are_distinct(self):
        with localcontext() as ctx:
            ctx.prec = 80
            pi = audit.core.mathematical_pi()
            d, t, swapped = audit.eta(1, 1, pi), audit.eta(1, 2, pi), audit.eta(2, 1, pi)
            self.assertGreater(audit.eta(1, 0, pi), d)
            self.assertGreater(d, t)
            self.assertGreater(t, swapped)
            self.assertEqual(str(t), self.rows[0]["eta12_q1_k2"])

    def test_offsets_follow_98b_not_resonance_occupations(self):
        self.assertEqual(audit.offsets(1), [3, 3, 2, 1])
        self.assertEqual(audit.offsets(2), [24, 31, 34, 15])
        self.assertEqual(self.inputs["state"]["N"], 0)
        self.assertNotEqual(self.rows[0]["occupations"], [0]*4)

    def test_math_constants_and_alpha_equation_profile(self):
        with localcontext() as ctx:
            ctx.prec = 80
            row = self.rows[0]
            xi, pi, alpha = (D(row[v]) for v in ("xi", "pi", "alpha"))
            self.assertLess(abs(xi*xi-xi-1), D("1e-75"))
            self.assertLess(abs(D(row["alpha105_residual"])), D("1e-75"))
            self.assertLess(alpha, 1/D(2).sqrt())
            self.assertGreater(pi, 3)

    def test_printed_alpha_is_separate_not_an_exact_105_solution(self):
        row = self.rows[1]
        self.assertEqual(D(row["alpha"]), D("0.007297354572"))
        self.assertNotEqual(row["alpha"], self.rows[0]["alpha"])
        self.assertGreater(abs(D(row["alpha105_residual"])), D("1e-16"))

    def test_correction_terms_match_unsimplified_book_98c(self):
        with localcontext() as ctx:
            ctx.prec = 80
            for row in self.rows:
                alpha, d, xi, e = (D(row[v]) for v in ("alpha", "eta11", "xi", "e"))
                h = alpha/3*(1+d.sqrt())*(xi/d**2)**3*d**3
                g = d/(e*d)*(2*xi*d)*((1-d.sqrt())/(1+d.sqrt()))**2
                self.assertLess(abs(h-D(row["correction_H"])), D("1e-75"))
                self.assertLess(abs(g-D(row["correction_G"])), D("1e-75"))
                a3 = D(row["coefficients"][2])
                self.assertTrue(0 < a3 < 1)
                self.assertLess(abs(a3-(1-h-g)), D("1e-75"))

    def test_linear_active_W_path_and_N0(self):
        with localcontext() as ctx:
            ctx.prec = 80
            for row in self.rows:
                d, a16, g, w = (D(row[v]) for v in ("eta11", "A16", "g", "w"))
                pi, e, external, alpha = (D(row[v]) for v in ("pi", "e", "eta", "alpha"))
                expanded_A16 = (pi*e)**2+(pi*e)**2*alpha/(5*external) \
                    +(pi*e)**2*6*alpha*alpha/(5*external*pi)
                a1, a2, a3 = map(D, row["coefficients"])
                source_g = 27*a1+9*a2+2*a3+(-D(1)/3).exp()
                self.assertLess(abs(a16-expanded_A16), D("1e-75"))
                self.assertLess(abs(g-source_g), D("1e-75"))
                self.assertLess(abs(w-(1+d*a16)), D("1e-75"))
                self.assertLess(abs(D(row["W"])-g*w), D("1e-72"))
                self.assertEqual(row["W"], row["W1"])
                self.assertEqual(D(row["f_N0"]), 0)

    def test_successive_maxima_are_explicitly_verified(self):
        with localcontext() as ctx:
            ctx.prec = 80
            for row in self.rows:
                for coefficient, step in zip(row["coefficients"], row["greedy_steps"]):
                    a, n, p = D(coefficient), step["integer"], step["power"]
                    before = D(step["remaining_before"])
                    self.assertLessEqual(a*n**p, before)
                    self.assertGreater(a*(n+1)**p, before)
                    self.assertGreater(D(step["remaining_after"]), 0)
                    self.assertGreater(D(step["next_integer_margin"]), 0)

    def test_both_frozen_profiles_give_same_selection_tuple(self):
        for row in self.rows:
            self.assertEqual(row["integers"], [14, 9, 13, 7])
            self.assertEqual(row["occupations"], [11, 6, 11, 6])
            self.assertEqual(row["selection_case"], "ordinary_positive_rest")
            self.assertTrue(row["lower_occupation_bounds_pass"])

    def test_raw_log_is_inside_integer_cell_and_book_cap(self):
        for row in self.rows:
            self.assertTrue(0 < D(row["W4"]) < 1)
            self.assertTrue(7 < D(row["raw_N4"]) < 8)
            self.assertGreater(D(row["raw_integer_lower_margin"]), D("0.6"))
            self.assertGreater(D(row["raw_integer_upper_margin"]), D("0.3"))
            self.assertGreater(D(row["raw_cap_margin"]), 5)

    def test_direct_unweighted_structure_gate_rejects_zone_three(self):
        for row in self.rows:
            s = row["structure"]
            self.assertEqual(s["G_unweighted"], [11025, 285, 91, 7])
            self.assertEqual(s["delta_G_unweighted"], [2744, 81, 13, 1])
            self.assertEqual(s["beta_107a_unweighted"], [2459, -10, 6])
            self.assertFalse(s["noncollapsed_107a_passes"])
            self.assertTrue(s["second_row_passes"])

    def test_sigma_bandwidth_is_not_silently_merged_with_107a(self):
        with localcontext() as ctx:
            ctx.prec = 80
            for row in self.rows:
                s = row["structure"]
                self.assertTrue(s["sigma_positive"])
                self.assertTrue(s["sigma_at_least_one"])
                self.assertFalse(s["sigma_is_integer_in_decimal_evaluation"])
                self.assertLess(abs(D(s["sigma_minus_unweighted_beta4"])
                                    -D(s["sigma_difference_identity"])), D("1e-75"))
                self.assertLess(D(s["sigma_minus_unweighted_beta4"]), 0)

    def test_integerized_108_residual_is_positive_and_directly_reproduced(self):
        with localcontext() as ctx:
            ctx.prec = 80
            for row in self.rows:
                residual = D(row["equation_residual"])
                self.assertTrue(D("0.018") < residual < D("0.019"))
                self.assertLess(abs(residual-D(row["equation_residual_direct"])), D("1e-72"))
                self.assertLess(abs(D(row["real_inverse_residual"])), D("1e-75"))

    def test_lowering_N3_alone_cannot_restore_exact_108_with_fixed_N1_N2(self):
        # For N2=9, the direct 107 gate demands N3<=12: T12=78<81<T13=91.
        self.assertEqual(F(12*13, 2), 78)
        self.assertEqual(F(13*14, 2), 91)
        for row in self.rows:
            with localcontext() as ctx:
                ctx.prec = 80
                required_exp_at_12 = D(row["W4"])+D(row["coefficients"][2])
                self.assertGreater(required_exp_at_12, 1)
                # Smaller N3 only increases the required exp, but exp(-N4/3)<=1.

    def test_precision_stability_of_all_numeric_result_strings(self):
        higher = audit.build_report(precision=120)
        def compare(low, high):
            if isinstance(low, dict):
                for key in low:
                    compare(low[key], high[key])
            elif isinstance(low, list):
                for a, b in zip(low, high, strict=True):
                    compare(a, b)
            elif isinstance(low, str):
                try:
                    a, b = D(low), D(high)
                except ArithmeticError:
                    self.assertEqual(low, high)
                else:
                    self.assertTrue(a.is_finite() and b.is_finite())
                    self.assertLess(abs(a-b), D("1e-71"))
            else:
                self.assertEqual(low, high)
        with localcontext() as ctx:
            ctx.prec = 140
            compare(self.rows, higher["profiles"])

    def test_explicit_domains_and_no_unsupported_profile_mutation(self):
        for k in (0, 3, True, 1.0):
            with self.assertRaises(ValueError):
                audit.offsets(k)
        for q, k in ((-1, 1), (1, True), (1.0, 1)):
            with self.assertRaises(ValueError):
                audit.eta(q, k, D(3))
        for precision in (39, 201, True, 80.0):
            with self.assertRaises(ValueError):
                audit.build_report(precision=precision)
        with self.assertRaises(ValueError):
            audit.first_three([D(1), D(0), D(1)], D(2))
        with self.assertRaises(ValueError):
            audit.structure_diagnostics([1, 2, 3, True], D(1))

    def test_committed_snapshot_matches_new_calculation(self):
        self.assertEqual(json.loads(audit.OUTPUT.read_text(encoding="utf-8")), self.report)


if __name__ == "__main__":
    unittest.main()

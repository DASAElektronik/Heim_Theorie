"""Conditional H006 x3 selection checks, not tests of a particle mass."""

import copy
import json
import sys
import unittest
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"scripts"))
import audit_muon_selection as audit


class MuonSelectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inputs = json.loads(audit.INPUTS.read_text(encoding="utf-8"))
        cls.report = audit.build_report(precision=80)
        cls.rows = cls.report["profiles"]

    def test_two_source_charge_slots_are_equal_without_multiplicity_claim(self):
        self.assertEqual([audit.component_charge(x) for x in (0, 1)], [D(-1), D(-1)])
        for x in (-1, 2, True, 0.0):
            with self.subTest(x=x), self.assertRaises(ValueError):
                audit.component_charge(x)
        self.assertEqual(audit.STATE["kappa"], 1)

    def test_exact_source_factors_reduce_w1_and_w2(self):
        s = audit.STATE
        P, Q, q, kap = (s[v] for v in ("P", "Q", "q", "kappa"))
        c2, c3, cQ3 = P*(P-1)//2, P*(P-1)*(P-2)//6, Q*(Q-1)*(Q-2)//6
        self.assertEqual([1-Q, q-1, 1-P, c2, c3, cQ3], [0]*6)
        # Defined toy brackets: exact reduction check, not Heim coefficients.
        d, a16, a26, a31 = F(7, 8), F(9, 2), F(3, 5), F(2, 7)
        w1 = (1-Q)*F(111, 13)+kap*Q*d*a16
        w2 = (q-1)*5+(1-P)*7+c2*11+kap*(a26+q*d*d*a31)+cQ3*d*13+c3*17
        self.assertEqual(w1, d*a16)
        self.assertEqual(w2, a26+d*d*a31)
        self.assertEqual(w1+(1+w2)**(s["k"]-1), 1+d*a16)
        self.assertEqual(1-Q*(2-s["k"])*(1-kap), 1)  # No all-N electron shortcut.

    def test_contract_rejects_state_alpha_fit_and_policy_changes(self):
        changes = [
            ("state", "N", 1), ("state", "k", True), ("state", "kappa", 0),
            ("alpha_model", "eta12_q", 1), ("alpha_model", "eta12_k", True),
            (None, "mass_evaluation", True), (None, "mass_evaluation", 0),
            (None, "dimensional_constants", {"mass": "1"}),
            (None, "comparison_or_fit_inputs", ["target"]),
            (None, "selection_path", "literal XIV"),
            (None, "exp_ln_policy", "printed base for exp"),
            (None, "unannounced_target", 1),
            ("source", "id", "H010"), ("source", "path", "unrelated.pdf"),
            (None, "audit_date", "2026-09-07"),
        ]
        for container, key, value in changes:
            bad = copy.deepcopy(self.inputs)
            (bad if container is None else bad[container])[key] = value
            with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                audit.build_report(bad)
        with patch.object(audit, "component_charge", return_value=D(0)):
            with self.assertRaises(ValueError):
                audit.build_report()

    def test_all_twelve_profiles_are_predeclared_and_retained(self):
        self.assertEqual(len(self.rows), 12)
        keys = {(r["profile"]["id"], r["a16_reading"], r["alpha3_root_reading"]) for r in self.rows}
        self.assertEqual(len(keys), 12)
        bad = copy.deepcopy(self.inputs)
        bad["profiles"][0]["xi"] = "1.618"
        with self.assertRaises(ValueError):
            audit.build_report(bad)
        for field in ("a16_readings", "alpha3_root_readings"):
            bad = copy.deepcopy(self.inputs)
            bad[field].pop()
            with self.assertRaises(ValueError):
                audit.build_report(bad)

    def test_pure_numbers_and_indexed_eta_are_not_merged(self):
        for row in self.rows:
            self.assertNotEqual(row["eta"], row["eta11"])
            self.assertEqual(row["component_charges"], ["-1", "-1"])
            self.assertEqual(row["f_N0"], 0)
        with localcontext() as ctx:
            ctx.prec = 85
            row = self.rows[0]
            d, eta, pi, alpha = map(D, (row["eta11"], row["eta"], row["pure_numbers"]["pi"], row["alpha"]))
            self.assertLess(abs(d-pi/(pi**4+5).sqrt().sqrt()), D("1e-75"))
            self.assertLess(abs(eta-pi/(pi**4+4).sqrt().sqrt()), D("1e-75"))
            beta = D(row["beta"])
            self.assertLess(abs(alpha**2+beta**2-1), D("1e-75"))

    def test_w_reduction_and_regular_domains(self):
        with localcontext() as ctx:
            ctx.prec = 85
            for row in self.rows:
                d, a16, a26, a31 = map(D, (row["eta11"], row["A16"], row["A26"], row["A31"]))
                self.assertLess(abs(D(row["w1"])-d*a16), D("1e-74"))
                self.assertLess(abs(D(row["w2"])-a26-d*d*a31), D("1e-74"))
                self.assertLess(abs(D(row["w"])-1-d*a16), D("1e-74"))
                self.assertLess(abs(D(row["W"])-D(row["g"])*D(row["w"])), D("1e-72"))
                self.assertGreater(D(row["shifted_w2_base"]), 1)
                self.assertTrue(all(D(v).is_finite() and D(v) != 0 for v in row["domain_checks"].values()))
                self.assertEqual(D(row["domain_checks"]["XVIII_inactive_A24_denominator"]), 1)

    def test_slash_axis_changes_k4_but_no_constant_or_root_axis_does(self):
        for row in self.rows:
            k4 = 0 if row["a16_reading"] == "denominator_product" else 1
            self.assertEqual(row["selection_case"], "b")
            self.assertEqual(row["integers"], [14, 9, 3, k4])
            self.assertEqual(row["occupations"], [11, 6, 1, k4-1])
            self.assertEqual(row["K4_floor"], k4)
            self.assertEqual(row["integerization_method"], "decimal_floor_no_promotion")

    def test_greedy_trace_has_positive_lower_and_upper_margins(self):
        for row in self.rows:
            for item in row["greedy_steps"]:
                self.assertGreater(D(item["remaining_after"]), 0)
                self.assertGreater(D(item["next_integer_margin"]), D("0.1396"))
            self.assertEqual(row["greedy_steps"][-1]["remaining_after"], row["W4"])
            self.assertGreater(D(row["K4_floor_lower_margin"]), D("0.101"))
            self.assertGreater(D(row["K4_floor_upper_margin"]), D("0.101"))

    def test_raw_inverse_vs_floor_residual_and_analytic_bounds(self):
        with localcontext() as ctx:
            ctx.prec = 85
            for row in self.rows:
                r, raw, gap = map(D, (row["W4"], row["raw_K4"], row["equation_residual"]))
                theta = raw-row["K4_floor"]
                self.assertLess(abs(D(row["real_inverse_residual"])), D("1e-75"))
                self.assertLess(abs(gap-D(row["equation_residual_direct"])), D("1e-72"))
                self.assertLess(abs(gap-r*((theta/3).exp()-1)), D("1e-74"))
                self.assertGreater(gap, D("0.0237"))
                self.assertLess(gap, D(row["absolute_b_bound"]))
                self.assertLess(D(row["relative_exponential_residual"]), D(row["relative_exponential_b_bound"]))

    def test_no_observed_structure_boundary_and_negative_n4_is_allowed(self):
        for row in self.rows:
            self.assertTrue(row["structural_inequalities_satisfied"])
            self.assertFalse(row["exact_zone_boundary_in_decimal_evaluation"])
            for values in row["structural_margins"].values():
                self.assertGreater(min(map(D, values)), D("1.7456"))
        self.assertEqual(self.rows[0]["occupations"][-1], -1)

    def test_independent_numerical_anchors_are_regressions_not_fit_inputs(self):
        for index, values in (
            (0, ("2820.98334686566515376", ".77550392208869946149", ".76272671664486458439", ".22449607791130053851")),
            (2, ("2820.90062776759579924", ".69278482401934490485", "1.1011074817730742", ".023746486554444345575")),
        ):
            for field, expected in zip(("W", "W4", "raw_K4", "equation_residual"), values):
                self.assertLess(abs(D(self.rows[index][field])-D(expected)), D("1e-14"))
        self.assertFalse(self.inputs["comparison_or_fit_inputs"])

    def test_eighty_vs_one_hundred_twenty_digit_stability(self):
        higher = audit.build_report(precision=120)["profiles"]
        # Numeric scalar fields, coefficients, domains and trace/structure margins.
        def numeric_strings(obj):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    if key not in ("profile", "pure_numbers"):
                        yield from numeric_strings(value)
            elif isinstance(obj, (list, tuple)):
                for value in obj:
                    yield from numeric_strings(value)
            elif isinstance(obj, str):
                try:
                    yield D(obj)
                except ArithmeticError:
                    pass
        with localcontext() as ctx:
            ctx.prec = 140
            for low, high in zip(self.rows, higher):
                self.assertEqual(low["integers"], high["integers"])
                self.assertEqual(low["occupations"], high["occupations"])
                lo, hi = list(numeric_strings(low)), list(numeric_strings(high))
                self.assertEqual(len(lo), len(hi))
                self.assertGreater(len(lo), 50)
                for a, b in zip(lo, hi):
                    self.assertLess(abs(a-b), D("1e-70"))

    def test_precision_and_helper_domain_contracts(self):
        for precision in (True, 39, 201, 80.0):
            with self.assertRaises(ValueError):
                audit.build_report(precision=precision)
        for coeff, target in (((D(0), D(1), D(1)), D(4)),
                              ((D(1), D(1)), D(4)),
                              ((D(1),)*3, D(-1)), ((D(1),)*3, D("NaN"))):
            with self.assertRaises(ValueError):
                audit.maximal_integer_trace(coeff, target)
        with self.assertRaises(ValueError):
            audit.evaluate_profile(audit.PROFILES[0], "unknown", audit.ROOT_READINGS[0])
        with self.assertRaises(ValueError):
            audit.evaluate_profile(audit.PROFILES[0], audit.A16_READINGS[0], "unknown")

    def test_exact_greedy_helper_boundaries(self):
        for target, expected, rest in (("0", [0, 0, 0], "0"), ("8", [2, 0, 0], "0"),
                                       ("13.5", [2, 2, 1], ".5")):
            k, r, trace = audit.maximal_integer_trace((D(1),)*3, D(target))
            self.assertEqual(k, expected)
            self.assertEqual(r, D(rest))
            self.assertTrue(all(v["next_integer_margin"] > 0 for v in trace))

    def test_no_mass_evaluator_is_imported_and_snapshot_matches(self):
        source = Path(audit.__file__).read_text(encoding="utf-8")
        self.assertNotIn("import audit_n0_electron", source)
        self.assertNotIn("import audit_historical_n0", source)
        self.assertEqual(json.loads(audit.OUTPUT.read_text(encoding="utf-8")), self.report)
        self.assertFalse(self.report["inputs"]["dimensional_constants"])
        self.assertFalse(self.report["inputs"]["mass_evaluation"])


if __name__ == "__main__":
    unittest.main()

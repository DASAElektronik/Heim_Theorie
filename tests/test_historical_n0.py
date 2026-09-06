"""Fixed-cell algebra and isolation tests, not empirical particle-mass tests."""

import copy
import json
import sys
import unittest
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"scripts"))
import audit_historical_n0 as audit


class HistoricalN0Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inputs = json.loads(audit.INPUTS.read_text(encoding="utf-8"))
        cls.report = audit.build_report(80)

    def test_fixed_complete_factorial(self):
        rows = self.report["cells"]
        self.assertEqual([r["mask"] for r in rows], list(range(64)))
        for row in rows:
            expected = [axis for bit, axis in enumerate(audit.AXES) if row["mask"] & (1 << bit)]
            self.assertEqual(row["changed_axes"], expected)
            self.assertEqual(row["occupations"], [0]*4)
            self.assertEqual(row["K4_method"], "analytic_identity_W_equals_g")
            self.assertGreater(min(map(D, row["first_three_upper_margins"])), D("0.19"))
            self.assertGreater(min(map(D, row["A36_denominators"].values())), 0)

    def test_baseline_reproduces_unchanged_old_calculator(self):
        old = audit.n0.build_report(80)["profiles"][0]
        row = self.report["cells"][0]
        with localcontext() as ctx:
            ctx.prec = 100
            for new, prior in ((row["mass_kg"], old["mass_kg"]),
                               (row["alpha3"], old["selection_coefficients"][2]),
                               (row["G_aux"], old["mass_terms"]["G_aux"]),
                               (row["Phi_aux"], old["mass_terms"]["Phi_aux"])):
                self.assertLess(abs(D(new)-D(prior))/abs(D(prior)), D("1e-72"))

    def test_contract_rejects_changed_state_constants_axes_and_fitting(self):
        for kind in ("state", "baseline", "historical", "axes", "shared", "unit", "fit"):
            inputs = copy.deepcopy(self.inputs)
            if kind == "state":
                inputs["state"]["N"] = 1
            elif kind == "baseline":
                inputs["baseline"]["xi"] = "1.618"
            elif kind == "historical":
                inputs["historical"]["alpha_inverse"] = "137"
            elif kind == "axes":
                inputs["axes_in_forward_order"].reverse()
            elif kind == "shared":
                inputs["shared"]["s0_m"] = "2"
            elif kind == "unit":
                inputs["units"]["comparison_factor_kg_to_MeV_c2"] = "1"
            else:
                inputs["target_fitting"] = True
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                audit.evaluate_cell(0, inputs)

    def test_masks_and_extra_scope_are_bounded(self):
        for mask in (-1, 64, True, 0.5):
            with self.subTest(mask=mask), self.assertRaises(ValueError):
                audit.evaluate_cell(mask, self.inputs)
        with self.assertRaises(ValueError):
            audit.evaluate_cell(1, self.inputs, alternate_root_scope=True)

    def test_saved_output_is_never_a_mass_input(self):
        inputs = copy.deepcopy(self.inputs)
        inputs["comparison_only"]["saved_program_mass_MeV_c2"] = "123456789"
        changed = audit.build_report(80, inputs)
        self.assertEqual(changed["cells"], self.report["cells"])
        self.assertEqual(changed["forward_attribution"], self.report["forward_attribution"])
        self.assertNotEqual(changed["comparison"]["relative_to_saved"], self.report["comparison"]["relative_to_saved"])

    def test_both_orders_telescope_but_attribution_differs(self):
        with localcontext() as ctx:
            ctx.prec = 100
            rows = self.report["cells"]
            total = D(rows[63]["mass_kg"])-D(rows[0]["mass_kg"])
            by_order = []
            for key in ("forward_attribution", "reverse_attribution"):
                steps = self.report[key]
                self.assertEqual(len(steps), 6)
                self.assertEqual(steps[0]["before_mask"], 0)
                self.assertEqual(steps[-1]["after_mask"], 63)
                self.assertLess(abs(sum(D(s["delta_kg"]) for s in steps)-total), D("1e-105"))
                by_order.append({s["axis"]: D(s["delta_kg"]) for s in steps})
            self.assertNotEqual(by_order[0]["alpha_input"], by_order[1]["alpha_input"])
            self.assertGreater(abs(D(self.report["comparison"]["sum_of_isolated_deltas_minus_total"])), D("1e-39"))

    def test_attribution_order_requires_permutation_and_accepts_iterator(self):
        rows = [{"mass_kg": D(v+1)} for v in range(64)]
        self.assertEqual(len(audit.attribution(rows, reversed(range(6)))), 6)
        for order in ((0, 0, 1, 2, 3, 4), (0, 1), (0, 1, 2, 3, 4, 6)):
            with self.subTest(order=order), self.assertRaises(ValueError):
                audit.attribution(rows, order)

    def test_formula_effect_is_only_twelve_alpha3(self):
        with localcontext() as ctx:
            ctx.prec = 100
            rows = self.report["cells"]
            for mask in range(64):
                for bit in (0, 1):
                    if mask & (1 << bit):
                        continue
                    a, b = rows[mask], rows[mask | (1 << bit)]
                    self.assertEqual(a["Phi_aux"], b["Phi_aux"])
                    expected = 12*D(a["mu_kg"])*D(a["mass_plus"])*(D(b["alpha3"])-D(a["alpha3"]))
                    actual = D(b["mass_kg"])-D(a["mass_kg"])
                    self.assertLess(abs(expected-actual), D("1e-105"))

    def test_historical_alpha_is_input_not_computed_branch(self):
        with localcontext() as ctx:
            ctx.prec = 100
            a = self.report["cells"][0]
            b = self.report["cells"][63]
            self.assertLess(abs(D(b["alpha"])-1/D("137.03599976")), D("1e-79"))
            self.assertNotEqual(a["alpha"], b["alpha"])

    def test_n4_diagnostic_is_fixed_rest_mass_step(self):
        with localcontext() as ctx:
            ctx.prec = 100
            for row in self.report["cells"]:
                step = 4*D(row["mu_kg"])*D(row["mass_plus"])
                self.assertLess(abs(step-D(row["one_n4_step_kg"])), D("1e-105"))
                self.assertLess(abs(D(row["mass_kg"])-D(row["diagnostic_n4_minus1_mass_kg"])-step), D("1e-105"))

    def test_alternate_root_scope_is_separate_and_not_zero(self):
        a, b = self.report["cells"][0], self.report["baseline_alternate_root_scope"]
        self.assertFalse(a["alternate_root_scope"])
        self.assertTrue(b["alternate_root_scope"])
        self.assertEqual(a["alpha3_subtrahends"][0], b["alpha3_subtrahends"][0])
        self.assertGreater(D(b["mass_kg"]), D(a["mass_kg"]))
        with localcontext() as ctx:
            ctx.prec = 100
            self.assertLess((D(b["mass_kg"])-D(a["mass_kg"]))/D(a["mass_kg"]), D("1e-8"))

    def test_historical_conversion_only_and_mu_scaling(self):
        with localcontext() as ctx:
            ctx.prec = 130
            rows = self.report["cells"]
            for row in rows:
                self.assertLess(abs(D(row["mass_MeV_c2"])-D(row["mass_kg"])*D("5.6095892e29")), D("1e-75"))
            base = D(rows[0]["mu_kg"])
            hbar_ratio = D(rows[16]["mu_kg"])/base
            gamma_ratio = D(rows[32]["mu_kg"])/base
            self.assertLess(abs(hbar_ratio**6-(D("1.054571596e-34")/D("1.0545887e-34"))**5), D("1e-73"))
            self.assertLess(abs(gamma_ratio**6-D("6.6732e-11")/D("6.6733198e-11")), D("1e-73"))

    def test_80_120_digit_stability(self):
        high = audit.build_report(120)
        with localcontext() as ctx:
            ctx.prec = 140
            for low, hi in zip(self.report["cells"], high["cells"]):
                for key in ("mass_kg", "alpha3", "G_aux", "Phi_aux", "mu_kg"):
                    self.assertLess(abs(D(low[key])-D(hi[key]))/abs(D(hi[key])), D("1e-70"))

    def test_precision_bounds(self):
        for precision in (39, 201, True, 80.5):
            with self.subTest(precision=precision), self.assertRaises(ValueError):
                audit.build_report(precision)

    def test_exact_source_rounding_examples_not_binary_replay(self):
        pas = lambda x: int(x+F(1, 10**10))
        c = lambda x: int(x+(F(1, 10**7) if x >= 0 else -F(1, 10**7)))
        value = 1-F(5, 10**8)
        self.assertEqual((int(value), pas(value), c(value)), (0, 0, 1))
        self.assertEqual((pas(F(-1)), c(F(-1))), (0, -1))
        self.assertEqual(-3*F(-1, 3), 1)

    def test_independent_computed_anchors_not_experimental_targets(self):
        # Separate Machin/series/Newton calculation, documented and executed
        # in HISTORICAL_N0_NUMERICS_REVIEW. These are OUR outputs, not fits.
        historical = self.report["cells"][63]
        extra = self.report["baseline_alternate_root_scope"]
        with localcontext() as ctx:
            ctx.prec = 80
            for actual, anchor in (
                (historical["mass_kg"], "9.10938089197690386753098075105194e-31"),
                (historical["mu_kg"], "2.25898458329389528110641381162486e-31"),
                (historical["G_aux"], "215.999994882507734336596120389899"),
                (extra["mass_kg"], "9.07801749271748955615484414792726e-31"),
            ):
                self.assertLess(abs(D(actual)-D(anchor))/abs(D(anchor)), D("1e-29"))


if __name__ == "__main__":
    unittest.main()

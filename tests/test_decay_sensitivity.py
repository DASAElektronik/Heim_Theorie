"""Four fixed comparison cells; no inferred physical approximation tolerance."""

import json
import sys
import unittest
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"scripts"))
import audit_decay_sensitivity as audit
import audit_book_pseudosinglet as previous

I = audit.I


class DecaySensitivityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = audit.build_report()

    def test_contract_is_hash_bound_and_only_four_cells(self):
        self.assertEqual(len(self.rows), 4)
        self.assertEqual([r["A"] for r in self.rows], [F(1, 3), F(1, 5)]*2)
        document = audit.load_contract()
        document["target_fitting"] = True
        with patch.object(Path, "read_text", return_value=json.dumps(document)):
            with self.assertRaises(ValueError):
                audit.load_contract()

    def test_fixed_quantities_are_pairwise_not_cross_profile(self):
        for old, new in (self.rows[:2], self.rows[2:]):
            for key in ("a1", "a2", "a3", "A16", "w", "eta11", "alpha"):
                self.assertEqual(old[key], new[key])
            self.assertNotEqual(old["g"], new["g"])
        self.assertNotEqual(self.rows[0]["alpha"], self.rows[2]["alpha"])

    def test_baseline_shift_is_exactly_zero(self):
        for row in self.rows[::2]:
            self.assertEqual(row["delta_g"], I.point(0))
            self.assertEqual(row["delta_W"], I.point(0))

    def test_joint_reference_shift_and_total(self):
        for row in self.rows[1::2]:
            self.assertTrue(row["delta_g"].inside(F("0.10219944250"), F("0.10219944251")))
            self.assertTrue(row["delta_W"].inside(F("7.4736196435"), F("7.4736196436")))
            self.assertEqual(row["delta_W"], row["w"]*row["delta_g"])
            B = 27*row["a1"]+9*row["a2"]+2*row["a3"]
            self.assertEqual(row["g"], B+row["reference_exp"])
            self.assertEqual(row["W"], row["g"]*row["w"])

    def test_old_decimal_snapshot_fields_remain_enclosed(self):
        old = previous.build_report(precision=120)["profiles"]
        for row, decimal in zip(self.rows[::2], old, strict=True):
            for key in ("g", "w", "W"):
                self.assertTrue(row[key].lo <= F(decimal[key]) <= row[key].hi)
            self.assertEqual(row["forward"]["integers"], decimal["integers"])
            self.assertEqual(row["forward"]["N123"], decimal["first_three"])

    def test_original_ordinary_branch_and_direct_conflict(self):
        for row in self.rows[::2]:
            forward = row["forward"]
            self.assertEqual(forward["case"], "ordinary_positive_rest")
            self.assertEqual(forward["N123"], [14, 9, 13])
            self.assertEqual(forward["integers"], [14, 9, 13, 7])
            self.assertEqual(forward["gates"]["beta"], (2459, -10, 6))
            self.assertFalse(forward["gates"]["passes"])
            self.assertGreater(forward["branch_margin"].lo, 0)
            self.assertGreater(forward["residual"].lo, 0)

    def test_alternative_stops_at_certified_saturation_boundary(self):
        for row in self.rows[1::2]:
            forward = row["forward"]
            self.assertEqual(forward["N123"], [14, 10, 1])
            self.assertEqual(forward["case"], "saturation_required_not_implemented")
            self.assertNotIn("integers", forward)
            self.assertNotIn("residual", forward)
            self.assertLess(forward["cap"].hi, 1)
            self.assertLess(forward["W4"].hi, forward["exp_at_cap"].lo)
            self.assertGreater(forward["branch_margin"].lo, 0)
            self.assertLess(forward["W4"].hi, audit.exp_minus(row["A"]*14).lo)
            self.assertGreater(forward["W4"].lo, audit.exp_minus(row["A"]*15).hi)

    def test_range_reduced_exp_matches_independent_decimal(self):
        self.assertEqual(audit.exp_minus(F(0)), I.point(1))
        with localcontext() as ctx:
            ctx.prec = 120
            for x in (F(1, 5), F(1, 3), F(14, 5), F(25, 3)):
                interval = audit.exp_minus(x)
                value = F((-D(x.numerator)/D(x.denominator)).exp())
                self.assertTrue(interval.lo <= value <= interval.hi)

    def test_fresh_bounds_and_increased_budget_response(self):
        for row in self.rows:
            self.assertEqual(audit.finite_box(row), (14, 19, 26, 25))
            self.assertGreater(row["a1"].lo*15**3, row["W"].hi)
            self.assertGreater(audit.base.G2(20), 14**3)
            self.assertGreater(audit.base.G3(27), 19**2)
        changed = dict(self.rows[0], W=I.point(4000))
        self.assertEqual(audit.finite_box(changed)[0], 15)

    def test_gate_count_by_independent_enumeration(self):
        count = 0
        for a in range(15):
            for b in range(20):
                for c in range(27):
                    for d in range(26):
                        valid = (a**3 > sum(j*j for j in range(b+1))
                                 and b*b > c*(c+1)//2 and c > d
                                 and a**3 >= b*b >= c >= 1 and a > 0)
                        count += valid
        self.assertEqual(count, 9231)
        self.assertTrue(all(row["existence"]["integer_states"] == count for row in self.rows))

    def test_all_cells_exclude_integer_and_both_real_domains(self):
        for row in self.rows:
            e = row["existence"]
            self.assertTrue(e["integer_excluded"])
            self.assertEqual(e["integer_unresolved"], [])
            self.assertTrue(e["declared_real_relaxation_excluded"])
            self.assertTrue(e["additional_direct_real_gate_excluded"])
            self.assertGreater(e["certified_integer_gap"], 0)
            self.assertGreater(e["additional_direct_real_gap"], 0)
        for row in self.rows[1::2]:
            self.assertGreater(row["existence"]["certified_integer_gap"], F("0.9432492549"))
            self.assertGreater(row["existence"]["additional_direct_real_gap"], F("0.7619800080"))

    def test_saturation_prefix_does_not_itself_prove_full_exclusion(self):
        # This boundary point satisfies direct gates, but not exact energy.
        for row in self.rows[1::2]:
            self.assertTrue(audit.gates(14, 10, 1, 0)["passes"])
            residual = row["a1"]*14**3+row["a2"]*100+row["a3"]+1-row["W"]
            self.assertGreater(residual.lo, F("0.9432492549"))

    def test_lower_bound_display_never_rounds_up(self):
        for value in (F(1, 3), F(-1, 3), F("0.94324925496652")):
            displayed = F(audit.show_lower(value))
            self.assertLessEqual(displayed, value)
            self.assertLess(value-displayed, F(1, 10**12))

    def test_interval_sign_strictness_is_not_an_epsilon(self):
        interval = I(F(-1, 10**30), F(1, 10**30))
        self.assertFalse(interval.lo > 0 or interval.hi < 0)

    def test_invalid_domains(self):
        for x in (True, 0.2, "1/5"):
            with self.assertRaises(TypeError):
                audit.exp_minus(x)
        with self.assertRaises(ValueError):
            audit.exp_minus(F(-1))
        with self.assertRaises(ValueError):
            audit.gates(1, 2, 3, -1)
        with self.assertRaises(ValueError):
            audit.finite_box(dict(self.rows[0], a1=I.point(-1)))


if __name__ == "__main__":
    unittest.main()

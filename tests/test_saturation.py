"""Fixed saturation extension, mathematical TRC envelope, separate domains."""

import copy
import json
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"scripts"))
import audit_saturation as audit

I = audit.I


class SaturationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old = audit.decay.build_report()
        cls.rows = audit.build_report()

    def test_four_bound_cells_and_no_parameter_change(self):
        self.assertEqual(len(self.rows), 4)
        document = audit.load_contract()
        document["mass_evaluation"] = True
        with patch.object(Path, "read_text", return_value=json.dumps(document)):
            with self.assertRaises(ValueError):
                audit.load_contract()

    def test_extension_does_not_mutate_previous_output(self):
        before = copy.deepcopy(self.old)
        for row in self.old:
            audit.extend(row)
        self.assertEqual(self.old, before)

    def test_ordinary_controls_unchanged(self):
        for old, row in zip(self.old[::2], self.rows[::2], strict=True):
            self.assertEqual(row["integers"], old["forward"]["integers"])
            self.assertEqual(row["kind"], "unchanged_ordinary_control")
            self.assertFalse(row["direct_gates"]["passes"])
            self.assertIsNone(row["cap_choice"])

    def test_both_saturation_cells_select_zero_after_both_trc_options(self):
        for row in self.rows[1::2]:
            self.assertEqual(row["integers"], [14, 10, 1, 0])
            self.assertEqual(row["cap_choice"]["trc_envelope"], [(0, 0), (1, 0)])

    def test_synthetic_cap_envelope_equals_floor(self):
        for numerator in range(0, 301):
            cap = F(numerator, 30)
            self.assertEqual(audit.cap_selection(I.point(cap))["N4"], cap // 1)

    def test_exact_integer_cap_has_no_unconditional_minus_one(self):
        for n in range(5):
            choice = audit.cap_selection(I.point(n))
            self.assertEqual(choice, dict(N4=n, trc_envelope=[(n, n)]))

    def test_uncertain_or_negative_caps_are_not_rounded_into_acceptance(self):
        with self.assertRaises(ArithmeticError):
            audit.cap_selection(I(F(99, 100), F(101, 100)))
        with self.assertRaises(ValueError):
            audit.cap_selection(I.point(-1))

    def test_direct_and_weighted_conditions_remain_distinct(self):
        for row in self.rows[1::2]:
            self.assertEqual(row["direct_gates"]["beta"], (2359, 99, 1))
            self.assertEqual(row["direct_gates"]["second_row"], (2644, 99, 0))
            self.assertTrue(row["direct_gates"]["passes"])
            self.assertGreater(row["sigma_107b"].lo, 0)
            self.assertLess(row["sigma_107b"].hi, 1)

    def test_negative_small_occupations_respect_source_minima(self):
        for row in self.rows[1::2]:
            self.assertEqual(row["small_n"], (11, 7, -1, -1))
            self.assertTrue(row["small_n_lower_bounds_pass"])
            self.assertEqual(row["integers"][3], 0)
            self.assertNotEqual(row["direct_gates"]["beta"][2], 0)

    def test_saturated_residual_identity_is_positive(self):
        for old, row in zip(self.old[1::2], self.rows[1::2], strict=True):
            self.assertEqual(row["R_identity"], 1-old["forward"]["W4"])
            self.assertGreater(row["R_identity"].lo, F("0.9432492549"))
            self.assertGreater(row["R_direct"].lo, F("0.9432492549"))
            self.assertTrue(row["exact_scalar_excluded"])

    def test_non_saturation_branch_has_no_invented_continuation(self):
        row = dict(self.old[1], forward=dict(self.old[1]["forward"], case="transfer"))
        with self.assertRaises(ValueError):
            audit.extend(row)
        row["forward"] = dict(self.old[1]["forward"], branch_margin=I.point(0))
        with self.assertRaises(ArithmeticError):
            audit.extend(row)


if __name__ == "__main__":
    unittest.main()

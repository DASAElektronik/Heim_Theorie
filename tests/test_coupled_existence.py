"""Exact enclosures and a complete necessary-condition exclusion, not a fit."""

import json
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"scripts"))
import audit_coupled_existence as audit
import audit_book_pseudosinglet as previous

I = audit.Interval


class CoupledExistenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = audit.certify()

    def test_input_hash_rejects_changed_y(self):
        changed = audit.load_inputs()
        changed["Y_values"]["Y9"] = 2
        with patch.object(Path, "read_text", return_value=json.dumps(changed)):
            with self.assertRaises(ValueError):
                audit.load_inputs()

    def test_exact_input_types_and_interval_order(self):
        for value in (True, 0.1, "0.1"):
            with self.assertRaises(TypeError):
                I.point(value)
        with self.assertRaises(ValueError):
            I(F(2), F(1))
        with self.assertRaises(ValueError):
            I.point(2)**-1

    def test_outward_quantization_both_signs(self):
        for value in (F(1, 3), F(-1, 3), F(0), F(3, 8)):
            interval = I.point(value)
            self.assertLessEqual(interval.lo, value)
            self.assertGreaterEqual(interval.hi, value)
            self.assertLessEqual(interval.hi-interval.lo, F(1, audit.SCALE))

    def test_interval_arithmetic_contains_endpoint_products(self):
        for x in (I(F(-2), F(3)), I(F(1, 3), F(7, 5))):
            for y in (I(F(-4), F(-1)), I(F(-3), F(5))):
                for a in (x.lo, (x.lo+x.hi)/2, x.hi):
                    for b in (y.lo, (y.lo+y.hi)/2, y.hi):
                        for interval, exact in ((x+y, a+b), (x-y, a-b), (x*y, a*b)):
                            self.assertLessEqual(interval.lo, exact)
                            self.assertGreaterEqual(interval.hi, exact)

    def test_reciprocal_negative_and_positive_domains(self):
        for lo, hi in ((F(-5), F(-2)), (F(2), F(5))):
            result = I(lo, hi).reciprocal()
            self.assertLessEqual(result.lo, 1/hi)
            self.assertGreaterEqual(result.hi, 1/lo)
        for lo, hi in ((F(-1), F(1)), (F(0), F(1)), (F(0), F(0))):
            with self.assertRaises(ValueError):
                I(lo, hi).reciprocal()

    def test_square_root_isqrt_certifies_endpoints(self):
        for value in (F(0), F(4), F(2), F(1, 7), F(1, audit.SCALE)):
            source = I.point(value)
            result = source.sqrt()
            self.assertLessEqual(result.lo**2, source.lo)
            self.assertGreaterEqual(result.hi**2, source.hi)
        self.assertEqual(I.point(4).sqrt(), I.point(2))
        with self.assertRaises(ValueError):
            I.point(-1).sqrt()

    def test_machin_tangent_identity(self):
        tan_2a = 2*F(1, 5)/(1-F(1, 5)**2)
        tan_4a = 2*tan_2a/(1-tan_2a**2)
        tan_difference = (tan_4a-F(1, 239))/(1+tan_4a*F(1, 239))
        self.assertEqual(tan_difference, 1)

    def test_atan_odd_even_bounds_overlap_and_shrink(self):
        broad = audit.atan_reciprocal_bounds(5, terms=2)
        for terms in (3, 8, 9, 48):
            narrow = audit.atan_reciprocal_bounds(5, terms=terms)
            self.assertTrue(narrow.inside(broad.lo, broad.hi))
        with self.assertRaises(ValueError):
            audit.atan_reciprocal_bounds(1)

    def test_exp_positive_remainder_and_zero(self):
        self.assertEqual(audit.exp_positive_bounds(F(0)), I.point(1))
        for x in (F(1, 3), F(1)):
            broad = audit.exp_positive_bounds(x, terms=8)
            narrow = audit.exp_positive_bounds(x, terms=64)
            self.assertTrue(narrow.inside(broad.lo, broad.hi))
            self.assertGreater(narrow.lo, 1)
        for x in (F(-1), F(2)):
            with self.assertRaises(ValueError):
                audit.exp_positive_bounds(x)

    def test_certified_book_boxes_and_profile_separation(self):
        for row in self.rows:
            for key, bounds in audit.PROOF_BOX.items():
                self.assertTrue(row[key].inside(*bounds))
        self.assertGreater(self.rows[0]["alpha"].lo, 0)
        self.assertLess(self.rows[0]["alpha"].hi, F(1, 2))
        first, second = (row["alpha"] for row in self.rows)
        self.assertTrue(first.hi < second.lo or second.hi < first.lo)
        self.assertEqual(second, I.point(F("0.007297354572")))

    def test_old_decimal_values_are_enclosed_not_used_as_certificate(self):
        old = previous.build_report(precision=120)["profiles"]
        for row, prior in zip(self.rows, old, strict=True):
            for key in ("pi", "e", "xi", "eta", "eta11", "alpha", "A16", "g", "W"):
                value = F(prior[key])
                self.assertLessEqual(row[key].lo, value)
                self.assertGreaterEqual(row[key].hi, value)
            for j, key in enumerate(("a1", "a2", "a3")):
                value = F(prior["coefficients"][j])
                self.assertLessEqual(row[key].lo, value)
                self.assertGreaterEqual(row[key].hi, value)

    def test_structure_thresholds_and_finite_box(self):
        self.assertEqual(audit.G2(19), 2470)
        self.assertEqual(audit.G3(25), 325)
        self.assertTrue(all(v > 0 for v in audit.structure_thresholds().values()))
        # Energy first bounds N1<=14; gates then give N2<=19,N3<=26,N4<=25.
        for n1 in range(15):
            self.assertGreater(audit.G2(20), n1**3)
        for n2 in range(20):
            self.assertGreater(audit.G3(27), n2**2)

    def test_coarse_five_case_certificate(self):
        box = {key: I(*bounds) for key, bounds in audit.PROOF_BOX.items()}
        margins = audit.energy_margins(box)
        self.assertEqual(len(margins), 5)
        self.assertEqual(min(margins.values()), F(7, 5000))

    def test_both_profiles_have_certified_gap_larger_than_057(self):
        for row in self.rows:
            self.assertGreater(min(audit.energy_margins(row).values()), F(57, 1000))

    def test_exhaustive_finite_triples_with_relaxed_fourth_zone(self):
        # Independent enumeration of the proved finite box, not a chosen cutoff.
        # All N4>=0 (even real) give an exponential contribution in (0,1].
        count = 0
        for n1 in range(15):
            for n2 in range(20):
                if n1**3 <= audit.G2(n2):
                    continue
                for n3 in range(27):
                    if n2*n2 <= audit.G3(n3):
                        continue
                    count += 1
                    for row in self.rows:
                        low = row["a1"].lo*n1**3+row["a2"].lo*n2*n2+row["a3"].lo*n3
                        high = row["a1"].hi*n1**3+row["a2"].hi*n2*n2+row["a3"].hi*n3+1
                        self.assertTrue(high < row["W"].lo or low > row["W"].hi)
        self.assertGreater(count, 0)

    def test_old_greedy_tuple_fails_the_necessary_gate(self):
        n1, n2, n3, n4 = (14, 9, 13, 7)
        self.assertGreater(n1**3, audit.G2(n2))
        self.assertEqual(n2*n2-audit.G3(n3), -10)
        self.assertGreater(n3, n4)


if __name__ == "__main__":
    unittest.main()

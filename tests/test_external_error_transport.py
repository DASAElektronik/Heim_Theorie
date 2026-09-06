"""Own exact algebra examples; no repaired book inputs or physical error budget."""

import itertools
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"scripts"))
import audit_external_error_transport as audit


class ExternalErrorTransportTests(unittest.TestCase):
    def test_raw_three_point_identity(self):
        P, B, w, vn, v1, v0 = F(2), F(1), F(2), F(1, 4), F(1, 2), F(1)
        old = audit.residual(P, B, w, vn, v1, v0)
        for hn, h1, h0 in itertools.product((F(-1, 10), F(1, 5)), repeat=3):
            new = audit.residual(P, B, w, vn+hn, v1+h1, v0+h0)
            values = {0: h0, 1: h1, 2: hn}
            self.assertEqual(new-old, audit.raw_change(2, 1, w, values))

    def test_normalization_at_zero_reduces_to_effective_identity(self):
        values = {0: F(2, 3), 1: F(-1, 5), 7: F(3, 8)}
        for w in (F(1, 2), F(1), F(2), F(73)):
            self.assertEqual(audit.raw_change(7, 1, w, values),
                             audit.effective_change(w, values[7]-values[0], values[1]-values[0]))

    def test_all_weights_sum_to_zero(self):
        for n, w in itertools.product((0, 1, 2, F(7, 3)), (F(1, 2), F(1), F(2), F(73))):
            self.assertEqual(sum(audit.raw_weights(n, 1, w).values()), 0)

    def test_constant_raw_offsets_cancel_exactly(self):
        for n, offset in itertools.product((0, 1, 2, 100), (F(-5), F(0), F(2, 3))):
            values = {key: offset for key in (0, 1, n)}
            self.assertEqual(audit.raw_change(n, 1, 73, values), 0)

    def test_empty_state_and_skeleton_reference_are_different(self):
        self.assertEqual(audit.raw_weights(0, 1, 73), {F(0): F(73), F(1): F(-73)})
        self.assertEqual(audit.raw_weights(1, 1, 73), {F(1): F(-72), F(0): F(72)})
        values = {0: F(3, 10), 1: F(2, 10)}
        self.assertEqual(audit.raw_change(0, 1, 73, values), F(73, 10))
        self.assertEqual(audit.raw_change(1, 1, 73, values), F(72, 10))

    def test_raw_zero_value_is_not_required_to_equal_one(self):
        a = audit.residual(2, 1, 2, F(1, 4), F(1, 2), 1)
        b = audit.residual(2, 1, 2, F(1, 4)+3, F(1, 2)+3, 4)
        self.assertEqual(a, b)

    def test_one_sided_and_joint_changes_can_point_oppositely(self):
        # Toy v(n)=2^-n at n=2, not the book exponential.
        old = audit.residual(2, 1, 2, F(1, 4), F(1, 2), 1)
        c = F(1, 4)
        only_left = old+c
        joint = audit.residual(2, 1, 2, F(1, 4)+c, F(1, 2)+c, 1)
        self.assertEqual((old, only_left, joint), (F(-3, 4), F(-1, 2), F(-1)))

    def test_coalesced_interval_endpoints(self):
        boxes = {0: (F(-1, 10), F(1, 5)), 1: (F(-1, 3), F(1, 4)),
                 2: (F(1, 10), F(1, 2))}
        for n, w in itertools.product((0, 1, 2), (F(1, 2), F(1), F(73))):
            lo, hi = audit.raw_box(n, 1, w, boxes)
            corners = [audit.raw_change(n, 1, w, dict(zip(boxes, values)))
                       for values in itertools.product(*boxes.values())]
            self.assertEqual((lo, hi), (min(corners), max(corners)))

    def test_same_argument_box_is_tighter_than_three_independent_slots(self):
        eps, w = F(1, 10), F(73)
        lo, hi = audit.raw_box(1, 1, w, {0: (0, 0), 1: (-eps, eps)})
        self.assertEqual((lo, hi), ((1-w)*eps, (w-1)*eps))
        self.assertLess(hi, (1+w)*eps)

    def test_uniform_raw_bound_need_not_bound_effective_error(self):
        eps = F(1, 10)
        h0, h1 = -eps, eps
        self.assertLessEqual(abs(h0), eps)
        self.assertLessEqual(abs(h1), eps)
        self.assertEqual(abs(h1-h0), 2*eps)

    def test_strict_robustness_condition_and_inconclusive_equality(self):
        L = audit.GAP
        self.assertEqual(audit.robust_gap(L, L/2), L/2)
        self.assertIsNone(audit.robust_gap(L, L))
        self.assertIsNone(audit.robust_gap(L, 2*L))
        # An abstract equal budget may cancel; a large actual change need not.
        self.assertEqual(L-L, 0)
        self.assertNotEqual(L+2*L, 0)

    def test_local_error_control_is_not_global(self):
        # Own function witness only, not a corrected Heim solution.
        def h(n):
            return F(0) if n <= 25 else F(1)
        self.assertTrue(all(h(n) == 0 for n in range(26)))
        self.assertEqual(audit.raw_change(26, 1, 73, {0: h(0), 1: h(1), 26: h(26)}), 1)

    def test_changes_of_coefficients_and_w_include_cross_terms(self):
        P, B, w, vn, v1 = F(2), F(1), F(2), F(1, 4), F(1, 2)
        old = audit.residual(P, B, w, vn, v1, 1)
        for dP, dB, dw, dn, dr in itertools.product((F(-1, 4), F(1, 3)), repeat=5):
            new = audit.residual(P+dP, B+dB, w+dw, vn+dn, v1+dr, 1)
            self.assertEqual(new-old, audit.joint_change(w, dP, dB, dw, B+v1, dn, dr))

    def test_fixed_book_multiplier_and_gap_remain_certified(self):
        factors = audit.fixed_book_factors()
        self.assertEqual(len(factors), 2)
        for _, w in factors:
            self.assertLess(audit.W_FACTOR_LO, w.lo)
            self.assertLess(w.hi, audit.W_FACTOR_HI)
        # Logical sufficient envelope, NOT a measured or sourced error allowance.
        bound = audit.GAP/(1+audit.W_FACTOR_HI)
        self.assertEqual((1+audit.W_FACTOR_HI)*bound, audit.GAP)

    def test_printed_divisor_step_alone_leaves_two_candidates(self):
        candidates = [z for z in range(1, 15) if 15 % z == 0]
        self.assertEqual(candidates, [1, 3, 5])
        after_strict_A_order = [z for z in candidates if F(z, 15) > F(1, 15)]
        self.assertEqual(after_strict_A_order, [3, 5])
        # No calculation of states with either alternative is performed here.

    def test_invalid_domains_and_inexact_inputs_are_rejected(self):
        for value in (True, 0.1, "1/10"):
            with self.assertRaises(TypeError):
                audit.raw_weights(value, 1, 73)
        for n, q, w in ((-1, 1, 73), (1, 0, 73), (1, 1, 0)):
            with self.assertRaises(ValueError):
                audit.raw_weights(n, q, w)
        with self.assertRaises(ValueError):
            audit.raw_box(1, 1, 73, {0: (0, 0), 1: (1, 0)})
        with self.assertRaises(ValueError):
            audit.robust_gap(0, 1)


if __name__ == "__main__":
    unittest.main()

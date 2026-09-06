"""Exact reduced scalar diagnostics, NOT solutions of Heim's metronic theory.

No source constants, mass calculator, numerical target or Y9 fit is imported.
The proofs and their limited assumptions are in F16_DETERMINACY_2026-09-06.md.
Finite test samples check algebra; they do not by themselves prove limits.
"""

from fractions import Fraction as Q
import unittest


def scalar_sequence(m, a, b):
    """Own one-variable example, not the source's three metron coordinates."""
    if m < 0:
        raise ValueError("m must be nonnegative")
    return a + b / (1 + Q(m))


def slow_sequence(m, a, b, scale):
    """Own family with a fixed positive scale in each individual limit."""
    if m < 0 or scale <= 0:
        raise ValueError("m >= 0 and scale > 0 required")
    return a + b * scale / (scale + Q(m))


def invert_limit(t, g, d, f):
    """Own rearrangement of T=g(1+d*A)(1+f), with fixed external inputs."""
    if g <= 0 or d <= 0 or f == -1:
        raise ValueError("requires g,d > 0 and f != -1")
    return (t / (g * (1 + f)) - 1) / d


class F16DeterminacyTests(unittest.TestCase):
    def test_distinct_limits_have_identical_remainder(self):
        for m in (0, 1, 20, 10**12):
            first = scalar_sequence(m, Q(1), Q(1))
            second = scalar_sequence(m, Q(2), Q(1))
            self.assertEqual(second - first, 1)
            self.assertEqual(first - 1, second - 2)
            self.assertGreater(first, 0)

    def test_explicit_tail_bound(self):
        for b in (Q(-3), Q(0), Q(1, 5), Q(7)):
            for epsilon in (Q(1, 10), Q(1, 10**9)):
                m = int(abs(b) / epsilon) + 1
                error = abs(scalar_sequence(m, Q(2), b) - 2)
                self.assertEqual(error, abs(b) / (m + 1))
                self.assertLess(error, epsilon)

    def test_fixed_coupling_preserves_different_limits(self):
        d = Q(3, 5)
        for m in (0, 3, 80):
            f1 = scalar_sequence(m, Q(1), Q(1, 7))
            f2 = scalar_sequence(m, Q(2), Q(1, 7))
            self.assertEqual(d * f2 - d * f1, d)
            self.assertEqual((1 + d * f2) - (1 + d * f1), d)

    def test_skeleton_switch_does_not_measure_coefficient(self):
        # Source's k=1,Q=1,kappa=0 spinor role only; not all skeletons.
        d, switch = Q(3, 5), 0
        for a in (Q(-9), Q(0), Q(1), Q(100)):
            self.assertEqual(switch * d * a, 0)
            self.assertEqual(1 + switch * d * a, 1)

    def test_even_extra_zero_origin_does_not_fix_limit(self):
        # F(0)=0 is NOT a source condition; deliberately stronger toy premise.
        for a in (Q(1), Q(2)):
            self.assertEqual(scalar_sequence(0, a, -a), 0)
            self.assertEqual(scalar_sequence(10, a, -a), a * Q(10, 11))
        self.assertNotEqual(scalar_sequence(10, Q(1), Q(-1)),
                            scalar_sequence(10, Q(2), Q(-2)))

    def test_fixed_scale_has_explicit_tail_bound(self):
        for scale in (Q(1, 3), Q(5), Q(10**8)):
            b, epsilon = Q(3), Q(1, 100)
            m = int(b * scale / epsilon) + 1
            self.assertLess(slow_sequence(m, Q(2), b, scale) - 2,
                            epsilon)

    def test_large_m_alone_gives_no_uniform_small_error(self):
        for m in (1, 10**6, 10**30):
            # Different family member scale=m at each diagnostic point.
            # This does NOT deny convergence for any one fixed scale.
            self.assertEqual(slow_sequence(m, Q(2), Q(3), Q(m)) - 2,
                             Q(3, 2))

    def test_conditional_inverse_round_trip(self):
        for a in (Q(-1, 2), Q(1), Q(9)):
            for g in (Q(2), Q(7, 3)):
                for d in (Q(1, 3), Q(4, 5)):
                    for f in (Q(0), Q(1, 4)):
                        t = g * (1 + d * a) * (1 + f)
                        self.assertEqual(invert_limit(t, g, d, f), a)

    def test_inverse_slope_excludes_two_roots_at_fixed_inputs(self):
        g, d, f, a1, a2 = Q(2), Q(3, 5), Q(1, 4), Q(1), Q(2)
        t1 = g * (1 + d * a1) * (1 + f)
        t2 = g * (1 + d * a2) * (1 + f)
        self.assertEqual(t2 - t1, g * d * (1 + f) * (a2 - a1))
        self.assertNotEqual(t1, t2)

    def test_toys_and_inverse_reject_excluded_domains(self):
        with self.assertRaises(ValueError):
            scalar_sequence(-1, Q(1), Q(1))
        for m, scale in ((-1, Q(1)), (0, Q(0)), (1, Q(-2))):
            with self.assertRaises(ValueError):
                slow_sequence(m, Q(1), Q(1), scale)
        for g, d, f in ((Q(0), Q(1), Q(0)), (Q(1), Q(0), Q(0)),
                        (Q(-1), Q(1), Q(0)), (Q(1), Q(1), Q(-1))):
            with self.assertRaises(ValueError):
                invert_limit(Q(1), g, d, f)


if __name__ == "__main__":
    unittest.main()

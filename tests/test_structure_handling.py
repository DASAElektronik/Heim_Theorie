"""Own bounded diagnostics of selection/structure separation, not a solver.

No historical source program is imported or executed. Rational test inputs
are synthetic, not Heim particle inputs; no source constants are replaced.
The two H010 truncation maps below are exact-real readings of the explicit
offsets, not an emulation of a historical compiler or floating-point runtime.
Static source claims require the accompanying page/line reviews.
"""

from fractions import Fraction as F
import unittest

from test_book_selection import first_three
from test_k4_w4_selection import certified_floor, negative_log_interval


def direct_gates(numbers):
    """Unweighted H004 98e/323/107, restricted to positive integer zones."""
    if len(numbers) != 4 or any(type(n) is not int or n < 1 for n in numbers):
        raise ValueError("four positive integers required")
    a, b, c, d = numbers
    g = (F(a*a*(a+1)*(a+1), 4), F(b*(b+1)*(2*b+1), 6),
         F(c*(c+1), 2), F(d))
    differences = (a**3, b**2, c, 1)
    bandwidths = tuple(differences[i] - g[i+1] for i in range(3))
    second = tuple(differences[i] >= differences[i+1] for i in range(3))
    return bandwidths, second


def pascal_offset_trunc(value):
    return int(F(value) + F(1, 10**10))


def c_offset_trunc(value):
    value = F(value)
    return int(value + (F(-1, 10**7) if value < 0 else F(1, 10**7)))


def certify_integer_map(interval, integer_map):
    """Endpoint certificate on the sign-stable intervals used below."""
    lo, hi = interval
    if lo > hi or lo < 0 < hi:
        raise ValueError("ordered sign-stable interval required")
    a, b = integer_map(lo), integer_map(hi)
    if a != b:
        raise ArithmeticError("integer output not certified")
    return a


class StructureHandlingTests(unittest.TestCase):
    def test_greedy_maxima_and_sigma_cap_do_not_imply_zone23_gate(self):
        first, residual = first_three(F(145, 2), (F(1), F(1), F(1)))
        self.assertEqual(first, (4, 2, 4))
        self.assertEqual(residual, F(1, 2))
        raw = negative_log_interval(residual, F(1, 3))
        self.assertGreater(raw[0], 2)
        self.assertLess(raw[1], 3)
        n4 = certified_floor(raw)
        self.assertEqual(n4, 2)
        self.assertLess(raw[1], first[2])
        bandwidths, second = direct_gates(first + (n4,))
        self.assertEqual(bandwidths, (59, -6, 2))
        self.assertEqual(second, (True, True, True))

    def test_valid_upper_tuple_does_not_make_component_box_valid(self):
        upper, inside = (5, 4, 3, 2), (4, 2, 3, 2)
        self.assertTrue(all(k <= u for k, u in zip(inside, upper)))
        upper_b, upper_second = direct_gates(upper)
        lower_b, lower_second = direct_gates(inside)
        self.assertEqual(upper_b, (95, 10, 1))
        self.assertTrue(all(b >= 1 for b in upper_b))
        self.assertTrue(all(upper_second))
        self.assertEqual(lower_b, (59, -2, 1))
        self.assertTrue(all(lower_second))
        self.assertLess(lower_b[1], 1)

    def test_declared_offsets_agree_away_from_integer_boundaries(self):
        for value in (F(1, 4), F(17, 8), F(-1, 4), F(-17, 8)):
            self.assertEqual(pascal_offset_trunc(value), int(value))
            self.assertEqual(c_offset_trunc(value), int(value))

    def test_pascal_and_c_offsets_are_not_the_same_integer_map(self):
        # Exact-real reading at a negative integer: positive Pascal offset
        # moves toward zero, whereas the C offset moves away from zero.
        self.assertEqual(pascal_offset_trunc(F(-2)), -1)
        self.assertEqual(c_offset_trunc(F(-2)), -2)
        close_positive = 2 - F(1, 10**8)
        self.assertEqual(pascal_offset_trunc(close_positive), 1)
        self.assertEqual(c_offset_trunc(close_positive), 2)

    def test_negative_log_truncation_is_not_floor(self):
        raw = negative_log_interval(F(3, 2), F(1))
        self.assertLess(raw[1], 0)
        self.assertGreater(raw[0], -1)
        self.assertEqual(certified_floor(raw), -1)
        for integer_map in (pascal_offset_trunc, c_offset_trunc):
            self.assertEqual(certify_integer_map(raw, integer_map), 0)

    def test_positive_rest_alone_does_not_enforce_raw_sigma_cap(self):
        # Synthetic local stage: alpha3=1,N3=1,W3=5/4,lambda=1/3.
        raw = negative_log_interval(F(1, 4), F(1, 3))
        self.assertGreater(raw[0], 4)
        self.assertLess(raw[1], 5)
        cap = F(1)
        self.assertGreater(raw[0], cap)
        # H010 positive-rest path directly truncates, book path caps first.
        for integer_map in (pascal_offset_trunc, c_offset_trunc):
            self.assertEqual(certify_integer_map(raw, integer_map), 4)
        self.assertEqual(int(cap), 1)
        # Equality is only a cap check, not a claim of all active-zone gates.

    def test_one_transfer_differs_between_book_and_ports(self):
        # Synthetic alpha3=2, beforeN3=4, W3=19/2, r=3/2,lambda=1/15.
        alpha3, before = F(2), 4
        raw = negative_log_interval(F(3, 2), F(1, 15))
        self.assertGreater(raw[0], -7)
        self.assertLess(raw[1], -6)
        after = before - 1
        book_raw = tuple(x + alpha3*before for x in raw)
        self.assertGreater(book_raw[0], 1)
        self.assertLess(book_raw[1], 2)
        self.assertLess(book_raw[1], alpha3*after)
        self.assertEqual(certified_floor(book_raw), 1)
        for integer_map in (pascal_offset_trunc, c_offset_trunc):
            port_result = certify_integer_map(raw, integer_map) + integer_map(alpha3*after)
            self.assertEqual(port_result, 0)
        # This is not a real particle, a correction prescription, or evidence
        # that a single transfer suffices for all source inputs.

    def test_helper_domain_and_certificate_guards(self):
        for bad in ((1, 2, 3), (1, 2, 3, 0), (True, 2, 3, 4), (F(1), 2, 3, 4)):
            with self.assertRaises(ValueError):
                direct_gates(bad)
        with self.assertRaises(ValueError):
            certify_integer_map((F(-1), F(1)), int)
        with self.assertRaises(ValueError):
            certify_integer_map((F(2), F(1)), int)
        with self.assertRaises(ArithmeticError):
            certify_integer_map((F(1, 2), F(3, 2)), int)


if __name__ == "__main__":
    unittest.main()

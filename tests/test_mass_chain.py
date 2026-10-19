"""Exact H004 (98e)->(112) identities; no particle data, fit, or solver.

Printed (112b) coefficients N1..N3 are called c1..c3 here, NOT occupations.
Both K lines on printed p344 have +3*Q2. A +2 mutation is synthetic only.
"""

from fractions import Fraction as F
from itertools import product
import unittest


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            result[monomial] = result.get(monomial, 0) + coefficient
    return {m: c for m, c in result.items() if c}


def scale(polynomial, coefficient):
    return {m: c * coefficient for m, c in polynomial.items() if c * coefficient}


def mul(left, right):
    result = {}
    for (i, j), c in left.items():
        for (k, l), d in right.items():
            m = (i + k, j + l)
            result[m] = result.get(m, 0) + c * d
    return {m: c for m, c in result.items() if c}


def power(polynomial, degree):
    result = {(0, 0): 1}
    for _ in range(degree):
        result = mul(result, polynomial)
    return result


def zone_polynomials(x):
    """Unweighted forms after multiplying (98e) by four and using c_j."""
    one = {(0, 0): 1}
    return (
        mul(power(x, 2), power(add(one, x), 2)),
        mul(x, add(scale(power(x, 2), 2), scale(x, 3), one)),
        mul(x, add(one, x)),
        scale(x, 4),
    )


def printed_mixed_polynomials():
    n, q, one = {(1, 0): 1}, {(0, 1): 1}, {(0, 0): 1}
    nq = mul(n, q)
    h1 = mul(scale(nq, 2), add(
        one, scale(add(n, q, nq), 3),
        scale(add(power(n, 2), power(q, 2)), 2)))
    h2 = mul(scale(nq, 6), add(one, n, q))
    h3 = scale(nq, 2)
    return h1, h2, h3, {}


def weights(a):
    return a[0], F(2, 3) * a[1], 2 * a[2]


def source_sum(x, a):
    x1, x2, x3, x4 = x
    return (a[0] * x1**2 * (1+x1)**2 / 4
            + a[1] * x2 * (2*x2**2 + 3*x2 + 1) / 6
            + a[2] * x3 * (1+x3) / 2 + x4)


def pure(x, a):
    c1, c2, c3 = weights(a)
    x1, x2, x3, x4 = x
    return (c1*x1**2*(1+x1)**2 + c2*x2*(2*x2**2+3*x2+1)
            + c3*x3*(1+x3) + 4*x4)


def mixed(n, q, a):
    c1, c2, c3 = weights(a)
    n1, n2, n3, _ = n
    q1, q2, q3, _ = q
    return (2*n1*q1*(1+3*(n1+q1+n1*q1)+2*(n1**2+q1**2))*c1
            + 6*n2*q2*(1+n2+q2)*c2 + 2*n3*q3*c3)


def vector(values):
    return tuple(map(F, values))


class MassChainTests(unittest.TestCase):
    # Synthetic inputs only: not an alpha profile or a physically selected state.
    a = vector((F(2, 7), F(3, 2), F(5, 3)))
    q = vector((3, 3, 2, 1))

    def test_all_four_polynomial_identities_coefficientwise(self):
        n, q = {(1, 0): 1}, {(0, 1): 1}
        shifted = zone_polynomials(add(n, q))
        pure_n, pure_q = zone_polynomials(n), zone_polynomials(q)
        for left, fn, k, h in zip(shifted, pure_n, pure_q,
                                  printed_mixed_polynomials(), strict=True):
            self.assertEqual(left, add(fn, k, h))

    def test_quartic_mixed_coefficients(self):
        self.assertEqual(printed_mixed_polynomials()[0], {
            (1, 1): 2, (2, 1): 6, (1, 2): 6,
            (2, 2): 6, (3, 1): 4, (1, 3): 4})

    def test_cubic_and_linear_mixed_coefficients(self):
        h = printed_mixed_polynomials()
        self.assertEqual(h[1], {(1, 1): 6, (2, 1): 6, (1, 2): 6})
        self.assertEqual(h[2], {(1, 1): 2})
        self.assertEqual(h[3], {})

    def test_fractional_weights_follow_from_four_times_g(self):
        for x in product(map(F, (-2, 0, 1, 3)), repeat=4):
            self.assertEqual(4*source_sum(x, self.a), pure(x, self.a))

    def test_full_rational_identity(self):
        cases = (vector((0, 0, 0, 0)), vector((1, 2, 3, 4)),
                 vector((F(-1, 2), F(2, 3), F(5, 7), F(-4, 9))))
        for n, q in product(cases, repeat=2):
            x = tuple(u+v for u, v in zip(n, q, strict=True))
            self.assertEqual(4*source_sum(x, self.a),
                             pure(q, self.a)+pure(n, self.a)+mixed(n, q, self.a))

    def test_zero_small_n_is_scaffold_not_resonance_zero(self):
        n = vector((0, 0, 0, 0))
        self.assertEqual(pure(n, self.a), 0)
        self.assertEqual(mixed(n, self.q, self.a), 0)
        self.assertEqual(4*source_sum(self.q, self.a), pure(self.q, self.a))

    def test_empty_total_occupations_allow_cancellation(self):
        n = tuple(-v for v in self.q)
        self.assertEqual(pure(self.q, self.a)+pure(n, self.a)
                         + mixed(n, self.q, self.a), 0)
        self.assertEqual(source_sum(vector((0, 0, 0, 0)), self.a), 0)

    def test_mixed_terms_vanish_at_either_zero_argument(self):
        zero = vector((0, 0, 0, 0))
        self.assertEqual(mixed(zero, self.q, self.a), 0)
        self.assertEqual(mixed(self.q, zero, self.a), 0)

    def test_synthetic_two_in_place_of_three_is_detected(self):
        c2 = weights(self.a)[1]
        k_mutated = pure(self.q, self.a) - c2*self.q[1]**2
        self.assertEqual(4*source_sum(self.q, self.a)-k_mutated, 9)
        self.assertNotEqual(k_mutated, pure(self.q, self.a))

    def test_mu_and_phi_transformation(self):
        n = vector((1, 2, -1, 0))
        x = tuple(u+v for u, v in zip(n, self.q, strict=True))
        s = source_sum(x, self.a)
        p = pure(self.q, self.a)+pure(n, self.a)+mixed(n, self.q, self.a)
        for mu, ap, am, fs, charge in product(
                (F(2, 3),), (F(3, 2), F(-1, 2)), (F(1, 5), F(3, 2)),
                (F(0), F(7, 9)), (F(-1), F(0), F(2))):
            r, mu_plus = am/ap, 4*mu*ap
            original = mu_plus*(s+(1-r)*fs+charge*r)
            phi = 4*(1-r)*fs+4*charge*r
            self.assertEqual(original, mu*ap*(p+phi))

    def test_empirical_extraction_is_algebraic_inversion_not_prediction(self):
        # Arbitrary dimensionless rational witness, no measured particle mass.
        mu_plus, r, s, charge, supplied_m = map(F, (8, F(1, 4), 5, 1, 100))
        mu_s = mu_plus*(1-r)
        fs = (supplied_m-mu_plus*(s+charge*r))/mu_s
        self.assertEqual(mu_plus*(s+(1-r)*fs+charge*r), supplied_m)

    def test_degenerate_fs_scale_does_not_identify_fs(self):
        mu_plus, r, s, charge = map(F, (8, 1, 5, 1))
        outcomes = {mu_plus*(s+(1-r)*fs+charge*r) for fs in map(F, (-7, 0, 9))}
        self.assertEqual(len(outcomes), 1)
        with self.assertRaises(ZeroDivisionError):
            _ = F(1)/(mu_plus*(1-r))


if __name__ == "__main__":
    unittest.main()

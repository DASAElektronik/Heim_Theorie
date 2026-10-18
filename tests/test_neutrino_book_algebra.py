from fractions import Fraction as F
import unittest

from scripts.audit_neutrino_book_algebra import STATES, from_111, printed_118b


class NeutrinoBookAlgebraTests(unittest.TestCase):
    def setUp(self):
        self.params = dict(A=F(3), B=F(5), alpha=F(1, 100),
                           sqrt_eta11=F(2), xi=F(1, 2), eta_squared=F(4))

    def test_two_control_states_reproduce_printed_expressions(self):
        for xi in (F(1, 7), F(1, 2), F(3)):
            p = dict(self.params, xi=xi)
            for label in ('e', 'mu'):
                self.assertEqual(from_111(STATES[label], **p), printed_118b(label, **p))

    def test_pi_residual_independent_of_additive_term(self):
        residuals = []
        for B in (F(1, 100), F(5), F(10000)):
            p = dict(self.params, B=B)
            direct, printed = from_111(STATES['pi'], **p), printed_118b('pi', **p)
            self.assertEqual(direct-2*B, 2*(printed-2*B))
            self.assertGreater(direct, printed)
            self.assertLess(direct, 2*printed)
            residuals.append(direct-printed)
        self.assertEqual(residuals, [F(598, 25)]*3)

    def test_cross_state_identity_with_cleared_denominator(self):
        # Independent check: (1+4xi)*(phi_pi-2B)=2*(phi_e-2B).
        for xi in (F(1, 5), F(7, 3)):
            p = dict(self.params, xi=xi)
            e = from_111(STATES['e'], **p)-2*p['B']
            pi = from_111(STATES['pi'], **p)-2*p['B']
            self.assertEqual((1+4*xi)*pi, 2*e)
            self.assertEqual((1+4*xi)*(printed_118b('pi', **p)-2*p['B']), e)

    def test_no_unreviewed_state_or_singular_parameter_extension(self):
        for state in ((1, 0, 0), (2, 0, 1), (2, 1, 0)):
            with self.assertRaises(ValueError):
                from_111(state, **self.params)
        for key, value in (('eta_squared', F(0)), ('alpha', F(3)), ('xi', F(-1, 4))):
            with self.assertRaises(ValueError):
                from_111(STATES['pi'], **dict(self.params, **{key: value}))


if __name__ == '__main__':
    unittest.main()

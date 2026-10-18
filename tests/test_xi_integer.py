import unittest
from fractions import Fraction
from scripts.audit_xi_integer import STATES, EXPECTED, calculate, evaluate, trunc_div


class XiIntegerTests(unittest.TestCase):
    def test_truncation_is_toward_zero(self):
        for a, b, expected in ((2, 4, 0), (-7, 3, -2), (7, -3, -2), (-7, -3, 2)):
            self.assertEqual(trunc_div(a, b), expected)

    def test_xi_correction_note(self):
        old = evaluate((2, 1, 1, 1), 'listing_integer')
        new = evaluate((2, 1, 1, 1), 'rational_diagnostic')
        self.assertEqual((old['CS'], old['IQX'], old['KQ']), (0, [1, 0], [1, 0]))
        self.assertEqual((new['CS'], new['IQX'], new['KQ']), (-2, [0, -1], [0, 1]))
        # Independently reduced exact Xi expression, not a target fed to evaluator.
        self.assertEqual(Fraction(2 * (-1 - 1) * 2, 2 * 2), new['CS'])

    def test_twelve_independent_source_table_rows(self):
        for state, (cs, charges) in zip(STATES, EXPECTED):
            with self.subTest(state=state):
                row = evaluate(state, 'rational_diagnostic')
                self.assertEqual((row['CS'], row['IQX']), (cs, charges))
        self.assertEqual(calculate()['affected_multiplets'], [9])

    def test_electron_regression_and_scope(self):
        for mode in ('listing_integer', 'rational_diagnostic'):
            row = evaluate((1, 1, 1, 0), mode)
            self.assertEqual((row['CS'], row['IQX'][1], row['KQ'][1]), (0, -1, 1))
        with self.assertRaises(ValueError):
            evaluate((2, 2, 2, 2), 'listing_integer')
        with self.assertRaises(ValueError):
            evaluate(STATES[0], 'silent_fix')


if __name__ == '__main__':
    unittest.main()

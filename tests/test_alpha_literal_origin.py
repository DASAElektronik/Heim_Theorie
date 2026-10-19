"""H011 coefficient definition and exact printed-pair bounds."""
from decimal import Decimal as D,localcontext
from fractions import Fraction as F
import math
import unittest
from scripts.audit_alpha_literal_origin import calculate,exact_pair_bounds


class AlphaLiteralOriginTests(unittest.TestCase):
    def test_pair_contradiction_is_exact_and_does_not_need_eta(self):
        lo,hi=exact_pair_bounds()
        self.assertGreater(lo,1)
        self.assertLess(lo,hi)
        for p in (F('137.036027245'),F('137.036027255')):
            for q in (F('1.000014105'),F('1.000014115')):
                self.assertLessEqual(lo,1/p**2+1/q**2)
                self.assertGreaterEqual(hi,1/p**2+1/q**2)

    def test_h011_definition_is_distinct_from_book_definition(self):
        # Rational square root makes the coefficient distinction exact.
        root=F(9,10);z=root**2
        h011=(1-root)/(z*(1+root))
        book=root*(1-root)/(1+root)
        self.assertEqual(z*h011*(1+root),1-root)
        self.assertEqual(h011/book,1/root**3)
        self.assertNotEqual(h011,book)

    def test_independent_binary64_inverse_quadratic(self):
        pi=3.1415926535;eta=pi/(pi**4+4)**.25
        z=[pi/(pi**4+4+k)**.25 for k in (1,2)]
        coeff=[(1-math.sqrt(t))/(t*(1+math.sqrt(t))) for t in z]
        r=9*(5*eta+2*math.sqrt(eta)+1)/(2*pi)**5*(1-coeff[0]*coeff[1])
        b=1/(2*r*r)
        inverse_small=math.sqrt(b*(1+math.sqrt(1-2/b)))
        row=next(r for r in calculate()['rows'] if r['pi_profile']=='H015_PI_literal' and r['formula']=='H011_A_conditional_eta_bridge')
        self.assertAlmostEqual(inverse_small,float(row['inverse_small']),delta=5e-12)
        self.assertFalse(row['small_inverse_within_print_rounding'])

    def test_display_stability_and_complementary_inverse(self):
        self.assertEqual(calculate(80),calculate(110))
        with localcontext() as ctx:
            ctx.prec=60
            p=D('137.03602725')
            # p/sqrt(p²-1) independently expresses the reciprocal large root.
            independent=p/(p*p-1).sqrt()
            saved=D(calculate()['pair']['implied_large_inverse_from_printed_small'])
            self.assertLess(abs(independent-saved),D('5e-16'))


if __name__=='__main__': unittest.main()

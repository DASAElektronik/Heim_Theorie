from fractions import Fraction as F
import unittest

from scripts.audit_neutrino_field_bridge import phi_b49, source_pair_field, port_pair_field


class NeutrinoFieldBridgeTests(unittest.TestCase):
    def test_empty_k1_b49_is_zero_for_both_kappas_and_buw_signs(self):
        for kap in (0, 1):
            for buw in (F(-10), F(0), F(17, 3)):
                value = phi_b49(F(-2), F(-1), F(1), F(0), 1, 1, kap,
                                n4=F(4), fourth_root_two=F(6, 5), buw=buw,
                                alpha=F(1, 100), theta=F(8),
                                pi_over_e_squared=F(4, 3), sqrt_eta12=F(9, 10))
                self.assertEqual(value, 0)

    def test_source_coefficient_weights_from_b6(self):
        P, Q, n5, n6 = 1, 1, F(5, 7), F(2, 11)
        direct = P*(-1)**(P+Q)*(P+Q)*n5+Q*(P+1)*n6
        self.assertEqual(source_pair_field(n5, n6), direct)

    def test_source_equality_cannot_hold_for_both_projected_port_states(self):
        for B, T, D in ((F(3), F(2), F(5)), (F(1, 7), F(4, 9), F(2, 3))):
            lo = port_pair_field(0, F(-1), B, T, D)
            hi = port_pair_field(1, F(-1), B, T, D)
            self.assertEqual(lo, D)
            self.assertEqual(hi-lo, B*(1+T))
            self.assertGreater(hi-lo, 0)

    def test_parent_extraction_is_not_empty_evaluation(self):
        B, T, D = F(7), F(3, 2), F(2)
        self.assertEqual(port_pair_field(0, F(0), B, T, D)
                         -port_pair_field(0, F(-1), B, T, D), B)
        self.assertEqual(port_pair_field(1, F(0), B, T, D),
                         port_pair_field(1, F(-1), B, T, D))
        with self.assertRaises(ValueError):
            phi_b49(F(-2), F(0), F(1), F(0), 1, 1, 0,
                    n4=F(4), fourth_root_two=F(6, 5), buw=F(1), alpha=F(1),
                    theta=F(8), pi_over_e_squared=F(1), sqrt_eta12=F(1))


if __name__ == '__main__':
    unittest.main()

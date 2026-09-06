"""Scoped source-algebra and independent polynomial checks, not physics tests."""

import copy
import json
import sys
import unittest
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"scripts"))
import audit_n0_electron as audit


class N0ElectronTests(unittest.TestCase):
    def test_exact_configuration_and_null_coefficients(self):
        s = audit.STATE
        k, P, Q, kap, x = (s[v] for v in ("k", "P", "Q", "kappa", "x"))
        twice_charge = (P-2*x)*(1-kap*Q*(2-k))+s["epsilon"]*(k-1-(1+kap)*Q*(2-k))+s["C"]
        self.assertEqual(twice_charge, -2)
        self.assertEqual([1-Q, kap, s["q"]-1, 1-P, P*(P-1)//2, Q*(Q-1)*(Q-2)//6], [0]*6)
        self.assertEqual((k-1+0)**(2-k)+(2-k+0)**(k-1), 1)
        self.assertEqual(1-Q*(2-k)*(1-kap), 0)

    def test_exact_shifted_polynomial_identity(self):
        coeff = (F(2, 3), F(7, 5), F(11, 13))
        for n in ((0, 0, 0, 0), (-3, -3, -2, -1), (-2, -1, 0, 4), (2, 5, 4, 8)):
            with self.subTest(n=n):
                terms = audit.auxiliary_terms(n, coeff)
                self.assertEqual(terms["shifted_identity_residual"], 0)
                a, b, c, d = (v+q for v, q in zip(n, (3, 3, 2, 1)))
                independent = (a**4+2*a**3+a**2)*coeff[0]+(2*b**3+3*b*b+b)*coeff[1]+(c*c+c)*coeff[2]+4*d
                self.assertEqual(terms["K"]+terms["G"]+terms["H"], independent)

    def test_negative_n4_is_not_forbidden_and_changes_four_units(self):
        a = audit.auxiliary_terms((0, 0, 0, 0), (D(1), D(2), D(3)))
        b = audit.auxiliary_terms((0, 0, 0, -1), (D(1), D(2), D(3)))
        self.assertEqual(a["shifted_sum"]-b["shifted_sum"], 4)

    def test_invalid_occupations(self):
        for n in ((0, 0, 0), (0, 0, 0, 0.5), (0, 0, 0, True), (-4, 0, 0, 0)):
            with self.subTest(n=n), self.assertRaises(ValueError):
                audit.auxiliary_terms(n, (D(1), D(2), D(3)))

    def test_profile_and_state_are_not_arbitrary(self):
        inputs = json.loads(audit.INPUTS.read_text(encoding="utf-8"))
        for kind in ("state", "alpha", "experimental"):
            bad = copy.deepcopy(inputs)
            if kind == "state":
                bad["state"]["N"] = 2
            elif kind == "alpha":
                bad["alpha_model"]["eta12_k"] = 2
            else:
                bad["experimental_inputs"] = ["mass target"]
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                audit.evaluate_profile(inputs["profiles"][0], bad)

    def test_zero_selection_and_structural_inequalities(self):
        report = audit.build_report()
        for row in report["profiles"]:
            selection = row["selection"]
            self.assertEqual(selection["integers"], [3, 3, 2, 1])
            self.assertEqual(selection["occupations"], [0]*4)
            self.assertEqual(selection["integerization_method"], "analytic_identity_W_equals_g")
            self.assertGreater(min(D(v) for v in selection["XIII_margins"]+selection["XXXII_margins"]), 0)
            self.assertGreater(min(D(v["upper_margin"]) for v in selection["greedy_steps"]), D("0.19"))
            self.assertEqual(D(row["mass_terms"]["K_aux"]), 0)
            self.assertEqual(D(row["mass_terms"]["H_aux"]), 0)
            self.assertGreater(D(row["mass_terms"]["G_aux"]), 0)
            self.assertGreater(D(row["mass_terms"]["Phi_aux"]), 0)

    def test_xiv_is_not_silently_equal_to_xxvi(self):
        # At n4=0,k=Q4=1 the exponents are +1/3 and -1/3.
        self.assertEqual(1-2*F(1, 3), F(1, 3))
        self.assertEqual((1-2)*F(1, 3), F(-1, 3))
        for row in audit.build_report()["profiles"]:
            self.assertGreater(D(row["selection"]["XIV_minus_XXVI_at_zero"]), D("0.67"))

    def test_analytic_k4_identity_is_not_finite_decimal_rounding(self):
        # ln(exp(t))=t on the real domain; exact exponent arithmetic.
        self.assertEqual(-3*F(-1, 3), 1)
        self.assertEqual(int(D("0.9999999999999999999999")), 0)
        self.assertEqual(audit.zero_selection(D(1), D(1), D(1))["integerized_K4"], 1)

    def test_selection_domain_limits(self):
        for bad in map(D, ("0", "-1", "NaN", "Infinity")):
            with self.subTest(value=bad), self.assertRaises(ValueError):
                audit.zero_selection(D(1), D(1), bad)
        with self.assertRaises(ValueError):
            audit.zero_selection(D(1), D(1), D("0.1"))

    def test_mu_dimensions_are_mass(self):
        # Vectors (kg,m,s) for (gamma*hbar*s0)^(1/3)
        # * (hbar/(c*gamma))^(1/2) / s0; pi factors dimensionless.
        gamma, hbar, speed, length = (-1, 3, -2), (1, 2, -1), (0, 1, -1), (0, 1, 0)
        dims = tuple(F(g+h+l, 3)+F(h-c-g, 2)-l for g,h,c,l in zip(gamma,hbar,speed,length))
        self.assertEqual(dims, (1, 0, 0))

    def test_precision_and_independent_reductions(self):
        low, high = audit.build_report(80), audit.build_report(120)
        with localcontext() as ctx:
            ctx.prec = 140
            for a, b in zip(low["profiles"], high["profiles"]):
                for key in ("mass_kg", "mu_kg", "alpha", "alpha_mass_plus"):
                    self.assertLess(abs(D(a[key])-D(b[key]))/abs(D(b[key])), D("1e-70"))
                self.assertLess(abs(D(a["identity_residuals"]["Phi"])), D("1e-70"))
                total = sum(D(v) for v in a["contribution_kg"].values())
                self.assertLess(abs(total-D(a["mass_kg"])), D("1e-100"))

    def test_precision_boundaries(self):
        for precision in (39, 201):
            with self.assertRaises(ValueError):
                audit.build_report(precision)
        self.assertEqual(len(audit.build_report(40)["profiles"]), 3)


if __name__ == "__main__":
    unittest.main()

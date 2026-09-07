"""Independent rational checks for the conditional energy/wavelength audit."""

import sys
import unittest
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"scripts"))
import audit_energy_kinematics as energy


class EnergyKinematicsTests(unittest.TestCase):
    def test_exact_rational_three_fifths(self):
        r = energy.kinematic_ratios(D("0.6"))
        expected = {
            "s": D("0.8"), "gamma": D("1.25"),
            "source_pc_over_m0c2": D("0.75"), "kinetic_T_over_m0c2": D("0.25"),
            "source_pc_over_kinetic_T": D(3), "source_r_H_over_L0": D("0.8"),
            "source_y_over_L0": D("0.64"), "K_source_pc": D("0.48"),
            "K_kinetic_energy_only": D("0.16"), "K_kinetic_energy_and_dB": D(4)/15,
        }
        for key, value in expected.items():
            with self.subTest(key=key):
                self.assertEqual(r[key], value)
        self.assertEqual(r["lambda_dB_over_lambda_H"], D(5)/3)

    def test_independent_rational_dimension_cancellation(self):
        # Synthetic scales, not measured constants or fitted data.
        pi, hbar, m, c, eps0 = F(3), F(7), F(5), F(11), F(2)
        s = F(4, 5)
        for f, g, expected in ((F(3, 5), F(1), F(12, 25)),
                               (F(1, 5), F(1), F(4, 25)),
                               (F(1, 5), F(5, 3), F(4, 15))):
            wavelength = g*(2*pi*hbar)/(m*c)
            radius = wavelength/(2*pi)
            distance = radius*s
            energy_value = f*m*c*c
            charge_correction = 4*pi*eps0*distance*energy_value
            self.assertEqual(charge_correction/(4*pi*eps0*hbar*c), expected)

    def test_ordering_on_fixed_grid(self):
        for beta in energy.BETAS:
            r = energy.kinematic_ratios(beta)
            self.assertGreater(r["source_pc_over_kinetic_T"], 1)
            self.assertGreater(r["lambda_dB_over_lambda_H"], 1)
            self.assertLess(r["source_y_over_L0"], r["source_r_H_over_L0"])
            self.assertLess(r["K_kinetic_energy_only"], r["K_kinetic_energy_and_dB"])
            self.assertLess(r["K_kinetic_energy_and_dB"], r["K_source_pc"])

    def test_invalid_beta_domain(self):
        for beta in map(D, ("0", "1", "-0.1", "1.1", "NaN", "Infinity", "-Infinity")):
            with self.subTest(beta=beta), self.assertRaises(ValueError):
                energy.kinematic_ratios(beta)

    def test_small_beta_keeps_kinetic_energy(self):
        with localcontext() as ctx:
            ctx.prec = 50
            r = energy.kinematic_ratios(D("1e-40"))
            self.assertEqual(r["s"], 1)  # Tiny correction cannot fit, as documented.
            self.assertEqual(r["kinetic_T_over_mc2"], D("5e-81"))
            self.assertEqual(r["K_kinetic_energy_and_dB"], D("5e-41"))

    def test_near_one_input_does_not_round_speed_to_one(self):
        with localcontext() as ctx:
            ctx.prec = 30
            beta = D("0."+"9"*80)
            r = energy.kinematic_ratios(beta)
            self.assertGreater(r["s"], 0)
            self.assertGreater(r["gamma"], D("1e39"))
            self.assertGreater(r["source_y_over_L0"], 0)

    def test_energy_squared_identity(self):
        with localcontext() as ctx:
            ctx.prec = 80
            for beta in energy.BETAS:
                r = energy.kinematic_ratios(beta)
                residual = r["source_pc_over_m0c2"]**2-(r["gamma"]**2-1)
                self.assertLess(abs(residual), D("1e-75"))

    def test_source_closure_and_no_measured_inputs(self):
        report = energy.build_report()
        self.assertEqual(report["modern_reference_inputs"], [])
        self.assertFalse(report["target_fitting"])
        self.assertEqual([D(r["beta"]) for r in report["fixed_beta_examples"]], list(energy.BETAS))
        self.assertEqual(D(report["book_Y3_one_profile"]["Y3"]), 1)
        self.assertLess(abs(D(report["source_closure_residual"])), D("1e-75"))
        self.assertEqual(report["profile_status"]["kinetic_energy_only"], "our_unfitted_energy_substitution")

    def test_precision_limits(self):
        for precision in (39, 201):
            with self.assertRaises(ValueError):
                energy.build_report(precision)
        for precision in (40, 200):
            self.assertEqual(energy.build_report(precision)["precision"], precision)

    def test_book_source_index_regression(self):
        # Direct book q=1,k=1/2 definitions, independent of eta_k_q helper.
        # Reference digits independently checked by the mathematics reviewer;
        # they are a formula regression, not an experimental alpha target.
        with localcontext() as ctx:
            ctx.prec = 80
            pi = energy.core.mathematical_pi()
            branch = energy.book_source_branch(pi)
            eta = pi/(pi**4+4).sqrt().sqrt()
            self.assertEqual(branch["eta"], eta)
            self.assertEqual(branch["eta11"], pi/(pi**4+5).sqrt().sqrt())
            self.assertEqual(branch["eta12"], pi/(pi**4+6).sqrt().sqrt())
            self.assertEqual(branch["vartheta"], 5*eta+2*eta.sqrt()+1)
            self.assertLess(abs(1/branch["small_beta"]-D("137.0359609951515777422060897")), D("1e-25"))

    def test_precision_convergence(self):
        low, high = energy.build_report(80), energy.build_report(120)
        with localcontext() as ctx:
            ctx.prec = 140
            for a, b in zip(low["fixed_beta_examples"], high["fixed_beta_examples"]):
                for key in a:
                    self.assertLess(abs(D(a[key])-D(b[key])), D("1e-70"))
            for key in low["book_small_branch_ratios"]:
                self.assertLess(abs(D(low["book_small_branch_ratios"][key])-D(high["book_small_branch_ratios"][key])), D("1e-70"))


if __name__ == "__main__":
    unittest.main()

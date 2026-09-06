"""Independent algebraic regressions for the declared ring diagnostic."""

import sys
import unittest
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"scripts"))
import audit_wave_closure as wave


class WaveClosureTests(unittest.TestCase):
    def test_zero_and_signed_modes(self):
        zero = wave.scalar_mode(0)
        self.assertTrue(zero["constant_spatial_mode"])
        self.assertIsNone(zero["wavelength_over_circumference"])
        for n in (-2, -1, 1, 2):
            row = wave.scalar_mode(n)
            self.assertEqual(row["angular_laplacian_eigenvalue"], n*n)
            self.assertEqual(row["wavelength_over_circumference"], D(1)/abs(n))
            self.assertEqual(row["travelling_angular_generator_over_hbar"], n)
            self.assertEqual(row["balanced_standing_generator_mean_over_hbar"], 0)
            self.assertEqual(row["balanced_standing_generator_square_over_hbar2"], n*n)

    def test_mode_type_and_finite_wavelength_scope(self):
        for n in (True, D(1), 1.0, "1"):
            with self.assertRaises(ValueError):
                wave.scalar_mode(n)
        with self.assertRaises(ValueError):
            wave.wave_ratios(D("0.6"), D(1), 0)

    def test_independent_rational_dimension_cancellation(self):
        # Synthetic positive dimensional scales; no measured inputs.
        pi, hbar, mass, c, eps0 = map(F, (3, 7, 5, 11, 2))
        s = F(4, 5)
        for mode, zeta, f in ((1, F(1), F(3, 5)), (2, F(1), F(3, 5)),
                               (1, F(5, 3), F(3, 5)), (3, F(5, 3), F(1, 5))):
            wavelength = zeta*2*pi*hbar/(mass*c)
            radius = mode*wavelength/(2*pi)
            balance_energy = f*mass*c*c
            charge_term = 4*pi*eps0*radius*s*balance_energy
            k = charge_term/(4*pi*eps0*hbar*c)
            self.assertEqual(k, mode*zeta*f*s)

    def test_exact_rational_phase_examples(self):
        first = wave.wave_ratios(D("0.6"), D(1), 1)
        second = wave.wave_ratios(D("0.6"), D(1), -2)
        self.assertEqual(first["K_pc"], D("0.48"))
        self.assertEqual(first["K_T_comparator"], D("0.16"))
        self.assertEqual(second["K_pc"], D("0.96"))
        self.assertEqual(second["R_over_hbar_mc"], 2)
        self.assertEqual(first["component_pwave_over_mc"], 1)
        self.assertEqual(first["corpuscular_p_over_mc"], D("0.6"))
        compatible = wave.wave_ratios(D("0.5"), D(2))
        self.assertEqual(compatible["component_pwave_over_corpuscular_p"], 1)

    def test_exact_constant_phase_branches(self):
        for k, n, zeta in ((D("0.48"), 1, D(1)), (D("0.96"), -2, D(1)),
                           (D("0.96"), 1, D(2))):
            row = wave.constant_phase_branches(k, n, zeta)
            self.assertEqual(row["small_beta"], D("0.6"))
            self.assertEqual(row["large_beta"], D("0.8"))
        for precision in (40, 50, 80, 120, 200):
            with localcontext() as ctx:
                ctx.prec = precision
                for k, n, zeta in ((D("0.5"), 1, D(1)), (D(2), -2, D(2))):
                    row = wave.constant_phase_branches(k, n, zeta)
                    self.assertEqual(row["small_beta"], row["large_beta"])
                    self.assertEqual(row["small_beta"], D("0.5").sqrt())

    def test_same_wave_pc_exact_and_domains(self):
        self.assertEqual(wave.same_wave_pc_branch(D("0.8"))["beta"], D("0.6"))
        self.assertEqual(wave.same_wave_pc_branch(D("1.6"), -2)["beta"], D("0.6"))
        for k in (D(0), D(1), D(-1), D("NaN"), D("Infinity")):
            with self.assertRaises(ValueError):
                wave.same_wave_pc_branch(k)

    def test_invalid_positive_parameters_and_branches(self):
        for bad in (D(0), D(-1), D("NaN"), D("Infinity"), 1.0):
            with self.assertRaises(ValueError):
                wave.wave_ratios(D("0.6"), bad)
        with self.assertRaises(ValueError):
            wave.constant_phase_branches(D("0.5001"))
        with self.assertRaises(ValueError):
            wave.correction_family(D("0.1"), D("0.01"), D(1), D(0))

    def test_precision_loss_rejected(self):
        with localcontext() as ctx:
            ctx.prec = 40
            with self.assertRaises(ArithmeticError):
                wave.same_wave_pc_branch(D("1e-50"))
            with self.assertRaises(ArithmeticError):
                wave.constant_phase_branches(D("1e-50"))

    def test_proportionality_degeneracy_not_pure_y_multiplier(self):
        first = wave.correction_family(D("0.1"), D("0.01"), D(1), D(1))
        second = wave.correction_family(D("0.1"), D("0.01"), D(2), D("0.5"))
        self.assertEqual(first["K"], second["K"])
        self.assertEqual(first["K"], D("0.099"))
        third = wave.correction_family(D("0.1"), D("0.01"), D(1), D(2))
        self.assertEqual(third["K"], D("0.098"))
        self.assertNotEqual(third["K"], 2*first["K"])

    def test_exact_domain_not_rounded_onto_boundary(self):
        with localcontext() as ctx:
            ctx.prec = 40
            with self.assertRaises(ValueError):
                wave.constant_phase_branches(D("0.5"+"0"*80+"1"))
            with self.assertRaises(ArithmeticError):
                wave.constant_phase_branches(D("0.4"+"9"*80))
            with self.assertRaises(ValueError):
                wave.same_wave_pc_branch(D("1."+"0"*80+"1"))
            with self.assertRaises(ArithmeticError):
                wave.same_wave_pc_branch(D("0."+"9"*80))

    def test_report_residuals_and_no_fits(self):
        with localcontext() as ctx:
            ctx.prec = 80
            report = wave.build_report()
            self.assertEqual(report["modern_reference_inputs"], [])
            self.assertFalse(report["target_fitting"])
            for row in report["constant_c_phase_forward_diagnostics"]:
                for key in ("small_beta", "large_beta"):
                    beta, n, k = D(row[key]), row["n"], D(row["K"])
                    residual = n*beta*((1-beta)*(1+beta)).sqrt()-k
                    self.assertLess(abs(residual), D("1e-73"))
            row = report["same_wave_pc_forward_diagnostic"]
            self.assertLess(abs(((1-D(row["beta"]))*(1+D(row["beta"]))).sqrt()-D(row["K"])), D("1e-73"))
            ks = [row["K"] for row in report["proportionality_degeneracy"]]
            self.assertEqual(ks[0], ks[1])
            self.assertEqual(ks[0], ks[2])

    def test_book_reduction_and_precision_convergence(self):
        low, high = wave.build_report(80), wave.build_report(120)
        with localcontext() as ctx:
            ctx.prec = 140
            self.assertEqual(low["constant_c_phase_forward_diagnostics"][0]["small_beta"], low["book_Y3_one_profile"]["small_beta"])
            for a, b in zip(low["constant_c_phase_forward_diagnostics"], high["constant_c_phase_forward_diagnostics"]):
                for key in ("small_beta", "large_beta", "inverse_small_beta"):
                    self.assertLess(abs(D(a[key])-D(b[key])), D("1e-70"))
            self.assertLess(abs(D(low["same_wave_pc_forward_diagnostic"]["beta"])-D(high["same_wave_pc_forward_diagnostic"]["beta"])), D("1e-70"))

    def test_precision_bounds(self):
        for precision in (39, 201, True, 80.0):
            with self.assertRaises(ValueError):
                wave.build_report(precision)
        for precision in (40, 200):
            self.assertEqual(wave.build_report(precision)["precision"], precision)


if __name__ == "__main__":
    unittest.main()

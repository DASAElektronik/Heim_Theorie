"""Independent algebraic invariants and printed-output checks for H015 GINIT."""
from decimal import Decimal as D, localcontext
import json
import unittest
from scripts.audit_historical_constants import INPUT, audit, initialize


class HistoricalConstantsTests(unittest.TestCase):
    def setUp(self):
        self.tokens = json.loads(INPUT.read_text(encoding="utf-8"))["inputs"]

    def test_printed_output_and_precision(self):
        result = audit(60)
        self.assertEqual(result, audit(90))
        self.assertEqual(len(result["rows"]), 17)
        self.assertTrue(result["all_rows_match"])

    def test_charge_and_scale_squared_identities(self):
        with localcontext() as ctx:
            ctx.prec = 60
            v = initialize(self.tokens)
            charge = v["EQ"]**2*8*v["PI"]**4*v["RG"]/(9*v["THETA"]*v["HQ"])
            scale = v["AMU"]**6*3*v["GAM"]*v["C"]**3*v["S0"]**4/(v["PI"]**D("3.5")*v["HQ"]**5)
            self.assertLess(abs(charge-1), D("1e-55"))
            self.assertLess(abs(scale-1), D("1e-55"))

    def test_couplings_are_inputs_not_solved_outputs(self):
        original = initialize(self.tokens)
        changed = initialize(self.tokens | {"ALFA_inverse": "2Q0", "BETA_inverse": "4Q0"})
        self.assertEqual(changed["ALFA"], D(".5"))
        self.assertEqual(changed["BETA"], D(".25"))
        for name in ["ETA", "THETA", "EQ", "AMU", "ALFP", "ALFM"]:
            self.assertEqual(original[name], changed[name])

    def test_mass_factors_match_97_relation(self):
        with localcontext() as ctx:
            ctx.prec = 60
            v = initialize(self.tokens)
            self.assertLess(abs(v["ETA"]**2*(1+v["ALFP"])-v["ETA"]*(1+v["ALFM"])), D("1e-55"))


if __name__ == "__main__":
    unittest.main()

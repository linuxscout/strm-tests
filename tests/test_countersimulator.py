import unittest
from strmquiz.sequentiel.countersimulator import CounterSimulator


class TestCounterSimulator(unittest.TestCase):

    def setUp(self):
        # common test setup
        self.inputs = ["E"]
        self.outputs = ["Q0", "Q1", "Q2"]
        self.flip_types = ["D", "JK", "T"]

        self.sim = CounterSimulator(inputs=self.inputs, outputs=self.outputs, flip_types=self.flip_types)

        # initial signals
        self.init_signals = {
            "E": [1, -6],
            "Q0": [1, 0],
            "Q1": [1, 1],
            "Q2": [1, 2],
        }

    def test_inverse(self):
        self.assertEqual(self.sim.chrono.inverse([1, -2, 3]), [-1, 2, -3])


    def test_signal_mapping_d(self):
        # Q0 is D flip-flop, should take E as input
        mapping = self.sim.signal_map["Q0"]
        self.assertIn("D", mapping["inputs"])
        self.assertEqual(mapping["inputs"]["D"], "E")

    def test_signal_mapping_jk(self):
        # Q1 is JK, should take Q0 and Q0'
        mapping = self.sim.signal_map["Q1"]
        self.assertIn("J", mapping["inputs"])
        self.assertIn("K", mapping["inputs"])
        self.assertEqual(mapping["inputs"]["J"], "Q0")
        self.assertEqual(mapping["inputs"]["K"], "Q0'")

    def test_signal_mapping_t(self):
        # Q2 is T flip-flop, should take Q1
        mapping = self.sim.signal_map["Q2"]
        self.assertIn("T", mapping["inputs"])
        self.assertEqual(mapping["inputs"]["T"], "Q1")

    def test_resolve_counter(self):
        tmp_signals = dict(self.init_signals)  # copy
        result = self.sim.resolve_counter(tmp_signals)
        # Check that outputs include inverted signals
        for q in self.outputs:
            self.assertIn(q, result)
            self.assertIn(q + "'", result)

    def test_counter_new_flip_flop(self):
        # Add a custom SR flip-flop
        CounterSimulator.register_flip_flop(
            "SR", lambda prev, first: {"S": prev, "R": first}
        )
        sim2 = CounterSimulator(["E"], ["Q0"], ["SR"])
        mapping = sim2.signal_map["Q0"]
        self.assertIn("S", mapping["inputs"])
        self.assertIn("R", mapping["inputs"])


if __name__ == "__main__":
    unittest.main()

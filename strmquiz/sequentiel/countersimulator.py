import logging
from typing import Dict, List, Any, Callable

from . import chronograms
from .seqcircuitsimulator import SeqCircuitSimulator


class CounterSimulator(SeqCircuitSimulator):
    """
    A simulator for counters composed of multiple flip-flops.
    Extensible with new flip-flop types via `counter_flip_flop`.
    """

    # Registry of flip-flop input mapping rules
    flip_flop_registry: Dict[str, Callable[[str, str], Dict[str, str]]] = {}

    def __init__(
        self,
        inputs: List[str],
        outputs: List[str],
        flip_types: List[str],
        circuit_type: str = "counter",
        counter_type: str = "",
    ):
        self.counter_type = counter_type
        self.logger = logging.getLogger(self.__class__.__name__)
        super().__init__(
            inputs=inputs,
            outputs=outputs,
            flip_types=flip_types,
            circuit_type=circuit_type,
        )

        # self.inputs = inputs
        # self.outputs = outputs
        # self.flip_types = flip_types
        # self.signal_map = self._map_signals()
        # logger.debug("Signal map %s"%str(self.signal_map))
        # self.chrono = chronograms.Chronograms();
        # self.chrono.set_synch_type("rising")

    # ---------- Internal mapping ----------
    def _map_signals(self, shift: str = "right") -> Dict[str, Dict[str, Any]]:
        """Map signals for each flip-flop output based on its type."""
        tmp_outputs = self.outputs
        self.logger.debug("Counter type %s" % self.counter_type)
        if self.counter_type == "shift-left":
            tmp_outputs = list(reversed(tmp_outputs))
        signal_map = {}
        inverse = self.counter_type == "shift-left"
        signal_map = {}
        for i, q in enumerate(tmp_outputs):
            flip_type = self.flip_types[i]
            prev_out = tmp_outputs[i - 1] if i else self.inputs[0]

            if flip_type not in self.flip_flop_registry:
                raise ValueError(f"Unknown flip-flop type: {flip_type}")

            inputs_map = self.flip_flop_registry[flip_type](prev_out, self.inputs[0])

            signal_map[q] = {"inputs": inputs_map, "outputs": {"Q": q}}
        return signal_map

    def resolve(
        self,
        flip_type: str,
        signal_dict: Dict[str, List[int]],
        inputs: List[str],
        index: int,
    ) -> List[int]:
        """Dummy resolve: multiply Q signal by index for testing."""
        clock_shift = []
        edge = "rising"
        if index:  # avoid first case
            edge = "falling" if self.counter_type == "up" else "rising"
            self.chrono.set_synch_type(edge)
            clock_shift = [-1] if self.counter_type == "up" else []
        signal_result = self.chrono.resolve(
            flip_type=flip_type,
            signals=signal_dict,
            period=2 ** (index + 1),
            inputs=inputs,
        )
        # TODO: change clock signal to chronogram
        signal_result = clock_shift + signal_result
        return signal_result

        # return [x * index for x in signal_dict["Q"] * 6]

    # ---------- Simulation ----------
    def resolve_counter(
        self, tmp_signals: Dict[str, List[int]], signal_length: int = 10
    ) -> Dict[str, List[int]]:
        """Resolve signals for a counter given initial signals and flip-flop mapping."""
        self.logger.info("Resolving counter with outputs: %s", self.outputs)

        inverse = self.counter_type == "shift-left"
        for i, qi in enumerate(self.outputs if not inverse else reversed(self.outputs)):
            # for i, qi in enumerate(self.outputs):
            sig_list = tmp_signals.get(qi, [])
            self.logger.debug("Processing %s: %s", qi, sig_list)
            self.logger.debug("Signal map: %s", self.signal_map[qi])

            init_signal = {}
            f_inputs = self.signal_map[qi].get("inputs", {})

            for flip_input_key, sig_key in f_inputs.items():
                if sig_key.endswith("'"):
                    base_key = sig_key[:-1]
                    init_signal[flip_input_key] = self.chrono.inverse(
                        tmp_signals[base_key]
                    )
                else:
                    init_signal[flip_input_key] = tmp_signals[sig_key]

            # init_signal["Q"] = tmp_signals[qi]
            self.logger.debug("INIT_signal %d: %s", i, init_signal)

            new_signal = self.resolve(
                flip_type=self.flip_types[i],
                signal_dict=init_signal,
                inputs=list(f_inputs.keys()),
                index=i,
            )
            self.logger.debug(f" Signal before trunct '{qi}':{new_signal}")
            new_signal = self.chrono.truncate_signal(new_signal, size=signal_length)
            self.logger.debug(f" Signal after trunct '{qi}':{new_signal}")
            tmp_signals[qi] = new_signal
            tmp_signals[qi + "'"] = self.chrono.inverse(new_signal)

            self.logger.debug("New signal for %s: %s", qi, new_signal)

        return tmp_signals


# ==== Counter built-in flip-flops ====
CounterSimulator.register_flip_flop("D", lambda prev, first: {"D": prev})
CounterSimulator.register_flip_flop("JK", lambda prev, first: {"J": "Vcc", "K": "Vcc"})
CounterSimulator.register_flip_flop(
    "T", lambda prev, first: {"T": prev}
)  # example extension


# ==== Example Usage ====
if __name__ == "__main__":
    import pprint

    outputs = ["Q0", "Q1", "Q2", "Q3", "Q4"]
    inputs = ["E"]
    flip_types = ["D", "JK", "T", "JK", "D"]  # notice: includes "T"

    sim = CounterSimulator(inputs, outputs, flip_types)

    init_signals = {
        "E": [1, -6],
        "Q0": [1, 0],
        "Q1": [1, 1],
        "Q2": [1, 2],
        "Q3": [1, 3],
        "Q4": [1, 4],
    }

    final_signals = sim.resolve_counter(init_signals)

    sim.logger.info("Final TMP signals:\n%s", pprint.pformat(final_signals))

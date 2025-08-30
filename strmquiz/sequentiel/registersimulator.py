import logging
from typing import Dict, List, Any, Callable

from . import chronograms
from .seqcircuitsimulator import SeqCircuitSimulator
# --- Configure logging ---
logging.basicConfig(
    level=logging.DEBUG,  # change to INFO or WARNING in production
    format="%(levelname)s:%(name)s:%(message)s"
)
logger = logging.getLogger(__name__)

class RegisterSimulator(SeqCircuitSimulator):
    """
    A simulator for registers composed of multiple flip-flops.
    Extensible with new flip-flop types via `register_flip_flop`.
    """

    # Registry of flip-flop input mapping rules
    flip_flop_registry: Dict[str, Callable[[str, str], Dict[str, str]]] = {}

    def __init__(self, inputs: List[str], outputs: List[str], flip_types: List[str], circuit_type:str="register", register_type:str=''):
        self.register_type = register_type
        super().__init__(inputs= inputs, outputs=outputs, flip_types=flip_types, circuit_type=circuit_type)
        # self.inputs = inputs
        # self.outputs = outputs
        # self.flip_types = flip_types
        # self.signal_map = self._map_signals()
        # logger.debug("Signal map %s"%str(self.signal_map))
        # self.chrono = chronograms.Chronograms();
        # self.chrono.set_synch_type("rising")


    # ---------- Internal mapping ----------
    def _map_signals(self, shift:str="right") -> Dict[str, Dict[str, Any]]:
        """Map signals for each flip-flop output based on its type."""
        tmp_outputs = self.outputs
        logger.debug("Register type %s"%self.register_type)
        if self.register_type == "shift-left":
            tmp_outputs = list(reversed(tmp_outputs))
        signal_map = {}
        inverse = self.register_type == "shift-left"
        signal_map = {}
        for i, q in enumerate(tmp_outputs):
            flip_type = self.flip_types[i]
            prev_out = tmp_outputs[i - 1] if i else self.inputs[0]

            if flip_type not in self.flip_flop_registry:
                raise ValueError(f"Unknown flip-flop type: {flip_type}")

            inputs_map = self.flip_flop_registry[flip_type](prev_out, self.inputs[0])

            signal_map[q] = {
                "inputs": inputs_map,
                "outputs": {"Q": q}
            }
        return signal_map

    # ---------- Simulation ----------
    def resolve_register(self, tmp_signals: Dict[str, List[int]], signal_length:int=10) -> Dict[str, List[int]]:
        """Resolve signals for a register given initial signals and flip-flop mapping."""
        logger.info("Resolving register with outputs: %s", self.outputs)

        inverse = self.register_type == "shift-left"
        for i, qi in enumerate(self.outputs if not inverse else reversed(self.outputs)):
        # for i, qi in enumerate(self.outputs):
            sig_list = tmp_signals.get(qi, [])
            logger.debug("Processing %s: %s", qi, sig_list)
            logger.debug("Signal map: %s", self.signal_map[qi])

            init_signal = {}
            f_inputs = self.signal_map[qi].get("inputs", {})

            for flip_input_key, sig_key in f_inputs.items():
                if sig_key.endswith("'"):
                    base_key = sig_key[:-1]
                    init_signal[flip_input_key] = self.chrono.inverse(tmp_signals[base_key])
                else:
                    init_signal[flip_input_key] = tmp_signals[sig_key]

            # init_signal["Q"] = tmp_signals[qi]
            logger.debug("INIT_signal %d: %s", i, init_signal)

            new_signal = self.resolve(flip_type=self.flip_types[i], signal_dict=init_signal, inputs=list(f_inputs.keys()), index=i)
            new_signal = self.chrono.truncate_signal(new_signal, size=signal_length)
            tmp_signals[qi] = new_signal
            tmp_signals[qi + "'"] = self.chrono.inverse(new_signal)

            logger.debug("New signal for %s: %s", qi, new_signal)

        return tmp_signals


# ==== Register built-in flip-flops ====
RegisterSimulator.register_flip_flop("D", lambda prev, first: {"D": prev})
RegisterSimulator.register_flip_flop("JK", lambda prev, first: {"J": prev, "K": prev + "'"})
RegisterSimulator.register_flip_flop("T", lambda prev, first: {"T": prev})  # example extension


# ==== Example Usage ====
if __name__ == "__main__":
    import pprint
    outputs = ["Q0", "Q1", "Q2", "Q3", "Q4"]
    inputs = ["E"]
    flip_types = ["D", "JK", "T", "JK", "D"]  # notice: includes "T"

    sim = RegisterSimulator(inputs, outputs, flip_types)

    init_signals = {
        "E": [1, -6],
        "Q0": [1, 0],
        "Q1": [1, 1],
        "Q2": [1, 2],
        "Q3": [1, 3],
        "Q4": [1, 4],
    }

    final_signals = sim.resolve_register(init_signals)

    logger.info("Final TMP signals:\n%s", pprint.pformat(final_signals))

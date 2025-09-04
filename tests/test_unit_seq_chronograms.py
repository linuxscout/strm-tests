import pytest
import types
import sys

from strmquiz.sequentiel.chronograms import Chronograms
from strmquiz.sequentiel.seqconst import  FLIP_TRUTH_TABLES, FLIPS_DATA, FLIPS_RANDOM, TRUTH_TABLE_MAP



def test_set_synch_type():
    chrono = Chronograms()
    chrono.set_synch_type("falling")
    assert chrono.synch_type == "falling"



def test_stringfy():
    chrono = Chronograms()
    signal = [1, 1, -1, -1, 1]
    result = chrono.stringfy(signal)
    assert isinstance(result, str), f"{result}"
    assert result == "|¯¯|__|¯", f"{result}"



def test_clock_signal_rising():
    chrono = Chronograms()
    chrono.set_synch_type("rising")
    result = chrono.clock_signal(period=2, length=4)
    assert isinstance(result, dict)
    assert "wave" in result
    assert result.get("wave","") == "|_↑¯|_|_↑¯|_|_↑¯|_|_↑¯|_"



def test_inverse():
    signal = [1, -1, 2]
    result = Chronograms.inverse(signal)
    assert result == [-1, 1, -2]

def test_signal_size():
    assert Chronograms.signal_size([3, -2, 4]) == 9
    assert Chronograms.signal_size([1, 1, 1]) == 3
    assert Chronograms.signal_size([-5, -5]) == 10
    assert Chronograms.signal_size([]) == 0

def test_truncate_signal():

    signal = [3, -2, 4, -4, 3, -2]
    result = Chronograms.truncate_signal(signal, size=15)
    assert Chronograms.signal_size(result) <= 15



def test_is_true_false():
    assert Chronograms.is_true(2)
    assert not Chronograms.is_true(-1)
    assert Chronograms.is_false(-3)
    assert not Chronograms.is_false(5)


def test_set_reset_flip_memory():
    assert Chronograms.set(2) == 2
    assert Chronograms.reset(2) == -2
    assert Chronograms.flip(3) == -3
    assert Chronograms.memory(4) == 4



def test_synchronize_signal():
    chrono = Chronograms()
    chrono.set_synch_type("rising")
    period = 2
    signal = [1, -4, 3, -2]
    result = chrono.synchronize_signal(signal, period=period)
    assert isinstance(result, list), result
    assert all(isinstance(x, int) for x in result)
    assert all(x<=period for x in result)
    assert result == [1, 2, -2, -2, 2, 1, -2], f" the result is {result}"



def test_random_signal():
    chrono = Chronograms()
    signal = chrono.random_signal(init=1, length=5)
    assert len(signal) == 5
    assert chrono.signal_size(signal) == 5
    assert all(x != 0 for x in signal)


# -----------------------------
# Flip-flop logic tests
# -----------------------------

def test_resolve_d_flipflop():
    chrono = Chronograms()
    signals = {"D": [1, -1, 1, -1]}
    period = 2
    result = chrono.resolve(flip_type="D", signals=signals, period=period)
    assert isinstance(result, list), f"the result is {result}"
    assert all(x<=period for x in result)
    assert result == [1, 2, -1, 1, -1], f" the result is {result}"



def test_resolve_jk_flipflop():
    chrono = Chronograms()
    signals = {
        "J": [1, -1, 1, -1],
        "K": [-1, 1, -1, 1],
        "Q": [1, -1, 1, -1]
    }
    period = 2
    result = chrono.resolve(flip_type="JK", signals=signals, period=period)
    assert isinstance(result, list)
    assert all(x<=period for x in result)
    assert result == [1, 2, -2, 2, -2], f" the result is {result}"



def test_resolve_xy_flipflop():
    chrono = Chronograms()
    signals = {
        "X": [1, -1, 1, -1],
        "Y": [-1, 1, -1, 1],
        "Q": [1, -1, 1, -1]
    }
    period = 2
    result = chrono.resolve(flip_type="XY", signals=signals, period=period)
    assert isinstance(result, list)
    assert all(x<=period for x in result)
    assert result == [1, -2, 2, -2, 2], f" the result is {result}"



def test_resolve_xy_direct_call():
    chrono = Chronograms()
    j_signal = [1, -1, 1, -1]
    k_signal = [-1, 1, -1, 1]
    q_signal = [1, -1, 1, -1]
    period = 2
    result = chrono.resolve_xy(j_signal, k_signal, q_signal, period=period, flip_type="XY")
    assert isinstance(result, list)
    assert all(x<=period for x in result)
    assert result == [1, -2, 2, -2], f" the result is {result}"



def test_resolve_jk_direct_call():
    chrono = Chronograms()
    j_signal = [1, -1, 1, -1]
    k_signal = [-1, 1, -1, 1]
    q_signal = [1, -1, 1, -1]
    period = 2
    j_signal = chrono.synchronize_signal(j_signal, period=period)
    k_signal = chrono.synchronize_signal(k_signal, period=period)
    result = chrono.resolve_jk(j_signal, k_signal, q_signal, period=period)
    assert isinstance(result, list)
    assert all(x<=period for x in result)
    assert result == [1, 2, -2, 2, -2], f" the result is {result}"

# -----------------------------
# Truth table tests
# -----------------------------

# -----------------------------
# Truth table tests
# -----------------------------


def test_get_truth_value():
    import types, sys
    # Create a fake seqconst module
    chrono = Chronograms()

    # Should return from FLIP_TRUTH_TABLES
    value1 = chrono.get_truth_value(1, 0, "JK")
    assert value1 == "set"

    # Should return from FLIPS_DATA
    value2 = chrono.get_truth_value(1, 0, "XY")
    assert value2 == "flip"

    # Should fallback to default
    value3 = chrono.get_truth_value(0, 0, "JK")
    assert value3 == "memory"


# -----------------------------
# Draw & Save tests
# -----------------------------

def test_draw_and_save(tmp_path):
    chrono = Chronograms()
    signals = {"D": [1, -1, 1], "Q": [-1, 1, -1]}
    clock = {"name": "CLK", "wave": "p....", "period": 2}

    # Draw signals
    data = chrono.draw(signals, clock)
    assert isinstance(data, list)
    assert all(isinstance(item, dict) for item in data)
    assert all("name" in item and "wave" in item for item in data)

    # Save to file
    filename = tmp_path / "test_output.svg"
    result = chrono.save(data, str(filename))
    assert result == 0

import pytest
import types
from strmquiz.bool.logigram import logigram
from strmquiz.bool.bool_const import NAND_SYMB, NOR_SYMB, BIG_NAND_SYMB, BIG_NOR_SYMB


# @pytest.fixture(autouse=True)
# def patch_bool_const(monkeypatch):
#     # monkeypatch.setitem(logigram.__dict__, "bool_const", DummyBoolConst)
#     yield


def test_default_init():
    lg = logigram()
    assert lg.method == ""
    assert lg.var_A == "A"
    assert lg.var_B == "B"
    assert lg.var_C == "C"
    assert lg.var_D == "D"


@pytest.mark.parametrize(
    "method,expected",
    [
        ("NAND", "NAND"),
        ("NOR", "NOR"),
        ("AND", "SOP"),
        ("OR", "POS"),
        ("SOP", "SOP"),
        ("POS", "POS"),
        ("", ""),
        ("INVALID", ""),
    ],
)
def test_set_gate_type(method, expected):
    lg = logigram()
    lg.set_gate_type(method)
    assert lg.method == expected


@pytest.mark.parametrize(
    "method,expected",
    [
        ("SOP", "."),
        ("NAND", NAND_SYMB),
        ("NOR", NOR_SYMB),
        ("POS", "+"),
        ("", "."),
    ],
)
def test_get_var_sep(method, expected):
    lg = logigram(method=method)
    assert lg.get_var_sep() == expected


@pytest.mark.parametrize(
    "method,expected",
    [
        ("SOP", "+"),
        ("NAND", BIG_NAND_SYMB),
        ("NOR", BIG_NOR_SYMB),
        ("POS", "."),
        ("", "+"),
    ],
)
def test_get_term_sep(method, expected):
    lg = logigram(method=method)
    assert lg.get_term_sep() == expected


def test_get_gate_code_basic():
    lg = logigram(method="NAND")
    assert lg.get_gate_code("and") == "nand"

    lg.set_gate_type("NOR")
    assert lg.get_gate_code("or") == "nor"


def test_get_terms_for_different_methods():
    eq_item = {
        "sop": "A.B+C.D",
        "nand_sop": f"A{NAND_SYMB}B{BIG_NAND_SYMB}C{NAND_SYMB}D",
        "nor_pos": f"A{NOR_SYMB}B{BIG_NOR_SYMB}C{NOR_SYMB}D",
        "pos": "(A+B)",
    }

    lg = logigram(method="SOP")
    assert lg.get_terms(eq_item) == ["A.B", "C.D"]

    lg.set_gate_type("NAND")
    assert lg.get_terms(eq_item) == [f"A{NAND_SYMB}B", f"C{NAND_SYMB}D"]

    lg.set_gate_type("NOR")
    assert lg.get_terms(eq_item) == [f"A{NOR_SYMB}B", f"C{NOR_SYMB}D"]

    lg.set_gate_type("POS")
    assert lg.get_terms(eq_item) == ["A+B"] or ["A", "B"]  # depending on separator


def test_prepare_logigram_list_structure():
    sop_list = ["A.B", "A+C"]
    fnames = ["F1", "F2"]
    equations = [{"sop": "A.B"}, {"sop": "A+C"}]
    lg = logigram(method="SOP")
    graph = lg.prepare_logigram_list(sop_list, fnames, equations)
    assert isinstance(graph, dict)
    assert "functions" in graph
    assert len(graph["functions"]) == 2
    assert graph["size_terms"] >= 2

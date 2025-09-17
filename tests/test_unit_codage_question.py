import random

import pytest

from strmquiz.codage.question_codage import questionGenerator


@pytest.fixture
def qg():
    return questionGenerator()


# ----------------------------
# Deterministic methods
# ----------------------------
def test_int2base_and_base2int(qg):
    for base in [2, 8, 10, 16, 36]:
        for n in [0, 1, 5, 42, 255, 1024]:
            s = qg.int2base(n, base)
            back = qg.base2int(s, base)
            assert back == n


def test_dec_to_bcd_and_back(qg):
    n = 59
    bcd = qg.dec_to_bcd(n)
    assert bcd == "0101 1001"
    assert qg.bcd_to_dec(bcd) == n


def test_dec_to_excess3_and_back(qg):
    n = 59
    ex3 = qg.dec_to_excess3(n)
    assert ex3 == "1000 1100"
    assert qg.excess3_to_dec(ex3) == n


def test_to_symbol_and_from_symbol(qg):
    for i in range(36):
        sym = qg.to_symbol(i)
        assert qg.from_symbol(sym) == i
    with pytest.raises(ValueError):
        qg.from_symbol("!")


def test_number_to_digits(qg):
    digits = qg.number_to_digits("1A", 16)
    assert digits == [{"symbol": "1", "value": 1}, {"symbol": "A", "value": 10}]
    with pytest.raises(ValueError):
        qg.number_to_digits("1G", 16)


def test_binary_gray_conversion(qg):
    binary = "1011"
    gray = qg.binary_to_gray(binary)
    assert gray == "1110"
    back = qg.gray_to_binary(gray)
    assert back == binary


def test_gray_sequence(qg):
    seq = qg.gray_sequence_from_binary("0000", 4)
    assert seq == ["0000", "0001", "0011", "0010"]


def test_gray_explain(qg):
    res = qg.gray_explain("1011", "1110")
    assert "Copy first bit" in res["steps_bin2gray"][0]
    assert "Copy first bit" in res["steps_gray2bin"][0]


# ----------------------------
# Random-based methods (with monkeypatch)
# ----------------------------


def test_numeral_system(monkeypatch, qg):
    monkeypatch.setattr(random, "choice", lambda seq: seq[0])
    monkeypatch.setattr(random, "randint", lambda a, b: 42)
    res = qg.numeral_system()
    assert res["question"].startswith("(")
    assert "........" in res["question"]


def test_dec2x(monkeypatch, qg):
    monkeypatch.setattr(random, "randint", lambda a, b: 100)
    res = qg.dec2x(8, method=False)
    assert isinstance(res, str)
    method_res = qg.dec2x(8, method=True)
    assert " = " in method_res


def test_x2dec(monkeypatch, qg):
    monkeypatch.setattr(random, "randint", lambda a, b: 100)
    res = qg.x2dec(8, method=False)
    assert isinstance(res, str)
    method_res = qg.x2dec(8, method=True)
    assert " = " in method_res


def test_bin2(monkeypatch, qg):
    monkeypatch.setattr(random, "randint", lambda a, b: 20)
    nb, res = qg.bin2(8, method=False)
    assert isinstance(nb, str)
    assert isinstance(res, str)
    method_res = qg.bin2(8, method=True)
    assert "|" in method_res


def test_rand_arithm(monkeypatch, qg):
    monkeypatch.setattr(random, "choice", lambda seq: seq[0])
    monkeypatch.setattr(random, "randint", lambda a, b: 5)
    res = qg.rand_arithm()
    assert "question" in res
    assert "reponse" in res


def test_comp_one(monkeypatch, qg):
    monkeypatch.setattr(random, "randint", lambda a, b: 5)
    n, a, b, e = qg.comp_one(8, method=False)
    assert isinstance(n, int)
    tex = qg.comp_one(8, method=True)
    assert "cp1" in tex or "cp2" in tex


def test_intervalle(monkeypatch, qg):
    monkeypatch.setattr(random, "randint", lambda a, b: 4)
    n = qg.intervalle()
    assert n == 4
    text = qg.intervalle(4, method=True)
    assert "Positifs" in text


def test_ascii(qg):
    res = qg.ascii("AB", method=True)
    assert "A" in res and "B" in res
    compact = qg.ascii("AB", method=False)
    assert "0x41" in compact and "0x42" in compact


if __name__ == "__main__":
    pytest.main()

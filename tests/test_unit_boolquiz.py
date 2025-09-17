import pytest
from strmquiz.bool.boolquiz import bool_quiz
from strmquiz.bool.bool_const import NOR_SYMB, NAND_SYMB


@pytest.fixture
def bq():
    return bool_quiz()


def test_set_and_reset_vars(bq):
    bq.set_vars(entries=["X", "Y"], outputs=["Z"])
    assert bq.variables == ["X", "Y"]
    assert bq.vars_outputs == ["Z"]
    bq.reset_vars()
    assert bq.variables == bq.default_vars


def test_set_format(bq):
    bq.set_format("text")
    assert bq.format == "text"


def test_normalize_sop(bq):
    expr = "(A & B) | ~C"
    norm = bq.normalize(expr, mode=True)
    assert "+" in norm
    assert "." in norm or "C'" in norm


def test_normalize_pos(bq):
    expr = "(A | B) & ~C"
    norm = bq.normalize(expr, mode=False)
    assert "(" in norm
    assert ")" in norm


def test_simplify_and_form_canonique(bq):
    minterms = [1, 3, 7]
    sop, pos = bq.simplify(minterms)
    assert isinstance(sop, str)
    assert isinstance(pos, str)
    assert ("a'.c.d") in sop
    assert "(d).(a').(b'+c)" == pos
    bq.set_format("text")
    cnf, dnf = bq.form_canonique(minterms)
    assert isinstance(cnf, str)
    assert isinstance(dnf, str)

    assert ("A'.B.C.D") in dnf
    assert ("(A'+B'+C'+D)") in cnf


def test_add_bar(bq):
    bq.set_format("latex")
    assert bq.add_bar("A") == "\\bar A"
    bq.set_format("text")
    assert bq.add_bar("A") == "A'"


def test_minterm_and_maxterm_str(bq):
    s1 = bq.minterm_str(5)
    s2 = bq.maxterm_str(5)
    assert isinstance(s1, str)
    assert isinstance(s2, str)
    assert "A'.B.C'.D" == s1
    assert "(A+B'+C+D')" == s2


def test_draw_map(bq):
    minterms = [1, 3, 7]
    text = bq.draw_map(minterms, latex=False)
    tex = bq.draw_map(minterms, latex=True)
    assert isinstance(text, str)
    assert isinstance(tex, str)
    assert "AB\\CD\t00\t01\t11" in text
    assert "\\begin{karnaugh-map}" in tex


def test_make_nand_and_nor(bq):
    expr = "A.B + C"
    nand_expr = bq.make_nand(expr)
    nor_expr = bq.make_nor("A+B")
    assert isinstance(nand_expr, str)
    assert isinstance(nor_expr, str)
    assert nand_expr != expr or nor_expr != expr
    assert NAND_SYMB in nand_expr
    assert NOR_SYMB in nor_expr


def test_explain_nand_nor(bq):
    expr = "A.B + C"
    nand_steps = bq.explain_nand(expr)
    nor_steps = bq.explain_nor("A+B")
    assert isinstance(nand_steps, list)
    assert isinstance(nor_steps, list)
    assert all(isinstance(step, str) for step in nand_steps)


def test_normalize_latex(bq):
    expr = "A' + B' + C'"
    res = bq.normalize_latex(expr)
    assert "\\bar" in res


def test_rand_exp(bq):
    # random
    exp, minterms = bq.rand_exp()
    assert isinstance(exp, str), f"The result is {exp}"
    assert isinstance(minterms, list), f"The result is {minterms}"

    # not random
    input_minterms = [1, 12, 3, 15]
    exp, minterms = bq.rand_exp(minterms=input_minterms)
    assert isinstance(exp, str), f"The result is {exp}"
    assert isinstance(minterms, list), f"The result is {minterms}"
    assert minterms == input_minterms, f"The result is {minterms}, expr= {exp}"


def test_validate_terms_valid(bq):
    terms = [0, 1, 3, 15]
    result = bq.validate_terms(terms, name="minterms")
    assert result == [0, 1, 3, 15], "The result is {result}"


def test_validate_terms_duplicates_sorted(bq):
    terms = [3, 1, 1, 0, 15]
    result = bq.validate_terms(terms, name="maxterms")
    assert result == [
        0,
        1,
        3,
        15,
    ], "The result is {result}"  # duplicates removed, sorted


def test_validate_terms_non_integer(bq):
    with pytest.raises(TypeError):
        bq.validate_terms([1, "X", 2], name="dontcares")


@pytest.mark.skip(reason="To be implemented manually")
def test_validate_terms_out_of_range(bq):
    with pytest.raises(ValueError):
        bq.validate_terms([0, 5, 16], name="minterms")


def test_validate_terms_without_normalize(bq):
    terms = [3, 1, 1, 0, 15]
    result = bq.validate_terms(terms, name="dontcares", normalize=False)
    assert result == [
        3,
        1,
        1,
        0,
        15,
    ], "The result is {result}"  # unchanged, no sorting/unique


def test_validate_terms_list_valid(bq):
    terms_list = [[0, 1, 2], [3, 5, 7]]
    result = bq.validate_terms_list(terms_list)
    assert result == [[0, 1, 2], [3, 5, 7]]


def test_validate_terms_list_duplicates(bq):
    terms_list = [[3, 1, 1, 0], [15, 10, 10]]
    result = bq.validate_terms_list(terms_list)
    assert result == [[0, 1, 3], [10, 15]]  # normalized, duplicates removed


def test_validate_terms_list_invalid_type(bq):
    terms_list = [[0, "X"], [1, 2]]
    with pytest.raises(TypeError):
        bq.validate_terms_list(terms_list)


def test_validate_terms_list_out_of_range(bq):
    terms_list = [[0, 16], [1, 2]]
    with pytest.raises(ValueError):
        bq.validate_terms_list(terms_list)


def test_validate_terms_list_not_list(bq):
    with pytest.raises(TypeError):
        bq.validate_terms_list("not a list")

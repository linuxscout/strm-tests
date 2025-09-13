
import pytest
from strmquiz.question_builder.boolean_question_builder import BooleanQuestionBuilder


@pytest.fixture
def builder():
    """Fixture to provide a fresh BooleanQuestionBuilder instance."""
    return BooleanQuestionBuilder()

import pytest



def test_init(builder):
    assert builder is not None


def test_prepare_kmap_data(builder):
    result = builder._prepare_kmap_data(minterms=[1, 3], variables=["A", "B", "C", "D"])
    assert isinstance(result, dict)
    assert "minterms" in result, f"the result is {result}"



def test_question_map(builder):
    result = builder.question_map()
    assert isinstance(result, dict)
    assert "data_list" in result, f"the result is {result}"



def test_question_map_for_sop(builder):
    result = builder.question_map_for_sop(nb=1)
    assert isinstance(result, dict)
    assert "data_list" in result, f"the result is {result}"


@pytest.mark.skip(reason="To be implemented manually")
def test_question_funct(builder):
    result = builder.question_funct()
    assert isinstance(result, dict)
    assert "sop_quest" in result, f"the result is {result}"



def test_get_terms(builder):
    expr = "A.B + C.D"
    terms = builder.get_terms(expr, method="sop")
    assert isinstance(terms, list)
    assert terms==[['A', 'B'], ['C', 'D']], f"the result is {terms}"


def test_question_static_funct(builder):
    result = builder.question_static_funct(minterms=[1, 2, 3])
    assert isinstance(result, dict)
    assert "logicdiagramdict" in result, f"the result is {result}"


def test_question_static_nand_exp(builder):
    result = builder.question_static_nand_exp(minterms=[1, 2, 3])
    assert isinstance(result, dict)
    assert "minterms" in result, f"the result is {result}"
    assert result['sop'] == " a'.b'.c + a'.b'.d ", f"the result['sop'] is {result['sop']}"
    assert result['pos'] == "(a').(b').(c+d)", f"the result['pos'] is {result['pos']}"


def test_question_multi_funct(builder):
    result = builder.question_multi_funct(minterms_list=[[1, 2,3]], dont_care_list=[[]])
    assert isinstance(result, dict)
    assert "data_list" in result, f"the result is {result}"
    assert "minterms" in result["data_list"][0], f"the result is {result['data_list']}"
    assert result["data_list"][0]['sop'] == " a'.b'.c + a'.b'.d ", f"the result['sop'] is {result['data_list'][0]['sop']}"
    assert result["data_list"][0]['pos'] == "(a').(b').(c+d)", f"the result['pos'] is {result['data_list'][0]['pos']}"


def test_question_exp(builder):
    # random
    builder.set_random(True)
    result = builder.question_exp()
    assert isinstance(result, dict)
    assert "minterms" in result, f"the result is {result}"

    # fixed
    input_minterms = [1,12,3,15]
    input_minterms = [1,12,3,15]
    builder.set_random(False)
    result = builder.question_exp(minterms=input_minterms)
    assert isinstance(result, dict)
    assert "minterms" in result, f"the result is {result}"
    assert result['sop'] == " a.b.c.d + a'.b'.d + a.b.c'.d' ", f"the result['sop'] is '{result['sop']}'"
    assert result['pos'] == "(a+d).(a+b').(a'+b).(c'+d).(b'+c+d')", f"the result['pos'] is '{result['pos']}'"

    # fixed
    sop_quest = "a'.b'+a'.b'.c +a'.b'.d +a.b.c.d"
    input_minterms = [0,1,2,3,15]
    builder.set_random(False)
    result = builder.question_exp(minterms=input_minterms, sop_quest=sop_quest)
    assert isinstance(result, dict)
    assert "minterms" in result, f"the result is {result}"
    assert result['sop'] == " a'.b' + a.b.c.d ", f"the result['sop'] is '{result['sop']}'"
    assert result['pos'] == "(a+b').(a'+b).(b'+c).(b'+d)", f"the result['pos'] is '{result['pos']}'"
    assert result['sop_quest'] == sop_quest, f"the result['sop_quest'] is '{result['sop_quest']}'"


def test_prepare_logigram_list(builder):
    sop_list = ["A.B + C.D"]
    equations_list = [{'sop':"A.B + C.D"}]
    result = builder._prepare_logigram_list(sop_list, function_namelist=["F"], variables=["A", "B", "C", "D"],
                                            equations_list = equations_list)
    assert isinstance(result, dict)
    assert "functions" in result, f"the result is {result}"

def test_invalid_minterms(builder):
    with pytest.raises(TypeError):
        builder.question_multi_funct(minterms_list=[[1, 2, 3, "X", 20]], dont_care_list=[[]])
    with pytest.raises(ValueError):
        builder.question_multi_funct(minterms_list=[[1, 2, 3, 20]], dont_care_list=[[]])
def test_get_commands_info(builder):
    # not random numbers
    cmds = builder.get_commands_info()
    assert isinstance(cmds, dict)

def test_get_categories_info(builder):
    # not random numbers
    cats = builder.get_category_info()
    assert isinstance(cats, dict)
import pytest
from strmquiz.question_builder.sequential_question_builder import (
    SequentialQuestionBuilder,
)


@pytest.fixture
def builder():
    """Fixture that returns a SequentialQuestionBuilder instance."""
    return SequentialQuestionBuilder()


def test_init(builder):
    assert builder is not None


def test_prepare_chronogram(builder):
    result = builder._preprare_chrnonogram(
        input_vars=["D"],
        start_signals={"D": 1, "Q": 0},
        flip_type="D",
        length=10,
        synch_type="rising",
        output_vars=["Q"],
    )
    assert isinstance(result, dict)
    assert "answer_signals" in result


def test_prepare_chronogram_register(builder):
    result = builder._preprare_chrnonogram_register(
        input_vars=["E"],
        start_signals={"E": 0, "Q": 0},
        flip_list=[{"type": "D"}],
        nbits=2,
        length=10,
        synch_type="rising",
        output_vars=["Q"],
        register_type="shift-right",
    )
    assert isinstance(result, dict)


def test_prepare_chronogram_counter(builder):
    result = builder._preprare_chrnonogram_counter(
        start_signals={"V": 0, "D": 1, "Q": 0},
        flip_list=[{"type": "D"}],
        nbits=2,
        length=10,
        synch_type="rising",
        output_vars=["Q"],
        counter_type="up",
    )
    assert isinstance(result, dict)


def test_question_chronogram(builder):
    result = builder.question_chronogram(varlist={"D": 1, "Q": 0})
    assert isinstance(result, dict)
    assert "data" in result


def test_question_flip(builder):
    result = builder.question_flip(flip_type="D")
    assert isinstance(result, dict)
    assert "flip_data" in result


def test_question_register(builder):
    result = builder.question_register(register_random=False, flip_types=["D"], nbits=2)
    assert isinstance(result, dict)
    assert "register_data" in result


def test_question_counter(builder):
    result = builder.question_counter(
        counter_random=False, flip_types=["D"], nbits=2, counter_type="up"
    )
    assert isinstance(result, dict)
    assert "counter_data" in result


def test_question_seq_misc(builder):
    result = builder.question_seq_misc(varlist={"D": 1, "Q": 0})
    assert isinstance(result, dict)
    assert "data" in result


def test_get_commands_info(builder):
    # not random numbers
    cmds = builder.get_commands_info()
    assert isinstance(cmds, dict)


def test_get_categories_info(builder):
    # not random numbers
    cats = builder.get_category_info()
    assert isinstance(cats, dict)

from unittest.mock import Mock

import pytest

from strmquiz.question_builder import Question_Builder

# def test_use_formatter_accepts_valid_formatter():
#     qb = Question_Builder()
#     formatter = Mock()
#     formatter.render_question_answer = Mock(return_value=("Q", "A"))
#     qb.use_formatter(formatter)
#     q,  a = qb._render("template", {"x": 1})
#     assert q == "Q"
#     assert a == "A"


def test_use_formatter_rejects_invalid_formatter():
    qb = Question_Builder()
    bad_formatter = object()  # no render_question_answer
    with pytest.raises(AttributeError):
        qb.use_formatter(bad_formatter)


# def test_render_returns_error_on_failure(caplog):
#     qb = Question_Builder()
#     formatter = Mock()
#     formatter.render_question_answer.side_effect = Exception("fail")
#     qb.use_formatter(formatter)
#     q, a = qb._render("t", {})
#     assert "Error" in q
#     assert a == "Error"
#     assert "fail" in q or "fail" in a

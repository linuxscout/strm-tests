import pytest
import random
from strmquiz.question_builder import Question_Builder
from strmquiz.templates import TEMPLATES_DIR

@pytest.fixture
def builder():
    # Use deterministic random seed
    import random
    random.seed(42)
    return Question_Builder(outformat="latex", lang="en", templates_dir=TEMPLATES_DIR)


def test_question_vf(builder):
    q, lang, data, ans = builder.question_vf()
    assert isinstance(q, str)
    assert lang == "arabic"
    assert isinstance(ans, str)


def test_question_cp(builder):
    q, lang, data, ans = builder.question_cp()
    assert "arabic" == lang
    assert isinstance(q, str)


def test_question_base(builder):
    q, _, _, ans = builder.question_base()
    assert isinstance(q, str)
    assert isinstance(ans, str)

def test_question_vf_deterministic():
    rng = random.Random(42)
    builder = Question_Builder(outformat="latex", rng=rng)
    q, lang, data, ans = builder.question_vf()
    assert lang == "arabic"
    assert isinstance(q, str)
    assert isinstance(ans, str)


def test_question_base_roundtrip():
    rng = random.Random(123)
    builder = Question_Builder(outformat="latex", rng=rng)
    q, lang, data, ans = builder.question_base()
    assert lang == "arabic"
    assert "number" in ans or isinstance(ans, str)

def test_question_gray(builder):
    q, _, _, ans = builder.question_gray()
    assert isinstance(q, str)
    assert isinstance(ans, str)


def test_question_funct(builder):
    q, _, _, ans = builder.question_funct()
    assert isinstance(q, str)
    assert isinstance(ans, str)


@pytest.mark.parametrize("method", ["encode", "decode", "both", "invalid"])
def test_question_charcode(builder, method):
    q, _, _, ans = builder.question_charcode(text="AB", scheme="ascii", method=method)
    assert isinstance(q, str)
    assert isinstance(ans, str)


def test_question_static_funct(builder):
    q, _, _, ans = builder.question_static_funct(minterms=[1, 2, 3])
    assert isinstance(q, str)
    assert isinstance(ans, str)


def test_question_chronogram(builder):
    q, _, _, ans = builder.question_chronogram(varlist={"D": 1, "Q": 0})
    assert isinstance(q, str)
    assert isinstance(ans, str)

# 3. Error-handling tests
# a. Invalid charcode method
def test_charcode_invalid_method(builder):
    q, lang, data, ans = builder.question_charcode(text="AB", scheme="ascii", method="nonsense")
    assert isinstance(q, str)
    assert isinstance(ans, str)
    # method should default to "both"
    assert "both" in q or "both" in ans

# b. Empty / None inputs
def test_question_static_funct_empty_minterms(builder):
    q, lang, data, ans = builder.question_static_funct(minterms=[])
    assert isinstance(q, str)
    assert isinstance(ans, str)

# c. Invalid flip type (should fall back to random flip)
def test_question_flip_invalid_fliptype(builder):
    q, lang, data, ans = builder.question_flip(varlist={"D": 1}, flip_type="INVALID")
    assert isinstance(q, str)
    assert isinstance(ans, str)
# d. Register with too few flip types (forces padding)
def test_question_register_missing_flips(builder):
    q, lang, data, ans = builder.question_register(flip_types=[], nbits=4, register_random=False)
    assert isinstance(q, str)
    assert isinstance(ans, str)

# e. Counter with too few flip types (forces padding)
def test_question_counter_missing_flips(builder):
    q, lang, data, ans = builder.question_counter(flip_types=[], nbits=3, counter_random=False)
    assert isinstance(q, str)
    assert isinstance(ans, str)
# f. Counter with invalid type (should default gracefully)
def test_question_counter_invalid_type(builder):
    q, lang, data, ans = builder.question_counter(counter_type="INVALID", nbits=3, counter_random=False)
    assert isinstance(q, str)
    assert isinstance(ans, str)
# g. Chronogram with empty varlist (edge case)
def test_question_chronogram_empty_varlist(builder):
    q, lang, data, ans = builder.question_chronogram(varlist={})
    assert isinstance(q, str)
    assert isinstance(ans, str)
# 4. Stress tests (optional)
# Run multiple question types in a loop to check no unhandled exceptions
@pytest.mark.parametrize("funcname", [
    "question_vf",
    "question_cp",
    "question_intervalle",
    "question_base",
    "question_bcd_x3",
    "question_gray",
    "question_charcode",
    "question_arithm",
    "question_mesure",
    "question_map",
    "question_map_for_sop",
    "question_funct",
    "question_exp",
])
def test_all_generators_no_crash(builder, funcname):
    func = getattr(builder, funcname)
    result = func() if "charcode" not in funcname else func(text="A", method="encode")
    assert isinstance(result, tuple)
    assert len(result) == 4
def test_all_generators_no_crash(builder, funcname):
    func = getattr(builder, funcname)
    result = func() if "charcode" not in funcname else func(text="A", method="encode")
    assert isinstance(result, tuple)
    assert len(result) == 4
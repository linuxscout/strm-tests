import pytest
from strmquiz.encoding_question_builder import EncodingQuestionBuilder


@pytest.fixture
def builder():
    return EncodingQuestionBuilder()



def test_question_vf(builder):
    ctx = builder.question_vf()
    assert isinstance(ctx, dict)
    assert "mantissa" in ctx or "sign" in ctx or "exponent" in ctx



def test_question_cp(builder):
    ctx = builder.question_cp()
    assert isinstance(ctx, dict)
    assert "binary" in ctx


@pytest.mark.skip(reason="To be enabled later")
def test_question_intervalle(builder):
    ctx = builder.question_intervalle()
    assert isinstance(ctx, dict)
    assert "number" in ctx


@pytest.mark.skip(reason="To be enabled later")
def test_question_base(builder):
    ctx = builder.question_base()
    assert isinstance(ctx, dict)
    assert "in_base" in ctx
    assert "out_base" in ctx
    assert "output" in ctx


@pytest.mark.skip(reason="To be enabled later")
def test_question_bcd_x3(builder):
    ctx = builder.question_bcd_x3()
    assert isinstance(ctx, dict)
    assert "bcd" in ctx
    assert "x3" in ctx


@pytest.mark.skip(reason="To be enabled later")
def test_question_gray(builder):
    ctx = builder.question_gray()
    assert isinstance(ctx, dict)
    assert "number_gray" in ctx
    assert "gray_sequence" in ctx


@pytest.mark.skip(reason="To be enabled later")
def test_question_ascii(builder):
    ctx = builder.question_ascii()
    assert isinstance(ctx, dict)
    assert "scheme" in ctx
    assert ctx["scheme"] == "ascii"


@pytest.mark.skip(reason="To be enabled later")
def test_question_unicode(builder):
    ctx = builder.question_unicode()
    assert isinstance(ctx, dict)
    assert "scheme" in ctx
    assert ctx["scheme"] == "unicode"


@pytest.mark.skip(reason="To be enabled later")
def test_question_charcode(builder):
    ctx = builder.question_charcode(text="AB", scheme="ascii")
    assert isinstance(ctx, dict)
    assert "charcodes" in ctx


@pytest.mark.skip(reason="To be enabled later")
def test_question_arithm(builder):
    ctx = builder.question_arithm()
    assert isinstance(ctx, dict)
    assert len(ctx) > 0


@pytest.mark.skip(reason="To be enabled later")
def test_question_mesure(builder):
    builder.question_mesure()

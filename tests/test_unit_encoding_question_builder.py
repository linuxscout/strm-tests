import pytest
from strmquiz.encoding_question_builder import EncodingQuestionBuilder


@pytest.fixture
def builder():
    return EncodingQuestionBuilder()


def test_question_base(builder):
    # not random numbers
    builder.set_random(False)
    ctx = builder.question_base(decimal=102, out_base=8)
    assert isinstance(ctx, dict)
    assert "in_base" in ctx
    assert "out_base" in ctx
    assert ctx["output"] == '146'
    # random numbers
    builder.set_random(True)
    ctx = builder.question_base()
    assert isinstance(ctx, dict)
    assert "in_base" in ctx
    assert "out_base" in ctx

def test_question_vf(builder):
    # not random
    builder.set_random(False)
    ctx = builder.question_vf(number=3.15)
    assert isinstance(ctx, dict)
    assert "mantissa" in ctx or "sign" in ctx or "exponent" in ctx
    assert ctx["mantissa"] == '10010011001100110011001'
    assert ctx["sign"] == 0, f"The result is {ctx}"
    assert ctx["exponent"] == 1,  f"The result is {ctx}"

    # random
    builder.set_random(True)
    ctx = builder.question_vf()
    assert isinstance(ctx, dict)
    assert "mantissa" in ctx or "sign" in ctx or "exponent" in ctx



def test_question_cp(builder):
    # random
    builder.set_random(True)
    ctx = builder.question_cp()
    assert isinstance(ctx, dict)
    assert "binary" in ctx
    # not random
    builder.set_random(False)
    ctx = builder.question_cp(decimal=17)
    assert isinstance(ctx, dict)
    assert "binary" in ctx
    assert ctx['binary'] ==  '-10001',  f"The result is {ctx}"
    assert ctx['cp1'] ==  '11101110', f"The result is {ctx}"
    assert ctx['cp2'] == '11101111', f"The result is {ctx}"





def test_question_intervalle(builder):
    # random
    builder.set_random(True)
    ctx = builder.question_intervalle()
    assert isinstance(ctx, dict)
    assert "number" in ctx, f"The result is {ctx}"

    # not random
    builder.set_random(False)
    ctx = builder.question_intervalle(15)
    assert isinstance(ctx, dict)
    assert ctx["number"] == 15, f"The result is {ctx}"






def test_question_bcd_x3(builder):
    # random
    builder.set_random(True)
    ctx = builder.question_bcd_x3()
    assert isinstance(ctx, dict)
    assert "number" in ctx, f"The result is {ctx}"

    # not random
    builder.set_random(False)
    ctx = builder.question_bcd_x3(decimal_a=126, decimal_b= 1089)
    assert isinstance(ctx, dict)
    assert ctx['bcd'] == '0001 0010 0110', f"The result is {ctx}"
    assert ctx['x3'] == '0100 0101 1001', f"The result is {ctx}"





def test_question_gray(builder):


    # random
    builder.set_random(True)
    ctx = builder.question_gray()
    assert isinstance(ctx, dict)
    assert "number_gray" in ctx
    assert "gray_sequence" in ctx

    # not random
    builder.set_random(False)
    ctx = builder.question_gray(number = 26, sequence_length=3)
    assert isinstance(ctx, dict)
    assert ctx['number_gray'] == '10111', f"The result is {ctx}"
    assert ctx['gray_sequence'] == ['10111', '10110', '10010'], f"The result is {ctx}"



def test_question_ascii(builder):
    # random
    builder.set_random(True)
    ctx = builder.question_ascii()
    assert isinstance(ctx, dict)
    assert "scheme" in ctx
    assert ctx["scheme"] == "ascii"

    # not random
    builder.set_random(False)
    ctx = builder.question_ascii(text="Tah@ 0ki#")
    assert isinstance(ctx, dict)
    assert "scheme" in ctx
    assert ctx["charcodes"] == ['0x54', '0x61', '0x68', '0x40', '0x20', '0x30', '0x6b', '0x69', '0x23'], f"The result is {ctx}"



def test_question_unicode(builder):
    # random
    builder.set_random(True)
    ctx = builder.question_unicode()
    assert isinstance(ctx, dict)
    assert "scheme" in ctx
    assert ctx["scheme"] == "unicode"

    # not random
    builder.set_random(False)
    ctx = builder.question_unicode(text="بنية الآلة @")
    assert isinstance(ctx, dict)
    assert "scheme" in ctx
    assert ctx["charcodes"] == ['0x628', '0x646', '0x64a', '0x629', '0x20', '0x627', '0x644', '0x622', '0x644', '0x629', '0x20', '0x40'], f"The result is {ctx}"



@pytest.mark.skip(reason="To be enabled later")
def test_question_charcode(builder):
    # random
    builder.set_random(True)
    ctx = builder.question_charcode(scheme="ascii")
    assert isinstance(ctx, dict)
    assert "scheme" in ctx
    assert ctx["scheme"] == "unicode"

    # not random
    builder.set_random(False)
    ctx = builder.question_charcode(text="بنية الآلة @", scheme="ascii")
    assert isinstance(ctx, dict)
    assert "scheme" in ctx
    assert ctx["charcodes"] == ['0x628', '0x646', '0x64a', '0x629', '0x20', '0x627', '0x644', '0x622', '0x644', '0x629', '0x20', '0x40'], f"The result is {ctx}"




def test_question_arithm(builder):
    # random
    builder.set_random(True)
    ctx = builder.question_arithm()
    assert isinstance(ctx, dict)
    assert "number_c" in ctx

    # not random
    builder.set_random(False)
    ctx = builder.question_arithm(number_a=150, number_b=245,operation="+", base=8)
    assert isinstance(ctx, dict)
    assert "number_c" in ctx
    assert ctx["number_a"] == '226', f"The result is {ctx}"
    assert ctx["number_b"] == '365', f"The result is {ctx}"
    assert ctx["number_c"] == '613', f"The result is {ctx}"


@pytest.mark.skip(reason="To be enabled later")
def test_question_mesure(builder):
    builder.question_mesure()


def test_compute_steps_from10(builder):
    number_tmp, steps_from10, steps_to10, binary_mode = builder._compute_conversion_steps(
        number=25, in_base=10, out_base=2
    )
    assert isinstance(steps_from10, list)
    assert steps_to10 == []
    assert number_tmp == 0
    assert binary_mode is False



def test_compute_steps_to10(builder):
    number_tmp, steps_from10, steps_to10, binary_mode = builder._compute_conversion_steps(
        number=1011, in_base=2, out_base=10
    )
    assert isinstance(steps_to10, list)
    assert steps_from10 == []
    assert number_tmp == 0
    assert binary_mode is False



def test_compute_binary_mode(builder):
    number_tmp, steps_from10, steps_to10, binary_mode = builder._compute_conversion_steps(
        number="FF", in_base=16, out_base=2
    )
    assert binary_mode is True
    assert steps_from10 == []
    assert steps_to10 == []
    assert number_tmp == 0



def test_compute_steps_general_case(builder):
    number_tmp, steps_from10, steps_to10, binary_mode = builder._compute_conversion_steps(
        number="77", in_base=8, out_base=3
    )
    assert isinstance(steps_to10, list)
    assert isinstance(steps_from10, list)
    assert isinstance(number_tmp, int)
    assert binary_mode is False

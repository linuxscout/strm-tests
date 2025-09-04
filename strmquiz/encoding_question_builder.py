#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz_builder.py
#  
#  Copyright 2019 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import logging
# --- Configure logging ---
logging.basicConfig(
    level=logging.DEBUG,  # change to INFO or WARNING in production
    format="%(levelname)s:%(name)s:%(message)s"
)
logger = logging.getLogger(__name__)

import random



from .codage import question_codage as question
from .codage import ieee754


# 🔹 Constants
LANG_AR = "arabic"
LANG_EN = "english"

SECTION_FLOAT = "encoding/float"
SECTION_CP = "encoding/cp"
SECTION_INTERVAL = "encoding/interval"
SECTION_BASE = "base"
SECTION_ARITHM = "arithm"

SECTION_BCDX3 = "encoding/bcdx3"
SECTION_GRAY = "encoding/gray"
SECTION_CHARCODE = "encoding/charcode"
SECTION_MESURE = "mesure"
from .question_builder import Question_Builder

class EncodingQuestionBuilder(Question_Builder):
    """Generate quiz questions for different domains."""

    def __init__(self, outformat="latex", config_file="", lang="ar-en", templates_dir="",):
        # 🔹 Inject dependencies (makes testing easier)
        super().__init__(outformat=outformat, config_file=config_file, lang=lang, templates_dir=templates_dir,)

        self.qs = question.questionGenerator(latex=True)

        self.vf = ieee754.float_point()
        self.randomize = True



    # --- Example Questions (refactored) ---

    def question_vf(self, number:float=0):
        """Floating point encoding question."""

        x  = self.vf.vf_question() if self.randomize else self.vf.vf_question(number)

        result = self.vf.ieee754_components(x)
        context = {
            "number": result.get("number"),
            "abs_value": result.get("abs_value"),
            "sign": result.get("sign"),
            "binary_repr": result.get("binary_repr"),
            "exponent": result.get("exponent"),
            "exponent_raw": result.get("exponent_raw"),
            "exponent_bits": result.get("exponent_bits"),
            "mantissa": result.get("mantissa"),
            "final_binary": result.get("final_binary"),
            "hex": result.get("hex"),
        }
        return  context
        # return self._render(SECTION_FLOAT, ieee_dict)


    def question_cp(self, decimal=0):
        """Complement coding question."""
        try:
           n, a, cp1, cp2 = self.qs.comp_one(8) if self.randomize else self.qs.comp_one(nbits=8, n=decimal)

        except Exception as e:
            logger.exception("Failed to generate CP question")
            context = {"error": str(e)}
            return context
            # return self._render(SECTION_CP, {"error": str(e)})
        context = {"number": n, "binary": a, "cp1": cp1, "cp2": cp2}
        return context
        # return self._render(SECTION_CP, {"number": n, "binary": a, "cp1": cp1, "cp2": cp2})



    def question_intervalle(self, decimal=0):
        """Interval coding question."""
        n = self.qs.intervalle() if self.randomize else self.qs.intervalle(n=decimal)
        context = {"number": n}
        return context
        # return self._render(SECTION_INTERVAL, context)

    def question_base(self, decimal=0, in_base=10, out_base=10):
        """Base conversion question."""
        if self.randomize:
            res = self.qs.rand_numeral_system()
            number = res.get("number", 0)
            in_base = res.get("in_base", 10)
            out_base = res.get("out_base", 10)
            output = res.get("output", 0)
        else:
            number = decimal #self.qs.int2base(decimal, in_base)
            output = self.qs.int2base(decimal, out_base)

        # reproducible randomness via self.rng
        number_tmp = 0
        steps_from10, steps_to10, binary_mode = [], [], False
        if in_base == 10 and out_base != 10:
            steps_from10 = self.qs.make_steps_from10(number, out_base)
        elif in_base != 10 and out_base == 10:
            steps_to10 = self.qs.number_to_digits(number, in_base)
        elif in_base in (2, 8, 16) and out_base in (2, 8, 16):
            binary_mode = True
        elif in_base != 10 and out_base != 10:
            steps_to10 = self.qs.number_to_digits(number, in_base)
            number_tmp = self.qs.base2int(number, in_base)
            steps_from10 = self.qs.make_steps_from10(number_tmp, out_base)

        context = {
            "number": number,
            "number_tmp": number_tmp,
            "number_label": str(number),
            "in_base": in_base,
            "out_base": out_base,
            "output": output,
            "steps_from10": steps_from10,
            "steps_to10": steps_to10,
            "binary_mode": binary_mode,
        }
        return context
        # return self._render(SECTION_BASE, context)




    def question_bcd_x3(self, decimal_a=0, decimal_b=0, scheme="", method="",min_val=10, max_val=10**5):

        if self.randomize:
            number_a = number  = random.randint(min_val, max_val)
            number_b  = random.randint(min_val, max_val)
        else:
            number_a = number = decimal_a
            number_b  = decimal_b

        bcd = self.qs.dec_to_bcd(number)
        bcd_digits = bcd.split(" ")
        x3 = self.qs.dec_to_excess3(number)
        x3_digits = x3.split(" ")

        data_bcd = self.qs.bcd_addition_explain(number_a, number_b)
        data_x3 = self.qs.x3_addition_explain(number_a, number_b)
        context = {
            "number": str(number) ,
            "bcd": bcd,
            "bcd_digits": bcd_digits,
            "x3": x3,
            "x3_digits": x3_digits,
            "scheme":scheme,
            "method":method,
            "data_bcd":data_bcd,
            "data_x3":data_x3,
        }
        return context
        # return self._render(SECTION_BCDX3, context)

    def question_gray(self, number=0, sequence_length=2):

        if self.randomize:
            x  = random.randint(15, 256) if self.randomize else number
            seq_len  = random.randint(2, 10)
        else:
            x = number
            seq_len = sequence_length
        x_bin = self.qs.int2base(x, 2)
        x_gray = self.qs.binary_to_gray(x_bin)
        x_gray_sequence = self.qs.gray_sequence_from_binary(x_bin,seq_len)
        steps = self.qs.gray_explain(x_bin, x_gray)
        context = {
            "number_dec": str(x) ,
            "number_bin": str(x_bin),
            "number_gray": str(x_gray),
            "gray_sequence": x_gray_sequence,
            "sequence_length": seq_len,
            "method": "encode",
            "steps_gray2bin": steps.get("steps_gray2bin",[]),
            "steps_bin2gray": steps.get("steps_bin2gray",[]),
        }
        return context
        # return self._render(SECTION_GRAY, context)



    def question_ascii(self,method="both", text=""):
        """ encode/ decode in ASCII """
        return self.question_charcode(text=text,scheme="ascii", method=method)

    def question_unicode(self,method="both", text=""):
        """ encode/ decode in Unicode """
        return self.question_charcode(text=text,scheme="unicode", method=method)

    def question_charcode(self,text="",scheme="ascii", method="both"):
        """ encode/ decode in ASCII and unicode
        """
        if self.randomize and not text:
            text  = self.qs.rand_text(code=scheme)
        charcodes = self.qs.encode(text)
        if method not in ("encode", "decode", "both"):
            method = "both"
        context = {
            "charlist": list(text),
            "method": method, # encode decode
            "scheme":scheme,
            "charcodes":charcodes,
        }
        return context
        # return self._render(SECTION_CHARCODE, context)

    def question_arithm(self,number_a=0, number_b=0,operation="+", base=10):
        """
        question about arithmetics (addition and substraction)
        """
        if self.randomize:
            result = self.qs.rand_arithm()
        else:
            result = self.qs.arithm(number_a=number_a, number_b=number_b, base=base, operation=operation)
        context = {
            "question": result.get("question"),
            "reponse": result.get("reponse"),
            "number_a": result.get("number_a"),
            "number_b": result.get("number_b"),
            "number_c": result.get("number_c"),
            "operation": result.get("operation"),
            "base": result.get("base"),
        }
        return context
        # return self._render(SECTION_ARITHM, context)

    def question_mesure(self):
        raise NotImplementedError("Mesure questions are not yet supported")


if __name__ == '__main__':

    qb = EncodingQuestionBuilder()

    print("\n--- Test: Floating Point Question ---")
    print(qb.question_vf())

    print("\n--- Test: Complement Coding Question ---")
    print(qb.question_cp())

    print("\n--- Test: Base Conversion Question ---")
    print(qb.question_base())

    print("\n--- Test: Gray Code Question ---")
    print(qb.question_gray())

    print("\n--- Test: ASCII Question ---")
    print(qb.question_ascii())



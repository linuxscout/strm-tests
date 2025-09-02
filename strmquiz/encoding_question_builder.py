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

from .bool import bool_const
from .sequentiel import tex_chronograms
from .sequentiel import seqconst
from .sequentiel import registersimulator
from .sequentiel import countersimulator
# strmquiz/question_builder.py (refactored skeleton)


from .codage import question_codage as question
from .bool import boolquiz
from .codage import ieee754
from .display import quiz_format_factory


# 🔹 Constants
LANG_AR = "arabic"
LANG_EN = "english"

SECTION_FLOAT = "encoding/float"
SECTION_CP = "encoding/cp"
SECTION_INTERVAL = "encoding/interval"
SECTION_BASE = "base"
SECTION_ARITHM = "arithm"

SECTION_MAP = "bool/map"
SECTION_MAP_SOP = "bool/map-sop"
SECTION_FUNCTION = "bool/function"
SECTION_EXP = "bool/exp"
SECTION_MULTI = "bool/multi_funct"

SECTION_CHRONO = "sequential/timing"
SECTION_FLIP = "sequential/flip"
SECTION_REGISTER = "sequential/register"
SECTION_COUNTER = "sequential/counter"
SECTION_MISC = "sequential/misc"

SECTION_BCDX3 = "encoding/bcdx3"
SECTION_GRAY = "encoding/gray"
SECTION_CHARCODE = "encoding/charcode"
SECTION_MESURE = "mesure"
from .question_builder import Question_Builder

class EncodingQuestionBuilder(Question_Builder):
    """Generate quiz questions for different domains."""

    def __init__(self, outformat="latex", config_file="", lang="ar-en", templates_dir="",
                 rng=None, formater=None, answer_formater=None, qs=None, bq=None, vf=None):
        # 🔹 Inject dependencies (makes testing easier)
        super().__init__(outformat=outformat, config_file=config_file, lang=lang, templates_dir=templates_dir,
                 rng=rng, formater=formater, answer_formater=answer_formater, qs=qs, bq=bq, vf=vf)
        # self.rng = rng or random.Random()
        # self.qs = qs or question.questionGenerator(latex=True)
        # self.bq = bq or boolquiz.bool_quiz()
        # self.bq.set_format('')
        # self.vf = vf or ieee754.float_point()
        #
        # self.formater = formater or quiz_format_factory.quiz_format_factory.factory(
        #     outformat, lang=lang, templates_dir=templates_dir
        # )



    # --- Example Questions (refactored) ---

    def question_vf(self):
        """Floating point encoding question."""
        x = self.vf.vf_question()
        ieee_dict = self.vf.ieee754_components(x)
        return self._render(SECTION_FLOAT, ieee_dict)

    def question_cp(self):
        """Complement coding question."""
        n, a, cp1, cp2 = self.qs.comp_one(8)
        context = {"number": n, "binary": a, "cp1": cp1, "cp2": cp2}
        return self._render(SECTION_CP, context)

    def question_intervalle(self):
        """Interval coding question."""
        n = self.qs.intervalle()
        context = {"number": n}
        return self._render(SECTION_INTERVAL, context)

    def question_base(self):
        """Base conversion question."""
        res = self.qs.rand_numeral_system()
        number = res.get("number", 0)
        in_base = res.get("in_base", 10)
        out_base = res.get("out_base", 10)
        output = res.get("output", 0)

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
        return self._render(SECTION_BASE, context)




    def question_bcd_x3(self, scheme="", method=""):


        number  = self.rng.randint(10, 10**5)

        bcd = self.qs.dec_to_bcd(number)
        bcd_digits = bcd.split(" ")
        x3 = self.qs.dec_to_excess3(number)
        x3_digits = x3.split(" ")
        number_a  = number
        number_b  = self.rng.randint(10, 10**5)
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

        return self._render(SECTION_BCDX3, context)

    def question_gray(self,):

        x  = self.rng.randint(15, 256)

        x_bin = self.qs.int2base(x, 2)
        x_gray = self.qs.binary_to_gray(x_bin)
        seq_len  = self.rng.randint(2, 10)
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

        return self._render(SECTION_GRAY, context)



    def question_ascii(self,method="both", text=""):
        """ encode/ decode in ASCII """
        return self.question_charcode(text=text,scheme="ascii", method=method)

    def question_unicode(self,method="both", text=""):
        """ encode/ decode in ASCII """
        return self.question_charcode(text=text,scheme="unicode", method=method)

    def question_charcode(self,text="",scheme="ascii", method="both"):
        """ encode/ decode in ASCII and unicode
        """
        if not text:
            text  = self.qs.rand_text(code=scheme)
        charcodes = self.qs.encode(text)
        if method not in ("encode", "decode", "both"):
            method = "both"
        context = {
            # "text": self.formater.escape_string(text),
            "charlist": self.formater.escape_string(text),
            "method": method, # encode decode
            "scheme":scheme,
            "charcodes":charcodes,
        }

        return self._render(SECTION_CHARCODE, context)

    def question_arithm(self,):

        res =self.qs.rand_arithm()

        question =u"Faire les opérations suivantes: "
        answer = res.get('reponse','')
        arabic = u"أنجز العمليات الآتية: "

        context = res

        return self._render(SECTION_ARITHM, context)

    def question_mesure(self,):

        res =self.qs.rand_arithm()

        question =u"Faire les conversion suivantes: NOT IMPLEMENTED (MESURE questions) "
        answer = res.get('reponse','')
        context ={"answer":"Not Implemented",
                  "question": "Not Implementes"}


        return self._render(SECTION_MESURE, context)

def main(args):
    pass

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

from .question_builder import Question_Builder

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

class Question_Builder:
    """Generate quiz questions for different domains."""

    def __init__(self, outformat="latex", config_file="", lang="ar-en", templates_dir="",
                 rng=None, formater=None, answer_formater=None, qs=None, bq=None, vf=None):
        # 🔹 Inject dependencies (makes testing easier)
        self.rng = rng or random.Random()
        self.qs = qs or question.questionGenerator(latex=True)
        self.bq = bq or boolquiz.bool_quiz()
        self.bq.set_format('')
        self.vf = vf or ieee754.float_point()

        self.formater = formater or quiz_format_factory.quiz_format_factory.factory(
            outformat, lang=lang, templates_dir=templates_dir
        )
        self.answer_formater = answer_formater or quiz_format_factory.quiz_format_factory.factory(
            outformat, lang=lang, templates_dir=templates_dir
        )

    # 🔹 Common rendering helper
    def _render(self, template: str, context: dict):
        """Render a question and answer using the current formatter."""
        try:
            q, a = self.formater.render_question_answer(template, context)
            return q, LANG_AR, "data", a
        except Exception as e:
            logger.exception("Error rendering template %s", template)
            return f"Error: {e}", LANG_AR, "data", "Error"

    # --- Example Questions (refactored) ---
    #
    # def question_vf(self):
    #     """Floating point encoding question."""
    #     x = self.vf.vf_question()
    #     ieee_dict = self.vf.ieee754_components(x)
    #     return self._render(SECTION_FLOAT, ieee_dict)
    #
    # def question_cp(self):
    #     """Complement coding question."""
    #     n, a, cp1, cp2 = self.qs.comp_one(8)
    #     context = {"number": n, "binary": a, "cp1": cp1, "cp2": cp2}
    #     return self._render(SECTION_CP, context)
    #
    # def question_intervalle(self):
    #     """Interval coding question."""
    #     n = self.qs.intervalle()
    #     context = {"number": n}
    #     return self._render(SECTION_INTERVAL, context)
    #
    # def question_base(self):
    #     """Base conversion question."""
    #     res = self.qs.rand_numeral_system()
    #     number = res.get("number", 0)
    #     in_base = res.get("in_base", 10)
    #     out_base = res.get("out_base", 10)
    #     output = res.get("output", 0)
    #
    #     # reproducible randomness via self.rng
    #     number_tmp = 0
    #     steps_from10, steps_to10, binary_mode = [], [], False
    #     if in_base == 10 and out_base != 10:
    #         steps_from10 = self.qs.make_steps_from10(number, out_base)
    #     elif in_base != 10 and out_base == 10:
    #         steps_to10 = self.qs.number_to_digits(number, in_base)
    #     elif in_base in (2, 8, 16) and out_base in (2, 8, 16):
    #         binary_mode = True
    #     elif in_base != 10 and out_base != 10:
    #         steps_to10 = self.qs.number_to_digits(number, in_base)
    #         number_tmp = self.qs.base2int(number, in_base)
    #         steps_from10 = self.qs.make_steps_from10(number_tmp, out_base)
    #
    #     context = {
    #         "number": number,
    #         "number_tmp": number_tmp,
    #         "number_label": str(number),
    #         "in_base": in_base,
    #         "out_base": out_base,
    #         "output": output,
    #         "steps_from10": steps_from10,
    #         "steps_to10": steps_to10,
    #         "binary_mode": binary_mode,
    #     }
    #     return self._render(SECTION_BASE, context)
    #
    #
    #
    #
    # def question_bcd_x3(self, scheme="", method=""):
    #
    #
    #     number  = self.rng.randint(10, 10**5)
    #
    #     bcd = self.qs.dec_to_bcd(number)
    #     bcd_digits = bcd.split(" ")
    #     x3 = self.qs.dec_to_excess3(number)
    #     x3_digits = x3.split(" ")
    #     number_a  = number
    #     number_b  = self.rng.randint(10, 10**5)
    #     data_bcd = self.qs.bcd_addition_explain(number_a, number_b)
    #     data_x3 = self.qs.x3_addition_explain(number_a, number_b)
    #     context = {
    #         "number": str(number) ,
    #         "bcd": bcd,
    #         "bcd_digits": bcd_digits,
    #         "x3": x3,
    #         "x3_digits": x3_digits,
    #         "scheme":scheme,
    #         "method":method,
    #         "data_bcd":data_bcd,
    #         "data_x3":data_x3,
    #     }
    #
    #     return self._render(SECTION_BCDX3, context)
    #
    # def question_gray(self,):
    #
    #     x  = self.rng.randint(15, 256)
    #
    #     x_bin = self.qs.int2base(x, 2)
    #     x_gray = self.qs.binary_to_gray(x_bin)
    #     seq_len  = self.rng.randint(2, 10)
    #     x_gray_sequence = self.qs.gray_sequence_from_binary(x_bin,seq_len)
    #     steps = self.qs.gray_explain(x_bin, x_gray)
    #     context = {
    #         "number_dec": str(x) ,
    #         "number_bin": str(x_bin),
    #         "number_gray": str(x_gray),
    #         "gray_sequence": x_gray_sequence,
    #         "sequence_length": seq_len,
    #         "method": "encode",
    #         "steps_gray2bin": steps.get("steps_gray2bin",[]),
    #         "steps_bin2gray": steps.get("steps_bin2gray",[]),
    #     }
    #
    #     return self._render(SECTION_GRAY, context)
    #
    #
    #
    # def question_ascii(self,method="both", text=""):
    #     """ encode/ decode in ASCII """
    #     return self.question_charcode(text=text,scheme="ascii", method=method)
    #
    # def question_unicode(self,method="both", text=""):
    #     """ encode/ decode in ASCII """
    #     return self.question_charcode(text=text,scheme="unicode", method=method)
    #
    # def question_charcode(self,text="",scheme="ascii", method="both"):
    #     """ encode/ decode in ASCII and unicode
    #     """
    #     if not text:
    #         text  = self.qs.rand_text(code=scheme)
    #     charcodes = self.qs.encode(text)
    #     if method not in ("encode", "decode", "both"):
    #         method = "both"
    #     context = {
    #         # "text": self.formater.escape_string(text),
    #         "charlist": self.formater.escape_string(text),
    #         "method": method, # encode decode
    #         "scheme":scheme,
    #         "charcodes":charcodes,
    #     }
    #
    #     return self._render(SECTION_CHARCODE, context)
    #
    # def question_arithm(self,):
    #
    #     res =self.qs.rand_arithm()
    #
    #     question =u"Faire les opérations suivantes: "
    #     answer = res.get('reponse','')
    #     arabic = u"أنجز العمليات الآتية: "
    #
    #     context = res
    #
    #     return self._render(SECTION_ARITHM, context)
    #
    # def question_mesure(self,):
    #
    #     res =self.qs.rand_arithm()
    #
    #     question =u"Faire les conversion suivantes: NOT IMPLEMENTED (MESURE questions) "
    #     answer = res.get('reponse','')
    #     context ={"answer":"Not Implemented",
    #               "question": "Not Implementes"}
    #
    #
    #     return self._render(SECTION_MESURE, context)
    #
    # def _prepare_kmap_data(self, minterms, dontcares=[], correct=False, variables=[], simply_terms=[], method="sop", function_name="F"):
    #
    #
    #     maxterms = [x for x in range(16) if x not in minterms and x not in dontcares]
    #
    #
    #     kmap = []
    #     for x in range(16):
    #         if x in minterms:
    #             kmap.append("1")
    #         elif x in dontcares:
    #             kmap.append("x")
    #         else:
    #             kmap.append("0")
    #     formatted_simplification = []
    #     var_names = "".join(variables[:2]) + "\\" + "".join(variables[2:])
    #     table = [
    #         [var_names, "00", "01", "11", "10"],
    #         ["00", kmap[0], kmap[1], kmap[3], kmap[2]],
    #         ["00", kmap[4], kmap[5], kmap[7], kmap[6]],
    #         ["00", kmap[12], kmap[13], kmap[15], kmap[14]],
    #         ["00", kmap[8], kmap[9], kmap[11], kmap[10]],
    #     ]
    #     sop, pos = self.bq.simplify(minterms)
    #     cnf, dnf = self.bq.form_canonique(minterms)
    #
    #
    #     nand_sop = self.bq.make_nand(sop)
    #     nor_pos = self.bq.make_nor(pos)
    #     nand_dnf = self.bq.make_nand(dnf)
    #     nor_cnf = self.bq.make_nor(cnf)
    #     # nor_pos = self.bq.normalize_nand_nor(pos, "pos", "nor")
    #
    #
    #     # simplification = ""
    #
    #     simplification = self.bq.simplify_map(minterms, method=method)
    #
    #     formatted_simplification = self.formater.format_map_terms(simplification, method=method)
    #
    #     # explained NAND and NOR process
    #     # get expalined expression as table,
    #     # then format them
    #     nand_sop_explained_list = [self.formater.normalize_formula(expr) for expr in self.bq.explain_nand(sop)]
    #     nand_dnf_explained_list = [self.formater.normalize_formula(expr) for expr in self.bq.explain_nand(dnf)]
    #     nor_pos_explained_list = [self.formater.normalize_formula(expr) for expr in self.bq.explain_nor(pos)]
    #
    #
    #     nor_cnf_explained_list = [self.formater.normalize_formula(expr) for expr in self.bq.explain_nor(cnf)]
    #
    #
    #     # formated forms
    #     sop_formatted = self.formater.normalize_formula(sop)
    #     pos_formatted = self.formater.normalize_formula(pos)
    #     cnf_formatted = self.formater.normalize_formula(cnf)
    #     dnf_formatted = self.formater.normalize_formula(dnf)
    #     # formatted nand forms
    #     nand_sop_formatted = self.formater.normalize_formula(nand_sop)
    #     nor_pos_formatted = self.formater.normalize_formula(nor_pos)
    #     nand_dnf_formatted = self.formater.normalize_formula(nand_dnf)
    #     nor_cnf_formatted = self.formater.normalize_formula(nor_cnf)
    #
    #     # prepare terms
    #     sop_terms = []
    #     pos_terms = []
    #     dnf_terms = []
    #     cnf_terms = []
    #     nand_sop_terms = []
    #     nor_pos_terms = []
    #     nand_dnf_terms = []
    #     nor_cnf_terms = []
    #     return {
    #         "function_name":function_name,
    #         "minterms": minterms,
    #         "maxterms": maxterms,
    #         "dontcares": dontcares,
    #         "simplification": simplification,
    #         "sop": sop,
    #         "pos": pos,
    #         "sop_dict":{"default":sop,
    #                     "terms": sop_terms,
    #                     "formatted":sop_formatted,
    #                     "explained":["SOP not explained",]},
    #         "pos_dict":{"default":pos,
    #                     "terms": pos_terms,
    #                     "formatted":pos_formatted,
    #                     "explained":"POS not explained"},
    #         "nand_sop_dict": {"default": nand_sop,
    #                          "terms": nand_sop_terms,
    #                          "formatted": nand_sop_formatted,
    #                          "explained": nand_sop_explained_list},
    #         "nor_pos_dict":{"default":nor_pos,
    #                     "terms": nor_pos_terms,
    #                     "formatted":nor_pos_formatted,
    #                     "explained":nor_pos_explained_list},
    #         "dnf_dict": {"default": dnf,
    #                      "terms": dnf_terms,
    #                      "formatted": dnf_formatted,
    #                      "explained": ["dnf not explained",]},
    #         "cnf_dict": {"default": cnf,
    #                      "terms": cnf_terms,
    #                      "formatted": cnf_formatted,
    #                      "explained": ["cnf not explained",]},
    #         "nand_dnf_dict": {"default": nand_dnf,
    #                           "terms": nand_dnf_terms,
    #                           "formatted": nand_dnf_formatted,
    #                           "explained": nand_dnf_explained_list},
    #         "nor_cnf_dict": {"default": nor_cnf,
    #                          "terms": nor_cnf_terms,
    #                          "formatted": nor_cnf_formatted,
    #                          "explained": nor_cnf_explained_list},
    #         # "sop_formatted": sop_formatted,
    #         # "pos_formatted": pos_formatted,
    #         "formatted_simplification": formatted_simplification,
    #         "variables": variables,
    #         "ab": "".join(variables[:2]),
    #         "cd": "".join(variables[2:]),
    #         "table": table,
    #         "cnf":cnf,
    #         "dnf":dnf,
    #         "nand_sop":nand_sop,
    #         "nand_dnf":nand_dnf,
    #         "nor_pos":nor_pos,
    #         "nor_cnf":nor_cnf,
    #         "method":method,
    #     }
    #
    # def question_map(self, ):
    #
    #     nb_table = 3
    #     minterms_table = [self.bq.rand_funct() for i in range(nb_table)]
    #     data_list = []
    #     for minterms in minterms_table:
    #         data_list.append( self._prepare_kmap_data(minterms=minterms,
    #                                       dontcares=[],
    #                                       correct=True,
    #                                       variables=self.bq.variables
    #                                        )
    #                           )
    #
    #     context = {"data_list":data_list}
    #     return self._render(SECTION_MAP, context)
    #
    #
    # def question_map_for_sop(self,nb=2):
    #     self.bq.reset_vars()
    #     minterms_table =[self.bq.rand_funct() for i in range(nb)]
    #     data_list = []
    #     for minterms in minterms_table:
    #         data_list.append( self._prepare_kmap_data(minterms=minterms,
    #                                       dontcares=[],
    #                                       correct=True,
    #                                       variables=self.bq.variables
    #                                        )
    #                           )
    #
    #     context = {"data_list":data_list}
    #
    #     return self._render(SECTION_MAP_SOP, context)
    #
    #
    # def question_funct(self, ):
    #
    #     self.bq.reset_vars()
    #     sop_quest, minterms = self.bq.rand_exp()
    #
    #     sop_quest = self.formater.normalize_formula(sop_quest)
    #
    #     context  = self._prepare_kmap_data(minterms=minterms,
    #                                   dontcares=[],
    #                                   correct=True,
    #                                   variables=self.bq.variables
    #                                    )
    #
    #     sop, pos = self.bq.simplify(minterms)
    #     logigram = self.formater.draw_logigram(sop, function_name='F',
    #                                           variables=self.bq.variables)
    #     context["sop_quest"] = sop_quest
    #     context["logicdiagram"] = logigram
    #     equations_list = [{"sop": sop,
    #                        "pos": pos,
    #                        "nor_pos": context.get("nor_pos", ""),
    #                        "nand_sop": context.get("nand_sop", '')},
    #                       ]
    #     logigramdict = self.formater.prepare_logigram_list([sop, ], function_namelist=["F",],
    #                                                variables=["A","B","C","D"], equations_list=equations_list)
    #     context["logicdiagramdict"] = logigramdict
    #     # question, answer = self.formater.render_question_answer("bool/function", context)
    #     return self._render(SECTION_FUNCTION, context)
    #
    #
    #
    # def get_terms(self,expr,method="sop"):
    #     """split an expression into terms"""
    #     seps = {
    #         'sop':"+",
    #         'nand':bool_const.BIG_NAND_SYMB,
    #         'nor':bool_const.BIG_NOR_SYMB,
    #         'pos':".",
    #     }
    #     sep = seps.get(method.lower(),"+")
    #     return [[t.strip() for t in term.split(".")] for term in expr.split("+")]
    #
    # def question_static_funct(self, minterms, var_names=["A","B","C","D"], output_names=["S0","S1","S2","S3"], dont_care=[] ):
    #
    #     self.bq.set_vars(var_names, output_names)
    #
    #     sop_quest = ""
    #     fname = output_names[0]
    #     context = self._prepare_kmap_data(minterms=minterms,
    #                                       dontcares=dont_care,
    #                                       correct=True,
    #                                       variables=var_names,
    #                                       function_name=fname
    #                                       )
    #
    #     sop, pos = self.bq.simplify(minterms)
    #     logigram = self.formater.draw_logigram(sop, function_name=fname,
    #                                            variables=var_names)
    #     context["sop_quest"] = sop_quest
    #     context["logicdiagram"] = logigram
    #     context["terms"] = [[t.strip() for t in term.split(".")] for term in sop.split("+")]
    #     equations_list  = [{"sop": sop,
    #                            "pos": pos,
    #                            "nor_pos": context.get("nor_pos", ""),
    #                            "nand_sop": context.get("nand_sop", '')},
    #                         ]
    #     logigramdict = self.formater.prepare_logigram_list([sop, ], function_namelist=[fname,],
    #                                                variables=var_names,  equations_list= equations_list)
    #     context["logicdiagramdict"] = logigramdict
    #     # question, answer = self.formater.render_question_answer("bool/function", context)
    #     # return question, "arabic", "data", answer
    #     return self._render(SECTION_FUNCTION, context)
    #
    #
    #
    # def question_static_nand_exp(self, minterms, var_names=["A", "B", "C", "D"], output_names=["S0", "S1", "S2", "S3"],
    #                              dont_care=[], method="nand"):
    #     self.bq.set_vars(var_names, output_names)
    #
    #     sop_quest = ""
    #     fname = output_names[0]
    #     context = self._prepare_kmap_data(minterms=minterms,
    #                                       dontcares=dont_care,
    #                                       correct=True,
    #                                       variables=var_names,
    #                                       function_name=fname,
    #                                       method=method
    #                                       )
    #
    #     sop, pos = self.bq.simplify(minterms)
    #     logigram = self.formater.draw_logigram_nand_nor(sop, function_name=fname,
    #                                            variables=var_names, method=method)
    #
    #     context["sop_quest"] = sop_quest
    #     context["logicdiagram"] = logigram
    #     logigramdict = self.formater.prepare_logigram_list([sop, ], function_namelist=[fname,],
    #                                                variables=var_names, method=method)
    #     context["logicdiagramdict"] = logigramdict
    #     # question, answer = self.formater.render_question_answer("bool/function", context)
    #     # return question, "arabic", "data", answer
    #     return self._render(SECTION_FUNCTION, context)
    #
    #
    # def question_multi_funct(self, minterms_list, var_names=["A","B","C","D"],
    #  output_names=["S0","S1","S2","S3"], dont_care_list=[], method=""):
    #
    #     self.bq.set_vars(var_names, output_names)
    #
    #     sop_quest = ""
    #     fname = output_names[0]
    #     # one truth table
    #     # multiple karnaugh map
    #     # one logigram
    #     data_list = []
    #     sop_list = []
    #     pos_list = []
    #     terms_list  = []
    #     equations_list  = []
    #     for minterms, dont_care, fname in zip(minterms_list, dont_care_list, output_names):
    #         data = self._prepare_kmap_data(minterms=minterms,
    #                                           dontcares=dont_care,
    #                                           correct=True,
    #                                           variables=var_names,
    #                                           function_name=fname
    #                                           )
    #         data_list.append( data )
    #         sop, pos = self.bq.simplify(minterms)
    #         # sop = self.formater.normalize_formula(sop)
    #         sop_list.append(sop)
    #         equations_list.append( {"sop":sop,
    #                                 "pos":pos,
    #                                 "nor_pos":data.get("nor_pos",""),
    #                                 "nand_sop":data.get("nand_sop",'')})
    #
    #         # terms_list.append([[t.strip() for t in term.split(".")] for term in sop.split("+")])
    #     logigramdict = self.formater.prepare_logigram_list(sop_list, function_namelist=output_names,
    #                                                variables=var_names, method=method, equations_list=equations_list)
    #     # old method to draw logigram used only for latex,
    #     # deprecated
    #     logigram = self.formater.draw_logigram_list(sop_list, function_namelist=output_names,
    #                                                variables=var_names, method=method)
    #     context ={"data_list":data_list,
    #               "minterms_list":minterms_list,
    #               "dontcares_list": dont_care_list,
    #               "function_name_list": output_names,
    #               "variables": var_names,
    #               "sop_quest":sop_quest,
    #               # "terms_list":terms_list,
    #               "logicdiagram" : logigram,  # deprecated, used only for comparaison
    #               "logicdiagramdict" : logigramdict,
    #               "sop_list":sop_list,
    #               "method":method,
    #               }
    #     # question, answer = self.formater.render_question_answer("bool/multi_funct", context)
    #     # return question, "arabic", "data", answer
    #     return self._render(SECTION_MULTI, context)
    #
    # def question_exp(self,):
    #
    #     self.bq.reset_vars()
    #     sop_quest, minterms = self.bq.rand_exp()
    #
    #     sop_quest = self.formater.normalize_formula(sop_quest)
    #
    #     context  = self._prepare_kmap_data(minterms=minterms,
    #                                   dontcares=[],
    #                                   correct=True,
    #                                   variables=self.bq.variables,
    #                                   function_name="S",
    #                                    )
    #
    #
    #     context["sop_quest"] = sop_quest
    #     return self._render(SECTION_EXP, context)
    #     # question, answer = self.formater.render_question_answer("bool/exp", context)
    #     # return question, "arabic", "data", answer
    #
    # def _preprare_chrnonogram(self,  input_vars=["V",], start_signals={"D": 1,"Q":0}, flip_type="D", length=20, synch_type="rising", output_vars=["Q", ]):
    #
    #     # start_signals = start_signals
    #     chrono = tex_chronograms.Tex_Chronograms();
    #     init_signals = {}
    #     for key in start_signals:
    #         if key in output_vars:
    #             # add an empty signal
    #             init_signals[key] = [start_signals[key], ]
    #         else:
    #             signal_dict = chrono.question({key: start_signals[key]}, length=length)
    #             init_signals[key] = signal_dict[key]
    #     # input_vars = [k for k in varlist if k not in output_vars]
    #     # set synchronization type
    #     chrono.set_synch_type(synch_type)
    #
    #     # generate question
    #     # 1- clock
    #     # 2- signals without solution
    #     clock = chrono.clock_signal(length=length, period=1)
    #     # tex_data_question = chrono.draw(init_signals, clock)
    #
    #     # generate soltution
    #     # get solution for signal
    #     # 2 generate chrono for answer
    #     # if we want to generate multiple cases using "dual" or "all"
    #     if synch_type == "all" or synch_type == "dual":
    #         # set synchronization type
    #         chrono.set_synch_type("rising")
    #     # print(__file__,"before_resolve", flip_type, init_signals)
    #     out_signal = chrono.resolve(flip_type=flip_type, signals=init_signals.copy(), period=2, inputs=input_vars)
    #     # print(__file__,"after_resolve", flip_type, out_signal)
    #
    #     # output signal
    #     tmp_signals = init_signals.copy()
    #     tmp_signals[output_vars[0]] = out_signal
    #     # add inverse signal
    #     tmp_signals[output_vars[0] + "'"] = [-s for s in out_signal]
    #     # add more signals for multi cases
    #     if synch_type == "all" or synch_type == "dual":
    #         # set synchronization type
    #         chrono.set_synch_type("falling")
    #
    #         out_signal = chrono.resolve(flip_type=flip_type, signals=init_signals.copy(), period=2,inputs=input_vars)
    #         # output signal
    #         tmp_signals[output_vars[0] + ".falling"] = out_signal
    #
    #     if synch_type == "all":
    #         # set synchronization type
    #         chrono.set_synch_type("asynch")
    #         out_signal = chrono.resolve(flip_type=flip_type, signals=init_signals.copy(), period=2,inputs=input_vars)
    #         tmp_signals[output_vars[0] + ".asyn"] = out_signal
    #
    #     if synch_type == "all" or synch_type == "dual":
    #         # set synchronization type
    #         chrono.set_synch_type("dual")
    #
    #
    #     input_signals = {k:v for k,v in tmp_signals.items() if k in input_vars}
    #
    #     out_signals_initial = {k:v for k,v in init_signals.items() if k in output_vars}
    #
    #     out_signals_final = {k:v for k,v in tmp_signals.items() if k in output_vars}
    #
    #     tex_data_answer = chrono.draw(tmp_signals, clock)
    #
    #     data= {
    #     "varlist":start_signals,
    #     "flip_type":flip_type,
    #     "length":length,
    #     "synch_type":synch_type,
    #     "output_vars":output_vars,
    #     "input_vars": input_vars,
    #     "input_signals": input_signals,
    #     "output_signals":{"initial": out_signals_initial,
    #                 "final": out_signals_final,
    #                   },
    #     "clock":clock,
    #     "question_signals":init_signals,
    #     "answer_signals":tmp_signals,
    #     "tex_data_answer":tex_data_answer,
    #     }
    #     return data
    #
    # def _preprare_chrnonogram_register(self,  input_vars=["V",], start_signals={"D": 1,"Q":0}, flip_list=["D",], nbits =4,
    #                                 length=20, synch_type="rising", output_vars=["Q", ],register_type="shift-right"):
    #
    #     # start_signals = start_signals*
    #     flip_types = [x.get("type","") for x in flip_list]
    #     reg_sim = registersimulator.RegisterSimulator(inputs=input_vars, outputs=output_vars,
    #                                                   # flip_types=flip_types, register_type="shift-right")
    #                                                   flip_types=flip_types, register_type=register_type)
    #
    #     chrono = tex_chronograms.Tex_Chronograms();
    #     flip_type = flip_list[0].get("type","")
    #     init_signals = {}
    #     for key in start_signals:
    #         if key in output_vars:
    #             # add an empty signal
    #             init_signals[key] = [start_signals[key], ]
    #         else:
    #             signal_dict = chrono.question({key: start_signals[key]}, length=length)
    #             init_signals[key] = signal_dict[key]
    #     # input_vars = [k for k in varlist if k not in output_vars]
    #     # set synchronization type
    #     chrono.set_synch_type(synch_type)
    #
    #     # generate question
    #     # 1- clock
    #     clock = chrono.clock_signal(length=length, period=1)
    #
    #
    #     tmp_signals = reg_sim.resolve_register(init_signals.copy(), signal_length=length)
    #
    #
    #     input_signals = {k:v for k,v in tmp_signals.items() if k in input_vars}
    #
    #     out_signals_initial = {k:v for k,v in init_signals.items() if k in output_vars}
    #
    #     out_signals_final = {k:v for k,v in tmp_signals.items() if k in output_vars}
    #
    #     tex_data_answer = chrono.draw(tmp_signals, clock)
    #
    #     data= {
    #     "varlist":start_signals,
    #     "flip_type":flip_type,
    #     "length":length,
    #     "synch_type":synch_type,
    #     "output_vars":output_vars,
    #     "input_vars": input_vars,
    #     "input_signals": input_signals,
    #     "output_signals":{"initial": out_signals_initial,
    #                 "final": out_signals_final,
    #                   },
    #     "clock":clock,
    #     "question_signals":init_signals,
    #     "answer_signals":tmp_signals,
    #     "tex_data_answer":tex_data_answer,
    #     }
    #     return data
    #
    # def _preprare_chrnonogram_counter(self,  input_vars=["V",], start_signals={"D": 1,"Q":0}, flip_list=["D",], nbits =4,
    #                                 length=20, synch_type="rising", output_vars=["Q", ],counter_type="up"):
    #
    #     # start_signals = start_signals*
    #     flip_types = [x.get("type","") for x in flip_list]
    #     reg_sim = countersimulator.CounterSimulator(inputs=input_vars, outputs=output_vars,
    #                                                   flip_types=flip_types, counter_type=counter_type)
    #
    #     chrono = tex_chronograms.Tex_Chronograms()
    #     flip_type = flip_list[0].get("type","")
    #     init_signals = {}
    #     for key in start_signals:
    #         if key in output_vars:
    #             # add an empty signal
    #             init_signals[key] = [start_signals[key], ]
    #         else:
    #             if key == "Vcc":
    #                 init_signals[key] = [length*2]
    #             elif key == "Gnd":
    #                 init_signals[key] = [-length*2]
    #             else:
    #                 signal_dict = chrono.question({key: start_signals[key]}, length=length)
    #                 init_signals[key] = signal_dict[key]
    #     # set synchronization type
    #     chrono.set_synch_type(synch_type)
    #
    #     # generate question
    #     # 1- clock
    #     # 2- signals without solution
    #     clock = chrono.clock_signal(length=length, period=1)
    #
    #     # generate solution
    #     tmp_signals = reg_sim.resolve_counter(init_signals.copy(), signal_length=length)
    #
    #     # the counter hasn't inputs
    #     input_signals = {}
    #     out_signals_initial = {k:v for k,v in init_signals.items() if k in output_vars}
    #
    #     out_signals_final = {k:v for k,v in tmp_signals.items() if k in output_vars}
    #     tex_data_answer = chrono.draw(tmp_signals, clock)
    #
    #     data= {
    #     "varlist":start_signals,
    #     "flip_type":flip_type,
    #     "length":length,
    #     "synch_type":synch_type,
    #     "output_vars":output_vars,
    #     "input_vars": input_vars,
    #     "input_signals": input_signals,
    #     "output_signals":{"initial": out_signals_initial,
    #                 "final": out_signals_final,
    #                   },
    #     "clock":clock,
    #     "question_signals":out_signals_initial,
    #     "answer_signals":out_signals_final,
    #     "tex_data_answer":tex_data_answer,
    #     }
    #     return data
    #
    # def question_chronogram(self, varlist={}, flip_type="D", length=20, synch_type="rising", output_vars=["Q", ]):
    #
    #     """
    #     Generate Chronogram question
    #     """
    #     context= {}
    #     #TODO: fix in config file
    #     input_vars = [k for k in list(varlist.keys()) if not k.upper().startswith("Q")]
    #
    #     data = self._preprare_chrnonogram(input_vars=input_vars,start_signals=varlist, flip_type=flip_type, length=length, synch_type=synch_type, output_vars=output_vars)
    #
    #     context= {"data": data,
    #       }
    #     question, answer = self.formater.render_question_answer("sequential/timing", context)
    #     return question, "arabic", "data", answer
    #
    #
    # def _get_rand_flip(self,):
    #     seqs = seqconst.FLIPS_RANDOM
    #     name = self.rng.choice(list(seqs.keys()))
    #     inputs = list(name)
    #     init_signals = {e: 0 for e in inputs}
    #     init_signals.update({'Q': -1, "Q'": 1, })
    #     tt = seqs[name]
    #     varlist = inputs + ["Q", "Q'"]
    #
    #     return {'init_signals': init_signals,
    #             'inputs': inputs,
    #             'outputs': ['Q', "Q'"],
    #             'truth_table': tt,
    #             'type': name,
    #             'vars': varlist}
    # def question_flip(self, varlist={}, flip_type="D", length=20, synch_type="rising", output_vars=["Q", ]):
    #
    #     """
    #     Generate Chronogram question for a given flip
    #     """
    #     # if not standard flip type, generate a random one
    #     flip_data = seqconst.FLIPS_DATA.get(flip_type,{})
    #     if not flip_data:
    #         flip_data = self._get_rand_flip()
    #     flip_type_new = flip_data.get("type",flip_type)
    #     # set defaulyt var list for given flip
    #     # else take the given one
    #     start_signals = flip_data.get("init_signals",{})
    #     # a standard output for flip questions
    #     output_vars_new = ["Q", "Q'"]
    #
    #     data = self._preprare_chrnonogram(input_vars=flip_data["inputs"], start_signals=start_signals, flip_type=flip_type_new, length=length, synch_type=synch_type, output_vars=output_vars_new)
    #
    #     context= {"data": data,
    #               "flip_data":flip_data,
    #       }
    #     # question, answer = self.formater.render_question_answer("sequential/flip", context)
    #     # return question, "arabic", "data", answer
    #     return self._render(SECTION_FLIP, context)
    #
    # def question_register(self, varlist={}, flip_types=["D",], length=20, synch_type="rising", output_vars=["Q", ], register_type="shift-right",
    #                       nbits:int=2,
    #                       register_random:bool=True):
    #
    #     """
    #     Generate Chronogram question for a given register
    #     """
    #     if register_random:
    #         nbits = self.rng.randint(3,6)
    #         reg_flip_type_list = self.rng.choices(["D","JK"], k=nbits)
    #         # get data from flip standard
    #         reg_flip_list = [seqconst.FLIPS_DATA.get(ft,{}) for ft in reg_flip_type_list ]
    #     else:
    #         reg_flip_type_list = flip_types
    #         # in case that configuration fliptypes is missing
    #         if len(reg_flip_type_list) < nbits:
    #            reg_flip_type_list = reg_flip_type_list + ["D"] * (nbits-len(flip_types))
    #         # get data from flip standard
    #         reg_flip_list = [seqconst.FLIPS_DATA.get(ft,{}) for ft in reg_flip_type_list ]
    #
    #     inputs = ["E",]
    #     outputs = [f"Q{i}" for i in range(nbits)]
    #     vars_ = inputs + outputs
    #     init_signals= {e:0 for e in vars_}
    #     # register_type = "shift-left"
    #     if register_type.endswith("left"):
    #         shift = "left"
    #     else:
    #         shift = "right"
    #     register_data ={  'inputs': inputs,
    #           'outputs': outputs,
    #            'init_signals':  init_signals,
    #           'flip_list': reg_flip_list,
    #           'flip_type_list': reg_flip_type_list,
    #             "type":"",
    #            'nbits':nbits,
    #             "shift":shift,
    #           'vars':vars_ }
    #
    #     data = self._preprare_chrnonogram_register(input_vars=inputs,
    #                                       start_signals=init_signals,
    #                                       flip_list = reg_flip_list,
    #                                       length=length,
    #                                       nbits=nbits,
    #                                       synch_type=synch_type,
    #                                       output_vars=outputs,
    #                                       register_type=register_type)
    #
    #
    #     context= {"data": data,
    #               "register_data": register_data,
    #       }
    #     return self._render(SECTION_REGISTER, context)
    #     # question, answer = self.formater.render_question_answer("sequential/register", context)
    #     # return question, "arabic", "data", answer
    #
    #
    # def question_counter(self, varlist={}, flip_types=["D",], length=20, synch_type="rising", output_vars=["Q", ], counter_type="up",
    #                       nbits:int=2,
    #                       counter_random:bool=True):
    #
    #     """
    #     Generate Chronogram question for a given register
    #     """
    #     if counter_random:
    #         nbits = self.rng.randint(3,6)
    #         reg_flip_type_list = self.rng.choices(["D","JK"], k=nbits)
    #         # get data from flip standard
    #         reg_flip_list = [seqconst.FLIPS_DATA.get(ft,{}) for ft in reg_flip_type_list ]
    #     else:
    #         reg_flip_type_list = flip_types
    #         # in case that configuration fliptypes is missing
    #         if len(reg_flip_type_list) < nbits:
    #            # reg_flip_type_list = reg_flip_type_list + ["D"] * (nbits-len(flip_types))
    #            reg_flip_type_list = reg_flip_type_list + ["JK"] * (nbits-len(flip_types))
    #         # get data from flip standard
    #         reg_flip_list = [seqconst.FLIPS_DATA.get(ft,{}) for ft in reg_flip_type_list ]
    #
    #     inputs = ["Vcc","Gnd"]
    #     outputs = [f"Q{i}" for i in range(nbits)]
    #     vars_ = inputs + outputs
    #     if counter_type.lower() == "up":
    #         init_signals= {e:0 for e in vars_}
    #     else:
    #         init_signals= {e:1 for e in vars_}
    #     # special signals
    #     # init_signals['Vcc'] = [length*2]
    #     # init_signals['Gnd'] = [-length*2]
    #     # register_type = "shift-left"
    #     counter_data ={  'inputs': inputs,
    #           'outputs': outputs,
    #            'init_signals':  init_signals,
    #           'flip_list': reg_flip_list,
    #           'flip_type_list': reg_flip_type_list,
    #             "type":counter_type,
    #            'nbits':nbits,
    #           'vars':vars_ }
    #
    #     data = self._preprare_chrnonogram_counter(input_vars=inputs,
    #                                       start_signals=init_signals,
    #                                       flip_list = reg_flip_list,
    #                                       length=length,
    #                                       nbits=nbits,
    #                                       synch_type=synch_type,
    #                                       output_vars=outputs,
    #                                       counter_type=counter_type)
    #
    #
    #     context= {"data": data,
    #               "counter_data": counter_data,
    #       }
    #     return self._render(SECTION_COUNTER, context)
    #     # question, answer = self.formater.render_question_answer("sequential/counter", context)
    #     # return question, "arabic", "data", answer
    #
    #
    #
    # def question_seq_misc(self, varlist={}, flip_type="D", length=20, synch_type="rising", output_vars=["Q", ]):
    #
    #     """
    #     Generate Chronogram question for a given sequential miscellaneous circuit
    #     """
    #     context= {}
    #
    #     data = self._preprare_chrnonogram(varlist=varlist, flip_type=flip_type, length=length, synch_type=synch_type, output_vars=output_vars)
    #
    #     context= {"data": data,
    #       }
    #     return self._render(SECTION_MISC, context)
    #     # question, answer = self.formater.render_question_answer("sequential/misc", context)
    #     # return question, "arabic", "data", answer
    #

def main(args):
    pass

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

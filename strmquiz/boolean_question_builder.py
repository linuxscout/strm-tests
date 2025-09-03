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


from .bool import boolquiz



# 🔹 Constants
LANG_AR = "arabic"
LANG_EN = "english"


SECTION_MAP = "bool/map"
SECTION_MAP_SOP = "bool/map-sop"
SECTION_FUNCTION = "bool/function"
SECTION_EXP = "bool/exp"
SECTION_MULTI = "bool/multi_funct"

from .question_builder import Question_Builder

class BooleanQuestionBuilder(Question_Builder):
    """Generate quiz questions for different domains."""

    def __init__(self, outformat="latex", config_file="", lang="ar-en", templates_dir=""):
        # 🔹 Inject dependencies (makes testing easier)
        super().__init__(outformat=outformat, config_file=config_file, lang=lang, templates_dir=templates_dir)
        self.bq = boolquiz.bool_quiz()
        self.bq.set_format('')

    # --- Example Questions (refactored) ---

    def _prepare_kmap_data(self, minterms, dontcares=[], correct=False, variables=[], simply_terms=[], method="sop", function_name="F"):


        maxterms = [x for x in range(16) if x not in minterms and x not in dontcares]


        kmap = []
        for x in range(16):
            if x in minterms:
                kmap.append("1")
            elif x in dontcares:
                kmap.append("x")
            else:
                kmap.append("0")
        formatted_simplification = []
        var_names = "".join(variables[:2]) + "\\" + "".join(variables[2:])
        table = [
            [var_names, "00", "01", "11", "10"],
            ["00", kmap[0], kmap[1], kmap[3], kmap[2]],
            ["00", kmap[4], kmap[5], kmap[7], kmap[6]],
            ["00", kmap[12], kmap[13], kmap[15], kmap[14]],
            ["00", kmap[8], kmap[9], kmap[11], kmap[10]],
        ]
        sop, pos = self.bq.simplify(minterms)
        cnf, dnf = self.bq.form_canonique(minterms)


        nand_sop = self.bq.make_nand(sop)
        nor_pos = self.bq.make_nor(pos)
        nand_dnf = self.bq.make_nand(dnf)
        nor_cnf = self.bq.make_nor(cnf)
        # nor_pos = self.bq.normalize_nand_nor(pos, "pos", "nor")


        # simplification = ""

        simplification = self.bq.simplify_map(minterms, method=method)

        formatted_simplification = self.formater.format_map_terms(simplification, method=method)

        # explained NAND and NOR process
        # get expalined expression as table,
        # then format them
        nand_sop_explained_list = [self.formater.normalize_formula(expr) for expr in self.bq.explain_nand(sop)]
        nand_dnf_explained_list = [self.formater.normalize_formula(expr) for expr in self.bq.explain_nand(dnf)]
        nor_pos_explained_list = [self.formater.normalize_formula(expr) for expr in self.bq.explain_nor(pos)]


        nor_cnf_explained_list = [self.formater.normalize_formula(expr) for expr in self.bq.explain_nor(cnf)]


        # formated forms
        sop_formatted = self.formater.normalize_formula(sop)
        pos_formatted = self.formater.normalize_formula(pos)
        cnf_formatted = self.formater.normalize_formula(cnf)
        dnf_formatted = self.formater.normalize_formula(dnf)
        # formatted nand forms
        nand_sop_formatted = self.formater.normalize_formula(nand_sop)
        nor_pos_formatted = self.formater.normalize_formula(nor_pos)
        nand_dnf_formatted = self.formater.normalize_formula(nand_dnf)
        nor_cnf_formatted = self.formater.normalize_formula(nor_cnf)

        # prepare terms
        sop_terms = []
        pos_terms = []
        dnf_terms = []
        cnf_terms = []
        nand_sop_terms = []
        nor_pos_terms = []
        nand_dnf_terms = []
        nor_cnf_terms = []
        return {
            "function_name":function_name,
            "minterms": minterms,
            "maxterms": maxterms,
            "dontcares": dontcares,
            "simplification": simplification,
            "sop": sop,
            "pos": pos,
            "sop_dict":{"default":sop,
                        "terms": sop_terms,
                        "formatted":sop_formatted,
                        "explained":["SOP not explained",]},
            "pos_dict":{"default":pos,
                        "terms": pos_terms,
                        "formatted":pos_formatted,
                        "explained":"POS not explained"},
            "nand_sop_dict": {"default": nand_sop,
                             "terms": nand_sop_terms,
                             "formatted": nand_sop_formatted,
                             "explained": nand_sop_explained_list},
            "nor_pos_dict":{"default":nor_pos,
                        "terms": nor_pos_terms,
                        "formatted":nor_pos_formatted,
                        "explained":nor_pos_explained_list},
            "dnf_dict": {"default": dnf,
                         "terms": dnf_terms,
                         "formatted": dnf_formatted,
                         "explained": ["dnf not explained",]},
            "cnf_dict": {"default": cnf,
                         "terms": cnf_terms,
                         "formatted": cnf_formatted,
                         "explained": ["cnf not explained",]},
            "nand_dnf_dict": {"default": nand_dnf,
                              "terms": nand_dnf_terms,
                              "formatted": nand_dnf_formatted,
                              "explained": nand_dnf_explained_list},
            "nor_cnf_dict": {"default": nor_cnf,
                             "terms": nor_cnf_terms,
                             "formatted": nor_cnf_formatted,
                             "explained": nor_cnf_explained_list},
            # "sop_formatted": sop_formatted,
            # "pos_formatted": pos_formatted,
            "formatted_simplification": formatted_simplification,
            "variables": variables,
            "ab": "".join(variables[:2]),
            "cd": "".join(variables[2:]),
            "table": table,
            "cnf":cnf,
            "dnf":dnf,
            "nand_sop":nand_sop,
            "nand_dnf":nand_dnf,
            "nor_pos":nor_pos,
            "nor_cnf":nor_cnf,
            "method":method,
        }

    def question_map(self, ):

        nb_table = 3
        minterms_table = [self.bq.rand_funct() for i in range(nb_table)]
        data_list = []
        for minterms in minterms_table:
            data_list.append( self._prepare_kmap_data(minterms=minterms,
                                          dontcares=[],
                                          correct=True,
                                          variables=self.bq.variables
                                           )
                              )

        context = {"data_list":data_list}
        return context
        # return self._render(SECTION_MAP, context)


    def question_map_for_sop(self,nb=2):
        self.bq.reset_vars()
        minterms_table =[self.bq.rand_funct() for i in range(nb)]
        data_list = []
        for minterms in minterms_table:
            data_list.append( self._prepare_kmap_data(minterms=minterms,
                                          dontcares=[],
                                          correct=True,
                                          variables=self.bq.variables
                                           )
                              )

        context = {"data_list":data_list}
        return context
        # return self._render(SECTION_MAP_SOP, context)


    def question_funct(self, ):

        self.bq.reset_vars()
        sop_quest, minterms = self.bq.rand_exp()

        sop_quest = self.formater.normalize_formula(sop_quest)

        context  = self._prepare_kmap_data(minterms=minterms,
                                      dontcares=[],
                                      correct=True,
                                      variables=self.bq.variables
                                       )

        sop, pos = self.bq.simplify(minterms)
        # logigram = self.formater.draw_logigram(sop, function_name='F',
        #                                       variables=self.bq.variables)
        context["sop_quest"] = sop_quest
        context["logicdiagram"] = ""
        equations_list = [{"sop": sop,
                           "pos": pos,
                           "nor_pos": context.get("nor_pos", ""),
                           "nand_sop": context.get("nand_sop", '')},
                          ]
        logigramdict = self.formater.prepare_logigram_list([sop, ], function_namelist=["F",],
                                                   variables=["A","B","C","D"], equations_list=equations_list)
        context["logicdiagramdict"] = logigramdict
        # question, answer = self.formater.render_question_answer("bool/function", context)
        return context
        # return self._render(SECTION_FUNCTION, context)



    def get_terms(self,expr,method="sop"):
        """split an expression into terms"""
        seps = {
            'sop':"+",
            'nand':bool_const.BIG_NAND_SYMB,
            'nor':bool_const.BIG_NOR_SYMB,
            'pos':".",
        }
        sep = seps.get(method.lower(),"+")
        return [[t.strip() for t in term.split(".")] for term in expr.split("+")]

    def question_static_funct(self, minterms, var_names=["A","B","C","D"], output_names=["S0","S1","S2","S3"], dont_care=[] ):

        self.bq.set_vars(var_names, output_names)

        sop_quest = ""
        fname = output_names[0]
        context = self._prepare_kmap_data(minterms=minterms,
                                          dontcares=dont_care,
                                          correct=True,
                                          variables=var_names,
                                          function_name=fname
                                          )

        sop, pos = self.bq.simplify(minterms)
        # logigram = self.formater.draw_logigram(sop, function_name=fname,
        #                                        variables=var_names)
        context["sop_quest"] = sop_quest
        context["logicdiagram"] = ""
        context["terms"] = [[t.strip() for t in term.split(".")] for term in sop.split("+")]
        equations_list  = [{"sop": sop,
                               "pos": pos,
                               "nor_pos": context.get("nor_pos", ""),
                               "nand_sop": context.get("nand_sop", '')},
                            ]
        logigramdict = self.formater.prepare_logigram_list([sop, ], function_namelist=[fname,],
                                                   variables=var_names,  equations_list= equations_list)
        context["logicdiagramdict"] = logigramdict
        # question, answer = self.formater.render_question_answer("bool/function", context)
        # return question, "arabic", "data", answer
        return context
        # return self._render(SECTION_FUNCTION, context)



    def question_static_nand_exp(self, minterms, var_names=["A", "B", "C", "D"], output_names=["S0", "S1", "S2", "S3"],
                                 dont_care=[], method="nand"):
        self.bq.set_vars(var_names, output_names)

        sop_quest = ""
        fname = output_names[0]
        context = self._prepare_kmap_data(minterms=minterms,
                                          dontcares=dont_care,
                                          correct=True,
                                          variables=var_names,
                                          function_name=fname,
                                          method=method
                                          )

        sop, pos = self.bq.simplify(minterms)
        # logigram = self.formater.draw_logigram_nand_nor(sop, function_name=fname,
        #                                        variables=var_names, method=method)

        context["sop_quest"] = sop_quest
        context["logicdiagram"] = ""
        logigramdict = self.formater.prepare_logigram_list([sop, ], function_namelist=[fname,],
                                                   variables=var_names, method=method)
        context["logicdiagramdict"] = logigramdict
        # question, answer = self.formater.render_question_answer("bool/function", context)
        # return question, "arabic", "data", answer
        return context
        # return self._render(SECTION_FUNCTION, context)


    def question_multi_funct(self, minterms_list, var_names=["A","B","C","D"],
     output_names=["S0","S1","S2","S3"], dont_care_list=[], method=""):

        self.bq.set_vars(var_names, output_names)

        sop_quest = ""
        fname = output_names[0]
        # one truth table
        # multiple karnaugh map
        # one logigram
        data_list = []
        sop_list = []
        pos_list = []
        terms_list  = []
        equations_list  = []
        for minterms, dont_care, fname in zip(minterms_list, dont_care_list, output_names):
            data = self._prepare_kmap_data(minterms=minterms,
                                              dontcares=dont_care,
                                              correct=True,
                                              variables=var_names,
                                              function_name=fname
                                              )
            data_list.append( data )
            sop, pos = self.bq.simplify(minterms)
            # sop = self.formater.normalize_formula(sop)
            sop_list.append(sop)
            equations_list.append( {"sop":sop,
                                    "pos":pos,
                                    "nor_pos":data.get("nor_pos",""),
                                    "nand_sop":data.get("nand_sop",'')})

            # terms_list.append([[t.strip() for t in term.split(".")] for term in sop.split("+")])
        logigramdict = self.formater.prepare_logigram_list(sop_list, function_namelist=output_names,
                                                   variables=var_names, method=method, equations_list=equations_list)
        # old method to draw logigram used only for latex,
        # deprecated
        # logigram = self.formater.draw_logigram_list(sop_list, function_namelist=output_names,
        #                                            variables=var_names, method=method)
        context ={"data_list":data_list,
                  "minterms_list":minterms_list,
                  "dontcares_list": dont_care_list,
                  "function_name_list": output_names,
                  "variables": var_names,
                  "sop_quest":sop_quest,
                  # "terms_list":terms_list,
                  "logicdiagram" : "",#logigram,  # deprecated, used only for comparaison
                  "logicdiagramdict" : logigramdict,
                  "sop_list":sop_list,
                  "method":method,
                  }

        return context


    def question_exp(self,):

        self.bq.reset_vars()
        sop_quest, minterms = self.bq.rand_exp()

        sop_quest = self.formater.normalize_formula(sop_quest)

        context  = self._prepare_kmap_data(minterms=minterms,
                                      dontcares=[],
                                      correct=True,
                                      variables=self.bq.variables,
                                      function_name="S",
                                       )


        context["sop_quest"] = sop_quest
        return context



def main(args):
    pass

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

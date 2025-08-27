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
import random

from .codage import question_codage as question
from .bool import boolquiz
from .bool import bool_const
from .codage import ieee754
from .display import quiz_format_factory
from .sequentiel import tex_chronograms

class Question_Builder:
    """ Generate the question """
    def __init__(self, outformat="", config_file ="", lang="ar-en", templates_dir=""):
        self.qs = question.questionGenerator(latex=True)
        self.bq = boolquiz.bool_quiz()
        self.bq.set_format('')
        self.vf = ieee754.float_point()
        self.formater = quiz_format_factory.quiz_format_factory.factory(outformat, lang=lang, templates_dir=templates_dir)
        self.answer_formater = quiz_format_factory.quiz_format_factory.factory(outformat, lang=lang, templates_dir=templates_dir)


    def question_vf(self):
        x = self.vf.vf_question()
        # ieee_str = self.vf.IEEE754(x, True)
        ieee_dict = self.vf.ieee754_components(x)

        context = ieee_dict
        question, answer = self.formater.render_question_answer("encoding/float", context)
        return question, "arabic", "data", answer


    def question_cp(self,):
        n, a, cp1, cp2 = self.qs.comp_one(8)
        context = {
            "number": n,
            "binary": a,
            "cp1": cp1,
            "cp2": cp2,
        }

        question, answer = self.formater.render_question_answer("encoding/cp", context)
        return question, "arabic", "data", answer

    def question_intervalle(self,):

        n = self.qs.intervalle()

        context = {
            "number": n,
        }

        question, answer = self.formater.render_question_answer("encoding/interval", context)
        return question, "arabic", "data", answer


    def question_base(self,):

        res =self.qs.rand_numeral_system()
        number = res.get("number",0)
        in_base =   res.get("in_base", 10)
        out_base = res.get("out_base", 10)
        output = res.get("output",0)
        steps_from10 = []
        steps_to10 = []
        number_tmp = 0
        binary_mode = False

        if in_base == 10 and out_base != 10:
            steps_from10 = self.qs.make_steps_from10(number, out_base)
        elif in_base != 10 and out_base == 10:
            steps_to10 = self.qs.number_to_digits(number, in_base)
        elif in_base in (2,8,16) and out_base in (2,8,16):
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
            "binary_mode":binary_mode,

        }

        question, answer = self.formater.render_question_answer("base", context)
        return question, "arabic", "data", answer



    def question_bcd_x3(self, scheme="", method=""):


        number  = random.randint(10, 10**5)

        bcd = self.qs.dec_to_bcd(number)
        bcd_digits = bcd.split(" ")
        x3 = self.qs.dec_to_excess3(number)
        x3_digits = x3.split(" ")
        number_a  = number
        number_b  = random.randint(10, 10**5)
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


        question, answer = self.formater.render_question_answer("encoding/bcdx3", context)
        return question, "arabic", "data", answer

    def question_gray(self,):

        x  = random.randint(15, 256)

        x_bin = self.qs.int2base(x, 2)
        x_gray = self.qs.binary_to_gray(x_bin)
        seq_len  = random.randint(2, 10)
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

        question, answer = self.formater.render_question_answer("encoding/gray", context)
        return question, "arabic", "data", answer

    def question_unicode(self,):

        text  = self.qs.rand_numeral_system()
        context = {
            "text": self.formater.escape_string(text),
            "method": "encode",

        }

        question, answer = self.formater.render_question_answer("encoding/charcodes", context)
        return question, "arabic", "data", answer

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

        question, answer = self.formater.render_question_answer("encoding/charcode", context)
        return question, "arabic", "data", answer

    def question_arithm(self,):

        res =self.qs.rand_arithm()

        question =u"Faire les opérations suivantes: "
        answer = res.get('reponse','')
        arabic = u"أنجز العمليات الآتية: "

        context = res

        question, answer = self.formater.render_question_answer("arithm", context)
        return question, "arabic", "data", answer
        
    def question_mesure(self,):
        
        res =self.qs.rand_arithm()       

        question =u"Faire les conversion suivantes: NOT IMPLEMENTED (MESURE questions) "
        answer = res.get('reponse','')


        return question, "arabic", "data", answer

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
        question, answer = self.formater.render_question_answer("bool/map", context)
        return question, "arabic", "data", answer


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
        question, answer = self.formater.render_question_answer("bool/map-sop", context)
        return question, "arabic", "data", answer


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
        logigram = self.formater.draw_logigram(sop, function_name='F',
                                              variables=self.bq.variables)
        context["sop_quest"] = sop_quest
        context["logicdiagram"] = logigram
        equations_list = [{"sop": sop,
                           "pos": pos,
                           "nor_pos": context.get("nor_pos", ""),
                           "nand_sop": context.get("nand_sop", '')},
                          ]
        logigramdict = self.formater.prepare_logigram_list([sop, ], function_namelist=["F",],
                                                   variables=["A","B","C","D"], equations_list=equations_list)
        context["logicdiagramdict"] = logigramdict
        question, answer = self.formater.render_question_answer("bool/function", context)
        return question, "arabic", "data", answer
        # ~ answer += self.bq.draw_logigram(sop)

        return question, "arabic", "data", answer


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
        logigram = self.formater.draw_logigram(sop, function_name=fname,
                                               variables=var_names)
        context["sop_quest"] = sop_quest
        context["logicdiagram"] = logigram
        context["terms"] = [[t.strip() for t in term.split(".")] for term in sop.split("+")]
        equations_list  = [{"sop": sop,
                               "pos": pos,
                               "nor_pos": context.get("nor_pos", ""),
                               "nand_sop": context.get("nand_sop", '')},
                            ]
        logigramdict = self.formater.prepare_logigram_list([sop, ], function_namelist=[fname,],
                                                   variables=var_names,  equations_list= equations_list)
        context["logicdiagramdict"] = logigramdict
        question, answer = self.formater.render_question_answer("bool/function", context)
        return question, "arabic", "data", answer



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
        logigram = self.formater.draw_logigram_nand_nor(sop, function_name=fname,
                                               variables=var_names, method=method)

        context["sop_quest"] = sop_quest
        context["logicdiagram"] = logigram
        logigramdict = self.formater.prepare_logigram_list([sop, ], function_namelist=[fname,],
                                                   variables=var_names, method=method)
        context["logicdiagramdict"] = logigramdict
        question, answer = self.formater.render_question_answer("bool/function", context)
        return question, "arabic", "data", answer


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
        logigram = self.formater.draw_logigram_list(sop_list, function_namelist=output_names,
                                                   variables=var_names, method=method)
        context ={"data_list":data_list,
                  "minterms_list":minterms_list,
                  "dontcares_list": dont_care_list,
                  "function_name_list": output_names,
                  "variables": var_names,
                  "sop_quest":sop_quest,
                  # "terms_list":terms_list,
                  "logicdiagram" : logigram,  # deprecated, used only for comparaison
                  "logicdiagramdict" : logigramdict,
                  "sop_list":sop_list,
                  "method":method,
                  }
        question, answer = self.formater.render_question_answer("bool/multi_funct", context)
        return question, "arabic", "data", answer


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

        question, answer = self.formater.render_question_answer("bool/exp", context)
        return question, "arabic", "data", answer
    #
        
    def question_chronogram(self, varlist={}, flip_type="D", length=20, synch_type="rising", output_vars=["Q",]):
        
        """
        Generate Chronogram question
        """      
        chrono = tex_chronograms.Tex_Chronograms();
        # generate random signals 
        # according to prameters
        # ~ signals = {"D":[-1, 3, -0.5, +1.5, -5, 3.5, -6.5],
                   # ~ "Q":[-1] }
        if not varlist:
            varlist = {"D":1, "R":-1, "S":-1}
        signals ={}
        for key in varlist:
            if key in output_vars:
                # add an empty signal
                signals[key] = [varlist[key],]
            else:
                signal_dict = chrono.question({key:varlist[key]}, length=length)
                signals[key] = signal_dict[key]
        # ~ signals = chrono.question(varlist, length=length)
        logging.debug("quiz_builder:signals", signals)
        # set synchronization type
        chrono.set_synch_type(synch_type)
        
        # generate question
        # 1- clock
        # 2- signals without solution
        clock = chrono.clock_signal(length=length, period=1)        
        tex_data_question = chrono.draw(signals, clock)        
        
        # generate soltution
        # get solution for signal
        # 2 generate chrono for answer
        # if we want to generate multiple cases using "dual" or "all"
        logging.debug("initial: ",signals)
        if synch_type =="all" or synch_type =="dual":
            # set synchronization type
            chrono.set_synch_type("rising")
        out_signal = chrono.resolve(flip_type=flip_type,signals=signals.copy(), period=2) 
        # output signal    
        tmp_signals =    signals
        tmp_signals[output_vars[0]] = out_signal
        logging.debug("rising: ",out_signal)
        logging.debug("rising: ",signals)
        # add more signals for multi cases
        if synch_type =="all" or synch_type =="dual":
            # set synchronization type
            chrono.set_synch_type("falling")

            out_signal = chrono.resolve(flip_type=flip_type,signals=signals.copy(), period=2) 
            logging.debug("falling: ",signals)
            logging.debug("falling: ",out_signal)
            # output signal       
            tmp_signals[output_vars[0]+".desc"] = out_signal
        if synch_type =="all":
            # set synchronization type
            chrono.set_synch_type("asynch")
            out_signal = chrono.resolve(flip_type=flip_type,signals=signals.copy(), period=2) 
            # output signal       
            logging.debug("asynch: ",out_signal)
            logging.debug("asynch: ",signals)
            tmp_signals[output_vars[0]+".asyn"] = out_signal
        
        if synch_type =="all" or synch_type =="dual":
            # set synchronization type
            chrono.set_synch_type("dual")            
        
        tex_data_answer = chrono.draw(tmp_signals, clock)
            
        question =u"Complete the following timing diagram:\n\n "
        arabic = u"أكمل المخطط الزمني: "
        
        # make a figure
        answer ="""Chronogramme\n\n\n
        \\scalebox{2}{ %% scale
        %s
        } %%scale\n\n"""%tex_data_answer
        # use scale attribute isntead of scale command
        # ~ answer = tex_data_answer
        
        data ="""\n\n%s\n\n"""%tex_data_question
        # ~ data = tex_data_question

        return question, arabic, data, answer        





def main(args):
    pass

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

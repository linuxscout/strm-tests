#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz_format.py
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
# used for generating truth table
from jinja2 import Environment, FileSystemLoader, TemplateNotFound


import itertools
from . import format_const
from ..bool import logigram

class quiz_format:
    """ Generate a format for the test """
    def __init__(self, formatting="", lang="ar-en", templates_dir=""):
        self.formatting = formatting
        self.output = []
        self.tests = []
        self.newline = "\n"
        self.lang = lang
        self.templates_dir = templates_dir
        self.env = Environment(loader=FileSystemLoader(self.templates_dir),
                               trim_blocks=True,
                               lstrip_blocks=True,
                               )
        self.env.filters['group4'] = self.group_digits_by_4
        self.group_digit_sep = " "
        # self.variables = ["a","b","c","d"]
        #~ print("quiz_format")
    def header(self,):
        """
        """
        pass
    def footer(self,):
        """
        """
        pass
    def set_header(self,header):
        """
        """
        self.header = header
    def set_footer(self, footer):
        """
        """
        self.footer = footer
    def reset_output(self):
        """
        """
        self.output = []        
    def add_test(self, quiz_question_list):
        """
        """
        self.tests.append(quiz_question_list)


    def group_digits_by_4(self, value):
        try:
            s = str(value)
            int_part, dot, frac_part = s.partition('.')

            # Group integer part from the right
            int_groups = [int_part[max(i - 4, 0):i] for i in range(len(int_part), 0, -4)]
            int_part_grouped = self.group_digit_sep.join(reversed(int_groups))

            # Group fractional part from the left (if any)
            if frac_part:
                frac_groups = [frac_part[i:i + 4] for i in range(0, len(frac_part), 4)]
                frac_part_grouped = self.group_digit_sep.join(frac_groups)
                return f"{int_part_grouped}.{frac_part_grouped}"
            else:
                return int_part_grouped
        except Exception:
            return value  # fallback
    def render_question_answer(self, template_base: str, context: dict) -> tuple[str, str]:
        """
        عرض نص السؤال والجواب باستخدام القوالب المناسبة للغة والتنسيق.

        Args:
            template_base (str): اسم الأساس للقالب (مثل 'float' أو 'intervalle')
            context (dict): البيانات المستعملة في القالب

        Returns:
            tuple[str, str]: (نص السؤال، نص الجواب)
        """
        q_template_name = f"{template_base}/question.{self.formatting}"
        # a_template_name = f"{template_base}/answer.{self.formatting}"

        try:
            question_template = self.env.get_template(q_template_name)
            # answer_template = self.env.get_template(a_template_name)
        except TemplateNotFound as e:
            raise FileNotFoundError(f"Template '{e.name}' not found in {self.templates_dir}.")
        except Exception as e:
            import traceback
            traceback.print_exc()
        context["languages"] = ["ar","en", "fr"]

        context["RENDER_MODE"] = "question"
        question = question_template.render(context)
        context["RENDER_MODE"] = "answer"
        answer = question_template.render(context)

        return question, answer

    def add_question(self, quiz_question):
        """
        Add a question as  template 
        """
        # the test question contains parameters to generate a specific template
        # the category attribute get the destination template
        
        temp = self.get_template(quiz_question.get("catagory",""))
        if temp:
            newtext = temp.safe_substitute(quiz_question)
        else:
            newtext = self.newline.join(quiz_question.values())
        self.tests.append(newtext)

    def add_section(self, text, trans ="", level=1):
        """
        """

        newtext ="\n"+"#"*level + " " + text + " " + trans
        self.output.append(newtext)
        return newtext
        
    def add_text(self, text, trans=""):
        """
        """
        newtext ="\n"+ text + "\n"+ trans
        self.output.append(newtext)
        return newtext
        
    def add_verbatim(self, text, trans =""):    
        
        newtext  ="\n```\n"+ text + "\n```\n" + trans
        self.output.append(newtext)
        return newtext        

    def open_question(self, question_type):
        newtext =     ''
        self.output.append(newtext)
        return newtext
        
    def close_question(self, question_type):
        newtext =     ''
        self.output.append(newtext)
        return newtext
        
    def open_enumerate(self):
        newtext =     ''
        self.output.append(newtext)
        return newtext
        
    def open_itemize(self):
        newtext =     ''
        self.output.append(newtext)
        return newtext
        
    def close_enumerate(self):
        newtext =     ''
        self.output.append(newtext)
        return newtext
        
    def add_item(self, text):
        newtext =     ' -  '+  text +"\n"
        self.output.append(newtext)
        return newtext
        
    def close_itemize(self):
        newtext =     ''
        self.output.append(newtext)
        return newtext
        
    def open_minipage(self):
        newtext =     ''
        self.output.append(newtext)
        return newtext
        
    def close_minipage(self):
        newtext =     ''
        self.output.append(newtext)
        return newtext   
             
    def set_save(self):
        """
        Save added string to output
        """
        self.save = True

    def disable_save(self):
        """
        Save added string to output
        """
        self.save = False
    
    def display(self,):
        """
        """
        self.output = []
        # tests is a list
        # test is a list of dict
        self.add_section("Question", level=1)        
        for test in self.tests: 
            # print only test questions
            # question is a dict
            # ~ id":q_no,
            # ~ "question":q,
            # ~ "arabic":ar,
            # ~ "data":data,
            # ~ "answer":ans,  
            for question in test:
                # print question
                self.add_section(question.get("id","ID"),level=4)
                # self.add_text(question.get("question","QUESTION"),question.get("arabic","ARABIC"))
                self.add_text(question.get("question","QUESTION"))
                # self.add_text(question.get("data","DATA"))
            self.add_hrule()
            self.add_newpage()
            self.add_section("Correction",level=2)                
            # print correction
            # print section Correction
            # print page break
            for question in test:
                self.add_section(question.get("id","ID"),level=4)
                self.add_text(question.get("answer","ANSWER"))
            self.add_newpage() 

        return self.newline.join(self.output)
        
    def add_formula(self, text, trans=""): 
        
        newtext = ' [%s]'%text
        self.output.append(newtext)
        return newtext        
    
    def add_newline(self):  
          
        newtext= '\n'
        self.output.append(newtext)
        return newtext
        
    def add_hrule(self):    
        newtext= '\n-------------------------'
        self.output.append(newtext)
        return newtext
        
    def add_newpage(self):    
        newtext= '\n\n'
        self.output.append(newtext)
        return newtext    
            
    def reset(self,):
        self.output = []

    def truth_table(self, minterms, dontcares=[], variables=[], vars_outputs = []): 
        """ print truth table """
        # ~ variables = self.variables
        cases = itertools.product([0,1],[0,1],[0,1],[0,1])
        text = "N°\t" # line number
        text = "\t".join(variables)
        text = "\t"+ vars_outputs[0]
        
      
        
           
        for counter, item in enumerate(cases):
            f = 1 if counter in minterms else 0
            case = [counter] + list(item)+ [f]
            text += "\t".join([str(x) for x in case]) +"\n"


        return text

        
    def multiple_truth_table(self, minterms_list, dontcares_list=[], variables = [], vars_outputs= [] ): 
        """ print truth table for multiple function"""
        
        outputs_len= len(minterms_list)
        cases = itertools.product([0,1],[0,1],[0,1],[0,1])
        text = "N°\t"  # line number
        text = "\t".join(variables + vars_outputs[:outputs_len])
           
        for counter, item in enumerate(cases):
            case = [counter] + list(item)          

            for minterms, dontcares in zip(minterms_list, dontcares_list) :
                if counter in minterms:
                    f = 1
                elif counter in dontcares:
                    f = "X"
                else:
                    f = 0
                case.append(f)
            text += "\t".join([str(x) for x in case]) +"\n"

        return text
    # def set_vars(self, variables=[]):
    #     if variables:
    #         self.variables = variables
    def normalize_formula(self,s):
        """ normalize boolean string"""
        return str(s)

    def draw_map(self, minterms, dontcares=[], correct = False, variables = [], simply_terms=[], method="sop"):
        kmap=[]
        maxterms = [x for x in range(16) if x not in minterms and x not in dontcares]
        for x in range(16):
            if x  in minterms:
                kmap.append("1")
            elif x in dontcares:
                kmap.append("x")
            else:
                kmap.append("0")
        # ~ var_names  = "ab\\cd"
        var_names  = "".join(variables[:2])+"\\"+ "".join(variables[2:])
        table = [ [var_names,  "00","01", "11","10"],
        ["00", kmap[0], kmap[1],kmap[3],kmap[2]],
        ["00", kmap[4], kmap[5],kmap[7],kmap[6]],
        ["00", kmap[12], kmap[13],kmap[15],kmap[14]],
        ["00", kmap[8], kmap[9],kmap[11],kmap[10]],
        ]
        
        # draw simplification
        simplification = ""
        if correct:
            simplification = self.simplify_map(simply_terms)
        
        text = "\n".join(["\t".join(r) for r in table])
        cd = "".join(variables[2:])
        ab = "".join(variables[:2])
       

        return text

    def simplify_map(self, terms =[], method='and'):
        """
        Gererate diplay for terms
        """
        simpls = self.format_map_terms(terms=terms, method=method)
        return "\n".join(simpls)

    def format_map_terms(self, terms =[], method="sop"):
        """
        Gererate diplay for terms
        """

        if method in ("or","nor","pos"):
            pass
        else:
            pass

        simpls = terms

        return terms
    def draw_logigram(self, sop, function_name = "F", variables = []):
        """ draw a logigram """
        varnames = {
            "A":variables[0],
            "B":variables[1],
            "C":variables[2],
            "D":variables[3],
        }
        lggm ="Draw Logigramm in Text mode, not implemented"
        return lggm
    
    def draw_logigram_nand_nor(self, sop, function_name = "F", variables = [], method="NAND"):
        """ draw a logigram """
        varnames = {
            "A":variables[0],
            "B":variables[1],
            "C":variables[2],
            "D":variables[3],
        }
        lggm ="Draw Logigramm in Text mode, not implemented"
        return lggm
    def draw_logigram_list(self, sop_list, function_namelist = ["F",], variables = [], method="and"):
        """ draw a logigram """
        varnames = {
            "A":variables[0],
            "B":variables[1],
            "C":variables[2],
            "D":variables[3],
        }
        lggm ="Draw Logigramm in Text mode, not implemented"
        return lggm
    def prepare_logigram_list(self, sop_list, function_namelist = ["F",], variables = [], method="", equations_list=[]):
        """ draw a logigram """
        varnames = {
            "A":variables[0],
            "B":variables[1],
            "C":variables[2],
            "D":variables[3],
        }
        lg = logigram.logigram(varnames, method=method)
        lgdict = lg.prepare_logigram_list(sop_list, function_namelist, equations_list=equations_list)
        ## format labels
        for func_item in lgdict.get("functions", []):
            for term in func_item.get("terms", []):
                label = term.get("label", {})
                if "default" in label:
                    label["formatted"] = self.normalize_formula(label["default"])
        return lgdict


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

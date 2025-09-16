#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz_format_tex.py
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

import itertools
import re
from . import quiz_format
from . import format_const
from ..bool import logigram
from ..bool import bool_const

class quiz_format_tex(quiz_format.quiz_format):
    """ Generate a format for the test """
    def __init__(self, formatting="", lang="", templates_dir=""):
        super().__init__( formatting="tex", lang=lang, templates_dir=templates_dir)
        self.formatting = "tex"
        self.output = [] 
        self.header =""
        self.footer =""
        self.newline = "\n"
        self.group_digit_sep = "\,"
   
    def header(self,):
        """
        """
        self.header = """
        """
    def footer(self,):
        """
        """
        self.footer = """
        """
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
        
    def add_section(self, text, trans="", level=1):
        """
        """
        if level == 1:
            sect = "section"
        elif level == 2:
            sect = "subsection"
        elif level == 3:
            sect = "subsubsection"
        elif level == 4:
            sect = "paragraph"
        newtext = "\n\\%s{%s}\n"%(sect, text)
        self.output.append(newtext)
        return newtext
        
    def add_text(self, text, trans=""):
        """
        """
        self.output.append(text)
        return text
        
    def add_verbatim(self, text, trans=""):    
        
        newtext = '\n\\begin{verbatim}'
        newtext += text
        newtext += '\n\\end{verbatim}'
        self.output.append( newtext)
        return newtext
    
    def add_formula(self, text, trans=""):
        
        # split formula into  lines
        # if line hasn't formula tags add it
        lines  = text.split("\n")
        newtext = ""
        for line in lines:
            if line.startswith("$") or "$" in line:
                newtext+= line + self.newline
            else:
                newtext+= "$$%s$$%s"%(line, self.newline)
        # ~ newtext =    '$$%s$$\n'%text
        self.output.append(newtext)
        return newtext

    def open_enumerate(self):
        newtext =     '\\begin{enumerate}'
        self.output.append(newtext)
        return newtext
    def open_itemize(self):
        newtext =     '\\begin{itemize}'
        self.output.append(newtext)
        return newtext
    def close_enumerate(self):
        newtext =     '\\end{enumerate}'
        self.output.append(newtext)
        return newtext
    def add_item(self, text):
        newtext =     '\\item '+  text 
        self.output.append(newtext)
        return newtext
    def close_itemize(self):
        newtext =     '\\end{itemize}'
        self.output.append(newtext)
        return newtext
    def open_minipage(self):
        newtext =     '\\begin{minipage}{.5\\textwidth}\n'
        self.output.append(newtext)
        return newtext
    def close_minipage(self):
        newtext =     '\\end{minipage}\n'
        self.output.append(newtext)
        return newtext
    def add_newline(self):    
        self.output.append(self.newline)
    def add_hrule(self):    
        self.output.append('\n\n\\hrule width 1\linewidth')
    def add_newpage(self):    
        self.output.append('\pagebreak')

        # Escape for LaTeX
    @staticmethod
    def escape_string(s: str) -> str:
        replacements = {
            '\\': '\\textbackslash{}',
            '{': '\\{',
            '}': '\\}',
            '$': '\\$',
            '&': '\\&',
            '#': '\\hash{}',
            '_': '\\_{}',
            '%': '\\%',
            '^': '\\textasciicircum{}',
            '~': '\\textasciitilde{}',
        }
        return "".join([replacements.get(c,c) for c in s])


    def display2(self,):
        """
        """
        # ~ text = self.header
        # ~ text += "\n"+ self.output
        # ~ text += "\n"+ self.footer
        return "\n".join(self.output)

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
        return "\n".join(self.output)
        
 
    def truth_table(self, minterms, dontcares=[], variables=[], vars_outputs = []): 
        """ print truth table """
        # ~ variables = self.variables
        cases = itertools.product([0,1],[0,1],[0,1],[0,1])
        text = "N°\t" # line number
        text = "\t".join(variables)
        text = "\t"+ vars_outputs[0]
        
      
        
        tex = """%%\\begin{table}
        \\begin{tabular}{|c|c|c|c|c||c|}
    \\toprule
        """
        tex += "N° & " # line number
        tex += " & ".join(variables) 
        tex += " & "+ vars_outputs[0]
        tex += "\\\\ \\midrule"
           
        for counter, item in enumerate(cases):
            f = 1 if counter in minterms else 0
            case = [counter] + list(item)+ [f]
            if counter  and counter %4 ==0 :
                tex += "\\midrule"
            text += "\t".join([str(x) for x in case]) +"\n"
            tex += " & ".join([str(x) for x in case]) + "\\\\"

        tex += """\\bottomrule
        \\end{tabular}
        %%\\end{table}
        """
        self.output += tex
        return tex
    def multiple_truth_table(self, minterms_list, dontcares_list=[], variables = [], vars_outputs= [] ): 
        """ print truth table """
        
        outputs_len= len(minterms_list)
        cases = itertools.product([0,1],[0,1],[0,1],[0,1])
        text = "N°\t"  # line number
        text = "\t".join(variables + vars_outputs[:outputs_len])
        tex = """%%\\begin{table}\n
        \\begin{tabular}{|c|c|c|c|c||%s}\n
    \\toprule\n
        """%("c|"*outputs_len)
        tex += "N° &"  # line number
        tex += " & ".join(variables+vars_outputs[:outputs_len]) 
        tex += "\\\\ \\midrule\n"
           
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
            if counter  and counter %4 == 0 :
                tex += "\\midrule\n"
            text += "\t".join([str(x) for x in case]) +"\n"
            tex += " & ".join([str(x) for x in case]) + "\\\\\n"

        tex += """\\bottomrule\n
        \\end{tabular}\n
        %%\\end{table}\n
        """
        self.output.append(tex)
        
        return tex


    def normalize_formula2(self,s):
        """ normalize boolean string"""
        s= str(s)
        for v in self.variables:
            s = s.replace(f"{v.lower()}'", f'\\bar {v.lower()}')
            s = s.replace(f"{v.upper()}'", f'\\bar {v.upper()}')
        return s
    @staticmethod
    def normalize_formula(expr: str) -> str:
        # Match a word (letters/numbers/underscore) followed by a '
        expr = re.sub(r"([A-Za-z0-9_]+)'", r"\\overline{\1}", expr)
        # 3. Handle LaTeX \overline{...} -> MathML mover
        s = expr
        while True:
            s_out = re.sub(
                r"¬\{([^}]+)\}",
                r"\\overline{\1}",
                s
            )
            if s_out == s:
                break
            s = s_out
        # 5. Replace sum/product/uparrow/downarrow with MathML entities
        symbols = {
            bool_const.BIG_NAND_SYMB: '\\big\\uparrow ',
            bool_const.NAND_SYMB: "\\uparrow ",
            bool_const.BIG_NOR_SYMB: '\\big\\downarrow ',
            bool_const.NOR_SYMB: '\\downarrow ',

        }
        for k, v in symbols.items():
            s = s.replace(k, v)

        return s

    def draw_map(self, minterms, dontcares=[], correct = False, variables = [], simply_terms=[],
    method="sop"):
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
            simplification = self.simplify_map(simply_terms, method=method)
        
        text = "\n".join(["\t".join(r) for r in table])
        cd = "".join(variables[2:])
        ab = "".join(variables[:2])
        tex =  """\\begin{karnaugh-map}[4][4][1][%s][%s]"""%(cd, ab)
        tex +=  """
          \\minterms{%s}
          \\maxterms{%s}
        %%\\autoterms[0]
         \\terms{%s}{X}
        %% simplification
        %s
          %%\\implicant{5}{15}
          %%\\implicantedge{8}{8}{10}{10}
          %%\\implicantedge{8}{8}{10}{10}[8,10]
        \\end{karnaugh-map}"""%(", ".join([str(x) for x in minterms]), 
        ", ".join([str(x) for x in maxterms]),
        ", ".join([str(x) for x in dontcares])
        , simplification)

        self.output.append(tex)
        return tex

    def simplify_map(self, terms =[], method="sop"):
        """
        Gererate diplay for terms
        """
        #print(terms)
        simpls = self.format_map_terms(terms=terms, method=method)
        return "\n".join(simpls)

    def format_map_terms(self, terms =[], method="sop"):
        """
        Gererate diplay for terms
        """

        if method in ("or","nor","pos"):
            reduction_table = format_const.TEX_REDUCTION_TABLE_POS
            # remove extra parenthesis
            terms = [t.replace("(", "").replace(")", "") for t in terms]
            # terms = [t.replace(")",'') for t in terms]
        else:
            reduction_table = format_const.TEX_REDUCTION_TABLE

        simpls = [reduction_table.get(term, "") for term in terms]

        return simpls
        
    
    def draw_logigram(self, sop, function_name = "F", variables = []):
        """ draw a logigram """
        varnames = {
            "A":variables[0],
            "B":variables[1],
            "C":variables[2],
            "D":variables[3],
        }
        lg = logigram.logigram(varnames)
        return lg.draw_logigram(sop, function_name)
    
    def draw_logigram_nand_nor(self, sop, function_name = "F", variables = [], method="NAND"):
        """ draw a logigram """
        varnames = {
            "A":variables[0],
            "B":variables[1],
            "C":variables[2],
            "D":variables[3],
        }
        lg_maker = logigram.logigram(varnames)
        lggrm = lg_maker.draw_logigram(sop, function_name)
        # substitute gates into nand
        if method.upper()=="NAND":
            lggrm = lggrm.replace("[and gate US,", "[nand gate US,")
            lggrm = lggrm.replace("[or gate US,", "[nand gate US,")
            lggrm = lggrm.replace("[not gate US, draw, rotate=270]", "[nand gate US, draw, rotate=270, scale=0.5, logic gate inputs=nn]")
        elif method.upper()=="NOR":
            lggrm = lggrm.replace("[and gate US,", "[nor gate US,")
            lggrm = lggrm.replace("[or gate US,", "[nor gate US,")
            lggrm = lggrm.replace("[not gate US, draw, rotate=270]", "[nor gate US, draw, rotate=270, scale=0.5, logic gate inputs=nn]")
        if method.upper()=="NAND" or method.upper()=="NOR":
            lggrm = lggrm.replace("(notx.input)", "(notx.input 1)")
            lggrm = lggrm.replace("(noty.input)", "(noty.input 1)")
            lggrm = lggrm.replace("(notz.input)", "(notz.input 1)")
            lggrm = lggrm.replace("(notw.input)", "(notw.input 1)")
        return lggrm
    def draw_logigram_list(self, sop_list, function_namelist = ["F",], variables = [], method=""):
        """ draw a logigram """
        varnames = {
            "A":variables[0],
            "B":variables[1],
            "C":variables[2],
            "D":variables[3],
        }
        lg = logigram.logigram(varnames, method=method)
        return lg.draw_logigram_list(sop_list, function_namelist)

    @staticmethod
    def _wrap_arabic(txt, mode="inline"):
        if mode == "par":
            return f"\n\\begin{{arab}}[utf]\n {txt}\n \\end{{arab}}\n"
        if mode == "inline":
            return f"\\aRL{{{txt}}}"
        else:
            return f"\\aRL{{{txt}}}"
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

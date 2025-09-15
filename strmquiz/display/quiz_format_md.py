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
import html
from . import quiz_format
from . import format_const
from ..bool import bool_const


class quiz_format_md(quiz_format.quiz_format):
    """ Generate a format for the test """
    def __init__(self, formatting="", lang ="ar-en", templates_dir=""):
        super().__init__( formatting="md", lang=lang, templates_dir=templates_dir)
        self.formatting = "md"
        self.output =  []
        self.header =""
        self.footer =""
        self.newline = "\n"


   
    def header(self,):
        """
        """
        self.header = ""
    def footer(self,):
        """
        """
        self.footer = ""
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
    def open_enumerate(self):
        newtext =     '\n'
        self.output.append(newtext)
        return newtext
        
    def open_itemize(self):
        newtext =     '\n'
        self.output.append(newtext)
        return newtext
        
    def close_enumerate(self):
        newtext =      '\n'
        self.output.append(newtext)
        return newtext
        
    def add_item(self, text):
        newtext =     f'- {text}\n'
        self.output.append(newtext)
        return newtext
        
    def close_itemize(self):
        newtext =      '\n'
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
        
    def add_section(self, text, trans="", level=1):
        """
        """
        if level == 1:
            sect = "# "
        elif level == 2:
            sect = "## "
        elif level == 3:
            sect = "### "
        elif level == 4:
            sect = "#### "
        newtext = f"\n{sect} {text}\n"
        self.output.append(newtext)
        return newtext
        
    def add_text(self, text, trans=""):
        """
        """
        newtext ="\n"+ text
        self.output.append(newtext)
        return newtext        
    def add_verbatim(self, text, trans=""):    
        newtext = f'\n```{text}```\n'
        self.output.append(newtext)
        return newtext
    
    def add_formula(self, text, trans=""): 
        
        text = self.normalize_formula(text)   
        newtext = f'<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow>{text}</mrow></math>'
        newtext += self.newline
        self.output.append(newtext)
        return newtext    
    def add_newline(self):    
        newtext= '\n'
        self.output.append(newtext)
        return newtext          
    def add_hrule(self):    
        newtext= '\n--------\n'
        self.output.append(newtext)
        return newtext          
    def add_newpage(self):    
        newtext= '' 
        self.output.append(newtext)
        return newtext



    # Escape for HTML
    @staticmethod
    def escape_string(s: str) -> str:
        return "".join([html.escape(x) for x in s])
    # ~ def display(self,):
        # ~ """
        # ~ """
        # ~ return "\n".join(self.output)
        # ~ return repr(self.tests)
    def truth_table(self, minterms, dontcares=[], variables=[], vars_outputs = []): 
        """ print truth table """
        # ~ variables = self.variables
        cases = itertools.product([0,1],[0,1],[0,1],[0,1])
        # ~ text = "N°\t" # line number
        # ~ text = "\t".join(variables)
        # ~ text = "\t"+ vars_outputs[0]
        
        text = "<table border='1'>\n"
        text += "<tr><th>N°</th><th>"  # line number
        text += "</th><th>".join(variables) + "</th><th>"+ vars_outputs[0]+"</th>" 
        text += "</tr>\n"      
        
           
        for counter, item in enumerate(cases):
            f = 1 if counter in minterms else 0
            case = [counter] + list(item)+ [f]
            text += "<tr><td>"
            # ~ text += "\t".join([str(x) for x in case]) +"\n"
            text += "</td><td>".join([str(x) for x in case]) +"</td>"
            text += "</tr>\n"   
        text +="</table>\n"

        return text

        
    def multiple_truth_table(self, minterms_list, dontcares_list=[], variables = [], vars_outputs= [] ): 
        """ print truth table for multiple function"""
        
        outputs_len= len(minterms_list)
        cases = itertools.product([0,1],[0,1],[0,1],[0,1])
        text = "<table border='1'>\n"
        text += "<tr><th>N°</th><th>"  # line number
        text += "</th><th>".join(variables + vars_outputs[:outputs_len]) + "</th>"
        text += "</tr>\n"
           
        for counter, item in enumerate(cases):
            case = [counter] + list(item)          
            text += "<tr><td>"
            for minterms, dontcares in zip(minterms_list, dontcares_list) :
                if counter in minterms:
                    f = 1
                elif counter in dontcares:
                    f = "X"
                else:
                    f = 0
                case.append(f)
            text += "</td><td>".join([str(x) for x in case]) +"</td>"
            text += "</tr>\n"   
        text +="</table>\n"

        return text    
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
        text = "<table border='1'>\n<tr><td>\n"
        text += "</td></tr>\n<tr><td>".join(["</td><td>".join(r) for r in table])
        # ~ cd = "".join(variables[2:])
        # ~ ab = "".join(variables[:2])
        text += "</td></tr>\n</table>\n"       

        return text

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

    @staticmethod
    def normalize_formulaX( s: str):
        """Normalize a boolean string into MathML"""

        s = str(s)

        # 1. Handle negation with trailing prime: A' -> <mover>...</mover>
        s = re.sub(
            r"([A-Za-z0-9_]+)%s"%bool_const.NOT_VAR_SYMB,
            r"<mover><mi>\1</mi><mo>&OverBar;</mo></mover>",
            s
        )

        # 2. Handle LaTeX \overline{...} -> MathML mover
        while True:
            s_out = re.sub(
                r"\\overline\{([^}]+)\}",
                r"<mover><mrow>\1</mrow><mo>&OverBar;</mo></mover>",
                s
            )
            if s_out == s:
                break
            s = s_out
        # 3. Handle LaTeX \overline{...} -> MathML mover
        while True:
            s_out = re.sub(
                r"%s\{([^}]+)\}"%bool_const.NOT_TERM_SYMB,
                r"<mover><mrow>\1</mrow><mo>&OverBar;</mo></mover>",
                s
            )
            if s_out == s:
                break
            s = s_out
        # 4". Handle LaTeX \big{...} -> MathML mover

        s= re.sub(
            r"\\big\{([^}]+)\}",
            r'<mo stretchy="false" mathsize="150%">\1</mo>',
            s
        )

        # 5. Replace sum/product/uparrow/downarrow with MathML entities
        symbols = {
            "\\sum": "&sum;",
            "\\prod": "&prod;",
            bool_const.BIG_NAND_SYMB: '<mo stretchy="false" mathsize="150%">&uparrow;</mo>',
            bool_const.NAND_SYMB: "&uparrow;",
            bool_const.BIG_NOR_SYMB: '<mo stretchy="false" mathsize="150%">&downarrow;</mo>',
            bool_const.NOR_SYMB: '&downarrow;',
        }
        for k, v in symbols.items():
            s = s.replace(k, v)

        # 4. Strip math mode markers
        s = s.replace("$$", "")

        # 5. Wrap each line as <math> ... </math>
        lines = s.split("\n")
        newtext_list = [
            f'<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow>{line}</mrow></math>'
            for line in lines if line.strip()
        ]

        newtext = "\n".join(newtext_list)
        return newtext

    def format_map_terms(self, terms =[], method="sop"):
        """
        Gererate diplay for terms
        """

        if method in ("or","nor","pos"):
            reduction_table = format_const.HTML_REDUCTION_TABLE_POS
            # remove extra parenthesis
            terms = [t.replace("(", "").replace(")", "") for t in terms]
            # terms = [t.replace(")",'') for t in terms]
        else:
            reduction_table = format_const.HTML_REDUCTION_TABLE
        simpls = [
            (term, item[0], item[1])
            for term in terms
            if (item := reduction_table.get(term, [])) and len(item) > 1
        ]


        return simpls
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

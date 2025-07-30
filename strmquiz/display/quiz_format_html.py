#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_format_tex.py
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
from . import test_format
import latex2mathml.converter


class test_format_html(test_format.test_format):
    """ Generate a format for the test """
    def __init__(self, formatting=""):
        test_format.test_format.__init__(self)
        self.formatting = ""
        self.output =  []
        self.header =""
        self.footer =""
        self.newline = "<br/>\n"        

   
    def header(self,):
        """
        """
        self.header = """<html><body>
        """
    def footer(self,):
        """
        """
        self.footer = """</body></html>
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
    def open_enumerate(self):
        newtext =     '<ol>'
        self.output.append(newtext)
        return newtext
        
    def open_itemize(self):
        newtext =     '<ul>'
        self.output.append(newtext)
        return newtext
        
    def close_enumerate(self):
        newtext =      '</ol>'
        self.output.append(newtext)
        return newtext
        
    def add_item(self, text):
        newtext =     '<li>'+  text +" '</li>'\n"
        self.output.append(newtext)
        return newtext
        
    def close_itemize(self):
        newtext =      '</ul>'
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
            sect = "H1"
        elif level == 2:
            sect = "H2"
        elif level == 3:
            sect = "H3"
        elif level == 4:
            sect = "p"
        newtext = "\n<%s>%s</%s>\n"%(sect, text,sect)
        self.output.append(newtext)
        return newtext
        
    def add_text(self, text, trans=""):
        """
        """
        newtext ="\n"+ text
        self.output.append(newtext)
        return newtext        
    def add_verbatim(self, text, trans=""):    
        newtext = '\n<pre>'
        newtext +=  text
        newtext  +='\n</pre>'
        
        self.output.append(newtext)
        return newtext
    
    def add_formula(self, text, trans=""): 
        
        text = self.normalize_formula(text)   
        newtext= '<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow>%s</mrow></math>'%text
        newtext += self.newline
        self.output.append(newtext)
        return newtext    
    def add_newline(self):    
        newtext= '\n'
        self.output.append(newtext)
        return newtext          
    def add_hrule(self):    
        newtext= '\n<hr/>'
        self.output.append(newtext)
        return newtext          
    def add_newpage(self):    
        newtext= '' 
        self.output.append(newtext)
        return newtext  
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
    def normalize_formula(self,s):
        """ normalize boolean string"""
        s = str(s)

        for x in ("A", "B", "C", "D", 'a', 'b', 'c', 'd'):
            s = s.replace(x+"'","<mover><mi>%s</mi><mo>&OverBar;</mo></mover>"%x )
            s = s.replace("\\bar "+x ,"<mover><mi>%s</mi><mo>&OverBar;</mo></mover>"%x)
        # sum sympbol
        s = s.replace("\\sum", "&sum;")
        s = s.replace("\\prod", "&prod;")
        s = s.replace("\\uparrow", "&uparrow;")
        s = s.replace("\\downarrow", "&downarrow;")
        s = s.replace("\\overline{","<mover><mrow>")
        s = s.replace("}","</mrow><mo>&OverBar;</mo></mover>")
        # ~ s = s.replace("\n","<mspace linebreak='newline'/>")
        s = s.replace("$$","")
        # ~ text = s
        lines = s.split("\n")
        newtext_list = []
        for line in lines:
            newtext_list.append("<br/>")
            newtext_list.append('<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow>%s</mrow></math>'%line)
        newtext = "\n".join(newtext_list)
        self.output.append(newtext)
        return newtext         

        return s                 
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_format.py
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
import itertools
from . import format_const

class test_format:
    """ Generate a format for the test """
    def __init__(self, formatting=""):
        self.formatting = ""
        self.output = []
        self.tests = []
        self.newline = "\n"
        #~ print("test_format")        
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
    def add_test(self, test_question_list):
        """
        """
        self.tests.append(test_question_list)

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
                self.add_text(question.get("question","QUESTION"),question.get("arabic","ARABIC"))
                self.add_text(question.get("data","DATA"))
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
    def normalize_formula(self,s):
        """ normalize boolean string"""
        s= str(s)
        # ~ s = s.replace("A'","\\bar A")
        # ~ s = s.replace("B'","\\bar B")
        # ~ s = s.replace("C'","\\bar C")
        # ~ s = s.replace("D'","\\bar D")
        # ~ s = s.replace("a'","\\bar a")
        # ~ s = s.replace("b'","\\bar b")
        # ~ s = s.replace("c'","\\bar c")
        # ~ s = s.replace("d'","\\bar d")
        return s
    def draw_map(self, minterms, dontcares=[], correct = False, variables = [], simply_terms=[]):
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

    def simplify_map(self, terms =[]):
        """
        Gererate diplay for terms
        """
        #print(terms)
        simpls = []
        for term in terms:
            simpls.append(format_const.TEX_REDUCTION_TABLE.get(term, ""))
       
        return "\n".join(simpls)  
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
    def draw_logigram_list(self, sop_list, function_namelist = ["F",], variables = []):
        """ draw a logigram """
        varnames = {
            "A":variables[0],
            "B":variables[1],
            "C":variables[2],
            "D":variables[3],
        }
        lggm ="Draw Logigramm in Text mode, not implemented"
        return lggm 
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

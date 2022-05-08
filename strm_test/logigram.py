#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  logigram
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

#~ def normalize(self, s):
def normalize_latex( s):
    """ normalize boolean string"""
    s= str(s)
    s = s.replace("A'","\\bar A")
    s = s.replace("B'","\\bar B")
    s = s.replace("C'","\\bar C")
    s = s.replace("D'","\\bar D")
    return s


def draw_gate(term):
    latex_term = normalize(term)
        
    latex = """
    \\begin{tikzpicture}
        \\node (x) at (0, 1.5) {$A$};
        \\node (y) at (0, 1) {$B$};
        \\node (z) at (0, 0.5) {$C$};
        \\node (w) at (0, 0) {$D$};
      
        \\node[and gate US, draw, rotate=0, logic gate inputs=nnnn] at ($(w) + (2.5, 0.8)$) (xory) {};
        \\draw (xory.output) -- node[above]{$%s$} ($(xory) + (3, 0)$);
        """%latex_term
    if "A'" in term:
        latex += """
        %% X'
        \\node[not gate US, draw] at ($(x) + (0.8, 0)$) (notx) {};
        \\draw (x) -- (notx.input);
        \\draw (notx.output) -- ([xshift=0.35cm]notx.output) |- (xory.input 1);
        """
    elif "A" in term:
        latex += """%% X
        \\draw (x) -| ($(x) + (1.6, -0.4)$) |- (xory.input 1);
        """
    if "B'" in term:
        latex += """
        %Y'
        \\node[not gate US, draw] at ($(y) + (0.8, 0)$) (noty) {};
        \\draw (y) -- (noty.input);    
        \\draw (noty.output) -- ([xshift=0.2cm]noty.output) |- (xory.input 2);
      """
    elif "B" in term:
        latex +="""  
        %% Y
        \\draw (y) -| ($(y) + (1.5, -0.1)$) |- (xory.input 2);
    """
    if "C'" in term:
        latex += """
        %%Z'
        \\node[not gate US, draw] at ($(z) + (0.8, 0)$) (notz) {};
        \\draw (z) -- (notz.input);
        \\draw (notz.output) -- ([xshift=0.2cm]notz.output) |- (xory.input 3);
      """
    elif "C" in term:
        latex +="""
        %%Z
        \\draw (z) -| ($(z) + (1.5, 0.2)$) |- (xory.input 3);
    """
    if "D'" in term:
        latex += """
        %%W
        \\node[not gate US, draw] at ($(w) + (0.8, 0)$) (notw) {};
        \\draw (w) -- (notw.input);
        \\draw (notw.output) -- ([xshift=0.35cm]notw.output) |- (xory.input 4);
      """
    elif "D" in term:
        latex +="""    %%W
        \\draw (w) -| ($(w) + (1.6, 0.3)$) |- (xory.input 4);
    """
        
    latex +=""" 
    \\end{tikzpicture}
    """
    return latex

# ~ term="A'.B.C'.D"

# ~ print draw_gate(term)


class logigram:
    """ Trace a latex logigram for a given function"""
    def __init__(self, var_names=[]):
        # to allow to rename vars
        if var_names:
            self.var_names = var_names
        else:
            self.var_names = {"A":"A", "B":"B", "C":"C", "D":"D"}
        self.var_A = self.var_names.get("A", "A")
        self.var_A_bar = self.var_names.get("A", "A")+"'"
        self.var_B = self.var_names.get("B", "B")
        self.var_B_bar = self.var_names.get("B", "B")+"'"

        self.var_C = self.var_names.get("C", "C")
        self.var_C_bar = self.var_names.get("C", "C")+"'"
        
        self.var_D = self.var_names.get("D", "D")
        self.var_D_bar = self.var_names.get("D", "D")+"'"
        
        # define space and distance between AND gates
        self.and_gates_space = 1.2
        # define basic step of vars in figure
        self.vars_space =1.32
        


        
    def draw_logigram(self, sop, function_name="F"):
        """ draw a logigram from an sop """
        latex = " \\label{logigram-%s}\n"%function_name
        latex += "\\begin{tikzpicture}\n\n"
        terms = sop.upper().split("+")
        latex += self.draw_vars(len(terms))
        for cpt, term in enumerate(terms):
            latex += self.draw_gate(term, cpt)
        latex += self.draw_large_or(len(terms), function_name)
        latex += " \\end{tikzpicture}\n\n"        
        return latex
        
    def draw_logigram_list(self, sop_list=[], function_namelist=["F",]):
        """ draw a logigram from an sop """
        latex = " \\label{logigrammefonction%s}\n\n"%'-'.join(function_namelist)
        latex += " \\begin{tikzpicture}\n\n"
        size_terms = sum([len(l.split('+')) for l in sop_list])
        # ~ latex +="%% sizeterms : %d\n%%%s\n"%(size_terms, repr(sop_list))
        total_terms = 0
        # inverse index
        # we inverse index to get functions ordred in logigram
        sop_list.reverse()
        # reduce function names to be similar to SOP list to avoid any extra name
        function_namelist = function_namelist[:len(sop_list)]
        function_namelist.reverse()      
        for i in range(len(sop_list)):

            sop =  sop_list[i]
            function_name =  function_namelist[i]
            terms = sop.upper().split("+")
            # draw variables
            if(i==0):
                latex += self.draw_vars(size_terms)
                # ~ latex += self.draw_vars(len(terms))
            offset = total_terms +1
            for cpt, term in enumerate(terms):
                latex += self.draw_gate(term, offset+cpt, len(terms))
            latex += self.draw_large_or(len(terms), function_name, offset)
            total_terms += len(terms)
        latex += " \\end{tikzpicture}\n\n"        
        return latex
    def normalize_latex(self,s):
        """ normalize boolean string"""
        s= str(s)
        s = s.replace("A'","\\bar A")
        s = s.replace("B'","\\bar B")
        s = s.replace("C'","\\bar C")
        s = s.replace("D'","\\bar D")
        s = s.replace("a'","\\bar a")
        s = s.replace("b'","\\bar b")
        s = s.replace("c'","\\bar c")
        s = s.replace("d'","\\bar d")
        return s        
    def draw_vars(self, gates_count):
        """ draw vars lines """
        
        # the pos (position of Y) of a var is defined according to 
        # the total number of AND gates to draw (gates_count)
        # 
        y_pos = gates_count * self.vars_space

        # ~ if gates_count<2: y_pos +=1
        # ~ y_pos = (gates_count) * 1.32
        latex ="\\node (x) at (0, %.2f) {$%s$};\n"%(y_pos, self.var_names.get("A", "A"))
        latex += "\\node (y) at (0.5, %.2f) {$%s$};\n"%(y_pos, self.var_names.get("B", "B"))
        latex += "\\node (z) at (1, %.2f) {$%s$};\n"%(y_pos,self.var_names.get("C", "C"))
        latex += "\\node (w) at (1.5, %.2f) {$%s$};\n"%(y_pos, self.var_names.get("D", "D"))
        latex +="""
            \\node[not gate US, draw, rotate=270] at ($(x) + (0.25, -0.6)$) (notx) {};
            \\draw ($(x)+(0,-1ex)$) -| (notx.input); 
            \\node[not gate US, draw, rotate=270] at ($(y) + (0.25, -0.6)$) (noty) {};
            \\draw ($(y)+(0,-1ex)$) -| (noty.input); 
            \\node[not gate US, draw, rotate=270] at ($(z) + (0.25, -0.6)$) (notz) {};
            \\draw ($(z)+(0,-1ex)$) -| (notz.input);
            \\node[not gate US, draw, rotate=270] at ($(w) + (0.25, -0.6)$) (notw) {};
            \\draw ($(w)+(0,-1ex)$) -| (notw.input);
        """
        # ~ latex = latex.replace("ID", str(size))
        return latex
                
    def draw_large_or(self, gates_count, function_name="F", index=0):
        """ draw the final or gate"""
        # size : gates counts
        size = gates_count
        # y_pos : the position of OR gate according to their related gates
        y_pos = (index + (gates_count-1)/2)* self.and_gates_space
        # gate id: defined as current index
        gate_id = index
        # nb_input : defined as gates_counts
        nb_inputs = gates_count
        
        # if the gates count  is only one, we don't draw the gate OR
        if gates_count ==1:
            latex = """\\node at (6, %.2f) (xory%d) {};\n\n
            """%(y_pos, gate_id)
            latex +="""\draw (xory%d) node[above]{\scriptsize $%s$} ($(xory%d.east) + (+3ex, 0)$);\n\n
            """%(gate_id, function_name,  gate_id)            
        else:
            latex = """\\node[or gate US, draw, rotate=0, logic gate inputs=n%s] at (6, %.2f) (xory%d) {};\n\n
            """%("n"*nb_inputs,y_pos, gate_id)
            latex +="""\draw (xory%d.output) -- node[above]{\scriptsize $%s$} ($(xory%d.east) + (+3ex, 0)$);\n\n
            """%(gate_id, function_name,  gate_id)            
            
        # ~ """%("n"*nb_inputs,y_pos, gate_id, gate_id, function_name,  gate_id)

        # ~ """%("n"*nb_inputs, y_pos, gate_id, gate_id, function_name,  gate_id)

        # the offset is the distance between AND gate and  OR gate.
        offset = 1.6
        
        
        for i in range(size):
            and_gate_id = index + i
            if(gates_count == 1):
                latex +="""\\draw (xandy%d.output) -- ([xshift=%.2fcm]xandy%d.output) |- (xory%d);\n\n"""%(and_gate_id, offset, and_gate_id, gate_id)
            else:
                latex +="""\\draw (xandy%d.output) -- ([xshift=%.2fcm]xandy%d.output) |- (xory%d.input %d);\n\n"""%(and_gate_id, offset, and_gate_id, gate_id, nb_inputs-i)                
            if i < size//2:
                offset -=0.05
            else:
                offset +=0.05
        return latex

    def draw_line_var_to_gate(self, gate_id, var, bar, input_n, nb_vars = 2):
        """
        gate_id: xand1
        var : A,
        bar; A false, A bar true
        input_n: input line number
        """
        latex = ""
        # just a label
        latex += """%% %s\n"""%var.upper()
        if bar:
            latex += """\\draw [line width=0.25mm,   red] (not%s.output)
            -- ([xshift=0cm]not%s.output) """%(var, var)
        else:
            latex += """\\draw ($(%s) + (0, -1ex)$)"""%var
        
        # if only one var, draw just a line avoid input attribute
        if nb_vars == 1000:
            latex +="""|- (%s);\n"""%(gate_id) 
        else:
            latex +="""|- (%s.input %d);\n"""%(gate_id, input_n)             
            
        return latex

    def draw_gate(self, term, idg, size=0):
        """ id gate """
        latex_term = self.normalize_latex(term)
            
        # the offset is defined as the number of gates drawn to fix the distance
        offset = idg
        gate_id = "xandy%d"%idg
        # number of vars
        nb_vars = len(term.split("+"))
        # if there is one var only, draw a line instead of and gate
        if nb_vars == 1001:
            latex = """ \n\n      
                \\node at (2.5, %.2f) (xandy%d) {};"""%(offset*self.and_gates_space, idg)
            latex += """\\draw (xandy%d) -- node[above]{\scriptsize $%s$} ($(xandy%d) + (1.8, 0)$);
                """%(idg, latex_term, idg)
        else:
            latex = """ \n\n      
                \\node[and gate US, draw, rotate=0, logic gate inputs=nnnn] at (2.5, %.2f) (xandy%d) {};"""%(offset*self.and_gates_space, idg)
            latex += """\\draw (xandy%d.output) -- node[above]{\scriptsize $%s$} ($(xandy%d) + (1.8, 0)$);
                """%(idg, latex_term, idg)
        if self.var_A_bar in term:
            latex += self.draw_line_var_to_gate(gate_id, var= "x", bar=True, input_n=1, nb_vars=nb_vars)
        elif self.var_A in term:
            latex += self.draw_line_var_to_gate(gate_id, var= "x", bar=False, input_n=1, nb_vars=nb_vars)
        if self.var_B_bar in term:
            latex += self.draw_line_var_to_gate(gate_id, var= "y", bar=True, input_n=2, nb_vars=nb_vars)
        elif self.var_B in term:
            latex += self.draw_line_var_to_gate(gate_id, var= "y", bar=False, input_n=2, nb_vars=nb_vars)
        if self.var_C_bar in term:
            latex += self.draw_line_var_to_gate(gate_id, var= "z", bar=True, input_n=3, nb_vars=nb_vars)

        elif self.var_C in term:
            latex += self.draw_line_var_to_gate(gate_id, var= "z", bar=False, input_n=3, nb_vars=nb_vars)
        if self.var_D_bar in term:
            latex += self.draw_line_var_to_gate(gate_id, var= "w", bar=True, input_n=4, nb_vars=nb_vars)

        elif self.var_D in term:
            latex += self.draw_line_var_to_gate(gate_id, var= "w", bar=False, input_n=4, nb_vars=nb_vars)

            
        return latex   

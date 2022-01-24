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
        


        
    def draw_logigram(self, sop, function_name="F"):
        """ draw a logigram from an sop """
        latex = " \\begin{tikzpicture}\n\n"
        terms = sop.upper().split("+")
        latex += self.draw_vars(len(terms))
        for cpt, term in enumerate(terms):
            latex += self.draw_gate(term, cpt)
        latex += self.draw_large_or(len(terms), function_name)
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
    def draw_vars(self,size):
        """ draw vars lines """
        latex ="\\node (x) at (0, ID*1.5) {$%s$};\n"%(self.var_names.get("A", "A"))
        latex += "\\node (y) at (0.5, ID*1.5) {$%s$};\n"%(self.var_names.get("B", "B"))
        latex += "\\node (z) at (1, ID*1.5) {$%s$};\n"%(self.var_names.get("C", "C"))
        latex += "\\node (w) at (1.5, ID*1.5) {$%s$};\n"%(self.var_names.get("D", "D"))
        latex +="""
            \\node[not gate US, draw, rotate=270] at ($(x) + (0.25, -0.4)$) (notx) {};
            \\draw (x) -- (notx.input); 
            \\node[not gate US, draw, rotate=270] at ($(y) + (0.25, -0.4)$) (noty) {};
            \\draw (y) -- (noty.input); 
            \\node[not gate US, draw, rotate=270] at ($(z) + (0.25, -0.4)$) (notz) {};
            \\draw (z) -- (notz.input);
            \\node[not gate US, draw, rotate=270] at ($(w) + (0.25, -0.4)$) (notw) {};
            \\draw (w) -- (notw.input);
        """
        latex = latex.replace("ID", str(size))
        return latex
                
    def draw_large_or(self, size, function_name="F"):
        """ draw the final or gate"""
        latex = """\\node[or gate US, draw, rotate=0, logic gate inputs=n%s] at (5.5, %d*0.6) (xory) {};\n\n
                    \draw (xory.output) -- node[above]{\scriptsize$%s$} ($(xory) + (1, 0)$);\n\n"""%("n"*size, size, function_name)
        offset = 1.4
        for i in range(size):
            latex +="""\\draw (xandy%d.output) -- ([xshift=%.2fcm]xandy%d.output) |- (xory.input %d);\n\n"""%(i, offset, i, size-i)
            if i < size/2:
                offset -=0.05
            else:
                offset +=0.05
        return latex

  
    def draw_gate(self, term, idg):
        """ id gate """
        latex_term = self.normalize_latex(term)
            
        #~ latex = """
        #~ \\begin{tikzpicture}"""
        latex = """        
           
            \\node[and gate US, draw, rotate=0, logic gate inputs=nnnn] at (2.5, ID*1.5) (xandyID) {};
            \\draw (xandyID.output) -- node[above]{\scriptsize $%s$} ($(xandyID) + (1.8, 0)$);
            """%latex_term
        if self.var_A_bar in term:
            latex += """
            %% X'

            \\draw  [line width=0.25mm,   red] (notx.output) -- ([xshift=0cm]notx.output) |- (xandyID.input 1);
            """
        elif self.var_A in term:
            latex += """%% X
            \\draw (x) -| ($(x) + (0, 0)$) |- (xandyID.input 1);
            """
        if self.var_B_bar in term:
            latex += """
            %Y'

            \\draw [line width=0.25mm,   red] (noty.output) -- ([xshift=0cm]noty.output) |- (xandyID.input 2);
          """
        elif self.var_B in term:
            latex +="""  
            %% Y
            \\draw (y) -| ($(y) + (0, 0)$) |- (xandyID.input 2);
        """
        if self.var_C_bar in term:
            latex += """
            %%Z'

            \\draw [line width=0.25mm,   red] (notz.output) -- ([xshift=0cm]notz.output) |- (xandyID.input 3);
          """
        elif self.var_C in term:
            latex +="""
            %%Z
            \\draw (z) -| ($(z) + (0, 0)$) |- (xandyID.input 3);
        """
        if self.var_D_bar in term:
            latex += """
            %%W

            \\draw [line width=0.25mm,   red] (notw.output) -- ([xshift=0cm]notw.output) |- (xandyID.input 4);
          """
        elif self.var_D in term:
            latex +="""    %%W
            \\draw (w) -| ($(w) + (0, 0)$) |- (xandyID.input 4);
        """
            
        #~ latex +=""" 
        #~ \\end{tikzpicture}
        #~ """
        latex = latex.replace("ID", str(idg))
        return latex   

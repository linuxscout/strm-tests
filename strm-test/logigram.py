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

term="A'.B.C'.D"

print draw_gate(term)


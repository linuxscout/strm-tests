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

import re
from . import bool_const
from deprecated import deprecated


class logigram:
    """Trace a latex logigram for a given function"""

    def __init__(self, var_names=[], method=""):
        # to allow to rename vars
        if var_names:
            self.var_names = var_names
        else:
            self.var_names = {"A": "A", "B": "B", "C": "C", "D": "D"}
        self.var_A = self.var_names.get("A", "A")
        self.var_A_bar = self.var_names.get("A", "A") + "'"
        self.var_B = self.var_names.get("B", "B")
        self.var_B_bar = self.var_names.get("B", "B") + "'"

        self.var_C = self.var_names.get("C", "C")
        self.var_C_bar = self.var_names.get("C", "C") + "'"

        self.var_D = self.var_names.get("D", "D")
        self.var_D_bar = self.var_names.get("D", "D") + "'"

        # define space and distance between AND gates
        self.and_gates_space = 1.2
        # define basic step of vars in figure
        self.vars_space = 1.32
        method = method.upper()
        if method.upper() in ("NAND", "NOR", "SOP", "POS", "OR", "AND"):
            self.method = method
            if method == "AND":
                self.method = "SOP"
            elif method == "OR":
                self.method = "POS"

        else:
            self.method = ""

    def set_gate_type(self, method=""):
        """
        set gate type, empty for usual, NAND, or NOR for building logigram usign only
        NAND or NOR
        """
        method = method.upper()
        if method.upper() in ("NAND", "NOR", "SOP", "POS", "OR", "AND"):
            self.method = method
            if method == "AND":
                self.method = "SOP"
            elif method == "OR":
                self.method = "POS"

        else:
            self.method = ""

    def get_var_sep(
        self,
    ):
        """
        set the var separator,
        in nand case: product
        in nor case: sum
        in sop: product
        in pos: sum
        """
        # if self.method.upper() in ("NOR", "POS","OR" ):
        #     return '+'
        # else:
        #     return "."
        seps = {
            "sop": ".",
            "nand": bool_const.NAND_SYMB,
            "nor": bool_const.NOR_SYMB,
            "pos": "+",
        }
        sep = seps.get(self.method.lower(), ".")
        return sep

    def get_term_sep(
        self,
    ):
        """
        set the var separator,
        in nand case: sum
        in nor case: product
        in sop: sum
        in pos: product
        """
        # if self.method.upper() in ("NOR", "POS","OR" ):
        #     return '.'
        # else:
        #     return "+"
        seps = {
            "sop": "+",
            "nand": bool_const.BIG_NAND_SYMB,
            "nor": bool_const.BIG_NOR_SYMB,
            "pos": ".",
        }
        sep = seps.get(self.method.lower(), "+")
        return sep

    def get_gate_type(self):
        """
        return gate type
        """
        return self.method

    def get_gate_code(self, gate=""):
        gate = gate.lower()
        method = self.method.upper()
        if method == "NAND":
            return "nand"
        elif method == "NOR":
            return "nor"
        elif method in ("POS", "OR") and gate == "and":
            return "or"
        elif method in ("POS", "OR") and gate == "or":
            return "and"
        elif method in ("SOP", "AND") and gate == "and" or gate == "or":
            return gate
        else:
            return gate

    #
    # @deprecated(reason="Latex format is moved to quiz_format class")
    # def draw_logigram(self, sop, function_name="F"):
    #     """draw a logigram from an sop"""
    #     latex = " \\label{logigram-%s}\n" % function_name
    #     latex += "\\begin{tikzpicture}\n\n"
    #     latex += " %%Paramaters\n"
    #
    #     terms = sop.upper().split(self.get_term_sep())
    #     latex += "%% var position, can be modified\n"
    #     latex += "\\def\\varPos{%.2f}\n" % len(terms)
    #     latex += "\\def\\FunctionPos{6}\n"
    #     latex += self.draw_vars(len(terms))
    #     for cpt, term in enumerate(terms):
    #         latex += self.draw_gate(term, cpt)
    #     latex += self.draw_large_or(len(terms), function_name)
    #     latex += " \\end{tikzpicture}\n\n"
    #     return latex
    #
    # @deprecated(reason="Latex format is moved to quiz_format class")
    # def draw_logigram_list(
    #     self,
    #     sop_list=[],
    #     function_namelist=[
    #         "F",
    #     ],
    # ):
    #     """draw a logigram from an sop"""
    #     latex = " \\label{logigrammefonction%s}\n\n" % "-".join(function_namelist)
    #     latex += " \\begin{tikzpicture}\n\n"
    #     latex += " %%Paramaters\n"
    #     # the pos (position of Y) of a var is defined according to
    #     # the total number of AND gates to draw (gates_count)
    #
    #     size_terms = sum([len(l.split(self.get_term_sep())) for l in sop_list])
    #     latex += "%% var position, can be modified\n"
    #     latex += "\\def\\varPos{%.2f}\n" % (size_terms * self.vars_space)
    #     latex += "\\def\\FunctionPos{6}\n"
    #     # ~ latex +="%% sizeterms : %d\n%%%s\n"%(size_terms, repr(sop_list))
    #     total_terms = 0
    #     # inverse index
    #     # we inverse index to get functions ordred in logigram
    #     sop_list.reverse()
    #     # reduce function names to be similar to SOP list to avoid any extra name
    #     function_namelist = function_namelist[: len(sop_list)]
    #     function_namelist.reverse()
    #     for i in range(len(sop_list)):
    #
    #         sop = sop_list[i]
    #         function_name = function_namelist[i]
    #         terms = sop.upper().split(self.get_term_sep())
    #         # reverse terms
    #         terms.reverse()
    #         # draw variables
    #         if i == 0:
    #             latex += self.draw_vars(size_terms)
    #             # ~ latex += self.draw_vars(len(terms))
    #         offset = total_terms + 1
    #         for cpt, term in enumerate(terms):
    #             latex += self.draw_gate(
    #                 term,
    #                 offset + cpt,
    #                 len(terms),
    #                 term_num=cpt,
    #                 function_name=function_name,
    #             )
    #         latex += self.draw_large_or(len(terms), function_name, offset)
    #         total_terms += len(terms)
    #     latex += " \\end{tikzpicture}\n\n"
    #     return latex

    def get_terms(self, equation_item={}):
        """return terms according to used method"""

        expression = equation_item.get("sop", "")
        if self.method.upper() in ["NAND"]:
            expression = equation_item.get("nand_sop", "")
        elif self.method.upper() == "NOR":
            expression = equation_item.get("nor_pos", "")
        elif self.method.upper() in ["OR", "POS"]:
            expression = equation_item.get("pos", "")

        terms = [
            t.replace("(", "").replace(")", "").strip()
            for t in expression.split(self.get_term_sep())
        ]
        return terms

    def prepare_logigram_list(
        self,
        sop_list=[],
        function_namelist=[
            "F",
        ],
        equations_list=[],
    ):
        """draw a logigram from an sop"""

        graph = {
            "variables": self.var_names,
            "functions": [],
            "method": self.method,
            "notvar_gate": self.get_gate_code("not"),
            "term_gate": self.get_gate_code("and"),
            "function_gate": self.get_gate_code("or"),
            "size_terms": 0,
        }

        # the total number of AND gates to draw (gates_count)
        total_terms = 0
        # inverse index
        # we inverse index to get functions ordred in logigram
        # sop_list.reverse()
        # reduce function names to be similar to SOP list to avoid any extra name
        function_namelist = function_namelist[: len(sop_list)]
        # function_namelist.reverse()

        for i in range(len(sop_list)):
            sop = sop_list[i]
            function_name = function_namelist[i]
            terms = self.get_terms(equations_list[i])
            # reverse terms
            terms.reverse()
            terms_list = []
            for ti, term in enumerate(terms):
                vars = [
                    v.strip().upper() for v in term.strip().split(self.get_var_sep())
                ]
                terms_list.append(
                    {
                        "id": f"xandy{function_name}g{ti}",
                        "label": {"default": term, "formatted": term},
                        "name": term.upper(),
                        "vars": vars,
                        "nb_vars": len(vars),
                    }
                )
            total_terms += len(terms)
            function_item = {
                "name": function_name,
                "terms": terms_list,
                "nb_terms": len(terms),
            }
            graph["functions"].append(function_item)
        graph["size_terms"] = total_terms
        # latex += " \\end{tikzpicture}\n\n"
        return graph

    #
    # @deprecated(reason="Latex format is moved to quiz_format class")
    # @staticmethod
    # def normalize_latex(expr: str) -> str:
    #     # Match a word (letters/numbers/underscore) followed by a '
    #     return re.sub(r"([A-Za-z0-9_]+)'", r"\\overline{\1}", expr)
    #
    # def draw_vars(self, gates_count):
    #     """draw vars lines"""
    #
    #     #
    #     # ~ y_pos = gates_count * self.vars_space
    #
    #     # ~ latex = "% var position, can be modified\n"
    #     # ~ latex += "\\def\\varPos{%.2f}\n"%y_pos
    #
    #     # ~ if gates_count<2: y_pos +=1
    #     # ~ y_pos = (gates_count) * 1.32
    #     latex = "\\node (x) at (0, \\varPos) {$%s$};\n" % (self.var_names.get("A", "A"))
    #     latex += "\\node (y) at (0.5, \\varPos) {$%s$};\n" % (
    #         self.var_names.get("B", "B")
    #     )
    #     latex += "\\node (z) at (1, \\varPos) {$%s$};\n" % (
    #         self.var_names.get("C", "C")
    #     )
    #     latex += "\\node (w) at (1.5, \\varPos) {$%s$};\n" % (
    #         self.var_names.get("D", "D")
    #     )
    #
    #     gate_code = self.get_gate_code("not").lower()
    #     if gate_code in ("nand", "nor"):
    #         latex += """
    #             \\node[%s gate US, draw, rotate=270, scale=0.75] at ($(x) + (0.25, -0.6)$) (notx) {};
    #             \\draw ($(x)+(0,-1ex)$) -| (notx.input 1);
    #             \\draw ($(x)+(0,-1ex)$) -| (notx.input 2);
    #             \\node[%s gate US, draw, rotate=270, scale=0.75] at ($(y) + (0.25, -0.6)$) (noty) {};
    #             \\draw ($(y)+(0,-1ex)$) -| (noty.input 1);
    #             \\draw ($(y)+(0,-1ex)$) -| (noty.input 2);
    #             \\node[%s gate US, draw, rotate=270, scale=0.75] at ($(z) + (0.25, -0.6)$) (notz) {};
    #             \\draw ($(z)+(0,-1ex)$) -| (notz.input 1);
    #             \\draw ($(z)+(0,-1ex)$) -| (notz.input 2);
    #             \\node[%s gate US, draw, rotate=270, scale=0.75] at ($(w) + (0.25, -0.6)$) (notw) {};
    #             \\draw ($(w)+(0,-1ex)$) -| (notw.input 1);
    #             \\draw ($(w)+(0,-1ex)$) -| (notw.input 2);
    #         """ % (
    #             gate_code,
    #             gate_code,
    #             gate_code,
    #             gate_code,
    #         )
    #
    #     else:
    #
    #         latex += """
    #             \\node[not gate US, draw, rotate=270] at ($(x) + (0.25, -0.6)$) (notx) {};
    #             \\draw ($(x)+(0,-1ex)$) -| (notx.input);
    #             \\node[not gate US, draw, rotate=270] at ($(y) + (0.25, -0.6)$) (noty) {};
    #             \\draw ($(y)+(0,-1ex)$) -| (noty.input);
    #             \\node[not gate US, draw, rotate=270] at ($(z) + (0.25, -0.6)$) (notz) {};
    #             \\draw ($(z)+(0,-1ex)$) -| (notz.input);
    #             \\node[not gate US, draw, rotate=270] at ($(w) + (0.25, -0.6)$) (notw) {};
    #             \\draw ($(w)+(0,-1ex)$) -| (notw.input);
    #         """
    #     # ~ latex = latex.replace("ID", str(size))
    #     return latex
    #
    # @deprecated(reason="Latex format is moved to quiz_format class")
    # def draw_large_or(self, gates_count, function_name="F", index=0):
    #     """draw the final or gate"""
    #     # size : gates counts
    #     size = gates_count
    #     # y_pos : the position of OR gate according to their related gates
    #     y_pos = (index + (gates_count - 1) / 2) * self.and_gates_space
    #     # gate id: defined as current index
    #     gate_id = index
    #     # nb_input : defined as gates_counts
    #     nb_inputs = gates_count
    #     gate_code = self.get_gate_code("or")
    #     # if the gates count  is only one, we don't draw the gate OR
    #     latex = """\n\n%%%% Function %s Large OR Gate\n\n""" % function_name
    #     if gates_count == 1:
    #         latex += """\\node at (\\FunctionPos, %.2f) (xory%d) {};\n\n
    #         """ % (
    #             y_pos,
    #             gate_id,
    #         )
    #         latex += """\draw (xory%d) node[above]{\scriptsize $%s$} ($(xory%d.east) + (+3ex, 0)$);\n\n
    #         """ % (
    #             gate_id,
    #             function_name,
    #             gate_id,
    #         )
    #     else:
    #         latex += """\\node[%s gate US, draw, rotate=0, logic gate inputs=n%s] at (\\FunctionPos, %.2f) (xory%d) {};\n\n
    #         """ % (
    #             gate_code,
    #             "n" * nb_inputs,
    #             y_pos,
    #             gate_id,
    #         )
    #         latex += """\draw (xory%d.output) -- node[above]{\scriptsize $%s$} ($(xory%d.east) + (+3ex, 0)$);\n\n
    #         """ % (
    #             gate_id,
    #             function_name,
    #             gate_id,
    #         )
    #
    #     # the offset is the distance between AND gate and  OR gate.
    #     offset = 1.6
    #
    #     for i in range(size):
    #         and_gate_id = index + i
    #         if gates_count == 1:
    #             latex += (
    #                 """\\draw (xandy%d.output) -- ([xshift=%.2fcm]xandy%d.output) |- (xory%d);\n\n"""
    #                 % (and_gate_id, offset, and_gate_id, gate_id)
    #             )
    #         else:
    #             latex += (
    #                 """\\draw (xandy%d.output) -- ([xshift=%.2fcm]xandy%d.output) |- (xory%d.input %d);\n\n"""
    #                 % (and_gate_id, offset, and_gate_id, gate_id, nb_inputs - i)
    #             )
    #         if i < size // 2:
    #             offset -= 0.05
    #         else:
    #             offset += 0.05
    #     return latex
    #
    # @deprecated(reason="Latex format is moved to quiz_format class")
    # def draw_line_var_to_gate(self, gate_id, var, bar, input_n, nb_vars=2):
    #     """
    #     gate_id: xand1
    #     var : A,
    #     bar; A false, A bar true
    #     input_n: input line number
    #     """
    #     latex = ""
    #     # just a label
    #     latex += """%% %s\n""" % var.upper()
    #     if bar:
    #         latex += """\\draw [line width=0.25mm,   red] (not%s.output)
    #         -- ([xshift=0cm]not%s.output) """ % (
    #             var,
    #             var,
    #         )
    #     else:
    #         latex += """\\draw ($(%s) + (0, -1ex)$)""" % var
    #
    #     # if only one var, draw just a line avoid input attribute
    #     if nb_vars == 1000:
    #         latex += """|- (%s);\n""" % (gate_id)
    #     else:
    #         latex += """|- (%s.input %d);\n""" % (gate_id, input_n)
    #
    #     return latex
    #
    # @deprecated(reason="Latex format is moved to quiz_format class")
    # def draw_gate(self, term, idg, size=0, term_num=0, function_name=""):
    #     """id gate"""
    #
    #     latex_term = self.normalize_latex(term)
    #
    #     # the offset is defined as the number of gates drawn to fix the distance
    #     offset = idg
    #     gate_id = "xandy%d" % idg
    #     gate_code = self.get_gate_code("and")
    #     # number of vars
    #     nb_vars = len(term.split(self.get_term_sep()))
    #     # if there is one var only, draw a line instead of and gate
    #     latex = """ \n\n %%%% ***Function %s : Gate for term n° %d [%s]***\n""" % (
    #         function_name,
    #         term_num + 1,
    #         term,
    #     )
    #     if nb_vars == 1001:
    #         latex += """
    #             \\node at (2.5, %.2f) (xandy%d) {};""" % (
    #             offset * self.and_gates_space,
    #             idg,
    #         )
    #         latex += """\\draw (xandy%d) -- node[above]{\scriptsize $%s$} ($(xandy%d) + (1.8, 0)$);
    #             """ % (
    #             idg,
    #             latex_term,
    #             idg,
    #         )
    #     else:
    #         latex += """
    #             \\node[%s gate US, draw, rotate=0, logic gate inputs=nnnn] at (2.5, %.2f) (xandy%d) {};""" % (
    #             gate_code,
    #             offset * self.and_gates_space,
    #             idg,
    #         )
    #         latex += """\\draw (xandy%d.output) -- node[above]{\scriptsize $%s$} ($(xandy%d) + (1.8, 0)$);
    #             """ % (
    #             idg,
    #             latex_term,
    #             idg,
    #         )
    #     if self.var_A_bar in term:
    #         latex += self.draw_line_var_to_gate(
    #             gate_id, var="x", bar=True, input_n=1, nb_vars=nb_vars
    #         )
    #     elif self.var_A in term:
    #         latex += self.draw_line_var_to_gate(
    #             gate_id, var="x", bar=False, input_n=1, nb_vars=nb_vars
    #         )
    #     if self.var_B_bar in term:
    #         latex += self.draw_line_var_to_gate(
    #             gate_id, var="y", bar=True, input_n=2, nb_vars=nb_vars
    #         )
    #     elif self.var_B in term:
    #         latex += self.draw_line_var_to_gate(
    #             gate_id, var="y", bar=False, input_n=2, nb_vars=nb_vars
    #         )
    #     if self.var_C_bar in term:
    #         latex += self.draw_line_var_to_gate(
    #             gate_id, var="z", bar=True, input_n=3, nb_vars=nb_vars
    #         )
    #
    #     elif self.var_C in term:
    #         latex += self.draw_line_var_to_gate(
    #             gate_id, var="z", bar=False, input_n=3, nb_vars=nb_vars
    #         )
    #     if self.var_D_bar in term:
    #         latex += self.draw_line_var_to_gate(
    #             gate_id, var="w", bar=True, input_n=4, nb_vars=nb_vars
    #         )
    #
    #     elif self.var_D in term:
    #         latex += self.draw_line_var_to_gate(
    #             gate_id, var="w", bar=False, input_n=4, nb_vars=nb_vars
    #         )
    #
    #     return latex

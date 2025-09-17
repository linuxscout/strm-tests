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
    """Generate a format for the test"""

    def __init__(self, formatting="", lang="ar-en", templates_dir=""):
        super().__init__(formatting="md", lang=lang, templates_dir=templates_dir)
        self.formatting = "md"
        self.output = []
        self.header = ""
        self.footer = ""
        self.newline = "\n"


    def add_section(self, text, trans="", level=1):
        """ """
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
        """ """
        newtext = "\n" + text
        self.output.append(newtext)
        return newtext

    def add_formula(self, text, trans=""):

        text = self.normalize_formula(text)
        newtext = f'<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow>{text}</mrow></math>'
        newtext += self.newline
        self.output.append(newtext)
        return newtext


    def add_hrule(self):
        newtext = "\n--------\n"
        self.output.append(newtext)
        return newtext

    # Escape for HTML
    @staticmethod
    def escape_string(s: str) -> str:
        return "".join([html.escape(x) for x in s])


    @staticmethod
    def normalize_formula(expr: str) -> str:
        # Match a word (letters/numbers/underscore) followed by a '
        expr = re.sub(r"([A-Za-z0-9_]+)'", r"\\overline{\1}", expr)
        # 3. Handle LaTeX \overline{...} -> MathML mover
        s = expr
        while True:
            s_out = re.sub(r"¬\{([^}]+)\}", r"\\overline{\1}", s)
            if s_out == s:
                break
            s = s_out
        # 5. Replace sum/product/uparrow/downarrow with MathML entities
        symbols = {
            bool_const.BIG_NAND_SYMB: "\\big\\uparrow ",
            bool_const.NAND_SYMB: "\\uparrow ",
            bool_const.BIG_NOR_SYMB: "\\big\\downarrow ",
            bool_const.NOR_SYMB: "\\downarrow ",
        }
        for k, v in symbols.items():
            s = s.replace(k, v)

        return s


    def format_map_terms(self, terms=[], method="sop"):
        """
        Gererate diplay for terms
        """

        if method in ("or", "nor", "pos"):
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


if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv))

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


class quiz_format_txt(quiz_format.quiz_format):
    """Generate a format for the test"""

    def __init__(self, formatting="", lang="ar-en", templates_dir=""):
        super().__init__(formatting="txt", lang=lang, templates_dir=templates_dir)
        self.formatting = "txt"
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

    # Escape for HTML
    @staticmethod
    def escape_string(s: str) -> str:
        return "".join([html.escape(x) for x in s])

    @staticmethod
    def normalize_formula(expr: str) -> str:
        """display formula s it"""
        return expr


def main(args):
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv))

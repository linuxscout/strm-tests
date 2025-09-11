#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz_format_factory.py
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
from . import quiz_format
from . import quiz_format_html
from . import quiz_format_tex
from . import quiz_format_json
from . import quiz_format_md
from . import quiz_format_txt

OUTPUT_FORMAT_TABLE = {"txt":"Text",
                            "md":"MarkDown",
                            "tex":"LaTex",
                            "html":"HTML",
                            "json":"JSON"}
OUTPUT_FORMAT_VALUES_TABLE = list(set(list(OUTPUT_FORMAT_TABLE.keys()) + list(OUTPUT_FORMAT_TABLE.values())))
OUTPUT_FORMAT_VALUES_TABLE = [x.lower() for x in OUTPUT_FORMAT_VALUES_TABLE]
class quiz_format_factory:
    
    def __init__(self,):
        pass
    @staticmethod
    def factory(typef="", lang="ar-en", templates_dir=""):
        """ create a factory for format"""
        #~ print("TypeF", typef)
        if typef.lower()== "latex" or typef.lower() =="tex":
            return quiz_format_tex.quiz_format_tex(formatting=typef, lang=lang, templates_dir=templates_dir)
        elif typef.lower()== "text":
            return quiz_format.quiz_format(lang=lang, templates_dir=templates_dir)
        elif typef.lower()== "html":
            return quiz_format_html.quiz_format_html(lang=lang, templates_dir=templates_dir)
        elif typef.lower()== "json":
            return quiz_format_json.quiz_format_json(lang=lang, templates_dir=templates_dir)
        elif typef.lower() in ("markdown", "md") :
            return quiz_format_md.quiz_format_md(lang=lang, templates_dir=templates_dir)
        elif typef.lower() in ("text", "txt") :
            return quiz_format_txt.quiz_format_txt(lang=lang, templates_dir=templates_dir)
        else:
            return quiz_format.quiz_format(lang=lang, templates_dir=templates_dir)
    @staticmethod
    def is_available_format(format):
        return bool(format.lower() in OUTPUT_FORMAT_VALUES_TABLE)

    @staticmethod
    def get_available_format()->dict:
        return OUTPUT_FORMAT_TABLE

def main(args):
    outformats = ["tex", "csv", "md"]
    data = {"section":"Test n°1",
     "text":"Citer les 17 premiers nombres en octal",
      "formula":"1+2+3",
        }
    for frmt  in outformats:
        
        formatter = quiz_format_factory.factory(frmt)
        print(formatter)
        formatter.add_section(data['section'])
        formatter.add_text(data['text'])
        formatter.add_formula(data['formula'])
        formatter.add_newline()
        print(formatter.display())
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

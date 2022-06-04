#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_format_factory.py
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
from . import test_format
from . import test_format_html
from . import test_format_tex
class test_format_factory:
    
    def __init__(self,):
        pass
    @staticmethod
    def factory(typef=""):
        """ create a factory for format"""
        #~ print("TypeF", typef)
        if typef.lower()== "latex" or typef.lower() =="tex":
            return test_format_tex.test_format_tex()
        elif typef.lower()== "text":
            return test_format.test_format()
        elif typef.lower()== "html":
            return test_format_html.test_format_html()
        else:
            return test_format.test_format()
def main(args):
    outformats = ["tex", "csv", "md"]
    data = {"section":"Test n°1",
     "text":"Citer les 17 premiers nombres en octal",
      "formula":"1+2+3",
        }
    for frmt  in outformats:
        
        formatter = test_format_factory.factory(frmt)
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

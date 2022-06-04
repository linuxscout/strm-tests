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

from . import test_format

class test_format_tex(test_format.test_format):
    """ Generate a format for the test """
    def __init__(self, formatting=""):

        self.formatting = ""
        self.output =""
        self.header =""
        self.footer =""

   
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
        self.output = ""
        
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
        self.output +="\n<%s>%s<%s>\n"%(sect, text,sect)
        
    def add_text(self, text, trans=""):
        """
        """
        self.output +="\n"+ text
    def add_verbatim(self, text, trans=""):    
        self.output += '\n<pre>'
        self.output +=  text
        self.output +='\n</pre>'
    
    def add_formula(self, text, trans=""):    
        self.output += '%s'%text
    
    def add_newline(self):    
        self.output += '\n'
    def add_hrule(self):    
        self.output += '\n<hr/>'
    def add_newpage(self):    
        self.output += ''    
    def display(self,):
        """
        """
        text = self.header
        text += "\n"+ self.output
        text += "\n"+ self.footer
        return self.output
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

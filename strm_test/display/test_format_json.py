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

import itertools
import json
import pprint
from . import test_format
from . import test_format_html
from . import format_const
from ..bool import logigram

class test_format_json(test_format_html.test_format_html):
    """ Generate a format for the test """
    def __init__(self, formatting=""):

       test_format_html.test_format_html.__init__(self)
       pass

    def display(self,):
        """
        """
        # ~ return repr(self.tests )
        return json.dumps(self.tests )
        
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

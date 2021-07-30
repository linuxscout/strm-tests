#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gettest.py
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




import sys
import os
import argparse
import test_builder
from io import open
def grabargs():
    parser = argparse.ArgumentParser(description='Create tests for STRM 1- MI.')
    # add file name to import and filename to export
    
    #~ parser.add_argument("-f", dest="filename", required=True,
    #~ help="input file to convert", metavar="FILE")

    parser.add_argument("-o", dest="outfile", required=True,
    help="input file to convert", metavar="OUTFILE", default="output.txt")
    
    parser.add_argument("-d", dest="outformat", nargs='?',
    help="output format(text, latex, md)", metavar="FORMAT", default="text")
    

    parser.add_argument("-v", dest="version", nargs='?',
    help="Release version", metavar="Version", default="0.0.1")
    
    #~ parser.add_argument("-a",dest="all", type=bool, nargs='?',
                        #~ const=True, 
                        #~ help="Generate all categories")
    parser.add_argument("-t",dest="test_no", type=int, nargs='?',
                         help="the order of test to generate (1,2,3)", metavar="TEST_NO", default=1)
    parser.add_argument("-n",dest="number", type=int, nargs='?',
                         help="the number of tests samples to generate", metavar="NUMBER", default=1)
    parser.add_argument("-c",dest="category", type=str, nargs='?', default="all",
                        help="generate only the category of tests ()")
    parser.add_argument("--min",dest="minterms", type=str, nargs='?', default="",
                        help="Add list of minterms")
    args = parser.parse_args()
    return args


def main():
    args= grabargs()
    outfile = args.outfile
    outformat = args.outformat
    number = args.number
    test_no = args.test_no
    category = args.category
    version = args.version
    minterms = args.minterms
    # ~ minterms = args.minterms.split(',')
    # ~ minterms = [int(m) for m in minterms]
    # generate a builder with format
    tester = test_builder.test_builder(outformat)
    
    new_test = tester.get_test(number, repeat=6, args={"minterms":minterms})
    
    fl = open(outfile, "w+", encoding="utf8")
    fl.write(new_test)
    
if __name__ == '__main__':
    import sys
    sys.exit(main())

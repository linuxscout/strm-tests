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

import sys
import os
import argparse
from . import test_builder

def grabargs():
    parser = argparse.ArgumentParser(description='Create tests for STRM 1- MI.')
    # add file name to import and filename to export
    
    parser.add_argument("-f", dest="configfile", nargs='?',
    help="input config file", metavar="CONFIGFILE")

    parser.add_argument("-o", dest="outfile", required=True,
    help="input file to convert", metavar="OUTFILE", default="output.txt")
    
    parser.add_argument("-d", dest="outformat", nargs='?',
    help="output format(text, latex, md)", metavar="FORMAT", default="text")
    

    parser.add_argument("-v", dest="version", nargs='?',
    help="Release version", metavar="Version", default="0.0.1")
    

    parser.add_argument("-t",dest="test_id", type=str, nargs='?',
                         help="the order of test to generate (test1,test2,test3)", metavar="TEST_ID", default=1)
    parser.add_argument("-n",dest="number", type=int, nargs='?',
                         help="the number of tests samples to generate", metavar="NUMBER", default=1)
    parser.add_argument("-c",dest="category", type=str, nargs='?', default="all",
                        help="generate only the category of tests ()")
    parser.add_argument("--min",dest="minterms", type=str, nargs='?', default="",
                        help="Add list of minterms")
    args = parser.parse_args()
    return args


def main():
    args = grabargs()
    outfile = args.outfile
    configfile = args.configfile
    outformat = args.outformat
    test_id = args.test_id
    category = args.category
    version = args.version

    # generate a builder with format
    tester = test_builder.test_builder(outformat, config_file= configfile)
    
    new_test = tester.get_test(test_id)
    
    fl = open(outfile, "w+", encoding="utf8")
    fl.write(new_test)
    
if __name__ == '__main__':
    import sys
    sys.exit(main())

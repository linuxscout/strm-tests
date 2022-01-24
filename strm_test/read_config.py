#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  read_config.py
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
import os.path
import configparser
import ast
class read_config:
    def __init__(self, filename):
        # table of available tests configuration
        self.test_table =  {}
        # number of repetation for every test
        self.repeat = 1
        self.minterms = [[]]
        self.var_names = []
        self.output_names = []
        self.commands = []
        self.quizes = []
        self.debug = False
        self.read_tests(filename=filename)

    
    def read_tests(self, filename, select = "all"):
        config = configparser.ConfigParser()
        newpath = os.path.join(sys.path[0], filename)
        if (not config.read(newpath)):
        # ~ except:
            print("can't open the specified file %s"%newpath)
            sys.exit()
            return False;
        if self.debug:           
            print("path is", newpath, config.read(newpath))
        self.test_table = {}
        self.quizes = ast.literal_eval(config.get('QUIZES','quizes'))
        self.commands = ast.literal_eval(config.get('QUIZES','commands'))
        self.repeat = ast.literal_eval(config.get('Args','repeat'))
        self.minterms = ast.literal_eval(config.get('Args','minterms'))
        self.var_names = ast.literal_eval(config.get('Args','vars'))
        self.output_names = ast.literal_eval(config.get('Args','outputs'))
        for qz in self.quizes:
            self.test_table[qz] = ast.literal_eval(config.get('Tests', qz))
        if self.debug:
            print("Quizes: ", self.quizes)
            print("Tests", self.test_table)
            print("Commands", self.commands)
            print("repeat", self.repeat)
            print("minterms", self.minterms)
        
    
    def get_test_config(self, select = ""):
        
        if select in self.test_table:
            return self.test_table[select]
        else:
            return list(self.test_table.values())[0]
            

def main(args):
    tests = read_config.read_tests("../config/quiz.conf")
    print(tests)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
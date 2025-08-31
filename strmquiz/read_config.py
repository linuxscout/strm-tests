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
# import sys
# import os.path
# import configparser
# import ast
# import logging
# class read_config:
#     def __init__(self, filename):
#         # list of args
#         self.args = {}
#         # table of available tests configuration
#         self.test_table =  {}
#         # number of repetation for every test
#         self.repeat = 1
#         self.minterms = [[]]
#         self.var_names = []
#         self.output_names = []
#         self.commands = []
#         self.quizes = []
#         self.debug = True
#         # self.debug = False
#         # args for logigram
#         self.method = ""
#         self.simplification = ""
#         # args for encoding
#         self.text = ""
#         # args for chronogram
#         self.length = 10
#         self.flip_type = ""
#         self.varlist = {}
#         self.synch_type = "rising"
#         self.output = "Q"
#         self.random_question = False
#         self.questions_size  =1
#         self.register_type = ""
#         # ~ self.debug = False
#
#         self.read_tests(filename=filename)
#
#
#
#
#     def read_tests(self, filename, select = "all"):
#         config = configparser.ConfigParser()
#         newpath = os.path.join(sys.path[0], filename)
#         if (not config.read(newpath)):
#         # ~ except:
#             print("can't open the specified file %s"%newpath)
#             sys.exit()
#             return False;
#         if self.debug:
#             print("path is", newpath, config.read(newpath))
#         self.test_table = {}
#         self.quizes = ast.literal_eval(config.get('QUIZES','quizes'))
#         self.commands = ast.literal_eval(config.get('QUIZES','commands'))
#         self.repeat = ast.literal_eval(config.get('Args','repeat'))
#         self.method = ast.literal_eval(config.get('Args','method'))
#         self.text = ast.literal_eval(config.get('Args','text'))
#         # ~ self.simplification = ast.literal_eval(config.get('Args','simplification'))
#         self.random_question  = ast.literal_eval(config.get('Args','random'))
#         self.questions_size = ast.literal_eval(config.get('Args','size'))
#         self.minterms = ast.literal_eval(config.get('Args','minterms'))
#         self.var_names = ast.literal_eval(config.get('Args','vars'))
#         self.output_names = ast.literal_eval(config.get('Args','outputs'))
#         self.dontcare = ast.literal_eval(config.get('Args','dontcare'))
#
#         # args for chronogram
#         self.length = ast.literal_eval(config.get('Args','length'))
#         self.flip_type = ast.literal_eval(config.get('Args','flip_type'))
#         self.varlist = ast.literal_eval(config.get('Args','varlist'))
#         self.synch_type = ast.literal_eval(config.get('Args','synch_type'))
#         self.output = ast.literal_eval(config.get('Args','output'))
#         self.register_type = ast.literal_eval(config.get('Args','register_type'))
#         logging.debug(f"register_type {self.register_type}")
#
#         for qz in self.quizes:
#             self.test_table[qz] = ast.literal_eval(config.get('Tests', qz))
#         if self.debug:
#             logging.debug(f"Quizes:  '{self.quizes}'")
#             logging.debug(f"Tests: '{self.test_table}'")
#             logging.debug(f"Commands: '{self.commands}'")
#             logging.debug(f"repeat: '{self.repeat}'")
#             logging.debug(f"minterms: '{self.minterms}'")
#             logging.debug(f"flip_type :'{self.flip_type}'")
#             logging.debug(f"length: '{self.length}'")
#             logging.debug(f"varlist :'{self.varlist}'")
#             logging.debug(f"synch_type: '{self.synch_type}'")
#             logging.debug(f"size :'{self.questions_size}'")
#             logging.debug(f"random: '{self.random_question}'")
#             logging.debug(f"method: '{self.method}'")
#             logging.debug(f"text: '{self.text}'")
#             logging.debug(f"register_type: '{self.register_type}'")
#
#
#     def get_quiz_config(self, select = ""):
#
#         if select in self.test_table:
#             return self.test_table[select]
#         else:
#             return list(self.test_table.values())[0]
#
#
# def main(args):
#     tests = read_config.read_tests("../config/quiz.conf")
#     print(tests)
#     return 0
#
# if __name__ == '__main__':
#     import sys
#     sys.exit(main(sys.argv))
import sys
import os
import configparser
import ast
import logging


class ReadConfig:
    def __init__(self, filename, debug=True):
        self.debug = debug

        # --- Single source of truth ---
        # section -> { config_key: (attr_name, default_value) }
        self.fields = {
            "QUIZES": {
                "quizes": ("quizes", []),
                "commands": ("commands", []),
            },
            "Args": {
                "repeat": ("repeat", 1),
                "method": ("method", ""),
                "text": ("text", ""),
                "random": ("random_question", False),
                "size": ("questions_size", 1),
                "minterms": ("minterms", [[]]),
                "vars": ("var_names", []),
                "outputs": ("output_names", []),
                "dontcare": ("dontcare", []),
                "length": ("length", 10),
                "flip_type": ("flip_type", ""),
                "varlist": ("varlist", {}),
                "synch_type": ("synch_type", "rising"),
                "output": ("output", "Q"),
                "register_type": ("register_type", ""),
                "register_nbits": ("register_nbits", 2),
                "register_flips": ("register_flips", ["D","D"]),
                "register_random": ("register_random", False),
            },
        }

        # preload defaults
        for section in self.fields.values():
            for attr_name, default in section.values():
                setattr(self, attr_name, default)

        self.test_table = {}
        self.read_tests(filename)

    def _eval(self, raw):
        """Safe eval with fallback to string."""
        try:
            return ast.literal_eval(raw)
        except Exception:
            return raw

    def read_tests(self, filename, select="all"):
        config = configparser.ConfigParser()
        newpath = os.path.join(sys.path[0], filename)

        if not config.read(newpath):
            print(f"can't open the specified file {newpath}")
            sys.exit(1)

        if self.debug:
            logging.debug("path is %s", newpath)

        # --- Load values from config ---
        for section, keys in self.fields.items():
            for key, (attr, default) in keys.items():
                if config.has_option(section, key):
                    value = self._eval(config.get(section, key))
                else:
                    value = default
                setattr(self, attr, value)

        # --- Load tests ---
        self.test_table = {}
        for qz in self.quizes:
            if config.has_option("Tests", qz):
                self.test_table[qz] = self._eval(config.get("Tests", qz))

        if self.debug:
            for section in self.fields.values():
                for attr, _ in section.values():
                    logging.debug("%s: %r", attr, getattr(self, attr))
            logging.debug("Tests: %r", self.test_table)

    def get_quiz_config(self, select=""):
        if select in self.test_table:
            return self.test_table[select]
        return list(self.test_table.values())[0]


def main(args):
    cfg = ReadConfig("../config/quiz.conf")
    print(cfg.test_table)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

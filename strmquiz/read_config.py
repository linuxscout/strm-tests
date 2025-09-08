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
import sys
import os
import configparser
import ast
import logging


class ReadConfig:
    def __init__(self, filename, debug=True, validate=True):
        self.debug = debug
        self.validate_enabled = validate  # toggle validation
        self.warnings = []

        # --- Single source of truth ---
        # section -> { config_key: (attr_name, default_value) }
        self.fields = {
            "QUIZES": {
                "quizes": ("quizes", []),
                "commands": ("commands", []),
            },
            "Args": {
                #general
                "repeat": ("repeat", 1),
                # encoding
                # "method": ("method", ""),
                # "text": ("text", ""),
                "random": ("random_question", False),
                "size": ("questions_size", 1),
                # boolean
                # "minterms": ("minterms", [[]]),
                # "vars": ("var_names", []),
                # "outputs": ("output_names", []),
                # "dontcare": ("dontcare", []),
                # "sop_question":("sop_question",""),
                # "functions_number":("functions_number",2),
                # chronogram & flips
                # "length": ("length", 10),

                # "flip_type": ("flip_type", ""),
                # "varlist": ("varlist", {}),
                # "synch_type": ("synch_type", "rising"),
                # "output": ("output", "Q"),
                # register
                # "register_type": ("register_type", ""),
                # "register_nbits": ("register_nbits", 2),
                # "register_flips": ("register_flips", ["D","D"]),
                # "register_random": ("register_random", False),
                # counter
                # "counter_type": ("counter_type", ""),
                # "counter_nbits": ("counter_nbits", 2),
                # "counter_flips": ("counter_flips", ["JK", "JK"]),
                # "counter_random": ("counter_random", False),
                # encoding
                # "float":("float", 0),
                # "interval_nbits":("interval_nbits",8),
                # "complement_number":("complement_number",[0,0]),
                # "bases":("bases",[10, 10]),
                # "arithm_numbers":("arithm_numbers",[0, 0]),
                # "base_numbers":("base_numbers",[0, 0]),
                # "bcdx3_numbers":("bcdx3_numbers",[0, 0]),
                # "gray_number":("gray_number",0),
                # "gray_sequence":("gray_sequence",2),
                # "arihtm_operation":("arithm_operation",'+'),
            },
        }
        # --- Validation rules ---
        self.validators = {
            "repeat": {"range": (1, 100)},
            "size": {"range": (1, 50)},
            # "length": {"range": (1, 100)},
            # "synch_type": {"enum": ["rising", "falling"]},
            # "flip_type": {"enum": ["D", "T", "JK", "RS", "RST",""]},
            # "register_type": {"enum": ["shift-right", "shift-left", "parallel", ""]},
            # "output": {"enum": ["Q", "Q'", ""]},
            # "counter_type": {"enum": ["up", "down", ""]},
        }
        # preload defaults
        for section in self.fields.values():
            for attr_name, default in section.values():
                setattr(self, attr_name, default)

        self.test_table = {}
        self.read_tests(filename)
        if self.validate_enabled:
            self.validate_values()

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

    def validate_values(self):
        """Validate loaded config values against schema.
        If invalid, warn and reset to default.
        """
        self.warnings = []  # keep track of all warnings

        for section, keys in self.fields.items():
            for key, (attr, default) in keys.items():
                value = getattr(self, attr, None)

                if attr in self.validators:
                    rules = self.validators[attr]

                    # --- Range validation ---
                    if "range" in rules:
                        min_val, max_val = rules["range"]
                        if not (min_val <= value <= max_val):
                            msg = (
                                f"Invalid value for {attr}: {value!r} "
                                f"(expected in range [{min_val}, {max_val}]). "
                                f"Falling back to default {default!r}."
                            )
                            logging.warning(msg)
                            self.warnings.append(msg)
                            setattr(self, attr, default)
                            continue

                    # --- Enum validation ---
                    if "enum" in rules:
                        if value not in rules["enum"]:
                            msg = (
                                f"Invalid value for {attr}: {value!r} "
                                f"(expected one of {rules['enum']}). "
                                f"Falling back to default {default!r}."
                            )
                            logging.warning(msg)
                            self.warnings.append(msg)
                            setattr(self, attr, default)

    def print_warnings(self, stream=sys.stdout):
        """Pretty-print collected warnings."""
        if not hasattr(self, "warnings") or not self.warnings:
            print("No configuration warnings.", file=stream, flush=True)
            return

        print("Configuration Warnings:", file=stream,  flush=True)
        for i, msg in enumerate(self.warnings, 1):
            print(f"  {i}. {msg}", file=stream)



def main(args):
    cfg = ReadConfig("../config/quiz.conf")
    print(cfg.test_table)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

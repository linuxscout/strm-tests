#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz_builder.py
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
import logging
# --- Configure logging ---
import os.path

logging.basicConfig(
    level=logging.DEBUG,  # change to INFO or WARNING in production
    format="%(levelname)s:%(name)s:%(message)s"
)
logger = logging.getLogger(__name__)
import random
from deprecated import deprecated

from . import read_config
from .display import quiz_format_factory
from .question_builder_factory import question_builder_factory

from typing import TypedDict, Optional, Any

class CommandInfo(TypedDict):
    short: str
    long: str
    category: str

class CommandSummary(TypedDict):
    name: str
    short: str
    long: str

class CategoryInfo(TypedDict):
    short: str
    long: str
    commands: list[CommandSummary]

import os

class QuizBuilder:
    """ Generate the third test """
    def __init__(self, outformat="", config_file="", lang="", templates_dir=""):

        # --- Check if templates_dir exists
        if not templates_dir or not os.path.isdir(templates_dir):
            raise FileNotFoundError(f"Template directory not found: '{templates_dir}'")

        # --- If no config file provided, use default
        if not config_file:
            config_file = os.path.join(os.path.dirname(__file__), "config", "quiz.conf")

        # --- Check if config_file exists
        if not os.path.isfile(config_file):
            raise FileNotFoundError(f"Config file not found: '{config_file}'")

        # --- Save attributes
        self.config_file = config_file

        # --- Factories
        self.qsbuilder = question_builder_factory.factory(
            builder_name="", outformat=outformat, lang=lang, templates_dir=templates_dir
        )
        self.encode_qsbuilder = question_builder_factory.factory(
            builder_name="encoding", outformat=outformat, lang=lang, templates_dir=templates_dir
        )
        self.bool_qsbuilder = question_builder_factory.factory(
            builder_name="boolean", outformat=outformat, lang=lang, templates_dir=templates_dir
        )
        self.seq_qsbuilder = question_builder_factory.factory(
            builder_name="sequential", outformat=outformat, lang=lang, templates_dir=templates_dir
        )

        self.formater = quiz_format_factory.quiz_format_factory.factory(
            outformat, lang=lang, templates_dir=templates_dir
        )

        # --- Load config
        self.myconfig = read_config.ReadConfig(config_file)
        self.commands_info = {
            "float": {
                "category": "encoding",
                "short": "Floating-point representation",
                "long": "Questions on IEEE-754 floating-point format. Students convert between decimal and binary, identify mantissa, exponent, and sign bit."
            },
            "intervalle": {
                "category": "encoding",
                "short": "Integer intervals with complements",
                "long": "Covers integer ranges in binary representation, including signed numbers with Complement to 1 and Complement to 2."
            },
            "complement": {
                "category": "encoding",
                "short": "Number complements",
                "long": "Exercises about computing complement to one and complement to two for binary numbers."
            },
            "exp": {
                "category": "boolean algebra",
                "short": "Boolean expression simplification",
                "long": "Given a Boolean expression, students simplify it using algebraic rules or canonical forms."
            },
            "map": {
                "category": "boolean algebra",
                "short": "Karnaugh Map simplification",
                "long": "Simplify Boolean expressions using Karnaugh Maps. Identify prime implicants and reduce logic circuits."
            },
            "map-sop": {
                "category": "boolean algebra",
                "short": "K-map with canonical forms",
                "long": "Generate and simplify canonical forms (SOP/POS) using Karnaugh Maps. Students practice systematic minimization."
            },
            "function": {
                "category": "boolean algebra",
                "short": "Logic function analysis",
                "long": "Study a Boolean function given in algebraic form. Includes truth table, simplification, and circuit representation."
            },
            "base": {
                "category": "encoding",
                "short": "Numeral system conversion",
                "long": "Convert numbers between bases (binary, octal, decimal, hexadecimal). Includes integer and fractional parts."
            },
            "arithm": {
                "category": "encoding",
                "short": "Arithmetic in different bases",
                "long": "Perform addition, subtraction, multiplication, and division in binary, octal, or hexadecimal systems."
            },
            "mesure": {
                "category": "encoding",
                "short": "Unit conversions",
                "long": "Convert between units of information (bits, bytes, KB, MB) or physical measures (time, frequency) depending on context."
            },
            "static_funct": {
                "category": "boolean algebra",
                "short": "Canonical logical functions",
                "long": "Study logical functions expressed in canonical forms (SOP or POS). Students analyze and simplify them."
            },
            "nand_funct": {
                "category": "boolean algebra",
                "short": "Logic with NAND gates",
                "long": "Design and simplify logical functions using only NAND gates, showing functional completeness of NAND."
            },
            "nor_funct": {
                "category": "boolean algebra",
                "short": "Logic with NOR gates",
                "long": "Design and simplify logical functions using only NOR gates, showing functional completeness of NOR."
            },
            "multi_funct": {
                "category": "boolean algebra",
                "short": "Multi-output logic circuits",
                "long": "Draw and analyze circuits that implement multiple functions simultaneously, often from minterm tables."
            },
            "chronogram": {
                "category": "sequential logic",
                "short": "Sequential logic timing diagrams",
                "long": "Interpret and draw chronograms (timing diagrams) for flip-flops (RS, D, JK). Students analyze sequential behavior over time."
            },
            "ascii": {
                "category": "encoding",
                "short": "ASCII character codes",
                "long": "Convert characters to/from ASCII codes. Includes decimal, hexadecimal, and binary representations."
            },
            "ascii_text": {
                "category": "encoding",
                "short": "ASCII text encoding",
                "long": "Encode and decode short words or sentences using ASCII character tables."
            },
            "bcdx3": {
                "category": "encoding",
                "short": "BCD ×3 encoding",
                "long": "Convert numbers into Binary Coded Decimal (BCD) with ×3 correction. Used in digital arithmetic operations."
            }
        }

        # Predefined categories metadata
        self.categories_info = {
            "encoding": {
                "short": "Encoding & number systems",
                "long": "Covers numeral bases, complements, character encoding, floating point representation, and data measurement units."
            },
            "boolean algebra": {
                "short": "Boolean algebra & logic",
                "long": "Focuses on Boolean expressions, Karnaugh maps, logic simplification, and circuit design."
            },
            "sequential logic": {
                "short": "Sequential circuits",
                "long": "Includes flip-flops, registers, counters, and timing diagrams for analyzing sequential behavior."
            }
        }
        #~ print(outformat)
        self.commands = list(self.commands_info.keys())
        self.quiz_commands = {}
        self.quiz_commands[1] = [["base", "base", "arithm"],
        ["mesure", "base", "arithm"],
        ["base", "mesures", "arithm"],
        
        ]
        self.quiz_commands[2] = [["float", "map"],
        ["float", "map-sop"],
        ["float", "function"],
        ["complement","complement", "map"],
        ["function", "exp"],
        ["function", "exp"],        
        ]
        self.quiz_commands[3] =  [
#       ["float", "map"],
#        ["float", "map-sop"],
#        ["float", "function"],
#        ["complement","complement", "map"],
        ["function", "exp"],
        ["function", "exp"],
        ["function", "map"],
        ["function", "map"],
        ["function", "map"],
        ["function", "exp"],
        ]        
        self.quiz_commands[4] =  [
        ["static_funct","nand_funct"],
        ]        
        self.quiz_commands[5] =  [
        ["multi_funct",],
        ]
        self.quiz_commands[6] =  [
        ["chronogram",],
        ]

        self.TEMPLATE_MAP = {
            "float": "encoding/float",
            "complement": "encoding/cp",
            "intervalle": "encoding/interval",
            "base": "base",
            "bcdx3": "encoding/bcdx3",
            "gray": "encoding/gray",
            "ascii": "encoding/charcode",
            "ascii_text": "encoding/charcode",
            "unicode": "encoding/charcode",
            "charcode": "encoding/charcode",
            "arithm": "arithm",
            "mesure": "mesure",  # NotImplementedError for now
            "map": "bool/map",
            "map-sop": "bool/map-sop",
            "function": "bool/function",
            "nand_funct": "bool/function",
            "nor_funct": "bool/function",
            "static_funct": "bool/function",
            "exp": "bool/exp",
            "multi_funct": "bool/multi_funct",

            # 🔹 Sequential logic questions
            "chronogram": "sequential/timing",
            "flip": "sequential/flip",
            "register": "sequential/register",
            "counter": "sequential/counter",
            "misc": "sequential/misc",
            }
    def get_template(self, name):
        temp = self.TEMPLATE_MAP.get(name, "default")
        if temp == "default":
            raise NotImplementedError(f"Not Implemented template for command '{name}'")
        return temp
    def set_format(self, outformat="latex"):
        """ set a new format"""
        self.formater = quiz_format_factory.quiz_format_factory.factory(outformat)

    def reset(self,):
        """
        reset output
        """
        self.formater.reset()
    def get_quiz_config(self, test_id):
        """
        return testif according to config file
        """
        return self.myconfig.get_quiz_config(test_id)


    def _render(self, template: str, context: dict):
        """Render a question and answer using the current formatter."""
        try:
            q, a = self.formater.render_question_answer(template, context)
            # return q, LANG_AR, "data", a
            return q, a
        except Exception as e:
            logger.exception("Error rendering template %s", template)
            return f"Error: {e}",  "Error"
     

    def get_question(self, command, args=None):
        """
        تُولّد سؤالًا بناءً على الأمر المُعطى باستخدام الدوال المناسبة من qsbuilder.

        Parameters:
            command (str): نوع السؤال المطلوب توليده.
            args (dict, optional): المعطيات المُرسلة للدالة. الافتراضي هو None.

        Returns:
            tuple: (السؤال، اللغة، البيانات، الجواب) أو رسالة خطأ.
        """
        if args is None:
            args = self.myconfig.__dict__
        logger.debug(msg=f"Args in quizbuilder are {args}")
        logger.debug(msg=f"QuizBuilder : Text '{args.get('text','')}'")
        def command_ascii_text(args={}):
            return self.encode_qsbuilder.question_ascii(text=args.get("text",""), method=args.get("method",""))


        # boolean

        def command_static_funct(args={}):
            minterms = args["minterms"][0] if args["minterms"] else []
            dont_care = args["dontcare"][0] if args["dontcare"] else []
            return self.bool_qsbuilder.question_static_funct(minterms=minterms,
             var_names=args.get("var_names",[]), output_names=args.get("output_names",[])
             ,dont_care=dont_care)

        def command_nand_funct(args={}):
            minterms = args["minterms"][0] if args["minterms"] else []
            dont_care = args["dontcare"][0] if args["dontcare"] else []
            return self.bool_qsbuilder.question_static_nand_exp(minterms=minterms,
             var_names=args.get("var_names",[]), output_names=args.get("output_names",[])
             ,dont_care=dont_care, method="nand")
        def command_nor_funct(args={}):
            minterms = args["minterms"][0] if args["minterms"] else []
            dont_care = args["dontcare"][0] if args["dontcare"] else []
            return self.bool_qsbuilder.question_static_nand_exp(minterms=minterms,
             var_names=args.get("var_names",[]), output_names=args.get("output_names",[])
             ,dont_care=dont_care, method="nor")
        def command_multi_funct(args={}):
            return self.bool_qsbuilder.question_multi_funct(minterms_list=args.get("minterms",[[]]),
                   var_names=args.get("var_names",[]), output_names=args.get("output_names",[]),
                   dont_care_list=args.get("dontcare",[[]]), method=args.get("method",''))

        def command_chronogram(args={}):
            # print("quiz_builder:debug:arguments",args)
            return self.seq_qsbuilder.question_chronogram(
                varlist=args.get("varlist", {}),
                flip_type=args.get("flip_type", "D"),
                length=args.get("length", 10),
                synch_type=args.get("synch_type", "rising"),
                output_vars=args.get("output", "Q")
            )

        def command_flip(args={}):
            # print("quiz_builder:debug:arguments",args)
            return self.seq_qsbuilder.question_flip(
                varlist=args.get("varlist", {}),
                flip_type=args.get("flip_type", "D"),
                length=args.get("length", 10),
                synch_type=args.get("synch_type", "rising"),
                output_vars=args.get("output", "Q")
            )

        def command_counter(args={}):
            # print("quiz_builder:debug:arguments",args)
            return self.seq_qsbuilder.question_counter(
                varlist=args.get("varlist", {}),
                length=args.get("length", 10),
                synch_type=args.get("synch_type", "rising"),
                output_vars=args.get("output", "Q"),
                counter_type=args.get("counter_type", "up"),
                flip_types=args.get("counter_flips", []),
                nbits=args.get("counter_nbits", 2),
                counter_random=args.get("counter_random", False),
            )

        def command_register(args={}):
            # print("quiz_builder:debug:arguments",args)
            return self.seq_qsbuilder.question_register(
                varlist=args.get("varlist", {}),
                # flip_type=args.get("flip_type","D"),
                length=args.get("length", 10),
                synch_type=args.get("synch_type", "rising"),
                output_vars=args.get("output", "Q"),
                register_type=args.get("register_type", "shift-right"),
                flip_types=args.get("register_flips", []),
                nbits=args.get("register_nbits", 2),
                register_random=args.get("register_random", False),
            )

        def command_seq_misc(args={}):
            # print("quiz_builder:debug:arguments",args)
            return self.seq_qsbuilder.question_seq_misc(
                varlist=args.get("varlist", {}),
                flip_type=args.get("flip_type", "D"),
                length=args.get("length", 10),
                synch_type=args.get("synch_type", "rising"),
                output_vars=args.get("output", "Q")
            )
        # خارطة تربط كل أمر بدالة إنشاء السؤال وما إذا كانت تتطلب معطيات
        question_map = {
            # encoding
            "float": (self.encode_qsbuilder.question_vf, False),
            "intervalle": (self.encode_qsbuilder.question_intervalle, False),
            "complement": (self.encode_qsbuilder.question_cp, False),
            "base": (self.encode_qsbuilder.question_base, False),
            "arithm": (self.encode_qsbuilder.question_arithm, False),
            "mesure": (self.encode_qsbuilder.question_mesure, False),
            "ascii": (self.encode_qsbuilder.question_ascii, False),
            "unicode": (self.encode_qsbuilder.question_unicode, False),
            "bcdx3": (self.encode_qsbuilder.question_bcd_x3, False),
            "gray": (self.encode_qsbuilder.question_gray, False),


            "exp": (self.bool_qsbuilder.question_exp, False),
            "map": (self.bool_qsbuilder.question_map, False),
            "map-sop": (self.bool_qsbuilder.question_map_for_sop, False),
            "function": (self.bool_qsbuilder.question_funct, False),


            # command with parameters
            # encoding
            "ascii_text": (command_ascii_text, True),
            # boolean
            "static_funct": (command_static_funct, True),
            "nand_funct": (command_nand_funct, True),
            "nor_funct": (command_nor_funct, True),
            "multi_funct": (command_multi_funct, True),
            # sequential
            "chronogram": (command_chronogram, True),
            "flip": (command_flip, True),
            "counter": (command_counter, True),
            "register": (command_register, True),
            "seq_misc": (command_seq_misc, True),
        }

        entry = question_map.get(command)
        if not entry:
            return f"Unknown command: {command}", "Answer"
            # return f"Unknown command: {command}", "Arabic", "Data", "Answer"

        question_func, needs_args = entry

        try:
            result = question_func(args) if needs_args else question_func()
            if isinstance(result, dict):
                return self._render(self.get_template(command), result)
            else:
                raise BaseException(f"Warning to be fixed '{command}' not return a context dict {result}")
        except Exception as e:
            import traceback
            traceback_str = traceback.format_exc()
            print(f"Exception in get_question:\n{traceback_str}")
            return f"Error generating question '{command}': {e}", "Answer"

    def build_quiz(self, questions_names, rand=True, nb=2, repeat=2, args={}):
        """ generate a test"""
        if rand:
            questions_names = random.sample(questions_names, nb)
        # generate question from  command
        questions = [self.get_question(q, args=args) for q in questions_names]
        # ~ for i in range(repeat): " ignore repeat"
        quiz_questions = []
        for cpt, name in enumerate(questions_names):
            generated_question = self.get_question(name, args=args)
        # ~ for cpt, value in enumerate(questions):
            if not isinstance(generated_question, (tuple, list)):
                raise TypeError(f"Expected tuple/list for question '{name}', got {type(generated_question)}")

            if len(generated_question) == 2:
                qtext, ans = generated_question
            else:
                raise ValueError(
                    f"Invalid return value for question '{name}': "
                    f"expected 2  elements, got {len(generated_question)} → {generated_question}"
                )

            #     qtext, _, _, ans = generated_question
            # ~ qtext, ar, data, ans = value
            q_no = "Q%d"%(cpt+1)
            item = {"id":q_no,
            "category": name,
            "question":qtext,
            # "arabic":ar,
            # "data":data,
            "answer":ans,                
            }
            quiz_questions.append(item)
        self.formater.add_test(quiz_questions)
    #---------------------------------
    #  routines to extract categories and commands
    #------------------------------------
    @deprecated(reason="Replaced by get_commands_list()")
    def list_commands(self,):
        """ list all existing question types """
        return self.commands

    def get_commands_list(self,category=""):
        """ list all existing question types """
        if not category:
            return self.commands
        else:
            return [name for name, info in self.commands_info.items() if info["category"] == category]

    def get_commands_info(self, category=""):
        """ list all existing question types """
        if not category:
            return self.commands_info
        else:
            return {cmd:self.commands_info[cmd] for cmd in self.commands_info if self.commands_info[cmd]["category"]==category}

    def get_quiz(self,test_no="test1"):
        """
        Generate a test by number according to config file
        """

        randq = False
        randq = self.myconfig.random_question
        nb_questions = self.myconfig.questions_size
        repeat = self.myconfig.repeat
        args = self.myconfig.__dict__
        test_config = self.get_quiz_config(test_no)
        for test in test_config:
            for i in range(nb_questions):
                self.formater.open_question(test)
                self.formater.add_section("Question", level=1)
                self.build_quiz(test, rand=randq, repeat=repeat, args=args)
                self.formater.add_newpage()
                self.formater.close_question(test)
        return self.formater.display()

    import random
    from typing import Optional

    def get_categories(self) -> dict[str, CategoryInfo]:
        """
        Return a dictionary of categories with descriptions and their commands.
        """
        categories: dict[str, CategoryInfo] = {}
        for cat, meta in self.categories_info.items():
            categories[cat] = {
                "short": meta["short"],
                "long": meta["long"],
                "commands": [
                    {
                        "name": name,
                        "short": info["short"],
                        "long": info["long"]
                    }
                    for name, info in self.commands_info.items()
                    if info["category"] == cat
                ]
            }
        return categories
    @deprecated(reason="Replaced by get_commands_list(category=category)")
    def get_commands_by_category(self, category: str) -> list[str]:
        """Return a list of command names for a given category."""
        return self.get_commands_list(category=category)

    @deprecated(reason="Replaced by get_commands_list(category="")")
    def get_all_commands(self) -> list[str]:
        """Return all command names."""
        return  self.get_commands_list()

    def get_short_description(self, cmd: str) -> str:
        """Return short description for a command."""
        return self.commands_info.get(cmd, {}).get("short", f"No short description for '{cmd}'")

    def get_long_description(self, cmd: str) -> str:
        """Return long description for a command."""
        return self.commands_info.get(cmd, {}).get("long", f"No long description for '{cmd}'")

    @deprecated(reason="Replaced by get_random_commands(n=1)")
    def get_random_command(self, category: Optional[str] = None) -> tuple[str, CommandInfo]:
        """
        Return a random command (name, info).
        If category is given, pick only from that category.
        """
        if category:
            cmds = self.get_commands_by_category(category)
        else:
            cmds = list(self.commands_info.keys())

        if not cmds:
            raise ValueError(f"No commands found for category '{category}'")

        cmd = random.choice(cmds)
        return cmd, self.commands_info[cmd]

    def get_random_commands(self, n: int = 3, category: Optional[str] = None) -> dict[str, CommandInfo]:
        """
        Return a list of n random commands (name, info).
        If category is given, pick only from that category.
        """
        if category:
            cmds = self.get_commands_by_category(category)
        else:
            cmds = list(self.commands_info.keys())

        if not cmds:
            raise ValueError(f"No commands found for category '{category}'")

        n = min(n, len(cmds))
        selected = random.sample(cmds, k=n)
        commands_dict ={cmd:self.commands_info[cmd] for cmd in selected}
        return commands_dict

    def get_random_commands_list(self, n=3, category=None):
        """
        Return a list of n random commands (name).
        If category is given, pick only from that category.
        """
        commands_dict = self.get_random_commands(n=n, category=category)
        return list(commands_dict.keys())




def main(args):
    builder = QuizBuilder()
    test = builder.get_quiz(4)
    print(test)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

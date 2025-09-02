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
logging.basicConfig(
    level=logging.DEBUG,  # change to INFO or WARNING in production
    format="%(levelname)s:%(name)s:%(message)s"
)
logger = logging.getLogger(__name__)
import random
# ~ from . import question
# ~ from . import boolquiz
# ~ from . import ieee754
from . import read_config
from .display import quiz_format_factory
from .question_builder_factory import question_builder_factory
class QuizBuilder:
    """ Generate the third test """
    def __init__(self, outformat="", config_file ="", lang="", templates_dir=""):

        self.qsbuilder = question_builder_factory.factory(builder_name="", outformat=outformat, lang=lang, templates_dir=templates_dir)
        self.encode_qsbuilder = question_builder_factory.factory(builder_name="encoding",outformat=outformat, lang=lang, templates_dir=templates_dir)
        self.bool_qsbuilder = question_builder_factory.factory(builder_name="boolean",outformat=outformat, lang=lang, templates_dir=templates_dir)
        self.seq_qsbuilder = question_builder_factory.factory(builder_name="sequential",outformat=outformat, lang=lang, templates_dir=templates_dir)

        self.formater = quiz_format_factory.quiz_format_factory.factory(outformat)
        # if the file is not configured, use default config file
        if not config_file:
            config_file = "config/quiz.conf"
        self.config_file = config_file
        self.myconfig = read_config.ReadConfig(config_file)
        #~ print(outformat)
        self.commands = ["float",
         "intervalle",
         "complement",
         "exp",
         "map",
         "map-sop",
        "function",
        "base",
        "arithm",
        "mesure",
        "static_funct",
        "nand_funct",
        "nor_funct",
        "multi_funct",
        "chronogram",
        "ascii",
        "ascii_text",
        "bcdx3",

        ]
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

     

    def get_question(self, command, args={}):
        """
        تُولّد سؤالًا بناءً على الأمر المُعطى باستخدام الدوال المناسبة من qsbuilder.

        Parameters:
            command (str): نوع السؤال المطلوب توليده.
            args (dict, optional): المعطيات المُرسلة للدالة. الافتراضي هو None.

        Returns:
            tuple: (السؤال، اللغة، البيانات، الجواب) أو رسالة خطأ.
        """
        if args is None:
            args = {}
        def command_ascii_text(args={}):
            return self.encode_qsbuilder.question_ascii(text=args["text"], method=args["method"])


        # boolean

        def command_static_funct(args={}):
            return self.bool_qsbuilder.question_static_funct(minterms=args["minterms"][0],
             var_names=args["var_names"], output_names=args["output_names"]
             ,dont_care=args["dontcare"][0])

        def command_nand_funct(args={}):
            return self.bool_qsbuilder.question_static_nand_exp(minterms=args["minterms"][0],
             var_names=args["var_names"], output_names=args["output_names"]
             ,dont_care=args["dontcare"][0], method="nand")
        def command_nor_funct(args={}):
            return self.bool_qsbuilder.question_static_nand_exp(minterms=args["minterms"][0],
             var_names=args["var_names"], output_names=args["output_names"]
             ,dont_care=args["dontcare"][0], method="nor")
        def command_multi_funct(args={}):
            return self.bool_qsbuilder.question_multi_funct(minterms_list=args["minterms"],
                   var_names=args["var_names"], output_names=args["output_names"],
                   dont_care_list=args["dontcare"], method=args["method"])

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
            return question_func(args) if needs_args else question_func()
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

    def list_commands(self,):
        """ list all existing question types """
        return self.commands

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





def main(args):
    builder = QuizBuilder()
    test = builder.get_quiz(4)
    print(test)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

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
import random
# ~ from . import question
# ~ from . import boolquiz
# ~ from . import ieee754
from . import read_config
from .display import quiz_format_factory
from . import question_builder
# ~ from .sequentiel import tex_chronograms

class QuizBuilder:
    """ Generate the third test """
    def __init__(self, outformat="", config_file ="", lang="", templates_dir=""):

        self.qsbuilder = question_builder.Question_Builder(outformat, lang=lang, templates_dir=templates_dir)
        self.formater = quiz_format_factory.quiz_format_factory.factory(outformat)
        # if the file is not configured, use default config file
        if not config_file:
            config_file = "config/quiz.conf"
        self.config_file = config_file
        self.myconfig = read_config.read_config(config_file)
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

     
    #
    # def get_questionX(self, command, args={}):
    #     """
    #     return question from command
    #     """
    #     if command == "float":
    #         return self.qsbuilder.question_vf()
    #     elif command == "intervalle":
    #         return self.qsbuilder.question_intervalle()
    #     elif command == "complement":
    #         return self.qsbuilder.question_cp()
    #     elif command == "exp":
    #         return self.qsbuilder.question_exp()
    #     elif command == "map":
    #
    #         return self.qsbuilder.question_map()
    #     elif command == "map-sop":
    #
    #         return self.qsbuilder.question_map_for_sop()
    #     elif command == "function":
    #
    #         return self.qsbuilder.question_funct()
    #     elif command == "base":
    #         return self.qsbuilder.question_base()
    #
    #     elif command == "mesure":
    #         return self.qsbuilder.question_mesure()
    #
    #     elif command == "arithm":
    #         return self.qsbuilder.question_arithm()
    #     elif command == "chronogram":
    #         print("quiz_builder:debug:arguments",args)
    #         return self.qsbuilder.question_chronogram(
    #         varlist= args.get("varlist",{}),
    #         flip_type=args.get("flip_type","D"),
    #         length=args.get("length",10),
    #         synch_type=args.get("synch_type","rising"),
    #         output_vars=args.get("output","Q")
    #         )
    #     elif command == "static_funct":
    #         return self.qsbuilder.question_static_funct(args["minterms"][0],
    #          args["var_names"], args["output_names"]
    #          ,args["dontcare"][0])
    #     elif command == "nand_funct":
    #         return self.qsbuilder.question_static_nand_exp(args["minterms"][0],
    #          args["var_names"], args["output_names"]
    #          ,args["dontcare"][0], method="nand")
    #     elif command == "nor_funct":
    #         return self.qsbuilder.question_static_nand_exp(args["minterms"][0],
    #          args["var_names"], args["output_names"]
    #          ,args["dontcare"][0], method="nor")
    #     elif command == "multi_funct":
    #         return self.qsbuilder.question_multi_funct(args["minterms"],
    #                args["var_names"], args["output_names"],
    #                args["dontcare"], method=args["method"])
    #     else:
    #         return "Question Error: %s"%command.replace('_',''), "Arabic", "Data", "Answer"

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
        def command_chronogram(args={}):
            # print("quiz_builder:debug:arguments",args)
            return self.qsbuilder.question_chronogram(
            varlist= args.get("varlist",{}),
            flip_type=args.get("flip_type","D"),
            length=args.get("length",10),
            synch_type=args.get("synch_type","rising"),
            output_vars=args.get("output","Q")
            )
        def command_static_funct(args={}):
            return self.qsbuilder.question_static_funct(minterms=args["minterms"][0],
             var_names=args["var_names"], output_names=args["output_names"]
             ,dont_care=args["dontcare"][0])
        def command_nand_funct(args={}):
            return self.qsbuilder.question_static_nand_exp(minterms=args["minterms"][0],
             var_names=args["var_names"], output_names=args["output_names"]
             ,dont_care=args["dontcare"][0], method="nand")
        def command_nor_funct(args={}):
            return self.qsbuilder.question_static_nand_exp(minterms=args["minterms"][0],
             var_names=args["var_names"], output_names=args["output_names"]
             ,dont_care=args["dontcare"][0], method="nor")
        def command_multi_funct(args={}):
            return self.qsbuilder.question_multi_funct(minterms_list=args["minterms"],
                   var_names=args["var_names"], output_names=args["output_names"],
                   dont_care_list=args["dontcare"], method=args["method"])
        def command_ascii_text(args={}):
            return self.qsbuilder.question_ascii(text=args["text"], method=args["method"])
        # خارطة تربط كل أمر بدالة إنشاء السؤال وما إذا كانت تتطلب معطيات
        question_map = {
            "float": (self.qsbuilder.question_vf, False),
            "intervalle": (self.qsbuilder.question_intervalle, False),
            "complement": (self.qsbuilder.question_cp, False),
            "exp": (self.qsbuilder.question_exp, False),
            "map": (self.qsbuilder.question_map, False),
            "map-sop": (self.qsbuilder.question_map_for_sop, False),
            "function": (self.qsbuilder.question_funct, False),
            "base": (self.qsbuilder.question_base, False),
            "arithm": (self.qsbuilder.question_arithm, False),
            "mesure": (self.qsbuilder.question_mesure, False),
            "ascii":(self.qsbuilder.question_ascii, False),
            "unicode":(self.qsbuilder.question_unicode, False),
            "bcd-x3":(self.qsbuilder.question_bcd_x3, False),
            "gray":(self.qsbuilder.question_gray, False),
            # command with parameters
            "ascii_text": (command_ascii_text, True),
            "static_funct": (command_static_funct, True),
            "nand_funct": (command_nand_funct, True),
            "nor_funct": (command_nor_funct, True),
            "multi_funct": (command_multi_funct, True),
            "chronogram": (command_chronogram, True),
        }

        entry = question_map.get(command)
        if not entry:
            return f"Unknown command: {command}", "Arabic", "Data", "Answer"

        question_func, needs_args = entry

        try:
            return question_func(args) if needs_args else question_func()
        except Exception as e:
            import traceback
            traceback_str = traceback.format_exc()
            print(f"Exception in get_question:\n{traceback_str}")
            return f"Error generating question '{command}': {e}", "Arabic", "Data", "Answer"

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
            qtext, _, _, ans = generated_question
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
        args ={"minterms":self.myconfig.minterms,
        "var_names": self.myconfig.var_names,
        "output_names": self.myconfig.output_names,
        "dontcare": self.myconfig.dontcare,
        "length":self.myconfig.length,
        "varlist":self.myconfig.varlist,
        "synch_type":self.myconfig.synch_type,
        "flip_type":self.myconfig.flip_type,
        "output":self.myconfig.output,
        "method":self.myconfig.method,
        "text":self.myconfig.text,
        # ~ "simplification":self.myconfig.simplification,
        }
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

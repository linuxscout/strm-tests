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

class quiz_builder:
    """ Generate the third test """
    def __init__(self, outformat="", config_file =""):

        self.qsbuilder = question_builder.Question_Builder(outformat)
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
        return question from command
        """
        if command == "float":
            return self.qsbuilder.question_vf()
        elif command == "intervalle":
            return self.qsbuilder.question_intervalle()
        elif command == "complement":
            return self.qsbuilder.question_cp()
        elif command == "exp":
            return self.qsbuilder.question_exp()
        elif command == "map":

            return self.qsbuilder.question_map()
        elif command == "map-sop":

            return self.qsbuilder.question_map_for_sop()
        elif command == "function":

            return self.qsbuilder.question_funct()
        elif command == "base":
            return self.qsbuilder.question_base()

        elif command == "mesure":
            return self.qsbuilder.question_mesure()

        elif command == "arithm":
            return self.qsbuilder.question_arithm()
        elif command == "chronogram":
            print("quiz_builder:debug:arguments",args)
            return self.qsbuilder.question_chronogram(
            varlist= args.get("varlist",{}),
            flip_type=args.get("flip_type","D"),
            length=args.get("length",10),
            synch_type=args.get("synch_type","rising"),
            output_vars=args.get("output","Q")
            )
        elif command == "static_funct":
            return self.qsbuilder.question_static_funct(args["minterms"][0],
             args["var_names"], args["output_names"]
             ,args["dontcare"][0])
        elif command == "nand_funct":
            return self.qsbuilder.question_static_nand_exp(args["minterms"][0],
             args["var_names"], args["output_names"]
             ,args["dontcare"][0], method="nand")
        elif command == "nor_funct":
            return self.qsbuilder.question_static_nand_exp(args["minterms"][0],
             args["var_names"], args["output_names"]
             ,args["dontcare"][0], method="nor")
        elif command == "multi_funct":
            return self.qsbuilder.question_multi_funct(args["minterms"], 
                   args["var_names"], args["output_names"],
                   args["dontcare"], method=args["method"])
        else:
            return "Question Error: %s"%command.replace('_',''), "Arabic", "Data", "Answer"
            
    def test(self, questions_names, rand=True, nb=2, repeat=2, args={}):
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
            qtext, ar, data, ans = generated_question
            # ~ qtext, ar, data, ans = value
            q_no = "Q%d"%(cpt+1)
            item = {"id":q_no,
            "category": name,
            "question":qtext,
            "arabic":ar,
            "data":data,
            "answer":ans,                
            }
            quiz_questions.append(item)
        self.formater.add_test(quiz_questions)

    def test2(self, questions_names, rand=True, nb=2, repeat=2, args={}):
        """ generate a test"""
        if rand:
            questions_names = random.sample(questions_names, nb)
        # generate question from  command
        questions = [self.get_question(q, args=args) for q in questions_names]
        # ~ for i in range(repeat): " ignore repeat"
        for cpt, value in enumerate(questions):
            q, ar, data, an = value
            q_no = "Q%d"%(cpt+1)
            self.formater.add_section(q_no,level=4)
            self.formater.add_text(q,ar)
            self.formater.add_text(data)
        self.formater.add_hrule()
        self.formater.add_newpage()
        self.formater.add_section("Correction",level=2)
        
        for cpt, value in enumerate(questions):
            q, ar, data, ans = value
            q_no = "Q%d"%(cpt+1)
            self.formater.add_section(q_no,level=4)
            self.formater.add_text(ans)

    
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
        # ~ "simplification":self.myconfig.simplification,
        }
        test_config = self.get_quiz_config(test_no)
        for test in test_config:
            for i in range(nb_questions):
                self.formater.open_question(test)
                self.formater.add_section("Question", level=1)
                self.test(test, rand=randq, repeat=repeat, args=args)        
                self.formater.add_newpage()
                self.formater.close_question(test)
        return self.formater.display()





def main(args):
    builder = quiz_builder()
    args ={"minterms":[1,2,3]}
    test = builder.get_quiz(4,repeat=1, args=args)
    print(test)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

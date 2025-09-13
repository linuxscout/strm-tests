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
from typing import Dict,  Optional
logging.basicConfig(
    level=logging.INFO,  # change to INFO or WARNING in production
    format="%(levelname)s:%(name)s:%(message)s"
)
logger = logging.getLogger(__name__)
import random

from . import read_config
from .display import quiz_format_factory
from strmquiz.question_builder.question_builder_factory import question_builder_factory
from .argschemaloader import  myArgsValidator
from typing import TypedDict, Any

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
    _CATEGORIES_INFO = question_builder_factory.get_categories_info()
    _COMMANDS_INFO = question_builder_factory.get_commands_info()
    _TEMPLATES_MAP = question_builder_factory.get_templates_map()
    def __init__(self, outformat="", config_file="", lang="", templates_dir="", args_file=""):

        # --- Check if templates_dir exists
        if not templates_dir or not os.path.isdir(templates_dir):
            raise FileNotFoundError(f"Template directory not found: '{templates_dir}'")
        self.templates_dir = templates_dir
        self.lang = lang
        # --- If no config file provided, use default
        if not config_file:
            config_file = os.path.join(os.path.dirname(__file__), "config", "quiz.default.conf")


        # --- Check if config_file exists
        if not os.path.isfile(config_file):
            raise FileNotFoundError(f"Config file not found: '{config_file}'")


        # --- If no config file provided, use default
        if not args_file:
            args_file = os.path.join(os.path.dirname(__file__), "config", "args.default.json")

        # --- Check if args_file exists
        if not os.path.isfile(args_file):
            raise FileNotFoundError(f"Args file not found: '{args_file}'")
        # --- Save attributes
        self.config_file = config_file
        self.args_file = args_file

        # --- Factories

        # self.encode_qsbuilder = question_builder_factory.factory(builder_name="encoding")
        # # self.encode_qsbuilder.set_random(False)
        # self.bool_qsbuilder = question_builder_factory.factory(builder_name="boolean")
        # self.seq_qsbuilder = question_builder_factory.factory(builder_name="sequential")
        # self.builders_map = {
        #     "encoding": self.encode_qsbuilder,
        #     "boolean algebra": self.bool_qsbuilder,
        #     "sequential logic": self.seq_qsbuilder,
        # }
        self.builders_map = question_builder_factory.map_factory()

        self.formater = quiz_format_factory.quiz_format_factory.factory(outformat, lang=lang, templates_dir=templates_dir)

        # --- Load config
        self.myconfig = read_config.ReadConfig(config_file)

        self.quiz_commands = {}
        self.quiz_commands[1] = [["base", "base", "arithm"],
        ["mesure", "base", "arithm"],
        ["base", "mesure", "arithm"],
        
        ]
        self.quiz_commands[2] = [["float", "map"],
        ["float", "map-sop"],
        ["float", "function"],
        ["complement","complement", "map"],
        ["function", "exp"],
        ]
        self.quiz_commands[3] =  [
        ["function", "exp"],
        ["function", "map"],
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
        # --- Commands metadata (optional) ---
        self.commands_info = type(self)._COMMANDS_INFO
        # self.commands_info = self._load_commands_info()
        self.commands = list(self.commands_info.keys())
        self.categories_info = type(self)._CATEGORIES_INFO
        # self.categories_info = self._load_categories_info()
        # self.TEMPLATE_MAP = self._load_templates_map()
        self.TEMPLATE_MAP = type(self)._TEMPLATES_MAP

        # self.validation_schema_loader = myArgsValidator(self.get_commands_info())
        self.myvalidation_schema_loader = myArgsValidator(self.get_commands_info())

        self.select_random_values = True
        # --- Load args from json file if given, or from api
        self.my_args_dict = self.load_args()


    def get_quiz_commands(self, quiz_id):
        if self.myconfig.test_table:
            if quiz_id:
                return self.get_quiz_config(quiz_id)
            else:
                return  self.myconfig.test_table
        else:
            if quiz_id:
                return self.quiz_commands.get(quiz_id, {})
            else:
                return  self.quiz_commands

    def get_quiz_id_list(self):
        if self.myconfig.test_table:
            return (self.myconfig.test_table.keys())
        return list(self.quiz_commands.keys())

    def set_select_random_values(self, rand):
        self.select_random_values = bool(rand)
        for key in self.builders_map:
            self.builders_map[key].set_random(rand)


    def get_loaded_args(self):
        return self.my_args_dict

    # def _load_templates_map(self):
    #     return question_builder_factory.get_templates_map()
    #     templates = {}
    #     for key in self.builders_map:
    #         templates.update(self.builders_map[key].get_templates_map())
    #     return templates

    # def _load_commands_info(self):
    #     return question_builder_factory.get_commands_info()
    #     all_info = {}
    #     for key in self.builders_map:
    #         all_info.update(self.builders_map[key].get_commands_info())
    #     return all_info

    # def _load_categories_info(self):
    #     return question_builder_factory.get_categories_info()
    #     categories = {}
    #     for key in self.builders_map:
    #         categories[key] = self.builders_map[key].get_category_info().get(key,{})
    #     return categories

    def load_args(self, args_src:Dict[str, Any]={})-> Dict[str, Any]:
        """load args from file or api"""
        validated_args = {}
        # if no agrs given load defaul args from file
        if not args_src and self.args_file:
            args_src = self.args_file
        elif isinstance(args_src, Dict):
            args_src = args_src
        else: # no args sources and no args_file
            return {}
        # load schema of commands and args
        args_loader = myArgsValidator(args_src)
        # Pick one command (e.g. counter)
        for command in self.commands_info:
            command_schema = self.myvalidation_schema_loader.get_command_schema(command)
            args_values = args_loader.get_command_schema(command)
            validator = myArgsValidator(command_schema)
            # store validated args in a dict
            validated_args[command] = validator.validate_args(args_values)
        logger.debug(f"Loaded args: {validated_args}")
        return validated_args

    def validate_command_args(self, command="", args_src:Dict[str, Any]={})-> Dict[str, Any]:
        """
        if provided data contains mutiple commands and is a dict of dict.
        """
        """load args from file or api"""
        # if not args, load default args from file
        if isinstance(args_src, Dict):
            args_dict = args_src.get(command, {})
        else: # no args sources and no args_file
            return {}

        schema_loader = self.myvalidation_schema_loader
        logger.debug(f"dict_args:{args_dict}")
        validated_args = schema_loader.validate_args(args_dict, command=command)
        return validated_args

    def get_template(self, name):
        temp = self.TEMPLATE_MAP.get(name, "default")
        if temp == "default":
            raise NotImplementedError(f"Not Implemented template for command '{name}'")
        return temp

    @staticmethod
    def get_available_formats()->dict:
        """return all available format"""
        return quiz_format_factory.quiz_format_factory.get_available_format()

    def set_format(self, outformat="latex"):
        """ set a new format"""
        is_available = quiz_format_factory.quiz_format_factory.is_available_format(outformat)
        if outformat != self.get_format() and is_available:
            self.formater = quiz_format_factory.quiz_format_factory.factory(outformat, templates_dir=self.templates_dir)
            logger.debug(f"Changed formatter into {outformat} from {self.get_format()} is available {is_available}")
        else:
            logger.debug(f"Not Changed formatter into {outformat} from from {self.get_format()}  is available {is_available}")

    def get_format(self,):
        """ get current used format a new format"""
        return self.formater.get_format()

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

    def get_args(self, command=''):
        """
        return args, for a specific command if needed
        """
        # params are stored in config file
        # TODO: get agrs from api or from json file
        args = self.myconfig.__dict__
        if command:
            return self.my_args_dict.get(command,{})
        else:
            return self.my_args_dict.copy()

        return args

    def get_question(self, command, args=None):
        """Generate a question based on command by delegating to the correct builder."""
        if args is None:
            args = self.get_args(command = command)

        # Determine the correct builder
        category = self.commands_info.get(command, {}).get("category", "")


        builder = self.builders_map.get(category)
        if not builder:
            return f"Unknown command category for '{command}'", "Answer"

        # Delegate to builder's internal get_question
        try:
            result = builder.get_question(command, args)
            if isinstance(result, dict):
                return self._render(self.get_template(command), result)
            else:
                raise ValueError(f"Command '{command}' must return a context dict, got {result}")
        except Exception as e:
            import traceback
            traceback_str = traceback.format_exc()
            logger.error(f"Error generating question '{command}': {traceback_str}")
            return f"Error generating question '{command}': {e}", "Answer"

    def build_quiz(self, questions_names, rand=True, nb=2, repeat=2, args={}):
        """ generate a test"""
        if rand:
            questions_names = random.sample(questions_names, nb)
        # generate question from  command
        # questions = [self.get_question(q, args=args) for q in questions_names]
        # ~ for i in range(repeat): " ignore repeat"
        quiz_questions = []
        for cpt, name in enumerate(questions_names):
            generated_question = self.get_question(name, args=args.get(name,{}))
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
    def get_commands_list(self,category=""):
        """ list all existing question types """
        if not category:
            return self.commands
        else:
            return [name for name, info in self.commands_info.items() if info["category"] == category]
    # @classmethod
    @classmethod
    def get_commands_info(cls, category=""):
        """ list all existing question types """
        if not category:
            return cls._COMMANDS_INFO
        else:
            return {cmd:cls._COMMANDS_INFO[cmd] for cmd in cls._COMMANDS_INFO if cls._COMMANDS_INFO[cmd]["category"]==category}

    def get_quiz(self,test_no="test1"):
        """
        Generate a test by number according to config file
        """

        randq = False
        randq = self.myconfig.random_question
        nb_questions = self.myconfig.questions_size
        repeat = self.myconfig.repeat
        args = self.get_args()
        test_config = self.get_quiz_config(test_no)
        for test in test_config:
            for i in range(nb_questions):
                self.formater.open_question(test)
                self.formater.add_section("Question", level=1)
                self.build_quiz(test, rand=randq, repeat=repeat, args=args)
                self.formater.add_newpage()
                self.formater.close_question(test)
        return self.formater.display()


    @classmethod
    def get_categories(cls) -> dict[str, CategoryInfo]:
        """
        Return a dictionary of categories with descriptions and their commands.
        """
        categories: dict[str, CategoryInfo] = {}
        for cat, meta in cls._CATEGORIES_INFO.items():
            logger.debug(f"{cat}:{meta}")
            categories[cat] = {
                "short": meta.get("short",''),
                "long": meta.get("long",""),
                "commands": [
                    {
                        "name": name,
                        "short": info["short"],
                        "long": info["long"]
                    }
                    for name, info in cls._COMMANDS_INFO.items()
                    if info["category"] == cat
                ]
            }
        return categories

    def get_short_description(self, cmd: str) -> str:
        """Return short description for a command."""
        return self.commands_info.get(cmd, {}).get("short", f"No short description for '{cmd}'")

    def get_long_description(self, cmd: str) -> str:
        """Return long description for a command."""
        return self.commands_info.get(cmd, {}).get("long", f"No long description for '{cmd}'")


    def get_random_commands(self, n: int = 3, category: Optional[str] = None) -> dict[str, CommandInfo]:
        """
        Return a list of n random commands (name, info).
        If category is given, pick only from that category.
        """
        cmds = self.get_commands_list(category=category)

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

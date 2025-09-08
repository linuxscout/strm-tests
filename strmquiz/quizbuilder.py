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
import json
import logging
# --- Configure logging ---
import os.path
from typing import Any, Dict, Union

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
from .argschemaloader import ArgValidator, ArgSchemaLoader
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
    def __init__(self, outformat="", config_file="", lang="", templates_dir="", args_file=""):

        # --- Check if templates_dir exists
        if not templates_dir or not os.path.isdir(templates_dir):
            raise FileNotFoundError(f"Template directory not found: '{templates_dir}'")

        # --- If no config file provided, use default
        if not config_file:
            config_file = os.path.join(os.path.dirname(__file__), "config", "quiz.conf")


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
        self.qsbuilder = question_builder_factory.factory( builder_name="",)
        self.encode_qsbuilder = question_builder_factory.factory(builder_name="encoding")
        self.encode_qsbuilder.set_random(False)
        self.bool_qsbuilder = question_builder_factory.factory(builder_name="boolean")
        self.seq_qsbuilder = question_builder_factory.factory(builder_name="sequential")

        self.formater = quiz_format_factory.quiz_format_factory.factory(outformat, lang=lang, templates_dir=templates_dir)

        # --- Load config
        self.myconfig = read_config.ReadConfig(config_file)



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
        # --- Commands metadata (optional) ---
        self.commands_info = self._load_commands_info()
        self.commands = list(self.commands_info.keys())
        self.categories_info = self._load_categories_info()
        self.TEMPLATE_MAP = self._load_templates_map()
        # --- Load args from json file if given, or from api
        self.my_args_dict = self.load_args()
    def _load_templates_map(self):
        templates = {}
        for builder in [self.encode_qsbuilder, self.bool_qsbuilder, self.seq_qsbuilder]:
            templates.update(builder.get_templates_map())
        return templates

    def _load_commands_info(self):
        all_info = {}
        for builder in [self.encode_qsbuilder, self.bool_qsbuilder, self.seq_qsbuilder]:
            all_info.update(builder.get_commands_info())
        return all_info

    def _load_categories_info(self):
        categories = {}
        for builder in [self.encode_qsbuilder, self.bool_qsbuilder, self.seq_qsbuilder]:
            categories[builder.CATEGORY] = builder.get_category_info()
        return categories

    def load_args(self, args_src:Dict[str, Any]={})-> Dict[str, Any]:
        """load args from file or api"""
        validated_args = {}
        if not args_src and self.args_file:
            args_src = self.args_file
        elif isinstance(args_src, Dict):
            args_src = args_src
        else: # no args sources and no args_file
            return {}
        # load schema of commands and args
        schema_loader = ArgSchemaLoader(self.get_commands_info())
        args_loader = ArgSchemaLoader(args_src)
        # Pick one command (e.g. counter)
        for command in self.commands_info:
            command_schema = schema_loader.get_command_schema(command)
            args_values = args_loader.get_command_schema(command)
            validator = ArgValidator(command_schema)
            # store validated args in a dict
            validated_args[command] = validator.validate_args(args_values)
        logger.debug(f"Loaded args: {validated_args}")
        return validated_args


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
        builder_map = {
            "encoding": self.encode_qsbuilder,
            "boolean algebra": self.bool_qsbuilder,
            "sequential logic": self.seq_qsbuilder,
        }

        builder = builder_map.get(category)
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

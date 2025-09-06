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

from .display import quiz_format_factory

from deprecated import deprecated
# 🔹 Constants
LANG_AR = "arabic"
LANG_EN = "english"


class Question_Builder:
    """Generate quiz questions for different domains."""

    def __init__(self, outformat="latex", config_file="", lang="ar-en", templates_dir="",):
        pass
        # 🔹 Inject dependencies (makes testing easier)
        # self.qs = question.questionGenerator(latex=True)
        # self.bq = boolquiz.bool_quiz()
        # self.bq.set_format('')
        # self.vf = ieee754.float_point()

        self.formater = quiz_format_factory.quiz_format_factory.factory(outformat)
        self.formater = None

        self.randomize = True
        self.command_map = {}
        self.CATEGORY = ""
        self.categories_info = {
            self.CATEGORY: {
                "short": "Short description for default catogory for Abstract Question builder",
                "long": "Long description for default catogory for Asbtract Question builder."
            },
        }
        self.commands_info = {}
        self.templates_map = {}
    # 🔹 Common rendering helper
    # @deprecated(reason=" All format and rendrening operation are moved to quizbuilder")
    # def _render(self, template: str, context: dict):
    #     """Render a question and answer using the current formatter."""
    #     try:
    #         q, a = self.formater.render_question_answer(template, context)
    #         # return q, LANG_AR, "data", a
    #         return q, a
    #     except Exception as e:
    #         logger.exception("Error rendering template %s", template)
    #         return f"Error: {e}",  "Error"



    def set_random(self, value:bool=True):
        self.randomize = bool(value)

    # def use_formatter(self, formatter=None):
    #     obj = formatter
    #     method_name = "render_question_answer"
    #     method = getattr(obj, method_name, None)
    #     if not callable(method):
    #         raise AttributeError(f"In method 'use_formatter', {obj.__class__.__name__} has no callable method '{method_name}'")
    #     else:
    #         self.formater = formatter
    #     return method


    def get_question(self, command, args):
        # func = self.command_map.get(command)
        # if not func:
        #     raise ValueError(f"Unknown Encoding command '{command}'")
        # return func(args)
        entry = self.command_map.get(command)
        if not entry:
            return f"Unknown command: {command}", "Answer"
            # return f"Unknown command: {command}", "Arabic", "Data", "Answer"

        question_func, needs_args = entry

        try:
            result = question_func(args) if needs_args else question_func()
            if isinstance(result, dict):
                return result
            else:
                raise BaseException(f"Warning to be fixed '{command}' not return a context dict {result}")
        except Exception as e:
            import traceback
            traceback_str = traceback.format_exc()
            print(f"Exception in get_question:\n{traceback_str}")
            return f"Error generating question '{command}': {e}", "Answer"


    def get_commands_info(self):
        return self.commands_info

    def get_templates_map(self):
        return self.templates_map

    def get_category_info(self):
        return self.categories_info.get(self.CATEGORY,
                                        {"short":"No short description",
                                        "long":"No long description"}
                                        )
def main(args):
    pass

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

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

from strmquiz.display import quiz_format_factory

class Question_Builder:
    """Generate quiz questions for different domains."""
    _CATEGORY = ""
    _CATEGORIES_INFO = {
        _CATEGORY: {
            "short": "Short description for default catogory for Abstract Question builder",
            "long": "Long description for default catogory for Asbtract Question builder."
        },
    }
    _COMMANDS_INFO = {}
    _TEMPLATES_MAP = {}

    def __init__(self,):

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

    def set_random(self, value:bool=True):
        self.randomize = bool(value)

    def get_question(self, command, args):
        entry = self.command_map.get(command)
        if not entry:
            return f"Unknown command: {command}", "Answer"

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

    @classmethod
    def get_commands_info(cls):
        return cls._COMMANDS_INFO
    @classmethod
    def get_templates_map(cls):
        return cls._TEMPLATES_MAP
    @classmethod
    def get_category_info(cls):
        return cls._CATEGORIES_INFO #.get(cls._CATEGORY)
    @classmethod
    def get_category_name(cls):
        return cls._CATEGORY
def main(args):
    pass

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

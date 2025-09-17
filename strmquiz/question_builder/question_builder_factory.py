#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz_factory.py
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

from strmquiz.question_builder.boolean_question_builder import \
    BooleanQuestionBuilder
from strmquiz.question_builder.encoding_question_builder import \
    EncodingQuestionBuilder
from strmquiz.question_builder.question_builder import Question_Builder
from strmquiz.question_builder.sequential_question_builder import \
    SequentialQuestionBuilder


class question_builder_factory:
    _CATEGORY = ""
    _CATEGORIES_INFO = (
        EncodingQuestionBuilder.get_category_info()
        | BooleanQuestionBuilder.get_category_info()
        | SequentialQuestionBuilder.get_category_info()
    )
    _COMMANDS_INFO = (
        EncodingQuestionBuilder.get_commands_info()
        | BooleanQuestionBuilder.get_commands_info()
        | SequentialQuestionBuilder.get_commands_info()
    )
    _TEMPLATES_MAP = (
        EncodingQuestionBuilder.get_templates_map()
        | BooleanQuestionBuilder.get_templates_map()
        | SequentialQuestionBuilder.get_templates_map()
    )

    def __init__(
        self,
    ):
        pass

    @staticmethod
    def factory(builder_name=""):
        if builder_name == EncodingQuestionBuilder.get_category_name():
            return EncodingQuestionBuilder()
        elif builder_name == BooleanQuestionBuilder.get_category_name():
            return BooleanQuestionBuilder()
        elif builder_name == SequentialQuestionBuilder.get_category_name():
            return SequentialQuestionBuilder()
        else:

            return Question_Builder()
        pass

    @classmethod
    def map_factory(cls):
        builders_map = {}
        for cat in cls._CATEGORIES_INFO:
            if cat == EncodingQuestionBuilder.get_category_name():
                builders_map[cat] = EncodingQuestionBuilder()
            elif cat == BooleanQuestionBuilder.get_category_name():
                builders_map[cat] = BooleanQuestionBuilder()
            elif cat == SequentialQuestionBuilder.get_category_name():
                builders_map[cat] = SequentialQuestionBuilder()
            else:
                builders_map[cat] = Question_Builder()
        return builders_map.copy()

    @classmethod
    def get_commands_info(cls):
        return cls._COMMANDS_INFO

    @classmethod
    def get_templates_map(cls):
        return cls._TEMPLATES_MAP

    @classmethod
    def get_categories_info(cls):
        return cls._CATEGORIES_INFO  # .get(cls._CATEGORY)


def main(args):
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv))

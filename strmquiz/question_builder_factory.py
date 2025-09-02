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

from .question_builder import Question_Builder
from .encoding_question_builder import EncodingQuestionBuilder
from .boolean_question_builder import BooleanQuestionBuilder
from .sequential_question_builder import  SequentialQuestionBuilder
class question_builder_factory:
    def __init__(self,):
        pass
    @staticmethod
    def factory(builder_name="", outformat="", config_file ="", lang="", templates_dir=""):
        if builder_name == "encoding":
            return  EncodingQuestionBuilder(outformat=outformat, lang=lang, templates_dir=templates_dir)
        if builder_name == "boolean":
            return  BooleanQuestionBuilder(outformat=outformat, lang=lang, templates_dir=templates_dir)
        if builder_name == "sequential":
            return  SequentialQuestionBuilder(outformat=outformat, lang=lang, templates_dir=templates_dir)
        else:

            return  Question_Builder(outformat=outformat, lang=lang, templates_dir=templates_dir)
        pass

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_format_tex.py
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

from . import quiz_format

class quiz_format_json(quiz_format.quiz_format):
    """ Generate a format for the test """
    def __init__(self, formatting="", lang="ar-en", templates_dir=""):

       super().__init__(formatting="json", lang=lang, templates_dir=templates_dir)
       pass

    def display(self,):
        """
        """
        # ~ return repr(self.tests )
        return json.dumps(self.tests )
    def render_question_answer(self, template_base: str, context: dict) -> tuple[str, str]:
        """
        عرض نص السؤال والجواب باستخدام القوالب المناسبة للغة والتنسيق.

        Args:
            template_base (str): اسم الأساس للقالب (مثل 'float' أو 'intervalle')
            context (dict): البيانات المستعملة في القالب

        Returns:
            tuple[str, str]: (نص السؤال، نص الجواب)
        """
        # In json we have not templates for question,
        # we return only parameters
        context["languages"] = ["ar","en", "fr"]
        question =answer = json.dumps(context)
        return question, answer
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mqg_gift.py
#  
#  Copyright 2021 zerrouki <zerrouki@majd4>
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
import sys
from moodle_question_generator import moodleQuestionGenerator

class MQG_gift(moodleQuestionGenerator):
    def __init__(self, category="None"):
        
        self.category = []
    def save(self, filename):
        """save generated questions to file"""
        if filename:
            try:
                fl = open(filename,"w")
                for q in self.category:
                    fl.write((q))
            except:
                print("Can't open file", filename)
                sys.exit()
        else:
            for q in questlist:
                print((q))
    def add(self, question):
        """ add the current question into question list"""
        self.category.append(question)
            
    def shortanswer(self, questext, answers, wrongs=[]):
        """ generate a short quesion"""
        answers = u", =".join(answers)
        if wrongs:
            answers +=", "+ u", ~".join(wrongs)
        question = u"""{questtext}{{={answer}}}\n\n""".format(qid="0", name="Convert Base", questtext=questext,
     answer=answers, note="Rien")
        return question

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

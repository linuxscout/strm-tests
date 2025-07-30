#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mqg_xml.py
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

from moodle_question_generator import moodleQuestionGenerator
from moodlexport import Question, Category

class MQG_xml(moodleQuestionGenerator):
    def __init__(self, category="None"):
        
        self.category = Category(category)
        
    def convertbase(self, base1=10, base2=2, start=0 ,end = 1):
        questlist = []
        for i in range(start,end):
            questvalue = "<p>Convert from base %d to base %d</p>\\nthe following number <p>%d</p>"%(base1, base2,i)
            
            answer = u"%s"%questionGenerator.int2base(i, base2)
            questext = self.shortanswer_question(questvalue, answer)
            questlist.append(questext)
        return questlist
            
    def shortanswer(self, questext, answers, wrongs =[]):
        """ generate a short quesion"""
        question = Question("essay")
        question.text(questext)
        question.grade(1)
        return question
    def save(self,filename):
        """ export questions"""
        self.category.save(filename)
    def add(self, question):
        """ add the current question into question list"""
        question.addto(self.category)
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

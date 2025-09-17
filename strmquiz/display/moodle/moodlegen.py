#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  moodlegen.py
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
import random
import sys

from ieee754 import float_point
from mqg_gift import MQG_gift
from mqg_xml import MQG_xml
from question import questionGenerator


class MQG_builder:
    def __init__(self, output_format="GIFT"):

        if output_format.upper() == "GIFT":
            self.generator = MQG_gift()
        elif output_format.upper() == "XML":
            self.generator = MQG_xml()
        else:
            self.generator = MQG_gift()
        self.qgenerator = questionGenerator()

    def convertbase(self, base1=0, base2=0, start=0, end=0, randomize=False):
        questlist = []

        # interval if not given
        if not start and not end:
            start = 10
            end = 255
        for i in range(start, end):
            # random bases if not given
            if randomize:
                base_list = [
                    (2, 16),
                    (16, 2),
                    (10, 16),
                    (16, 10),
                    (8, 16),
                    (16, 8),
                    (7, 5),
                    (6, 12),
                ]
                base1, base2 = random.choice(base_list)
                # ~ base_list.remove(base1)
                # ~ base2 = random.choice(base_list)
            if base1 != 10:
                nb_source = questionGenerator.int2base(i, base1)
            else:
                nb_source = i
            nb_dist = questionGenerator.int2base(i, base2)
            questvalue = (
                "::Conversion base::Convertir de la base %d à la base  %d le nombre suivant %s "
                % (base1, base2, nb_source)
            )
            answers = ["%s" % nb_dist]
            wrongs = []
            questext = self.generator.shortanswer(questvalue, answers, wrongs)
            self.generator.add(questext)
        return questlist

    def comp_one_two(self, nbits=8, start=0, end=0, randomize=False):

        questlist = []
        # interval if not given
        if not start and not end:
            start = 10
            end = 255
        for i in range(start, end):
            # random bases if not given
            if randomize:
                nbits = random.choice([8, 10, 12, 16])
            n, binairy, comp1, comp2 = self.qgenerator.comp_one(nbits=nbits)
            if i <= end / 2:
                questvalue = (
                    "::Complément à 2:: Convertir le nombre suivant -%d en complément à 2 sur  %dbits"
                    % (n, nbits)
                )
                answers = ["%s" % comp2]
            else:
                questvalue = (
                    "::Complément à 2:: Convertir en binaire, le nombre suivant %s codé complément à 2 sur  %dbits"
                    % (comp2, nbits)
                )
                answers = ["-%d" % n]

            wrongs = []
            questext = self.generator.shortanswer(questvalue, answers, wrongs)
            self.generator.add(questext)
        return questlist

    def float_quest(self, n=0, iteration=10, randomize=False):

        questlist = []
        # interval if not given
        vf = float_point()
        for i in range(iteration):
            # random bases if not given
            if randomize:
                n = random.randint(10, 255) + round(random.random(), 3)

            hexfloat = vf.IEEE754(n)
            if i <= iteration / 2:
                questvalue = (
                    "::Virgule flottante:: Representer le nombre suivant en IEEE-754-32bits %f"
                    % (n)
                )
                answers = ["%s" % hexfloat]
            else:
                questvalue = (
                    "::Virgule flottante:: Decoder le nombre suivant codé en IEEE-754-32bits %s"
                    % (hexfloat)
                )
                answers = ["-%f" % n]

            wrongs = []
            questext = self.generator.shortanswer(questvalue, answers, wrongs)
            self.generator.add(questext)
        return questlist

    def save(self, filename):
        self.generator.save(filename)


def main(args):

    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv))

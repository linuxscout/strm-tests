#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  genmoodle.py
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
sys.path.append("../strm-test/")
sys.path.append("../")

import moodlegen

def main(args):
    gen_type="gift"
    # ~ gen_type="xml"
    mqg = moodlegen.MQG_builder(gen_type)
    # generate 10 question about base 10 to 16
    base1 = 10
    base2 = 16
    start = 10
    end = 25
    # ~ questlist = mqg.convertbase(base1, base2, start, end)
    questlist = mqg.convertbase(randomize=True)
    # ~ questlist = mqg.comp_one_two(randomize=True)
    # ~ questlist = mqg.float_quest(iteration=10, randomize=True)
    mqg.save("output/test.txt")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gen_random_minterms.py
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


def generate_minterms(length):

    list_mins = []
    l = list(range(16))
    for i in range(length):
        list_mins.append(random.sample(l, k=random.randint(3, 12)))
    return list_mins


def main(args):
    n = 10
    list_minterms = generate_minterms(n)
    print(list_minterms)
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv))

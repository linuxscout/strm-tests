#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  genarte_maxterm.py
#
#  Copyright 2022 zerrouki <zerrouki@majd4>
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
TermTables = {
    0: (0, 0, 0, 0),
    1: (0, 0, 0, 1),
    2: (0, 0, 1, 0),
    3: (0, 0, 1, 1),
    4: (0, 1, 0, 0),
    5: (0, 1, 0, 1),
    6: (0, 1, 1, 0),
    7: (0, 1, 1, 1),
    8: (1, 0, 0, 0),
    9: (1, 0, 0, 1),
    10: (1, 0, 1, 0),
    11: (1, 0, 1, 1),
    12: (1, 1, 0, 0),
    13: (1, 1, 0, 1),
    14: (1, 1, 1, 0),
    15: (1, 1, 1, 1),
}


def maxterm(n):
    term = []
    """ return a minterm for integer"""
    myterm = TermTables.get(n, (0, 0, 0, 0))
    variables = "abcd"
    for i in range(len(variables)):
        if myterm[i]:
            term.append(variables[i] + "'")
        else:
            term.append(variables[i])
    return "(%s)" % ("+".join(term))


def minterm(n):
    term = []
    """ return a minterm for integer"""
    myterm = TermTables.get(n, (0, 0, 0, 0))
    variables = "abcd"
    for i in range(len(variables)):
        if myterm[i]:
            term.append(variables[i])
        else:
            term.append(variables[i] + "'")
    return "(%s)" % ("+".join(term))


def main(args):
    dic = {}

    for n in range(16):
        dic[n] = minterm(n)
    print("minterms", dic)
    for n in range(16):
        dic[n] = maxterm(n)
    print("maxterms", dic)
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv))

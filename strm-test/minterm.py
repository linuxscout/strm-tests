#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  minterm.py
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

def minterm(n):
    """ return a minterm for integer"""
    term =[]
    for var in 'dcba':
        v = var if n % 2 ==1 else var +"'"
        n = n / 2
        term.append(v)
    term.sort()
    return ".".join(term)
    
def maxterm(n):
    term =[]         
    """ return a minterm for integer"""
    for var in 'dcba':
        v = var if n % 2 ==0 else var +"'"
        n = n / 2
        term.append(v)
    term.sort()
    return "(" + "+".join(term)+")"

def main(args):
    
    for i in range(16):
        #~ print i, minterm(i);
        print i, maxterm(i);
    return 0
    
if __name__ == '__main__':
    import sys
    
    sys.exit(main(sys.argv))

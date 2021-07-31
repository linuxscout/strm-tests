#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bool_const.py
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

REDUCTION_TABLE ={
    # one variable
    "a": "\\implicant{12}{10}",
    "a'": "\\implicant{0}{6}",
    "b":"\\implicant{4}{14}",
    "b'": "\\implicantedge{0}{2}{8}{10}",
    "c":"\\implicant{3}{10}",
    "c'":"\\implicant{0}{9}",
    "d":"\\implicant{1}{11}",
    "d'": "\\implicantedge{0}{8}{2}{10}", 
    # two variables
    #a
     "a.b": "\\implicant{12}{14}",     
     "a.b'": "\\implicant{8}{10}",     
     "a.c": "\\implicant{15}{10}",     
     "a.c'": "\\implicant{12}{9}",     
     "a.d": "\\implicant{13}{11}",     
     "a.d'": "\\implicantedge{12}{8}{14}{10}", 
     #a'     
     "a'.b": "\\implicant{4}{6}",     
     "a'.b'": "\\implicant{0}{2}",     
     "a'.c": "\\implicant{3}{6}",     
     "a'.c'": "\\implicant{0}{5}",     
     "a'.d": "\\implicant{1}{7}",     
     "a'.d'": "\\implicantedge{0}{4}{2}{6}",  
     # b       
     "b.c": "\\implicant{7}{14}",     
     "b.c'": "\\implicant{4}{13}",     
     "b.d": "\\implicant{5}{15}",     
     "b.d'": "\\implicantedge{4}{12}{6}{14}", 
    # b'
     "b'.c": "\\implicantedge{3}{2}{11}{10}",     
     "b'.c'": "\\implicantedge{0}{1}{8}{9}",     
     "b'.d": "\\implicantedge{1}{3}{9}{11}",     
     "b'.d'": " \implicantcorner{0}{2}", 
     # c       
     "c.d": "\\implicant{3}{11}",     
     "c.d'":"\\implicant{2}{10}", 
          
     "c'.d": "\\implicant{1}{9}",     
     "c'.d'":"\\implicant{0}{8}",  
     #d
     # Three variables
     # a
     "a.b.c": "\\implicant{15}{14}",     
     "a.b.c'": "\\implicant{12}{13}",     
     "a.b.d": "\\implicant{13}{15}",     
     "a.b.d'": "\\implicantedge{12}{12}{14}{14}", 
     
     "a.b'.c": "\\implicant{10}{10}",     
     "a.b'.c'": "\\implicant{8}{9}",     
     "a.b'.d": "\\implicant{9}{11}",     
     "a.b'.d'": "\\implicantedge{8}{8}{10}{10}", 
      
     "a.c.d": "\\implicant{15}{11}",     
     "a.c.d'": "\\implicant{14}{10}",     
     "a.c'.d": "\\implicant{13}{9}",     
     "a.c'.d'": "\\implicant{12}{8}",      
     # a'
     "a'.b.c": "\\implicant{7}{6}",     
     "a'.b.c'": "\\implicant{4}{5}",     
     "a'.b.d": "\\implicant{5}{7}",     
     "a'.b.d'": "\\implicantedge{4}{4}{6}{6}", 
     
     "a'.b'.c": "\\implicant{3}{2}",     
     "a'.b'.c'": "\\implicant{0}{1}",     
     "a'.b'.d": "\\implicant{1}{3}",     
     "a'.b'.d'": "\\implicantedge{0}{0}{2}{2}",       

     "a'.c.d": "\\implicant{3}{7}",     
     "a'.c.d'": "\\implicant{2}{6}",     
     "a'.c'.d": "\\implicant{1}{5}",     
     "a'.c'.d'": "\\implicant{0}{4}",      
      
     "b.c.d": "\\implicant{7}{15}",     
     "b.c.d'": "\\implicant{6}{14}",     
     "b.c'.d": "\\implicant{5}{13}",     
     "b.c'.d'": "\\implicant{4}{12}",      
      
     "b'.c.d": "\\implicantedge{3}{3}{11}{11}",     
     "b'.c.d'": "\\implicantedge{2}{2}{10}{10}",     
     "b'.c'.d": "\\implicantedge{1}{1}{9}{9}",     
     "b'.c'.d'": "\\implicantedge{0}{0}{8}{8}",      
    # Four vars
    "a'.b'.c'.d'": "\\implicant{0}{0}",
    "a'.b'.c'.d": "\\implicant{1}{1}",
    "a'.b'.c.d'": "\\implicant{2}{2}",
    "a'.b'.c.d": "\\implicant{3}{3}",
    "a'.b.c'.d'": "\\implicant{4}{4}",
    "a'.b.c'.d": "\\implicant{5}{5}",
    "a'.b.c.d'": "\\implicant{6}{6}",
    "a'.b.c.d": "\\implicant{7}{7}",
    "a.b'.c'.d'": "\\implicant{8}{8}",
    "a.b'.c'.d": "\\implicant{9}{9}",
    "a.b'.c.d'": "\\implicant{10}{10}",
    "a.b'.c.d": "\\implicant{11}{11}",
    "a.b.c'.d'": "\\implicant{12}{12}",
    "a.b.c'.d": "\\implicant{13}{13}",
    "a.b.c.d'": "\\implicant{14}{14}",
    "a.b.c.d": "\\implicant{15}{15}", 
   
}
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  question.py
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
import string
import random
import ieee754

class questionGenerator:
    """ class to generate question about some course parts"""
    def __init__(self, latex=False):
        self.latex= latex



    @staticmethod
    def int2base(x, base):
        """ convert an integer to a base"""
        digs = string.digits + string.ascii_letters    
        if x < 0:
            sign = -1
        elif x == 0:
            return digs[0]
        else:
            sign = 1

        x *= sign
        digits = []

        while x:
            digits.append(digs[int(x % base)])
            x = int(x / base)

        if sign < 0:
            digits.append('-')

        digits.reverse()

        return ''.join(digits) 
    @staticmethod
    def int2base(x, base, method=False):
        """ convert an integer to a base"""
        digs = string.digits + string.ascii_letters    
        if x < 0:
            sign = -1
        elif x == 0:
            return digs[0]
        else:
            sign = 1

        x *= sign
        digits = []
        text = ""
        while x:
            text +="%8d = %d x %7d + %6d\n"%(x,base, int(x/base), x%base)
            digits.append(digs[int(x % base)])
            x = int(x / base)

        if sign < 0:
            digits.append('-')

        digits.reverse()
        if method:
            return text
        return ''.join(digits) 
    @staticmethod
    def base2int(number, base, method=False):
        #split number in figures
        figures = [int(i,base) for i in str(number)]
        #invert oder of figures (lowest count first)
        figures = figures[::-1]
        result = 0
        text = []
        #loop over all figures
        for i in range(len(figures)):
            #add the contirbution of the i-th figure
            result += figures[i]*base**i
            text.append("%d x %d^%d"%(figures[i],base,i))
        text = " + ".join(text)
        text += "= %d"%result
        if method:
            return text
        return result
    def numeral_system(self, in_base = 0, out_base=0):
        """
        generate question in to out base
        """
        if not in_base and not out_base:
            base_list = [2,5,6,8,10,12,16]
            in_base = random.choice(base_list)
            base_list.remove(in_base)
            out_base = random.choice(base_list)
        n = random.randint(12, out_base**8)
        nb = self.int2base(n, in_base)
        method = self.int2base(n, in_base, True)
        res = self.int2base(n, out_base)
        
        return {"question":"(%s)_{%d} = (........)_{%d}"%(nb,in_base, out_base),
        "reponse":"(%s)_{%d} = (%s)_{%d}"%(nb, in_base,res, out_base),
        "method":method,
        }
    def dec2x(self, x, method=False):
        """ convert from base x to 10 """
        n = random.randint(12, x**8)
        nb = self.int2base(n, x)
        if method :
            return self.int2base(n, x, True)
        else:
            return nb     
    def x2dec(self, x, method=False):
        """ convert from base 10 to base x """
        n = random.randint(12, x**8)
        nb = self.int2base(n, x)
        if method :
            return self.int2base(n, x, True)
        else:
            return nb 


    def bin2(self, x, reverse = False, method=False):
        """ convert from base 10 to base x """
        n = random.randint(12, 2**20)
        nb  =  self.int2base(n, 2)
        res =  self.int2base(n, x)
        if x == 8:
            group = 3
            sep = " |   "
            begin = "  "
        else:
            group = 4
            sep = "  |   "
            begin = "  "            
        if method :
            if len(nb)% group != 0: 
                nbx = "0"*(group-len(nb)%group) + nb
            else:
                nbx = nb

            nbx_l = [nbx[i:i+group] for i in range(0, len(nbx), group)]
            textbin = " | ".join(nbx_l)
            textother = begin+ sep.join(list(res))
            if reverse:
                return u"\n".join([textother, textbin])
            return "\n".join([textbin, textother])
        else:
            if reverse:
                return res, nb
            return nb, res       
    
    def bin2oct(self,reverse = False, method=False):
        return self.bin2(16, reverse, method)
        
    def bin2hex(self, reverse = False, method=False):
        return self.bin2(16, reverse, method)

    def rand_numeral_system(self):
        """
        generate question in to out base
        """
        out_base = random.choice([2, 5, 6, 8, 12, 16])
        in_base = random.choice([2, 5, 6, 8, 12, 16])
        nb = random.randint(12, out_base**8)
        res = self.int2base(nb, out_base)
        
        return {"question":"$(%s)_{%d} = (........)_{%d}$"%(nb,in_base, out_base),
        "reponse":"$(%s)_{%d} = (%s)_{%d}$"%(nb, in_base,res, out_base),
        }
    def rand_arithm(self):
        """
        generate question in arithmetic mode
        """
        base = random.choice([2, 5, 6, 8, 12, 16])
        op = random.choice(["+","-"])
        if op == "+":
            a, b, c = self.addition_base(base)       
        else:
            a, b, c = self.sub_base(base)       

        question =u"Faire le opérations suivants  en base %d "%base
        
        return {"question": " %9s\n%s%9s\n----------\n\n"%(a,op, b),
        "reponse": " %9s\n%s%9s\n----------\n %9s\n"%(a,op,b,c),
        }
    def sys_num_reponse(self, x, y):
        """ print the solution"""
        
        if x == 10 and y != 10:
            self.int2base_repr(x,y)
            
    def addition_base(self, x, method=False):
        """ addition in base x """    
        a = random.randint(12, x**8)
        b = random.randint(12, x**8)
        c = a+b
        a = self.int2base(a, x)
        b = self.int2base(b, x)
        c = self.int2base(c, x)
        if method:
            text = " %9s\n+%9s\n----------\n %9s\n"%(a,b,c)
            return text
        return a,b,c
    
    def sub_base(self, x, method=False):
        """ addition in base x """    
        a = random.randint(12, x**8)
        b = random.randint(12, x**8)
        if a <b :
            a,b=b,a
        c = a-b
        a = self.int2base(a, x)
        b = self.int2base(b, x)
        c = self.int2base(c, x)
        if method:
            text = " %9s\n-%9s\n----------\n %9s\n"%(a,b,c)
            return text
        return a,b,c
    def bin2cp1(self, a, nbits):
        """ convert a binary int to complemnt to one"""
        if len(a) < nbits-1:
            a = "0"*(nbits-1-len(a)) +a
        b = "1" # sign bit
        for c in a:
            if c =="0":
                b+="1"
            else:
                b+="0"
        return b
    def comp_one(self, nbits, n=0, method=False):
        """ convert a number on n bits x """
        if not n:   
            n = random.randint(12, 2**(nbits-1))
        d = self.int2base(n-1, 2)
        a = self.int2base(n, 2)
        
        b = self.bin2cp1( a, nbits)
        e = self.bin2cp1( d, nbits)
        a = "-"+a
        if method:
            text = "$-%d\n%9s_2\n%9s_cp1\n%9s_cp2"%(n,a,b,e)
            tex = "\n\n$-%d$\n\n$%9s_{2}$\n\n$%9s_{cp1}$\n\n$%9s_{cp2}$"%(n,a,b,e)
            if self.latex :
                return tex
            return text
        return n,a,b,e
    
    def intervalle(self, n=0, method=False):
        """ specify the intervalle for n  bits """    
        if not n:
            n = random.randint(4, 100)
        text = u"Positifs [0; 2^(%d)-1]"%n
        text +="\n"+u"Valeur absolue [-(2^(%d)-1);2^(%d)-1]"%(n-1,n-1)
        text +="\n"+u"Compelement à 1 [-(2^(%d)-1);2^(%d)-1]"%(n-1,n-1)
        text +="\n"+u"Compelement à 2 [-(2^(%d)-1);2^(%d)-1]"%(n,n-1)
        text += u"\nPositifs [0; %d]"%(2**n-1)
        text +="\n"+u"Valeur absolue [%d; %d]"%(-(2**(n-1)-1),2**(n-1)-1)
        text +="\n"+u"Compelement à 1 [%d; %d]"%(-(2**(n-1)-1),2**(n-1)-1)
        text +="\n"+u"Compelement à 2 [%d; %d]"%(-2**(n-1),2**(n-1)-1)
        
        tex= u"Positifs $[0; 2^{%d}-1]$ [0; %d]"%(n , 2**n-1)
        tex +="\n\n"+u"Valeur absolue [$-(2^{%d}-1);2^{%d}-1$] = [%d; %d]"%(n-1,n-1, -(2**(n-1)-1),2**(n-1)-1)
        tex +="\n\n"+u"Compelement à 1 [$-(2^{%d}-1);2^{%d}-1$] = [%d; %d]"%(n-1,n-1, -(2**(n-1)-1),2**(n-1)-1)
        tex +="\n\n"+u"Compelement à 2 [$-(2^{%d}-1);2^{%d}-1$] = [%d; %d]"%(n,n-1, -(2**(n-1)),2**(n-1)-1)
        #~ tex += "\n\nPositifs [0; %d]"%(2**n-1)
        #~ tex +="\n\n"+u"Valeur absolue [%d; %d]"%(-(2**(n-1)-1),2**(n-1)-1)
        #~ tex +="\n\n"+u"Compelement à 1 [%d; %d]"%(-(2**(n-1)-1),2**(n-1)-1)
        #~ tex +="\n\n"+u"Compelement à 2 [%d; %d]"%(-2**(n-1),2**(n-1)-1)
        if method:
            if self.latex:
                return tex
            return text
        else:
            return n
        return text
    def ascii(self, s, method=False):
        """ convert a string to ascii code """
        
        l = list(s)
        a = []
        for c in l:
            a.append(hex(ord(c)))
        text = "  "+"  |   ".join(l) +"\n"
        text += " | ".join(a) +"\n"
        if method :
            return text
        else:
            return u" ".join(a)
def main(args):
    qs = questionGenerator()
    print qs.numeral_system(12,2)
    print qs.numeral_system()
    print(qs.int2base(152, 8, True))
    print(qs.dec2x(8, True))
    print(qs.base2int(152,8, True))
    print(qs.bin2oct(method=True))
    print(qs.bin2hex(method=True))
    print(qs.bin2oct(reverse =True,method= True))
    print(qs.bin2hex(reverse=True, method=True))
    print(qs.addition_base(6, method=True))
    print(qs.sub_base(6, method=True))
    print(qs.addition_base(2, method=True))
    print(qs.sub_base(2, method=True))
    print(qs.comp_one(8, method=True))
    print(qs.intervalle(16))
    print(qs.ascii("Taha Zerrouki@gmail.com", True))
    # float point
    vf = ieee754.float_point()
    vf.vf_question()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


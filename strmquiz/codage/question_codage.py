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
from . import codequestion_const as cqconst
class questionGenerator:
    """ class to generate question about some course parts"""
    def __init__(self, latex=False):
        self.latex= latex
        self.DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"



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
        base_list = [2, 2,2,2,2, 2,2,5, 6, 8,8,8, 12, 16,16,16]
        out_base = random.choice([2, 2,2,2,2, 2,2,5, 6, 8,8,8, 12, 16,16,16])
        in_base = random.choice(base_list)
        while in_base == out_base:
            in_base = random.choice(base_list)
        nb10 = random.randint(12, out_base**8)
        res = self.int2base(nb10, out_base)
        if in_base != 10:
            nb = self.int2base(nb10, in_base)
        else:
            nb = nb10
        
        return {"question":"$(%s)_{%d} = (........)_{%d}$"%(nb,in_base, out_base),
        "reponse":"$(%s)_{%d} = (%s)_{%d}$"%(nb, in_base,res, out_base),
        "number":nb,
        "in_base":in_base,
        "out_base":out_base,
        "output":res,
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
        "number_a":a,
        "number_b":b,
        "number_c":c,
        "operation":op,
        "base":base,
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
            n = random.randint(12, 2**(min(8,nbits-1)))
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

    def encode(self, s):
        """ convert a string to ascii code/unicode """
        return [hex(ord(c)) for c in s]

    def rand_text(self, code="ascii"):

        if code.lower() == "ascii":
            return random.choice(cqconst.ASCII_STRINGS)
        elif code.lower() == "unicode":
            return random.choice(cqconst.UNICODE_STRINGS)
        else:
            return random.choice(cqconst.ASCII_STRINGS)

    def dec_to_bcd(self, n: int) -> str:
        """
        Convert a decimal number to BCD (Binary Coded Decimal).
        Each digit is represented by 4 bits.
        """
        return ' '.join(f"{int(digit):04b}" for digit in str(n))

    def dec_to_excess3(self, n: int) -> str:
        """
        Convert a decimal number to Excess-3 code.
        Each digit is represented by 4 bits after adding 3.
        """
        return ' '.join(f"{int(digit) + 3:04b}" for digit in str(n))

    def bcd_to_dec(self, bcd: str) -> int:
        """
        Convert a BCD (Binary Coded Decimal) string to decimal.
        Input format: groups of 4 bits separated by spaces or not.
        Example: '0101 1001' -> 59
        """
        # Remove spaces and split into chunks of 4 bits
        bcd = bcd.replace(" ", "")
        digits = [bcd[i:i + 4] for i in range(0, len(bcd), 4)]
        return int(''.join(str(int(d, 2)) for d in digits))

    def excess3_to_dec(self, ex3: str) -> int:
        """
        Convert an Excess-3 code string to decimal.
        Input format: groups of 4 bits separated by spaces or not.
        Example: '1000 1100' -> 59
        """
        ex3 = ex3.replace(" ", "")
        digits = [ex3[i:i + 4] for i in range(0, len(ex3), 4)]
        return int(''.join(str(int(d, 2) - 3) for d in digits))

    def to_symbol(self, x: int) -> str:
        return self.DIGITS[x]

    def from_symbol(self, ch: str) -> int:
        """Convert a digit symbol to its integer value."""
        ch = ch.upper()
        if ch not in self.DIGITS:
            raise ValueError(f"Invalid digit symbol: {ch}")
        return self.DIGITS.index(ch)

    def number_to_digits(self, num_str: str, base: int):
        """
        Convert a number string in base X into a list of dicts:
        [{"symbol": "A", "value": 10}, ...]
        """
        digits = []
        num_str = str(num_str)
        for ch in num_str.upper():
            value = self.from_symbol(ch)
            if value >= base:
                raise ValueError(f"Digit '{ch}' not valid in base {base}")
            digits.append({"symbol": ch, "value": value})
        return digits

    def make_steps_from10(self, n: int, b: int):
        """explain convert base from 10 to base x"""
        steps = []
        x = n
        while x > 0:
            q, r = divmod(x, b)
            steps.append({
                "dividend": x,
                "quotient": q,
                "remainder": r,
                "symbol": self.to_symbol(r)
            })
            x = q
        return steps

    def make_steps_to10(self, n: int, b: int):
        """explain convert base from base X to base 10"""
        steps = []
        x = n
        return steps
    def int_to_bin4(self, n: int) -> str:
        """Convert integer (0–15) to 4-bit binary string."""
        return format(n & 0xF, "04b")

    def bcd_addition_explainXX(self, a_digits, b_digits):
        """
        Perform BCD addition digit by digit (right to left).
        a_digits, b_digits are lists of 4-bit binary strings (["0010","0101"]).
        Returns a dict suitable for rendering in HTML.
        """
        n = len(a_digits)
        carries = [0]  # initial carry
        sums_bin, sums_dec = [], []
        corrections = []
        final_digits_bin, final_digits_dec = [], []

        for i in range(n):
            da = int(a_digits[i], 2)
            db = int(b_digits[i], 2)
            raw_sum = da + db + carries[i]

            sums_bin.append(self.int_to_bin4(raw_sum))
            sums_dec.append(raw_sum)

            if raw_sum > 9:  # needs correction
                corrections.append("+0110")
                corrected = raw_sum + 6
                final_digits_bin.append(self.int_to_bin4(corrected % 16))
                final_digits_dec.append(corrected % 10)
                carries.append(1)
            else:
                corrections.append("---")
                final_digits_bin.append(self.int_to_bin4(raw_sum))
                final_digits_dec.append(raw_sum % 10)
                carries.append(0)

        # Check for extra carry
        extra_digit_bin, extra_digit_dec = None, None
        if carries[-1] == 1:
            extra_digit_bin = "0001"
            extra_digit_dec = 1

        return {
            "digits_a_bin": a_digits,
            "digits_b_bin": b_digits,
            "digits_a_dec": [int(x, 2) for x in a_digits],
            "digits_b_dec": [int(x, 2) for x in b_digits],
            "carry_in": carries[:-1],
            "carry_out": carries[1:],
            "sums_bin": sums_bin,
            "sums_dec": sums_dec,
            "corrections": corrections,
            "final_digits_bin": final_digits_bin,
            "final_digits_dec": final_digits_dec,
            "extra_digit_bin": extra_digit_bin,
            "extra_digit_dec": extra_digit_dec,
            "A_total_dec": int("".join(str(int(x,2)) for x in a_digits)),
            "B_total_dec": int("".join(str(int(x,2)) for x in b_digits)),
            "Result_total_dec": int(
                (str(extra_digit_dec) if extra_digit_dec else "") +
                "".join(str(d) for d in final_digits_dec)
            ),
        }

    def bcd_addition_explain(self, a, b):
        """
        Perform BCD addition digit by digit (right to left).
        a, b: two integers
        Returns a dict suitable for rendering in HTML/Latex.
        """
        max_digit = 16
        # detect the max length
        ln = max(len(str(a)), len(str(b)), len(str(a+b)))
        # add extra zeros to align numbers
        a_str = str(a).zfill(ln)
        b_str = str(b).zfill(ln)
        c_str = str(a + b).zfill(ln)
        a_digits = self.dec_to_bcd(a_str).split(" ")
        b_digits = self.dec_to_bcd(b_str).split(" ")
        c_digits = self.dec_to_bcd(c_str).split(" ")

        a_decimals = list(a_str)
        b_decimals = list(b_str)
        c_decimals = list(c_str)
        # get carries
        # to avoid out of range
        # added to first line
        carries_before_correct = [0] * (ln + 1)
        # added to the correciton step
        carries_after_correct = [0] * (ln + 1)
        corrections = [0] * ln
        tmp_decimals = [0] * ln
        tmp_digits = ["0000"] * ln
        result_dec = [0]*ln
        for i in range(ln - 1, -1, -1):
            ai = int(a_decimals[i])
            bi = int(b_decimals[i])
            ci = int(c_decimals[i])
            # get carries
            ci_tmp = ai + bi + carries_before_correct[i + 1]
            if ci_tmp > ci:
                corrections[i] = 6
                # if a + b and carry < 16ة
                # it generate a bin numnber without carry
                if ci_tmp >= max_digit:
                    carries_before_correct[i] = 1
                #
                # if ci_tmp + carries_after_correct[i + 1] + corrections[i] >= 10:
                elif (ci_tmp + carries_after_correct[i + 1])>= 10:
                    carries_after_correct[i] = 1

            tmp_decimals[i] = ci_tmp%16
            tmp_digits[i] = self.int_to_bin4(ci_tmp%16)
            # used for test
            result_dec[i] = (tmp_decimals[i] + corrections[i] + carries_after_correct[i+1]) % max_digit
            # result_dec[i] = (tmp_decimals[i] + corrections[i] ) % max_digit
        # test if correct results
        # if tmp digits + corrections + carries after corrections
        # are equal to final result,
        # it's ok

        for i in range(ln):
            if  result_dec[i] != int(c_decimals[i]):
                test_ok = False
                break
        else:
            test_ok = True

        return {
            "scheme": "bcd",
            "a_dec": a,
            "b_dec": b,
            "total_dec": a + b,
            "test_result_dec":result_dec,
            "test_ok":test_ok,
            "digits_a_bin": a_digits,
            "digits_b_bin": b_digits,
            "final_digits_bin": c_digits,
            "digits_a_dec": a_decimals,
            "digits_b_dec": b_decimals,
            "final_digits_dec": c_decimals,
            "carry_in": carries_before_correct[1:],
            "carry_out": carries_after_correct[1:],
            "sums_bin": tmp_digits,
            "sums_dec": tmp_decimals,
            "corrections": corrections,
        }
    def display_bcd_results(self, result):

        fields = [            "a_dec",
            "b_dec",
                              '------------------',
            "total_dec",
                'test_ok',
                  'carry_in',
                  'digits_a_dec',
                  'digits_b_dec',
                  '------------------',
                  'carry_out',
                  'sums_dec',
                  'corrections',
                  '------------------',
                  'final_digits_dec',
                  'test_result_dec',
                  "",
                  "",
                  '******* BINARY ***********',
                  'carry_in',
                  'digits_a_bin',
                  'digits_b_bin',
                  '------------------',
                  'carry_out',
                  'sums_bin',
                  'corrections'
                  '------------------',
                  'final_digits_bin',
                   ]

        ln_max = max([len(f) for f in fields])
        for f in fields:
            value = result.get(f,"")
            text = value
            if type(value) == list:
                text = "\t".join([str(v) for v in value])
            print(f.ljust(ln_max), text)
    def test_bcd(self,test_set):
        counter = 0
        wrong_case = []
        for a,b in test_set:
            result = q.bcd_addition_explain(a, b)
            if not result["test_ok"]:
                counter += 1
                wrong_case.append([a,b])
                # pprint(result)
                self.display_bcd_results(result)
        print(f"Error on {counter}/{len(test_set)} cases.")
        print("wrong_case = ", wrong_case)

    def x3_addition_explain(self, a, b):
        """
        Perform X3 addition digit by digit (right to left).
        a, b: two integers
        Returns a dict suitable for rendering in HTML/Latex.
        """
        max_digit = 16
        # detect the max length
        ln = max(len(str(a)), len(str(b)), len(str(a+b)))
        # add extra zeros to align numbers
        a_str = str(a).zfill(ln)
        b_str = str(b).zfill(ln)
        c_str = str(a + b).zfill(ln)
        a_digits = self.dec_to_excess3(a_str).split(" ")
        b_digits = self.dec_to_excess3(b_str).split(" ")
        c_digits = self.dec_to_excess3(c_str).split(" ")

        a_decimals = list(a_str)
        b_decimals = list(b_str)
        c_decimals = list(c_str)
        # get carries
        # to avoid out of range
        # added to first line
        carries = [0] * (ln + 1)
        # not used, only for compatibility
        carries_outs = [0] * (ln + 1)
        # added to the correciton step
        corrections = [-3] * ln
        tmp_decimals = [0] * ln
        tmp_digits = ["0011"] * ln
        result_dec = [0]*ln
        for i in range(ln - 1, -1, -1):
            ai = int(a_decimals[i]) +3
            bi = int(b_decimals[i]) +3
            ci = int(c_decimals[i]) +3
            # get carries
            ci_tmp = ai + bi + carries[i + 1]
            if ci_tmp >= max_digit:
                corrections[i] = 3
                carries[i] = 1
            else:
                corrections[i] = -3
                carries[i] = 0
            tmp_decimals[i] = ci_tmp%16
            tmp_digits[i] = self.int_to_bin4(ci_tmp%16)
            # used for test
            result_dec[i] = tmp_decimals[i] + corrections[i] - 3

        for i in range(ln):
            if  result_dec[i] != int(c_decimals[i]):
                test_ok = False
                break
        else:
            test_ok = True

        return {
            "scheme":"x3",
            "a_dec": a,
            "b_dec": b,
            "total_dec": a + b,
            "test_result_dec":result_dec,
            "test_ok":test_ok,
            "digits_a_bin": a_digits,
            "digits_b_bin": b_digits,
            "final_digits_bin": c_digits,
            "digits_a_dec": a_decimals,
            "digits_b_dec": b_decimals,
            "final_digits_dec": c_decimals,
            "carry_in": carries[1:],
            "carry_out": carries_outs[1:],
            "sums_bin": tmp_digits,
            "sums_dec": tmp_decimals,
            "corrections": corrections,
        }
def main(args):
    qs = questionGenerator()
    print(qs.numeral_system(12,2))
    print(qs.numeral_system())
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
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


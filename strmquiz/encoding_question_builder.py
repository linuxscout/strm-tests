#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz_builder.py
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
import logging
# --- Configure logging ---
logging.basicConfig(
    level=logging.DEBUG,  # change to INFO or WARNING in production
    format="%(levelname)s:%(name)s:%(message)s"
)
logger = logging.getLogger(__name__)

import random



from .codage import question_codage as question
from .codage import ieee754


from .question_builder import Question_Builder

class EncodingQuestionBuilder(Question_Builder):
    """Generate quiz questions for different domains."""

    def __init__(self, outformat="latex", config_file="", lang="ar-en", templates_dir="",):
        # 🔹 Inject dependencies (makes testing easier)
        super().__init__()
        # super().__init__(outformat=outformat, config_file=config_file, lang=lang, templates_dir=templates_dir,)

        self.qs = question.questionGenerator(latex=True)

        self.vf = ieee754.float_point()
        self.randomize = True
        self.CATEGORY = "encoding"

        # Predefined categories metadata
        self.categories_info = {
            self.CATEGORY: {
                "short": "Encoding & number systems",
                "long": "Covers numeral bases, complements, character encoding, floating point representation, and data measurement units."
            },
        }
        self.CATEGORY = "encoding"

        self.categories_info = {
            self.CATEGORY: {
                "short": "Encoding & number systems",
                "long": "Covers numeral bases, complements, character encoding, "
                        "floating point representation, and data measurement units."
            },
        }
        self.commands_info = {
            "float": {
                "category": self.CATEGORY,
                "short": "Floating-point representation",
                "long": "IEEE-754 floating-point conversion and analysis.",
                "example":"Represent 1.5 under the IEEE-754 standard.",
                "template": "encoding/float",
                #"handler": self.command_vf,
                "args": {
                    "float": {"type": "float", "default": 0, "label":"Float number"},
                },
            },
            "intervalle": {
                "category": self.CATEGORY,
                "short": "Integer intervals with complements",
                "long": "Binary integer ranges, signed numbers, Complement-1 and Complement-2.",
                "example": "What is the interval to represent with 4bits in signed value.",
                "template": "encoding/interval",
                #"handler": self.command_intervalle,
                "args": {
                    "nbits": {"type": "integer", "default": 8, "range": [1, 64], "label":"Bits number"},
                },
            },
            "complement": {
                "category": self.CATEGORY,
                "short": "Number complements",
                "long": "Exercises on complement to one and complement to two.",
                "example": "Represent the following number in signed value, 1's complement and 2's complement.",
                "template": "encoding/cp",
                #"handler": self.command_complement,
                "args": {
                    "number": {"type": "integer", "default": 0, "label":"Number (decimal)"},
                },
            },
            "base": {
                "category": self.CATEGORY,
                "short": "Numeral system conversion",
                "long": "Convert numbers between bases (binary, octal, decimal, hex).",
                "example": "Convert the following number (125)_8 = (.....)_2.",
                "template": "base",
                #"handler": self.command_base,
                "args": {
                    "number": {"type": "integer", "default": 0, "label":"Number (decimal)"},
                    "in_base": {"type": "integer", "default": 10, "label":"From base"},
                    "out_base": {"type": "integer", "default": 10, "label":"To base"},
                },
            },
            "arithm": {
                "category": self.CATEGORY,
                "short": "Arithmetic in different bases",
                "long": "Perform arithmetic in binary, octal, or hex systems.",
                "example": "Calculate 125 + 13 in base 8.",
                "template": "arithm",
                #"handler": self.command_arithm,
                "args": {
                    "number_a": {"type": "integer", "default": 0,  "label":"Number A (decimal)"},
                    "number_b": {"type": "integer", "default": 0 , "label":"Number B (decimal)"},
                    "operation": {
                        "type": "string",
                        "default": "+",
                        "choices": ["+", "-", "*", "/"],
                        "label": "Operation"
                    },
                    "base": {"type": "integer", "default": 10 , "label":"Base"},
                },
            },
            "mesure": {
                "category": self.CATEGORY,
                "short": "Unit conversions",
                "long": "Convert between info units (bits, bytes, KB, MB) or physical units (time, freq).",
                "example": "What's the time to download 4 GB file with a connection of 2Mbps",
                "template": "mesure",
                #"handler": self.command_mesure,
                "args": {},
            },
            "ascii": {
                "category": self.CATEGORY,
                "short": "ASCII character codes",
                "long": "Convert characters to/from ASCII in decimal, hex, binary.",
                "template": "encoding/charcode",
                "example": "Encode 'My text' into ASCII" ,
                #"handler": self.command_ascii,
                "args": {
                    "text": {"type": "string", "default": "", "label":"Text"},
                    "method": {"type": "string", "default": "both", "choices": ["both", "encode","decode"],  "label":"Method"},
                },
            },
            "ascii_text": {
                "category": self.CATEGORY,
                "short": "ASCII text encoding",
                "long": "Encode/decode short words using ASCII tables.",
                "example": "Encode 'My text' into ASCII",
                "template": "encoding/charcode",
                #"handler": self.command_ascii_text,
                "args": {
                    "text": {"type": "string", "default": "",  "label":"Text"},
                    "method": {"type": "string", "default": "both", "choices": ["both", "encode","decode"],  "label":"Method"},
                },
            },
            "unicode": {
                "category": self.CATEGORY,
                "short": "Unicode encoding",
                "long": "Convert characters to/from Unicode representations.",
                "example": "Encode 'My text' into Unicode",
                "template": "encoding/charcode",
                #"handler": self.command_unicode,
                "args": {
                    "text": {"type": "string", "default": "",  "label":"Text"},
                    "method": {"type": "string", "default": "both", "choices": ["both", "encode","decode"],  "label":"Method"},
                },
            },
            "bcdx3": {
                "category": self.CATEGORY,
                "short": "BCD ×3 encoding",
                "long": "Convert numbers into Binary Coded Decimal (BCD) with ×3 correction.",
                "example": "Encode 125  and 18 in BCD, then do addition in BCD.",
                "template": "encoding/bcdx3",
                #"handler": self.command_bcdx3,
                "args": {
                    "number_a": {"type": "integer", "default": 0,   "label":"Number A (decimal)"},
                    "number_b": {"type": "integer", "default": 0,   "label":"Number B (decimal)"},
                    "scheme": {"type": "string", "default": "both", "choices": ["both", "bcd","x3"],  "label":"Scheme"},
                },
            },
            "gray": {
                "category": self.CATEGORY,
                "short": "Gray code",
                "long": "Exercises on Gray code conversions and sequences.",
                "example": "Let x = (11011)gray, what's the following number.",
                "template": "encoding/gray",
                #"handler": self.command_gray,
                "args": {
                    "gray_number": {"type": "integer", "default": 0,  "label":"Gray number (decimal)"},
                    "gray_sequence": {"type": "integer", "default": 2, "label":"Gray sequence length"},
                },
            },
        }

        self.command_map = {
            "float": (self.command_vf, True),
            "intervalle": (self.command_intervalle, True),
            "complement": (self.command_complement, True),
            "base": (self.command_base, True),
            "arithm": (self.command_arithm, True),
            "mesure": (self.command_mesure, True),
            "ascii": (self.command_ascii, True),
            "unicode": (self.command_unicode, True),
            "bcdx3": (self.command_bcdx3, True),
            "gray": (self.command_gray, True),
            # encoding
            "ascii_text": (self.command_ascii, True),
        }
        self.templates_map = {
            "float": "encoding/float",
            "complement": "encoding/cp",
            "intervalle": "encoding/interval",
            "base": "base",
            "bcdx3": "encoding/bcdx3",
            "gray": "encoding/gray",
            "ascii": "encoding/charcode",
            "ascii_text": "encoding/charcode",
            "unicode": "encoding/charcode",
            "charcode": "encoding/charcode",
            "arithm": "arithm",
            "mesure": "mesure",  # NotImplementedError for now
        }

    def command_ascii_text(self, args={}):
        return self.question_ascii(text=args.get("text",""), method=args.get("method",""))


    def command_ascii(self, args={}):
        return self.question_ascii(text=args.get("text",""), method=args.get("method",""))

    def command_unicode(self, args={}):
        return self.question_unicode(text=args.get("text",""), method=args.get("method",""))

    def command_vf(self, args={}):
        return self.question_vf(number=args.get("float",0))

    def command_intervalle(self, args={}):
        return self.question_intervalle(decimal=args.get("nbits",8))


    def command_complement(self, args={}):
        return self.question_cp(decimal=args.get("number",0))

    def command_gray(self, args={}):
        return self.question_gray(number=args.get("gray_number",0),
                                   sequence_length=args.get("gray_sequence",2))

    def command_bcdx3(self, args={}):
        return self.question_bcd_x3(decimal_a= args.get("number_a",0),
                                    decimal_b= args.get("number_b",0),
                                    scheme = args.get("scheme",""),
                                    )


    def command_arithm(self, args={}):
        return self.question_arithm(number_a= args.get("number_a",0),
                                    number_b= args.get("number_b",0),
                                    operation = args.get("operation","+"),
                                    base = args.get("base",10),
                                    )

    def command_base(self, args={}):
        return self.question_base(decimal= args.get("number_a",0),
                                   in_base=args.get("in_base",10),
                                   out_base=args.get("out_base",10),
                                    )

    def command_mesure(self, args={}):
        return self.question_mesure()
    # --- Example Questions (refactored) ---

    def question_vf(self, number:float=0):
        """Floating point encoding question."""

        x  = self.vf.vf_question() if self.randomize else self.vf.vf_question(number)

        result = self.vf.ieee754_components(x)
        context = {
            "number": result.get("number"),
            "abs_value": result.get("abs_value"),
            "sign": result.get("sign"),
            "binary_repr": result.get("binary_repr"),
            "exponent": result.get("exponent"),
            "exponent_raw": result.get("exponent_raw"),
            "exponent_bits": result.get("exponent_bits"),
            "mantissa": result.get("mantissa"),
            "final_binary": result.get("final_binary"),
            "hex": result.get("hex"),
        }
        return  context
        # return self._render(SECTION_FLOAT, ieee_dict)


    def question_cp(self, decimal=0):
        """Complement coding question."""
        try:
           n, a, cp1, cp2 = self.qs.comp_one(8) if self.randomize else self.qs.comp_one(nbits=8, n=decimal)

        except Exception as e:
            logger.exception("Failed to generate CP question")
            context = {"error": str(e)}
            return context
            # return self._render(SECTION_CP, {"error": str(e)})
        context = {"number": n, "binary": a, "cp1": cp1, "cp2": cp2}
        return context
        # return self._render(SECTION_CP, {"number": n, "binary": a, "cp1": cp1, "cp2": cp2})



    def question_intervalle(self, decimal=0):
        """Interval coding question."""
        n = self.qs.intervalle() if self.randomize else self.qs.intervalle(n=decimal)
        context = {"number": n}
        return context
        # return self._render(SECTION_INTERVAL, context)

    def question_base2(self, decimal=0, in_base=10, out_base=10):
        """Base conversion question."""
        if self.randomize:
            res = self.qs.rand_numeral_system()
            number = res.get("number", 0)
            in_base = res.get("in_base", 10)
            out_base = res.get("out_base", 10)
            output = res.get("output", 0)
        else:
            number = decimal #self.qs.int2base(decimal, in_base)
            output = self.qs.int2base(decimal, out_base)

        # reproducible randomness via self.rng
        number_tmp = 0
        steps_from10, steps_to10, binary_mode = [], [], False
        if in_base == 10 and out_base != 10:
            steps_from10 = self.qs.make_steps_from10(number, out_base)
        elif in_base != 10 and out_base == 10:
            steps_to10 = self.qs.number_to_digits(number, in_base)
        elif in_base in (2, 8, 16) and out_base in (2, 8, 16):
            binary_mode = True
        elif in_base != 10 and out_base != 10:
            steps_to10 = self.qs.number_to_digits(number, in_base)
            number_tmp = self.qs.base2int(number, in_base)
            steps_from10 = self.qs.make_steps_from10(number_tmp, out_base)

        context = {
            "number": number,
            "number_tmp": number_tmp,
            "number_label": str(number),
            "in_base": in_base,
            "out_base": out_base,
            "output": output,
            "steps_from10": steps_from10,
            "steps_to10": steps_to10,
            "binary_mode": binary_mode,
        }
        return context
        # return self._render(SECTION_BASE, context)

    def question_base(self, decimal=0, in_base=10, out_base=10):
        """Base conversion question."""
        if self.randomize:
            res = self.qs.rand_numeral_system()
            number = res.get("number", 0)
            in_base = res.get("in_base", 10)
            out_base = res.get("out_base", 10)
            output = res.get("output", 0)
        else:
            number = decimal
            output = self.qs.int2base(decimal, out_base)

        number_tmp, steps_from10, steps_to10, binary_mode = self._compute_conversion_steps(
            number, in_base, out_base
        )

        return {
            "number": number,
            "number_tmp": number_tmp,
            "number_label": str(number),
            "in_base": in_base,
            "out_base": out_base,
            "output": output,
            "steps_from10": steps_from10,
            "steps_to10": steps_to10,
            "binary_mode": binary_mode,
        }

    def _compute_conversion_steps(self, number, in_base, out_base):
        """
        Compute conversion steps depending on input/output bases.
        Returns: (number_tmp, steps_from10, steps_to10, binary_mode)
        """
        number_tmp, steps_from10, steps_to10, binary_mode = 0, [], [], False

        if in_base == 10 and out_base != 10:
            # direct from base 10 → other
            steps_from10 = self.qs.make_steps_from10(number, out_base)

        elif in_base != 10 and out_base == 10:
            # from another base → base 10
            steps_to10 = self.qs.number_to_digits(number, in_base)

        elif in_base in (2, 8, 16) and out_base in (2, 8, 16):
            # shortcut: binary/octal/hex conversions
            binary_mode = True

        elif in_base != 10 and out_base != 10:
            # general case: base X → base 10 → base Y
            steps_to10 = self.qs.number_to_digits(number, in_base)
            number_tmp = self.qs.base2int(number, in_base)
            steps_from10 = self.qs.make_steps_from10(number_tmp, out_base)

        return number_tmp, steps_from10, steps_to10, binary_mode

    def question_bcd_x3(self, decimal_a=0, decimal_b=0, scheme="", method="",min_val=10, max_val=10**5):

        if self.randomize:
            number_a = number  = random.randint(min_val, max_val)
            number_b  = random.randint(min_val, max_val)
        else:
            number_a = number = decimal_a
            number_b  = decimal_b

        bcd = self.qs.dec_to_bcd(number)
        bcd_digits = bcd.split(" ")
        x3 = self.qs.dec_to_excess3(number)
        x3_digits = x3.split(" ")

        data_bcd = self.qs.bcd_addition_explain(number_a, number_b)
        data_x3 = self.qs.x3_addition_explain(number_a, number_b)
        context = {
            "number": str(number) ,
            "bcd": bcd,
            "bcd_digits": bcd_digits,
            "x3": x3,
            "x3_digits": x3_digits,
            "scheme":scheme,
            "method":method,
            "data_bcd":data_bcd,
            "data_x3":data_x3,
        }
        return context
        # return self._render(SECTION_BCDX3, context)

    def question_gray(self, number=0, sequence_length=2):

        if self.randomize:
            x  = random.randint(15, 256) if self.randomize else number
            seq_len  = random.randint(2, 10)
        else:
            x = number
            seq_len = sequence_length
        x_bin = self.qs.int2base(x, 2)
        x_gray = self.qs.binary_to_gray(x_bin)
        x_gray_sequence = self.qs.gray_sequence_from_binary(x_bin,seq_len)
        steps = self.qs.gray_explain(x_bin, x_gray)
        context = {
            "number_dec": str(x) ,
            "number_bin": str(x_bin),
            "number_gray": str(x_gray),
            "gray_sequence": x_gray_sequence,
            "sequence_length": seq_len,
            "method": "encode",
            "steps_gray2bin": steps.get("steps_gray2bin",[]),
            "steps_bin2gray": steps.get("steps_bin2gray",[]),
        }
        return context
        # return self._render(SECTION_GRAY, context)



    def question_ascii(self,method="both", text=""):
        """ encode/ decode in ASCII """
        return self.question_charcode(text=text,scheme="ascii", method=method)

    def question_unicode(self,method="both", text=""):
        """ encode/ decode in Unicode """
        return self.question_charcode(text=text,scheme="unicode", method=method)

    def question_charcode(self,text="",scheme="ascii", method="both"):
        """ encode/ decode in ASCII and unicode
        """
        if self.randomize:
            text  = self.qs.rand_text(code=scheme)
        charcodes = self.qs.encode(text)
        if method not in ("encode", "decode", "both"):
            method = "both"
        context = {
            "charlist": list(text),
            "method": method, # encode decode
            "scheme":scheme,
            "charcodes":charcodes,
        }
        return context
        # return self._render(SECTION_CHARCODE, context)

    def question_arithm(self,number_a=0, number_b=0,operation="+", base=10):
        """
        question about arithmetics (addition and substraction)
        """
        if self.randomize:
            result = self.qs.rand_arithm()
        else:
            result = self.qs.arithm(number_a=number_a, number_b=number_b, base=base, operation=operation)
        context = {
            "question": result.get("question"),
            "reponse": result.get("reponse"),
            "number_a": result.get("number_a"),
            "number_b": result.get("number_b"),
            "number_c": result.get("number_c"),
            "operation": result.get("operation"),
            "base": result.get("base"),
        }
        return context
        # return self._render(SECTION_ARITHM, context)

    def question_mesure(self):
        # Multipliers to convert FROM base to the display unit.
        # Base units: size=MB, speed=MB/s, time=seconds.
        size_units = [("KB", 1024.0), ("MB", 1.0), ("GB", 1 / 1024.0)]
        speed_units = [("KB/s", 1024.0), ("MB/s", 1.0), ("GB/s", 1 / 1024.0), ("Mbps", 8.0)]
        time_units = [("seconds", 1.0), ("minutes", 60.0), ("hours", 3600.0)]

        # Pick random base values
        size_MB = random.choice([100, 250, 500, 1024, 2048, 4096])
        speed_MBps = random.choice([2, 5, 10, 20, 50, 100])
        time_sec = size_MB / speed_MBps

        # Pick display units
        size_unit, size_mult = random.choice(size_units)
        speed_unit, speed_mult = random.choice(speed_units)
        time_unit, time_div = random.choice(time_units)  # divide by seconds-per-unit

        # Convert for display
        display_size = size_MB * size_mult
        display_speed = speed_MBps * speed_mult
        display_time = time_sec / time_div

        # Decide question type
        ask = random.choice(["time", "size", "speed"])
        solution_steps = []
        a = ""

        if ask == "time":
            q = (f"A file of size {display_size:.2f} {size_unit} is downloaded with a speed of "
                 f"{display_speed:.2f} {speed_unit}. How long will the download take (in {time_unit})?")
            solution_steps = [
                {"step": 1, "operation": "Convert size to MB",
                 "expression": f"{display_size:.2f} {size_unit} = {size_MB:.2f} MB"},
                {"step": 2, "operation": "Convert speed to MB/s",
                 "expression": f"{display_speed:.2f} {speed_unit} = {speed_MBps:.2f} MB/s"},
                {"step": 3, "operation": "Time = Size / Speed",
                 "expression": f"{size_MB:.2f} ÷ {speed_MBps:.2f} = {time_sec:.2f} seconds"},
                {"step": 4, "operation": f"Convert seconds → {time_unit}",
                 "expression": f"{time_sec:.2f} ÷ {time_div:g} = {display_time:.2f} {time_unit}"}
            ]
            a = f"{display_time:.2f} {time_unit}"

        elif ask == "size":
            given_time = random.choice([60, 120, 300, 600, 1800])  # seconds
            display_given_time = given_time / time_div
            q = (f"A file was downloaded in {display_given_time:.2f} {time_unit} with a speed of "
                 f"{display_speed:.2f} {speed_unit}. What was the file size in {size_unit}?")
            size_MB_calc = given_time * speed_MBps
            solution_steps = [
                {"step": 1, "operation": "Convert time to seconds",
                 "expression": f"{display_given_time:.2f} {time_unit} = {given_time} seconds"},
                {"step": 2, "operation": "Convert speed to MB/s",
                 "expression": f"{display_speed:.2f} {speed_unit} = {speed_MBps:.2f} MB/s"},
                {"step": 3, "operation": "Size = Speed × Time",
                 "expression": f"{speed_MBps:.2f} × {given_time} = {size_MB_calc:.2f} MB"},
                {"step": 4, "operation": f"Convert MB → {size_unit}",
                 "expression": f"{size_MB_calc:.2f} × {size_mult:g} = {size_MB_calc * size_mult:.2f} {size_unit}"}
            ]
            a = f"{size_MB_calc * size_mult:.2f} {size_unit}"

        else:  # ask == "speed"
            given_time = random.choice([60, 120, 300, 600, 1800])  # seconds
            display_given_time = given_time / time_div
            q = (f"A file of size {display_size:.2f} {size_unit} was downloaded in "
                 f"{display_given_time:.2f} {time_unit}. What was the average speed in {speed_unit}?")
            speed_calc_MBps = size_MB / given_time
            solution_steps = [
                {"step": 1, "operation": "Convert size to MB",
                 "expression": f"{display_size:.2f} {size_unit} = {size_MB:.2f} MB"},
                {"step": 2, "operation": "Convert time to seconds",
                 "expression": f"{display_given_time:.2f} {time_unit} = {given_time} seconds"},
                {"step": 3, "operation": "Speed = Size / Time",
                 "expression": f"{size_MB:.2f} ÷ {given_time} = {speed_calc_MBps:.2f} MB/s"},
                {"step": 4, "operation": f"Convert MB/s → {speed_unit}",
                 "expression": f"{speed_calc_MBps:.2f} × {speed_mult:g} = {speed_calc_MBps * speed_mult:.2f} {speed_unit}"}
            ]
            a = f"{speed_calc_MBps * speed_mult:.2f} {speed_unit}"

        context = {
            "ask": ask,
            "question": q,
            "answer": a,
            "solution": solution_steps,
            "given": {
                "size": {"value": display_size, "unit": size_unit, "base_MB": size_MB},
                "speed": {"value": display_speed, "unit": speed_unit, "base_MBps": speed_MBps},
                "time": {"value": display_time, "unit": time_unit, "base_seconds": time_sec},
            }
        }
        return context

        # raise NotImplementedError("Mesure questions are not yet supported")


if __name__ == '__main__':

    qb = EncodingQuestionBuilder()

    print("\n--- Test: Floating Point Question ---")
    print(qb.question_vf())

    print("\n--- Test: Complement Coding Question ---")
    print(qb.question_cp())

    print("\n--- Test: Base Conversion Question ---")
    print(qb.question_base())

    print("\n--- Test: Gray Code Question ---")
    print(qb.question_gray())

    print("\n--- Test: ASCII Question ---")
    print(qb.question_ascii())



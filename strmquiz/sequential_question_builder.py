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

from .sequentiel import chronograms
from .sequentiel import seqconst
from .sequentiel import registersimulator
from .sequentiel import countersimulator




from .bool import boolquiz



from .question_builder import Question_Builder

class SequentialQuestionBuilder(Question_Builder):
    """Generate quiz questions for different domains."""

    def __init__(self, outformat="latex", config_file="", lang="ar-en", templates_dir=""):
        # 🔹 Inject dependencies (makes testing easier)
        super().__init__()
        self.bq = boolquiz.bool_quiz()
        self.bq.set_format('')
        self.CATEGORY = "sequential logic"

        # Predefined categories metadata
        self.categories_info = {
            self.CATEGORY: {
                "short": "Sequential circuits",
                "long": "Includes flip-flops, registers, counters, and timing diagrams for analyzing sequential behavior."
            }
        }
        self.commands_info = {
            "chronogram": {
                "category": self.CATEGORY,
                "short": "Sequential logic timing diagrams",
                "long": "Interpret and draw chronograms (timing diagrams) for flip-flops (RS, D, JK).",
                "example":"LEt have the following setup, complete the following timing diagram.",
                "template": "sequential/timing",
                #"handler": self.command_chronogram,
                "args": {
                    "varlist": {"type": "dict", "default": {}, "label": "Variables",},
                    "flip_type": {
                        "type": "string",
                        "default": "D",
                        "choices": ["D", "T", "JK", "RS", "RST"],
                        "label":"Flip flop type",
                    },
                    "length": {"type": "integer", "default": 10, "range": [1, 100]},
                    "synch_type": {
                        "type": "string",
                        "default": "rising",
                        "choices": ["rising", "falling"],
                        "label": "Synchronization type (edge)",
                    },
                    "output": {"type": "list", "default": ["Q"],"label": "Length of timing diagram",},
                },
            },
            "flip": {
                "category": self.CATEGORY,
                "short": "Flip-flop operation",
                "long": "Analyze the behavior of flip-flops (RS, D, JK, T) given inputs and clock signals.",
                "example": "LEt have the following Flip flip, give the truth table, then complete the following timing diagram.",
                "template": "sequential/flip",
                #"handler": self.command_flip,
                "args": {
                    "varlist": {"type": "dict", "default": {}, "label": "Variables",},
                    "flip_type": {
                        "type": "string",
                        "default": "D",
                        "choices": ["D", "T", "JK", "RS", "RST"],
                        "label": "Flip flop type",
                    },
                    "length": {"type": "integer", "default": 10, "range": [1, 100], "label": "Length of timing diagram",},
                    "synch_type": {
                        "type": "string",
                        "default": "rising",
                        "choices": ["rising", "falling"],
                        "label": "Synchronization type (edge)",
                    },
                    "output": {"type": "list", "default": ["Q"],"label": "Length of timing diagram",},
                },
            },
            "counter": {
                "category": self.CATEGORY,
                "short": "Counter design and behavior",
                "long": "Analyze synchronous and asynchronous up/down counters.",
                "example": "LEt have the following Setup, give the flip flop truth table, then complete the following timing diagram.",
                "template": "sequential/counter",
                #"handler": self.command_counter,
                "args": {
                    "varlist": {"type": "dict", "default": {}, "label": "Variables",},
                    "length": {"type": "integer", "default": 10, "range": [1, 100], "label": "Length of timing diagram",},
                    "synch_type": {
                        "type": "string",
                        "default": "rising",
                        "choices": ["rising", "falling"],
                        "label": "Synchronization type (edge)",
                    },
                    "output": {"type": "list", "default": ["Q"],"label": "Length of timing diagram",},
                    "counter_type": {
                        "type": "string",
                        "default": "up",
                        "choices": ["up", "down"],
                        "label":"Counter type",
                    },
                    "counter_flips": {"type": "list", "default": ["JK", "JK"], "label": "Counter flip flop type list",},
                    "counter_nbits": {"type": "integer", "default": 2, "range": [1, 16], "label":"Counter bits numbze (size)"},
                    "counter_random": {"type": "boolean", "default": False, "label":"Random counter"},
                },
            },
            "register": {
                "category": self.CATEGORY,
                "short": "Register analysis",
                "long": "Study shift registers and parallel registers with data movement and control operations.",
                "example": "LEt have the following Setup, give the flip flop truth table, then complete the following timing diagram.",
                "template": "sequential/register",
                #"handler": self.command_register,
                "args": {
                    "varlist": {"type": "dict", "default": {}, "label": "Variables",},
                    "length": {"type": "integer", "default": 10, "range": [1, 100], "label": "Length of timing diagram",},
                    "synch_type": {
                        "type": "string",
                        "default": "rising",
                        "choices": ["rising", "falling"],
                        "label": "Synchronization type (edge)",
                    },
                    "output": {"type": "list", "default": ["Q"],"label": "Length of timing diagram",},
                    "register_type": {
                        "type": "string",
                        "default": "shift-right",
                        "choices": ["shift-right", "shift-left", "parallel"],
                        "label": "Register type",
                    },
                    "register_flips": {"type": "list", "default": ["D", "D"],  "label": "Register flip flop type list",},
                    "register_nbits": {"type": "integer", "default": 2, "range": [1, 16], "label":"Register bits number"},
                    "register_random": {"type": "boolean", "default": False, "label":"Random register"},
                },
            },
            "seq_misc": {
                "category": self.CATEGORY,
                "short": "Miscellaneous sequential circuits",
                "long": "State machines, pulse generators, and hybrid sequential systems.",
                "example": "LEt have the following Setup, give the flip flop truth table, then complete the following timing diagram.",
                "template": "sequential/misc",
                #"handler": self.command_seq_misc,
                "args": {
                    "varlist": {"type": "dict", "default": {}, "label": "Variables",},
                    "flip_type": {
                        "type": "string",
                        "default": "D",
                        "choices": ["D", "T", "JK", "RS", "RST"],
                        "label": "Flip flop type",
                    },
                    "length": {"type": "integer", "default": 10, "range": [1, 100], "label": "Length of timing diagram",},
                    "synch_type": {
                        "type": "string",
                        "default": "rising",
                        "choices": ["rising", "falling"],
                        "label": "Synchronization type (edge)",
                    },
                    "output": {"type": "list", "default": ["Q"],"label": "Length of timing diagram",},
                },
            },
        }

        self.command_map = {
            "chronogram": (self.command_chronogram, True),
            "flip": (self.command_flip, True),
            "counter": (self.command_counter, True),
            "register": (self.command_register, True),
            "seq_misc": (self.command_seq_misc, True),
        }
        self.templates_map = {
            "chronogram": "sequential/timing",
            "flip": "sequential/flip",
            "register": "sequential/register",
            "counter": "sequential/counter",
            "seq_misc": "sequential/misc",
        }
    # sequential
    def command_chronogram(self, args={}):
        # print("quiz_builder:debug:arguments",args)
        return self.question_chronogram(
            varlist=args.get("varlist", {}),
            flip_type=args.get("flip_type", "D"),
            length=args.get("length", 10),
            synch_type=args.get("synch_type", "rising"),
            output_vars=args.get("output",  ["Q"])
        )

    def command_flip(self, args={}):
        # print("quiz_builder:debug:arguments",args)
        return self.question_flip(
            varlist=args.get("varlist", {}),
            flip_type=args.get("flip_type", "D"),
            length=args.get("length", 10),
            synch_type=args.get("synch_type", "rising"),
            output_vars=args.get("output", ["Q"])
        )

    def command_counter(self, args={}):
        # print("quiz_builder:debug:arguments",args)
        return self.question_counter(
            varlist=args.get("varlist", {}),
            length=args.get("length", 10),
            synch_type=args.get("synch_type", "rising"),
            output_vars=args.get("output", ["Q"]),
            counter_type=args.get("counter_type", "up"),
            flip_types=args.get("counter_flips", []),
            nbits=args.get("counter_nbits", 2),
            counter_random=args.get("counter_random", False),
        )

    def command_register(self, args={}):
        # print("quiz_builder:debug:arguments",args)
        return self.question_register(
            varlist=args.get("varlist", {}),
            # flip_type=args.get("flip_type","D"),
            length=args.get("length", 10),
            synch_type=args.get("synch_type", "rising"),
            output_vars=args.get("output",  ["Q"]),
            register_type=args.get("register_type", "shift-right"),
            flip_types=args.get("register_flips", []),
            nbits=args.get("register_nbits", 2),
            register_random=args.get("register_random", False),
        )

    def command_seq_misc(self, args={}):
        # print("quiz_builder:debug:arguments",args)
        return self.question_seq_misc(
            varlist=args.get("varlist", {}),
            flip_type=args.get("flip_type", "D"),
            length=args.get("length", 10),
            synch_type=args.get("synch_type", "rising"),
            output_vars=args.get("output",  ["Q",])
        )
    def _preprare_chrnonogram(self,  input_vars=["V",], start_signals={"D": 1,"Q":0}, flip_type="D", length=20, synch_type="rising", output_vars=["Q", ]):

        # start_signals = start_signals
        # chrono = tex_chronograms.Tex_Chronograms();
        chrono = chronograms.Chronograms();
        init_signals = {}
        for key in start_signals:
            if key in output_vars:
                # add an empty signal
                init_signals[key] = [start_signals[key], ]
            else:
                signal_dict = chrono.question({key: start_signals[key]}, length=length)
                init_signals[key] = signal_dict[key]
        # input_vars = [k for k in varlist if k not in output_vars]
        # set synchronization type
        chrono.set_synch_type(synch_type)

        # generate question
        # 1- clock
        # 2- signals without solution
        clock = chrono.clock_signal(length=length, period=1)
        # tex_data_question = chrono.draw(init_signals, clock)

        # generate soltution
        # get solution for signal
        # 2 generate chrono for answer
        # if we want to generate multiple cases using "dual" or "all"
        if synch_type == "all" or synch_type == "dual":
            # set synchronization type
            chrono.set_synch_type("rising")
        # print(__file__,"before_resolve", flip_type, init_signals)
        out_signal = chrono.resolve(flip_type=flip_type, signals=init_signals.copy(), period=2, inputs=input_vars)
        # print(__file__,"after_resolve", flip_type, out_signal)

        # output signal
        tmp_signals = init_signals.copy()
        tmp_signals[output_vars[0]] = out_signal
        # add inverse signal
        tmp_signals[output_vars[0] + "'"] = [-s for s in out_signal]
        # add more signals for multi cases
        if synch_type == "all" or synch_type == "dual":
            # set synchronization type
            chrono.set_synch_type("falling")

            out_signal = chrono.resolve(flip_type=flip_type, signals=init_signals.copy(), period=2,inputs=input_vars)
            # output signal
            tmp_signals[output_vars[0] + ".falling"] = out_signal

        if synch_type == "all":
            # set synchronization type
            chrono.set_synch_type("asynch")
            out_signal = chrono.resolve(flip_type=flip_type, signals=init_signals.copy(), period=2,inputs=input_vars)
            tmp_signals[output_vars[0] + ".asyn"] = out_signal

        if synch_type == "all" or synch_type == "dual":
            # set synchronization type
            chrono.set_synch_type("dual")


        input_signals = {k:v for k,v in tmp_signals.items() if k in input_vars}

        out_signals_initial = {k:v for k,v in init_signals.items() if k in output_vars}

        out_signals_final = {k:v for k,v in tmp_signals.items() if k in output_vars}

        # tex_data_answer = chrono.draw(tmp_signals, clock)

        data= {
        "varlist":start_signals,
        "flip_type":flip_type,
        "length":length,
        "synch_type":synch_type,
        "output_vars":output_vars,
        "input_vars": input_vars,
        "input_signals": input_signals,
        "output_signals":{"initial": out_signals_initial,
                    "final": out_signals_final,
                      },
        "clock":clock,
        "question_signals":init_signals,
        "answer_signals":tmp_signals,
        "tex_data_answer":"",#tex_data_answer,
        }
        return data

    def _preprare_chrnonogram_register(self,  input_vars=["V",], start_signals={"D": 1,"Q":0}, flip_list=["D",], nbits =4,
                                    length=20, synch_type="rising", output_vars=["Q", ],register_type="shift-right"):

        # start_signals = start_signals*
        flip_types = [x.get("type","") for x in flip_list]
        reg_sim = registersimulator.RegisterSimulator(inputs=input_vars, outputs=output_vars,
                                                      # flip_types=flip_types, register_type="shift-right")
                                                      flip_types=flip_types, register_type=register_type)

        chrono = chronograms.Chronograms();
        # chrono = tex_chronograms.Tex_Chronograms();
        flip_type = flip_list[0].get("type","")
        init_signals = {}
        for key in start_signals:
            if key in output_vars:
                # add an empty signal
                init_signals[key] = [start_signals[key], ]
            else:
                signal_dict = chrono.question({key: start_signals[key]}, length=length)
                init_signals[key] = signal_dict[key]
        # input_vars = [k for k in varlist if k not in output_vars]
        # set synchronization type
        chrono.set_synch_type(synch_type)

        # generate question
        # 1- clock
        clock = chrono.clock_signal(length=length, period=1)


        tmp_signals = reg_sim.resolve_register(init_signals.copy(), signal_length=length)


        input_signals = {k:v for k,v in tmp_signals.items() if k in input_vars}

        out_signals_initial = {k:v for k,v in init_signals.items() if k in output_vars}

        out_signals_final = {k:v for k,v in tmp_signals.items() if k in output_vars}

        tex_data_answer = "Empty"#chrono.draw(tmp_signals, clock)

        data= {
        "varlist":start_signals,
        "flip_type":flip_type,
        "length":length,
        "synch_type":synch_type,
        "output_vars":output_vars,
        "input_vars": input_vars,
        "input_signals": input_signals,
        "output_signals":{"initial": out_signals_initial,
                    "final": out_signals_final,
                      },
        "clock":clock,
        "question_signals":init_signals,
        "answer_signals":tmp_signals,
        "tex_data_answer":tex_data_answer,
        }
        return data

    def _preprare_chrnonogram_counter(self,  input_vars=["V",], start_signals={"D": 1,"Q":0}, flip_list=["D",], nbits =4,
                                    length=20, synch_type="rising", output_vars=["Q", ],counter_type="up"):

        # start_signals = start_signals*
        flip_types = [x.get("type","") for x in flip_list]
        reg_sim = countersimulator.CounterSimulator(inputs=input_vars, outputs=output_vars,
                                                      flip_types=flip_types, counter_type=counter_type)

        chrono = chronograms.Chronograms()
        # chrono = tex_chronograms.Tex_Chronograms()
        flip_type = flip_list[0].get("type","")
        init_signals = {}
        for key in start_signals:
            if key in output_vars:
                # add an empty signal
                init_signals[key] = [start_signals[key], ]
            else:
                if key == "Vcc":
                    init_signals[key] = [length*2]
                elif key == "Gnd":
                    init_signals[key] = [-length*2]
                else:
                    signal_dict = chrono.question({key: start_signals[key]}, length=length)
                    init_signals[key] = signal_dict[key]
        # set synchronization type
        chrono.set_synch_type(synch_type)

        # generate question
        # 1- clock
        # 2- signals without solution
        clock = chrono.clock_signal(length=length, period=1)

        # generate solution
        tmp_signals = reg_sim.resolve_counter(init_signals.copy(), signal_length=length)

        # the counter hasn't inputs
        input_signals = {}
        out_signals_initial = {k:v for k,v in init_signals.items() if k in output_vars}

        out_signals_final = {k:v for k,v in tmp_signals.items() if k in output_vars}
        # tex_data_answer = chrono.draw(tmp_signals, clock)

        data= {
        "varlist":start_signals,
        "flip_type":flip_type,
        "length":length,
        "synch_type":synch_type,
        "output_vars":output_vars,
        "input_vars": input_vars,
        "input_signals": input_signals,
        "output_signals":{"initial": out_signals_initial,
                    "final": out_signals_final,
                      },
        "clock":clock,
        "question_signals":out_signals_initial,
        "answer_signals":out_signals_final,
        "tex_data_answer":"Empty",
        }
        return data

    def question_chronogram(self, varlist={}, flip_type="D", length=20, synch_type="rising", output_vars=["Q", ]):

        """
        Generate Chronogram question
        """
        context= {}
        #TODO: fix in config file
        input_vars = [k for k in list(varlist.keys()) if not k.upper().startswith("Q")]

        data = self._preprare_chrnonogram(input_vars=input_vars, start_signals=varlist, flip_type=flip_type, length=length, synch_type=synch_type, output_vars=output_vars)

        context= {"data": data,
          }
        return context



    def _get_rand_flip(self,):
        seqs = seqconst.FLIPS_RANDOM
        name = random.choice(list(seqs.keys()))
        inputs = list(name)
        init_signals = {e: 0 for e in inputs}
        init_signals.update({'Q': -1, "Q'": 1, })
        tt = seqs[name]
        varlist = inputs + ["Q", "Q'"]

        return {'init_signals': init_signals,
                'inputs': inputs,
                'outputs': ['Q', "Q'"],
                'truth_table': tt,
                'type': name,
                'vars': varlist}
    def question_flip(self, varlist={}, flip_type="D", length=20, synch_type="rising", output_vars=["Q", ]):

        """
        Generate Chronogram question for a given flip
        """
        # if not standard flip type, generate a random one
        flip_data = seqconst.FLIPS_DATA.get(flip_type,{})
        if not flip_data:
            flip_data = self._get_rand_flip()
        flip_type_new = flip_data.get("type",flip_type)
        # set defaulyt var list for given flip
        # else take the given one
        start_signals = flip_data.get("init_signals",{})
        # a standard output for flip questions
        output_vars_new = ["Q", "Q'"]

        data = self._preprare_chrnonogram(input_vars=flip_data["inputs"], start_signals=start_signals, flip_type=flip_type_new, length=length, synch_type=synch_type, output_vars=output_vars_new)

        context= {"data": data,
                  "flip_data":flip_data,
          }

        return context


    def question_register(self, varlist={}, flip_types=["D",], length=20, synch_type="rising", output_vars=["Q", ], register_type="shift-right",
                          nbits:int=2,
                          register_random:bool=True):

        """
        Generate Chronogram question for a given register
        """
        if register_random:
            nbits = random.randint(3,6)
            reg_flip_type_list = random.choices(["D","JK"], k=nbits)
            # get data from flip standard
            reg_flip_list = [seqconst.FLIPS_DATA.get(ft,{}) for ft in reg_flip_type_list ]
        else:
            reg_flip_type_list = flip_types
            # in case that configuration fliptypes is missing
            if len(reg_flip_type_list) < nbits:
               reg_flip_type_list = reg_flip_type_list + ["D"] * (nbits-len(flip_types))
            # get data from flip standard
            reg_flip_list = [seqconst.FLIPS_DATA.get(ft,{}) for ft in reg_flip_type_list ]

        inputs = ["E",]
        outputs = [f"Q{i}" for i in range(nbits)]
        vars_ = inputs + outputs
        init_signals= {e:0 for e in vars_}
        # register_type = "shift-left"
        if register_type.endswith("left"):
            shift = "left"
        else:
            shift = "right"
        register_data ={  'inputs': inputs,
              'outputs': outputs,
               'init_signals':  init_signals,
              'flip_list': reg_flip_list,
              'flip_type_list': reg_flip_type_list,
                "type":"",
               'nbits':nbits,
                "shift":shift,
              'vars':vars_ }

        data = self._preprare_chrnonogram_register(input_vars=inputs,
                                          start_signals=init_signals,
                                          flip_list = reg_flip_list,
                                          length=length,
                                          nbits=nbits,
                                          synch_type=synch_type,
                                          output_vars=outputs,
                                          register_type=register_type)


        context= {"data": data,
                  "register_data": register_data,
          }
        return context



    def question_counter(self, varlist={}, flip_types=["D",], length=20, synch_type="rising", output_vars=["Q", ], counter_type="up",
                          nbits:int=2,
                          counter_random:bool=True):

        """
        Generate Chronogram question for a given register
        """
        if counter_random:
            nbits = random.randint(3,6)
            reg_flip_type_list = random.choices(["D","JK"], k=nbits)
            # get data from flip standard
            reg_flip_list = [seqconst.FLIPS_DATA.get(ft,{}) for ft in reg_flip_type_list ]
        else:
            reg_flip_type_list = flip_types
            # in case that configuration fliptypes is missing
            if len(reg_flip_type_list) < nbits:
               # reg_flip_type_list = reg_flip_type_list + ["D"] * (nbits-len(flip_types))
               reg_flip_type_list = reg_flip_type_list + ["JK"] * (nbits-len(flip_types))
            # get data from flip standard
            reg_flip_list = [seqconst.FLIPS_DATA.get(ft,{}) for ft in reg_flip_type_list ]

        inputs = ["Vcc","Gnd"]
        outputs = [f"Q{i}" for i in range(nbits)]
        vars_ = inputs + outputs
        if counter_type.lower() == "up":
            init_signals= {e:0 for e in vars_}
        else:
            init_signals= {e:1 for e in vars_}
        # special signals
        # init_signals['Vcc'] = [length*2]
        # init_signals['Gnd'] = [-length*2]
        # register_type = "shift-left"
        counter_data ={  'inputs': inputs,
              'outputs': outputs,
               'init_signals':  init_signals,
              'flip_list': reg_flip_list,
              'flip_type_list': reg_flip_type_list,
                "type":counter_type,
               'nbits':nbits,
              'vars':vars_ }

        data = self._preprare_chrnonogram_counter(input_vars=inputs,
                                          start_signals=init_signals,
                                          flip_list = reg_flip_list,
                                          length=length,
                                          nbits=nbits,
                                          synch_type=synch_type,
                                          output_vars=outputs,
                                          counter_type=counter_type)


        context= {"data": data,
                  "counter_data": counter_data,
          }
        return context




    def question_seq_misc(self, varlist={}, flip_type="D", length=20, synch_type="rising", output_vars=["Q", ]):

        """
        Generate Chronogram question for a given sequential miscellaneous circuit
        """
        context= {}

        data = self._preprare_chrnonogram(flip_type=flip_type, length=length, synch_type=synch_type, output_vars=output_vars)

        context= {"data": data,
          }
        return context



def main(args):
    pass

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

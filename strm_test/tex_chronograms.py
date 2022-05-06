#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
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
import wavedrom
import json
import random
from . import chronograms
TEMPLATE_RISING = """
\\begin{tikztimingtable}
%[timing/slope=.0, timing/draw grid]
[timing/slope=.0,  timing/wscale=1]
% horloge signal
{SIGNALS}
\\extracode
\\begin{scope}[gray,semitransparent,densely dotted,thin]
\\horlines{}
\\vertlines{0}
\\end{scope}
\\begin{scope}[red,semitransparent,densely dotted,thin]
\\vertlines{1,3,...,\\twidth}
\\end{scope}
\\end{tikztimingtable}
"""
TEMPLATE_FALLING = """
\\begin{tikztimingtable}
%[timing/slope=.0, timing/draw grid]
[timing/slope=.0,  timing/wscale=1]
% horloge signal
{SIGNALS}
\\extracode
\\begin{scope}[gray,semitransparent,densely dotted,thin]
\\horlines{}
\\vertlines{0}
\\end{scope}
\\begin{scope}[red,semitransparent,densely dotted,thin]
\\vertlines{2,4,...,\\twidth}
\\end{scope}
\\end{tikztimingtable}
"""
class Tex_Chronograms(chronograms.Chronograms):
    """
    A class to generate questions and answers on chronograms
    """
    def __init__(self,):
        # H scale for scale draw
        self.hscale = 2
        self.start_high = "H"
        self.extend_high = "H"
        self.start_low = "L"
        self.extend_low = "L" 
        self.synch_type = "rising"
    def draw(self, signals={}, clock={}):
        """
        Draw a chronogram with data as signals, use a synchronisation moment,
        @param signals: a dict of list of intergers, positive represent high, negatives represent low
        @type signals: dict of list of integers
        @return: signal data 
        @rtype:  list of signal dict
        """
        data = []
        if clock:
            data.append(clock)
        for key in signals:
            # tread signal
            # convert a list of value into string
            wave = self.stringfy(signals[key])
            sig = { "name": key,   "wave": wave }
            data.append(sig)

        # draw latex
        signals_data = data
        lines = []
        for signal in signals_data:
            name = signal.get('name', "X")
            wave = signal.get('wave', "L")
            lines.append("$%s$ & %s\\\\"%(name, wave))
        if(self.synch_type=="falling"):
            output = TEMPLATE_FALLING.replace("{SIGNALS}", "\n".join(lines))
        else:
            output = TEMPLATE_RISING.replace("{SIGNALS}", "\n".join(lines))        
        return output;
    
    def stringfy(self, signal_list=[]):
        """
        Convert signal data into suitable string format
        """
        signal_list = [-1 if i == 0 else i for i in signal_list]
        wave = ""
        for i in signal_list:
            # positive and previous null or negative new wave
            if (i>0):
                wave += " "+str(i)+self.start_high
            # negative or zero and previous null or pative new wave
            elif(i<0):
                wave += " "+str(abs(i))+self.start_low  

        return wave
        
    def clock_signal(self, synch_type="rising", period=2, length=10):
        """
        get clock signal for a period and a lenght,
        @param synch_type: define the moment of synchronization
        @type synch_type: enumerate string ('rising', "falling", "high", "low", "asynch")
        @param period: define clock
        @type period: integer, default 2
        @param length: define diagram length
        @type length: integer, default 10
        @return: an svg string
        @rtype:  string as svg code
        """
        clock = {}
        synch_type = self.synch_type
        if( synch_type != "asyngh"):
            clock = { "name": "H",   "wave": "","period": period  }
            if(synch_type == "rising"):
                clock["wave"] = "[timing/c/rising arrows] "
            elif (synch_type == "falling"):
                clock["wave"] = "[timing/c/falling arrows] "
            elif (synch_type == "high"):
                clock["wave"] = "[timing/c/rising arrows] "
            elif (synch_type == "low"):
                clock["wave"] = "[timing/c/no arrows] "
            else:
                clock["wave"] = "[timing/c/no arrows] "
            clock["wave"] = clock["wave"]+ "C %d{%dC}"%(length, period)
        return clock

    def save(self, signals_data=[], filename=""):
        """
        Save SVG code on given filename
        @param signals: signals data
        @type signals: list of signal dict
        @param filename: file name to be used
        @type filename: string
        @return: success code/fail code
        @rtype:  integer
        """
        # ~ lines = []
        # ~ for signal in signals_data:
            # ~ name = signal.get('name', "X")
            # ~ wave = signal.get('wave', "L")
            # ~ lines.append("$%s$ & %s\\\\"%(name, wave))
        # ~ if(self.synch_type=="falling"):
            # ~ output = TEMPLATE_FALLING.replace("{SIGNALS}", "\n".join(lines))
        # ~ else:
            # ~ output = TEMPLATE_RISING.replace("{SIGNALS}", "\n".join(lines))
        # ~ print(signals_data)
        try:
            fl= open(filename, "w")
            fl.write(signals_data)
            return 0
        except:
            print("Error: can't write into file ", filename)
            return -1
        return 0; 
        
    def random_signal2(self, init=-1, length=10):
        """
        generate a random list of signal data
        
        """
       
        fracs= [0.5,0.5,0.25,0.75,0,0,0,0,0,0]
        signal = [random.randint(-8,+8)+random.choice(fracs) for i in range(length)]
        # avoid 0
        signal = [-1 if i == 0 else i for i in signal]
        return signal
        
    def random_signal(self, init=-1, length=10):
        """
        generate a random list of signal data
        
        """
        # choice first sign
        sign = random.choice([-1, 1])
        total = 0
        fracs= [0.5,0.5,0.25,0.75,0,0,0,0,0,0]
        signal = []
        # the signal must limited by length
        while(total < length and length - total > 1):
            # generate a step with decimals
            step = random.randint(0,4)+random.choice(fracs)
            # avoid zero
            if(not step):
                step = 1
            # if total is greater than length reduce last step 
            if total + step > length:
                step = length - total
            total += step
            signal.append(sign*step)
            # inverse sign
            sign *= -1
            
        # if total is less than length add a new step 
        if total < length:
            step = (length - total)* sign
            signal.append(length - total)
       
        # to check
        s = [abs(i) for i in signal]
        print(sum(s)==length, "Check list generation, ", s, sum(s) )
        
        return signal



if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

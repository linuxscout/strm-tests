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
from deprecated import deprecated
import wavedrom
import json
import random
import chronograms

@deprecated(reason="SVG format is moved to quiz_format class")
class SVG_Chronograms(chronograms.Chronograms):
    """
    A class to generate questions and answers on chronograms
    """
    def __init__(self,):
        # H scale for scale draw
        self.format = "wavedrom"
        self.hscale = 2
        self.start_high = "h"
        self.extend_high = "."
        self.start_low = "l"
        self.extend_low = "."
        # 
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
        return data;
    def stringfy2(self, signal_list=[]):
        """
        Convert signal data into suitable string format
        """
        # ~ wave = "".join([str(i) for i in  singal_list])
        # replace zeros by -1
        signal_list = [-1 if i == 0 else i for i in signal_list]
        wave = ""
        previous_case = 0
        for i in signal_list:
            # positive and previous null or negative new wave
            if (i>=1 and previous_case <=0):
                wave += "h"
                # add points
                if i>1:
                    wave += "."*abs(i-1)
                
            # negative or zero and previous null or pative new wave
            elif(i<0 and previous_case >=0):
                wave += "l"
                # add points
                if i<-1:
                    wave += "."*abs(i)-1                    
            # positive and previous positive OR negative and previous negative, extends
            elif (i>=1 and previous_case >=0) or (i<=1 and previous_case <=0):
                wave += "."*abs(i)
            previous_case = i
        print("Signal", signal_list, "wave", wave)
                
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
            clock = { "name": "H",   "wave": "P.......","period": period  }
            if(synch_type == "rising"):
                clock["wave"] = "lP"
            elif (synch_type == "falling"):
                clock["wave"] = "hN"
            elif (synch_type == "high"):
                clock["wave"] = "lp"
            elif (synch_type == "low"):
                clock["wave"] = "hn"
            else:
                clock["wave"] = "lp"
            clock["wave"] = clock["wave"]+ "."*length
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
        result_data = {"signal": signals_data,
         "config" : { "hscale" : self.hscale }}
        print(result_data)
        svg = wavedrom.render(json.dumps(result_data))
        try:
            svg.saveas(filename)
            return 0
        except:
            return -1
        return 0; 




if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

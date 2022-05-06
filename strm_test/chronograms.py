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
class Chronograms:
    """
    A class to generate questions and answers on chronograms
    """
    def __init__(self,):
        # H scale for scale draw
        self.hscale = 2
        high_char = "\u00AF" # unicode macron

        # define symbols used for high and low
        self.start_high = "|"+high_char
        self.extend_high = high_char
        self.start_low = "|_"
        self.extend_low = "_"
        # define period symbols
               
        self.rising_period = "\u2191%s|_"%high_char     #rising_edge = "\u2191" # unicode uparrow
        self.falling_period = "\u2193_|"+high_char   #falling_edge = "\u2193" # unicode uparrow
        self.high_period = "|%s|_"%high_char 
        self.low_period  = "|_|"+high_char 
        # config
        self.synch_type = "rising"     
    def set_synch_type(self, synch):
        """
        set synchronization type
        """
        
        self.synch_type = synch
        
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
    def stringfy(self, signal_list=[]):
        """
        Convert signal data into suitable string format
        """

        signal_list = [-1 if i == 0 else i for i in signal_list]

        wave = ""
        previous_case = 0
        for i in signal_list:
            # positive and previous null or negative new wave
            if (i>=1 and previous_case <=0):
                wave += self.start_high
                # add points
                if i>1:
                    wave += self.extend_high*abs(i-1)
                
            # negative or zero and previous null or pative new wave
            elif(i<0 and previous_case >=0):
                wave += self.start_low
                # add points
                if i<-1:
                    wave += self.extend_low*abs(i)-1                    
            # positive and previous positive OR negative and previous negative, extends
            elif (i>=1 and previous_case >=0):
                wave += self.extend_high*abs(i)
            elif (i<=1 and previous_case <=0):
                wave += self.extend_low*abs(i)
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
                clock["wave"] = self.start_low + self.rising_period
            elif (synch_type == "falling"):
                clock["wave"] = self.start_high + self.falling_period
            elif (synch_type == "high"):
                clock["wave"] = self.start_low + self.high_period
            elif (synch_type == "low"):
                clock["wave"] = elf.start_low + self.low_period
            else:
                clock["wave"] = "lp"
            clock["wave"] = clock["wave"]*length
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

        print("********** chronogram ***************")
        print("========= START =========")
        for sig in signals_data:
            print(sig.get("name"), sig.get("wave"))
        print("========= END  =========") 
        return 0; 

    def question(self, varlist={}, length=10):
        """
        Generate question Data for given variables
        @param varlist: list of vars names and their initail values
        @type varlist: dict of string keys with int values
        @param synch_type: define the moment of synchronization
        @type synch_type: enumerate string ('rising', "falling", "high", "low")
        @return: data question as signals with their data list
        @rtype:  dict of string keys with int list values
        """
        signals = {}
        for key in varlist:
            init_value = varlist[key]
            signals[key] = self.random_signal(init=init_value, length=length)        
        return signals;     
                  
    def resolve(self, flip_type="", signals={}, period=2):
        """
        Generate an signal answer for given variables signals especialy for a given flipflop type
        @param flip_type: flip flop name
        @type flip_type: string
        @param signals: a dict of list of intergers, positive represent high, negatives represent low
        @type signals: dict of list of integers
        @param synch_type: define the moment of synchronization
        @type synch_type: enumerate string ('rising', "falling", "high", "low")
        @return: data question as signals with their data list
        @rtype:  dict of string keys with int list values
        """
        out_signal = []
        if(flip_type.upper()=="D"):
            out_signal = self.synchronize_signal(signals.get("D"), period=period)

        if(flip_type.upper()=="JK"):
            j_signal = self.synchronize_signal(signals.get("J", []), period=period)
            k_signal = self.synchronize_signal(signals.get("K",[]), period=period)
            q_signal = signals.get("Q",[-1,])
            
            return self.resolve_jk(j_signal, k_signal, q_signal, period=period)
                
                    
        
            
        return out_signal
    def resolve_jk(self, j_signal, k_signal, q_signal, period=2):
        """
        """
        # ~ return j_signal
        if (not j_signal or not k_signal or not  q_signal):
            return out_signal;            
        elif(len(j_signal) != len(k_signal)):
            return out_signal;

        if self.synch_type == "falling":
            q_signal[0] = q_signal[0]*period
        previous = q_signal[0]
        for i in range(1,len(j_signal)):
            j = j_signal[i]
            k = k_signal[i]
            if abs(previous) != period:
                previous *=period
            if(j<0 and k<0): #  0 0  memory
                q_signal.append(previous)
            elif(j<0 and k>0): # 0 1  reset
                q_signal.append(-period)
            elif(j>0 and k<0): # 1 0 set
                q_signal.append(period)
            elif(j>0 and k>0): # 1 1  flip
                q_signal.append(-previous)
            previous = q_signal[i]
        print("j signal:", j_signal)
        print("k signal:", k_signal)
        print("q signal:", q_signal)            
                
        return q_signal

    def synchronize_signal(self, signal=[], period=2):
        """
        Synchronize a signal with periods
        @param signal: list of intergers, positive represent high, negatives represent low
        @type signal: list of integers
        @param synch_type: define the moment of synchronization
        @type synch_type: enumerate string ('rising', "falling", "high", "low")
        @return: list of intergers of valeu synchronized with clock
        @rtype:  list of integer
        """

        # buffer
        n = 0
        sign = 1 if signal[0]>0 else -1
        out_signal = [sign*period]
        if self.synch_type=="rising":
            n = 1
            out_signal = [sign*period//2,]
        for sig in signal:
            n += abs(sig)
            sign = 1 if sig>0 else -1
            while n >= period:
                n -= period
                out_signal.append(sign*period)
        return out_signal;
    
    def random_signal(self, init=-1, length=10):
        """
        generate a random list of signal data
        
        """
        signal = [random.randint(-1,1) for i in range(length)]
        # avoid 0
        signal = [-1 if i == 0 else i for i in signal]
        return signal
        
def test_draw():
    """ Test draw function """
    svg = wavedrom.render("""
{ "signal": [
 { "name": "H",   "wave": "P.......","period": 2  },
 { "name": "D",    "wave": "105.......0.100000111110." },
 { "name": "Q",   "wave": "zp.........5555z.", "data": "D0 D1 D2 D3" }
]}""")
    svg.saveas("demo1.svg")

def test_draw2():
    """ Test draw function """
    chrono = Chronograms();
    filename = "output.svg"
    varlist = {"D":1, "Q":-1, "R":-1, "S":-1}
    signals = chrono.question(varlist)
    clock = chrono.clock_signal(length=6, period=2.5)
        
    data = chrono.draw(signals, clock)
    print("data", json.dumps(data))
    chrono.save(data, filename)
    
def main(args):
    test_draw()
    test_draw2()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

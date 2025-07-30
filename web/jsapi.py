#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  jsapi.py
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

import threading
import time
import sys
import random
import webview
sys.path.append('../')
import strmquiz

class Api:
    def __init__(self, viewer):
        self.cancel_heavy_stuff_flag = False
        self.viewer = viewer
        # ~ result = self.viewer.parser.action('freerooms')
        # ~ print(result)        

    
    def init(self):
        response = {
            'message': 'Hello from Python {0}'.format(sys.version)
        }
        return response

    def getRandomNumber(self):
        response = {
            'message': 'Here is a random number courtesy of randint: {0}'.format(random.randint(0, 100000000))
        }
        return response

    def doHeavyStuff(self):
        time.sleep(0.1)  # sleep to prevent from the ui thread from freezing for a moment
        now = time.time()
        self.cancel_heavy_stuff_flag = False
        for i in range(0, 1000000):
            _ = i * random.randint(0, 1000)
            if self.cancel_heavy_stuff_flag:
                response = {'message': 'Operation cancelled'}
                break
        else:
            then = time.time()
            response = {
                'message': 'Operation took {0:.1f} seconds on the thread {1}'.format((then - now), threading.current_thread())
            }
        return response

    def cancelHeavyStuff(self):
        time.sleep(0.1)
        self.cancel_heavy_stuff_flag = True


    def doaction(self, name, format_output="latex"):

        self.viewer.parser.set_format(format_output);
        if name.startswith("test"):
            self.viewer.parser.reset()
                
            result = self.viewer.parser.get_test(name)
        else:
            result = self.viewer.parser.get_question(name)
        
        response = {
            'message': result
        }
        return response

    def error(self):
        raise Exception('This is a Python exception')



if __name__ == '__main__':
    api = Api()
    filename = "ressources/html/main.html"
    htmlfile = open(filename)
    htmlcontent = htmlfile.read()
    try:
        htmlfile = open(filename)
        htmlcontent = htmlfile.read()
    except:
        print("Can't open file %s"%filename)
        sys.exit()
    window = webview.create_window('API example', html=htmlcontent, js_api=api)
    webview.start()


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
import web.webviewer as webviewer
from web.jsapi import Api


if __name__ == '__main__':

    filename = "resources/html/main.html"
    config_file = "config/quiz2.conf"
    viewer = webviewer.mywebviewer(config_file)    
    # welcome window
    welcomefilename = "resources/html/welcome.html"

    # main window
    api = Api(viewer)
    window = webview.create_window('STRM Test Generator', filename, js_api=api, )
    webview.start(debug=True)


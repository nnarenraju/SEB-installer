# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
restrict.py
    Restricts the usage of any .exe file while running

Created on Thu Aug 13 13:15:35 2020

__author__      = nnarenraju
__copyright__   = Copyright 2020, Restrictor
__credits__     = nnarenraju
__license__     = Apache License 2.0
__version__     = 1.0.0
__maintainer__  = nnarenraju
__email__       = nnarenraju@gmail.com
__status__      = Debugging


Github Repository: NULL

Documentation: NULL

"""

import re
import time
import numpy as np
from subprocess import Popen, PIPE

def run(command):
    process = Popen(command,shell=True,stdout=PIPE,stderr=PIPE)    
    # Get stdout and break
    stdout, stderr = process.communicate()
    return stdout.decode('utf-8')

# Get the abspath of Zoom.exe
stdout = run("wmic process where \"name='Zoom.exe'\" get ProcessID, ExecutablePath")
PATH = re.findall(r'(.:\\.*?\.[\w:]+)', stdout)
# Kill new processes
stdout = run("wmic process get ProcessId")
PID  = re.findall(r'[0-9]+', stdout)

# Check stdout for new processes
while True:
    time.sleep(5)
    stdout = run("wmic process get ProcessId")
    new = re.findall(r'[0-9]+', stdout)
    diff = np.setdiff1d(new, PID)
    if any(diff):
        _ = [run("taskkill /F /PID {}".format(ID)) for ID in diff]
    
    
    
    
    
    
    
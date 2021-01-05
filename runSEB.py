# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import re
import shutil
from subprocess import Popen, PIPE

def run(command, out=False):
    process = Popen(command,shell=True,stdout=PIPE,stderr=PIPE)    
    # Get stdout and break
    if out:
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr

# Get the abspath of Zoom.exe
while True:
    stdout,_= run("wmic process where \"name='Zoom.exe'\" get ProcessID, ExecutablePath", out=True)
    if not _:
        PATH = re.search(r'(.:\\.*?\.[\w:]+)', stdout)
        break

# Save zoom path
with open("SebClientSettings.seb", "r") as foo:
    contents = foo.read()

# Regex for path replacement
search = r"...............................Zoom...."
re.sub(search,re.escape(PATH.group()),contents)

# Write new .seb file
with open("test.seb",'w') as foo:
    foo.write(contents)

# Download SEB from SourceForge
#_=run("curl -L -s -o seb.exe https://sourceforge.net/projects/seb/files/latest/download")

# Search for .seb savefile location
sebsave = r"C:\Users\Admin\AppData\Roaming\SafeExamBrowser"
while True:
    if os.path.isdir(sebsave):
        shutil.move(r"test.seb", sebsave)
        os.startfile("C:\Program Files\SafeExamBrowser\Configuration\SEBConfigTool.exe")
        break
        
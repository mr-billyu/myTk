#!/usr/bin/env python3

#
# Parse Configurable Button data.
#
import re

data = ['  edit    : LightSteelBlue:  /home/data/scripts/e2 %filename',
        '  te      : Light SkyBlue :  te %filename                   ',
        '  prt     : DeepSkyBlue   :  prt %filename                  ',
        '  rm      : tomato        :  rm %filetype %filename         ',
        '  sh      : gold          :  sh                             ',
        '  notes   : burlywood     :  notes                          ',
        '  lock    : chocolate     :  lock                           ']

for rcd in data:
    print(rcd)
    x = re.sub('^\s*', '', rcd)
    x1 = re.sub('\s*$', '', x)
    x2 = re.sub('\s*:\s*', ':', x1)
    print(x2)
    (desc, color, action) = x2.split(':')
    print(desc)
    print(color)
    print(action)
    print(' ')


'''
#
# Replace '|' with ','
#
for s in ('(txt)', '(txt|)', '(txt|py)', '(txt|py|)'):
    print(s + ': ' + s.replace('|)', ')'))
'''

'''
#
# argparse
#
import argparse
parser = argparse.ArgumentParser(description='GUI program that searches' +
                                             ' all *.txt files in a' +
                                             ' directory for entered' +
                                             ' parameter.')
parser.add_argument('directory', help='Directory to search')
parser.add_argument('filetype', help='Comma separate list of file types')
args = parser.parse_args()
directory = args.directory
filetype = args.filetype
print(directory)
print(filetype)
for file in filetype.split(','):
    print(file)
'''

'''
#
# Use regular expression to separate line into parts.
#
import re
line = "/home/pi/ssh/BillyU_data/Bill/Documents/raspberrypi/test.txt:abcd"
m = re.match(r'(^\S*/)(\S*.txt:.*)', line)

print(m.group(0))
print(m.group(1))
print(m.group(2))
'''

'''
#
# Open a new shell and start less program.
#
import os
os.system('lxterminal -e less Win.pm')
'''

'''
#
# Remove '\n' from end of line
#
import os
results = os.popen("grep list *.py") 
for line in results:
    print(line.rstrip())
'''

'''
#
# Simple program using scrollbar.
#
from tkinter import *
from tkinter import ttk
root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

mainloop()
'''

'''
#
# Setting and clearing textvariable
#
from tkinter import *
from tkinter import ttk
def cb(evnt):
    print(v.get())
    v.set("")

win = Tk()
win.title("test")
v = StringVar()
entry = Entry(win, textvariable=v)
entry.pack()
entry.bind('<Return>', cb)
win.mainloop()
'''

'''
#
# Get input from entry window.
#
from tkinter import *
from tkinter import ttk
def cb(evnt):
    print(entry.get())

win = Tk()
win.title("test")
entry = Entry(win)
entry.pack()
entry.bind('<Return>', cb)
win.mainloop()
'''

'''
#
# Menu example
#
menudata = (("File", ("Quit", "root.quit"), ("Exit", "root.quit")),
            ("Help", ("About", "about"))
           )

for column in menudata:
    print(column)
    for entry in column:
        print(entry, type(entry))
'''

#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

import re
line = "/home/pi/ssh/BillyU_data/Bill/Documents/raspberrypi/test.txt:abcd"
m = re.match(r'(^\S*/)(\S*.txt:.*)', line)

print(m.group(0))
print(m.group(1))
print(m.group(2))



'''
import os
os.system('lxterminal -e less Win.pm')
'''

'''
import os
results = os.popen("grep list *.py") 
for line in results:
    print(line.rstrip())
'''

'''
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
menudata = (("File", ("Quit", "root.quit"), ("Exit", "root.quit")),
            ("Help", ("About", "about"))
           )

for column in menudata:
    print(column)
    for entry in column:
        print(entry, type(entry))
'''

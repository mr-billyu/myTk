#!/usr/bin/env python3

from myTk import myTk
import os
import re


def get_entry(event='x'):
    global path
    gui.clearlist('results')
    param = gui.getentry('searchfor')
    option = '-n'
    if gui.getcheckbutton('case') == 0:
        option = option + 'i'
    if gui.getcheckbutton('word') == 1:
        option = option + 'w'
    option = option + ' '
    results = os.popen("grep " + option + " " + param + 
             " /home/pi/ssh/BillyU_data/Bill/Documents/raspberrypi/*.txt")
    for line in results:
        m = re.match(r'(^\S*/)(\S*.txt:.*)', line)
        path = m.group(1)
        gui.setlist('results', m.group(2))
    gui.setlist('results', '======END======')

def get_selected(event):
    global path
    selection = gui.getlistselection('results').split(":", 2)
    filename = path + selection[0]
    os.system('lxterminal -e less +' + selection[1] + ' ' + filename)

gui = myTk()
Win = gui.win('Search Pi Notes', '640x480')

gui.frame('fill')
menudata = (("file", ("quit", Win.quit)),)
gui.menubar(menudata)

gui.frame('fill')
gui.textentry('searchfor', 'Find', 50)
gui.bindentry('searchfor', '<Return>', get_entry)
gui.focusentry('searchfor')
gui.checkbutton('case', 'Case', get_entry)
gui.checkbutton('word', 'Word', get_entry)

gui.frame('expand')
gui.listbox('results')
gui.bindlist('results', '<Double-1>', get_selected)

Win.mainloop()

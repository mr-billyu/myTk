#!/usr/bin/env python3

import argparse
from myTk import myTk
import os
import re


def get_entry(event='x'):
    global directory
    gui.clearlist('results')
    param = gui.getentry('searchfor')
    option = '-n'
    if gui.getcheckbutton('case') == 0:
        option = option + 'i'
    if gui.getcheckbutton('word') == 1:
        option = option + 'w'
    option = option + ' '
    results = os.popen("grep " + option + " " + param + " " +
             directory + "/*.txt")
    for line in results:
        m = re.match(r'(^\S*/)(\S*.txt:.*)', line)
        gui.setlist('results', m.group(2))
    gui.setlist('results', '======END======')

def get_selected(event):
    global directory 
    selection = gui.getlistselection('results').split(":", 2)
    filename = directory + '/' + selection[0]
    os.system('lxterminal -e less +' + selection[1] + ' ' + filename)

#=========================================================================
parser = argparse.ArgumentParser(description='GUI program that searches' +
                                             ' all *.txt files in a' +
                                             ' directory for entered' +
                                             ' parameter.')
parser.add_argument('directory', help='Directory to search')
args = parser.parse_args()
directory = args.directory
print(directory)

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

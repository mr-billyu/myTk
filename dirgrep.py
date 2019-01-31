#!/usr/bin/env python3

import argparse
from myTk import myTk
import os
import re

def get_entry(event='x'):
    gui.clearlist('results')
    param = gui.getentry('searchfor')
    option = '-n'
    if gui.getcheckbutton('case') == 0:
        option = option + 'i'
    if gui.getcheckbutton('word') == 1:
        option = option + 'w'
    option = option + ' '
    search_and_report(param, option)

def clear_entry(event='x'):
    gui.setentry('searchfor', '')

def set_entry_and_search(param):
    gui.setentry('searchfor', param)
    option = '-n '
    search_and_report(param, option)

def search_and_report(param, option):
    files = ''
    types = '('
    for ft in filetypes.split(','):
        ft = ft.replace(" ", "")
        files = files + directory + "/*." + ft + " "
        types = types + ft + '|'
    types = types + ')'
    types = types.replace('|)', ')')

    results = os.popen("grep " + option + " " + param + " " + files)
    for line in results:
        exp = '(^\S*/)(\S*' + types + ':.*)'
        m = re.match(exp, line)
        gui.setlist('results', m.group(2))
    gui.setlist('results', '======END======')

def get_selected(event):
    selection = gui.getlistselection('results').split(":", 2)
    filename = directory + '/' + selection[0]
    os.system('lxterminal -e less +' + selection[1] + ' ' + filename)

def main():
    global gui
    global directory
    global filetypes
    parser = argparse.ArgumentParser(
                         description='GUI program that searches' +
                                     ' all specified file types' +
                                     ' in a directory for entered' +
                                     ' parameter.')
    parser.add_argument('directory', help='Directory to search.' +
                                          ' ie. /home/pi/Documents')
    parser.add_argument('filetypes', help='Comma separated list of file' +
                                          ' types. ie. py,txt,pl')
    parser.add_argument('--searchfor', help='Optional string to search' +
                                            ' for', nargs='?')
    args = parser.parse_args()
    directory = args.directory
    filetypes = args.filetypes
    searchfor = args.searchfor

    gui = myTk()
    Win = gui.win('Search Pi Notes', '640x480')

    gui.frame('fill')
    menudata = (("file", ("quit", Win.quit)),)
    gui.menubar(menudata)

    gui.frame('fill')
    gui.textentry('searchfor', 'Find', 50)
    gui.bindentry('searchfor', '<Return>', get_entry)
    gui.bindentry('searchfor', '<3>', clear_entry)
    gui.focusentry('searchfor')
    gui.checkbutton('case', 'Case', get_entry)
    gui.checkbutton('word', 'Word', get_entry)

    gui.frame('expand')
    gui.listbox('results')
    gui.bindlist('results', '<Double-1>', get_selected)
    if searchfor:
        set_entry_and_search(searchfor)

    Win.mainloop()

if __name__ == '__main__':
    main()

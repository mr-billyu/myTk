#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

class myTk():
    '''
    Create Window Object:
        self = myTk()

    Create Widgets Methods:
        widget = obj.win('title', 'geometry')
        widget = obj.button('desc', 'color', 'command')
        widget = obj.checkbutton('id', 'desc', 'command')
        widget = obj.frame(<'fill'|'expand'|''>)
        widget = obj.label('l|c|r', 'text')
        widget = obj.list('id')
        widget = obj.multilist('id')
        widget = obj.menubar(menudata)
            where:  menudata = (("File", ("New", create_file), 
                                         ("Save", save_file),
                                         ("Quit", root.quit)),

                                ("Edit", ("Copy", copy_selection),
                                         ("Paste", paste_selection),
                                         ("Clear", clear_screen)),

                                ("Help", ("About", about))
                               )

        widget = obj.textbox('id')
        widget = obj.textentry('id', 'prompt', size)

    Get Data Methods:
        value     = obj.getentry('id')
        selection = obj.getlistselection('id')
        linenbr   = obj.getlistline('id')
        []        = obj.getallsellistline('id')
        top       = obj.getlisttop('id')
        value     = obj.getcheckbutton('id')
        []        = obj.gettextall('id')
        value     = obj.gettextindex('id')
        value     = obj.gettextselection('id')

    Set/Clear Data Methods:
        obj.clearlist('id')
        obj.setlist('id', 'line')
        obj.setlistsel('id', 'linenbr')
        obj.setlistpos('id', 'linenbr')
        obj.setlisttop('id', 'linenbr')
        obj.setentry('id', value)
        obj.setcheckbutton('id', value)
        obj.cleartext('id')
        obj.inserttext('id', 'index', 'line')
        obj.settextpos('id', 'index')

    Action Methods:
        obj.bindentry('id', '<key>', callbackfunc)

    User Configurable buttons:

    User Configurable menus:

    Misc Methods:

    Note: Some valid keys: <Return>, <Button-1>, <Double-Button-3>, 
             'a', '1', 'b', etc.
          Some valid colors: 'LightSteelBlue', 'LightSkyBlue', 'white',
          'black', 'cyan', 'DeepSkyBlue, 'tomato', 'gold', 'burlywood',
          'chocolate', 'DodgerBlue', 'navyblue', etc.
    '''

    def __init__(self):
        self.entry = {} 
        self.lbox = {}
        self.tbox = {}
        self.ckbutton = {}
        self.btn = {}

    def win(self, title, geometry):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(geometry)
        return(self.root)

    def menubar(self, menudata):
        menubar = Menu(self.frm)
        for column in menudata:
            menu = Menu(menubar)
            for entry in column:             
                if isinstance(entry, str):
                    menubar.add_cascade(label=entry, menu=menu)
                else:
                    menu.add_command(label=entry[0], command=entry[1])
        self.root.config(menu=menubar)

    def frame(self, option):
        self.frm = ttk.Frame(self.root)
        if option == 'fill':
            self.frm.pack(side=TOP, fill=X)
        elif option == 'expand':
            self.frm.pack(side=TOP, fill=BOTH, expand=1)
        else:
            self.frm.pack(side=TOP)

    def label(self, position, text):
        if position == 'l':
            position = 'left'
        elif position == 'c':
            position = 'top'
        else:
            position = 'right'
        ttk.Label(self.frm, text=text).pack(side=position)

    def textentry(self, id, prompt, width):
        self.label('l', 'User Input')
        self.entry[id] = {} 
        self.entry[id]['value'] = StringVar() 
        self.entry[id]['obj'] = Entry(self.frm, width=width,
                                bg="white", fg="black",
                                textvariable=self.entry[id]['value'])
        self.entry[id]['obj'].pack(side=LEFT, fill=X)

    def bindentry(self, id, key, callbackfunc):
        self.entry[id]['obj'].bind(key, callbackfunc)

    def focusentry(self, id):
        self.entry[id]['obj'].focus()

    def getentry(self, id):
        return(self.entry[id]['value'].get())

    def setentry(self, id, value):
        self.entry[id]['value'].set(value)
    
    def listbox(self, id):
        vsb = Scrollbar(self.frm, orient=VERTICAL)
        vsb.pack(side=RIGHT, fill=Y)

        hsb = Scrollbar(self.frm, orient=HORIZONTAL)
        hsb.pack(side=BOTTOM, fill=X)

        self.lbox[id] = {}
        self.lbox[id] = Listbox(self.frm, bg="white", fg="black",
                                yscrollcommand=vsb.set,
                                xscrollcommand=hsb.set)
        self.lbox[id].pack(side=LEFT, expand=1, fill=BOTH)

        vsb.config(command=self.lbox[id].yview)
        hsb.config(command=self.lbox[id].xview)

    def bindlist(self, id, key, callbackfunc):
        self.lbox[id].bind(key, callbackfunc)

    def getlistselection(self, id):
        line = self.lbox[id].curselection()
        if line:
            selection = self.lbox[id].get(line)
        else:
            selection = ''
        return(selection)

    def getlistline(self, id):
        return(self.lbox[id].curselection())

    def getallsellistline(self, id):
        return(self.lbox[id].curselection()) #Same as getlistline???

    def getlisttop(self, id):
        return(self.lbox[id].nearest(0))

    def clearlist(self, id):
        self.lbox[id].delete(0, 'end') 

    def setlist(self, id, data):
        self.lbox[id].insert('end', data)

    def setlistsel(self, id, linenbr):
        self.lbox[id].select_set(linenbr)

    def setlistpos(self, id, linenbr):
        self.lbox[id].see(linenbr)

    def setlisttop(self, id, linenbr):
        self.lbox[id].yview(linenbr)

    def checkbutton(self, id, desc, callbackfunc):
        self.ckbutton[id] = {}
        self.ckbutton[id]['value'] = IntVar()
        self.ckbutton[id]['obj'] = ttk.Checkbutton(self.frm, text=desc, 
                                      variable=self.ckbutton[id]['value'],
                                      command=callbackfunc)
        self.ckbutton[id]['obj'].pack(side=LEFT, fill=X)

    def getcheckbutton(self, id):
        return(self.ckbutton[id]['value'].get())

    def setcheckbutton(self, id, value):
        self.ckbutton[id]['value'].set(value)
        

    def textbox(self, id):
        vsb = Scrollbar(self.frm, orient=VERTICAL)
        vsb.pack(side=RIGHT, fill=Y)

        hsb = Scrollbar(self.frm, orient=HORIZONTAL)
        hsb.pack(side=BOTTOM, fill=X)

        self.tbox[id] = Text(self.frm, bg="white", fg="black",
                             yscrollcommand=vsb.set,
                             xscrollcommand=hsb.set)
        self.tbox[id].pack(side=LEFT, expand=1, fill=BOTH)

        vsb.config(command=self.tbox[id].yview)
        hsb.config(command=self.tbox[id].xview)

    def bindtext(self, id, key, callbackfunc):
        self.tbox[id].bind(key, callbackfunc)

    def gettextall(self, id):
        return(self.tbox[id].get('1.0', 'end'))

    def gettextindex(self, id):
        #Returns linenbr.lineposition.
        return(self.tbox[id].index('insert'))

    def gettextselection(self, id):
        return(self.tbox[id].selection_get())

    def cleartext(self, id):
        self.tbox[id].delete('0.0', 'end')

    def inserttext(self, id, index, line):
        #index 'linenbr.linepos'
        self.tbox[id].insert(index, line)

    def settextpos(self, id, index):
        #index 'linenbr.linepos'
        self.tbox[id].see(index)

    def button(self, desc, color, func):
        self.btn[desc] = Button(text=desc, background=color, command=func)
        self.btn[desc].pack(side='left')

    def About(self):
        print("Python3 tkinker sample program.")

'''
==========================================================================
                               Test Code
==========================================================================
'''
if __name__ == "__main__":
    tests = ('textentry', 'textbox', 'button', 'label')
    selection = ''

    def about():
        print("about test")

    def get_entry(arg):
        print(app.getentry('input_1'))
        app.setentry('input_1', "")
        
    def get_selected_line(arg):
        print(app.getlistselection('results'))

    def get_selected_text():
        global selection
        selection = app.gettextselection('display')

    def get_textbox_index(arg):
        print(app.gettextindex('display'))

    def clear_textbox():
        app.cleartext('display')

    def set_textbox(arg):
        app.inserttext('display', '0.0', '0123456789012345678901234567890')

    def paste():
        index = app.gettextindex('display')
        app.inserttext('display', index, selection)

    def set_textbox_pos(arg):
        app.inserttext('display', '1.10', 'abcdefg')

    def insert_button():
        print('test button pressed')
        paste()

    def get_case():
        print("get case")
        print(app.getcheckbutton('case'))

    def get_word():
        print("get word")
        print(app.getcheckbutton('word'))

    app = myTk()
    Win = app.win('Tkinter Template', '640x480')

    app.frame('fill')
    if 'textbox' in tests:
        menudata = (("File", ("Quit", Win.quit)), 

                    ("Edit", ("Copy", get_selected_text), 
                             ("Paste", paste),
                             ("Clear", clear_textbox)),

                    ("Help", ("About", about))
                   )   
    else:
        menudata = (("File", ("Quit", Win.quit)),

                    ("Help", ("About", about))
                   )
    app.menubar(menudata)

    if 'label' in tests:
        app.frame('fill')
        app.label('l', 'left')
        app.frame('fill')
        app.label('c', 'center')
        app.frame('fill')
        app.label('r', 'right')

    if 'textentry' in tests:
        app.frame('fill')
        app.textentry('input_1', 'User Input', 50)
        app.bindentry('input_1', '<Return>', get_entry)
        app.focusentry('input_1')
        app.checkbutton('case', 'Case', get_case) 
        app.checkbutton('word', 'Word', get_word)

    if 'listbox' in tests: 
        app.frame('expand')
        app.listbox('results')
        app.bindlist('results', '<Double-Button-1>', get_selected_line)
        for i in range(100):
            app.setlist('results', "this is a test line " + str(i))
        app.setlisttop('results', 3)
        app.setlistpos('results', 50)
        app.setlistsel('results', 45)

    if 'textbox' in tests:
        app.frame('expand')
        app.textbox('display')
        app.bindtext('display', '<Button-2>', get_textbox_index)
        for i in range(200):
            app.inserttext('display', str(i) + '.0', 
                            "this is a test of textbox" + str(i) + "\n")
        print(app.gettextall('display'))

    if 'button' in tests:
        app.frame('fill')
        app.button('copy', 'white', get_selected_text)
        app.button('paste', 'LightSteelBlue', paste)
        app.button('clear', 'DodgerBlue', clear_textbox)

    app.root.mainloop()



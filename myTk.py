#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

class myTk():
    '''
    Create Window Object:
        self = myTk()

    Quit Window Object:
        obj.quit()

    Create Widgets Methods:
        obj.win('title', 'geometry')
        obj.button('desc', 'color', 'command')
        obj.checkbutton('id', 'desc', 'command')
        obj.combobox('id', 'label', values[])
        obj.frame(<'fill'|'expand'|''>)
        obj.label('l|c|r', 'text')
        obj.list('id')
        obj.multilist('id')
        obj.menubar(menudata)
            where:  menudata = (("File", ("New", create_file), 
                                         ("Save", save_file),
                                         ("Quit", root.quit)),

                                ("Edit", ("Copy", copy_selection),
                                         ("Paste", paste_selection),
                                         ("Clear", clear_screen)),

                                ("Help", ("About", about))
                               )

        obj.textbox('id')
        obj.rotextbox('id')
        obj.radiobutton('id', "desc", ((label0, 'val1'),
                                                (label1, 'val2'),
                                                (label2, 'val3'))
        obj.textentry('id', 'prompt', size)

    Get Data Methods:
        value     = obj.getentry('id')
        selection = obj.getlistselection('id')
        linenbr   = obj.getlistline('id')
        []        = obj.getallsellistline('id')
        top       = obj.getlisttop('id')
        value     = obj.getcheckbutton('id')
        []        = obj.gettextboxall('id')
        value     = obj.gettextboxindex('id')
        value     = obj.gettextboxselection('id')
        value     = obj.getcombobox('id')
        selection = obj.getradiobutton('id')

    Set/Clear Data Methods:
        obj.clearlist('id')
        obj.clearrotextbox('id')
        obj.cleartextbox('id')
        obj.setcombobox('id', 'value')
        obj.setlist('id', 'line')
        obj.setlistsel('id', 'linenbr')
        obj.setlistpos('id', 'linenbr')
        obj.setlisttop('id', 'linenbr')
        obj.setentry('id', value)
        obj.setcheckbutton('id', value)
        obj.insertrotextbox('id', 'index', 'line')
        obj.inserttextbox('id', 'index', 'line')
        obj.settextboxpos('id', 'index')
        obj.setcursor('watch'|'normal')
        obj.setradiobutton('id', 'value')

    Action Methods:
        obj.bindentry('id', '<key>', callbackfunc)
        obj.bindlist('id', '<key>', callbackfunc)
        obj.bindrotextbox('id' '<key>', callbackfunc)
        obj.bindtextbox('id', '<key>', callbackfunc)
        obj.bindcombobox('id', '<key>', callbackfunc)

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
        self.rotbox = {}
        self.ckbutton = {}
        self.btn = {}
        self.cbox = {}
        self.radiobtn = {}

    def win(self, title, geometry):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(geometry)

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
        self.label('l', prompt)
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

    def bindtextbox(self, id, key, callbackfunc):
        self.tbox[id].bind(key, callbackfunc)

    def gettextboxall(self, id):
        return(self.tbox[id].get('1.0', 'end'))

    def gettextboxindex(self, id):
        #Returns linenbr.lineposition.
        return(self.tbox[id].index('insert'))

    def gettextboxselection(self, id):
        print(id)
        return(self.tbox[id].selection_get())

    def cleartextbox(self, id):
        self.tbox[id].delete('0.0', 'end')

    def inserttextbox(self, id, index, line):
        #index 'linenbr.linepos'
        self.tbox[id].insert(index, line)

    def settextboxpos(self, id, index):
        #index 'linenbr.linepos'
        self.tbox[id].see(index)

    def rotextbox(self, id):
        vsb = Scrollbar(self.frm, orient=VERTICAL)
        vsb.pack(side=RIGHT, fill=Y)

        hsb = Scrollbar(self.frm, orient=HORIZONTAL)
        hsb.pack(side=BOTTOM, fill=X)

        self.rotbox[id] = Text(self.frm, bg="white", fg="black",
                               yscrollcommand=vsb.set,
                               xscrollcommand=hsb.set,
                               state='disabled')
        self.rotbox[id].pack(side=LEFT, expand=1, fill=BOTH)

        vsb.config(command=self.rotbox[id].yview)
        hsb.config(command=self.rotbox[id].xview)

    def bindrotextbox(self, id, key, callbackfunc):
        self.rotbox[id].bind(key, callbackfunc)
 
    def insertrotextbox(self, id, index, line):
        self.rotbox[id].config(state='normal')
        #index 'linenbr.linepos'
        self.rotbox[id].insert(index, line)
        self.rotbox[id].config(state='disabled')

    def clearrotextbox(self, id, index, line):
        self.rotbox[id].config(state='normal')
        self.rotbox[id].delete('0.0', 'end')
        self.rotbox[id].config(state='disabled')

    def getrotextboxselection(self, id):
        return(self.rotbox[id].selection_get())

    def button(self, desc, color, func):
        self.btn[desc] = Button(text=desc, background=color, command=func)
        self.btn[desc].pack(side='left')

    def setcursor(self, curs):
        if curs != 'watch':
            curs = 'top_left_arrow'

        self.root.config(cursor=curs)
        if self.entry != {}:
            for id in self.entry:
                self.entry[id]['obj'].config(cursor=curs)
        if self.lbox != {}:
            for id in self.lbox:
                self.lbox[id].config(cursor=curs)
        if self.tbox != {}:
            for id in self.tbox:
                self.tbox[id].config(cursor=curs)
        if self.rotbox != {}:
            for id in self.rotbox:
                self.rotbox[id].config(cursor=curs)

    def combobox(self, id, label, values):
        self.label('l', label)
        self.cbox[id] = {}
        self.cbox[id]['value'] = StringVar()
        self.cbox[id]['obj'] = ttk.Combobox(self.frm, values=values,
                                    textvariable=self.cbox[id]['value'])
        self.cbox[id]['obj'].pack(side=LEFT, fill=X)

    def setcombobox(self, id, default):
        self.cbox[id]['value'].set(default)

    def getcombobox(self, id):
        return(self.cbox[id]['value'].get())

    def bindcombobox(self, id, key, callbackfunc):
        self.cbox[id]['obj'].bind(key, callbackfunc)

    def radiobutton(self, id, desc, buttondata):
        self.label('l', desc)
        self.radiobtn[id] = {}
        self.radiobtn[id]['value'] = StringVar()
        for text, value in buttondata:
            self.radiobtn[id]['obj'] = Radiobutton(self.frm, text=text, 
                                       value=value,
                                       variable=self.radiobtn[id]['value'])
            self.radiobtn[id]['obj'].pack(side=LEFT, fill=X)

    def getradiobutton(self, id):
        return(self.radiobtn[id]['value'].get())

    def setradiobutton(self, id, val):
        self.radiobtn[id]['value'].set(val)

    def quit(self):
        self.root.quit()


'''
==========================================================================
                               Test Code
==========================================================================
'''
if __name__ == "__main__":
    tests = ('combobox', 'textbox', 'rotextbox', 'textentry', 'radiobutton', 'button')
    selection = ''

    def about():
        print("about test")

    def get_entry(arg):
        print(app.getentry('input_1'))
        app.setentry('input_1', "")
        
    def get_selected_line(arg):
        print(app.getlistselection('results'))

    def get_selected_rotext(arg):
        print(app.getrotextboxselection('rodisplay'))

    def get_textbox_index(arg):
        print(app.gettextboxindex('display'))

    def copy():
        global selection
        selection = app.gettextboxselection('display')

    def clear():
        app.cleartextbox('display')

    def paste():
        index = app.gettextboxindex('display')
        app.inserttextbox('display', index, selection)

    def set_textbox():
        app.inserttextbox('display', '0.0', '0123456789012345678934567890')

    def get_selected_text(arg):
        global selection
        selection = app.gettextboxselection('display')
        print(selection)

    def get_case():
        print("get case")
        print(app.getcheckbutton('case'))

    def get_word():
        print("get word")
        print(app.getcheckbutton('word'))

    def get_cursor():
        if app.getcheckbutton('cursor'):
            app.setcursor('watch')
        else:
            app.setcursor('top_left_arrow')

    def get_combobox(arg):
        print(app.getcombobox('combo'))

    def get_radiobutton():
        print(app.getradiobutton('test'))

    app = myTk()
    app.win('myTk Tests', '640x480')

    app.frame('fill')
    if 'textbox' in tests:
        menudata = (("File", ("Quit", app.quit)), 

                    ("Edit", ("Copy", copy), 
                             ("Paste", paste),
                             ("Clear", clear)),

                    ("Help", ("About", about))
                   )   
    else:
        menudata = (("File", ("Quit", app.quit)),

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

    if '2nd_textentry' in tests:
        app.frame('fill')
        app.textentry('input_2', 'User In2', 45)
        app.checkbutton('cursor', 'Cursor', get_cursor)

    if 'radiobutton' in tests:
        modes = [('Monochrome', '1'),
                 ('Grayscale', '2'),
                 ('true color', '3'),
                 ('color separate', '4')]
        app.frame('fill')
        app.radiobutton('test', 'label', modes)
        app.setradiobutton('test', '2')

    if 'combobox' in tests:
        app.frame('fill')
        app.combobox('combo', 'combobox', ('a', 'b', 'cdefghijk'))
        app.setcombobox('combo', 'default')
        app.bindcombobox('combo', '<Return>', get_combobox)

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
        app.bindtextbox('display', '<Button-2>', get_textbox_index)
        for i in range(200):
            app.inserttextbox('display', str(i) + '.0', 
                            "this is a test of textbox" + str(i) + "\n")

    if 'rotextbox' in tests:
        app.frame('expand')
        app.rotextbox('rodisplay')
        app.bindrotextbox('rodisplay', '<Button-2>', get_selected_rotext)
        for i in range(200):
            app.insertrotextbox('rodisplay', str(i) + '.0', 
                              "this is a test of rotextbox" + str(i) + "\n")

    if 'button' in tests:
        app.frame('fill')
        if 'textbox' in tests:
            app.button('copy text', 'white', copy)
            app.button('paste text', 'LightSteelBlue', paste)
            app.button('clear text', 'DodgerBlue', clear)
            app.button('load text', 'tomato', set_textbox)
        if 'radiobutton' in tests:
            app.button('radiobutton', 'white', get_radiobutton)

    app.root.mainloop()



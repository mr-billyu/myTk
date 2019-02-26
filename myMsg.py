#!/usr/bin/env python3

from myTk import myTk
import argparse

parser = argparse.ArgumentParser(description='Display the message on the' +
                                             'command line in a window.')
parser.add_argument('msg', help='Message to display.')
args = parser.parse_args()
message = args.msg

def ok():
    msg.quit()

msg = myTk()
msg.win('Message', '440x100')

f = msg.frame('')
tb = msg.rotextbox('message')
tb.config(width=60, height=4)
msg.insertrotextbox('message', '0.0', message)

b = msg.button('Close', 'tomato', ok)
b.pack_forget()
b.pack(side='right')

msg.root.mainloop()


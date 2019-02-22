#!/usr/bin/env python3

from myTk import myTk

def ok():
    msg.quit()

msg = myTk()
msg.win('Message', '640x100')

msg.frame('expand')
msg.rotext('message')
msg.insertrotext('message', '0.0', 'Test Message')

msg.frame('fill')
msg.button('Ok', 'tomato', ok)

msg.root.mainloop()


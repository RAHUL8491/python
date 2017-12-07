"""
GUI APP to Flip a coin
"""
import Tkinter
from Tkinter import *
import tkMessageBox
import random

def OnClick():
    x = random.randint(0, 1)
    if x:
        print "Head"
        r = "HEAD"
    else:
        print "Tail"
        r = "TAIL"
    tkMessageBox.showinfo("RESULT", "RESULT: " + str(r))
# GUI
root = Tk()
root.title("FLIP A COIN")
# BUTTON
B = Tkinter.Button(root, text="FLIP!", command=OnClick)
B.pack()
B.grid_location(30, 30)
#Loop
root.mainloop()

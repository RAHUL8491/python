"""
GUI APP to convert currency 1 to currency 2's value given exchange rate

#Author : Satheesh Gopalan

#Version 1

# On the date of 26 July 2017
"""

import Tkinter
from Tkinter import *
import tkMessageBox

def OnClick():
    """ 
        Handle the Button click's
        Gets input
        Verifies that input is valid       
    """
    currency1 = 0
    exchange_rate = 0
    state = 0
    try:
        currency1 = float(E1.get())
        exchange_rate = float(E2.get())

    except ValueError:
        print "Bad Input!"
        state = 1
        E1.delete(0, END)
        E2.delete(0,END)

    result(currency1,exchange_rate,state)

def result(x,y,z):
    """ Print the Result in message box 
        
        Variable z is to verify that input are valid (in GOOD STATE)
        
        Variable x and y are inputs
    
    """
    if z ==1 :
        tkMessageBox.showinfo("RESULTS", "Invalid Input !! \n Please Try Again !! \n\n Press \"OK\" to quit.")
        root.quit()
    else :
        r = x * y
        tkMessageBox.showinfo("RESULTS", "Value in Currency 2 is : " + str(r) + "\n Rounded off Value :" + str(round(r,2)))



# GUI

root = Tk()
root.title("Currency Converter")

#Labels & Enteries

L1 = Label(root, text="Currency 1 Amount  ")
L1.pack()
L1.grid_location(0,0)

E1 = Entry(root , bd =5 )
E1.pack()
L1.grid_location(20,0)

L2 = Label(root, text="Exchange Rate ")
L2.pack()
L2.grid_location(0,20)

E2 = Entry(root , bd =5 )
E2.pack()
L2.grid_location(20,30)

#BUTTON
B = Tkinter.Button(root, text ="Convert!",command = OnClick )
B.pack()
B.grid_location(30,30)

#LOOP IT TILL YOU MAKE IT
root.mainloop()

"""
GUI APP to Calulate BMI

#Author : Satheesh Gopalan

#Version 1

# On the date of 1st Aug 2017
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
    height = 0
    weight = 0
    state = 0
    try:
        height = float(E1.get())
        weight = float(E2.get())

    except ValueError:
        print "Bad Input!"
        state = 1
        E1.delete(0, END)
        E2.delete(0,END)

    result(height/100,weight,state)

def result(x,y,z):
    """ Print the Result in message box 
        
        Variable z is to verify that input are valid (in GOOD STATE)
        
        Variable x and y are inputs
    
    """
    if z ==1 :
        tkMessageBox.showinfo("ERROR!", "Invalid Input !! \n Please Try Again !! \n\n Press \"OK\" to quit.")
        root.quit()
    else :

        r = y / x
        r = r / x
        r = round(r,2)

        if r < 0:
            t = "You must have given Invalid Input !! Enter Height in Centimeter & Weight in KG's"
        elif r > 0 and r < 18.5:
            t = " UNDERWEIGHT! "
        elif r > 18.5 and r < 24.9:
            t = " HEALTHY ! Good for you! You have an Ideal BMI"
        elif r > 24.9 and r < 30:
            t = " OVERWEIGHT !! You should control diet & get some Exercise!"
        elif r > 30:
            t = " OBESE!! You probably should see a doctor ! "

        tkMessageBox.showinfo("BMI", "Your BMI is : " + str(r) + "\n You are : " + t)



# GUI

root = Tk()
root.title("BMI CALCULATOR")

#Labels & Enteries

L1 = Label(root, text="HEIGHT (in centimeter)")
L1.pack()
L1.grid_location(0,0)

E1 = Entry(root , bd =5 )
E1.pack()
L1.grid_location(20,0)

L2 = Label(root, text="WEIGHT (in Kg's)")
L2.pack()
L2.grid_location(0,20)

E2 = Entry(root , bd =5 )
E2.pack()
L2.grid_location(20,30)

#BUTTON
B = Tkinter.Button(root, text ="Calculate BMI !",command = OnClick )
B.pack()
B.grid_location(30,30)

#LOOP IT TILL YOU MAKE IT
root.mainloop()

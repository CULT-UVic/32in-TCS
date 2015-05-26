#!/usr/bin/python

"""
Observing GUI for the 32-inch telescope at UVic

Interface software for using the Princeton instruments CCD through C functions
compiled with WinView

Authors:
    Zack Draper
    
Last modified: March 2015

"""

import Tkinter as tk
import tkMessageBox
from PIL import Image, ImageTk

#Establish primary frame
root = tk.Tk()
root.title("32-inch Control Interface")
frame = tk.Frame(root,width=1000,height=500)
frame.pack()

#Insert obligitory UVic image

img = Image.open("./uvic_astro.jpg")
img = img.resize((150, 150), Image.ANTIALIAS)
uvastro = ImageTk.PhotoImage(img)
img1 = tk.Label(image=uvastro)
img1.place(x=20, y=20)

#Allow user to take a series of Darks with one button
def dark_exposure():
    tkMessageBox.showinfo( "Hello Python", "Hello World")
    
dark = tk.Button(frame, text = "Take Darks", command = dark_exposure, height=2,width=20)

dark.place(x=800,y=100)

#Execute GUI
root.mainloop()

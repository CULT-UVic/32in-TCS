#!/usr/bin/python

"""
Observing GUI for the 32-inch telescope at UVic

Interface software for using the Princeton instruments CCD through C functions
compiled with WinView

Authors:
    Zack Draper, Nic Annau
    
Last modified: March 2015

"""
import pysao 
import Tkinter as tk
import tkMessageBox
from PIL import Image, ImageTk
import sys, os

#Establish primary frame
root = tk.Tk()
root.title("32-inch Control Interface")
frame = tk.Frame(root,width=1000,height=700, bg='dark red')
frame.pack()

#Display experiment setup label
title = tk.Label(root, text="Experiment Setup", bg = "dark red", fg="white")
title.pack()
title.place(x=250, y = 25)

#Insert obligitory UVic image
img = Image.open("./astronomy.JPG")
img = img.resize((150, 210), Image.ANTIALIAS)
uvastro = ImageTk.PhotoImage(img)
img1 = tk.Label(image=uvastro)
img1.place(x=20, y=20)

#Allow user to select exposures they would like to execute, including more than one type of image
def dark_exposure():
    tkMessageBox.showinfo( "Hello Python", "Hello World")
def ds9_window():
	os.system('ds9 &')
def light_exposure():
	tkMessageBox.showinfo( "Hello Python", "Hello World")
def bias_exposure():
	tkMessageBox.showinfo( "Hello Python", "Hello World")
def flat_standard():
	tkMessageBox.showinfo( "Hello Python", "Hello World")
def flat_short():
	tkMessageBox.showinfo( "Hello Python", "Hello World")
def apply_exp():
	tkMessageBox.showinfo("Test", "Testing")

#Master 'take exposure' button (only used after the experiment has been set up)
exp = tk.Button(frame, text="Take Exposures", command = apply_exp, height=2, width = 20, bg='dark red', highlightbackground='dark red')
exp.place(x=800, y=440)

'''    
dark = tk.Button(frame, text = "Take Darks", command = dark_exposure, height=2,width=20)
ds9_button = tk.Button(frame, text="Open ds9", command = ds9_window, height=2, width = 20, bg='dark red')
light_exposure = tk.Button(frame, text="Take Lights", command = light_exposure, height=2, width = 20, bg='dark red')
bias_exposure = tk.Button(frame, text="Take Bias", command = bias_exposure, height=2, width = 20, background='dark red')
flat_standard = tk.Button(frame, text="Take Standard Flat", command = flat_standard, height=2, width = 20, bg='dark red')
flat_short = tk.Button(frame, text="Take Short Flat", command = flat_short, height=2, width = 20, bg='dark red')

dark.place(x=800,y=100)
ds9_button.place(x=800, y= 300)
light_exposure.place(x=500, y=100)
bias_exposure.place(x=500, y=200)
flat_standard.place(x=500, y=300)
flat_short.place(x= 800, y=200)
'''
ds9_button = tk.Button(frame, text="Open ds9", command = ds9_window, height=2, width = 20, bg='dark red', highlightbackground='dark red')
ds9_button.place(x=800, y= 50)
#define series of check boxes that have either a "yes" or "no" value associated with them
dark_var = tk.IntVar()
dark_choice = tk.Checkbutton(frame, text="Take Dark Frame", variable=dark_var, onvalue="yes", offvalue="no", bg='dark red', fg='white')
dark_choice.place(x=250, y=50)

light_var = tk.IntVar()
light_choice = tk.Checkbutton(root, text="Take Light Frame", variable=light_var, onvalue="yes", offvalue="no", bg='dark red')
light_choice.place(x=250, y=250)

bias_var = tk.IntVar()
bias_choice = tk.Checkbutton(root, text="Take Bias Frame", variable=bias_var, onvalue="yes", offvalue="no", bg='dark red')
bias_choice.place(x=250, y=450)

flat_var = tk.IntVar()
flat_choice = tk.Checkbutton(root, text="Take Standard Flat Frame", variable=flat_var, onvalue="yes", offvalue="no", bg='dark red')
flat_choice.place(x=500, y=50)

flat_short_var = tk.IntVar()
flat_short_choice = tk.Checkbutton(root, text="Take Short Flat Frame", variable=flat_short_var, onvalue="yes", offvalue="no", bg='dark red')
flat_short_choice.place(x=500, y=250)

#Entry boxes
entry_dark_txt = tk.Label(root, text="Number of Dark Frames", bg = "dark red", fg="white")
entry_dark_txt.pack()
entry_dark_txt.place(x=250, y = 70)
entry_dark = tk.Entry(root, width=7)
entry_dark.pack()
entry_dark.insert(0, "0")
entry_dark.place(x=253, y=90)
entry_dark_txt_len = tk.Label(root, text="Length of Exposure (s)", bg = "dark red", fg="white")
entry_dark_txt_len.pack()
entry_dark_txt_len.place(x=250, y = 120)
entry_dark_len = tk.Entry(root, width=7)
entry_dark_len.pack()
entry_dark_len.insert(0, "0")
entry_dark_len.place(x=253, y=140)

entry_light_txt = tk.Label(root, text="Number of Light Frames", bg = "dark red", fg="white")
entry_light_txt.pack()
entry_light_txt.place(x=250, y = 270)
entry_light = tk.Entry(root, width=7)
entry_light.pack()
entry_light.insert(0, "0")
entry_light.place(x=253, y=290)
entry_light_txt_len = tk.Label(root, text="Length of Exposure (s)", bg = "dark red", fg="white")
entry_light_txt_len.pack()
entry_light_txt_len.place(x=250, y = 320)
entry_light_len = tk.Entry(root, width=7)
entry_light_len.pack()
entry_light_len.insert(0, "0")
entry_light_len.place(x=253, y=340)

entry_bias_txt = tk.Label(root, text="Number of Bias Frames", bg = "dark red", fg="white")
entry_bias_txt.pack()
entry_bias_txt.place(x=250, y = 470)
entry_bias = tk.Entry(root, width=7)
entry_bias.pack()
entry_bias.insert(0, "0")
entry_bias.place(x=253, y=490)
entry_bias_txt_len = tk.Label(root, text="Length of Exposure (s)", bg = "dark red", fg="white")
entry_bias_txt_len.pack()
entry_bias_txt_len.place(x=250, y = 520)
entry_bias_len = tk.Entry(root, width=7)
entry_bias_len.pack()
entry_bias_len.insert(0, "0")
entry_bias_len.place(x=253, y=540)

entry_flat_txt = tk.Label(root, text="Number of Flat Frames", bg = "dark red", fg="white")
entry_flat_txt.pack()
entry_flat_txt.place(x=500, y = 70)
entry_flat = tk.Entry(root, width=7)
entry_flat.pack()
entry_flat.insert(0, "0")
entry_flat.place(x=503, y=90)
entry_flat_txt_len = tk.Label(root, text="Length of Exposure (s)", bg = "dark red", fg="white")
entry_flat_txt_len.pack()
entry_flat_txt_len.place(x=500, y = 120)
entry_flat_len = tk.Entry(root, width=7)
entry_flat_len.pack()
entry_flat_len.insert(0, "0")
entry_flat_len.place(x=503, y=140)

entry_flat_short_txt = tk.Label(root, text="Number of Flat Frames", bg = "dark red", fg="white")
entry_flat_short_txt.pack()
entry_flat_short_txt.place(x=500, y = 270)
entry_flat_short = tk.Entry(root, width=7)
entry_flat_short.pack()
entry_flat_short.insert(0, "0")
entry_flat_short.place(x=503, y=290)
entry_flat_short_txt_len = tk.Label(root, text="Length of Exposure (s)", bg = "dark red", fg="white")
entry_flat_short_txt_len.pack()
entry_flat_short_txt_len.place(x=500, y = 320)
entry_flat_short_len = tk.Entry(root, width=7)
entry_flat_short_len.pack()
entry_flat_short_len.insert(0, "0")
entry_flat_short_len.place(x=503, y=340)

#Execute GUI
root.mainloop()

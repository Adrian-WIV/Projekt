import tkinter as tk
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

root = ThemedTk(theme = "winxpblue")
root.geometry('300x400')

mybutton = ttk.Button(root, text = "nutzloser \n Knopf")

mytreeview = ttk.Treeview(root,)

myentry = ttk.Entry(root)

mybutton.place(relx=0.5, rely=0.5, anchor = CENTER)
myentry.place(relx = 0.5, rely = 0.8, anchor = N)
mytreeview.place(relx = 0.5, anchor = N)


root.mainloop()
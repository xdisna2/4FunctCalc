from tkinter import *
from tkinter import ttk

# Creates top level window
root = Tk()

label = ttk.Label(root, text='0')
label.grid(row = 0, column = 0, columnspan = 3)
label.pack()

# Functions for output
def output1():
    label.config(text='1')
def output2():
    label.config(text='2')
def output3():
    label.config(text='3')
def clearall():
    label.config(text='0')

# Create buttons 1,2,3
num1 = ttk.Button(root, text='1', command=output1)
num2 = ttk.Button(root, text='2', command=output2)
num3 = ttk.Button(root, text='3', command=output3)
clear = ttk.Button(root, text='Clear', command=clearall)

# Geometry packs them
num1.pack()
num2.pack()
num3.pack()
clear.pack()

root.mainloop()




from tkinter import *
from tkinter import ttk

# Creates top level window
root = Tk()

# Functions for output
def output1():
    print(1)
def output2():
    print(2)
def output3():
    print(3)

# Create buttons 1,2,3
num1 = ttk.Button(root, text='1', command=output1)
num2 = ttk.Button(root, text='2', command=output2)
num3 = ttk.Button(root, text='3', command=output3)

# Geometry packs them
num1.pack()
num2.pack()
num3.pack()

root.mainloop()




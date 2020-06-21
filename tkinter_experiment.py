from tkinter import *
from tkinter import ttk

# Creates top level window
root = Tk()

label = ttk.Label(root, text='0')
label.grid(row = 0, column = 0, columnspan = 3)
label.pack()

# Functions for output (Shorter revised version
def output(number):
    label.config(text=number)


# Create buttons 1,2,3 (creating a lambda function makes an anonymous function)
num1 = ttk.Button(root, text='1', command=lambda: output(1))
num2 = ttk.Button(root, text='2', command=lambda: output(2))
num3 = ttk.Button(root, text='3', command=lambda: output(3))
clear = ttk.Button(root, text='Clear', command=lambda: output(0))

# Geometry packs them
num1.pack()
num2.pack()
num3.pack()
clear.pack()
root.mainloop()




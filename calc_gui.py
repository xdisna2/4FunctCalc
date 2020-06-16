from tkinter import *
from tkinter import ttk

# Create the top-level window
root = Tk()

# Stores the buttons for the numbers in a frame
numbers = ttk.Frame(root)
numbers.pack()

numbers.config(height = 150, width = 250)
numbers.config(relief = RIDGE)
num1 = ttk.Button(numbers, text = '1').grid()


root.mainloop()


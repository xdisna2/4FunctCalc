from tkinter import *
from tkinter import ttk

# Create the top-level window
root = Tk()

# Stores the buttons for the numbers in a frame
numbers = ttk.Frame(root)
numbers.pack()

numbers.config(height = 150, width = 250)
numbers.config(relief = RIDGE)
deci = ttk.Button(numbers, text = '.').grid(row = 3, column = 2)
num0 = ttk.Button(numbers, text = '0').grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
num1 = ttk.Button(numbers, text = '1').grid(row = 2, column = 0)
num2 = ttk.Button(numbers, text = '2').grid(row = 2, column = 1)
num3 = ttk.Button(numbers, text = '3').grid(row = 2, column = 2)
num4 = ttk.Button(numbers, text = '4').grid(row = 1, column = 0)
num5 = ttk.Button(numbers, text = '5').grid(row = 1, column = 1)
num6 = ttk.Button(numbers, text = '6').grid(row = 1, column = 2)
num7 = ttk.Button(numbers, text = '7').grid(row = 0, column = 0)
num8 = ttk.Button(numbers, text = '8').grid(row = 0, column = 1)
num9 = ttk.Button(numbers, text = '9').grid(row = 0, column = 2)



root.mainloop()


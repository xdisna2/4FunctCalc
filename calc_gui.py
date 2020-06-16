from tkinter import *
from tkinter import ttk

# Create the top-level window
root = Tk()

# Stores the buttons for the numbers in a frame
numbers = ttk.Frame(root)
numbers.pack()

numbers.config(height = 150, width = 250)
numbers.config(relief = RIDGE)
num0 = ttk.Button(numbers, text = '0').grid()
num1 = ttk.Button(numbers, text = '1').grid()
num2 = ttk.Button(numbers, text = '2').grid()
num3 = ttk.Button(numbers, text = '3').grid()
num4 = ttk.Button(numbers, text = '4').grid()
num5 = ttk.Button(numbers, text = '5').grid()
num6 = ttk.Button(numbers, text = '6').grid()
num7 = ttk.Button(numbers, text = '7').grid()
num8 = ttk.Button(numbers, text = '8').grid()
num9 = ttk.Button(numbers, text = '9').grid()



root.mainloop()


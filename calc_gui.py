from tkinter import *
from tkinter import ttk

# Create the top-level window
root = Tk()

# Label for number output
output = ttk.Label(root, text = '0')
output.pack()

# Stores the buttons for the numbers in a frame
calc = ttk.Frame(root)
calc.pack()

# Number Frames
numbers = ttk.Frame(calc)
numbers.grid(row = 0, column = 0)

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

# 4 Function Operations
operations = ttk.Frame(calc)
operations.grid(row = 0, column = 1)

operations.config(height = 150, width = 50, relief = RAISED)
add = ttk.Button(operations, text = '+').grid(row = 0, column = 0)
sub = ttk.Button(operations, text = '-').grid(row = 1, column = 0)
div = ttk.Button(operations, text = '/').grid(row = 2, column = 0)
multi = ttk.Button(operations, text = 'x').grid(row = 3, column = 0)

# Equals
equate = ttk.Button(calc, text = '=').grid(row = 1, column = 0, columnspan = 2, sticky = W + E)



root.mainloop()


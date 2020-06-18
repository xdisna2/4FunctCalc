from tkinter import *
from tkinter import ttk

# Create the top-level window
root = Tk()
root.title('4 Function Calculator')
# Prevents the Calculator from being resized
root.resizable(False, False)

# Label for number output
output = Label(root, text = '0', height = 2, background = 'snow')
output.pack(fill = X)

# Stores the buttons for the numbers in a frame
calc = ttk.Frame(root)
calc.pack()

# Number Frames
numbers = ttk.Frame(calc)
numbers.grid(row = 0, column = 0)

# Configures the frame height and width
numbers.config(height = 150, width = 200, relief = RIDGE, padding = 5)
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
op_wd = 8
op_pd = 5
operations = ttk.Frame(calc)
operations.grid(row = 0, column = 1)

operations.config(height = 150, width = op_wd, relief = SUNKEN, padding = op_pd)
add = ttk.Button(operations, text = '+')
sub = ttk.Button(operations, text = '-')
div = ttk.Button(operations, text = '/')
multi = ttk.Button(operations, text = 'x')

# Operation grid manager
add.grid(row = 0, column = 0)
sub.grid(row = 1, column = 0)
div.grid(row = 2, column = 0)
multi.grid(row = 3, column = 0)

# Operation Button width
add.config(width = op_wd)
sub.config(width = op_wd)
div.config(width = op_wd)
multi.config(width = op_wd)

# Equals button
equate = ttk.Button(calc, text = '=').grid(row = 1, column = 0, columnspan = 2, sticky = W + E)


root.mainloop()


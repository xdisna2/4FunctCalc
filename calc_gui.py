from tkinter import *
from tkinter import ttk
user_num = ''
expr = ''
signs = ['+', '-', '/', '*']

# Outputs numbers to Label and gathers expression for calculation
def number_disp(number):
    global user_num
    global expr

    # If FIRST number is 0 and the string is blank then do not do anything
    # Other than that output the input
    if not(number == 0 and user_num == ''):

        # If that number is not a sign then concatenate and display the ouput
        if number not in signs:
            user_num += str(number)
            output.config(text=user_num)

        # If it is a sign then add the number and the sign to the current expression
        # Then clear the user_num left over for the next number
        else:
            expr = expr + user_num + number
            user_num = ''

# Resets Label and also clears all calculations
def clear_num(num):
    global user
    global expr
    output.config(text=str(num))
    user = ''
    expr = ''

# Calculates based on given expression
def evaluate():
    global user_num
    global expr
    # Add in the second number to the expression
    expr += user_num
    # Evaluate the string expression
    answer = float(eval(expr))
    # Checks to see if the float could be an integer
    if answer.is_integer():
        # If so then round to an int and output
        output.config(text=str(round(answer)))
    else:
        output.config(text=str(answer))

    # Makes the answer the user_num for future calculations
    user_num = str(answer)
    expr = ''


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

# Configures the frame height and width along with Button configurations
numbers.config(height = 150, width = 200, relief = RIDGE, padding = 5)
deci = ttk.Button(numbers, text = '.', command = lambda : number_disp('.')).grid(row = 3, column = 2)
num0 = ttk.Button(numbers, text = '0', command = lambda : number_disp(0)).grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
num1 = ttk.Button(numbers, text = '1', command = lambda : number_disp(1)).grid(row = 2, column = 0)
num2 = ttk.Button(numbers, text = '2', command = lambda : number_disp(2)).grid(row = 2, column = 1)
num3 = ttk.Button(numbers, text = '3', command = lambda : number_disp(3)).grid(row = 2, column = 2)
num4 = ttk.Button(numbers, text = '4', command = lambda : number_disp(4)).grid(row = 1, column = 0)
num5 = ttk.Button(numbers, text = '5', command = lambda : number_disp(5)).grid(row = 1, column = 1)
num6 = ttk.Button(numbers, text = '6', command = lambda : number_disp(6)).grid(row = 1, column = 2)
num7 = ttk.Button(numbers, text = '7', command = lambda : number_disp(7)).grid(row = 0, column = 0)
num8 = ttk.Button(numbers, text = '8', command = lambda : number_disp(8)).grid(row = 0, column = 1)
num9 = ttk.Button(numbers, text = '9', command = lambda : number_disp(9)).grid(row = 0, column = 2)

# 4 Function Operation Buttons
op_wd = 8
op_pd = 5
operations = ttk.Frame(calc)
operations.grid(row = 0, column = 1)

operations.config(height = 150, width = op_wd, relief = SUNKEN, padding = op_pd)
add = ttk.Button(operations, text = '+', command = lambda : number_disp('+'))
sub = ttk.Button(operations, text = '-', command = lambda : number_disp('-'))
div = ttk.Button(operations, text = '/', command = lambda : number_disp('/'))
multi = ttk.Button(operations, text = 'x', command = lambda : number_disp('*'))

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

# Equals button and clear button
box3 = ttk.Frame(root)
box3.pack()
equate = ttk.Button(box3, text = '=', command= lambda : evaluate()).grid(row = 0, column = 0)
clear = ttk.Button(box3, text = 'C', command=lambda : clear_num(0)).grid(row = 0, column = 1)

root.mainloop()


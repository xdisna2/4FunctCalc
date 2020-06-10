from calc_functions import math

# 4 Function Calculator
if __name__ == '__main__':

    # Calculator will loop forever until prompted
    again = 'y'
    while again == 'y':
        # Asks user to input 2 numbers (for now...)
        # Asks user to input 2 numbers (of any type float or int)
        num1 = float(input())
        num2 = float(input())

        # Asks user to do "what" to the numbers (for now...)
        print("Please select an operation")
        functions = ['Addition', 'Subtraction', 'Division', 'Multiplication']
        for i in range (4):
            print(f"{i+1}: {functions[i]}")

        user_input = int(input())
        # Will compute results based on number selection
        if user_input == 1:
            result = math.add(num1, num2)

        elif user_input == 2:
            result = math.sub(num1, num2)

        elif user_input == 3:
            result = math.div(num1, num2)

        else:
            result = math.multi(num1, num2)

        if result.is_integer():
            x = round(result)
            print(x)
        else:
            print(x)

        again = input("Enter 'y' to continue")

    print("Goodbye")

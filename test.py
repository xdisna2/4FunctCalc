# Testing type conversions

# Entering an int
x = float(input("Number 1:"))
# Convert to float
# So matter its a string it will include the .0 to make it a float
print(x)

# Change from float to int
x = 11.0
print(type(x))
x = round(11.0)
print(type(x))

# Test out is_integer function
# Note to self you must declare it as a float to try it out
x = float(input("Enter a number:"))

# Convert to int
if x.is_integer():
    x = round(x)
    print(x)

# Lets try adding two numbers of different types
x = 11
y = 11.5

z = x + y
# Of course this will output a float
print(z)

# What if it was 2 floats but they add to become an integer?
x = 11.0
y = 11.0

z = x + y
# It will output a float but truly its an even whole number
print(z)

# Now if the total adds up to become an integer then it will make it an integer (whole number)
if z.is_integer():
    z = round(z)
    print(z)
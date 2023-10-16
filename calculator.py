
# EXAMPLE 1
x = 1
y = 2
z = x + y
print(z)

# EXAMPLE 2: we use int() function to convert the string input value to an integer
x = input("what's x? ") # the user input, even if loooks like a number it is a string
y = input("what's y? ") # the user input, even if loooks like a number it is a string
z = int(x) + int(y) # int() converts a string to an integer
print(z)

#EXAMPLE 3:
x = float(input("what's x? ")) # the user input, even if loooks like a number it is a string ~float() converts the string to a number with a decimal point
y = float(input("what's y? ")) # the user input, even if loooks like a number it is a string ~float() converts the string to a number with a decimal point

b = x / y #divide x/y
print(b)

z = round(x / y) # round the result of x/y to the nearest integer
print(z)

a = round(x / y, 2) #round the result of x/y to the nearest number of ~2~ digits 
print(a)
    #or
c = x / y
print(f"{c:.2f}") #round the result of x/y to the nearest number of ~2~ digits 


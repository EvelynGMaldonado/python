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
print(f"{c:.2f}")
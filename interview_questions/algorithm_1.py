'''
Subject: math Module

Math module has a set of methods and constants used for mathematical tasks.

1. Create a solution that accepts three diferent inputs representing the values for x, y, and z. 

2. Write the necessary code to output x to the power of (y to the power of z) ~ Recursive call for x power y power z
    -Problem:  x to the power of (y to the power of z)
    -Output: The result of x power y power z is: {power_of_x_to_y_to_z}


'''

import math

x = float(input("Enter a value for x: "))
y = float(input("Enter a value for x: "))
z = float(input("Enter a value for x: "))

power_of_x_to_y_to_z = math.pow(math.pow(x, y), z)

print(f"The result of x power y power z is: {power_of_x_to_y_to_z}")
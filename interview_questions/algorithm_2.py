'''
Using math functions

Given three floating-point numbers x, y, and z, output x to the power of z, x to the power of (y to the power of z), the absolute value of (x minus y), and the square root of (x to the power of z).

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f} {your_value4:.2f}')

Ex: If the input is:
    5.0
    1.5
    3.2

Then the output is:
    172.47 361.66 3.50 13.13

'''

import math
''' Type your code here. '''

x = float(input())
y = float(input())
z = float(input())

x_to_z = math.pow(x, z)
y_to_z = math.pow(y, z)
x_to_y_to_z = math.pow(math.pow(x, y), z)
x_to_y_to_z_1 = math.pow(x, y_to_z)
ab_of_x_y = math.fabs(x - y)
sq_of_x_to_z = math.sqrt(math.pow(x, z))




print(f'{x_to_z:.2f} {x_to_y_to_z_1:.2f} {ab_of_x_y:.2f} {sq_of_x_to_z:.2f}')
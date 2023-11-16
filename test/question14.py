'''
Create a solution that accepts an integer input. 
Import the built-in module math and use its factorial() method to calculate the factorial of the integer input. 
Output the value of the factorial, as well as a Boolean value identifying whether the factorial output is greater than 100.

The solution output should be in the format
    factorial_value
    Boolean_value

Sample Input/Output:
    If the input is
        10
    
    then the expected output is
        3628800
        True

    Alternatively, if the input is
        3

    then the expected output is
        6
        False

*
Input to program: 
10
*

'''

#import math module and call factorial()
#solution accepts integer input
#solution outputs the factorial of the integer input 
#solution outputs Boolean identification of whether the factorial is >100

import math



try:
    number_check = int(input("Enter a whole positive number: "))
    
    factorial_value = math.factorial(number_check)
    
    print(factorial_value)
    
    if factorial_value > 100:
        print("True")
    else:
        print("False")
    
except ValueError:
    print("Invalid input. Please enter a valid positive number")
    


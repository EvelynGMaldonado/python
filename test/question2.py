'''
Create a solution that accepts an integer input representing any number of ounces. 
Output the converted total number of tons, pounds, and remaining ounces based on the input ounces value. 
There are 16 ounces in a pound and 2,000 pounds in a ton.

The solution output should be in the format
    Tons: value_1
    Pounds: value_2
    Ounces: value_3

Sample Input/Output:
    If the input is
        32035
    
    then the expected output is
        Tons: 1
        Pounds: 2
        Ounces: 3

*
Input to program: 
32035
*

'''

ouncesUserInput = int(input())

totalTons = 1
totalPounds =1
totalOunces =1
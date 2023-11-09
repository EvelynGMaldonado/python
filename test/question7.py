'''
Create a solution that accepts an integer input to compare against the following list:
    predef_list = [4, -27, 15, 33, -10]

Output a Boolean value indicating whether the input value is greater than the maximum value from predef_list


The solution output should be in the format
    Greater Than Max? Boolean_value

Sample Input/Output:
    If the input is
        20
    
    then the expected output is
        Greater Than Max? False

*
Input to program: 
20
*

'''


#solution accepts an integer input
#solution outputs Boolean value indicating if integer input is greater than the maximum value when compared to predef_list

predef_list = [4, -27, 15, 33, -10]

valueA = int(input("Please enter a number: "))

#ordering the list
predef_list.sort()

#getting the max value of the list
list_max_value = predef_list[-1]


if valueA > list_max_value:
    print("Greater Than Max? True")
else:
    print("Greater Than Max? False")
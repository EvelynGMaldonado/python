'''
Create a solution that accepts one integer input representing the index value for any of the string elements in the following list:
    frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

Output the string element of the index value entered. 
The solution should be placed in a try block and implement an exception of "Error" if an incompatible integer input is provided.

The solution output should be in the format
    frameworks_element

Sample Input/Output:
    If the input is
        2
    
    then the expected output is
        CherryPy
    
    Alternatively, if the integer input is
        7
    
    then the expected output is
        Error

*
Input to program: 
2
*

'''

#use try block with exception "Error" when index value is not found in list
#solution accepts an integer input
#solution outputs the corresponding string value for the integer input

frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

for i in range (len(frameworks)):
    try:
        i_value = int(input("Enter a number: "))
        print (frameworks[i_value])
        break

    except ValueError:
        print("Error Value")

    except:
        print('Error') #Error: Index out of range
        break


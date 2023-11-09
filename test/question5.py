'''
Create a solution that accepts five integer inputs. Output the sum of the five inputs three times, converting the inputs to the requested data type prior to finding the sum.
    First output: sum of five inputs maintained as integer values
    Second output: sum of five inputs converted to float values
    Third output: sum of five inputs converted to string values (concatenate)


The solution output should be in the format
    Integer: integer_sum_value
    Float: float_sum_value
    String: string_sum_value

Sample Input/Output:
    If the input is
        1
        3
        6
        2
        7
    
    then the expected output is
        Integer: 19
        Float: 19.0
        String: 13627

*
Input to program: 
1
3
6
2
7
*

'''

#solution accepts five integer inputs
#solution outputs three sums of input values; convert before calculating sum
#first output: sum of five inputs maintained as integer values
#second output: sum of five inputs converted to float values
#third output: sum of five inputs converted to string values (concatenate)

value1 = int(input("Enter value 1: "))
value2 = int(input("Enter value 2: "))
value3 = int(input("Enter value 3: "))
value4 = int(input("Enter value 4: "))
value5 = int(input("Enter value 5: "))

integer_sum_value = value1 + value2 + value3 + value4 + value5
float_sum_value = float(value1) + float(value2) + float(value3) + float(value4) + float(value5)
string_sum_value = str(value1) + str(value2) + str(value3) + str(value4) + str(value5)

print(f"Integer: {integer_sum_value}")
print(f"Float: {float_sum_value}")
print(f"String: {string_sum_value}")
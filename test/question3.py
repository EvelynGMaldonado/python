'''
Create a solution that accepts an integer input representing the index value for any any of the five elements in the following list:
    various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]
Using the built-in function type() and getting its name by using the .name attribute, output data type (e.g., int”, “float”, “bool”, “str”) based on the input index value of the list element.


The solution output should be in the format
    Element index_value: data_type

Sample Input/Output:
    If the input is
        4
    
    then the expected output is
        Element 4: tuple

*
Input to program: 
4
*

'''

#use built-in function type()
#get name by using the built-in attribute __name__
#solution accepts integer input representing list element index
#solution outputs data type of list element based on input index value

various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

index_value = int(input("Select a number from 0-5: "))

index_variable = various_data_types[index_value]
print(f"index_variable: {index_variable}")

data_type_by_index = type(index_variable)
print(f"data_type_by_index: {data_type_by_index}")

data_type_name_by_index = type(index_variable).__name__
print(f"data_type_name_by_index: {data_type_name_by_index}")

print(f"Element {index_value}: {data_type_name_by_index}")
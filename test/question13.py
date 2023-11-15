'''
Create a solution that accepts an input identifying the name of a CSV file, for example, "input1.csv". 
Each file contains two rows of comma-separated values. 
Import the built-in module csv and use its open() function and reader() method to create a dictionary of key:value pairs for each row of comma-separated values in the specified file. 
Output the file contents as two dictionaries.

The solution output should be in the format
    {'key': 'value', 'key': 'value', 'key': 'value'}
    {'key': 'value', 'key': 'value', 'key': 'value'}

Sample Input/Output:
    If the input is
        input1.csv
    
    then the expected output is
        {'a': '100', 'b': '200', 'c': '300'}
        {'bananas': '1.85', 'steak': '19.99', 'cookies': '4.52'}

    Alternatively, if the input is
        input2.csv

    then the expected output is
        {'d': '400', 'e': '500', 'f': '600'}
        {'celery': '2.81', 'milk': '4.34', 'bread': '5.63'}

*
Input to program: 
input1.csv
*

'''

#import csv module and call open(), reader()
#solution accepts input identifying name of CSV file (i.e., "input1.csv")
#solution outputs each row of CSV file contents as a dictionary of elements


import csv

file_name = str(input())

dictionary_output = {}

with open(file_name, "r") as file:
    data_file = csv.reader(file)
    for row in data_file:
        #print(row)
        dictionary_output = {row[column].strip(): row[column + 1].strip() for column in range(0, len(row), 2)}
        print(dictionary_output)
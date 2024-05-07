'''
EXCERCISE #14: VERIFY DATA IS VALID (NUMERIC)

    Interview/Test Question might be something like -->

It is important to ensure that user input is valid before acceptance to verify that the data received is of the expected data type.
Using the provided template code, validate that the zip code input by the user is an integer data type.

For example, 
If an integer input is:
12345
The output to the console will be the following:
Your zip code is 12345.

Alternatively, if a non-integer value input is:
abcdefg
The output to the console will be the following:
Please use numeric digits for the zip code.

'''


#check if the zipcode input is numeric

if __name__ == '__main__': 
        
    zipCode = input()
    try:
        #check that zip code is an integer value

        print(f'Your zip code is {zipCode}.')

    except:
        print('Please use numeric digits for the zip code.')
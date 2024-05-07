'''
EXCERCISE #11: CHECK DATA TO VERIFY VALUES/NULL

    Interview/Test Question might be something like -->

    External data quality can affect downstream systems, reporting, and metrics and cause vulnerabilities in our systems. 
    a) Using the templated code provided, write one method to check if a string is not null and a separate method to check if a string contains all numbers.
    b) Your first variable will be a string and contain a simple sentence, such as "I like dogs." Your second variable will be an integer and will contain a few numbers, such as 12345.
    c) Complete the functions in the code template.


For example, if the variables in the templated code are:
I like dogs.
12345
The output to the console will be the following:
True
True

Alternatively, if the variable values in the template code are changed to:
None
12345
The output to the console will be the following:
False
True

Alternatively, if the variable values in the template code are changed to:
None
"I love dogs"
The output to the console will be the following:
False
False    

'''

# verify we only have digits

def check_numeric_value(wg_int):
    
        #return true if numeric value is an integer, else return false.  
        #Hint: use isinstance() function
    if type(wg_int) == str:
        try:
            cast_int = int(wg_int)
            return(isinstance(wg_int, int))
        except Exception as e:
            return False
    else:
        return(isinstance(wg_int, int))

# verify if the string is null

def check_null_string (wg_string):
    
    # check if wg_string is not null return true else return false
    if wg_string:
        return True
    else:
        return False
    
if __name__ == '__main__':  
    
    wg_string = "I like dogs." # use keyword None to test
    wg_int = 12345
    
    print(check_null_string (wg_string))
    print(check_numeric_value(wg_int))
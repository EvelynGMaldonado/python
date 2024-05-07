'''

EXERCISE #1: CREATE A BUILT-IN FUNCTION THAT DETERMINES IF A NUMBER IS EVEN OR ODD 

    Interview/Test Question might be something like --> IMPLEMENT "is_even" USING A BOOLEAN FUNCTION.

    a) define a main function and call it at the end of the file.
    b) creating any variables into my main() function that I might need to store date
    c) call any needed functions into my main() function, using conditionals if needed.
    d) define any functions used into the main function right before calling the main function at the end of the page.

'''

import logging
import sys

#log division by zero error to the log, the output is printed to the screen 
def divideByZeroError(dividend, divisor):

    logging.basicConfig(stream=sys.stdout,format='%(levelname)s:%(message)s')
    
    try:

        quotient = dividend/divisor  
        print (quotient)
        
    except Exception as e:

        #logging error here, use str(e) as part of the output

if __name__ == '__main__': 

    dividend = int(input())
    divisor = int(input())
    
    divideByZeroError(dividend,divisor)
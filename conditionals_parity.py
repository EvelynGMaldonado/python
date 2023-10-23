
#PARITY --> helps us to determine if a number is even (a number exactly divided by 2 with no reminder ~ 0) or odd.
x = int(input("what's x? "))

if x % 2 == 0:
    print("the number you've entered is even")
else:
    print("the number you've entered is an odd number")


#CREATE A BUILT-IN FUNCTION THAT DETERMINES IF A NUMBER IS EVEN OR ODD 
def main(): # a) defining the main function
    # b) creating the x variable to store the number to be reviewed.
    x = int(input("what is the number you want to check? "))

    # c) calling any needed functions into my main() functions, using conditionals if needed.
        #creating a conditional "if" to determine if a number is even or odd by implementing the is_even() boolean function
    if is_even(x): # calling is_even function into my main function having the value stored in the variable x as parameter to run the is_even function
        print("the inputed number is even") #statement to be printed if is_even() boolean function returns True 
    else:
        print("the inputed number is an odd number") #statement to be printed if is_even() boolean function returns False 


# d) defining the functions called into my main() function
def is_even(numb_check): # defining is_even BOOLEAN Function, having numb_check as the parameter taken by the function
    if numb_check % 2 == 0:
        return True
    else:
        return False

main() # a) calling my main function at the end of the file

    #OR
def main(): # a) defining the main function
    # b) creating the x variable to store the number to be reviewed.
    x = int(input("what is the number you want to check? "))

    # c) calling any needed functions into my main() functions, using conditionals if needed.
        #creating a conditional "if" to determine if a number is even or odd by implementing the is_even() boolean function
    if is_even(x): # calling is_even function into my main function having the value stored in the variable x as parameter to run the is_even function
        print("the inputed number is even") #statement to be printed if is_even() boolean function returns True 
    else:
        print("the inputed number is an odd number") #statement to be printed if is_even() boolean function returns False 


# d) defining the functions called into my main() function
def is_even(numb_check): # defining is_even BOOLEAN Function, having numb_check as the parameter taken by the function
    return True if numb_check % 2 == 0 else False

main() # a) calling my main function at the end of the file

    #OR
def main(): # a) defining the main function
    # b) creating the x variable to store the number to be reviewed.
    x = int(input("what is the number you want to check? "))

    # c) calling any needed functions into my main() functions, using conditionals if needed.
        #creating a conditional "if" to determine if a number is even or odd by implementing the is_even() boolean function
    if is_even(x): # calling is_even function into my main function having the value stored in the variable x as parameter to run the is_even function
        print("the inputed number is even") #statement to be printed if is_even() boolean function returns True 
    else:
        print("the inputed number is an odd number") #statement to be printed if is_even() boolean function returns False 


# d) defining the functions called into my main() function
def is_even(numb_check): # defining is_even BOOLEAN Function, having numb_check as the parameter taken by the function
    return (numb_check % 2 == 0) #since it is a boolean function, if numb_check % 2 == 0, it will return true, otherwise, it will return false

main() # a) calling my main function at the end of the file
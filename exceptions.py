#EXCEPTIONS means that something has gone wrong in our program
#Keywords: try & except & else

#SyntaxError -->

#Runtime Error -->

#NameError -->

# EXAMPLE: 1 - ValueError --> TRY to convert the user's input to an int, EXCEPT if sometung goes wrong.
try: # tells python to try to do something 
    x = int(input("What is x? "))
    print(f"x is {x}")
except ValueError: #tells python what do I want to do in exceptional cases: when the input from the user is not a number.
    print("x is not an integer, please enter a number")

# EXAMPLE: 2 - NameError --> we are doing something with the name of the variable that we shouldn't and gives us a NameError saying name x is not defined
try: # tells python to try to do something 
    x = int(input("What is x? "))
    print(f"x is {x}")
except ValueError: #tells python what do I want to do in exceptional cases: when the input from the user is not a number.
    print(f"{x} is not an integer, please enter a number")

    #OR
try: # tells python to try to do something 
    x = int(input("What is x? "))
except ValueError: #tells python what do I want to do in exceptional cases: when the input from the user is not a number.
    print("x is not an integer, please enter a number")

print(f"x is {x}")

    #The FIX for the NameError is using the KEYWORD: ELSE
try: # tells python to try to do something 
    x = int(input("What is x? "))
except ValueError: #tells python what do I want to do in exceptional cases: when the input from the user is not a number.
    print("x is not an integer, please enter a number")
else: #when the exception/error is not happending then we print the integer inputed by the user
    print(f"x is {x}")

    #OR
    #FIX the NameError using: WHILE TRUE, TRY, EXCEPT, ELSE, BREAK
while True: #inducing infinite loop
    try: # tells python to try to do something 
        x = int(input("What is x? "))
    except ValueError: #tells python what do I want to do in exceptional cases: when the input from the user is not a number.
        print("x is not an integer, please enter a number")
    else:
        break #when there is no value error happening then I get out of the loop/ stop requesting the user to enter a number
print(f"x is {x}")

    #OR
    #FIX the NameError using: WHILE TRUE, TRY, EXCEPT, BREAK
while True: #inducing infinite loop
    try: # tells python to try to do something 
        x = int(input("What is x? "))
        break #when there is no value error happening then I get out of the loop/ stop requesting the user to enter a number
    except ValueError: #tells python what do I want to do in exceptional cases: when the input from the user is not a number.
        print("x is not an integer, please enter a number")
        
print(f"x is {x}")

    #OR
    #FIX the NameError having our own function and using: WHILE TRUE, TRY, EXCEPT, ELSE, BREAK, RETURN
def main():
    x = get_int()
    print(f"x is {x}") 

def get_int():
    while True: #inducing infinite loop
        try: # tells python to try to do something 
            x = int(input("What is x? "))
        except ValueError: #tells python what do I want to do in exceptional cases: when the input from the user is not a number.
            print("x is not an integer, please enter a number")
        else:
            break #when there is no value error happening then I get out of the loop/ stop requesting the user to enter a number
    return x #we need to return a value when inventing our own functions

main()
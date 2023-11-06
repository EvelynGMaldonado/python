def main():
    x = get_int("What's x? ") #
    print(f"x is {x}") 

def get_int(prompt): #
    while True: #inducing infinite loop
        try: # tells python to try to do something 
            x = int(input(prompt)) #
            return x #we need to return a value when inventing our own functions
        except ValueError: #tells python what do I want to do in exceptional cases: when the input from the user is not a number.
            print("x is not an integer, please enter a number")

main()
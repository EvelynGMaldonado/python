# FUNCTION: print()
print("hello, world") #say hello world

# FUNCTION: input()
print("what's your name? ") #ask user for its name
input() #blink cursor waiting for the user to input its name
print("hello, inputed_name") #trying to print the user's inputed name after the word hello
    # or
input("what's your name? ") #ask user for its name and blink cursor waiting for the user to input its name
print("hello, inputed_name") #trying to print the user's inputed name after the word hello

# VARIABLES TO RETURN VALUES
name = input("what's your name? ") #ask user for its name and blink cursor waiting for the user to input its name
print("Hello, " + name) #print the user's inputed name after the word Hello using + to separate arguments ~ CONCATENATION OF STRINGS
    # or
name = input("what's your name? ") #ask user for its name and blink cursor waiting for the user to input its name
print("Hello,", name) #print the user's inputed name after the word Hello using , to separate arguments
    # or
name = input("what's your name? ") #ask user for its name and blink cursor waiting for the user to input its name
print("Hello, ", end="") #print the word Hello using , to separate arguments and overriding the default value of end='\n' to end=""
print(name) #print the user's inputed name after the word Hello 
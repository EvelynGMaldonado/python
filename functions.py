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
print(f"Hello, {name}") #using format string (letter f at the beggining of the string, before the first quote mark) with no space withing f and ", advices python to format the statement in a speacial way to return the value name that has to be written within curly braces: {name}. 
    # or
name = input("what's your name? ") #ask user for its name and blink cursor waiting for the user to input its name
print("Hello, ", end="") #print the word Hello using comma to separate arguments and overriding the default value of end='\n' to end=""
print(name) #print the user's inputed name after the word Hello 
    # or
name = input("what's your name? ") #ask user for its name and blink cursor waiting for the user to input its name
print("Hello, ", sep="*") #print the word Hello using comma to separate arguments and overriding the default value of sep=' ' to sep="*"
print(name) #print the user's inputed name after the word Hello 
    # or
name = input("what's your name? ") #ask user for its name and blink cursor waiting for the user to input its name
print("Hello, ", name, sep="*") #print the word Hello using comma to separate arguments, then print the user's inputed name after the word Hello adding a comma after it for it to be separate from the sep parameter, we are also overriding the default value of sep=' ' to sep="*"

#USING QUOTES WHEN PRINTING A STRING STATEMENT
print('Hello, "friend"') #use single quotes for the string and double quotes for what I want to print double quoted.
print("Hello, \"friend\"") #adding back slashes in front of our double inner quotes for the computer to realize that those inner quotes are not quotes to start and finish the thought, but they are literal quotes.


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

# FUNCTION: int()
x = input("what's x? ") # the user input, even if loooks like a number it is a string
y = input("what's y? ") # the user input, even if loooks like a number it is a string
z = int(x) + int(y) # int() converts a string to an integer
print(z)
    #or
x = int(input("what's x? "))
y = int(input("what's y? "))
print(x + y)
    #or
print(int(input("what's x? ")) + int(input("what's y? ")))

#FUNCTION float()
x = float(input("what's x? ")) #user string input is converted to a number with a decimal point
y = float(input("what's y? "))
print(x + y)

#FUNCTION round()
x = float(input("what's x? ")) #user string input is converted to a number with a decimal point
y = float(input("what's y? "))
z = round(x + y)
print(z)
    #or
x = float(input("what's x? ")) #user string input is converted to a number with a decimal point
y = float(input("what's y? "))
z = round(x + y)
print(f"{z:,}") #it is a helper to separate every 3 digits by a comma

#FUNCTION return 
def main():
    x = int(input("what's x? "))
    print("x squared is", square(x))

def square(number):
    return number * number

main()
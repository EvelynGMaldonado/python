name = input("what's your name? ") # ask user for their name and store it in VARIABLE "name"
name = name.strip().title() # remove white space from str and capitalize every first letter of the provided user's name
first, last = name.split(" ") #creating first variable and last variable to store the smaller strings, use .split(" ") to split one string into two smaller strings by space
print(f"Hello, {first}")
print(f"Welcome, {last}")
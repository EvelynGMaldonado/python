
# DATATYPE: .strip() --> removes the white space to the left and right from the str
name = input("what's your name? ") # ask user for their name and store it in VARIABLE "name"
name = name.strip()
print(f"Hello, {name}") # personilized greeting to the user, using its inputed name as a RETURNED VALUE

# DATATYPE: .capitalize() --> capitalizes only the first letter of the str
name = input("what's your name? ") # ask user for their name and store it in VARIABLE "name"
name = name.capitalize()
print(f"Hello, {name}") # personilized greeting to the user, using its inputed name as a RETURNED VALUE

# DATATYPE: .title() --> capitalizes the first letter from each word of the str
name = input("what's your name? ") # ask user for their name and store it in VARIABLE "name"
name = name.title() 
print(f"Hello, {name}") # personilized greeting to the user, using its inputed name as a RETURNED VALUE

# DATATYPE: .split() --> splits one string into multiple smaller strings
name = input("what's your name? ") # ask user for their name and store it in VARIABLE "name"
name = name.strip().title() # remove white space from str and capitalize every first letter of the provided user's name
first, last = name.split(" ") #creating first variable and last variable to store the smaller strings, use .split(" ") to split one string into two smaller strings by space
print(f"Hello, {first}")
print(f"Welcome, {last}")

# USING MORE THAN ONE DATATYPE AT THE TIME
# DATATYPES: .strip() and .title()
name = input("what's your name? ") # ask user for their name and store it in VARIABLE "name"
name = name.strip().title() # remove white space from str and capitalize every first letter of the provided user's name
print(f"Hello, {name}") # personilized greeting to the user, using its inputed name as a RETURNED VALUE
    #or
name = input("what's your name? ").strip().title() # ask user for their name and store it in VARIABLE "name" and remove white space from str and capitalize every first letter of the provided user's name
print(f"Hello, {name}") # personilized greeting to the user, using its inputed name as a RETURNED VALUE
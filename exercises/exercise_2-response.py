
# MATCH --> is similar to "switch" in other programming languages
#Prompt the user for its name, and based on the answer, the program will tell them the house their known to be on the Harry Potter's world.
name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("who?")

    #OR
name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("who?")

    #OR
#using the MATCH and CASE technique
name = input("What's your name? ")
match name:
    case "Harry": 
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who? ")

    #OR
name = input("What's your name? ")
match name:
    case "Harry" | "Hermione" | "Ron": 
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who? ")
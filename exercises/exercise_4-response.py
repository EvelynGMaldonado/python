#LOOP --> Create a Infinite Loop that says "meow" depending on the number inputed by the user
    #Ask the user how many times a cat should "meow", and based on its response, the program will "meow" the desired number of times.
    #The user must give a positive value

while True:
    n = int(input('How many times do you want the cat to "meow" ? ')) # 1 create the variable
    if n < 0: #conditional to accept only positive numbers
        continue #repeat the question if n < 0
    else:
        for _ in range(n):
            print("meow")
        break


    #OR
while True:
    n = int(input('How many times do you want the cat to "meow" ? ')) # 1 create the variable
    if n > 0: #conditional to accept only positive numbers
        break
for _ in range(n):
    print("meow")


    #OR
# DEFINE A MAIN FUNCTION CALLED MEOW() THAT ASKS A USER HOW MANY TIMES A CAT SHOULD "MEOW", ACCEPTS ONLY POSSITIVE VALUES, AND PRINTS THE WORD "MEOW" THE DESIRED NUMBER OF TIMES
def main(): #defining the main function
    meow() #calling the meow() function

def meow(): #defining the meow() function
    while True:
        n = int(input('How many times do you want the cat to "meow" ? ')) #creating the variable
        if n < 0:
            continue
        else:
            for _ in range(n):
                print("meo0ow")
            break

main()


    #OR
def main(): #defining the main function
    meow() #calling the meow() function

def meow(): #defining the meow() function
    while True:
        n = int(input('How many times do you want the cat to "meow" ? ')) #creating the variable
        if n < 0:
            continue
        else:
            positive_meow(n)
            break

def positive_meow(positiveNumber):
    for _ in range(positiveNumber):
        print("meooow")

main()


    #OR
def main(): #defining the main function
    meow() #calling the meow() function

def meow(): #defining the meow() function
    get_number() #callig the get_number method

def get_number():
    while True:
        n = int(input('How many times do you want the cat to "meow" ? ')) #creating the variable
        if n < 0:
            continue
        else:
            positive_meow(n)
            return n

def positive_meow(n):
    for _ in range(n):
        print("meooowww")

main()
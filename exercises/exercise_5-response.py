#MARIO BROSS GAME
# 1 - Define a main function that is able to print a column of 3 hash (#)
def main():
    print_column(3)

def print_column(heigh):
    for _ in range(heigh):
        print("#")

main()

    #OR
def main():
    print_column(3)

def print_column(heigh):
    print("#\n" * heigh, end="")

main()

# 2 - Define a main function that is able to print a row of 4 question marks (?)
def main():
    print_row(4)

def print_row(width): #needs to be fixed!!!!
    for _ in range(width):
        print("?", end="")

main()

    #OR
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()

# 3 - Implement a 3 * 3 grid using reusable code
def main():
    print_square(3) #the width and high are 3

def print_square(size):
    for i in range(size): #for each row in the square
        for j in range(size): #for each spot in the row
            print("#", end="") #prints a hash sign
        print() #we print an empty line at the end of the grid
    
main()

    #OR
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)

main()

    #OR
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()
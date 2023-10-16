
name = input("what's your name? ")
print(name)


#def is utilized to define/create a new function
#EXAMPLE 1
def hello():
    print("Hello!")

hello()

#EXAMPLE 2
def hello1(param1):
    print("Hello1, " + param1)

hello1(name)
    #or
def hello2(param2):
    print("Hello2,", param2)

hello2(name)

#FILE ORGANIZATION
def main():
    name = input("type your name: ").strip()
    helloFunction(name)
    helloFunction()

def helloFunction(param3 = "world"):
    print("Hello, " + param3)

main()

#EXAMPLE 3 : #FUNCTION return 
def main():
    x = int(input("what's x? "))
    print("x squared is", square(x))

def square(number):
    return number * number

main()
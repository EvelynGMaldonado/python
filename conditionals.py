
#create two variables
x = int(input("what's x? "))
y = int(input("what's y? "))

#create conditional: BOOLEAN EXPRESSION ~ question that has a yes or no answer / true or false answer
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

    #OR

#create conditional: BOOLEAN EXPRESSION POTENTIALLY MUTUALLY EXCLUSIVELY using the keyword: elif
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

        #OR

#create conditional: BOOLEAN EXPRESSION POTENTIALLY MUTUALLY EXCLUSIVELY using the keyword: else
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

            #OR

#create conditional: BOOLEAN EXPRESSION POTENTIALLY MUTUALLY EXCLUSIVELY using the keyword: or
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

    #OR

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")



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

#create conditional: BOOLEAN EXPRESSION POTENTIALLY MUTUALLY EXCLUSIVELY using the keyword: and, if, elif, else
score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score <= 90:
    print("Grade: B")
elif score >= 70 and score <= 80:
    print("Grade: C")
elif score >= 60 and score <= 70:
    print("Grade: D")
else:
    print("Grade: F")

    #OR
if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score <= 90:
    print("Grade: B")
elif 70 <= score <= 80:
    print("Grade: C")
elif 60 <= score <= 70:
    print("Grade: D")
else:
    print("Grade: F")
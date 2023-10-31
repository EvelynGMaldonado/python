#List of strings
students = ["Hermione", "Harry", "Ron"]

#printing all the names from the students variable
students = ["Hermione", "Harry", "Ron"]
print(students) 

#printing the student name by index from the students variable
students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])

#printing all the names contained in the students variable as a vertical list 
#ITERATING USING: FOR LOOP --> STRINGS
students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)

    #OR
#ITERATING USING: FOR LOOP --> INDEX(i), NUMBERS, RANGE, and LEN
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)): #obtaining the lenght of the students list & passing it as the argument in the range function
    print(students[i]) #printing the name of every student 

    #OR
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)): #obtaining the lenght of the students list & passing it as the argument in the range function
    print(i, students[i]) #printing the name of every student and its index allocation number

    #OR
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)): #obtaining the lenght of the students list & passing it as the argument in the range function
    print(i + 1, students[i]) #printing the name of every student and its allocation number starting from 1


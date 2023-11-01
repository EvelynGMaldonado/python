#DICTIONARIES(dict): Associating two lists, using curly brackets that contain key: value
students_classroom = {
    "Evelyn": "Group A",
    "Wendy": "Group A",
    "Luz": "Group A",
    "Bulmaro": "Group B",
    "Justin": "Group C",
}

#Pring the classroom associated to each student
students_classroom = {
    "Evelyn": "Group A",
    "Wendy": "Group A",
    "Luz": "Group A",
    "Bulmaro": "Group B",
    "Justin": "Group C",
}

print(students_classroom["Evelyn"])
print(students_classroom["Wendy"])
print(students_classroom["Luz"])
print(students_classroom["Bulmaro"])
print(students_classroom["Justin"])

#Print all the keys contained in the students dictionary
students_classroom = {
    "Evelyn": "Group A",
    "Wendy": "Group A",
    "Luz": "Group A",
    "Bulmaro": "Group B",
    "Justin": "Group C",
}

for student in students_classroom:
    print(student)

#Use the key to index into the dictionary, and return the student name and the classroom the student belongs to
students_classroom = {
    "Evelyn": "Group A",
    "Wendy": "Group A",
    "Luz": "Group A",
    "Bulmaro": "Group B",
    "Justin": "Group C",
}

for student in students_classroom:
    print(student, students_classroom[student], sep=", ")

#LIST OF DICTIONARIES: We have a list of students, and each student is a dictionary.
students = [
    {"name": "Evelyn", "group": "Group A", "grade": "First"},
    {"name": "Wendy", "group": "Group B", "grade": "Second"},
    {"name": "Luz", "group": "Group C", "grade": "Third"},
    {"name": "Bulmaro", "group": "Group C", "grade": None},
    {"name": "Justin", "group": "Group A", "grade": None}
]

for student in students: #we are iterating over the list of students dictionaries'
    print(student["name"]) #printing the value of the current students name key
    print(student["name"], student["group"], sep=", ") #print the value of the name, and group keys
    print(student["name"], student["group"], student["grade"], sep=", ") #printing the value of every key of every dictionary

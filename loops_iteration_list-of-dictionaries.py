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

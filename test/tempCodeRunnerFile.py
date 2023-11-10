unformatted_studentID  = input("Enter a nine digit number: ")

if len(unformatted_studentID ) == 9 and unformatted_studentID.isdigit():
    uStudentID_to_string = str(unformatted_studentID)
    #print(unformatted_studentID)

    #create 3 substrings from uStudentID_to_string which now has 11 characters and 11 indexes: ea "123456789"
    sstring1 = uStudentID_to_string[:3]
    print(sstring1)
    
    sstring2 = uStudentID_to_string[3:5]
    print(sstring2)

    sstring3 = uStudentID_to_string[5:]
    print(sstring3)

    #print("-".join([sstring1, sstring2, sstring3]))

    studentID_final = "-".join([sstring1, sstring2, sstring3])
    print(studentID_final)
else:
    print("You must enter a 9 digits number")
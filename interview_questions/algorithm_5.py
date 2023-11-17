'''

Seasons

Write a program that takes a date as input and outputs the date's season in the northern hemisphere. The input is a string to represent the month and an int to represent the day.

Ex: 
If the input is:
    April
    11
the output is:
    Spring

*In addition, check if the string and int are valid (an actual month and day).

Ex: 
If the input is:
    Blue
    65
the output is:
    Invalid 

The dates for each season in the northern hemisphere are:
Spring: March 20 - June 20
Summer: June 21 - September 21
Autumn: September 22 - December 20
Winter: December 21 - March 19

'''

try:
    
    input_month = str(input("Please enter a month: "))
    input_day = int(input("Please enter a number for the day of the selected month: "))
    month_lower = input_month.lower().strip()

    days_31 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    days_30 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    days_29 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

    if month_lower == "january" and input_day in days_31:
        print("Winter")
    elif month_lower == "february" and input_day in days_29:
        print("Winter")
    elif month_lower == "march" and 19 >= input_day >= 1:
        print("Winter")
    elif month_lower == "march" and 31 >= input_day >= 20:
        print("Spring")
    elif month_lower == "april" and input_day in days_30:
        print("Spring")
    elif month_lower == "may" and input_day in days_31:
        print("Spring")
    elif month_lower == "june" and 20 >= input_day >= 1:
        print("Spring")
    elif month_lower == "june" and 30 >= input_day >= 21:
        print("Summer")
    elif month_lower == "july" and input_day in days_31:
        print("Summer")
    elif month_lower == "august" and input_day in days_31:
        print("Summer")
    elif month_lower == "september" and 21 >= input_day >= 1:
        print("Summer")
    elif month_lower == "september" and 30 >= input_day >= 22:
        print("Autum")
    elif month_lower == "october" and input_day in days_31:
        print("Autum")
    elif month_lower == "november" and input_day in days_30:
        print("Autum")
    elif month_lower == "december" and 20 >= input_day >= 1 :
        print("Autum")
    elif month_lower == "december" and 31 >= input_day >= 21 :
        print("Winter")
    else:
        print("Invalid") #Please enter a valid month / number of days for the selected month

except ValueError:
    print("Please enter alpha characters for the month and whole numbers for the day.")

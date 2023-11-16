'''
Create a solution that accepts any three integer inputs representing the base (b1, b2) and height (h) measurements of a trapezoid in meters. 
Output the exact area of the trapezoid in square meters as a float value. 
The exact area of a trapezoid can be calculated by finding the average of the two base measurements, then multiplying by the height measurement.

Trapezoid Area Formula:
    A = [(b1 + b2) / 2] * h


The solution output should be in the format
    Trapezoid area: area_value square meters

Sample Input/Output:
    If the input is
        3
        4
        5
    
    then the expected output is
        Trapezoid area: 17.5 square meters

    Alternatively, if the input is
        3
        5
        7

    then the expected output is
        Trapezoid area: 28.0 square meters

*
Input to program: 
3
4
5
*

'''

#solution accepts three integer values representing base and height measurements of a trapezoid
#first and second integers represent base 1 and base 2; third integer represents height
#solution outputs the trapezoid area in square meters using formula A = ½(b1+b2)h

b1 = int(input("Enter the base 1 measurement in meters: "))
b2 = int(input("Enter the base 2 measurement in meters: "))
h = int(input("Enter the height measurement in meters: "))

area_value = float(((b1 + b2) / 2) * h)

print(f"Trapezoid area: {area_value} square meters")

    #OR
#solution accepts three integer values representing base and height measurements of a trapezoid
#first and second integers represent base 1 and base 2; third integer represents height 
#solution outputs the trapezoid area in square meters using formula A = ½(b1+b2)h


try:
    b1 = int(input("Enter the base 1 measurement in meters: "))
    b2 = int(input("Enter the base 2 measurement in meters: "))
    h = int(input("Enter the height measurement in meters: "))
    
    area_value = float(((b1 + b2) / 2) * h)
    
    print(f"Trapezoid area: {area_value} square meters")
    
except ValueError:
    print("Please enter only whole and positive numbers")
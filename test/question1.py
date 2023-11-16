'''
Create a solution that accepts three integer inputs representing the number of times an employee travels to a job site. 
Output the total distance traveled to two decimal places given the following miles per employee commute to the job site. 
Output the total distance traveled to two decimal places given the following miles per employee commute to the job site:

    Employee A: 15.62 miles
    Employee B: 41.85 miles
    Employee C: 32.67 miles

The solution output should be in the format
    Distance: total_miles_traveled

Sample Input/Output:
    If the input is
        1
        2
        3

    then the expected output is
        Distance: 197.33 miles

*
Input to program: 
1
2
3
*

'''
#Employee A: 15.62 miles
#Employee B: 41.85 miles
#Employee C: 32.67 miles
#solution accepts three integer inputs representing the number of times an employee travels to the job site
#solution outputs "Distance: " followed by the total value to two decimal places

distanceA = 15.62
distanceB = 41.85
distanceC = 32.67

timesA = int(input("Enter number of times: "))
timesB = int(input("Enter number of times: "))
timesC = int(input("Enter number of times: "))

empA = distanceA * timesA
empB = distanceB * timesB
empC = distanceC * timesC

total_miles_traveled = empA + empB + empC

print(f"Distance: {total_miles_traveled} miles")


    #OR

employeeA = 15.62
employeeB = 41.85
employeeC = 32.67

try:
    timesA = int(input("Enter number of times: "))
    timesB = int(input("Enter number of times: "))
    timesC = int(input("Enter number of times: "))
    
    total_miles_A = round((employeeA * timesA), 2)
    total_miles_B = round((employeeB * timesB), 2)
    total_miles_C = round((employeeC * timesC), 2)
    
    total_miles_traveled = total_miles_A + total_miles_B + total_miles_C
    
    print(f"Distance: {total_miles_traveled} miles")
    
except ValueError:
    print("Invalid input. Please enter a valid positive number")
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
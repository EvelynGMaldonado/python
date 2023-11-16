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
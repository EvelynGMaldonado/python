'''
Create a solution that accepts an integer input representing water temperature in degrees Fahrenheit. 

Output a description of the water state based on the following scale:
    If the temperature is below 33° F, the water is “Frozen”.
    If the water is between 33° F and 80° F (including 33), the water is “Cold”.
    If the water is between 80° F and 115° F (including 80), the water is "Warm".
    If the water is between 115° F and 211° (including 115) F, the water is “Hot".
    If the water is greater than or equal to 212° F, the water is “Boiling”.

Additionally, output a safety comment only during the following circumstances:
    If the water is exactly 212° F, the safety comment is "Caution: Hot!"
    If the water temperature is less than 33° F, the safety comment is "Watch out for ice!"

The solution output should be in the format
    water_state
    optional_safety_comment

Sample Input/Output:
    If the input is
        118
    
    then the expected output is
        Hot
    
    Alternatively, if the input is
        32

    then the expected output is
        Frozen
        Watch out for ice!

*
Input to program: 
118
*

'''

#temperature >= 212, water state is "Boiling"
#temperature (115, 211], water state is "Hot"
#temperature [80, 115], water state is "Warm"
#temperature [33, 80), water state is "Cold"
#temperature < 33, water state is "Frozen"
#temperature = 212, safety comment "Caution: Hot!"
#temperature < 33, safety comment "Watch out for ice!"
#solution accepts integer input representing a water temperature
#solution outputs the water state and potential safety comment based on temperature

temperature_value_check = int(input("Please enter temperature value: "))


if temperature_value_check < 33:
    print("Frozen")
    print("Watch out for ice!")
elif 33 <= temperature_value_check < 80:
    print("Cold")
elif 80 <= temperature_value_check < 115:
    print("Warm")
elif 115 <= temperature_value_check < 211:
    print("Hot")
elif temperature_value_check == 212:
    print("Caution: Hot!")
elif temperature_value_check >= 212:
    print("Boiling")
else:
    print("the value is not recognized, please try again")
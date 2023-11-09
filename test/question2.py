'''
Create a solution that accepts an integer input representing any number of ounces. 
Output the converted total number of tons, pounds, and remaining ounces based on the input ounces value. 
There are 16 ounces in a pound and 2,000 pounds in a ton.

The solution output should be in the format
    Tons: value_1
    Pounds: value_2
    Ounces: value_3

Sample Input/Output:
    If the input is
        32035
    
    then the expected output is
        Tons: 1
        Pounds: 2
        Ounces: 3

*
Input to program: 
32035
*

'''
#there are 16 ounces in a pound and 2000 pounds in a ton
#solution accepts an integer value representing any number of ounces
#solution outputs the converted tons, pounds, and ounces represented by the input value of ounces

    #1 ton = 2000 pounds = 32000 ounces
one_ton_to_ounces = 32000

    #1 pound  = 16 ounces
one_pound_to_ounces = 16


enter_ounces = int(input("Enter the number of ounces you want to convert: ")) #32035

remainding_ounces_after_tons = enter_ounces % one_ton_to_ounces #35
total_tons = int((enter_ounces - remainding_ounces_after_tons) / one_ton_to_ounces) # 1

remainding_ounces_after_pounds = remainding_ounces_after_tons % one_pound_to_ounces #3
total_pounds = int((remainding_ounces_after_tons - remainding_ounces_after_pounds) / one_pound_to_ounces) #2

total_ounces = remainding_ounces_after_pounds


print(f"Tons: {total_tons}\nPounds: {total_pounds}\nOunces: {total_ounces}")

'''
Interstate highway numbers

Primary U.S. interstate highways are numbered 1-99. Odd numbers (like the 5 or 95) go north/south, 
and evens (like the 10 or 90) go east/west. 
Auxiliary highways are numbered 100-999, and service the primary highway indicated by the rightmost two digits. 
Thus, I-405 services I-5, and I-290 services I-90. 
Note: 200 is not a valid auxiliary highway because 00 is not a valid primary highway number.

Given a highway number, indicate whether it is a primary or auxiliary highway. If auxiliary, indicate what primary highway it serves. Also indicate if the (primary) highway runs north/south or east/west.

Ex: 
If the input is:
    90
the output is:
    I-90 is primary, going east/west.

Ex: 
If the input is:
    290
the output is:
    I-290 is auxiliary, serving I-90, going east/west.

Ex: 
If the input is:
    0
the output is:
    0 is not a valid interstate highway number. 

Ex: 
If the input is:
    200
the output is:
    200 is not a valid interstate highway number.

'''
#primary highways = 1 to 99
    #odd = N/S
    #even = E/W
#auxiliary highways = 100 to 999
    #last two digits = # of primary highway it servs


try:
    highway_number = int(input("Please enter the highway number: "))
    
    #check if it is a valid interstate highway number
    if highway_number <= 0:
        print(f"{highway_number} is not a valid interstate highway number.")
    elif highway_number > 999:
        print(f"{highway_number} is not a valid interstate highway number.")
    elif 99 >= highway_number >= 1:
        if (highway_number % 2) == 0: 
            #number is even
            print(f"I-{highway_number} is primary, going east/west.") 
        else:
            #number is odd
            print(f"I-{highway_number} is primary, going north/south.") 
    elif 999 >= highway_number >= 100:
        #check if it is a valid interstate highway number
        last_two = int(str(highway_number)[-2:])
        if last_two == 00:
            print(f"{highway_number} is not a valid interstate highway number.")
        else:
            if (last_two % 2) == 0:
                #number is even
                print(f"I-{highway_number} is auxiliary, serving I-{last_two}, going east/west.")
            else:
                #number is odd
                print(f"I-{highway_number} is auxiliary, serving I-{last_two}, going north/south.")
    else:
        print("Something went wrong, please try again.")
except ValueError:
    print("Please enter only the number of the highway, without any letters or other characters.")
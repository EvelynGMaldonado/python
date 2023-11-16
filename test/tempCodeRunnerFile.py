predef_list = [4, -27, 15, 33, -10]

try:
    value_check = int(input("Please enter a number: "))
    
    predef_list.sort()
    
    max_predef_list = predef_list[-1]
    
    print(max_predef_list)
    
    if value_check > max_predef_list:
        print(f"Greater Than Max? True")
    else:
        print(f"Greater Than Max? False")
    
except ValueError:
    print("Please enter whole numbers")
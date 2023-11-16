frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

for i in range (len(frameworks)):
    try:
        i_value = int(input("Enter a number: "))
        
        frameworks_element = frameworks[i_value]
        
        print(frameworks_element)
        
        break
    
    except EOFError:
        pass
    except IndexError:
        print("Error") #The provided number(index) is out of range
    except ValueError:
        print("Please provide whole numbers")
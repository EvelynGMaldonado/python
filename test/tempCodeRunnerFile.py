frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

for i in range (len(frameworks)):
    try:
        i_value = int(input("Enter a number: "))
        print (frameworks[i_value])
        break

    except ValueError:
        print("Error Value.")

    except:
        print('Error') #Error: Index out of range
        break

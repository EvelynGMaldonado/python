various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

try:
    index_value = int(input("Select a number from 0-5: "))
    print(index_value)
    
    element_by_index = various_data_types[index_value]
    print(element_by_index)
    
    data_type = type(element_by_index).__name__
    print(data_type)
    
    print(f"Element {index_value}: {data_type}")
    
except ValueError:
    print("Please enter only numbers")

except IndexError:
    print("Index is out of range, please select a number from 0-5")
'''
Create a solution that accepts a string input representing a grocery store item and an integer input identifying the number of items purchased on a recent visit. 
The following dictionary purchase lists available items as the key with the cost per item as the value.
    purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

Additionally,
    If fewer than ten items are purchased, the price is the full cost per item.
    If between ten and twenty items (inclusive) are purchased, the purchase gets a 5% discount.
    If twenty-one or more items are purchased, the purchase gets a 10% discount.
    Output the chosen item and total cost of the purchase to two decimal places.

The solution output should be in the format
    item_purchased $total_purchase_cost

Sample Input/Output:
    If the input is
        bananas
        12
    
    then the expected output is
        bananas $21.09

    Alternatively, if the input is
        cookies
        144

    then the expected output is
        cookies $585.79

    

*
Input to program: 

*

'''

#cost per item: <10 is full price, 10-20 (inclusive) is 5% discount, and 21+ is 10% discount
#solution accepts a string input representing an item (dictionary key)
#solution accepts an integer input representing the number of items to be purchased
#solution outputs the item and total cost of purchase

purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

try:
    item_name = str(input("Enter the item name: "))
    item_quantity = int(input("Enter the number of items you want to purchase: "))
    item_full_price = purchase[item_name] * item_quantity
    # print(item_full_price)

    if 0 <= item_quantity < 10:
        #item_full_price = purchase[item_name] * item_quantity
        #print(item_full_price)
        item_total_price = round(item_full_price, 2)
        print(f"{item_name} ${item_total_price}")

    elif 10 <= item_quantity <= 20:
        purchase_discount_5 = float(item_full_price * 0.05 )
        #print(purchase_discount_5)
        item_total_price_5 = round((item_full_price - purchase_discount_5), 2)
        print(f"{item_name} ${item_total_price_5}")

    elif item_quantity > 21:
        purchase_discount_10 = float(item_full_price * .10 )
        item_total_price_10 = round((item_full_price - purchase_discount_10), 2)
        print(f"{item_name} ${item_total_price_10}")
        
except ValueError:
    print("Please enter the correct name for item_name, and whole possitive numbers for item_quantity")


    #OR
#cost per item: <10 is full price, 10-20 (inclusive) is 5% discount, and 21+ is 10% discount
#solution accepts a string input representing an item (dictionary key)
#solution accepts an integer input representing the number of items to be purchased
#solution outputs the item and total cost of purchase

purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

try:
    item_name = str(input())
    item_name_lower = item_name.lower().strip()
    find_item = purchase[item_name_lower]
    item_quantity = int(input())
    
    if item_quantity < 0:
        print(f"You must enter positive whole numbers or zero if you bought 0 items of {item_name}")

    elif item_quantity == 0:
        print(f"{item_name_lower} $0.00")

    elif 1 <= item_quantity < 10:
        single_item_price = purchase[item_name_lower]
        full_item_price = float(single_item_price * item_quantity)
        total_purchase_cost = round(full_item_price, 2)
        print(f"{item_name_lower} ${total_purchase_cost}")

    elif 20 >= item_quantity >=10:
        single_item_price = purchase[item_name_lower]
        full_item_price = float(single_item_price * item_quantity)
        purchase_discount = full_item_price *0.05
        total_item_price = full_item_price - purchase_discount
        total_purchase_cost = round(total_item_price, 2)
        print(f"{item_name_lower} ${total_purchase_cost}")

    elif item_quantity > 21:
        single_item_price = purchase[item_name_lower]
        full_item_price = float(single_item_price * item_quantity)
        purchase_discount = full_item_price * 0.10
        total_item_price = full_item_price - purchase_discount
        total_purchase_cost = round(total_item_price, 2)
        print(f"{item_name_lower} ${total_purchase_cost}")
    else:
        print("Something went wrong, please try again.")
except KeyError:
    print(f"{item_name_lower} does not exist. Please try again")
except ValueError:
    print("Please provide alphanumeric for name of the item and whole numbers for quantity of your chose item")
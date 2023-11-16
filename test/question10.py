'''
Create a solution that accepts an integer input identifying how many shares of stock are to be purchased from the Old Town Stock Exchange, followed by an equivalent number of string inputs representing the stock selections. 
The following dictionary stock lists available stock selections as the key with the cost per selection as the value.
    stocks = {'TSLA': 912.86 , 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

Output the total cost of the purchased shares of stock to two decimal places.


The solution output should be in the format
    Total price: $cost_of_stocks

Sample Input/Output:
    If the input is
        3
        SOFI
        AMZN
        LVLU
    
    then the expected output is
        Total price: $150.53

*
Input to program: 
3
SOFI
AMZN
LVLU
*

'''


#solution accepts an integer input representing the number of stock selections
#solution accepts string inputs equivalent to the integer input identifying the stock selections
#solution outputs the total cost of stock as "Total price: $" followed by the total cost to 2 decimal places

stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}


stocks_quantity = int(input("Please enter the total number of stocks that you want to buy: "))
if stocks_quantity >= 1:
    stock_names = []
    stock_prices = []
    for i in range(stocks_quantity):
        stock_name = input(f"Please enter {stocks_quantity} stock selections (1 per line): ")
        stock_name_to_upper = stock_name.upper()
        stock_value = float(stocks[stock_name_to_upper])
        print(stock_value)

        stock_prices.append(stock_value)

        stock_names.append(stock_name)
        socks_list_to_upper = [stock.upper() for stock in stock_names]

    print(stock_prices)
    print(socks_list_to_upper)

    cost_of_stocks = sum(stock_prices)
    print(cost_of_stocks)
    
    print(f"Total price: ${cost_of_stocks}")
else:
    print("Total price: $0.00")



    #OR
#solution accepts an integer input representing the number of stock selections
#solution accepts string inputs equivalent to the integer input identifying the stock selections
#solution outputs the total cost of stock as "Total price: $" followed by the total cost to 2 decimal places

stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

try:
    stock_quantity = int(input("Please enter the total number of stocks that you want to buy: "))
    stock_name_list = []
    stock_price_list =[]
    if stock_quantity >= 1:
        for i in range(stock_quantity):
            try:
                current_stock_name = str(input(f"Please write the name of your {stock_quantity} selected stock(s) (one per line): "))
                current_stock_name_to_upper = current_stock_name.upper()
                
                current_stock_value = float(stocks[current_stock_name_to_upper])
                print(f"Printing current_stock_value: {current_stock_value}")
                
                stock_name_list.append(current_stock_name_to_upper)
                stock_price_list.append(current_stock_value)
                
                
            except ValueError:
                print("Please enter the stock name")
        
        print(f"Printing the stock_name_list: {stock_name_list}")
        print(f"Printing the stock_price_list: {stock_price_list}")
        
        total_stock_price = sum(stock_price_list)
        print(f"Printing the total_stock_price: {total_stock_price}")
        
        cost_of_stocks = round(total_stock_price, 2)
        print(f"Printing the cost_of_stocks: {cost_of_stocks}")
        
        print(f"Total price: ${cost_of_stocks}")
    
    elif stock_quantity == 0:
        print(f"Total price: $0.00")
        
    else:
        print("You must provide whole and positive numbers")
except ValueError:
    print("Please enter whole numbers")
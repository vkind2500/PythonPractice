'''

Here is the general syntax for dictionary comprehension:

{key:value for (key,value) in dict.items() if condition}

'''

# To increase the price of each stock by 2% of following disctionary

stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}

updated_stocks = {key:value*1.02 for key,value in stocks.items()}

print(updated_stocks)

# Using lambda and map

increased_stocks = map(lambda item:(item[0], item[1]*1.02),stocks.items())


# print(dict(increased_stocks))

# To select stocks whose prices are greater than 200

updated_stocks = {key:value for key,value in stocks.items() if value>200}

print(updated_stocks)

# Using lambda and filter()

filtered_stocks = filter(lambda item:item[1]>200,stocks.items())

print(dict(filtered_stocks))







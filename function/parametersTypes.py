'''
To specify default values for parameters, you use the following syntax:

def function_name(param1, param2=value2, param3=value3, ...):

When you call a function and pass an argument to the parameter that has a default value, the function will use that argument instead of the default value.

However, if you don’t pass the argument, the function will use the default value.

Note - To use default parameters, you need to place parameters with the default values after other parameters.
Otherwise, you’ll get a syntax error.

For example, you cannot do something like this:

def function_name(param1=value1, param2, param3): -> This causes a syntax error.'''



'''The greet() function has two parameters: name and message. And the message parameter has a default value of 'Hi'.

The following calls the greet() function and passes the two arguments:'''

def greet(name, message='Hi'):
    return f"{message} {name}"


greeting = greet('John', 'Hello')
print(greeting)

'''Output:

Hello John

The following example calls the greet() function without passing the second argument:'''

def greet(name, message='Hi'):
    return f"{message} {name}"


greeting = greet('John')
print(greeting)


'''Output:

Hi John

Multiple default parameters'''

def greet(name='there', message='Hi'):
    return f"{message} {name}"

greeting = greet()
print(greeting)


'''Output:

Hi there

Introduction to the Python keyword arguments'''

def get_net_price(price, discount):
    return price * (1-discount)

net_price = get_net_price(100, 0.1)
print(net_price)

'''In the get_net_price(100, 0.1) function call, we pass each argument as a positional argument. In other words, we pass the price argument first and the discount argument second.

However, the function call get_net_price(100, 0.1) has a readability issue. Because by looking at that function call only, you don’t know which argument is price and which one is the discount.

To improve the readability, Python introduces the keyword arguments.

The following shows the keyword argument syntax:

fn(parameter1=value1,parameter2=value2)

When you use the keyword arguments, their names that matter, not their positions.

Keyword arguments and default parameters

Suppose that you have the following get_net_price() function that calculates the net price from the selling price, tax, and discount.'''

def get_net_price(price, tax=0.07, discount=0.05):
    return price * (1 + tax - discount)

'''The following calls the get_net_price() function and uses the default values for tax and discount parameters:'''

net_price = get_net_price(100)
print(net_price)

'''Suppose that you want to use the default value for the tax parameter but not discount. The following function call doesn’t work correctly.'''

net_price = get_net_price(100, 0.06)

'''because Python will assign 100 to price and 0.1 to tax, not discount.

To fix this, you must use keyword arguments:'''

net_price = get_net_price(price=100, discount=0.06)
print(net_price)

'''Note - Once you use a keyword argument, you need to use keyword arguments for the remaining parameters.

The following will result in an error because it uses the positional argument after a keyword argument:'''

net_price = get_net_price(100, tax=0.08, 0.06)
Code language: Python (python)

'''Error:

SyntaxError: positional argument follows keyword argument

To fix this, you need to use the keyword argument for the third argument like this:'''

net_price = get_net_price(100, tax=0.08, discount=0.06)
print(net_price)







def greet(name, message='Hi'):
    """function with default parameter message"""
    return f"{message} {name}"

# Calling function with both the arguments
greeting = greet('John', 'Hello')
print(greeting)


def greet(name, message='Hi'):
    """function with default parameter message"""
    return f"{message} {name}"


# Calling function without message argument
greeting = greet('John')
print(greeting)



def greet(name='there', message='Hi'):
    """Multiple default parameters"""
    return f"{message} {name}"

# Calling greet() function without argument
greeting = greet()
print(greeting)


def get_net_price(price, discount):
    """_summary_

    Args:
        price (_type_): _description_
        discount (_type_): _description_

    Returns:
        _type_: _description_
    """
    return price * (1-discount)

net_price = get_net_price(100, 0.1)
print(net_price)


# Calculating net_price using default values of tax and discount
net_price = get_net_price(100)
print(net_price)


# Calculating net_price using default value of tax
net_price = get_net_price(price=100, discount=0.06)
print(net_price)




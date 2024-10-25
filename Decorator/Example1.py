def currency(fn):
    def wrapper(*args,**kwargs):
        result = fn(*args,**kwargs)
        print(f'${result}')
    return wrapper    



def net_price(price, tax):
    """_summary_

    Args:
        price (_type_): _description_
        tax (_type_): _description_

    Returns:
        _type_: _description_
    """    
    return price * (1 + tax)


net_price = currency(net_price)
net_price(100,0.5)

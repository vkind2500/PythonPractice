print(f'import <module_name> example')

import pricing

net_price = pricing.get_net_price(
    price=100,
    tax_rate=0.01
)

print(net_price)

print(f'import <module_name> as new_name example')

import pricing as pp

net_price = pp.get_net_price(
    price=100,
    tax_rate=0.01
)

print(net_price)

print(f'from <module_name> import <name> example')

from pricing import get_net_price

net_price = get_net_price(
    price=100,
    tax_rate=0.01
)

print(net_price)

print(f'from <module_name> import <name> as <new_name>: rename the imported objects example')

from pricing import get_net_price as calculate_net_price

net_price = calculate_net_price(
    price=100,
    tax_rate=0.01
)

print(net_price)

print(f'from <module_name> import * : import all objects from a module')

from pricing import *

net_price = calculate_net_price(
    price=100,
    tax_rate=0.01
)

get_tax_rate = get_tax(price=100,tax_rate=0.6)

print(get_tax_rate)
print(net_price)

'''

Note :-  It’s not a good practice to use import * because if the imported modules have the same object,
the object from the second module will override the first one. The program may not work as we would expect.

'''










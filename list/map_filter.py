"""

The map() function iterates over all elements in a list (or a tuple), applies a function to each, and returns a new iterator of the new elements.

The following shows the basic syntax of the map() function:

iterator = map(fn, list)

In this syntax, fn is the name of the function that will call on each element of the list.

In fact, we can pass any iterable to the map() function, not just a list or tuple.


"""

def double(bonus):
    return 2*bonus

bonuses = [100,200,300]

bonus_iterator = map(double,bonuses)

# Convert iterator to list

print(list(bonus_iterator))

iterator1 = map(double,bonuses)

# Loop over iterator

for bonus in iterator1:
    print(bonus)

# Using lambda Expression

bonusesList = list(map(lambda bonus:bonus*2,bonuses))

print(bonusesList)


# To return a new list where each element is transformed into the proper case:

names = ['david', 'peter', 'jenifer']

new_names = list(map(lambda name:name.capitalize(),names))

print(f'New Names -> {new_names}')

# Calculate the tax amount for each product with a 10% tax and add the tax amount to the third element of each item in the following list.

carts = [('SmartPhone', 400),
         ('Tablet', 450),
         ('Laptop', 700)]


new_carts = list(map(lambda cart:[cart[0],cart[1],cart[1]*0.1] ,carts))

print (new_carts)

'''

Filter List Element

'''

scores = [70, 60, 80, 90, 50]

# To get all elements from the scores list where each element is greater than or equal to 70

print(list(filter(lambda score: score>=70,scores)))

# To get all the countries whose populations are greater than 300 million

countries = [
    ['China', 1394015977],
    ['United States', 329877505],
    ['India', 1326093247],
    ['Indonesia', 267026366],
    ['Bangladesh', 162650853],
    ['Pakistan', 233500636],
    ['Nigeria', 214028302],
    ['Brazil', 21171597],
    ['Russia', 141722205],
    ['Mexico', 128649565]
]

print(list(filter(lambda country:country[-1]>300000000,countries)))

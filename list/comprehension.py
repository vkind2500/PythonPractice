'''

Syntax : [output_expression for element in list if condition]

where condition is optional predicate

'''


# To get a list of squares based on this numbers list

numbers = [1, 2, 3, 4, 5]

squares = [n*n for n in numbers]

print(squares)

""" This can be achived also using map and lambda as below :- """

print(list(map(lambda n:n*n,numbers)))

# To get a list of mountains where the height is greater than 8600 meters

mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kanchendzonga', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]


print([m for m in mountains if m[1]>8600])

# Using filter and lambda

print(list(filter(lambda m : m[1]>8600,mountains)))


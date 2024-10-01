from functools import reduce

'''

Python offers a function called reduce() that allows you to reduce a list in a more concise way.

Here is the syntax of the reduce() function:

** Unlike the map() and filter() functions, the reduce() isn’t a built-in function in Python.
** In fact, the reduce() function belongs to the functools module.

'''

# The following illustrates how to use the reduce() function to calculate the sum of elements of the scores list:

def sum(a, b):
    print(f"a={a}, b={b}, {a} + {b} ={a+b}")
    return a + b

scores = [75, 65, 80, 95, 50]

total = reduce(sum,scores)

print(total)

# Using lambda

total1 = reduce(lambda a,b:a+b,scores)

print(total1)




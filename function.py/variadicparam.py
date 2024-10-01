"""

When a function has a parameter preceded by an asterisk (*), it can accept a variable number of arguments
and we can pass zero, one, or more arguments to the *args parameter.

In Python, the parameters like *args are called variadic parameters.
Functions that have variadic parameters are called variadic functions.

Note that we don’t need to name args for a variadic parameter.
For example, you can use any meaningful names like *numbers, *strings, *lists, etc.

However, by convention, Python uses the *args for a variadic parameter.


"""

def add(*args):
    print(args)
    print(type(args))


add()

# Output
# ()
# <class 'tuple'>


def sum1(*args):
    total = 0
    for i in args:
        total = total + i
    return total

print(sum1(1,2,3))

# If we use the *args argument, you cannot add more positional arguments. However, we can use keyword arguments.

# The following example results in an error because it uses a positional argument after the *arg argument:

def add(x, y, *args, z):
    return x + y + sum(args) + z


# add(10, 20, 30, 40, 50) will throw TypeError

# To fix it, we need to use a keyword argument after the *args argument as follows:

def add2(x, y, *args, z):
    return x + y + sum(args) + z


print(add2(10, 20, 30, 40, z=50))

# Unpacking arguments

'''

The following point function accepts two arguments &
returns a string representation of a point with x-coordinate and y-coordinate:

'''

def point(x, y):
    return f'({x},{y})'


# If we pass a tuple to the point function, we’ll get an error:

a = (0, 0)

# origin = point(a) will throw TypeError: point() missing 1 required positional argument: 'y'


# To fix this, we need to prefix the tuple a with the operator * like this:


a = (0, 0)
origin = point(*a)
print(origin)



'''

1)   Python lambda expressions allow you to define anonymous functions.
2)   Anonymous functions are functions without names.
3)   The anonymous functions are useful when you need to use them once.
4)   A lambda expression typically contains one or more arguments, but it can have only one expression.

Syntax:

lambda parameters:expression

It is equivalent to below function

def anonymous(parameters):
    return expression


'''


# Functions that accept a function example

def get_full_name(first_name,last_name,formatter):
    """
    The get_full_name() function accepts three arguments:

    First name (first_name)
    Last name (last_name)
    A function that will format the full name (formatter).

    """
    return formatter(first_name,last_name)

"""The following defines two functions that return a full name from the first name and last name in different formats:"""

def first_last(first_name,last_name):
    return f'{first_name} {last_name}'

def last_first(first_name,last_name):
    return f'{last_name} {first_name}'

"""And this shows you how to call the get_full_name() function by passing the first name, last name, and first_last / last_first functions:"""

full_name =  get_full_name("Lalit","Chauhan",first_last) # return first_name Last_name

print(full_name)

full_name =  get_full_name("Lalit","Chauhan",last_first) # return Last_name first_name

print(full_name)

""" Instead of defining first_last and last_first, we can use lambda expression as below"""

print("============ Using Lambda Expression =============")

full_name =  get_full_name("Lalit","Chauhan",lambda first_name,last_name:f'{first_name} {last_name}') # return first_name Last_name

print(full_name)

full_name =  get_full_name("Lalit","Chauhan",lambda first_name,last_name:f'{last_name} {first_name}')

print(full_name)

# Functions that return a function example

""" The following times() function returns a function which is a lambda expression: """

def times(n):
    return lambda x:n*x

# Call times function

double = times(3)

# Since the times() function returns a function, the double is also a function. To call it, we place parentheses like this:

print(double(2))

# lambda in a loop

callables = []

for i in [1,2,3]:
    callables.append(lambda :  i)

for f in callables:
    print(f())

"""

 The expected output will be:

    1
    2
    3

However, the program shows the following output:

    3
    3
    3

The problem is that all the there lambda expressions reference the i variable, not the current value of i.
When we call the lambda expressions, the value of the variable i is 3.

To fix this, you need to bind the i variable to each lambda expression at the time the lambda expression is created.
One way to do it is to use the default argument:

"""

print("After Fixing")

callables = []

for i in [1,2,3]:
    callables.append(lambda i=i:  i)

for f in callables:
    print(f())

"""

How the Fix Works

-> Default Argument:

    lambda i=i: i creates a lambda function with a default argument i set to the current value of i in the loop.
    This means that the value of i at the time the lambda is created is stored in the default argument.

-> Capturing the Value:

    Each lambda function now has its own i parameter with a default value that was the value of i at the time of creation.
    When the lambda function is called, it uses this default value.

-> Final Result:

    Each lambda function retains the value of i at the time it was added to the callables list.
    Therefore, calling each lambda returns 1, 2, and 3 respectively.

* First Iteration (i = 1):

lambda i=i: i becomes lambda i=1: i.
This lambda captures i=1 as its default argument.

* Second Iteration (i = 2):

lambda i=i: i becomes lambda i=2: i.
This lambda captures i=2 as its default argument.

* Third Iteration (i = 3):

lambda i=i: i becomes lambda i=3: i.
This lambda captures i=3 as its default argument.

* Calling the Lambdas:

When f() is called, it uses the default value of i that was captured.
Thus, the outputs are 1, 2, and 3.

Summary
=======

Original Issue: The lambdas captured the variable i, not its value at the time of creation. Since i was 3 after the loop, all lambdas returned 3.

Fix: Using a default argument in the lambda function captures the value of i at the time of creation, resulting in the expected outputs 1, 2, and 3.

"""






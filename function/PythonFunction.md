# User Defined Function

Here’s a simple function that shows a greeting:

```python
def greet():
    """ Display a greeting to users """
    print('Hi')
```

A function definition starts with the ``def`` keyword and the name of the function (``greet``).

The function definition always ends in a colon ``:``.

All the indented lines that follow the function definition make up the **function’s body**.

### Passing information to Python functions

```python
def greet(name):
    print(f"Hi {name}")
```

The ``name`` is called a **function parameter** or simply a **parameter**.

When you call a function with a parameter, we need to pass the information.
The value that you pass into a function is called an **argument**. 

```python
greet('John') # John is an argument
```

**Output:**

``Hi John``

### Parameters vs. Arguments

A parameter is a piece of information that a function needs. And you specify the parameter in the function definition. For example, the ``greet()`` function has a parameter called ``name``.

An argument is a piece of data that you pass into the function. For example, the text string ``'John'`` is the function argument.

### Returning a value

A function can perform a task like the ``greet()`` function. Or it can return a value. The value that a function returns is called a return value.

To return a value from a function, you use the ``return`` statement inside the function body.


```python

def greet(name):
    return f"Hi {name}"

greeting = greet('John')
print(greeting) # Hi John    

```

### Python functions with multiple parameters

A function can have zero, one, or multiple parameters.

The following example defines a function called ``sum()`` that calculates the sum of two numbers:

```python
def sum(a, b):
    return a + b


total = sum(10,20)
print(total) # 30
```

### Introduction to the help() function

Python provides a built-in function called ``help()`` that allows us to show the documentation of a function.

The following example shows the documentation of the ``print()`` function:

```
help(print)
```

**Output:**

```
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

>> Note that we can use the ``help()`` function to show the documentation of **modules, classes, functions, and keywords**. 

### Using docstrings to document functions

To document your functions, we can use docstrings. 
When the first line in the function body is a string, Python will interpret it as a docstring. For example:

```python
def add(a, b):
    """ Add two arguments
    Arguments:
        a: an integer
        b: an integer
    Returns:
        The sum of the two arguments"""
    return a + b
```

And we can use the ``help()`` function to find the documentation of the ``add()`` function:

```
help(add)
```

**Output:**

```
add(a, b)
    Add the two arguments
    Arguments:
            a: an integer
            b: an integer
        Returns:
            The sum of the two arguments        
```

Python stores the docstrings in the ``__doc__`` property of the function.

The following example shows how to access the ``__doc__`` property of the ``add()`` function:

```
add.__doc__
```

### Introduction to Python default parameters

To specify default values for parameters, we use the following syntax:

```
def function_name(param1, param2=value2, param3=value3, ...):
```

When we call a function and pass an argument to the parameter that has a default value, the function will use that argument instead of the default value.

To use default parameters, we need to place parameters with the default values after other parameters. Otherwise, we’ll get a syntax error.

```
def function_name(param1=value1, param2, param3):
```

The following example defines the ``greet()`` function that returns a greeting message:

```python
def greet(name, message='Hi'):
    return f"{message} {name}"

# Here we pass the second argument to the greet() function, the function uses the argument instead of the default value
greeting1 = greet('John', 'Hello')

# Here we didn't pass the second argument to the greet() function, the function uses the default value
greeting2 = greet('John')

print(greeting1) # Hello John 
print(greeting2) # Hi John
```

### Multiple default parameters

The following redefines the ``greet()`` function with the two parameters that have default values:

```python
def greet(name='there', message='Hi'):
    return f"{message} {name}"

# Here, we call greet function without passing any argument(s).
greeting = greet()
print(greeting) # Hi there

```

### Introduction to the Python keyword arguments


Suppose that we want the greet() function to return a greeting like Hello there. 
We may come up with the following function call:

```python
def greet(name='there', message='Hi'):
    return f"{message} {name}"


greeting = greet('Hello')
print(greeting)
```

Unfortuntely, it returns an unexpected value:

**Output:**

```
Hi Hello
```

Because when we pass the 'Hello' argument, the greet() function treats it as the first argument, not the second one.

To resolve this, we need to call the greet() function using keyword arguments like this:

```python
def greet(name='there', message='Hi'):
    return f"{message} {name}"


greeting = greet(message='Hello')
print(greeting) # Hello there
```

By using the keyword argument syntax, we don’t need to specify the arguments in the same order as defined in the function.

When we use the keyword arguments, their names that matter, not their positions.

Suppose that we have the following ``get_net_price()`` function that calculates the net price from the selling price, tax, and discount.

```python
def get_net_price(price, tax=0.07, discount=0.05):
    return price * (1 + tax - discount)
```

Suppose that we want to use the default value for the tax parameter but not discount. The following function call doesn’t work correctly.

```python
net_price = get_net_price(100, 0.06)
```
… because Python will assign ``100`` to price and ``0.6`` to tax, not discount.

To fix this, we must use keyword arguments:

```python
net_price = get_net_price(price=100, discount=0.06)
print(net_price) # 101.0
```

> Disclaimer : Once we use a keyword argument, we need to use keyword arguments for the remaining parameters.

```python
"""The following will result in an error because it uses the positional argument after a keyword argument:"""
net_price = get_net_price(100, tax=0.08, 0.06)
```

#### [Example Code of function](function.py)

## Lambda Expressions

1)   Python lambda expressions allow us to define anonymous functions.
2)   Anonymous functions are functions without names.
3)   The anonymous functions are useful when we need to use them once.
4)   A lambda expression typically contains one or more arguments, but it can have only one expression.

**Syntax:**

``lambda parameters:expression``

It is equivalent to below function

```python
def anonymous(parameters):
    return expression
```

#### Case 1 : Functions that accept a function example

The following defines a function called ``get_full_name()`` that format the full name from the first name and last name:

```python
def get_full_name(first_name,last_name,formatter):
    return formatter(first_name,last_name)
```

The following defines two functions that return a full name from the first name and last name in different formats:

```python
def first_last(first_name, last_name):
    return f"{first_name} {last_name}"


def last_first(first_name, last_name):
    return f"{last_name}, {first_name}"
    
```

Let's see how to call the ``get_full_name()`` function by passing the first name, last name, and ``first_last`` / ``last_first`` functions:

```python
full_name = get_full_name('John', 'Doe', first_last)
print(full_name) # John Doe

full_name = get_full_name('John', 'Doe', last_first)
print(full_name) #  Doe, John
```

Instead of defining the ``first_last`` and ``last_first`` functions, we can use lambda expressions.

```python

lambda first_name,last_name: f"{first_name} {last_name}" # lambda expression for first_last name 

lambda first_name, last_name: f"{last_name} {first_name}" # lambda expression for last_first name 

```

#### [Complete Example Code](lambda1.py)


#### Case 2 : Functions that return a function example

The following ``times()`` function returns a function which is a lambda expression:

```python
def times(n):
    return lambda x:n*x

double = times(3)
print(double(2)) # 6
```
#### [Example Code: Function that returns function](lambda2.py)

### Python lambda in a loop

See the following example:

```python
callables = []
for i in (1, 2, 3):
    callables.append(lambda: i)

for f in callables:
    print(f())
```

How it works.

-   First, define a list with the name callables.
-   Second, iterate from 1 to 3, create a new lambda expression in each iteration, and add it to the callables list.
-   Third, loop over the callables and call each function.

**The expected output will be:**

```
1
2
3
```
**However, the program shows the following output:**

```
3
3
3
```

#### Why?

The problem is that all the there lambda expressions reference the i variable, not the current value of i and when we call the lambda expressions, the value of the variable i is 3.

#### How to fix?

To fix this, we need to bind the i variable to each lambda expression at the time the lambda expression is created using **default argument**.

```python
callables = []
for i in (1, 2, 3):
    callables.append(lambda a=i: a)

for f in callables:
    print(f())
```

#### How the Fix Works

-   **Default Argument**

    ``lambda i=i: i`` creates a lambda function with a default argument i set to the current value of i in the loop.
    This means that the value of i at the time the lambda is created is stored in the default argument.

-   **Capturing the Value**

    Each lambda function now has its own i parameter with a default value that was the value of i at the time of creation.
    When the lambda function is called, it uses this default value.

-   **Final Result**

    Each lambda function retains the value of i at the time it was added to the callables list.
    Therefore, calling each lambda returns 1, 2, and 3 respectively.

**First Iteration (i = 1):**

``lambda i=i: i`` becomes ``lambda i=1: i``.
This lambda captures i=1 as its default argument.

**Second Iteration (i = 2):**

``lambda i=i: i`` becomes ``lambda i=2: i``.
This lambda captures i=2 as its default argument.

**Third Iteration (i = 3):**

``lambda i=i: i`` becomes ``lambda i=3: i``.
This lambda captures i=3 as its default argument.






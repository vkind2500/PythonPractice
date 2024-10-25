# Python Decorators

A decorator is essentially a function that takes another function as an argument, adds some kind of functionality to it, and returns a new function.

### A simple Python decorator example

The following defines a ``net_price`` function which calculates the net price from selling price and tax and returns the ``net_price`` as a number.

```python
def net_price(price, tax):
    """ calculate the net price from price and tax
    Arguments:
        price: the selling price
        tax: value added tax or sale tax
    Return
        the net price
    """
    return price * (1 + tax)

```

Suppose that we need to format the net price using the USD currency without changing the current implementation of ``net_price``. To do it, we can use a ``decorator``.

The following defines ``currency`` decorator :

```python
def currency(fn):
    def wrapper(*args,**kwargs):
        result = fn(*args,**kwargs)
        return f'${result}'
    return wrapper    
```

The ``currency`` function returns the ``wrapper`` function. The ``wrapper`` function has the ``*args`` and ``**kwargs`` parameters.

These parameters allow us to call any ``fn`` function with any combination of ``positional`` and ``keyword-only`` arguments.

In this example, the ``wrapper`` function essentially executes the ``fn`` function directly and doesn’t change any behavior of the ``fn`` function.

#### How to use currency decorator

To use the currency decorator, we need to pass the ``net_price`` function to it to get a new function and execute the new function as if it were the original function. For example:

```python
net_price = currency(net_price)
print(net_price(100,0.5))
```

**Put it all togther**

```python
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
net_price(100,0.5) # $150.0

```

[Full Example Code](Example1.py)

Generally, if ``decorate`` is a decorator function and we want to decorate another function ``fn``, we can use this syntax:

```
fn = decorate(fn)
```

To make it more convenient, Python provides a shorter way like this:

```
@decorate
def fn():
    pass
```

For example, instead of using the following syntax :- 

```python
net_price = currency(net_price)
```

...we can decorate the ``net_price`` function using the ``@currency`` as follows:

```python
@currency
def net_price(price, tax):
    """ calculate the net price from price and tax
    Arguments:
        price: the selling price
        tax: value added tax or sale tax
    Return
        the net price
    """
    return price * (1 + tax)
```

### Introspecting decorated functions

When you write ``@decorator`` above a function definition, Under the hood, Python replaces my_function with decorator(my_function).

Here’s a concrete example to see it in action:

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorator is running")
        result = func(*args, **kwargs)
        print("Decorator finished")
        return result
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
```

The @decorator syntax tells Python to replace ``say_hello`` with the result of ``decorator(say_hello)``. Hence ``say_hello()`` becomes ``decorator(say_hello)()``.

``decorator(say_hello)`` now pointing to wrapper, which wraps the original functionality with extra code and ``decorator(say_hello)()`` calls the wrapper function.

### ``wraps`` function from functools

When we define a wrapper function, the original function loose it's metadata such as name, docstring, and other attributes.

**Example**

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call.")
        result = func(*args, **kwargs)
        print("After the function call.")
        return result
    return wrapper

@my_decorator
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

# Calling the decorated function
print(greet("Alice"))

# Checking the name and docstring of the decorated function
print(greet.__name__)  # Outputs: wrapper (not what we want)
print(greet.__doc__)   # Outputs: None (lost the docstring)
help(net_price) # wrapper(*args, **kwargs)
```

To fix this, we can use the ``wraps`` function from the functools standard module. In fact, the wraps function is also a ``decorator``.

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # This preserves the metadata of func
    def wrapper(*args, **kwargs):
        print("Before the function call.")
        result = func(*args, **kwargs)
        print("After the function call.")
        return result
    return wrapper

@my_decorator
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

# Calling the decorated function
print(greet("Alice"))

# Checking the name and docstring of the decorated function
print(greet.__name__)  # Outputs: greet
print(greet.__doc__)   # Outputs: Return a greeting message.
help(greet) # Return a greeting message.
```

#### [Full Example Code](Example2.py)


## Decorator with Arguments

Decorators with arguments in Python allow one to pass parameters to your decorators, enhancing their functionality. 

***Example of a Decorator with Arguments***

Suppose that we have a function called ``say`` that prints out a message and we want to execute the ``say()`` function 5 times repeatedly each time we call it. For example:

```python
def say(message):
    ''' print the message 
    Arguments
        message: the message to show
    '''
    print(message)

say('Hi')    
```
**Output**

```
Hi
Hi
Hi
Hi
Hi
```

To do that , we can define the ``repeat_5_times`` decorator as follows:

```python
def repeat_5_times(fn):
    @wraps
    def wrapper(*args,**kwargs):
        for i in range(5):
            fn(*args,**kwargs)
    return wrapper        
``` 

Since ``i`` is not used inside for loop, we can replace ``i`` with ``_``.Hence, we can write ``repeat_5_times`` decorator as follows :-

```python
def repeat_5_times(fn):
    @wraps
    def wrapper(*args,**kwargs):
        for _ in range(5):
            fn(*args,**kwargs)
    return wrapper        
``` 

Sum it all together :

```python
from functools import wraps

def repeat_5_times(fn):
    """_summary_

    Args:
        fn (function): _description_

    Returns:
        _type_: _description_
    """    
    @wraps  
    def wrapper(*args,**kwargs):       
        for _ in range(5):
            fn(*args,**kwargs)
    return wrapper      


@repeat_5_times
def say(message):
    ''' print the message 
    Arguments
        message: the message to show
    '''
    print(message)
    
say('Hi')    
```

**Output**

```
Hi
Hi
Hi
Hi
Hi
```

### [Full Example Code](Example3.py)

What if we want to execute the ``say()`` function repeatedly ten times. In this case, we need to change the hard-coded value 5 in the repeat decorator.However, this solution isn’t flexible.

To fix this, we need to change the repeat decorator so that it accepts an argument that specifies the number of times a function should execute like this:

```
@repeat(5)
def say(message):
    ...
```

To define the ``repeat`` decorator, the repeat(5) should return the original decorator.

```python
def repeat(times):
    # return the original "repeat" decorator
```

The new ``repeat`` function returns a ``decorator``. And it’s often referred to as a **decorator factory**.

The following ``repeat`` function returns a decorator:

```python
def repeat(times):
    ''' call a function a number of times '''
    def decorate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = fn(*args, **kwargs)
            return result
        return wrapper
    return decorate

```

***Note that the new repeat function isn’t a decorator. It’s a decorator factory that returns a decorator.***

Put it all together.

```python
from functools import wraps

def repeat(times):
    """_summary_

    Args:
        times (_type_): _description_
    """    
    def decorate(fn):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                fn(*args, **kwargs)
        return wrapper
    return decorate        

@repeat(10)
def say(message):
    ''' print the message 
    Arguments
        message: the message to show
    '''
    print(message)
    
say('Hi')   
```

#### [Full Example Code](Example4.py)

Under the hood, python replaces `say()` with ``repeat(10)(say)('Hi')``. If we see carefully,``repeat(10)`` return ``decorate`` function  referencing to value 10 and ``repeat(10)(say)`` return ``wrapper`` function which executes ``say`` function for the argument ``Hi`` for 10 times.

>Here ``decorate``and ``wrapper`` both are closures.

## Class Decorators

A Python class decorator is simply a class that implements the ``__call__`` method, allowing an instance of the class to be used as a decorator.

For example, the following ``star`` function prints out a number of * characters before and after calling the decorated function:

```python
def star(n):
    def decorate(fn):
        def wrapper(*args, **kwargs):
            print(n*'*')
            result = fn(*args, **kwargs)
            print(result)
            print(n*'*')
            return result
        return wrapper
    return decorate
```

The ``star`` is a **decorator factory** that returns a decorator. It accepts an argument that specifies the number of * characters to display.

The following illustrates how to use the star decorator factory:

```python
@star(5)
def add(a, b):
    return a + b


add(10, 20)
```

**Output**

```
*****
30
*****
```

The ``star()`` decorator factory takes an argument and returns a decorator function which is **callable**. 

The **callable** takes an argument ``fn`` which is a function that will be decorated.

A class instance can be a callable when it implements the ``__call__`` method. Therefore, we can make the ``__call__`` method as a decorator.

The following example rewrites the ``star`` decorator factory using a class instead:

```python
class Star:
    def __init__(self, n):
        self.n = n

    def __call__(self, fn):
        def wrapper(*args, **kwargs):
            print(self.n*'*')
            result = fn(*args, **kwargs)
            print(result)
            print(self.n*'*')
            return result
        return wrapper
```

And we can use the ``Star`` class as a decorator like this:

```python
@Star(5)
def add(a, b):
    return a + b
```

The ``@Star(5)`` returns an instance of the ``Star`` class. That instance is a callable, so under the hood Python replaces ``add(10,20)`` with ``Star(5)(add)(10,20)``

Put it all together:

from functools import wraps

```python
class Star:
    def __init__(self, n):
        self.n = n

    def __call__(self, fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(self.n*'*')
            result = fn(*args, **kwargs)
            print(result)
            print(self.n*'*')
            return result
        return wrapper


@Star(5)
def add(a, b):
    return a + b


add(10, 20)

```

Put it all together :

```python
class Star:
    def __init__(self,n):
        self.n = n

    def __call__(self, fn):
        def wrapper(*args,**kwargs):
            print(self.n*'*')
            print(fn(*args,**kwargs))
            print(self.n*'*')
        return wrapper    

@Star(5)
def add(a,b):
    return a+b

add(10,9)
```

**Output**

```
*****
19
*****
```

### [Full Example Code](Example5.py)

**key Consideration**

-   Use callable classes as decorators by implementing the ``__call__`` method.
-   Pass the decorator arguments to the ``__init__`` method.
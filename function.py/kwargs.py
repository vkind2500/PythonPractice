"""

In Python, a function can have a parameter preceded by two stars (**).

For example: **kwwargs

The **kwargs is called a keyword parameter.

When a function has the **kwargs parameter, it can accept a variable number of keyword arguments as a dictionary.

The two stars (**) are important.

However, the name kwargs is by convention. Therefore, you can use any other meaningful names such as **configs and **files.

"""

def connect(**kwargs):
    print(kwargs)

connect(server='localhost', port=3306, user='root', password='Py1hon!Xt')

# However to pass a dictionary to the function, we need to add two stars (**) to the argument like this:


config = {'server': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'Py1thon!Xt12'}

connect(**config)

# If we execute connect(config) it will give Type Error : 0 positional arguments

# If a function has the **kwargs parameter and other parameters, we need to place the **kwargs after other parameters.

# Using both *args and **kwargs arguments

def fn(*args, **kwargs):
    print(args)
    print(kwargs)

fn(1, 2, x=10, y=20)

# Output:

'''
(1, 2)
{'x': 10, 'y': 20}
'''





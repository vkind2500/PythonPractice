# Python ``__name__``

When we import a module, Python executes the file associated with the module.

Often, we want to write a script that can be executed directly or imported as a module. The ``__name__`` variable allows us to do that.

The ``__name__`` is a special variable in Python. It’s special because Python assigns a different value to it, depending on how the script executes containing ``__name__`` executes.


``__name__`` variable has double underscores at both sides, hence it’s called dunder name.



When we run the script directly, Python sets the ``__name__`` variable to ``'__main__'``.

However, if we import a file as a module, Python sets the **module name** to the ``__name__`` variable.



Let's we have **billing.py** containing two functions ``calculate_tax()`` & ``print_billing_doc()``.

In addition, it has a statement that prints out the ``__name__``  variable value to the screen:


```python
def calculate_tax(price, tax):
    return price * tax


def print_billing_doc():
    tax_rate = 0.1
    products = [{'name': 'Book',  'price': 30},
                {'name': 'Pen', 'price': 5}]

    # print billing header
    print(f'Name\tPrice\tTax')

    # print the billing item
    for product in products:
        tax = calculate_tax(product['price'], tax_rate)
        print(f"{product['name']}\t{product['price']}\t{tax}")


print(__name__)
```

Now we import the **billing** module into **app.py** as follows:

```python
import billing

```

When we execute the **app.py**, ``print(__name__)`` in **billing.py** prints the value ->  ***'billing'***

However if we execute **billing.py**, ``print(__name__)`` in **billing.py** prints the value ``'__main__'``.

Therefore, the __name__ variable allows us to check when the file is executed directly or imported as a module.

#### [Example Code of app.py](app.py) and [billing.py](billing.py)
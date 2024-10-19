# Python ``__str__``

Let’s start with the ``Person`` class:

```python
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
```

The ``Person`` class has three instance attributes including ``first_name``, ``last_name``, and ``age``.

The following creates a new instance of the ``Person`` class and display it:

```python
person = Person('John', 'Doe', 25)
print(person)
```

**Output:**

```
<__main__.Person object at 0x0000023CA16D13A0>
```

When we use the print() function to display the instance of the Person class, the print() function shows the memory address of that instance.

To customize the string representation of a class instance, the class needs to implement the ``__str__`` magic method.

The following illustrates how to implement the ``__str__`` method in the ``Person`` class:

```python
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'Person({self.first_name},{self.last_name},{self.age})'
```

And when we use the ``print()`` function to print out an instance of the ``Person`` class, Python calls the ``__str__`` method defined in the ``Person`` class. For example:

```
person = Person('John', 'Doe', 25)
print(person)
```

**Output:**

```
Person(John,Doe,25)
```

#### Refer : [Example 1](__str__.py)
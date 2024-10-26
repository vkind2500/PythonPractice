# Python ``__init__``

When we create a new object of a class, Python automatically calls the ``__init__()`` method to initialize the object’s attributes.

The ``__init__()`` method has two underscores (__) on each side. Therefore, the ``__init__()`` is often called dunder init. 

The double underscores at both sides of the __init__() method indicate that Python will use the method internally. 

> *In other words, you should not explicitly call this method.*


The following defines the Person class with the ``__init__()`` method:

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    person = Person('John', 25)
    print(f"I'm {person.name}. I'm {person.age} years old.")
```

When we create an instance of the Person class, Python performs two things:

1. Create a new instance of the Person class by setting the object’s namespace such as ``__dict__`` attribute to empty ({}).
2. Call the ``__init__`` method to initialize the attributes of the newly created object.

> *Note that the ``__init__`` method doesn’t create the object but only initializes the object’s attributes. Hence, the ``__init__()`` is not a constructor.*

If the __init__ has parameters other than the self, we need to pass the corresponding arguments when creating a new object like the example above. Otherwise, we’ll get an error.


The ``__init__()`` method’s parameters can have default values. For example:

```
class Person:
    def __init__(self, name, age=22):
        self.name = name
        self.age = age


if __name__ == '__main__':
    person = Person('John')
    print(f"I'm {person.name}. I'm {person.age} years old.")

```    

**Output:**

``
I'm John. I'm 22 years old.
``

#### Example : [Class having ``__init__``](Example3.py)

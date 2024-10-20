## Python ``__eq__`` method

When we compare two objects of a class using ``==``, Python calls the ``__eq__`` method to determine if they are considered equal.

If ``__eq__`` is not defined in a class, By default, Python uses the ``is`` operator inherited from the base object class, which compares objects by their memory addresses (i.e., they are considered equal only if they are the same instance).

```python
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

john = Person('John', 'Doe', 25)
jane = Person('Jane', 'Doe', 25)

print(john is jane)  # False
print(john == jane) # False
```

Since ``john`` and ``jane`` have the same age, you want them to be equal. In other words, you want the following expression to return ``True``:

To do it, we can implement the ``__eq__`` dunder method in the ``Person`` class.

The following shows how to implement the ``__eq__`` method in the ``Person`` class that returns ``True`` if two person objects have the same age:

```python
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other):
        # Check if the 'other' object is an instance of Person
        if isinstance(other, Person):
            return self.age == other.age
        return False

john = Person('John', 'Doe', 25)
jane = Person('Jane', 'Doe', 25)
mary = Person('Mary', 'Doe', 27) 

print(john == mary)  # False
print(john == john)  # True
print(john == 20) # False
```


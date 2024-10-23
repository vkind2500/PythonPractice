# Python ``__bool__``

An object of a custom class is associated with a boolean value. By default, it evaluates to ``True``. 

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    person = Person('John', 25)

print(bool(person))  #True    
```

To override this default behavior, we implement the ``__bool__`` special method. The ``__bool__`` method must return a boolean value, True or False.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __bool__(self):
        if self.age < 18 or self.age > 65:
            return False
        return True



person1 = Person('Jane', 16)
person2 = Person('Bob',44)

print(bool(person))  # False
print(bool(person)) # True
```

## The ``__len__`` method

-   If a custom class doesn’t have the ``__bool__`` method, Python will look for the ``__len__``() method. 

-   If the ``__len__`` is zero, the object is ``False``. Otherwise, it’s ``True``.

-   If a class doesn’t implement the ``__bool__`` and ``__len__`` methods, the objects of the class will evaluate to ``True``.

```python
class Payroll:
    def __init__(self, length):
        self.length = length

    def __len__(self):
        print('len was called...')
        return self.length


if __name__ == '__main__':
    payroll = Payroll(0)
    print(bool(payroll))  # False

    payroll.length = 10
    print(bool(payroll))  # True
```
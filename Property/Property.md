# Python Property

The following defines a ``Person`` class that has two attributes ``name`` and ``age``, and create a new instance of the ``Person`` class:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


john = Person('John', 18)
```

Since ``age`` is the instance attribute of the Person class, we can assign it a new value like this:

```
john.age = -1
```

Above assignment is technically valid but it is semantically incorrect to assign -1 as ``age`` to ``john``.

To ensure that the age is not zero or negative,we can add check for ``age`` before assignemnt as follows:

```python
age = -1 
if age <= 0 :
    raise ValueError('Age cannot be Zero or Negative')
else:
    john.age = age    
```

Though it is correct but we need to do this every time before assigning a value to ``age`` attribute which is repititive and difficult to maintain.

To avoid this repetition, we can define a pair of methods called getter and setter.


## Getter and setter

The getter and setter methods provide an interface for accessing an instance attribute:

-   The getter returns the value of an attribute
-   The setter sets a new value for an attribute


The following shows the new ``Person`` class with a ``getter`` and ``setter`` for the ``age`` attribute:

```python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.self_age(age)

    def set_age(self,age):
        if age <= 0 :
            raise ValueError('The age must be positive')
        else :
            self._age = age
    def get_age(self):
        return self._age

```

By convention the getter and setter have the following name: ``get_<attribute>()`` and ``set_<attribute>()``.

>**Note:** We made age attribute [private](<../Classes and Objects/Encapsulation.md>) by appending ``_`` to it. To know more about private attributes.

The above code works just fine but it has backward compatibility issues.

Imageine we are using ``Person`` class for a while and other developers have beenn already using it. And now we add the getter and setter, all the code that directly accessed or modified ``age`` will break because it expects a public attribute ``age``

To define a ``getter`` and ``setter`` method while achieving backward compatibility, we can use the ``property()`` class.

### The Python property class

The property class returns a ``property`` object. 

The ``property()`` class has the following syntax:

``property(fget=None, fset=None, fdel=None, doc=None)``

The ``property()`` has the following parameters:

-   fget is a function to get the value of the attribute, or the getter method.
-   fset is a function to set the value of the attribute, or the setter method.
-   fdel is a function to delete the attribute.
-   oc is a docstring i.e., a comment.

The following uses the ``property()`` function to define the ``age`` property for the ``Person`` class.


```python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.self_age(age)

    def set_age(self,age):
        if age <= 0 :
            raise ValueError('The age must be positive')
        else :
            self._age = age
    def get_age(self):
        return self._age

    age = property(set_age,get_age)       

```

In the ``Person`` class, we create a new property object by calling the ``property()`` and assign the property object to the ``age`` attribute. 

When we assign a value to the age object:

```python
john.age = 19
```

Python will call the function assigned to the ``fset`` argument, which is the ``set_age()``.

Similarly, when we read from the ``age`` property object, Python will execute the function assigned to the ``fget`` argument, which is the ``get_age()`` method.

By using the ``property()`` class, we can add a property to a class while maintaining backward compatibility. 

>Note that the ``age`` is a class attribute, not an instance attribute.
>
>The ``Person.__dict__`` stores the class attributes of the Person class. 
>
>The following shows the contents of the ``Person.__dict__``:
>
>```python
>mappingproxy({'__dict__': <attribute '__dict__' of 'Person' >objects>,
>              '__doc__': None,
>              '__init__': <function Person.__init__ at >0x000002242F5B2670>,
>              '__module__': '__main__',
>              '__weakref__': <attribute '__weakref__' of 'Person' >objects>,
>              'age': <property object at 0x000002242EE39180>,
>              'get_age': <function Person.get_age at >0x000002242F5B2790>,
>              'set_age': <function Person.set_age at >0x000002242F5B2700>})
>
>
>When we assign value to ``age`` using statement  ``john.age = >19``,Python looks up the ``age`` attribute in the ``john.>__dict__`` first. Because Python doesn’t find the ``age`` attribute in the ``john.__dict__``, it’ll then find the age attribute in the ``Person.__dict__``.


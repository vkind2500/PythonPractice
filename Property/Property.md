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

## Getting Started With Python’s property()

Here’s the full signature of ``property()``:

```
property([fget=None, fset=None, fdel=None, doc=None])
```

The first two arguments take function objects that will play the role of getter (fget) and setter (fset) methods. Python automatically calls these function objects when you access or mutate the attribute at hand.

The ``property()`` has the following parameters:

-   fget is a function to get the value of the attribute, or the getter method.
-   fset is a function to set the value of the attribute, or the setter method.
-   fdel is a function to delete the attribute.
-   doc is a docstring i.e., a comment.
<br>
<br>
<div style="background-color: #e0f7fa; color: #000; border: 1px solid #ddd; padding: 10px; border-radius: 8px; box-shadow: 2px 2px 8px rgba(0,0,0,0.1);">
  <strong>Note:</strong> The return value of property() is the property object which act as managed attribute itself.
</div>
<br>
<br>

-   If we access the managed attribute with something like ``obj.attr``, then Python automatically calls ``fget()``. 
-   If we assign a new value to the attribute with something like ``obj.attr = value``, then Python calls ``fset()`` using the input value as an argument. 
-   Finally, if we run a ``del obj.attr`` statement, then Python automatically calls ``fdel()``.
<br>
<br>

<div style="background-color: #e0f7fa; color: #000; border: 1px solid #ddd; padding: 10px; border-radius: 8px; box-shadow: 2px 2px 8px rgba(0,0,0,0.1);">
  <strong>Note:</strong> It’s common to refer to property() as a built-in function. However, property is a class with a function-like name. That’s why most Python developers call it a function.
</div>

<br>
<br>

The following uses the ``property()`` function to define the ``age`` property for the ``Person`` class.
<br>

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

#### [Example Code ](Example1.py)


### ``age`` is Class Attribute
---

The ``Person.__dict__`` stores the class attributes of the Person class. 

The following shows the contents of the ``Person.__dict__``:

```python
mappingproxy({'__dict__': <attribute '__dict__' of 'Person' objects>,
              '__doc__': None,
              '__init__': <function Person.__init__ at >0x000002242F5B2670>,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'Person' objects>,
             'age': <property object at 0x000002242EE39180>,
              'get_age': <function Person.get_age at 0x000002242F5B2790>,
             'set_age': <function Person.set_age at 0x000002242F5B2700>})
```

When we assign value to ``age`` using statement  ``john.age = 19``,Python looks up the ``age`` attribute in the ``john.>__dict__`` first. Because Python doesn’t find the ``age`` attribute in the ``john.__dict__``, it’ll then find the age attribute in the ``Person.__dict__``.

## Property Decorator

To define a getter for the ``age`` attribute, we use the property class like this:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def get_age(self):
        return self._age

    age = property(fget=get_age)
```

The ``property`` class accepts a getter and returns a ``property`` object, age.

***This creates an unnecessary redundancy as we can get the ``age`` of a ``Person`` object using either the ``age`` property or the ``get_age()`` method.*** 

To avoid this redundancy, we can rename the ``get_age()`` method to the ``age()`` method like this:

```python

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def age(self):
        return self._age

    age = property(fget=age)
```

The ``property()`` accepts a callable (age) and returns a callable. Therefore, it is a decorator.

> **Remember** the expression **``fn = decorate(fn)``** 
> is equivalent to below syntax :-
>```
>   @decorate
>   def fn():
>       pass   
>```

<br><br>
Therefore, we can use the ``@property`` decorator to decorate the ``age()`` method as follows:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age
```
So by using the ``@property`` decorator, we can simplify the property definition for a class.

### Setter decorators

The following adds a ``setter`` method ``(set_age)`` to assign a value to ``_age`` attribute to the ``Person`` class:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    def set_age(self, value):
        if value <= 0:
            raise ValueError('The age must be positive')
        self._age = value
```        

To assign the ``set_age`` to the ``fset`` of the age property object, we can call the ``setter()`` method of the age property object like the following:

```python
age = age.setter(set_age)
```

The ``age.setter()`` method accepts a callable and returns another callable (a property object). 
<br><br>
Therefore, we can use the decorator ``@age.setter`` for the ``set_age()`` method like this:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def set_age(self, value):
        if value <= 0:
            raise ValueError('The age must be positive')
        self._age = value
```

<div style="background-color: #e0f7fa; color: #000; border: 1px solid #ddd; padding: 10px; border-radius: 8px; box-shadow: 2px 2px 8px rgba(0,0,0,0.1);">
  <strong>Note:</strong> When we decorate the <b>set_age</b> method with <b>@age.setter</b> we create a new property and reassign the class-level name <b>.age</b>
  <br><br>
  This new property contains <b>getter</b> methods of the initial property along with the addition of the new <b>setter</b> method. 
</div>

<br><br>


Now, we can change the ``set_age()`` method to the ``age()`` method and use the ``age`` property in the ``__init__()`` method:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError('The age must be positive')
        self._age = value
```

<br><br>

To summarize, we can use decorators to create a property using the following pattern:

```python
class MyClass:
    def __init__(self, attr):
        self.prop = attr

    @property
    def prop(self):
        return self.__attr

    @prop.setter
    def prop(self, value):
        self.__attr = value

    @prop.deleter
    def prop(self):
        print(f'Delete attr')
        del self.__attr    
```

### Readonly Property

To define a readonly property, we need to create a property with only the getter. However, it is not truly read-only because we can always access the underlying attribute and change it.

The following example defines a class called ``Circle`` that has a ``radius`` attribute and an ``area()`` property:

```python
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2


c = Circle(10)
print(c.area)

```

### Caching properties

Suppose we create a new circle object and access the area property many times. Each time, the area needs to be recalculated, which is not efficient.

To make it more performant, we need to recalculate the area of the circle only when the radius changes. If the radius doesn’t change, we can reuse the previously calculated area.

To do it, we can use the caching technique:

-   First, calculate the area and save it in a cache.
-   Second, if the radius changes, reset the area. Otherwise, return - the area directly from the cache without recalcuation.

The following defines the new ``Circle`` class with cached ``area`` property:

```python
import math


class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('Radius must be positive')

        if value != self._radius:
            self._radius = value
            self._area = None

    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * self.radius ** 2

        return self._area
```

**How it works**

-   First, set the ``_area`` to ``None`` in the ``__init__`` method. The ``_area`` attribute is the cache that stores the calculated ``area``.

-   Second, if the ``radius`` changes (in the setter), reset the ``_area`` to ``None``.

-   Third, define the ``area`` computed property. The ``area`` property returns ``_area`` if it is not ``None``. Otherwise, calculate the ``area``, save it into the ``_area``, and return it.

### Python Delete Property


#### [Full Example Code of Circle Class](Example2.py)

Underhood, the ``@property`` decorator uses the property class that has three methods: ***setter, getter, and deleter***.

By using the deleter, we can delete a property from an object. 
<br><br>
Notice that the ``deleter()`` method deletes a property of an object, not a class.

The following defines the ``Person`` class with the ``name`` property:

```python
from pprint import pprint


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('name cannot be empty')
        self._name = value

    @name.deleter
    def name(self):
        del self._name
```

The following uses the ``del`` keyword to delete the ``name`` property:

```python
del person.name
```

Internally, Python will execute the ``deleter`` method that deletes the ``_name`` attribute from the person object. The ``person.__dict__`` will be empty.

### [Full Example Code](Example3.py)
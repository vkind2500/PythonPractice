# Encapsulation and Private Attributes

Encapsulation refers to the concept of restricting access to certain components of an object and protecting the internal state of an object from being modified accidentally or directly by external code. 

This is one of the fundamental principles of Object-Oriented Programming (OOP). 

Encapsulation is achieved through the use of access modifiers and by defining methods that allow controlled access to the object’s data.

>**Note** : Python doesn’t have a concept of private attributes. In other words, all attributes are accessible from the outside of a class.

As a workaround, Python uses a single underscore (_) or double underscore (__) to indicate that a variable is private or intended to be used internally.

1. **Single underscore (``_``)**: A hint to developers that the variable or method is intended for internal use (though still accessible). This is more of a convention.

2. Double underscore (``__``) : If we prefix an attribute name with double underscores (__) like ``__attribute``, Python will automatically change the name of the ``__attribute`` to ``_class__attribute`` which makes the variable harder to access from outside the class, effectively making it private. **This is called the name mangling in Python**.

However, we still can access it using the ``_class__attribute`` name

#### Refer [Example 5](Example5.py)

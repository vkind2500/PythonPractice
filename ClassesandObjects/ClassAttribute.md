# Class Variables

Class variables are bound to the class. They’re shared by all instances of that class. 

The following example adds the extension and version class variables to the ``HtmlDocument`` class:

```
class HtmlDocument:
    extension = 'html'
    version = '5'
```

Both ``extension`` and ``version`` are the class variables of the HtmlDocument class. They’re bound to the HtmlDocument class.

### Get the values of class variables

1. Using Dot Notation
    
    ```
    print(HtmlDocument.extension) # html
    print(HtmlDocument.version) # 5
    ```

#### Note : If we access a class variable that doesn’t exist, we’ll get an AttributeError exception. 

2. Using ``getattr()`` function

    ```
    extension = getattr(HtmlDocument, 'extension')
    version = getattr(HtmlDocument, 'version')

    print(extension)  # html
    print(version)  # 5
    ```

#### Note : If we access a class variable that doesn’t exist, we’ll get an AttributeError exception. To avoid the exception, we can specify a default value if the class variable doesn’t exist like this:

    ```
    media_type = getattr(HtmlDocument, 'media_type', 'text/html')
    print(media_type) # text/html

    ```

### Set values for class variables

To set a value for a class variable, you use the dot notation:

``HtmlDocument.version = 10``

or you can use the setattr() built-in function:

``setattr(HtmlDocument, 'version', 10)``

#### Note : Since Python is a dynamic language, we can add a class variable to a class at runtime after we have created it.

### Delete class variables

To delete a class variable at runtime, you use the delattr() function:

``delattr(HtmlDocument, 'version')``

Or you can use the del keyword:

``del HtmlDocument.version``

### Class variable storage

Python stores class variables in the ``__dict__`` attribute.

```
from pprint import pprint


class HtmlDocument:
    extension = 'html'
    version = '5'


HtmlDocument.media_type = 'text/html'

pprint(HtmlDocument.__dict__)
```
#### Output:

```
mappingproxy({'__dict__': <attribute '__dict__' of 'HtmlDocument' objects>,
              '__doc__': None,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'HtmlDocument' objects>,
              'extension': 'html',
              'media_type': 'text/html',
              'version': '5'})
```

As clearly shown in the output, the ``__dict__`` has three class variables: extension, media_type, and version besides other predefined class variables.

### ``__dict__`` is mapping proxy object?

In Python, a mapping proxy is a special type of object that provides a read-only view of a dictionary.

This is useful when we want to expose a dictionary-like interface without allowing the underlying dictionary to be modified.

Hence Python does not allow you to change the ``__dict__`` directly. For example, the following will result in an error:

```
HtmlDocument.__dict__['released'] = 2008

Output:

TypeError: 'mappingproxy' object does not support item assignment
```

However, we can use the setattr() function or dot notation to indirectly change the __dict__ attribute.

### Callable class attributes

An attribute of a class that can be called like a function. This is typically achieved by defining a method within a class or by using a staticmethod or classmethod. 

#### Here are the main ways to create callable class attributes:

1.  Instance Methods
    
    Instance methods are defined within a class and are callable on instances of that class. 

    ```
    class MyClass:
        def instance_method(self):
            return "This is an instance method!"

    obj = MyClass()
    print(obj.instance_method())  # Output: This is an instance method!
    ```
2. Class Methods

    Class methods are defined with the @classmethod decorator. They take the class itself as the first argument (usually named cls) and can be called on the class or its instances.

    ```
    class MyClass:
        @classmethod
        def class_method(cls):
            return "This is a class method!"

    print(MyClass.class_method())  # Output: This is a class method!
    obj = MyClass()
    print(obj.class_method())       # Output: This is a class method!
    ```

3. Static Methods

    Static methods are defined with the @staticmethod decorator. They do not receive an implicit first argument and can be called without needing an instance of the class or the class itself. They are used when the method does not need access to class or instance data.

    ```
    class MyClass:
        @staticmethod
        def static_method():
            return "This is a static method!"

    print(MyClass.static_method())  # Output: This is a static method!
    obj = MyClass()
    print(obj.static_method())       # Output: This is a static method!
    ```

4. Overriding the ``__call__ `` Method

    We can also make an instance of a class callable by implementing the ``__call__`` method in the class. This allows you to create an object that can be called like a function.

    ```
    class CallableClass:
        def __call__(self, *args, **kwargs):
            return f"Called with arguments: {args} and keyword arguments: {kwargs}"

    callable_instance = CallableClass()
    print(callable_instance(1, 2, key='value'))  # Output: Called with arguments: (1, 2) and keyword arguments: {'key': 'value'}

    ```

   ### Refer : [Example 1](Example1.py)

### How Python class attributes work 

When we access an attribute via an instance of the class, Python searches for the attribute in the instance attribute list which is object ``__dict__``. If the instance attribute list doesn’t have that attribute, Python continues looking up the attribute in the class attribute list which is class ``__dict__``. Python returns the value of the attribute as long as it finds the attribute in the instance attribute list or class attribute list.

However, if we access an attribute via Class, Python directly searches for the attribute in the class attribute list - ``__dict__``.

### When to use Python class attributes

1. **Storing class constants** - Since a constant doesn’t change from instance to instance of a class, it’s handy to store it as a class attribute.

For example, the Circle class has the ``pi`` constant that is the same for all instances of the class. Therefore, it’s a good candidate for the class attributes.

2. **Tracking data across of all instances** - The following adds the ``circle_list`` class attribute to the ``Circle`` class. When we create a new instance of the ``Circle`` class, the constructor adds the instance to the list:

```python
class Circle:
    circle_list = []
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius
        # add the instance to the circle list
        self.circle_list.append(self)

    def area(self):
        return self.pi * self.radius**2

    def circumference(self):
        return 2 * self.pi * self.radius


c1 = Circle(10)
c2 = Circle(20)

print(len(Circle.circle_list))  # 2
```

3. **Defining default values** : Sometimes, we want to set a default value for all instances of a class. In this case, we can use a class attribute.

The following example defines a ``Product`` class. All the instances of the ``Product`` class will have a default discount specified by the ``default_discount`` class attribute:

```python
class Product:
    default_discount = 0

    def __init__(self, price):
        self.price = price
        self.discount = Product.default_discount

    def set_discount(self, discount):
        self.discount = discount

    def net_price(self):
        return self.price * (1 - self.discount)


p1 = Product(100)
print(p1.net_price())
 # 100

p2 = Product(200)
p2.set_discount(0.05)
print(p2.net_price())
 # 190
```
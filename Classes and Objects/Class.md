# Python Class

### Objects

An object is a container that contains data and functionality.


#### Objects's State

Since data represents the ``object`` at a particular moment in time. Therefore, the data of an ``object`` is called the state. Python uses attributes to model the state of an ``object``.

#### Object's Behaviour

Python uses functions to model the behaviors. When a function is associated with an object, it becomes a method of the object.


### Define a class

The following example defines a Person class:

```
class Person:
    pass
```

#### Class Naming Convention
 
 Use capitalized names for classes in Python. If the class name contains multiple words, use the CamelCase format, for example SalesEmployee.

##### Note: Since the Person class is incomplete; we need to use the ``pass`` statement to indicate that we’ll add more code to it later.

To create an instance of a class, we use the class name with parentheses like this:

``person = Person()``

When printing out the person object, we’ll see its name and memory address:

```
class Person:
    pass
person = Person()

print(person)
```

#### Output:

```
<__main__.Person object at 0x000001C46D1C47F0>
```

To get an identity of an object, you use the id() function. For example:

```
print(id(person))
```

#### Output:

```
1943155787760
```

The id of an object is unique. In Python, the id() returns the memory address of an object. The hex() function converts the integer returned by the id() function to a lowercase hexadecimal string prefixed with 0x:

```
print(hex(id(person)))

Output:

0x1c46d1c47f0

```
### isinstance()

Returns True if an object is an instance of a class:

print(isinstance(person, Person))  # True

## A class is also an object in Python

Everything in Python is an object, including classes.

When we define the Person class, Python creates an object with the name Person. 

The Person object has attributes. For example, you can find its name using the ``__name__`` attribute:

```
print(Person.__name__)

Output:

Person
```

The ``Person`` object has the type of ``type``:

```
print(type(Person))

Output:

<class 'type'>
```

The Person class also has a behavior. 
For example, it can create a new instance:

``person = Person()``

## Class Variables

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

4. Overriding the __call__ Method

    We can also make an instance of a class callable by implementing the ``__call__`` method in the class. This allows you to create an object that can be called like a function.

    ```
    class CallableClass:
        def __call__(self, *args, **kwargs):
            return f"Called with arguments: {args} and keyword arguments: {kwargs}"

    callable_instance = CallableClass()
    print(callable_instance(1, 2, key='value'))  # Output: Called with arguments: (1, 2) and keyword arguments: {'key': 'value'}

    ```
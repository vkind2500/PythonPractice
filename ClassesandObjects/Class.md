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


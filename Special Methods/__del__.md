# Python ``__del__``

In Python, the garbage collector manages memory automatically. The garbage collector will destroy the objects that are not referenced.

If an object implements the ``__del__`` method, Python calls the ``__del__`` method right before the garbage collector destroys the object.

However, the garbage collector determines when to destroy the object. Therefore, it determines when the ``__del__`` method will be called.


The following defines a Person class with the special ``__del__`` method, create a new instance of the ``Person``, and set it to None:

```python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print('__del__ was called')


if __name__ == '__main__':
    person = Person('John Doe', 23)
    person = None

```

**Output:**

```
__del__ was called
```

When we set the person object to None, the garbage collector destroys it because there is no reference. Therefore, the ``__del__`` method was called.

If we use the ``del`` keyword to delete the person object, the ``__del__`` method is also called:

```python
person = Person('John Doe', 23)
del person
```
**Output:**

```
__del__ was called
```

>**Note:** The del statement itself does not directly call the ``__del__`` method. Instead, del removes a reference to an object. 

## The Python ``__del__`` pitfalls

1. Python calls the ``__del__`` method when all object references are gone.
2. Should not use the ``__del__`` method to clean up the resources. It’s recommended to use the context manager.
3. If the ``__del__`` method itself holds references to other objects, those objects are not automatically destroyed as part of the ``__del__`` method. The other objects will only be destroyed when their reference counts drop to zero.

```python
class A:
    def __del__(self):
        print("A's __del__ called")

class B:
    def __init__(self):
        self.a = A()
    
    def __del__(self):
        print("B's __del__ called")
        # Accessing 'a' in __del__ method
        print("Referencing A object in B's __del__:", self.a)

# Example usage:
b = B()
a = b.a
del b  # This will trigger B's __del__ and then A's __del__


```
**Expected Output:**

```
B's __del__ called
Referencing A object in B's __del__: <__main__.A object at 0x...>  # Memory address of the A instance
```

4. If the ``__del__`` references the global objects, it may create unexpected behaviors.
5. If an exception occurs inside the ``__del__`` method, Python does not raise the exception but keeps it silent.

>**Note:** In some environments (like the interactive Python interpreter), ``__del__`` can indeed be called when a script finishes or when the last reference to an object is deleted after the script terminates, because Python cleans up any remaining objects at the end of a program’s execution.

**Example**

```python
class B:
    def __del__(self):
        print("B's __del__ called")

b = B()  # Create an instance of B

```
**Output:**

```
B's __del__ called
```


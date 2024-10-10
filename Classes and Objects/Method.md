# Introduction to the Python methods

A method is a function that is bound to an instance of a class. Let's see how it works under the hood.

The following defines a Request class that contains a function ``send()``:

```
class Request:
    def send():
        print('Sent')
```

And if we call the ``send()`` function via the Request class like this:

```
Request.send() # Sent
```

Here ``send()`` is a function object, which is an instance of the function class and to verify this, we'll the check the output of below statement:

```
print(Request.send) 
```

Output:

```
# <function Request.send at 0x00000276F9E00310>
```

and if we verify the type of send using type function , we'll get <<span style="color:blue;">class</span> <span style="color:red;">'function'</span>>

```
print(type(Request.send)) # <class 'function'>
```

Let's creates a new instance of the Request class:

```
http_request = Request()
```

If we display the ``http_request.send``, it’ll return a bound method object:

```
print(http_request.send)
```

**Output:**

```
<bound method Request.send of <__main__.Request object at 0x00000104B6C3D580>>

```

So the ``http_request.send`` is not a function like ``Request.send``

which proves that if we define a function inside a class, it’s purely a function. However, when we access that function via an object, the function becomes a method.

Notice, if we call a ``send()`` function via ``http_request`` instance, we'll get a ``TypeError ``

*"TypeError: send() takes 0 positional arguments but 1 was given"*

> **Reason** : Because the ``http_request.send`` is a method that is bound to the ``http_request`` object, Python always implicitly passes the object to the method as the first argument.

The following redefines the ``Request`` class where the ``send`` function accepts a list of arguments:

```
class Request:
    def send(*args):
        print('Sent', args)
```

If we calls the send function from the Request class:

```
Request.send()
```

**Output:**

```
Sent ()
```

The ``send()`` function doesn’t receive any arguments.

However, if we call the send() function from an instance of the Request class, the args is not empty:

```
print(hex(id(http_request)))
http_request.send()
```

**Output:**

```
0x1ee3a74d580
Sent (<__main__.Request object at 0x000001374AF4D580>,)
```

>**Notice** : The ``http_request`` object is the same as the one Python passes to the ``send()`` method as the first argument because they have the same memory address.
and by convention, it is called self:


Hence we should redefines the ``Request`` class as:

```
class Request:
    def send(self):
        print('Sent', self)
```        





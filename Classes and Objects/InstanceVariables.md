# Python Instance Variables


The following defines a HtmlDocument class with two class variables:

```
from pprint import pprint


class HtmlDocument:
    version = 5
    extension = 'html'


pprint(HtmlDocument.__dict__)

print(HtmlDocument.extension)
print(HtmlDocument.version)
```

**Output:**

```
mappingproxy({'__dict__': <attribute '__dict__' of 'HtmlDocument' objects>,
              '__doc__': None,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'HtmlDocument' objects>,
              'extension': 'html',
              'version': 5})
```

The ``HtmlDocument`` class has two class variables: ``extension`` and ``version``. Python stores these two variables in the ``__dict__ `` attribute.

When we access the class variables via the class, Python looks them up in the ``__dict__``  of the class.

The following creates a new instance of the ``HtmlDocument`` class:

```
home = HtmlDocument()
```

The home is an instance of the ``HtmlDocument`` class. It has its own ``__dict__`` attribute:

```
print(home.__dict__)
```

**Output:**

```
{}
```

### Difference between Class and Instance ``__dict__``

<table border="2" cellpadding="5" cellspacing="0">
  <tr>
    <th>Class ``__dict__``</th>
    <th>Instance ``__dict__``</th>
  </tr>
  <tr>
    <td>mapping proxy object</td>
    <td>dictionary</td>
  </tr>
  <tr>
    <td>Immutable</td>
    <td>Mutable</td>
  </tr>
</table>


### Can we access class variables from instance of class?

Yes, Python allows you to access the class variables from an instance of a class.

```
print(home.extension)
print(home.version)

```

In this case, Python looks up the variables ``extension`` and ``version`` in ``home.__dict__`` first. If it doesn’t find them there, it’ll go up to the class and look up in the ``HtmlDocument.__dict__``.

However, if Python can find the variables in the ``__dict__`` of the instance, it won’t look further in the ``__dict__`` of the class.

The following defines the ``version`` variable in the home object:

```
home.version = 6
```

Python adds the version variable to the ``__dict__`` attribute of the ``home`` object:

```
print(home.__dict__)
```
The ``__dict__`` now contains one instance variable:

```
{'version': 6}
```

In practice, we initialize instance variables for all instances of a class in the __init__ method.

For example, the following redefines the ``HtmlDocument`` class that has two instance variables ``name`` and ``contents``

```
class HtmlDocument:
    version = 5
    extension = 'html'

    def __init__(self, name, contents):
        self.name = name
        self.contents = contents
```

When creating a new instance of the HtmlDocument, we need to pass the corresponding arguments like this:

```
blank = HtmlDocument('Blank', 'test')
```

#### Refer : [Example 4](Example4.py)
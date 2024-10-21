# Python ``__hash__``

The **hash()** function accepts an object and returns the hash value as an integer. 

When we pass an object to the hash() function, Python will execute the ``__hash__`` special method of the object.

The following examples shows how to retrive hash value of an object:-

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('John', 22)
p2 = Person('Jane', 22)

print(hash(p1)) # 110373112736
print(hash(p2)) # 110373572343

```

It means that when we pass the **p1** object to the **hash()** function, Python will call the ``__hash__`` method of the **p1** object.

### What happen if only ``__eq__`` method is overrided 

-   When a class overrides the ``__eq__`` method, objects of that class can indeed become *unhashable*. 

-   This is because Python assumes that the default ``__hash__`` method (inherited from object) is no longer valid because objects that compare as equal should also have the same hash value. 

-   To prevent inconsistencies, Python automatically makes instances of the class unhashable unless you explicitly override ``__hash__`` as well.

- We won't able to store such objects in mapping type such as *Dictionary* and *Set*


The following **Person** class implements the ``__eq__`` method:

```python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return isinstance(other, Person) and self.age == other.age

```

If we attempt to call ``hash(p1)`` or we attempt to use the *Person* object in a set we'll get an error. For example :

```python

p1 = Person('Lalit',34)    
print(hash(p1)) # 
```

**OR**

```
members = {
    Person('John', 22),
    Person('Jane', 22)
}

```
**Output :**
```
TypeError: unhashable type: 'Person'
```


### How to fix it

To make the **Person** class hashable and work well in data structures like dictionaries, we need to do two things:

-   Implement the ``__hash__`` method.
-   The hash of the class should remain immutable. 

**Example:** 

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    def __eq__(self, other):
        return isinstance(other, Person) and self.age == other.age

    def __hash__(self):
        return hash(self.age)
    
    
person1 = Person('Dinesh',24)
person2 = Person('Jane',67)
person3 = Person('Lingam',23)

print(f'Hash of person1 is {hash(person1)}')

member = {person1:'young',person2:'old',person3:'young'}

print(f'member(person1) is {member[person1]}')    
```

**Output**

```
Hash of person1 is 24
member(person1) is young
```
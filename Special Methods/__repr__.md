# Python ``__repr__``

The __repr__ method returns the string representation of an object that ideally is unambiguous and can be used to recreate the object (if possible).


In other words, if we pass the returned string of the ``repr()`` method to the eval() function, we’ll get the a new object having same values as the object_name. 


<details>
  <summary>  Here’s an example to demonstrate that:</summary>

  ```python
  class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

    # Creating an object of the Person class
    p = Person("Alice", 30)

    # Using repr() to get a string representation
    representation = repr(p)
    print(representation)  # Output: Person(name='Alice', age=30)

    # Using eval() to recreate the object from the string representation
    new_p = eval(representation)

    # Checking if the new object has the same values
    print(new_p.name)  # Output: Alice
    print(new_p.age)   # Output: 30
 ```
</details>

#### [Example Code to create object from string representation of object using eval()](Example1.py)  

#### **Key Points:**

1. When a class doesn’t implement the ``__str__`` method and we pass an instance of that class to the ``str()``, Python returns the result of the ``__repr__`` method because internally the ``__str__`` method calls the ``__repr__`` method

    **For example:**

    ```python
    person = Person('John', 'Doe', 25)
    print(person) # Person("John","Doe",25) 
    ```
2. 	If ``__repr__`` is not defined, Python falls back on a default implementation, which is not usually informative (e.g., <Person object at 0x7f04f8>).

3. If a class implements the __str__ method, Python will call the __str__ method when you pass an instance of the class to the str(). 

   <details>
   <summary>  Here’s an example to demonstrate that:</summary>

    ```python
    class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f'Person("{self.first_name}","{self.last_name}",{self.age})'

    def __str__(self):
        return f'({self.first_name},{self.last_name},{self.age})'


    person = Person('John', 'Doe', 25)
    # use str()
    print(person)

    # use repr()
    print(repr(person))
    ```
</details>

#### [Example Code to demonstrate](Example2.py)

#### Difference between ``__repr__`` and ``__str__``

	•	``__repr__``: Focuses on providing an unambiguous, developer-facing representation.
	•	``__str__``: Focuses on a readable, user-facing representation. If __str__ is not defined, Python falls back to __repr__.

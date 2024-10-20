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
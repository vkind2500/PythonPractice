class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other):
        # Check if the 'other' object is an instance of Person
        if isinstance(other, Person):
            return self.age == other.age
        return False

john = Person('John', 'Doe', 25)
jane = Person('Jane', 'Doe', 25)
mary = Person('Mary', 'Doe', 27) 

print(john == mary)  # False
print(john == john)  # True
print(john == 20) # False
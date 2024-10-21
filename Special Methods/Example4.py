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
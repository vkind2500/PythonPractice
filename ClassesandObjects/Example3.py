class Person:
    def __init__(self, name, age=22):
        self.name = name
        self.age = age


if __name__ == '__main__':
    person = Person('John')
    print(f"I'm {person.name}. I'm {person.age} years old.")
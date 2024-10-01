print("To generate a sequence of number from 0 , 1, 2 ,.....n")

for i in range(10):
    print(i,end=', ')

print("")

print("Specifying the starting and ending value for the sequence")

for i in range(2,8):
    print(i,end=', ')

print("")

print("Specifying the increment for the sequence")

for i in range(10,20,2):
    print(i,end=', ')

print("")

# Introduction to the Python for else statement

'''

for item in iterables:
    # process item
else:
    # statement

'''

'''

Suppose that we have a list of people, where each person is a dictionary that consists of name and age like this:

people = [{'name': 'John', 'age': 25},
        {'name': 'Jane', 'age': 22},
        {'name': 'Peter', 'age': 30},
        {'name': 'Jenifer', 'age': 28}]

And we want to search for a person by name.

If the list contains the person, we want to display the information of that person.
Otherwise, we want to show a message saying that the name is not found.

'''

people = [{'name': 'John', 'age': 25},
        {'name': 'Jane', 'age': 22},
        {'name': 'Peter', 'age': 30},
        {'name': 'Jenifer', 'age': 28}]

name = input('Enter a name:')

for person in people:
    if person['name'] == name:
        print(person)
        break
else:
    print(f'{name} not found!')


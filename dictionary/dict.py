
'''
    *A Python dictionary is a collection of key-value pairs where each key is associated with a value.
    *A value in the key-value pair can be a number, a string, a list, a tuple, or even another dictionary.
    *In fact, we can use a value of any valid type in Python as the value in the key-value pair.
    *A key in the key-value pair must be immutable.
    *In other words, the key cannot be changed, for example, a number, a string, a tuple, etc.

'''

# Defining empty dictionary

empty_dict = {}

print(type(empty_dict))

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

print(person)

# Accessing value using []

print(person['favorite_colors'])

# Accessing value using get()

print(person.get('favorite_colors'))

# Adding new key-value pair

person['gender'] = 'Male'
print(person)

# Remove key - value pair using del

del person['gender']
print(person)

# print all keys

print(person.keys())

# print all values

print(person.values())

# print key-value pairs

print(person.items())

# Loop through dictionary

for key in person:
    print(person[key])

# Loop through dictionary using key and value

for key,value in person.items():
    print(key,value)

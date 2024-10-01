person = {'name': 'Jenn', 'age': 23}


# Method 1
sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(sentence)

# Method 2

sentence = 'My name is {} and I am {} years old.'.format(person['name'],person['age'])
print(sentence)

# Method 3

sentence = 'My name is {0} and I am {1} years old.'.format(person['name'],person['age'])
print(sentence)

# Method 3

sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence)

# If we need to access the attribute of Object of class , we will use . instead of []

class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jack', '33')


sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)


# If we provide keyword argument in format method

sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')
print(sentence)

# Using **kwargs way

sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence)

# Formatting

sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)

print(sentence)

# Formatting of Data and Time

import datetime

my_date = datetime.datetime(2024, 9, 11, 12, 30, 45)


# To print in the format : March 01, 2016

sentence = '{:%B %d, %Y}'.format(my_date)

print(sentence)

# To print in the format -> March 01, 2016 fell on a Tuesday and was the 061 day of the year.

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)

print(sentence)

















